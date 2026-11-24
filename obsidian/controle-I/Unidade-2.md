# Unidade 2 — Sistemas de Controle I

## Linearização

Fórmula geral:

$$
\boxed{y-y_0=\left.\frac{df}{dx}\right|_{x=x_0}(x-x_0)}
$$

**Exemplo:**

 a) Linearize a função $y=\sqrt{x}$ em $x_0=4$.

 b) Encontre o erro relativo e absoluto em $x=4{,}001$.

**a)**

$$
\begin{aligned}
y_0&=\sqrt{x_0}=\sqrt4=2\\
\left.\frac{df}{dx}\right|_{x=4}&=\frac1{2\sqrt4}=\frac14\\
y-2&=\frac14(x-4)\\
y&=\frac x4-1+2\\
\boxed{y=0{,}25x+1}
\end{aligned}
$$

**b)**

$$
\begin{aligned}
y_N&=\sqrt{4{,}001}\approx2{,}00024\quad\text{(não linear)}\\
y_L&=0{,}25\cdot4{,}001+1=2{,}00025\\
E_{abs}&=|y_L-y_N|\approx0\\
E_{rel}&=\frac{|y_L-y_N|}{y_N}
\end{aligned}
$$

**SISO:**

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (b0) at (1.4,0) {$G(s)$};
\draw[->] (0,0) -- node[above] {$X(s)$} (b0.west);
\draw[->] (b0.east) -- node[above] {$Y(s)$} (2.9,0);

\end{tikzpicture}
\end{document}
```

$$
y-y_0=\left.\frac{df}{dx}\right|_{x=x_0}(x-x_0)
$$

**MISO ou MIMO:**

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (b) at (2,0) {$G(s)$};
\draw[->] (0,.2) -- node[above] {$X(s)$} (b.160);
\draw[->] (0,-.2) -- node[above] {$Y(s)$} (b.200);
\draw[->] (b.east) -- node[above] {$Z(s)$} (4,0);

\end{tikzpicture}
\end{document}
```

$$
z-z_0=\left.\frac{\partial f}{\partial x}\right|_0(x-x_0)+\left.\frac{\partial f}{\partial y}\right|_0(y-y_0)
$$

> Obs.: o desenho é MISO; as derivadas parciais foram identificadas conforme a variável de cada termo (os índices aparecem trocados no caderno).

## Resposta no domínio do tempo

Polos e zeros:

$$
FT=\frac{s+2}{s+3}
$$

- Zeros: fazem o numerador tender a zero.
- Polos: fazem a função tender a infinito (denominador tende a zero).

> Obs.: está anotado $F=\text{Polos}/\text{Zeros}$; na forma fatorada da FT os zeros estão no numerador e os polos no denominador.

### Sistemas de primeira ordem

$$
\begin{aligned}
C(s)&=R(s)G(s)=\frac1s\frac{a}{s+a}=\frac{a}{s(s+a)}\\
&=\frac As+\frac B{s+a},\qquad A=1,\ B=-1\\
c(t)&=1-e^{-at}
\end{aligned}
$$

Em $t=1/a$:

$$
c(t)=1-e^{-1}=0{,}632
$$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw[->] (0,0)--(6.6,0) node[right] {$at$};\draw[->] (0,0)--(0,2.65) node[above] {$c(t)$};
\draw[blue,thick,domain=0:6,samples=80] plot (\x,{2*(1-exp(-\x))});
\draw[dashed] (0,2)--(6,2) node[right] {setpoint};
\foreach \x/\lab in {1/{1},2.3026/{2{,}3},4/{4}} {\draw[dashed,gray] (\x,0)--(\x,{2*(1-exp(-\x))})--(0,{2*(1-exp(-\x))});\node[below] at (\x,0) {$\lab$};}
\node[left] at (0,1.264) {$0{,}632$};\node[left] at (0,1.8) {$0{,}90$};\node[above left] at (0,1.965) {$0{,}98$};

\end{tikzpicture}
\end{document}
```

- Constante de tempo: $\boxed{\tau=1/a}$ → 63% do valor final.
- Tempo de subida (rise time): $\boxed{T_r=2{,}2/a}$ → de 10% a 90% do valor final (o início está anotado como 2% no caderno).
- Tempo de acomodação (settling time): $\boxed{T_s=4/a}$ → até 98% do valor final.

### Sistemas de segunda ordem

Em ordem de rapidez anotada:

- Não amortecido ($\zeta=0$): dois polos puramente imaginários.
- Subamortecido ($0<\zeta<1$): dois polos complexos e distintos.
- Criticamente amortecido ($\zeta=1$): dois polos reais e iguais.
- Superamortecido ($\zeta>1$): dois polos reais e distintos.

Função de transferência geral de segunda ordem:

$$
\boxed{G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}}
$$

$\omega_n$: frequência natural; $\zeta$: coeficiente de amortecimento.

**Exemplo:** determine $\omega_n$ e $\zeta$.

**a)**

$$
G(s)=\frac{12}{s^2+8s+12}
$$

$$
\omega_n^2=12\Rightarrow\omega_n=\sqrt{12},\qquad 2\zeta\omega_n=8\Rightarrow\zeta=\frac8{2\sqrt{12}}\approx1{,}15
$$

**b)**

$$
G(s)=\frac{16}{s^2+8s+16}
$$

$$
\omega_n=\sqrt{16}=4,\qquad\zeta=\frac8{2\cdot4}=1
$$

#### Tempo de pico

$$
\boxed{T_p=\frac{\pi}{\omega_n\sqrt{1-\zeta^2}}}
$$

Relacionado com a parte imaginária.

#### Ultrapassagem percentual

$$
\boxed{\%UP=\frac{c_{max}-c_{final}}{c_{final}}\cdot100}
$$

$$
\boxed{\%UP=e^{-\frac{\zeta\pi}{\sqrt{1-\zeta^2}}}\cdot100}
$$

Isolando o zeta:

$$
\boxed{\zeta=\frac{-\ln(\%UP/100)}{\sqrt{\pi^2+\ln^2(\%UP/100)}}}
$$

#### Tempo de acomodação

$$
\boxed{T_s=\frac4{\zeta\omega_n}}
$$

Relaciona-se com a parte real.

#### Tempo de subida

$$
\boxed{T_r=\frac{\pi-\beta}{\omega_n\sqrt{1-\zeta^2}}}
$$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw[->] (-4,0)--(1.1,0) node[right] {Re};\draw[->] (0,-1)--(0,3) node[above] {Im};\draw[blue,thick,->] (0,0)--(-2.8,2.1) node[midway,above] {$\omega_n$};\draw[dashed] (-2.8,0)--(-2.8,2.1)--(0,2.1);\node[below] at (-2.8,0) {$-\zeta\omega_n$};\node[right] at (0,2.1) {$j\omega_n\sqrt{1-\zeta^2}$};\draw (-.7,0) arc (180:143:.7);\node at (-.95,.31) {$\beta$};
\end{tikzpicture}
\end{document}
```

$$
\beta=\arctan\left(\frac{\omega_n\sqrt{1-\zeta^2}}{-\zeta\omega_n}\right)
$$

> Obs.: o desenho mede $\beta$ a partir do eixo real negativo; para esse ângulo agudo, usa-se $\zeta\omega_n$ positivo no denominador.

## Teorema do valor final para sistemas de 1ª e 2ª ordem

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\begin{scope}[shift={(0,0)}]
\draw[->] (0,0)--(6.6,0) node[right] {$at$};\draw[->] (0,0)--(0,2.65) node[above] {$c(t)$};
\draw[blue,thick,domain=0:6,samples=80] plot (\x,{2*(1-exp(-\x))});
\draw[dashed] (0,2)--(6,2) node[right] {setpoint};
\foreach \x/\lab in {1/{1},2.3026/{2{,}3},4/{4}} {\draw[dashed,gray] (\x,0)--(\x,{2*(1-exp(-\x))})--(0,{2*(1-exp(-\x))});\node[below] at (\x,0) {$\lab$};}
\node[left] at (0,1.264) {$0{,}632$};\node[left] at (0,1.8) {$0{,}90$};\node[above left] at (0,1.965) {$0{,}98$};

\end{scope}
\begin{scope}[shift={(0,-4)}]
\draw[->] (0,0)--(6.5,0) node[right] {$t$};\draw[->] (0,0)--(0,2.8) node[above] {$c(t)$};\draw[dashed] (0,1.8)--(6.3,1.8) node[right] {$c_{final}$};\draw[blue,thick,domain=0:6.2,samples=120] plot (\x,{1.8*(1-exp(-.7*\x)*(cos(155*\x)+.7/2.705*sin(155*\x)))});\draw[dashed] (1.16,0)--(1.16,2.60);\node[below] at (1.16,0) {$T_p$};\draw[dashed] (0,2.60)--(1.16,2.60);\node[left] at (0,2.6) {$c_{max}$};\draw[dashed] (5.71,0)--(5.71,1.8);\node[below] at (5.71,0) {$T_s$};\node[below] at (.675,0) {$T_r$};
\end{scope}

\end{tikzpicture}
\end{document}
```

Valor final = setpoint.

$$
\boxed{f(\infty)=\lim_{s\to0}sF(s)}
$$

### Resposta do sistema com polos adicionais

$$
\frac1{(s^2+2s+5)(s+20)}
$$

$(s+20)$ é desprezado porque esse polo está muito distante. Por via de regra é adotada uma distância de cinco constantes de tempo.

$$
p_{1,2}=-1\pm j2
$$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw[->] (-6.6,0)--(1,0) node[right] {Re};\draw[->] (0,-2)--(0,2) node[above] {Im};\foreach \x/\y in {-6/0,-.3/1.3,-.3/-1.3}{\node[red] at (\x,\y) {$\times$};}\node[below] at (-6,0) {$-20$};\node[below] at (-.3,0) {$-1$};\node[right] at (0,1.3) {$j2$};\node[right] at (0,-1.3) {$-j2$};\draw[<->] (-6,-.55)--(-.3,-.55) node[midway,below] {$19\tau$};
\end{tikzpicture}
\end{document}
```

$19\tau>5\tau$: logo podemos desprezar o polo (notação do caderno).

## Diagrama de bloco

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\draw[->] (0,0) -- node[above] {$R(s)$} (2,0);
\draw[->] (3,0) -- node[above] {$C(s)$} (5,0);
\begin{scope}[shift={(0,-1.4)}]
\node[b] (b0) at (1.4,0) {$G(s)$};
\draw[->] (0,0) -- node[above] {$R(s)$} (b0.west);
\draw[->] (b0.east) -- node[above] {$C(s)$} (2.9,0);

\end{scope}
\begin{scope}[shift={(0,-3)}]
\node[s] (s) at (2,0) {$+$};
\draw[->] (0,0) -- node[above] {$R_1$} (s.west);
\draw[->] (1,-1) -- node[above] {$R_2$} (s.south west);
\draw[->] (2,-1.25) -- node[above] {$R_3$} (s.south);
\node[] at (2.35,-0.5) {$-$};
\draw[->] (s.east) -- node[above] {$C=R_1+R_2-R_3$} (6,0);

\end{scope}
\begin{scope}[shift={(0,-5.3)}]
\draw[->] (0,0) -- node[above] {$R(s)$} (4,0);
\fill (2,0) circle (1.4pt);
\draw[->] (2,0)|-(4,.6);\draw[->] (2,0)|-(4,-.6);\node[] at (4.45,0.6) {$R(s)$};
\node[] at (4.45,-0.6) {$R(s)$};

\end{scope}

\end{tikzpicture}
\end{document}
```

**Série:** multiplica as FTs.

$$
\frac CR=G_1G_2
$$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (b0) at (1.4,0) {$G_1$};
\draw[->] (0,0) -- node[above] {$R$} (b0.west);
\node[b] (b1) at (3.4,0) {$G_2$};
\draw[->] (b0.east) -- (b1.west);
\draw[->] (b1.east) -- node[above] {$C$} (4.9,0);

\end{tikzpicture}
\end{document}
```

**Paralelo:** soma/subtrai as FTs.

$$
\frac CR=G_1+G_2
$$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (a) at (2,0) {$G_1$};
\node[b] (b) at (2,-1.4) {$G_2$};
\node[s] (s) at (4.2,0) {$+$};
\draw[->] (0,0) -- node[above] {$R$} (a.west);
\draw[->] (a.east) -- (s.west);
\draw[->] (.7,0) |- (b.west);\draw[->] (b.east) -| (s.south);
\fill (0.7,0) circle (1.4pt);
\node[] at (3.9,-0.45) {$\pm$};
\draw[->] (s.east) -- node[above] {$C$} (5.5,0);

\end{tikzpicture}
\end{document}
```

**Realimentação:**

$$
\frac CR=\frac G{1\pm GH}
$$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (s0) at (1,0) {$+$};
\draw[->] (0,0) -- node[above] {$R$} (s0.west);
\node[] at (0.73,-0.43) {$-$};
\node[b] (b0) at (2.6,0) {$G_1$};
\draw[->] (s0.east) -- (b0.west);
\draw[->] (b0.east) -- node[above] {$C$} (4.5,0);
\fill (3.8,0) circle (1.4pt);
\node[b] (h) at (2.4,-1.25) {$H_1$};
\draw[->] (3.8,0) |- (h.east);\draw[->] (h.west) -| (s0.south);

\end{tikzpicture}
\end{document}
```

### Transformações de diagramas de blocos

1. Combinação de blocos em cascata: $Y=(P_1P_2)X$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (b0) at (1.4,0) {$P_1$};
\draw[->] (0,0) -- node[above] {$X$} (b0.west);
\node[b] (b1) at (3.4,0) {$P_2$};
\draw[->] (b0.east) -- (b1.west);
\draw[->] (b1.east) -- node[above] {$Y$} (4.9,0);
\node[] at (-0.75,-0.9) {$\equiv$};
\begin{scope}[shift={(0,-1.8)}]
\node[b] (b0) at (1.4,0) {$P_1P_2$};
\draw[->] (0,0) -- node[above] {$X$} (b0.west);
\draw[->] (b0.east) -- node[above] {$Y$} (2.9,0);

\end{scope}

\end{tikzpicture}
\end{document}
```

2. Combinação de blocos em paralelo ou eliminação de uma malha direta: $Y=P_1X\pm P_2X$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (a) at (2,0) {$P_1$};
\node[b] (b) at (2,-1.4) {$P_2$};
\node[s] (s) at (4.2,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (a.west);
\draw[->] (a.east) -- (s.west);
\draw[->] (.7,0) |- (b.west);\draw[->] (b.east) -| (s.south);
\fill (0.7,0) circle (1.4pt);
\node[] at (3.9,-0.45) {$\pm$};
\draw[->] (s.east) -- node[above] {$Y$} (5.5,0);
\node[] at (-0.75,-1.45) {$\equiv$};
\begin{scope}[shift={(0,-2.9)}]
\node[b] (b0) at (1.4,0) {$P_1\pm P_2$};
\draw[->] (0,0) -- node[above] {$X$} (b0.west);
\draw[->] (b0.east) -- node[above] {$Y$} (2.9,0);

\end{scope}

\end{tikzpicture}
\end{document}
```

3. Remoção de um bloco de um percurso direto: $Y=P_1X\pm P_2X$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (a) at (2,0) {$P_1$};
\node[b] (b) at (2,-1.4) {$P_2$};
\node[s] (s) at (4.2,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (a.west);
\draw[->] (a.east) -- (s.west);
\draw[->] (.7,0) |- (b.west);\draw[->] (b.east) -| (s.south);
\fill (0.7,0) circle (1.4pt);
\node[] at (3.9,-0.45) {$\pm$};
\draw[->] (s.east) -- node[above] {$Y$} (5.5,0);
\node[] at (-0.75,-1.5) {$\equiv$};
\begin{scope}[shift={(0,-3)}]
\node[b] (p) at (1.5,0) {$P_2$};
\node[b] (q) at (3.5,0) {$P_1/P_2$};
\node[s] (s) at (5,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (p.west);
\draw[->] (p.east) -- (q.west);
\draw[->] (q.east) -- (s.west);
\draw[->] (2.45,0)|-(2.45,-1.1)-|(s.south);\fill (2.45,0) circle (1.4pt);
\draw[->] (s.east) -- node[above] {$Y$} (6.1,0);

\end{scope}

\end{tikzpicture}
\end{document}
```

4. Eliminação de uma malha de realimentação: $Y=P_1(X\pm P_2Y)$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (s0) at (1,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (s0.west);
\node[] at (0.73,-0.43) {$-$};
\node[b] (b0) at (2.6,0) {$P_1$};
\draw[->] (s0.east) -- (b0.west);
\draw[->] (b0.east) -- node[above] {$Y$} (4.5,0);
\fill (3.8,0) circle (1.4pt);
\node[b] (h) at (2.4,-1.25) {$P_2$};
\draw[->] (3.8,0) |- (h.east);\draw[->] (h.west) -| (s0.south);
\node[] at (-0.75,-1.4) {$\equiv$};
\begin{scope}[shift={(0,-2.8)}]
\node[b] (b0) at (1.4,0) {$\frac{P_1}{1\mp P_1P_2}$};
\draw[->] (0,0) -- node[above] {$X$} (b0.west);
\draw[->] (b0.east) -- node[above] {$Y$} (2.9,0);

\end{scope}

\end{tikzpicture}
\end{document}
```

5. Remoção de um bloco de uma malha de realimentação: $Y=P_1(X\pm P_2Y)$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (s0) at (1,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (s0.west);
\node[] at (0.73,-0.43) {$-$};
\node[b] (b0) at (2.6,0) {$P_1$};
\draw[->] (s0.east) -- (b0.west);
\draw[->] (b0.east) -- node[above] {$Y$} (4.5,0);
\fill (3.8,0) circle (1.4pt);
\node[b] (h) at (2.4,-1.25) {$P_2$};
\draw[->] (3.8,0) |- (h.east);\draw[->] (h.west) -| (s0.south);
\node[] at (-0.75,-1.4) {$\equiv$};
\begin{scope}[shift={(0,-2.8)}]
\node[b] (p) at (0.8,0) {$1/P_2$};
\begin{scope}[shift={(1.65,0)}]
\node[s] (s0) at (1,0) {$+$};
\draw[->] (0,0) -- node[above] {$$} (s0.west);
\node[] at (0.73,-0.43) {$-$};
\node[b] (b0) at (2.6,0) {$P_1P_2$};
\draw[->] (s0.east) -- (b0.west);
\draw[->] (b0.east) -- node[above] {$Y$} (4.5,0);
\fill (3.8,0) circle (1.4pt);
\draw[->] (3.8,0) |- (1,-1.25) -- (s0.south);

\end{scope}
\draw[->] (-.7,0) -- node[above] {$X$} (p.west);
\draw[->] (p.east) -- (1.65,0);

\end{scope}

\end{tikzpicture}
\end{document}
```

6a. Reorganizando os pontos de soma: $Z=W\pm X\pm Y$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (a) at (1.6,0) {$+$};
\node[s] (b) at (3.6,0) {$+$};
\draw[->] (0,0) -- node[above] {$W$} (a.west);
\draw[->] (a.east) -- (b.west);
\draw[->] (b.east) -- node[above] {$Z$} (5,0);
\draw[->] (1.6,-1) -- node[left] {$X$} (a.south);
\draw[->] (3.6,-1) -- node[left] {$Y$} (b.south);
\node[] at (1.25,-0.4) {$\pm$};
\node[] at (3.25,-0.4) {$\pm$};
\node[] at (-0.75,-1.3) {$\equiv$};
\begin{scope}[shift={(0,-2.6)}]
\node[s] (a) at (1.6,0) {$+$};
\node[s] (b) at (3.6,0) {$+$};
\draw[->] (0,0) -- node[above] {$W$} (a.west);
\draw[->] (a.east) -- (b.west);
\draw[->] (b.east) -- node[above] {$Z$} (5,0);
\draw[->] (1.6,-1) -- node[left] {$Y$} (a.south);
\draw[->] (3.6,-1) -- node[left] {$X$} (b.south);
\node[] at (1.25,-0.4) {$\pm$};
\node[] at (3.25,-0.4) {$\pm$};

\end{scope}

\end{tikzpicture}
\end{document}
```

6b. Reorganizando os pontos de soma: $Z=W\pm X\pm Y$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (a) at (1.6,0) {$+$};
\node[s] (b) at (3.6,0) {$+$};
\draw[->] (0,0) -- node[above] {$W$} (a.west);
\draw[->] (a.east) -- (b.west);
\draw[->] (b.east) -- node[above] {$Z$} (5,0);
\draw[->] (1.6,-1) -- node[left] {$X$} (a.south);
\draw[->] (3.6,-1) -- node[left] {$Y$} (b.south);
\node[] at (1.25,-0.4) {$\pm$};
\node[] at (3.25,-0.4) {$\pm$};
\node[] at (-0.75,-1.35) {$\equiv$};
\begin{scope}[shift={(0,-2.7)}]
\node[s] (a) at (3.6,0) {$+$};
\node[s] (b) at (3.6,-1.15) {$+$};
\draw[->] (0,0) -- node[above] {$W$} (a.west);
\draw[->] (0,-1.15) -- node[above] {$X$} (b.west);
\draw[->] (3.6,-2.1) -- node[left] {$Y$} (b.south);
\draw[->] (b.north) -- (a.south);
\draw[->] (a.east) -- node[above] {$Z$} (5,0);

\end{scope}

\end{tikzpicture}
\end{document}
```

7. Movendo um ponto de soma à frente de um bloco: $Z=PX\pm Y$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (p) at (1.6,0) {$P$};
\node[s] (s) at (4,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (p.west);
\draw[->] (p.east) -- (s.west);
\draw[->] (s.east) -- node[above] {$Z$} (5.3,0);
\draw[->] (4,-1.35) -- node[right] {$Y$} (s.south);
\node[] at (3.65,-0.42) {$\pm$};
\node[] at (-0.75,-1.4) {$\equiv$};
\begin{scope}[shift={(0,-2.8)}]
\node[s] (s) at (2,0) {$+$};
\node[b] (p) at (4,0) {$P$};
\draw[->] (0,0) -- node[above] {$X$} (s.west);
\draw[->] (s.east) -- (p.west);
\draw[->] (p.east) -- node[above] {$Z$} (5.4,0);
\node[b] (q) at (4,-1.35) {$1/P$};
\draw[->] (5.6,-1.35) -- node[above] {$Y$} (q.east);
\draw[->] (q.west)-|(s.south);\node[] at (1.65,-0.42) {$\pm$};

\end{scope}

\end{tikzpicture}
\end{document}
```

8. Movendo um ponto de soma para além de um bloco: $Z=P(X\pm Y)$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (s) at (2,0) {$+$};
\node[b] (p) at (4,0) {$P$};
\draw[->] (0,0) -- node[above] {$X$} (s.west);
\draw[->] (s.east) -- (p.west);
\draw[->] (p.east) -- node[above] {$Z$} (5.4,0);
\draw[->] (2,-1.35) -- node[right] {$Y$} (s.south);
\node[] at (1.65,-0.42) {$\pm$};
\node[] at (-0.75,-1.4) {$\equiv$};
\begin{scope}[shift={(0,-2.8)}]
\node[b] (p) at (1.6,0) {$P$};
\node[s] (s) at (4,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (p.west);
\draw[->] (p.east) -- (s.west);
\draw[->] (s.east) -- node[above] {$Z$} (5.3,0);
\node[b] (q) at (1.6,-1.35) {$P$};
\draw[->] (0,-1.35) -- node[above] {$Y$} (q.west);
\draw[->] (q.east)-|(s.south);\node[] at (3.65,-0.42) {$\pm$};

\end{scope}

\end{tikzpicture}
\end{document}
```

9. Movendo um ponto de tomada à frente de um bloco: $Y=PX$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (p) at (2.4,0) {$P$};
\draw[->] (0,0) -- node[above] {$X$} (p.west);
\draw[->] (p.east) -- node[above] {$Y$} (4.8,0);
\fill (3.7,0) circle (1.4pt);
\draw[->] (3.7,0)--(3.7,-1.2)--(0,-1.2) node[left] {$Y$};\node[] at (-0.75,-1.3) {$\equiv$};
\begin{scope}[shift={(0,-2.6)}]
\node[b] (p) at (2.4,0) {$P$};
\draw[->] (0,0) -- node[above] {$X$} (p.west);
\draw[->] (p.east) -- node[above] {$Y$} (4.8,0);
\fill (0.8,0) circle (1.4pt);
\node[b] (q) at (2.4,-1.2) {$P$};
\draw[->] (0.8,0)|-(q.west);\draw[->] (q.east) -- node[above] {$Y$} (4.8,-1.2);

\end{scope}

\end{tikzpicture}
\end{document}
```

10. Movendo um ponto de tomada para além de um bloco: $Y=PX$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (p) at (2.4,0) {$P$};
\draw[->] (0,0) -- node[above] {$X$} (p.west);
\draw[->] (p.east) -- node[above] {$Y$} (4.8,0);
\fill (0.8,0) circle (1.4pt);
\draw[->] (0.8,0)--(0.8,-1.2)--(0,-1.2) node[left] {$X$};\node[] at (-0.75,-1.3) {$\equiv$};
\begin{scope}[shift={(0,-2.6)}]
\node[b] (p) at (2.4,0) {$P$};
\draw[->] (0,0) -- node[above] {$X$} (p.west);
\draw[->] (p.east) -- node[above] {$Y$} (4.8,0);
\fill (3.7,0) circle (1.4pt);
\node[b] (q) at (2.1,-1.2) {$1/P$};
\draw[->] (3.7,0)|-(q.east);\draw[->] (q.west) -- node[above] {$X$} (0,-1.2);

\end{scope}

\end{tikzpicture}
\end{document}
```

11. Movendo um ponto de tomada à frente de um ponto de soma: $Z=X\pm Y$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (s) at (3,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (s.west);
\draw[->] (s.east) -- node[above] {$Z$} (5,0);
\draw[->] (3,-1.4) -- node[right] {$Y$} (s.south);
\node[] at (2.65,-0.4) {$\pm$};
\fill (4.1,0) circle (1.4pt);
\draw[->] (4.1,0)|-(4.1,-2)--(0,-2) node[left] {$Z$};\node[] at (-0.75,-1.8) {$\equiv$};
\begin{scope}[shift={(0,-3.6)}]
\node[s] (s) at (3,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (s.west);
\draw[->] (s.east) -- node[above] {$Z$} (5,0);
\draw[->] (3,-1.4) -- node[right] {$Y$} (s.south);
\node[] at (2.65,-0.4) {$\pm$};
\fill (1.1,0) circle (1.4pt);
\node[s] (q) at (1.4,-2) {$+$};
\draw[->] (1.1,0)|-(q.east);\draw[->] (3,-1.4)|-(3,-2.8)-|(q.south);\fill (3,-1.4) circle (1.4pt);
\draw[->] (q.west) -- node[above] {$Z$} (0,-2);
\node[] at (1.7,-2.42) {$\pm$};

\end{scope}

\end{tikzpicture}
\end{document}
```

12. Movendo um ponto de tomada para além de um ponto de soma: $Z=X\pm Y$.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (s) at (3,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (s.west);
\draw[->] (s.east) -- node[above] {$Z$} (5,0);
\draw[->] (3,-1.4) -- node[right] {$Y$} (s.south);
\node[] at (2.65,-0.4) {$\pm$};
\fill (1.1,0) circle (1.4pt);
\draw[->] (1.1,0)|-(1.1,-2)--(0,-2) node[left] {$X$};\node[] at (-0.75,-1.8) {$\equiv$};
\begin{scope}[shift={(0,-3.6)}]
\node[s] (s) at (3,0) {$+$};
\draw[->] (0,0) -- node[above] {$X$} (s.west);
\draw[->] (s.east) -- node[above] {$Z$} (5,0);
\draw[->] (3,-1.4) -- node[right] {$Y$} (s.south);
\node[] at (2.65,-0.4) {$\pm$};
\fill (4.1,0) circle (1.4pt);
\node[s] (q) at (1.4,-2) {$+$};
\draw[->] (4.1,0)|-(q.east);\draw[->] (3,-1.4)|-(3,-2.8)-|(q.south);\fill (3,-1.4) circle (1.4pt);
\draw[->] (q.west) -- node[above] {$X$} (0,-2);
\node[] at (1.7,-2.42) {$\mp$};

\end{scope}

\end{tikzpicture}
\end{document}
```

## Diagrama de fluxo

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (b0) at (1.4,0) {$G$};
\draw[->] (0,0) -- node[above] {$$} (b0.west);
\draw[->] (b0.east) -- node[above] {$$} (2.9,0);
\node[] at (3.8,0) {$\equiv$};
\node[s] (a) at (4.7,0) {};
\node[s] (b) at (6.6,0) {};
\draw[->] (a.east) -- node[above] {$G$} (b.west);
\node[] at (6.6,-0.45) {sinal};

\end{tikzpicture}
\end{document}
```

Fórmula geral (Mason):

$$
\boxed{\frac{C(s)}{R(s)}=\frac{\sum_k T_k\Delta_k}{\Delta}}
$$

- $T_k$: ganho do caminho direto $k$.
- $\Delta_k$: determinante considerando os laços que não tocam o caminho direto $k$.
- $k$: índice dos caminhos diretos.

$$
\Delta=1-\sum G_L+\sum G_{L\,2\times2}-\sum G_{L\,3\times3}+\cdots
$$

Ganhos dos laços; produtos dos ganhos dos laços que não se tocam dois a dois, três a três etc.

## Estabilidade

### Critério de Routh-Hurwitz

Polinômio do exemplo:

$$
a_4s^4+a_3s^3+a_2s^2+a_1s+a_0
$$

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[b] (p) at (3.6,0) {$a_4s^4+a_3s^3+a_2s^2+a_1s+a_0$};
\draw[->] (-.2,0) -- node[above] {$R(s)$} (p.west);
\draw[->] (p.east) -- node[above] {$C(s)$} (7.4,0);

\end{tikzpicture}
\end{document}
```

| Potência | 1ª coluna | 2ª coluna | 3ª coluna |
|---|---|---|---|
| $s^4$ | $a_4$ | $a_2$ | $a_0$ |
| $s^3$ | $a_3$ | $a_1$ | $0$ |
| $s^2$ | $b_3$ | $b_2=a_0$ | $b_1=0$ |
| $s^1$ | $c_3$ | $c_2=0$ | $c_1=0$ |
| $s^0$ | $d_3$ | $d_2=0$ | $d_1=0$ |

$$
\begin{aligned}
b_3&=-\frac{\begin{vmatrix}a_4&a_2\\a_3&a_1\end{vmatrix}}{a_3},&b_2&=-\frac{\begin{vmatrix}a_4&a_0\\a_3&0\end{vmatrix}}{a_3}=a_0\\
b_1&=-\frac{\begin{vmatrix}a_4&0\\a_3&0\end{vmatrix}}{a_3}=0\\
c_3&=-\frac{\begin{vmatrix}a_3&a_1\\b_3&b_2\end{vmatrix}}{b_3},&c_2&=-\frac{\begin{vmatrix}a_3&0\\b_3&0\end{vmatrix}}{b_3}=0\\
d_3&=-\frac{\begin{vmatrix}b_3&b_2\\c_3&c_2\end{vmatrix}}{c_3}
\end{aligned}
$$

Analisamos as mudanças de sinal na primeira coluna: $a_4,\ a_3,\ b_3,\ c_3,\ d_3$. Se houver mudanças, existem polos no SPD (semiplano direito).

### Caso especial: linha de zeros

$$
P(s)=20s^5+8s^4+5s^3+6s^2+1
$$

| Potência | 1ª coluna | 2ª coluna | 3ª coluna |
|---|---:|---:|---:|
| $s^5$ | 20 | 5 | 0 |
| $s^4$ | 8 | 6 | 1 |
| $s^3$ | -10 | $-5/2$ | 0 |
| $s^2$ | 4 | 1 | 0 |
| $s^1$ | 0 | 0 | 0 |
| $s^0$ | | | |

$$
\begin{aligned}
b_3&=-\frac{\begin{vmatrix}20&5\\8&6\end{vmatrix}}8=-10,&b_2&=-\frac{\begin{vmatrix}20&0\\8&1\end{vmatrix}}8=-5/2\\
c_3&=-\frac{\begin{vmatrix}8&6\\-10&-5/2\end{vmatrix}}{-10}=4,&c_2&=1\\
d_3&=-\frac{\begin{vmatrix}-10&-5/2\\4&1\end{vmatrix}}4=0
\end{aligned}
$$

1º Pega a linha acima (par): $P_{aux}(s)=4s^2+1=0$.

2º Deriva ela; esse valor é a nova linha de zeros:

$$
\frac{dP_{aux}(s)}{ds}=8s
$$

| Potência | 1ª coluna | 2ª coluna | 3ª coluna |
|---|---:|---:|---:|
| $s^5$ | 20 | 5 | 0 |
| $s^4$ | 8 | 6 | 1 |
| $s^3$ | -10 | $-5/2$ | 0 |
| $s^2$ | 4 | 1 | 0 |
| $s^1$ | 8 | 0 | 0 |
| $s^0$ | 1 | 0 | 0 |

Duas mudanças de sinal: $8\rightarrow-10$ e $-10\rightarrow4$.

Polinômio geral: 2 SPD, 1 SPE (semiplano esquerdo), 2 no eixo $j\omega$.

**Exemplo:**

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth,line width=.65pt, every node/.style={font=\small}, b/.style={draw,minimum width=1.1cm,minimum height=.62cm,inner sep=4pt},s/.style={draw,circle,inner sep=0pt,minimum size=5mm}]
\node[s] (s0) at (1,0) {$+$};
\draw[->] (0,0) -- node[above] {$R$} (s0.west);
\node[] at (0.73,-0.43) {$-$};
\node[b] (b0) at (2.6,0) {$\frac{K}{s(s+7)(s+11)}$};
\draw[->] (s0.east) -- (b0.west);
\draw[->] (b0.east) -- node[above] {$C$} (4.5,0);
\fill (3.8,0) circle (1.4pt);
\draw[->] (3.8,0) |- (1,-1.25) -- (s0.south);

\end{tikzpicture}
\end{document}
```

Malha fechada:

$$
G(s)=\frac K{s^3+18s^2+77s+K}
$$

| Potência | 1ª coluna | 2ª coluna |
|---|---|---|
| $s^3$ | 1 | 77 |
| $s^2$ | 18 | $K$ |
| $s^1$ | $(1386-K)/18$ | 0 |
| $s^0$ | $K$ | 0 |

**Estável:**

$$
\frac{1386-K}{18}>0\Rightarrow K<1386
$$

**Instável:**

$$
\frac{1386-K}{18}<0\Rightarrow K>1386
$$

**Marginalmente estável (limiar da estabilidade):**

$$
\frac{1386-K}{18}=0\Rightarrow K=1386
$$

> Obs.: considerando $K>0$, a faixa estável completa é $0<K<1386$.
