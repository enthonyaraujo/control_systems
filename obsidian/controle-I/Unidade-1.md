# Unidade 1 — Sistemas de Controle I

## 1. Introdução aos sistemas de controle

Principais partes do sistema de controle:

1. Planta: qualquer objeto físico a ser controlado.
2. Controle: o cérebro do sistema.
3. Atuador: executa a ação física da planta.
4. Sensor: mede a saída do sistema e envia a informação de volta.
5. Distúrbio: um sinal que afeta de modo adverso.

**Sistemas de malha aberta:** a saída não tem nenhum efeito sobre a ação de controle.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (b0) at (1.4,0) {$\mathrm{Controle}$};
\draw[->] (0,0) -- node[above] {$$} (b0.west);
\node[b] (b1) at (3.4,0) {$\mathrm{Atuador}$};
\draw[->] (b0.east) -- (b1.west);
\node[b] (b2) at (5.4,0) {$\mathrm{Planta}$};
\draw[->] (b1.east) -- (b2.west);
\draw[->] (b2.east) -- node[above] {$$} (6.9,0);

\end{tikzpicture}
\end{document}
```

**Sistemas de malha fechada:** um sinal é realimentado da saída para a entrada e usado para modificar a entrada, de tal maneira que a saída seja mantida constante.

Erro = Entrada − Saída.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (s0) at (1,0) {$+$};
\draw[->] (0,0) -- node[above] {$\mathrm{Entrada}$} (s0.west);
\node[] at (0.73,-0.43) {$-$};
\node[b] (b0) at (2.6,0) {$\mathrm{Controle}$};
\draw[->] (s0.east) -- node[above] {$\mathrm{Erro}$} (b0.west);
\node[b] (b1) at (4.75,0) {$\mathrm{Atuador}$};
\draw[->] (b0.east) -- (b1.west);
\node[b] (b2) at (6.9,0) {$\mathrm{Planta}$};
\draw[->] (b1.east) -- (b2.west);
\draw[->] (b2.east) -- node[above] {$\mathrm{Saida}$} (8.8,0);
\fill (8.100000000000001,0) circle (1.4pt);
\node[b] (h) at (4.550000000000001,-1.25) {$\mathrm{Sensor}$};
\draw[->] (8.100000000000001,0) |- (h.east);\draw[->] (h.west) -| (s0.south);

\end{tikzpicture}
\end{document}
```

## 2. Modelagem no domínio da frequência

### Transformada de Laplace

$$
\boxed{\mathcal L\{f(t)\}=F(s)=\int_0^\infty f(t)e^{-st}\,dt}
$$

| $f(t)$ | $F(s)$ |
|---|---|
| $\delta(t)$ | $1$ |
| $u(t)$ | $1/s$ |
| $tu(t)$ | $1/s^2$ |
| $t^nu(t)$ | $n!/s^{n+1}$ |
| $e^{-at}u(t)$ | $1/(s+a)$ |
| $\sin(\omega t)u(t)$ | $\omega/(s^2+\omega^2)$ |
| $\cos(\omega t)u(t)$ | $s/(s^2+\omega^2)$ |

**Teoremas:**

| Teorema | Nome |
|---|---|
| $\mathcal L\{f(t)\}=\int_0^\infty f(t)e^{-st}dt$ | Definição |
| $\mathcal L\{Kf(t)\}=KF(s)$ | Linearidade |
| $\mathcal L\{f_1(t)+f_2(t)\}=F_1(s)+F_2(s)$ | Linearidade |
| $\mathcal L\{e^{-at}f(t)\}=F(s+a)$ | Deslocamento em frequência |
| $\mathcal L\{f(t-T)\}=e^{-sT}F(s)$ | Deslocamento no tempo |
| $\mathcal L\{f(at)\}=\frac1a F(s/a)$ | Escala |
| $\mathcal L\{df/dt\}=sF(s)-f(0^-)$ | Derivação |
| $\mathcal L\{d^2f/dt^2\}=s^2F(s)-sf(0^-)-f'(0^-)$ | Derivação |
| $\mathcal L\{d^nf/dt^n\}=s^nF(s)-\sum_{k=1}^n s^{n-k}f^{(k-1)}(0^-)$ | Derivação |
| $\mathcal L\{\int_0^t f(\tau)d\tau\}=F(s)/s$ | Integração |
| $f(\infty)=\lim_{s\to0}sF(s)$ | Valor final |
| $f(0^+)=\lim_{s\to\infty}sF(s)$ | Valor inicial |

### Transformada de Laplace inversa

$$
\mathcal L^{-1}\{F(s)\}=f(t)=\frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}F(s)e^{st}ds
$$

### Transformada de Laplace inversa por frações parciais

Seja:

$$
F(s)=\frac{s^3+2s^2+6s+7}{s^2+s+5}=\frac{N(s)}{D(s)}
$$

- Se a ordem de $N(s)$ é menor que a de $D(s)$, a operação pode ser realizada.
- Se a ordem de $N(s)$ é maior que a de $D(s)$, realiza-se uma divisão sucessiva (polinômios) até a ordem ficar inferior.

Pela divisão: quociente + resto/divisor.

$$
\begin{aligned}
s^3+2s^2+6s+7-(s^3+s^2+5s)&=s^2+s+7\\
s^2+s+7-(s^2+s+5)&=2\\
F(s)&=s+1+\frac{2}{s^2+s+5}
\end{aligned}
$$

O grau de $N(s)$ agora é menor, logo aplica-se o método de frações parciais.

Existem três casos:

1. Raízes do denominador reais e distintas.
2. Raízes do denominador reais e repetidas.
3. Raízes do denominador complexas e distintas.

| Caso | $F(s)$ | $f(t)$ |
|---|---|---|
| 1 | $\frac{K}{s+a}$ | $Ke^{-at}$ |
| 2 | $\frac{K}{(s+a)^2}$ | $Kte^{-at}$ |
| 3 | $\frac{K}{s+\alpha-j\beta}+\frac{K^*}{s+\alpha+j\beta}$ | $2\lvert K\rvert e^{-\alpha t}\cos(\beta t+\theta)$ |

Sendo $K=a+jb$, $|K|=\sqrt{a^2+b^2}$ e $\theta=\arctan(-b/a)$ (sinal anotado no caderno; depende da convenção usada para $K$).

## 3. Modelagem de circuitos elétricos

| Componente | Tensão–corrente | Corrente–tensão | Tensão–carga | Impedância $Z(s)$ | Admitância $Y(s)$ |
|---|---|---|---|---|---|
| Capacitor | $v=\frac1C\int i\,dt$ | $i=C\frac{dv}{dt}$ | $v=q/C$ | $1/(Cs)$ | $Cs$ |
| Resistor | $v=Ri$ | $i=v/R$ | $v=R\frac{dq}{dt}$ | $R$ | $1/R$ |
| Indutor | $v=L\frac{di}{dt}$ | $i=\frac1L\int v\,dt$ | $v=L\frac{d^2q}{dt^2}$ | $Ls$ | $1/(Ls)$ |

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw (0.000,0.000) -- (0.200,0.000) -- (0.338,0.120) -- (0.475,-0.120) -- (0.613,0.120) -- (0.750,-0.120) -- (0.887,0.120) -- (1.025,-0.120) -- (1.163,0.120) -- (1.300,0.000) -- (1.500,0.000);
\node[] at (0.75,-0.55) {$R$};
\draw (2.4,0) .. controls (2.4299999999999997,0.32) and (2.745,0.32) .. (2.775,0) .. controls (2.8049999999999997,0.32) and (3.12,0.32) .. (3.15,0) .. controls (3.1799999999999997,0.32) and (3.495,0.32) .. (3.525,0) .. controls (3.5549999999999997,0.32) and (3.87,0.32) .. (3.9,0);
\node[] at (3.15,-0.55) {$L$};
\draw (4.72,0.09) -- (5.28,0.09) (4.72,-0.09) -- (5.28,-0.09);
\draw (5,.09) -- (5,.45) (5,-.09) -- (5,-.45);\node[] at (5,-0.7) {$C$};

\end{tikzpicture}
\end{document}
```

### Circuito simples

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw (0,1) circle (.32);\node at (0,1.13) {$+$};\node at (0,0.87) {$-$};
\draw (0,.68) -- (0,0) -- (6,0) -- (6,.91) (6,1.09) -- (6,2) -- (4,2) (0,1.32) -- (0,2) -- (1,2);
\draw (5.72,1.09) -- (6.28,1.09) (5.72,0.91) -- (6.28,0.91);
\node[] at (-0.7,1) {$v(t)$};
\node[] at (6.65,1) {$C$};
\draw (1,2) .. controls (1.03,2.32) and (1.345,2.32) .. (1.375,2) .. controls (1.405,2.32) and (1.72,2.32) .. (1.75,2) .. controls (1.78,2.32) and (2.095,2.32) .. (2.125,2) .. controls (2.155,2.32) and (2.47,2.32) .. (2.5,2);
\draw (3.400,2.000) -- (3.600,2.000) -- (3.738,2.120) -- (3.875,1.880) -- (4.013,2.120) -- (4.150,1.880) -- (4.287,2.120) -- (4.425,1.880) -- (4.562,2.120) -- (4.700,2.000) -- (4.900,2.000);
\draw (2.5,2) -- (3.4,2) (4.9,2) -- (6,2);
\node[] at (1.75,2.4) {$L$};
\node[] at (4.15,2.3) {$R$};
\node[] at (2.8,0.9) {$i(t)$};
\node[] at (5.4,1) {$V_C$};
\node[] at (5.7,1.55) {$+$};
\node[] at (5.7,0.4) {$-$};
\node[] at (-0.75,-1.65) {$\equiv$};
\begin{scope}[shift={(0,-3.3)}]
\draw (0,1) circle (.32);\node at (0,1.13) {$+$};\node at (0,0.87) {$-$};
\draw (0,.68) -- (0,0) -- (6,0) -- (6,.91) (6,1.09) -- (6,2) -- (4,2) (0,1.32) -- (0,2) -- (1,2);
\draw (5.72,1.09) -- (6.28,1.09) (5.72,0.91) -- (6.28,0.91);
\node[] at (-0.7,1) {$V(s)$};
\node[] at (6.65,1) {$1/(sC)$};
\draw (1,2) .. controls (1.03,2.32) and (1.345,2.32) .. (1.375,2) .. controls (1.405,2.32) and (1.72,2.32) .. (1.75,2) .. controls (1.78,2.32) and (2.095,2.32) .. (2.125,2) .. controls (2.155,2.32) and (2.47,2.32) .. (2.5,2);
\draw (3.400,2.000) -- (3.600,2.000) -- (3.738,2.120) -- (3.875,1.880) -- (4.013,2.120) -- (4.150,1.880) -- (4.287,2.120) -- (4.425,1.880) -- (4.562,2.120) -- (4.700,2.000) -- (4.900,2.000);
\draw (2.5,2) -- (3.4,2) (4.9,2) -- (6,2);
\node[] at (1.75,2.4) {$Ls$};
\node[] at (4.15,2.3) {$R$};
\node[] at (2.8,0.9) {$I(s)$};
\node[] at (5.4,1) {$V_C$};
\node[] at (5.7,1.55) {$+$};
\node[] at (5.7,0.4) {$-$};

\end{scope}

\end{tikzpicture}
\end{document}
```

Aplica $\sum V(s)=0$ no domínio de Laplace:

$$
\begin{aligned}
-V(s)+LsI(s)+RI(s)+\frac{1}{sC}I(s)&=0\\
V(s)&=\left(Ls+R+\frac1{sC}\right)I(s)\\
\frac{I(s)}{V(s)}&=\frac1{Ls+R+\frac1{sC}}
\end{aligned}
\tag{1}
$$

Note que $i_C(t)=C\frac{dv_C(t)}{dt}$. Aplicando Laplace de ambos os lados, utilizamos também o teorema da derivação.

$$
\mathcal L\left\{\frac{df}{dt}\right\}=sF(s)-f(0^-)
$$

$C$ é constante; pelo teorema da linearidade podemos retirá-la de dentro da Laplace.

$$
\begin{aligned}
\mathcal L\{i_C(t)\}&=\mathcal L\left\{C\frac{dv_C(t)}{dt}\right\}\\
I(s)&=C\mathcal L\left\{\frac{dv_C(t)}{dt}\right\}\\
I(s)&=CsV_C(s)
\end{aligned}
\tag{2}
$$

Substituindo (2) em (1), com condições iniciais nulas:

$$
\begin{aligned}
\frac{sCV_C(s)}{V(s)}&=\frac1{Ls+R+\frac1{sC}}\\
\frac{V_C(s)}{V(s)}&=\frac1{s^2LC+sRC+1}\\
\boxed{\frac{V_C(s)}{V(s)}=\frac{1/(LC)}{s^2+\frac RL s+\frac1{LC}}}
\end{aligned}
$$

### Circuito complexo por análise de malha/nodal

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw (0,1) circle (.32);\node at (0,1.13) {$+$};\node at (0,0.87) {$-$};
\draw (0,.68) -- (0,0) -- (6,0) -- (6,.91) (6,1.09) -- (6,2) -- (4,2) (0,1.32) -- (0,2) -- (1,2);
\draw (5.72,1.09) -- (6.28,1.09) (5.72,0.91) -- (6.28,0.91);
\node[] at (-0.7,1) {$v(t)$};
\node[] at (6.65,1) {$C$};
\draw (1.000,2.000) -- (1.200,2.000) -- (1.337,2.120) -- (1.475,1.880) -- (1.613,2.120) -- (1.750,1.880) -- (1.887,2.120) -- (2.025,1.880) -- (2.163,2.120) -- (2.300,2.000) -- (2.500,2.000);
\draw (4.000,2.000) -- (4.200,2.000) -- (4.338,2.120) -- (4.475,1.880) -- (4.612,2.120) -- (4.750,1.880) -- (4.888,2.120) -- (5.025,1.880) -- (5.163,2.120) -- (5.300,2.000) -- (5.500,2.000);
\draw (2.5,2) -- (4,2) (5.5,2) -- (6,2) (3,2) -- (3,1.75) (3,.25) -- (3,0);
\begin{scope}[shift={(3,.25)},rotate=90]\draw (0,0) .. controls (0.03,0.32) and (0.345,0.32) .. (0.375,0) .. controls (0.405,0.32) and (0.72,0.32) .. (0.75,0) .. controls (0.78,0.32) and (1.095,0.32) .. (1.125,0) .. controls (1.155,0.32) and (1.47,0.32) .. (1.5,0);
\end{scope}
\node[] at (1.75,2.3) {$R_1$};
\node[] at (4.75,2.3) {$R_2$};
\node[] at (3.55,1) {$L$};
\node[] at (1.5,0.85) {$i_1(t)$};
\node[] at (4.6,0.85) {$i_2(t)$};
\node[] at (-0.75,-1.65) {$\equiv$};
\begin{scope}[shift={(0,-3.3)}]
\draw (0,1) circle (.32);\node at (0,1.13) {$+$};\node at (0,0.87) {$-$};
\draw (0,.68) -- (0,0) -- (6,0) -- (6,.91) (6,1.09) -- (6,2) -- (4,2) (0,1.32) -- (0,2) -- (1,2);
\draw (5.72,1.09) -- (6.28,1.09) (5.72,0.91) -- (6.28,0.91);
\node[] at (-0.7,1) {$V(s)$};
\node[] at (6.65,1) {$1/(sC)$};
\draw (1.000,2.000) -- (1.200,2.000) -- (1.337,2.120) -- (1.475,1.880) -- (1.613,2.120) -- (1.750,1.880) -- (1.887,2.120) -- (2.025,1.880) -- (2.163,2.120) -- (2.300,2.000) -- (2.500,2.000);
\draw (4.000,2.000) -- (4.200,2.000) -- (4.338,2.120) -- (4.475,1.880) -- (4.612,2.120) -- (4.750,1.880) -- (4.888,2.120) -- (5.025,1.880) -- (5.163,2.120) -- (5.300,2.000) -- (5.500,2.000);
\draw (2.5,2) -- (4,2) (5.5,2) -- (6,2) (3,2) -- (3,1.75) (3,.25) -- (3,0);
\begin{scope}[shift={(3,.25)},rotate=90]\draw (0,0) .. controls (0.03,0.32) and (0.345,0.32) .. (0.375,0) .. controls (0.405,0.32) and (0.72,0.32) .. (0.75,0) .. controls (0.78,0.32) and (1.095,0.32) .. (1.125,0) .. controls (1.155,0.32) and (1.47,0.32) .. (1.5,0);
\end{scope}
\node[] at (1.75,2.3) {$R_1$};
\node[] at (4.75,2.3) {$R_2$};
\node[] at (3.55,1) {$sL$};
\node[] at (1.5,0.85) {$I_1(s)$};
\node[] at (4.6,0.85) {$I_2(s)$};

\end{scope}

\end{tikzpicture}
\end{document}
```

Análise de malha: determinar $I_2(s)/V(s)$.

**Malha 1:**

$$
\begin{aligned}
-V+R_1I_1+sL(I_1-I_2)&=0\\
-V+R_1I_1+sLI_1-sLI_2&=0\\
-V+(R_1+sL)I_1-sLI_2&=0
\end{aligned}
\tag{1}
$$

**Malha 2:**

$$
\begin{aligned}
sL(I_2-I_1)+R_2I_2+\frac1{sC}I_2&=0\\
-sLI_1+sLI_2+R_2I_2+\frac1{sC}I_2&=0\\
I_1&=\frac{I_2(sL+R_2+1/(sC))}{sL}\\
I_1&=I_2\left(\frac{s^2LC+sR_2C+1}{s^2LC}\right)
\end{aligned}
\tag{2}
$$

Substituindo (2) em (1):

$$
-V+(R_1+sL)I_2\left(\frac{s^2LC+sR_2C+1}{s^2LC}\right)-sLI_2=0
$$

$$
s^2LCV=I_2(s^2R_1LC+sR_1R_2C+R_1+s^3L^2C+s^2R_2LC+sL-s^3L^2C)
$$

$$
\boxed{\frac{I_2}{V}=\frac{s^2LC}{(R_1+R_2)s^2LC+(R_1R_2C+L)s+R_1}}
$$

## 4. Modelagem de sistemas mecânicos translacionais

| Componente | Força–velocidade | Força–deslocamento | Impedância $Z(s)=F(s)/X(s)$ |
|---|---|---|---|
| Mola | $f=K\int v\,dt$ | $f=Kx$ | $K$ |
| Amortecedor viscoso | $f=f_vv$ | $f=f_v\frac{dx}{dt}$ | $f_vs$ |
| Massa | $f=M\frac{dv}{dt}$ | $f=M\frac{d^2x}{dt^2}$ | $Ms^2$ |

### Sistema mecânico simples

Determine $X(s)/F(s)$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw[very thick] (0,-1) -- (0,1);
\draw (-0.18,-0.9500000000000001) -- (0,-0.8);\draw (-0.18,-0.7200000000000001) -- (0,-0.5700000000000001);\draw (-0.18,-0.49) -- (0,-0.34);\draw (-0.18,-0.26) -- (0,-0.10999999999999999);\draw (-0.18,-0.03) -- (0,0.12);\draw (-0.18,0.2000000000000001) -- (0,0.3500000000000001);\draw (-0.18,0.43000000000000005) -- (0,0.5800000000000001);\draw (-0.18,0.66) -- (0,0.81);
\draw (0.000,0.420) -- (0.200,0.420) -- (0.450,0.540) -- (0.700,0.300) -- (0.950,0.540) -- (1.200,0.300) -- (1.450,0.540) -- (1.700,0.300) -- (1.950,0.540) -- (2.200,0.420) -- (2.400,0.420);
\node[] at (1.2,0.77) {$K$};
\draw (0,-0.42) -- (0.96,-0.42) (0.96,-0.6) -- (0.96,-0.24) (1.56,-0.6699999999999999) -- (0.86,-0.6699999999999999) (1.56,-0.16999999999999998) -- (0.86,-0.16999999999999998) (1.56,-0.6699999999999999) -- (1.56,-0.16999999999999998) (1.56,-0.42) -- (2.4,-0.42);
\node[] at (1.2,-0.8200000000000001) {$f_v$};
\node[draw,minimum width=1.15cm,minimum height=1.6cm] (m3) at (3,0) {$M$};
\draw[->] (3.6,0) -- node[above] {$f(t)$} (4.8,0);
\draw[->] (3,.95) -- node[above] {$x(t)$} (4.25,.95);

\end{tikzpicture}
\end{document}
```

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[draw,minimum width=1.1cm,minimum height=2.0cm] (m) at (0,0) {$M$};
\draw[->] (-.56,0.78) -- node[above] {$KX$} (-2.1,0.78);
\draw[->] (-.56,0.0) -- node[above] {$f_vsX$} (-2.1,0.0);
\draw[->] (-.56,-0.78) -- node[above] {$Ms^2X$} (-2.1,-0.78);
\draw[->] (.56,0.68) -- node[above] {$F$} (2.3,0.68);

\end{tikzpicture}
\end{document}
```

$$
\sum F=0\Rightarrow -(Ms^2+f_vs+K)X(s)+F(s)=0
$$

$$
\boxed{\frac{X(s)}{F(s)}=\frac1{Ms^2+f_vs+K}}
$$

### Sistema mecânico complexo

Determine $X_2(s)/F(s)$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw[very thick] (0,-1) -- (0,1);
\draw (-0.18,-0.9500000000000001) -- (0,-0.8);\draw (-0.18,-0.7200000000000001) -- (0,-0.5700000000000001);\draw (-0.18,-0.49) -- (0,-0.34);\draw (-0.18,-0.26) -- (0,-0.10999999999999999);\draw (-0.18,-0.03) -- (0,0.12);\draw (-0.18,0.2000000000000001) -- (0,0.3500000000000001);\draw (-0.18,0.43000000000000005) -- (0,0.5800000000000001);\draw (-0.18,0.66) -- (0,0.81);
\draw (0.000,0.000) -- (0.200,0.000) -- (0.375,0.120) -- (0.550,-0.120) -- (0.725,0.120) -- (0.900,-0.120) -- (1.075,0.120) -- (1.250,-0.120) -- (1.425,0.120) -- (1.600,0.000) -- (1.800,0.000);
\node[] at (0.9,0.35) {$K_1$};
\node[draw,minimum width=1.15cm,minimum height=1.6cm] (m2p4) at (2.4,0) {$M_1$};
\draw (3.000,0.400) -- (3.200,0.400) -- (3.400,0.520) -- (3.600,0.280) -- (3.800,0.520) -- (4.000,0.280) -- (4.200,0.520) -- (4.400,0.280) -- (4.600,0.520) -- (4.800,0.400) -- (5.000,0.400);
\node[] at (4.0,0.75) {$K_2$};
\draw (3,-0.4) -- (3.8,-0.4) (3.8,-0.5800000000000001) -- (3.8,-0.22000000000000003) (4.3,-0.65) -- (3.6999999999999997,-0.65) (4.3,-0.15000000000000002) -- (3.6999999999999997,-0.15000000000000002) (4.3,-0.65) -- (4.3,-0.15000000000000002) (4.3,-0.4) -- (5,-0.4);
\node[] at (4.0,-0.8) {$f_{v3}$};
\node[draw,minimum width=1.15cm,minimum height=1.6cm] (m5p6) at (5.6,0) {$M_2$};
\draw (6.200,0.000) -- (6.400,0.000) -- (6.575,0.120) -- (6.750,-0.120) -- (6.925,0.120) -- (7.100,-0.120) -- (7.275,0.120) -- (7.450,-0.120) -- (7.625,0.120) -- (7.800,0.000) -- (8.000,0.000);
\node[] at (7.1000000000000005,0.35) {$K_3$};
\draw[very thick] (8,-1) -- (8,1);
\draw (7.82,-0.9500000000000001) -- (8,-0.8);\draw (7.82,-0.7200000000000001) -- (8,-0.5700000000000001);\draw (7.82,-0.49) -- (8,-0.34);\draw (7.82,-0.26) -- (8,-0.10999999999999999);\draw (7.82,-0.03) -- (8,0.12);\draw (7.82,0.2000000000000001) -- (8,0.3500000000000001);\draw (7.82,0.43000000000000005) -- (8,0.5800000000000001);\draw (7.82,0.66) -- (8,0.81);
\draw[->] (1.15,1.0) -- node[above] {$F(t)$} (2.35,1.0);
\draw[->] (2.4,1.0) -- node[above] {$x_1(t)$} (3.4,1.0);
\draw[->] (5.6,1.0) -- node[above] {$x_2(t)$} (6.6,1.0);
\draw (-.1,-.85) -- (8,-.85);\node[] at (2.4,-1.15) {$f_{v1}$};
\node[] at (5.6,-1.15) {$f_{v2}$};

\end{tikzpicture}
\end{document}
```

Forças em $M_1$ (deslocamentos $X_1$ e $X_2$):

```tikz
\begin{document}
\begin{tikzpicture}[yscale=1.45,>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[draw,minimum width=1.1cm,minimum height=2.8cm] (m) at (0,0) {$M_1$};
\draw[->] (-.56,0.78) -- node[above] {$K_1X_1$} (-2.1,0.78);
\draw[->] (-.56,0.39) -- node[above] {$K_2X_1$} (-2.1,0.39);
\draw[->] (-.56,0.0) -- node[above] {$f_{v1}sX_1$} (-2.1,0.0);
\draw[->] (-.56,-0.3899999999999999) -- node[above] {$f_{v3}sX_1$} (-2.1,-0.3899999999999999);
\draw[->] (-.56,-0.78) -- node[above] {$M_1s^2X_1$} (-2.1,-0.78);
\draw[->] (.56,0.68) -- node[above] {$F$} (2.3,0.68);
\draw[->] (.56,0.0) -- node[above] {$K_2X_2$} (2.3,0.0);
\draw[->] (.56,-0.68) -- node[above] {$f_{v3}sX_2$} (2.3,-0.68);

\end{tikzpicture}
\end{document}
```

$$
-(K_1+K_2+f_{v1}s+f_{v3}s+M_1s^2)X_1+(K_2+f_{v3}s)X_2+F=0
$$

$$
(M_1s^2+(f_{v1}+f_{v3})s+K_1+K_2)X_1-(f_{v3}s+K_2)X_2=F(s)\tag{1}
$$

Forças em $M_2$:

```tikz
\begin{document}
\begin{tikzpicture}[yscale=1.45,>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[draw,minimum width=1.1cm,minimum height=2.8cm] (m) at (0,0) {$M_2$};
\draw[->] (-.56,0.78) -- node[above] {$K_2X_2$} (-2.1,0.78);
\draw[->] (-.56,0.39) -- node[above] {$K_3X_2$} (-2.1,0.39);
\draw[->] (-.56,0.0) -- node[above] {$f_{v2}sX_2$} (-2.1,0.0);
\draw[->] (-.56,-0.3899999999999999) -- node[above] {$f_{v3}sX_2$} (-2.1,-0.3899999999999999);
\draw[->] (-.56,-0.78) -- node[above] {$M_2s^2X_2$} (-2.1,-0.78);
\draw[->] (.56,0.68) -- node[above] {$K_2X_1$} (2.3,0.68);
\draw[->] (.56,-0.68) -- node[above] {$f_{v3}sX_1$} (2.3,-0.68);

\end{tikzpicture}
\end{document}
```

$$
-(M_2s^2+(f_{v2}+f_{v3})s+K_2+K_3)X_2+(f_{v3}s+K_2)X_1=0
$$

$$
-(f_{v3}s+K_2)X_1+(M_2s^2+(f_{v2}+f_{v3})s+K_2+K_3)X_2=0
$$

> Obs.: o sinal do primeiro termo aparece positivo na última linha do caderno; foi mantido negativo aqui conforme a equação imediatamente anterior.

## 5. Modelagem de sistemas mecânicos rotacionais

| Componente | Torque–velocidade angular | Torque–deslocamento angular | Impedância $Z(s)=T(s)/\Theta(s)$ |
|---|---|---|---|
| Mola | $T=K\int\omega\,dt$ | $T=K\theta$ | $K$ |
| Amortecedor viscoso | $T=D\omega$ | $T=D\frac{d\theta}{dt}$ | $Ds$ |
| Inércia | $T=J\frac{d\omega}{dt}$ | $T=J\frac{d^2\theta}{dt^2}$ | $Js^2$ |

Determine as equações:

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw[very thick] (0,-1) -- (0,1);
\draw (-0.18,-0.9500000000000001) -- (0,-0.8);\draw (-0.18,-0.7200000000000001) -- (0,-0.5700000000000001);\draw (-0.18,-0.49) -- (0,-0.34);\draw (-0.18,-0.26) -- (0,-0.10999999999999999);\draw (-0.18,-0.03) -- (0,0.12);\draw (-0.18,0.2000000000000001) -- (0,0.3500000000000001);\draw (-0.18,0.43000000000000005) -- (0,0.5800000000000001);\draw (-0.18,0.66) -- (0,0.81);
\draw (0,0) -- (0.7200000000000001,0) (0.7200000000000001,-0.18) -- (0.7200000000000001,0.18) (1.1700000000000002,-0.25) -- (0.6200000000000001,-0.25) (1.1700000000000002,0.25) -- (0.6200000000000001,0.25) (1.1700000000000002,-0.25) -- (1.1700000000000002,0.25) (1.1700000000000002,0) -- (1.8,0);
\node[] at (0.9,-0.4) {$D_1$};
\node[b] (j1) at (2.4,0) {$J_1$};
\draw (3.000,0.000) -- (3.200,0.000) -- (3.400,0.120) -- (3.600,-0.120) -- (3.800,0.120) -- (4.000,-0.120) -- (4.200,0.120) -- (4.400,-0.120) -- (4.600,0.120) -- (4.800,0.000) -- (5.000,0.000);
\node[] at (4.0,0.35) {$K$};
\node[b] (j2) at (5.6,0) {$J_2$};
\draw (6.2,0) -- (6.92,0) (6.92,-0.18) -- (6.92,0.18) (7.37,-0.25) -- (6.82,-0.25) (7.37,0.25) -- (6.82,0.25) (7.37,-0.25) -- (7.37,0.25) (7.37,0) -- (8.0,0);
\node[] at (7.1000000000000005,-0.4) {$D_2$};
\draw[very thick] (8,-1) -- (8,1);
\draw (7.82,-0.9500000000000001) -- (8,-0.8);\draw (7.82,-0.7200000000000001) -- (8,-0.5700000000000001);\draw (7.82,-0.49) -- (8,-0.34);\draw (7.82,-0.26) -- (8,-0.10999999999999999);\draw (7.82,-0.03) -- (8,0.12);\draw (7.82,0.2000000000000001) -- (8,0.3500000000000001);\draw (7.82,0.43000000000000005) -- (8,0.5800000000000001);\draw (7.82,0.66) -- (8,0.81);
\node[] at (2.4,0.75) {$T(t),\theta_1(t)$};
\node[] at (5.6,0.75) {$\theta_2(t)$};

\end{tikzpicture}
\end{document}
```

Torques em $J_1$:

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[draw,minimum width=1.1cm,minimum height=2.0cm] (m) at (0,0) {$J_1$};
\draw[->] (-.56,0.78) -- node[above] {$J_1s^2\Theta_1$} (-2.1,0.78);
\draw[->] (-.56,0.0) -- node[above] {$D_1s\Theta_1$} (-2.1,0.0);
\draw[->] (-.56,-0.78) -- node[above] {$K\Theta_1$} (-2.1,-0.78);
\draw[->] (.56,0.68) -- node[above] {$T$} (2.3,0.68);
\draw[->] (.56,-0.68) -- node[above] {$K\Theta_2$} (2.3,-0.68);

\end{tikzpicture}
\end{document}
```

$$
\begin{aligned}
\sum T&=0\\
T-(J_1s^2+D_1s+K)\Theta_1+K\Theta_2&=0\\
(J_1s^2+D_1s+K)\Theta_1-K\Theta_2&=T
\end{aligned}
\tag{1}
$$

Torques em $J_2$:

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[draw,minimum width=1.1cm,minimum height=2.0cm] (m) at (0,0) {$J_2$};
\draw[->] (-.56,0.78) -- node[above] {$J_2s^2\Theta_2$} (-2.1,0.78);
\draw[->] (-.56,0.0) -- node[above] {$D_2s\Theta_2$} (-2.1,0.0);
\draw[->] (-.56,-0.78) -- node[above] {$K\Theta_2$} (-2.1,-0.78);
\draw[->] (.56,0.68) -- node[above] {$K\Theta_1$} (2.3,0.68);

\end{tikzpicture}
\end{document}
```

$$
-K\Theta_1+(J_2s^2+D_2s+K)\Theta_2=0\tag{2}
$$

## 6. Modelagem de sistemas mecânicos rotacionais com engrenagens

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw (0,0) circle (0.55);\fill (0,0) circle (1pt);
\draw (0.550,0.000) -- (0.630,0.000);
\draw (0.508,0.210) -- (0.582,0.241);
\draw (0.389,0.389) -- (0.445,0.445);
\draw (0.210,0.508) -- (0.241,0.582);
\draw (0.000,0.550) -- (0.000,0.630);
\draw (-0.210,0.508) -- (-0.241,0.582);
\draw (-0.389,0.389) -- (-0.445,0.445);
\draw (-0.508,0.210) -- (-0.582,0.241);
\draw (-0.550,0.000) -- (-0.630,0.000);
\draw (-0.508,-0.210) -- (-0.582,-0.241);
\draw (-0.389,-0.389) -- (-0.445,-0.445);
\draw (-0.210,-0.508) -- (-0.241,-0.582);
\draw (-0.000,-0.550) -- (-0.000,-0.630);
\draw (0.210,-0.508) -- (0.241,-0.582);
\draw (0.389,-0.389) -- (0.445,-0.445);
\draw (0.508,-0.210) -- (0.582,-0.241);
\node[] at (0,0) {$N_1$};
\draw (1.5,0) circle (0.95);\fill (1.5,0) circle (1pt);
\draw (2.450,0.000) -- (2.530,0.000);
\draw (2.378,0.364) -- (2.452,0.394);
\draw (2.172,0.672) -- (2.228,0.728);
\draw (1.864,0.878) -- (1.894,0.952);
\draw (1.500,0.950) -- (1.500,1.030);
\draw (1.136,0.878) -- (1.106,0.952);
\draw (0.828,0.672) -- (0.772,0.728);
\draw (0.622,0.364) -- (0.548,0.394);
\draw (0.550,0.000) -- (0.470,0.000);
\draw (0.622,-0.364) -- (0.548,-0.394);
\draw (0.828,-0.672) -- (0.772,-0.728);
\draw (1.136,-0.878) -- (1.106,-0.952);
\draw (1.500,-0.950) -- (1.500,-1.030);
\draw (1.864,-0.878) -- (1.894,-0.952);
\draw (2.172,-0.672) -- (2.228,-0.728);
\draw (2.378,-0.364) -- (2.452,-0.394);
\node[] at (1.5,0) {$N_2$};
\node[] at (0,1.25) {$T_1,\theta_1$};
\node[] at (1.5,1.25) {$T_2,\theta_2$};
\draw[->] (-.75,.1) arc (175:60:.75);\draw[->] (2.65,.1) arc (5:120:1.15);
\end{tikzpicture}
\end{document}
```

**Ângulo:** $l_1=l_2$.

$$
r_1\theta_1=r_2\theta_2\Rightarrow \frac{\theta_1}{\theta_2}=\frac{r_2}{r_1}=\frac{N_2}{N_1}
$$

**Torque:**

$$
T_1\theta_1=T_2\theta_2\Rightarrow\boxed{\frac{T_2}{T_1}=\frac{N_2}{N_1}}
$$

**Impedância:**

$$
\boxed{\frac{Z_D}{Z_O}=\left(\frac{N_D}{N_O}\right)^2}
$$

$D$: destino; $O$: origem.

### Trem de engrenagens

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw (0,0) circle (0.4);\fill (0,0) circle (1pt);
\draw (0.400,0.000) -- (0.480,0.000);
\draw (0.370,0.153) -- (0.443,0.184);
\draw (0.283,0.283) -- (0.339,0.339);
\draw (0.153,0.370) -- (0.184,0.443);
\draw (0.000,0.400) -- (0.000,0.480);
\draw (-0.153,0.370) -- (-0.184,0.443);
\draw (-0.283,0.283) -- (-0.339,0.339);
\draw (-0.370,0.153) -- (-0.443,0.184);
\draw (-0.400,0.000) -- (-0.480,0.000);
\draw (-0.370,-0.153) -- (-0.443,-0.184);
\draw (-0.283,-0.283) -- (-0.339,-0.339);
\draw (-0.153,-0.370) -- (-0.184,-0.443);
\draw (-0.000,-0.400) -- (-0.000,-0.480);
\draw (0.153,-0.370) -- (0.184,-0.443);
\draw (0.283,-0.283) -- (0.339,-0.339);
\draw (0.370,-0.153) -- (0.443,-0.184);
\node[] at (0,0) {$N_1$};
\draw (1,0) circle (0.6);\fill (1,0) circle (1pt);
\draw (1.600,0.000) -- (1.680,0.000);
\draw (1.554,0.230) -- (1.628,0.260);
\draw (1.424,0.424) -- (1.481,0.481);
\draw (1.230,0.554) -- (1.260,0.628);
\draw (1.000,0.600) -- (1.000,0.680);
\draw (0.770,0.554) -- (0.740,0.628);
\draw (0.576,0.424) -- (0.519,0.481);
\draw (0.446,0.230) -- (0.372,0.260);
\draw (0.400,0.000) -- (0.320,0.000);
\draw (0.446,-0.230) -- (0.372,-0.260);
\draw (0.576,-0.424) -- (0.519,-0.481);
\draw (0.770,-0.554) -- (0.740,-0.628);
\draw (1.000,-0.600) -- (1.000,-0.680);
\draw (1.230,-0.554) -- (1.260,-0.628);
\draw (1.424,-0.424) -- (1.481,-0.481);
\draw (1.554,-0.230) -- (1.628,-0.260);
\node[] at (1,0) {$N_2$};
\draw (1,-1.65) circle (0.4);\fill (1,-1.65) circle (1pt);
\draw (1.400,-1.650) -- (1.480,-1.650);
\draw (1.370,-1.497) -- (1.443,-1.466);
\draw (1.283,-1.367) -- (1.339,-1.311);
\draw (1.153,-1.280) -- (1.184,-1.207);
\draw (1.000,-1.250) -- (1.000,-1.170);
\draw (0.847,-1.280) -- (0.816,-1.207);
\draw (0.717,-1.367) -- (0.661,-1.311);
\draw (0.630,-1.497) -- (0.557,-1.466);
\draw (0.600,-1.650) -- (0.520,-1.650);
\draw (0.630,-1.803) -- (0.557,-1.834);
\draw (0.717,-1.933) -- (0.661,-1.989);
\draw (0.847,-2.020) -- (0.816,-2.093);
\draw (1.000,-2.050) -- (1.000,-2.130);
\draw (1.153,-2.020) -- (1.184,-2.093);
\draw (1.283,-1.933) -- (1.339,-1.989);
\draw (1.370,-1.803) -- (1.443,-1.834);
\node[] at (1,-1.65) {$N_3$};
\draw (2,-1.65) circle (0.6);\fill (2,-1.65) circle (1pt);
\draw (2.600,-1.650) -- (2.680,-1.650);
\draw (2.554,-1.420) -- (2.628,-1.390);
\draw (2.424,-1.226) -- (2.481,-1.169);
\draw (2.230,-1.096) -- (2.260,-1.022);
\draw (2.000,-1.050) -- (2.000,-0.970);
\draw (1.770,-1.096) -- (1.740,-1.022);
\draw (1.576,-1.226) -- (1.519,-1.169);
\draw (1.446,-1.420) -- (1.372,-1.390);
\draw (1.400,-1.650) -- (1.320,-1.650);
\draw (1.446,-1.880) -- (1.372,-1.910);
\draw (1.576,-2.074) -- (1.519,-2.131);
\draw (1.770,-2.204) -- (1.740,-2.278);
\draw (2.000,-2.250) -- (2.000,-2.330);
\draw (2.230,-2.204) -- (2.260,-2.278);
\draw (2.424,-2.074) -- (2.481,-2.131);
\draw (2.554,-1.880) -- (2.628,-1.910);
\node[] at (2,-1.65) {$N_4$};
\draw (2,-3.3) circle (0.4);\fill (2,-3.3) circle (1pt);
\draw (2.400,-3.300) -- (2.480,-3.300);
\draw (2.370,-3.147) -- (2.443,-3.116);
\draw (2.283,-3.017) -- (2.339,-2.961);
\draw (2.153,-2.930) -- (2.184,-2.857);
\draw (2.000,-2.900) -- (2.000,-2.820);
\draw (1.847,-2.930) -- (1.816,-2.857);
\draw (1.717,-3.017) -- (1.661,-2.961);
\draw (1.630,-3.147) -- (1.557,-3.116);
\draw (1.600,-3.300) -- (1.520,-3.300);
\draw (1.630,-3.453) -- (1.557,-3.484);
\draw (1.717,-3.583) -- (1.661,-3.639);
\draw (1.847,-3.670) -- (1.816,-3.743);
\draw (2.000,-3.700) -- (2.000,-3.780);
\draw (2.153,-3.670) -- (2.184,-3.743);
\draw (2.283,-3.583) -- (2.339,-3.639);
\draw (2.370,-3.453) -- (2.443,-3.484);
\node[] at (2,-3.3) {$N_5$};
\draw (3,-3.3) circle (0.6);\fill (3,-3.3) circle (1pt);
\draw (3.600,-3.300) -- (3.680,-3.300);
\draw (3.554,-3.070) -- (3.628,-3.040);
\draw (3.424,-2.876) -- (3.481,-2.819);
\draw (3.230,-2.746) -- (3.260,-2.672);
\draw (3.000,-2.700) -- (3.000,-2.620);
\draw (2.770,-2.746) -- (2.740,-2.672);
\draw (2.576,-2.876) -- (2.519,-2.819);
\draw (2.446,-3.070) -- (2.372,-3.040);
\draw (2.400,-3.300) -- (2.320,-3.300);
\draw (2.446,-3.530) -- (2.372,-3.560);
\draw (2.576,-3.724) -- (2.519,-3.781);
\draw (2.770,-3.854) -- (2.740,-3.928);
\draw (3.000,-3.900) -- (3.000,-3.980);
\draw (3.230,-3.854) -- (3.260,-3.928);
\draw (3.424,-3.724) -- (3.481,-3.781);
\draw (3.554,-3.530) -- (3.628,-3.560);
\node[] at (3,-3.3) {$N_6$};
\draw (1,0) -- (1,-1.65) (2,-1.65) -- (2,-3.3);\node[] at (-0.8,0) {$\theta_1$};
\node[] at (4,-3.3) {$\theta_4$};

\end{tikzpicture}
\end{document}
```

$$
\boxed{\frac{\theta_4}{\theta_1}=\frac{N_1N_3N_5}{N_2N_4N_6}}
$$

**Exemplo:** determine $\Theta_2(s)/T(s)$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (j1) at (0,0) {$J_1=2$};
\draw (1.4,0) circle (0.35);\fill (1.4,0) circle (1pt);
\draw (1.750,0.000) -- (1.830,0.000);
\draw (1.723,0.134) -- (1.797,0.165);
\draw (1.647,0.247) -- (1.704,0.304);
\draw (1.534,0.323) -- (1.565,0.397);
\draw (1.400,0.350) -- (1.400,0.430);
\draw (1.266,0.323) -- (1.235,0.397);
\draw (1.153,0.247) -- (1.096,0.304);
\draw (1.077,0.134) -- (1.003,0.165);
\draw (1.050,0.000) -- (0.970,0.000);
\draw (1.077,-0.134) -- (1.003,-0.165);
\draw (1.153,-0.247) -- (1.096,-0.304);
\draw (1.266,-0.323) -- (1.235,-0.397);
\draw (1.400,-0.350) -- (1.400,-0.430);
\draw (1.534,-0.323) -- (1.565,-0.397);
\draw (1.647,-0.247) -- (1.704,-0.304);
\draw (1.723,-0.134) -- (1.797,-0.165);
\node[] at (1.4,0) {$4$};
\draw (1.4,-1) circle (0.65);\fill (1.4,-1) circle (1pt);
\draw (2.050,-1.000) -- (2.130,-1.000);
\draw (2.001,-0.751) -- (2.074,-0.721);
\draw (1.860,-0.540) -- (1.916,-0.484);
\draw (1.649,-0.399) -- (1.679,-0.326);
\draw (1.400,-0.350) -- (1.400,-0.270);
\draw (1.151,-0.399) -- (1.121,-0.326);
\draw (0.940,-0.540) -- (0.884,-0.484);
\draw (0.799,-0.751) -- (0.726,-0.721);
\draw (0.750,-1.000) -- (0.670,-1.000);
\draw (0.799,-1.249) -- (0.726,-1.279);
\draw (0.940,-1.460) -- (0.884,-1.516);
\draw (1.151,-1.601) -- (1.121,-1.674);
\draw (1.400,-1.650) -- (1.400,-1.730);
\draw (1.649,-1.601) -- (1.679,-1.674);
\draw (1.860,-1.460) -- (1.916,-1.516);
\draw (2.001,-1.249) -- (2.074,-1.279);
\node[] at (1.4,-1) {$12$};
\node[b] (j2) at (3,-1) {$J_2=1$};
\draw (4.5,-1) circle (0.65);\fill (4.5,-1) circle (1pt);
\draw (5.150,-1.000) -- (5.230,-1.000);
\draw (5.101,-0.751) -- (5.174,-0.721);
\draw (4.960,-0.540) -- (5.016,-0.484);
\draw (4.749,-0.399) -- (4.779,-0.326);
\draw (4.500,-0.350) -- (4.500,-0.270);
\draw (4.251,-0.399) -- (4.221,-0.326);
\draw (4.040,-0.540) -- (3.984,-0.484);
\draw (3.899,-0.751) -- (3.826,-0.721);
\draw (3.850,-1.000) -- (3.770,-1.000);
\draw (3.899,-1.249) -- (3.826,-1.279);
\draw (4.040,-1.460) -- (3.984,-1.516);
\draw (4.251,-1.601) -- (4.221,-1.674);
\draw (4.500,-1.650) -- (4.500,-1.730);
\draw (4.749,-1.601) -- (4.779,-1.674);
\draw (4.960,-1.460) -- (5.016,-1.516);
\draw (5.101,-1.249) -- (5.174,-1.279);
\node[] at (4.5,-1) {$16$};
\draw (4.5,-2) circle (0.35);\fill (4.5,-2) circle (1pt);
\draw (4.850,-2.000) -- (4.930,-2.000);
\draw (4.823,-1.866) -- (4.897,-1.835);
\draw (4.747,-1.753) -- (4.804,-1.696);
\draw (4.634,-1.677) -- (4.665,-1.603);
\draw (4.500,-1.650) -- (4.500,-1.570);
\draw (4.366,-1.677) -- (4.335,-1.603);
\draw (4.253,-1.753) -- (4.196,-1.696);
\draw (4.177,-1.866) -- (4.103,-1.835);
\draw (4.150,-2.000) -- (4.070,-2.000);
\draw (4.177,-2.134) -- (4.103,-2.165);
\draw (4.253,-2.247) -- (4.196,-2.304);
\draw (4.366,-2.323) -- (4.335,-2.397);
\draw (4.500,-2.350) -- (4.500,-2.430);
\draw (4.634,-2.323) -- (4.665,-2.397);
\draw (4.747,-2.247) -- (4.804,-2.304);
\draw (4.823,-2.134) -- (4.897,-2.165);
\node[] at (4.5,-2) {$4$};
\node[b] (j3) at (6,-2) {$J_3=16$};
\draw (6.750,-2.000) -- (6.950,-2.000) -- (7.088,-1.880) -- (7.225,-2.120) -- (7.362,-1.880) -- (7.500,-2.120) -- (7.638,-1.880) -- (7.775,-2.120) -- (7.913,-1.880) -- (8.050,-2.000) -- (8.250,-2.000);
\node[] at (7.5,-1.65) {$K=64$};
\draw[very thick] (8.25,-2.7) -- (8.25,-1.3);
\draw (8.07,-2.65) -- (8.25,-2.5);\draw (8.07,-2.42) -- (8.25,-2.27);\draw (8.07,-2.19) -- (8.25,-2.04);\draw (8.07,-1.96) -- (8.25,-1.81);\draw (8.07,-1.73) -- (8.25,-1.58);
\draw (j1.east)--(1.4,0) (1.4,-1)--(j2.west) (j2.east)--(4.5,-1) (4.5,-2)--(j3.west) (j3.east)--(6.75,-2);\node[] at (0,0.8) {$T,D_1=1$};
\node[] at (3,-0.25) {$D_2=2$};
\node[] at (6,-1.25) {$D_3=32$};

\end{tikzpicture}
\end{document}
```

$$
\begin{aligned}
J_{eq}&=J_1\left(\frac{N_2}{N_1}\right)^2+J_2+J_3\left(\frac{N_3}{N_4}\right)^2\\
&=2\left(\frac{12}{4}\right)^2+1+16\left(\frac4{16}\right)^2=20\\
D_{eq}&=D_1\left(\frac{N_2}{N_1}\right)^2+D_2+D_3\left(\frac{N_3}{N_4}\right)^2\\
&=1\left(\frac{12}{4}\right)^2+2+32\left(\frac4{16}\right)^2=13\\
K_{eq}&=64\left(\frac4{16}\right)^2=4
\end{aligned}
$$

$$
T_{eq}:\quad\frac{T_2}{T_1}=\frac{N_2}{N_1}\Rightarrow T_2=\frac{12}{4}T(s)=3T(s)
$$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (j) at (0,0) {$J_{eq}=20$};
\draw (0.850,0.400) -- (1.050,0.400) -- (1.325,0.520) -- (1.600,0.280) -- (1.875,0.520) -- (2.150,0.280) -- (2.425,0.520) -- (2.700,0.280) -- (2.975,0.520) -- (3.250,0.400) -- (3.450,0.400);
\node[] at (2.15,0.75) {$4$};
\draw (0.85,-0.4) -- (1.8900000000000001,-0.4) (1.8900000000000001,-0.5800000000000001) -- (1.8900000000000001,-0.22000000000000003) (2.54,-0.65) -- (1.79,-0.65) (2.54,-0.15000000000000002) -- (1.79,-0.15000000000000002) (2.54,-0.65) -- (2.54,-0.15000000000000002) (2.54,-0.4) -- (3.45,-0.4);
\node[] at (2.15,-0.8) {$13$};
\draw[very thick] (3.45,-1) -- (3.45,1);
\draw (3.27,-0.9500000000000001) -- (3.45,-0.8);\draw (3.27,-0.7200000000000001) -- (3.45,-0.5700000000000001);\draw (3.27,-0.49) -- (3.45,-0.34);\draw (3.27,-0.26) -- (3.45,-0.10999999999999999);\draw (3.27,-0.03) -- (3.45,0.12);\draw (3.27,0.2000000000000001) -- (3.45,0.3500000000000001);\draw (3.27,0.43000000000000005) -- (3.45,0.5800000000000001);\draw (3.27,0.66) -- (3.45,0.81);
\draw[->] (-1.8,0) -- node[above] {$3T(s)$} (j.west);
\node[] at (0,0.75) {$\theta_2$};

\end{tikzpicture}
\end{document}
```

$$
3T(s)-(20s^2+13s+4)\Theta_2=0
$$

$$
\boxed{\frac{\Theta_2}{T(s)}=\frac3{20s^2+13s+4}}
$$

## 7. Modelagem de sistemas eletromecânicos

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw (1.000,2.000) -- (1.200,2.000) -- (1.337,2.120) -- (1.475,1.880) -- (1.613,2.120) -- (1.750,1.880) -- (1.887,2.120) -- (2.025,1.880) -- (2.163,2.120) -- (2.300,2.000) -- (2.500,2.000);
\draw (3,2) .. controls (3.03,2.32) and (3.345,2.32) .. (3.375,2) .. controls (3.405,2.32) and (3.72,2.32) .. (3.75,2) .. controls (3.78,2.32) and (4.095,2.32) .. (4.125,2) .. controls (4.155,2.32) and (4.47,2.32) .. (4.5,2);
\draw (0,2)--(1,2) (2.5,2)--(3,2) (4.5,2)--(5.5,2)--(5.5,1.4) (5.5,.6)--(5.5,0)--(0,0);\draw (5.25,.6) rectangle (5.75,1.4);\fill (0,2) circle(1.2pt) (0,0) circle(1.2pt);\node[] at (0.1,1) {$e_a(t)$};
\node[] at (1.75,2.35) {$R_a$};
\node[] at (3.75,2.4) {$L_a$};
\node[] at (2.8,1) {$i_a(t)$};
\node[] at (6.2,1) {$V_{cea}$};
\node[] at (5.95,1.55) {$+$};
\node[] at (5.95,0.45) {$-$};
\draw[->] (5.75,.85) -- node[above] {$T_m$} (7,-.25);
\node[] at (7.1,-0.6) {$\theta_m$};
\begin{scope}[shift={(1,-1.5)}]
\node[b] (b0) at (1.4,0) {$G(s)$};
\draw[->] (0,0) -- node[above] {$E_a(s)$} (b0.west);
\draw[->] (b0.east) -- node[above] {$\Theta_m(s)$} (2.9,0);

\end{scope}

\end{tikzpicture}
\end{document}
```

- $R_a$: resistência da armadura.
- $L_a$: indutância da armadura.
- $i_a(t)$: corrente da armadura.
- $e_a(t)$: tensão da armadura.
- $v_{cea}(t)$: força contraeletromotriz.
- $T_m(t)$: torque do motor.
- $\theta_m(t)$: deslocamento angular do eixo do motor.

$$
v_{cea}(t)=K_{cea}\frac{d\theta_m(t)}{dt}\Rightarrow V_{cea}(s)=K_{cea}s\Theta_m(s)\tag{1}
$$

$K_{cea}$: constante FCEM.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw (1.000,2.000) -- (1.200,2.000) -- (1.337,2.120) -- (1.475,1.880) -- (1.613,2.120) -- (1.750,1.880) -- (1.887,2.120) -- (2.025,1.880) -- (2.163,2.120) -- (2.300,2.000) -- (2.500,2.000);
\draw (3,2) .. controls (3.03,2.32) and (3.345,2.32) .. (3.375,2) .. controls (3.405,2.32) and (3.72,2.32) .. (3.75,2) .. controls (3.78,2.32) and (4.095,2.32) .. (4.125,2) .. controls (4.155,2.32) and (4.47,2.32) .. (4.5,2);
\draw (0,2)--(1,2) (2.5,2)--(3,2) (4.5,2)--(5.5,2)--(5.5,1.4) (5.5,.6)--(5.5,0)--(0,0);\draw (5.25,.6) rectangle (5.75,1.4);\fill (0,2) circle(1.2pt) (0,0) circle(1.2pt);\node[] at (0.1,1) {$E_a(s)$};
\node[] at (1.75,2.35) {$R_a$};
\node[] at (3.75,2.4) {$sL_a$};
\node[] at (2.8,1) {$I_a(s)$};
\node[] at (6.2,1) {$V_{cea}$};
\node[] at (5.95,1.55) {$+$};
\node[] at (5.95,0.45) {$-$};

\end{tikzpicture}
\end{document}
```

**LKT:**

$$
\begin{aligned}
-E_a+(R_a+sL_a)I_a+V_{cea}&=0\\
(sL_a+R_a)I_a+V_{cea}&=E_a
\end{aligned}
\tag{2}
$$

O torque desenvolvido pelo motor é proporcional à corrente da armadura.

$$
T_m(s)=K_TI_a(s)\Rightarrow I_a(s)=\frac1{K_T}T_m(s)\tag{3}
$$

Substituindo (1) e (3) em (2):

$$
(sL_a+R_a)\frac1{K_T}T_m+K_{cea}s\Theta_m=E_a\tag{4}
$$

Carregamento mecânico equivalente típico em um motor:

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (j) at (0,0) {$J_m$};
\draw (0.6,0) -- (1.56,0) (1.56,-0.18) -- (1.56,0.18) (2.16,-0.25) -- (1.46,-0.25) (2.16,0.25) -- (1.46,0.25) (2.16,-0.25) -- (2.16,0.25) (2.16,0) -- (3.0,0);
\node[] at (1.7999999999999998,-0.4) {$D_m$};
\draw[very thick] (3,-1) -- (3,1);
\draw (2.82,-0.9500000000000001) -- (3,-0.8);\draw (2.82,-0.7200000000000001) -- (3,-0.5700000000000001);\draw (2.82,-0.49) -- (3,-0.34);\draw (2.82,-0.26) -- (3,-0.10999999999999999);\draw (2.82,-0.03) -- (3,0.12);\draw (2.82,0.2000000000000001) -- (3,0.3500000000000001);\draw (2.82,0.43000000000000005) -- (3,0.5800000000000001);\draw (2.82,0.66) -- (3,0.81);
\draw[->] (-2,0) -- node[above] {$T_m(s)$} (j.west);
\node[] at (0,0.8) {$\theta_m$};

\end{tikzpicture}
\end{document}
```

$J_m$: inércia da armadura. $D_m$: amortecimento viscoso da armadura.

$$
T_m-(J_ms^2+D_ms)\Theta_m=0\Rightarrow T_m(s)=(J_ms^2+D_ms)\Theta_m(s)\tag{5}
$$

Substituindo (5) em (4):

$$
(sL_a+R_a)\frac1{K_T}(J_ms^2+D_ms)\Theta_m+K_{cea}s\Theta_m=E_a
$$

Obs.: considerando a indutância da armadura muito pequena em relação à resistência, sua influência pode ser desprezada: $sL_a+R_a\approx R_a$.

$$
\left[\frac{R_a}{K_T}(J_ms+D_m)+K_{cea}\right]s\Theta_m=E_a
$$

$$
\begin{aligned}
\frac{\Theta_m}{E_a}&=\frac1{\left[\frac{R_a}{K_T}(J_ms+D_m)+K_{cea}\right]s}\\
&=\frac{K_T/R_a}{s\left[J_ms+D_m+\frac{K_{cea}K_T}{R_a}\right]}\\
\boxed{\frac{\Theta_m}{E_a}=\frac{\frac{K_T}{R_a}\frac1{J_m}}{s\left[s+\frac1{J_m}\left(D_m+\frac{K_TK_{cea}}{R_a}\right)\right]}}
\end{aligned}
$$

### Constantes mecânicas

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (m) at (0,0) {$\mathrm{Motor}$};
\draw (1.5,0) circle (0.45);\fill (1.5,0) circle (1pt);
\draw (1.950,0.000) -- (2.030,0.000);
\draw (1.916,0.172) -- (1.990,0.203);
\draw (1.818,0.318) -- (1.875,0.375);
\draw (1.672,0.416) -- (1.703,0.490);
\draw (1.500,0.450) -- (1.500,0.530);
\draw (1.328,0.416) -- (1.297,0.490);
\draw (1.182,0.318) -- (1.125,0.375);
\draw (1.084,0.172) -- (1.010,0.203);
\draw (1.050,0.000) -- (0.970,0.000);
\draw (1.084,-0.172) -- (1.010,-0.203);
\draw (1.182,-0.318) -- (1.125,-0.375);
\draw (1.328,-0.416) -- (1.297,-0.490);
\draw (1.500,-0.450) -- (1.500,-0.530);
\draw (1.672,-0.416) -- (1.703,-0.490);
\draw (1.818,-0.318) -- (1.875,-0.375);
\draw (1.916,-0.172) -- (1.990,-0.203);
\node[] at (1.5,0) {$N_1$};
\draw (1.5,-1.15) circle (0.7);\fill (1.5,-1.15) circle (1pt);
\draw (2.200,-1.150) -- (2.280,-1.150);
\draw (2.147,-0.882) -- (2.221,-0.852);
\draw (1.995,-0.655) -- (2.052,-0.598);
\draw (1.768,-0.503) -- (1.798,-0.429);
\draw (1.500,-0.450) -- (1.500,-0.370);
\draw (1.232,-0.503) -- (1.202,-0.429);
\draw (1.005,-0.655) -- (0.948,-0.598);
\draw (0.853,-0.882) -- (0.779,-0.852);
\draw (0.800,-1.150) -- (0.720,-1.150);
\draw (0.853,-1.418) -- (0.779,-1.448);
\draw (1.005,-1.645) -- (0.948,-1.702);
\draw (1.232,-1.797) -- (1.202,-1.871);
\draw (1.500,-1.850) -- (1.500,-1.930);
\draw (1.768,-1.797) -- (1.798,-1.871);
\draw (1.995,-1.645) -- (2.052,-1.702);
\draw (2.147,-1.418) -- (2.221,-1.448);
\node[] at (1.5,-1.15) {$N_2$};
\node[b] (j) at (3.2,-1.15) {$J_c$};
\draw (3.8,-1.15) -- (4.6,-1.15) (4.6,-1.3299999999999998) -- (4.6,-0.97) (5.1,-1.4) -- (4.5,-1.4) (5.1,-0.8999999999999999) -- (4.5,-0.8999999999999999) (5.1,-1.4) -- (5.1,-0.8999999999999999) (5.1,-1.15) -- (5.8,-1.15);
\node[] at (4.8,-1.5499999999999998) {$D_c$};
\draw[very thick] (5.8,-1.8) -- (5.8,-0.5);
\draw (5.62,-1.75) -- (5.8,-1.6);\draw (5.62,-1.52) -- (5.8,-1.37);\draw (5.62,-1.29) -- (5.8,-1.1400000000000001);\draw (5.62,-1.06) -- (5.8,-0.91);\draw (5.62,-0.8300000000000001) -- (5.8,-0.68);
\draw (m.east)--(1.5,0) (1.5,-1.15)--(j.west) (j.east)--(3.8,-1.15);\node[] at (0,-0.55) {$J_a,D_a$};

\end{tikzpicture}
\end{document}
```

$$
\boxed{J_m=J_a+J_c\left(\frac{N_1}{N_2}\right)^2}\qquad
\boxed{D_m=D_a+D_c\left(\frac{N_1}{N_2}\right)^2}
$$

### Constantes elétricas

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw[->] (0,0)--(4,0) node[right] {$\omega$};\draw[->] (0,0)--(0,2.6) node[above] {$T$};\draw[blue,thick] (0,2.2)--(3.3,0);\node[] at (-0.55,2.2) {$T_{bloq}$};
\node[] at (3.3,-0.35) {$\omega_{vazio}$};
\node[] at (1.55,1.35) {$e_a$};

\end{tikzpicture}
\end{document}
```

$$
\boxed{K_{cea}=\frac{e_a}{\omega_{vazio}}}\qquad\boxed{\frac{K_T}{R_a}=\frac{T_{bloq}}{e_a}}
$$
