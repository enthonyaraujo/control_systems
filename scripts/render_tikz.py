#!/usr/bin/env python3
"""Gera as versões GitHub a partir de obsidian/controle-*/Unidade-*.md (Python 3.10+)."""
from __future__ import annotations
import argparse
from html import escape
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BLOCK = re.compile(r'^```tikz[ \t]*\n(.*?)^```[ \t]*$', re.M | re.S)
DISPLAY = re.compile(r'^\$\$([^\n]+?)\$\$[ \t]*$', re.M)
NS = '{http://www.w3.org/2000/svg}'
PREAMBLE = r'''\documentclass[border=5pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,shapes.geometric}
'''


def parse(source):
    original = source.read_text(encoding='utf-8')
    figures = []
    def replace(match):
        number = len(figures) + 1
        headings = re.findall(r'^#{1,6}\s+(.+)$', original[:match.start()], re.M)
        heading = re.sub(r'[\[\]`*]', '', headings[-1] if headings else source.stem)
        path = f'assets/{source.stem.lower()}/figura-{number:02d}.svg'
        figures.append((f'{source.parent.name}/{path}', match.group(1)))
        alt = escape(f'Figura {number} — {heading}', quote=True)
        return f'<p align="center">\n  <img src="{path}" alt="{alt}" />\n</p>'
    text = BLOCK.sub(replace, original)
    if re.search(r'^```tikz\b', text, re.M):
        raise ValueError(f'Bloco TikZ sem fechamento: {source.name}')
    # Delimitadores em linhas separadas para a renderização matemática do GitHub.
    text = DISPLAY.sub(lambda m: '$$\n' + m.group(1) + '\n$$', text)
    return text, figures


def run(command, cwd):
    result = subprocess.run(command, cwd=cwd, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True, timeout=120)
    if result.returncode:
        raise RuntimeError(f'{command[0]} falhou:\n{result.stdout[-6000:]}')


def render(job, staging):
    path, body = job
    try:
        with tempfile.TemporaryDirectory(prefix='tikz-') as tmp:
            work = Path(tmp)
            (work / 'figure.tex').write_text(PREAMBLE + body, encoding='utf-8')
            run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                 '-file-line-error', '-no-shell-escape', 'figure.tex'], work)
            run(['pdftocairo', '-svg', 'figure.pdf', 'figure.svg'], work)
            svg = (work / 'figure.svg').read_text(encoding='utf-8')
            # Fundo claro para manter o contraste também no modo escuro.
            svg, count = re.subn(r'(<svg\b[^>]*>)', r'\1\n<rect width="100%" height="100%" fill="#ffffff"/>', svg, count=1)
            tree = ET.fromstring(svg)
            if count != 1 or tree.tag != NS+'svg' or not tree.get('viewBox'):
                raise ValueError('SVG inválido')
            if tree.findall('.//'+NS+'image'):
                raise ValueError('Imagem raster incorporada')
            for node in tree.iter():
                for key, value in node.attrib.items():
                    if key.endswith('href') and not value.startswith('#'):
                        raise ValueError(f'Referência externa: {value}')
            dest = staging / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(svg, encoding='utf-8')
        print(f'OK {path}', flush=True)
    except Exception as exc:
        raise RuntimeError(f'Erro em {path}: {exc}') from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--course', choices=['controle-I', 'controle-II'], help='Gerar apenas uma disciplina')
    parser.add_argument('--jobs', type=int, default=4, help='Compilações paralelas')
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error('--jobs precisa ser positivo')
    for cmd in ('pdflatex', 'pdftocairo'):
        if not shutil.which(cmd):
            parser.error(f'Dependência ausente: {cmd}')
    courses = [args.course] if args.course else ['controle-I', 'controle-II']
    sources = sorted(p for c in courses for p in (ROOT/'obsidian'/c).glob('Unidade-*.md'))
    if not sources:
        parser.error('Nenhuma unidade em obsidian/')
    documents, figures = {}, []
    for source in sources:
        text, jobs = parse(source)
        documents[Path(source.parent.name)/source.name] = text
        figures.extend(jobs)
        print(f'{source.parent.name}/{source.name}: {len(jobs)} diagramas', flush=True)
    # Publica somente depois que todos os diagramas forem compilados.
    with tempfile.TemporaryDirectory(prefix='controle-render-') as tmp:
        staging = Path(tmp)
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            list(pool.map(lambda job: render(job, staging), figures))
        expected = {path for path, _ in figures}
        for path, _ in figures:
            dest = ROOT / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(staging/path, dest)
        for name, text in documents.items():
            (ROOT/name).parent.mkdir(parents=True, exist_ok=True)
            (ROOT/name).write_text(text, encoding='utf-8')
        for old in (p for c in courses for p in (ROOT/c/'assets').glob('unidade-*/figura-*.svg')):
            if re.fullmatch(r'figura-\d+\.svg', old.name) and old.relative_to(ROOT).as_posix() not in expected:
                old.unlink()
        for name, text in documents.items():
            for path in re.findall(r'<img src="(assets/[^"\n]+)"', text):
                if not (ROOT/name.parent/path).is_file():
                    raise FileNotFoundError(path)
    print(f'Concluído: {len(documents)} unidades e {len(figures)} SVGs.', flush=True)


if __name__ == '__main__':
    main()
