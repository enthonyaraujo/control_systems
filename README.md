# Sistemas de Controle

Anotações das disciplinas de **Sistemas de Controle I e II** do curso de Engenharia de Computação da Universidade Federal Rural do Semi-Árido (UFERSA).

O material reúne conceitos teóricos, demonstrações matemáticas, exemplos resolvidos, circuitos e diagramas de controle, transcritos das anotações de aula para Markdown. As equações são escritas em LaTeX e as figuras são reconstruídas em TikZ, sem utilizar recortes dos cadernos originais.

## Conteúdo

### Sistemas de Controle I

| Unidade | Tópicos |
| :--- | :--- |
| [Unidade 1](controle-I/Unidade-1.md) | Introdução aos sistemas de controle, transformada de Laplace e modelagem de sistemas elétricos, mecânicos e eletromecânicos. |
| [Unidade 2](controle-I/Unidade-2.md) | Linearização, resposta no domínio do tempo, diagramas de blocos, fórmula de Mason e critério de Routh-Hurwitz. |
| [Unidade 3](controle-I/Unidade-3.md) | Erros em regime permanente, distúrbios, controle digital, transformada Z e critério de Jury. |

### Sistemas de Controle II

| Unidade | Tópicos |
| :--- | :--- |
| [Unidade 1](controle-II/Unidade-1.md) | Lugar geométrico das raízes (LGR), condições de módulo e fase, assíntotas e análise de estabilidade. |
| [Unidade 2](controle-II/Unidade-2.md) | Projeto de controladores por avanço e atraso de fase, controladores P, PI, PD e PID. |
| [Unidade 3](controle-II/Unidade-3.md) | Representação por variáveis de estado, controlabilidade, alocação de polos, observabilidade e observadores de estado. |

## Como acessar as anotações

- **GitHub:** acesse as unidades pelos links acima. Os 133 gráficos e diagramas já estão disponíveis em formato vetorial SVG.
- **Obsidian:** abra ou importe a pasta [`obsidian/`](obsidian/). Instale e ative o plugin comunitário [TikZJax](https://github.com/artisticat1/obsidian-tikzjax) para renderizar os diagramas diretamente no Markdown.
- **Ferramentas de IA:** utilize os arquivos de `obsidian/`, que preservam o texto, as equações e o código-fonte dos diagramas.

## Geração dos diagramas

Os arquivos em `obsidian/` são a fonte principal das anotações. O script [`render_tikz.py`](scripts/render_tikz.py) compila os blocos TikZ em SVG e gera as versões de leitura para o GitHub.

**Requisitos:** Python 3.10 ou superior, TeX Live (LaTeX, lmodern, TikZ, PGFPlots e standalone) e Poppler (`pdftocairo`).

Para gerar todas as unidades localmente:

```bash
python3 scripts/render_tikz.py --jobs 4
```

Para gerar somente uma disciplina:

```bash
python3 scripts/render_tikz.py --course controle-I --jobs 4
python3 scripts/render_tikz.py --course controle-II --jobs 4
```

A geração também é automatizada pelo [GitHub Actions](.github/workflows/render-tikz.yml) quando as fontes ou o script são alterados na branch padrão. O workflow pode ser executado manualmente na aba **Actions**. O commit automático dos arquivos gerados depende das permissões de escrita do repositório.

> Para atualizar o conteúdo, edite os arquivos da pasta `obsidian/`, não as versões geradas.

## Tecnologias

[Markdown](https://www.markdownguide.org/) · [LaTeX](https://www.latex-project.org/) · [TikZ/PGFPlots](https://pgfplots.sourceforge.net/) · [SVG](https://www.w3.org/Graphics/SVG/) · [Python](https://www.python.org/) · [Obsidian](https://obsidian.md/) · GitHub Actions

## Sobre o material

Repositório destinado ao estudo e à consulta dos conteúdos abordados em sala de aula. O material não substitui a bibliografia das disciplinas.
