# Unidade 1 — Sistemas de Controle II

## Lugar geométrico das raízes (LGR)

### Definição

O lugar geométrico das raízes de um sistema é a representação em um gráfico das raízes da equação característica do sistema (os polos da FT de malha fechada) para algum parâmetro do sistema que é variado.

**Exemplo:** considere um sistema de controle representado pelo seguinte diagrama de blocos:

```tikz
\begin{document}
\begin{tikzpicture}
\node[draw,circle,minimum size=7mm,inner sep=0pt] (sum) at (1.5,0) {};
\draw[->] (0,0) node[left] {$R(s)$} -- (sum.west);
\node[font=\scriptsize] at (1.03,.18) {$+$};
\node[font=\scriptsize] at (1.27,-.47) {$-$};

\node[draw,minimum width=10mm,minimum height=9mm] (gain) at (2.8,0) {$K$};
\node[draw,minimum width=23mm,minimum height=12mm] (plant) at (4.8,0) {$\frac{1}{s(s+2)}$};
\draw[->] (sum) -- (gain);
\draw[->] (gain) -- (plant);
\draw[->] (plant) -- (7.2,0) node[right] {$Y(s)$};
\fill (6.4,0) circle (1.5pt);
\draw[->] (6.4,0) -- (6.4,-1.5) -| (sum.south);
\node[font=\scriptsize,blue!70!black] at (2.8,.75) {Amplificador};
\end{tikzpicture}
\end{document}
```

**1. Malha aberta:**

$$G(s)=K\frac{N(s)}{D(s)}$$

- $N(s)$: zeros.
- $D(s)$: polos.

**2. Malha fechada:**

$$T(s)=\frac{G(s)}{1+G(s)H(s)}$$

$$D(s)+KN(s)=0,\qquad K\geq 0$$

As raízes dependem de $K$ (de $0$ a $\infty$).

**Polos dominantes:**

$$\boxed{s=-\zeta\omega_n\pm\omega_n\sqrt{1-\zeta^2}\,j}$$

- $\omega_n$: frequência angular.
- $\zeta$: coeficiente de amortecimento.

### Resposta do sistema

*Esboço da resposta transitória e do regime permanente.*

```tikz
\begin{document}
\begin{tikzpicture}[x=.95cm,y=2cm]
\draw[->] (0,0) -- (9.4,0) node[right] {$t$};
\draw[->] (0,0) -- (0,1.75) node[above] {$y(t)$};
\draw[gray,dashed] (0,1) node[left] {$1$} -- (9,1);
\draw[blue!70!black,thick] plot coordinates {(0.000,0.000) (0.151,0.046) (0.302,0.170) (0.453,0.350) (0.603,0.560) (0.754,0.778) (0.905,0.982) (1.056,1.156) (1.207,1.290) (1.358,1.378) (1.508,1.418) (1.659,1.415) (1.810,1.375) (1.961,1.308) (2.112,1.223) (2.263,1.131) (2.413,1.042) (2.564,0.963) (2.715,0.899) (2.866,0.854) (3.017,0.829) (3.168,0.823) (3.318,0.833) (3.469,0.858) (3.620,0.891) (3.771,0.929) (3.922,0.967) (4.073,1.003) (4.223,1.032) (4.374,1.055) (4.525,1.069) (4.676,1.075) (4.827,1.073) (4.978,1.065) (5.128,1.052) (5.279,1.037) (5.430,1.021) (5.581,1.005) (5.732,0.991) (5.883,0.980) (6.034,0.973) (6.184,0.969) (6.335,0.969) (6.486,0.971) (6.637,0.976) (6.788,0.982) (6.939,0.988) (7.089,0.995) (7.240,1.001) (7.391,1.007) (7.542,1.010) (7.693,1.013) (7.844,1.013) (7.994,1.013) (8.145,1.011) (8.296,1.009) (8.447,1.006) (8.598,1.003) (8.749,1.000) (8.899,0.998)};
\draw[gray,dashed] (5.8,0) -- (5.8,1.65);
\node[font=\small] at (2.8,1.56) {Transit\'orio};
\node[font=\small] at (7.6,1.56) {Regime permanente};
\node[font=\small] at (1.3,-.33) {$R(s)=1$};
\end{tikzpicture}
\end{document}
```

- $T_s$ (%): tempo de acomodação.
- $M_p$ (%): máximo sobressinal.

**Solução do sistema:**

```tikz
\begin{document}
\begin{tikzpicture}
\node[draw,circle,minimum size=7mm,inner sep=0pt] (sum) at (1.5,0) {};
\draw[->] (0,0) node[left] {$R(s)$} -- (sum.west);
\node[font=\scriptsize] at (1.03,.18) {$+$};
\node[font=\scriptsize] at (1.27,-.47) {$-$};

\node[draw,minimum width=10mm,minimum height=9mm] (gain) at (2.8,0) {$K$};
\node[draw,minimum width=23mm,minimum height=12mm] (plant) at (4.8,0) {$\frac{1}{s(s+2)}$};
\draw[->] (sum) -- (gain);
\draw[->] (gain) -- (plant);
\draw[->] (plant) -- (7.2,0) node[right] {$Y(s)$};
\fill (6.4,0) circle (1.5pt);
\draw[->] (6.4,0) -- (6.4,-1.5) -| (sum.south);
\node[font=\scriptsize,blue!70!black] at (2.8,.75) {Amplificador};
\end{tikzpicture}
\end{document}
```

$$T(s)=\frac{K}{s^2+2s+K}$$

O sistema é de segunda ordem, sendo ele estável para os valores de $K$ positivos. A equação característica de um sistema de segunda ordem é dada por:

$$\boxed{s^2+2\zeta\omega_n s+\omega_n^2=0}$$

Supondo, por exemplo, um $\zeta=0{,}707$, e comparando as equações, temos:

$$\omega_n^2=K$$

$$2\zeta\omega_n=2$$

$$\omega_n=\frac{2}{2\times0{,}707}\approx1{,}41\ \mathrm{rad/s}$$

Logo:

$$K=(1{,}41)^2\approx2$$

### Efeito nas raízes

Equação característica:

$$s^2+2s+K=0$$

- $K\to0$:

$$s^2+2s=0$$
$$s(s+2)=0$$
$$\boxed{s=0}\qquad\boxed{s=-2}$$

- $K\to1$:

$$s^2+2s+1=0$$
$$\boxed{s=-1}\quad\text{(dupla)}$$

- $K\to2$:

$$s^2+2s+2=0$$
$$s=-1\pm j$$

**Observação:** raízes reais distintas ou iguais; raízes complexas conjugadas.

Representando no plano complexo $s$:

```tikz
\begin{document}
\begin{tikzpicture}[x=1.350cm,y=1.350cm]
\draw[gray!18,very thin] (-3.00000,-1.70000) -- (-3.00000,1.70000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-1.70000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-1.70000) -- (-2.00000,1.70000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-1.70000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-1.70000) -- (-1.00000,1.70000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-1.70000) {$-1$};
\draw[gray!18,very thin] (1.00000,-1.70000) -- (1.00000,1.70000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-1.70000) {$1$};
\draw[gray!18,very thin] (-3.00000,-1.00000) -- (1.00000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-3.00000,1.00000) -- (1.00000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,1.00000) {$1j$};
\draw[->] (-3.00000,0.00000) -- (1.00000,0.00000);
\draw[->] (-0.00000,-1.70000) -- (0.00000,1.70000);
\node[font=\small,right] at (1.00000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,1.70000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-3.00000,-1.70000) rectangle (1.00000,1.70000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-1.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-1.00000,1.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-1.00000,-1.00000) {$\times$};
\node[font=\small,below left] at (-1.00000,0.00000) {$-1$};
\draw[gray,dashed] (-1.00000,-1.00000) -- (-1.00000,1.00000);
\end{tikzpicture}
\end{document}
```

### Função de transferência em malha fechada

1. Para $0<K<1$: raízes reais e distintas (constantes de tempo diferentes).
2. Para $K=1$: raízes reais iguais (sistema criticamente amortecido).
3. Para $K>1$: raízes complexas (com constante de tempo de 1 s).

Considerando o seguinte sistema representado na forma de diagrama de blocos:

```tikz
\begin{document}
\begin{tikzpicture}
\node[draw,circle,minimum size=7mm,inner sep=0pt] (sum) at (1.5,0) {};
\draw[->] (0,0) node[left] {$R(s)$} -- (sum.west);
\node[font=\scriptsize] at (1.03,.18) {$+$};
\node[font=\scriptsize] at (1.27,-.47) {$-$};

\node[draw,minimum width=19mm,minimum height=9mm] (plant) at (3.6,0) {$G(s)$};
\draw[->] (sum) -- node[above] {$E(s)$} (plant);
\draw[->] (plant) -- (6.2,0) node[right] {$Y(s)$};
\node[draw,minimum width=19mm,minimum height=9mm] (fb) at (3.6,-1.5) {$H(s)$};
\fill (5.3,0) circle (1.5pt);
\draw[->] (5.3,0) |- (fb.east);
\draw[->] (fb.west) -| (sum.south);
\end{tikzpicture}
\end{document}
```

A função de transferência do sistema em malha fechada é dada por:

$$E(s)=R(s)-H(s)Y(s)$$
$$Y(s)=E(s)G(s)$$
$$Y(s)=[R(s)-H(s)Y(s)]G(s)$$
$$Y(s)=R(s)G(s)-H(s)Y(s)G(s)$$
$$Y(s)+H(s)Y(s)G(s)=R(s)G(s)$$
$$Y(s)[1+H(s)G(s)]=R(s)G(s)$$
$$\boxed{\frac{Y(s)}{R(s)}=\frac{G(s)}{1+G(s)H(s)}}$$

O denominador corresponde à equação característica. Escrevendo a equação característica na forma complexa, temos:

$$G(s)H(s)=-1+0j$$

### Condições de módulo e fase

**1. Condição de módulo:**

$$|G(s)H(s)|=1$$

**2. Condição de fase:**

$$\angle G(s)H(s)=\pm\text{múltiplos de }180^\circ$$

> Obs.: múltiplos ímpares de $180^\circ$.

Escrevendo a função de transferência de malha aberta na forma de polos e zeros, temos:

$$G(s)H(s)=K\frac{N(s)}{D(s)}$$

$$G(s)H(s)=\frac{K(s-z_1)(s-z_2)\cdots(s-z_m)}{(s-p_1)(s-p_2)\cdots(s-p_n)}$$

Reescrevendo a condição de módulo:

$$|G(s)H(s)|=1$$

$$|G(s)H(s)|=\frac{|K||s-z_1||s-z_2|\cdots|s-z_m|}{|s-p_1||s-p_2|\cdots|s-p_n|}$$

Para $K\geq0$:

$$\frac{K|s-z_1||s-z_2|\cdots|s-z_m|}{|s-p_1||s-p_2|\cdots|s-p_n|}=1$$

### Coeficiente de ganho K

O coeficiente de ganho $K$ é dado por:

$$K=\frac{|s-p_1||s-p_2|\cdots|s-p_n|}{|s-z_1||s-z_2|\cdots|s-z_m|}$$

Considerando a equação característica, temos:

$$1+KG(s)H(s)=0$$

O valor $s_1$ é um ponto no lugar geométrico das raízes. O lado direito da equação:

$$K=-\frac{1}{G(s)H(s)}$$

Calculando o lado direito para $s_1$, isso resulta em um número real positivo.

$$G(s)H(s)=\frac{1}{s(s+2)}$$

```tikz
\begin{document}
\begin{tikzpicture}[x=1.350cm,y=1.350cm]
\draw[->] (-3.50000,0.00000) -- (1.70000,0.00000);
\draw[->] (-0.00000,-0.80000) -- (0.00000,1.10000);
\node[font=\small,right] at (1.70000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,1.10000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-3.50000,-0.80000) rectangle (1.70000,1.10000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[font=\small,below] at (-2.00000,0.00000) {$-2$};
\node[font=\small,above] at (-2.90000,0.00000) {$s_2$};
\node[font=\small,above] at (-0.90000,0.00000) {$s_1$};
\node[font=\small,above] at (0.95000,0.00000) {$s_3$};
\draw[] (-2.90000,0.00000) -- (-2.90000,0.20000);
\draw[] (-0.90000,0.00000) -- (-0.90000,0.20000);
\draw[] (0.95000,0.00000) -- (0.95000,0.20000);
\end{tikzpicture}
\end{document}
```

- Polos/zeros: 1 polo (ímpar) → número negativo.
- Polos/zeros: 2 polos (par) → número positivo. O zero é par.

```tikz
\begin{document}
\begin{tikzpicture}[x=1.350cm,y=1.350cm]
\draw[->] (-5.20000,0.00000) -- (1.70000,0.00000);
\draw[->] (-0.00000,-1.60000) -- (0.00000,1.60000);
\node[font=\small,right] at (1.70000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,1.60000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-5.20000,-1.60000) rectangle (1.70000,1.60000);
\draw[blue!70!black,very thick] (-5.20000,0.00000) -- (-4.00000,0.00000);
\draw[blue!70!black,very thick] (-2.50000,0.00000) -- (0.80000,0.00000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-4.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.50000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.80000,0.00000) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-1.35000,1.15000) {$\circ$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-1.35000,-1.15000) {$\circ$};
\node[font=\small,above] at (-4.90000,0.00000) {$s_6$};
\node[font=\small,above] at (-3.30000,0.00000) {$s_5$};
\node[font=\small,above] at (-2.00000,0.00000) {$s_4$};
\node[font=\small,above] at (-0.70000,0.00000) {$s_3$};
\node[font=\small,above] at (0.25000,0.00000) {$s_2$};
\node[font=\small,above] at (1.35000,0.00000) {$s_1$};
\node[font=\small,below] at (-4.00000,0.00000) {$p_2$};
\node[font=\small,below] at (-2.50000,0.00000) {$p_1$};
\node[font=\small,below] at (0.80000,0.00000) {$p_3$};
\node[font=\small,above] at (-1.35000,1.15000) {$z_1$};
\node[font=\small,below] at (-1.35000,-1.15000) {$z_2$};
\end{tikzpicture}
\end{document}
```

Pontos que pertencem ao LGR: $s_2,s_3,s_4,s_6$.

### Propriedades do LGR

#### 1. Número de ramos

Devemos marcar os polos e zeros de malha aberta do sistema: polo ($\times$), zero ($\circ$). O número de ramos é igual ao número $n$ de polos.

```tikz
\begin{document}
\begin{tikzpicture}[x=1.350cm,y=1.350cm]
\draw[->] (-3.00000,0.00000) -- (1.00000,0.00000);
\draw[->] (-0.00000,-0.90000) -- (0.00000,0.90000);
\node[font=\small,right] at (1.00000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,0.90000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-3.00000,-0.90000) rectangle (1.00000,0.90000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-1.00000,0.00000) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-2.00000,0.00000) {$\circ$};
\node[font=\small,below] at (-2.00000,0.00000) {$z$};
\node[font=\small,below] at (-1.00000,0.00000) {$p$};
\end{tikzpicture}
\end{document}
```

**Exemplo:** 2 ramos (quantidade de polos).

```tikz
\begin{document}
\begin{tikzpicture}[x=1.350cm,y=1.350cm]
\draw[->] (-3.00000,0.00000) -- (1.00000,0.00000);
\draw[->] (-0.00000,-0.80000) -- (0.00000,0.80000);
\node[font=\small,right] at (1.00000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,0.80000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-3.00000,-0.80000) rectangle (1.00000,0.80000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[font=\small,below] at (-2.00000,0.00000) {$-2$};
\end{tikzpicture}
\end{document}
```

#### 2. Simetria

O lugar geométrico das raízes é simétrico em relação ao eixo real, uma vez que consideramos que os modelos do sistema usados são funções racionais, ou seja, razão entre dois polinômios com coeficientes reais.

#### 3. Pontos de início e término

Esta propriedade estabelece que o lugar geométrico das raízes se origina nos polos e termina nos zeros de malha aberta, respectivamente.

**Prova:** a equação característica do sistema em malha fechada é dada por:

$$1+KG(s)H(s)=0$$

$$1+\frac{K(s-z_1)(s-z_2)\cdots(s-z_m)}{(s-p_1)(s-p_2)\cdots(s-p_n)}=0$$

Reescrevendo a equação acima, temos:

$$(s-p_1)(s-p_2)\cdots(s-p_n)+K(s-z_1)(s-z_2)\cdots(s-z_m)=0$$

O ponto de partida corresponde a $K\to0$, logo:

$$\boxed{(s-p_1)(s-p_2)\cdots(s-p_n)=0}$$

Utilizando a condição de módulo, temos:

$$|KG(s)H(s)|=1$$

$$\frac{K|s-z_1||s-z_2|\cdots|s-z_m|}{|s-p_1||s-p_2|\cdots|s-p_n|}=1$$

$$\frac{|s-z_1||s-z_2|\cdots|s-z_m|}{|s-p_1||s-p_2|\cdots|s-p_n|}=\frac{1}{K}\to0$$

O ponto de término corresponde a $K\to\infty$, logo temos:

$$\boxed{|s-z_1||s-z_2|\cdots|s-z_m|=0}$$

#### 4. Assíntotas

Se a função de transferência de malha aberta $G(s)H(s)$ possui $n-m$ zeros no infinito, ou seja, $n-m\geq1$, o lugar geométrico das raízes tende a uma assíntota quando $K\to\infty$.

As assíntotas são determinadas pelos ângulos:

$$\boxed{\alpha_i=\frac{2i+1}{n-m}\times180^\circ}$$

$$i=0,1,2,\ldots,|n-m|-1$$

**Exemplo:** $n-m=2$.

$$\alpha_0=\frac{2\times0+1}{2}\times180^\circ=90^\circ$$
$$\alpha_1=\frac{2\times1+1}{2}\times180^\circ=270^\circ$$

```tikz
\begin{document}
\begin{tikzpicture}[x=1.350cm,y=1.350cm]
\draw[gray!18,very thin] (-3.00000,-2.00000) -- (-3.00000,2.00000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-2.00000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-2.00000) -- (-2.00000,2.00000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-2.00000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-2.00000) -- (-1.00000,2.00000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-2.00000) {$-1$};
\draw[gray!18,very thin] (1.00000,-2.00000) -- (1.00000,2.00000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-2.00000) {$1$};
\draw[gray!18,very thin] (-3.00000,-2.00000) -- (1.00000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-3.00000,-1.00000) -- (1.00000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-3.00000,1.00000) -- (1.00000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,1.00000) {$1j$};
\draw[gray!18,very thin] (-3.00000,2.00000) -- (1.00000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,2.00000) {$2j$};
\draw[->] (-3.00000,0.00000) -- (1.00000,0.00000);
\draw[->] (-0.00000,-2.00000) -- (0.00000,2.00000);
\node[font=\small,right] at (1.00000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,2.00000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-3.00000,-2.00000) rectangle (1.00000,2.00000);
\draw[blue!70!black,very thick] (-2.00000,0.00000) -- (0.00000,0.00000);
\draw[gray,dashed,thick,->] (-1.00000,0.00000) -- (-1.00000,2.00000);
\node[font=\small,above right] at (-1.00000,1.40000) {$90^\circ$};
\draw[gray,dashed,thick,->] (-1.00000,0.00000) -- (-1.00000,-2.00000);
\node[font=\small,below right] at (-1.00000,-1.40000) {$270^\circ$};
\fill[black] (-1.00000,0.00000) circle[radius=1.5pt];
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[font=\small,below left] at (-1.00000,0.00000) {$\sigma$};
\end{tikzpicture}
\end{document}
```

**Caso geral:**

$$\alpha_0=\frac{1}{n-m}\times180^\circ$$
$$\alpha_1=\frac{3}{n-m}\times180^\circ$$
$$\alpha_2=\frac{5}{n-m}\times180^\circ$$

As assíntotas cruzam o eixo real em:

$$\boxed{\sigma=\frac{\sum\text{polos de }G(s)H(s)-\sum\text{zeros de }G(s)H(s)}{n-m}}$$

- Polos: $0$ e $-2$ (na anotação inferior aparece 2).
- Zeros: não tem.
- $\alpha_0=90^\circ$, $\alpha_1=270^\circ$, $n-m=2$.

$$\sigma=\frac{(0-2)-0}{2}=-1\quad\longrightarrow\quad K=1$$

Se os polos/zeros são complexos conjugados, temos:

$$\boxed{\sigma=\frac{\sum\operatorname{Re}(p_i)-\sum\operatorname{Re}(z_i)}{n-m}}$$

- Polos: $-x\pm jy$.
- Zeros: $-c\pm jy$.

#### 5. Pontos de saída e de entrada

Pontos em que as raízes da equação característica deixam de ser reais para se tornarem complexas conjugadas (ponto de saída) ou, inversamente, pontos de entrada.

**Prova:** considere a equação característica do sistema:

$$1+KG(s)H(s)=0$$

Supondo que:

$$G(s)H(s)=\frac{KN(s)}{D(s)},\qquad D(s)\neq0,\quad D(s)\geq N(s)$$

Reescrevendo a equação característica:

$$1+K\frac{N(s)}{D(s)}=0$$
$$D(s)+KN(s)=0$$
$$\boxed{K=-\frac{D(s)}{N(s)}}$$

Os pontos de saída e de entrada sobre o eixo real podem ser calculados a partir das raízes de:

$$\frac{dK}{ds}=0$$

$$-\left[\frac{D'(s)N(s)-D(s)N'(s)}{N(s)^2}\right]=0$$

$$D'(s)N(s)-D(s)N'(s)=0$$

**Exemplo:**

$$G(s)=\frac{1}{s(s+2)},\qquad H(s)=1$$
$$N(s)=1,\qquad D(s)=s^2+2s$$
$$D(s)+KN(s)=0$$
$$s^2+2s+K=0$$
$$K=-(s^2+2s)$$

Aplicando a condição $dK/ds=0$, temos:

$$[-(s^2+2s)]'=0$$
$$2s+2=0$$
$$\boxed{s=-1}$$

#### 6. Cruzamento com o eixo imaginário

Os pontos de cruzamento com o eixo imaginário são obtidos considerando $s=0\pm j\omega$.

$$D(j\omega)+KN(j\omega)=0+j\omega$$

A parte real $D(j\omega)$ e a parte imaginária $KN(j\omega)$ dependem de $K$ e $\omega$ e devem ser nulas. Portanto, a solução destas equações determina os pontos de cruzamento com o eixo imaginário.

Outra forma de determinar os pontos de cruzamento com o eixo imaginário seria utilizando o critério de estabilidade de Routh-Hurwitz.

| Potência | Primeira coluna | Segunda coluna |
|---|---|---|
| $s^n$ | $a_0$ | $a_2$ |
| $s^{n-1}$ | $a_1$ | $a_3$ |
| $s^{n-2}$ | $b_1$ | $\cdots$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $s^0$ | $g_1$ | |

Estabilidade: estável, instável ou marginalmente estável.

**Exemplo:** considere um sistema representado pela seguinte função de transferência:

$$G(s)H(s)=\frac{K}{s(s+1)(s+2)}$$

- Zeros: não tem.
- Polos: 3.
- Assíntotas: $n-m=3-0=3$.

$$\alpha_0=\frac{180^\circ}{3}=60^\circ$$
$$\alpha_1=\frac{3\times180^\circ}{3}=180^\circ$$
$$\alpha_2=\frac{5\times180^\circ}{3}=300^\circ$$

```tikz
\begin{document}
\begin{tikzpicture}[x=1.200cm,y=1.200cm]
\draw[gray!18,very thin] (-4.00000,-2.50000) -- (-4.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-2.50000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-2.50000) -- (-3.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-2.50000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-2.50000) -- (-2.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-2.50000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-2.50000) -- (-1.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-2.50000) {$-1$};
\draw[gray!18,very thin] (1.00000,-2.50000) -- (1.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-2.50000) {$1$};
\draw[gray!18,very thin] (-4.00000,-2.00000) -- (1.40000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.00000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-4.00000,-1.00000) -- (1.40000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.00000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-4.00000,1.00000) -- (1.40000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.00000,1.00000) {$1j$};
\draw[gray!18,very thin] (-4.00000,2.00000) -- (1.40000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.00000,2.00000) {$2j$};
\draw[->] (-4.00000,0.00000) -- (1.40000,0.00000);
\draw[->] (-0.00000,-2.50000) -- (0.00000,2.50000);
\node[font=\small,right] at (1.40000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,2.50000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.00000,-2.50000) rectangle (1.40000,2.50000);
\draw[gray,dashed,thick,->] (-1.00000,0.00000) -- (0.44338,2.50000);
\node[font=\small,above right] at (0.01036,1.75000) {$60^\circ$};
\draw[gray,dashed,thick,->] (-1.00000,0.00000) -- (-4.00000,0.00000);
\draw[gray,dashed,thick,->] (-1.00000,0.00000) -- (0.44338,-2.50000);
\node[font=\small,below right] at (0.01036,-1.75000) {$300^\circ$};
\fill[black] (-1.00000,0.00000) circle[radius=1.5pt];
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-1.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[font=\small,below left] at (-1.00000,0.00000) {$\sigma$};
\end{tikzpicture}
\end{document}
```

**Solução:**

Considere $s=j\omega$. Temos:

$$D(s)+KN(s)=0$$
$$D(j\omega)+KN(j\omega)=0$$
$$D(s)=s^3+3s^2+2s$$

$$(j\omega)^3+3(j\omega)^2+2(j\omega)+K=0$$
$$j^3\omega^3+3j^2\omega^2+2j\omega+K=0$$
$$-j\omega^3-3\omega^2+2j\omega+K=0$$

- Parte real: $K-3\omega^2$.
- Parte imaginária: $2\omega-\omega^3=0$.

$$K-3\omega^2=0\qquad\text{e}\qquad2\omega-\omega^3=0$$
$$\omega(2-\omega^2)=0$$

Raízes: $\omega=0$ e $\omega=\pm\sqrt2$.

Para apenas no eixo imaginário, o $\omega$ tem que ser $\omega=\pm\sqrt2$.

Pontos de cruzamento:

$$s=\pm j\sqrt2$$
$$K-3(\sqrt2)^2=0$$
$$\boxed{K=6}$$

**Utilizando o critério de Routh-Hurwitz:**

$$s^3+3s^2+2s+K=0$$

| Potência | Primeira coluna | Segunda coluna |
|---|---:|---:|
| $s^3$ | 1 | 2 |
| $s^2$ | 3 | $K$ |
| $s^1$ | $b_1$ | 0 |
| $s^0$ | $K$ | 0 |

$$b_1=-(K-6)=-K+6$$
$$0=-K+6\quad\longrightarrow\quad\boxed{K=6}$$

> Obs.: falta o divisor 3 em $b_1$; o valor de $K$ no cruzamento não muda.

Polinômio auxiliar:

$$Q(s)=3s^2+K=3s^2+6$$
$$\boxed{s=\pm\sqrt2}$$

> Obs.: os pontos são imaginários ($\pm j\sqrt2$).

#### 7. Ângulos de partida de um polo complexo e chegada de um zero complexo

Esta propriedade permite determinar a direção dos ramos na proximidade dos polos e zeros complexos conjugados.

**1. Ângulo de partida:**

$$\boxed{\phi_{p_j}=\sum_{i=1}^{m}\phi_{z_i}-\sum_{i\neq j}^{n}\phi_{p_i}\pm\text{múltiplo ímpar de }180^\circ}$$

**2. Ângulo de chegada:**

$$\boxed{\theta_{z_j}=\sum_{i=1}^{n}\theta_{p_i}-\sum_{i\neq j}^{m}\theta_{z_i}\pm\text{múltiplo ímpar de }180^\circ}$$

## Exemplo 1 — Sistema de terceira ordem sem zeros

Considere um sistema representado pela seguinte função de transferência:

$$G(s)H(s)=\frac{K}{s(s+2)(s+3)}$$

**1. Marcar os polos e zeros no plano complexo:**

- Zeros: não tem ($m=0$).
- Polos: $0,-2,-3$ ($n=3$).

```tikz
\begin{document}
\begin{tikzpicture}[x=1.350cm,y=1.350cm]
\draw[->] (-4.40000,0.00000) -- (1.20000,0.00000);
\draw[->] (-0.00000,-0.65000) -- (0.00000,0.85000);
\node[font=\small,right] at (1.20000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,0.85000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.40000,-0.65000) rectangle (1.20000,0.85000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[font=\small,below] at (-3.00000,0.00000) {$-3$};
\node[font=\small,below] at (-2.00000,0.00000) {$-2$};
\end{tikzpicture}
\end{document}
```

**a) Segmentos:**

| Segmento | Quantidade de polos e zeros à direita | Faz parte do LGR? |
|---|---:|---|
| $0$ a $+\infty$ | 0 | Não |
| $0$ a $-2$ | 1 | Sim |
| $-2$ a $-3$ | 2 | Não |
| $-3$ a $-\infty$ | 3 | Sim |

```tikz
\begin{document}
\begin{tikzpicture}[x=1.350cm,y=1.350cm]
\draw[->] (-4.40000,0.00000) -- (1.20000,0.00000);
\draw[->] (-0.00000,-0.65000) -- (0.00000,0.85000);
\node[font=\small,right] at (1.20000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,0.85000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.40000,-0.65000) rectangle (1.20000,0.85000);
\draw[blue!70!black,very thick] (-4.40000,0.00000) -- (-3.00000,0.00000);
\draw[blue!70!black,very thick] (-2.00000,0.00000) -- (0.00000,0.00000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[font=\small,below] at (-3.00000,0.00000) {$-3$};
\node[font=\small,below] at (-2.00000,0.00000) {$-2$};
\end{tikzpicture}
\end{document}
```

**2. Assíntotas:** $n-m=3-0=3$, com os seguintes ângulos:

$$\alpha_0=\frac{180^\circ}{n-m}=\frac{180^\circ}{3}=60^\circ$$
$$\alpha_1=\frac{3\times180^\circ}{n-m}=\frac{3\times180^\circ}{3}=180^\circ$$
$$\alpha_2=\frac{5\times180^\circ}{n-m}=\frac{5\times180^\circ}{3}=300^\circ$$

As assíntotas cruzam o eixo real em:

$$\sigma=\frac{\sum\text{polos de }G(s)H(s)-\sum\text{zeros de }G(s)H(s)}{n-m}$$
$$\sigma=\frac{(0-2-3)-0}{3}$$
$$\boxed{\sigma=-1{,}6}$$

```tikz
\begin{document}
\begin{tikzpicture}[x=0.938cm,y=0.938cm]
\draw[gray!18,very thin] (-4.00000,-3.20000) -- (-4.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-3.20000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-3.20000) -- (-3.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-3.20000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-3.20000) -- (-2.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-3.20000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-3.20000) -- (-1.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-3.20000) {$-1$};
\draw[gray!18,very thin] (1.00000,-3.20000) -- (1.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-3.20000) {$1$};
\draw[gray!18,very thin] (-4.70000,-3.00000) -- (1.40000,-3.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,-3.00000) {$-3j$};
\draw[gray!18,very thin] (-4.70000,-2.00000) -- (1.40000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-4.70000,-1.00000) -- (1.40000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-4.70000,1.00000) -- (1.40000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,1.00000) {$1j$};
\draw[gray!18,very thin] (-4.70000,2.00000) -- (1.40000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,2.00000) {$2j$};
\draw[gray!18,very thin] (-4.70000,3.00000) -- (1.40000,3.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,3.00000) {$3j$};
\draw[->] (-4.70000,0.00000) -- (1.40000,0.00000);
\draw[->] (-0.00000,-3.20000) -- (0.00000,3.20000);
\node[font=\small,right] at (1.40000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,3.20000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.70000,-3.20000) rectangle (1.40000,3.20000);
\draw[blue!70!black,very thick] (-4.70000,0.00000) -- (-3.00000,0.00000);
\draw[blue!70!black,very thick] (-2.00000,0.00000) -- (0.00000,0.00000);
\draw[gray,dashed,thick,->] (-1.66667,0.00000) -- (0.18085,3.20000);
\node[font=\small,above right] at (-0.37340,2.24000) {$60^\circ$};
\draw[gray,dashed,thick,->] (-1.66667,0.00000) -- (-4.70000,0.00000);
\draw[gray,dashed,thick,->] (-1.66667,0.00000) -- (0.18085,-3.20000);
\node[font=\small,below right] at (-0.37340,-2.24000) {$300^\circ$};
\fill[black] (-1.66667,0.00000) circle[radius=1.5pt];
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[font=\small,below left] at (-1.66667,0.00000) {$\sigma$};
\end{tikzpicture}
\end{document}
```

**3. Pontos de saída/entrada:**

$$D(s)+KN(s)=0$$
$$N(s)=1,\qquad D(s)=s^3+5s^2+6s$$
$$s^3+5s^2+6s+K=0$$
$$K=-(s^3+5s^2+6s)$$

Aplicando a condição $dK/ds=0$:

$$-(3s^2+10s+6)=0$$
$$3s^2+10s+6=0$$

Raízes:

$$\boxed{s=-0{,}78},\qquad s=-2{,}54$$

Só usa uma porque está dentro do LGR.

**4. Cruzamento com o eixo imaginário:**

$$s^3+5s^2+6s+K=0$$

1º método: $s=0+j\omega=j\omega$.

$$(j\omega)^3+5(j\omega)^2+6j\omega+K=0$$
$$-j\omega^3-5\omega^2+6j\omega+K=0$$

- Parte real: $K-5\omega^2$.
- Parte imaginária: $-\omega^3+6\omega$.

$$-(\omega^3-6\omega)=0$$
$$\omega(\omega^2-6)=0$$
$$\omega=0\quad\text{e}\quad\omega=\pm\sqrt6$$
$$s=\pm j\sqrt6$$

$$K-5\omega^2=0$$
$$K=5(\sqrt6)^2$$
$$\boxed{K=30}$$

Representando no plano $s$:

```tikz
\begin{document}
\begin{tikzpicture}[x=0.938cm,y=0.938cm]
\draw[gray!18,very thin] (-4.00000,-3.20000) -- (-4.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-3.20000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-3.20000) -- (-3.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-3.20000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-3.20000) -- (-2.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-3.20000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-3.20000) -- (-1.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-3.20000) {$-1$};
\draw[gray!18,very thin] (1.00000,-3.20000) -- (1.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-3.20000) {$1$};
\draw[gray!18,very thin] (-4.70000,-3.00000) -- (1.40000,-3.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,-3.00000) {$-3j$};
\draw[gray!18,very thin] (-4.70000,-2.00000) -- (1.40000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-4.70000,-1.00000) -- (1.40000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-4.70000,1.00000) -- (1.40000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,1.00000) {$1j$};
\draw[gray!18,very thin] (-4.70000,2.00000) -- (1.40000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,2.00000) {$2j$};
\draw[gray!18,very thin] (-4.70000,3.00000) -- (1.40000,3.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,3.00000) {$3j$};
\draw[->] (-4.70000,0.00000) -- (1.40000,0.00000);
\draw[->] (-0.00000,-3.20000) -- (0.00000,3.20000);
\node[font=\small,right] at (1.40000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,3.20000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.70000,-3.20000) rectangle (1.40000,3.20000);
\draw[gray,dashed,thick,->] (-1.66667,0.00000) -- (0.18085,3.20000);
\node[font=\small,above right] at (-0.37340,2.24000) {$60^\circ$};
\draw[gray,dashed,thick,->] (-1.66667,0.00000) -- (-4.70000,0.00000);
\draw[gray,dashed,thick,->] (-1.66667,0.00000) -- (0.18085,-3.20000);
\node[font=\small,below right] at (-0.37340,-2.24000) {$300^\circ$};
\fill[black] (-1.66667,0.00000) circle[radius=1.5pt];
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-3.00000,0.00000) (-4.70000,0.00000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-2.00000,0.00000) (-0.78475,0.00000) (-0.77004,0.28014) (-0.72358,0.57873) (-0.64554,0.89150) (-0.52951,1.24340) (-0.37655,1.63091) (-0.18010,2.07276) (0.07121,2.59371) (0.38055,3.20000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(0.00000,0.00000) (-0.78475,0.00000) (-0.77985,-0.16119) (-0.76501,-0.32499) (-0.72358,-0.57873) (-0.65695,-0.85161) (-0.56558,-1.14185) (-0.44746,-1.45811) (-0.29899,-1.81061) (-0.11286,-2.21576) (0.10914,-2.66967) (0.38055,-3.20000)
};
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[font=\small,below left] at (-1.66667,0.00000) {$\sigma$};
\fill[orange!80!black] (-0.78475,0.00000) circle[radius=2pt];
\node[font=\small,below left] at (-0.78475,0.00000) {$s\approx-0{,}78$};
\fill[orange!80!black] (0.00000,2.44949) circle[radius=2pt];
\node[font=\small,above right] at (0.00000,2.44949) {$j\sqrt{6}$};
\fill[orange!80!black] (0.00000,-2.44949) circle[radius=2pt];
\node[font=\small,below right] at (0.00000,-2.44949) {$-j\sqrt{6}$};
\end{tikzpicture}
\end{document}
```

**Exercício para casa:** determinar $K$ para estável e instável.

**K para o sistema ser estável — 2º método: Routh-Hurwitz.**

| Potência | Primeira coluna | Segunda coluna |
|---|---:|---:|
| $s^3$ | 1 | 6 |
| $s^2$ | 5 | $K$ |
| $s^1$ | $b_1$ | 0 |
| $s^0$ | $K$ | |

$$b_1=-\frac{K-30}{5}$$

Para o sistema ser estável, $b_1>0$ (positivo), pois não pode ter mudança de sinal.

$$-\left(\frac{K-30}{5}\right)>0$$

Multiplicando por $-1$:

$$\frac{K-30}{5}<0$$
$$K-30<0$$
$$K<30$$

Faixa de $K$ para estabilidade:

$$\boxed{0<K<30}$$

**K para o sistema ser instável — 2º método: Routh-Hurwitz.**

| Potência | Primeira coluna | Segunda coluna |
|---|---:|---:|
| $s^3$ | 1 | 6 |
| $s^2$ | 5 | $K$ |
| $s^1$ | $b_1$ | 0 |
| $s^0$ | $K$ | |

$$b_1=-\frac{K-30}{5}$$

Para o sistema ser instável, $b_1<0$ (negativo), pois tem que ter mudança de sinal.

$$-\left(\frac{K-30}{5}\right)<0$$
$$\frac{K-30}{5}>0$$
$$K-30>0$$
$$\boxed{K>30}$$

**Gabarito:**

| Estabilidade | Valores de $K$ |
|---|---|
| Estável | $0<K<30$ |
| Instável | $K>30$ |
| Marginalmente estável | $K=30$ |

**K para o sistema ser marginalmente estável**

2º método: Routh-Hurwitz.

| Potência | Primeira coluna | Segunda coluna |
|---|---:|---:|
| $s^3$ | 1 | 6 |
| $s^2$ | 5 | $K$ |
| $s^1$ | $b_1$ | 0 |
| $s^0$ | $K$ | |

$$b_1=-\frac{K-30}{5}$$

Para operar marginalmente estável, $b_1=0$.

$$0=-\frac{K-30}{5}$$
$$\boxed{K=30}$$

Polinômio auxiliar:

$$Q(s)=5s^2+30=0$$
$$s=\pm\sqrt{\frac{30}{5}}$$
$$\boxed{s=\pm\sqrt6}$$

> Obs.: os pontos são imaginários ($\pm j\sqrt6$).

## Exemplo 2 — Adição de um zero em (s + 1)

Adicionando um zero em $(s+1)$, temos:

$$G(s)H(s)=\frac{(s+1)K}{s(s+2)(s+3)}$$

- Zero: $z=-1$.
- Polos: $p=0,-2,-3$.

**1. Marcar os polos e zeros no plano complexo $s$:**

```tikz
\begin{document}
\begin{tikzpicture}[x=1.350cm,y=1.350cm]
\draw[->] (-4.40000,0.00000) -- (1.20000,0.00000);
\draw[->] (-0.00000,-0.65000) -- (0.00000,0.85000);
\node[font=\small,right] at (1.20000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,0.85000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.40000,-0.65000) rectangle (1.20000,0.85000);
\draw[blue!70!black,very thick] (-3.00000,0.00000) -- (-2.00000,0.00000);
\draw[blue!70!black,very thick] (-1.00000,0.00000) -- (0.00000,0.00000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-1.00000,0.00000) {$\circ$};
\node[font=\small,below] at (-3.00000,0.00000) {$-3$};
\node[font=\small,below] at (-2.00000,0.00000) {$-2$};
\node[font=\small,below] at (-1.00000,0.00000) {$-1$};
\end{tikzpicture}
\end{document}
```

**a) Segmentos:**

- $0$ a $+\infty$, $-1$ a $-2$, $-3$ a $-\infty$: não fazem parte do LGR.
- $0$ a $-1$ e $-2$ a $-3$: fazem parte do LGR.

**2. Assíntotas:** $n-m=3-1=2$.

$$\alpha_0=\frac{180^\circ}{2}=90^\circ$$
$$\alpha_1=\frac{3\times180^\circ}{2}=270^\circ$$

As assíntotas cruzam o eixo real em:

$$\sigma=\frac{\sum\text{polos}-\sum\text{zeros}}{n-m}$$
$$\sigma=\frac{-5-(-1)}{2}=-2$$

```tikz
\begin{document}
\begin{tikzpicture}[x=1.200cm,y=1.200cm]
\draw[gray!18,very thin] (-4.00000,-2.50000) -- (-4.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-2.50000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-2.50000) -- (-3.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-2.50000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-2.50000) -- (-2.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-2.50000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-2.50000) -- (-1.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-2.50000) {$-1$};
\draw[gray!18,very thin] (1.00000,-2.50000) -- (1.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-2.50000) {$1$};
\draw[gray!18,very thin] (-4.60000,-2.00000) -- (1.40000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-4.60000,-1.00000) -- (1.40000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-4.60000,1.00000) -- (1.40000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,1.00000) {$1j$};
\draw[gray!18,very thin] (-4.60000,2.00000) -- (1.40000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,2.00000) {$2j$};
\draw[->] (-4.60000,0.00000) -- (1.40000,0.00000);
\draw[->] (-0.00000,-2.50000) -- (0.00000,2.50000);
\node[font=\small,right] at (1.40000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,2.50000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.60000,-2.50000) rectangle (1.40000,2.50000);
\draw[blue!70!black,very thick] (-3.00000,0.00000) -- (-2.00000,0.00000);
\draw[blue!70!black,very thick] (-1.00000,0.00000) -- (0.00000,0.00000);
\draw[gray,dashed,thick,->] (-2.00000,0.00000) -- (-2.00000,2.50000);
\node[font=\small,above right] at (-2.00000,1.75000) {$90^\circ$};
\draw[gray,dashed,thick,->] (-2.00000,0.00000) -- (-2.00000,-2.50000);
\node[font=\small,below right] at (-2.00000,-1.75000) {$270^\circ$};
\fill[black] (-2.00000,0.00000) circle[radius=1.5pt];
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-1.00000,0.00000) {$\circ$};
\node[font=\small,below left] at (-2.00000,0.00000) {$\sigma$};
\end{tikzpicture}
\end{document}
```

**3. Pontos de saída e entrada:** a equação característica do sistema é dada por:

$$D(s)+KN(s)=0$$
$$D(s)=s(s+2)(s+3),\qquad N(s)=s+1$$

$$s^3+5s^2+6s+K(s+1)=0$$
$$K=-\left[\frac{s^3+5s^2+6s}{s+1}\right]$$

Aplicando $dK/ds=0$, temos:

$$\frac{dK}{ds}=-\left[\frac{(3s^2+10s+6)(s+1)-(s^3+5s^2+6s)(1)}{(s+1)^2}\right]=0$$

$$3s^3+3s^2+10s^2+10s+6s+6-s^3-5s^2-6s=0$$
$$2s^3+8s^2+10s+6=0$$

Raízes (como anotadas):

$$\boxed{s=-2{,}46},\qquad s=-0{,}76\pm0{,}79j$$

O LGR é dado por:

```tikz
\begin{document}
\begin{tikzpicture}[x=0.938cm,y=0.938cm]
\draw[gray!18,very thin] (-4.00000,-3.20000) -- (-4.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-3.20000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-3.20000) -- (-3.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-3.20000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-3.20000) -- (-2.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-3.20000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-3.20000) -- (-1.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-3.20000) {$-1$};
\draw[gray!18,very thin] (1.00000,-3.20000) -- (1.00000,3.20000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-3.20000) {$1$};
\draw[gray!18,very thin] (-4.60000,-3.00000) -- (1.40000,-3.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,-3.00000) {$-3j$};
\draw[gray!18,very thin] (-4.60000,-2.00000) -- (1.40000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-4.60000,-1.00000) -- (1.40000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-4.60000,1.00000) -- (1.40000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,1.00000) {$1j$};
\draw[gray!18,very thin] (-4.60000,2.00000) -- (1.40000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,2.00000) {$2j$};
\draw[gray!18,very thin] (-4.60000,3.00000) -- (1.40000,3.00000);
\node[font=\small,left,font=\scriptsize] at (-4.60000,3.00000) {$3j$};
\draw[->] (-4.60000,0.00000) -- (1.40000,0.00000);
\draw[->] (-0.00000,-3.20000) -- (0.00000,3.20000);
\node[font=\small,right] at (1.40000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,3.20000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.60000,-3.20000) rectangle (1.40000,3.20000);
\draw[gray,dashed,thick,->] (-2.00000,0.00000) -- (-2.00000,3.20000);
\node[font=\small,above right] at (-2.00000,2.24000) {$90^\circ$};
\draw[gray,dashed,thick,->] (-2.00000,0.00000) -- (-2.00000,-3.20000);
\node[font=\small,below right] at (-2.00000,-2.24000) {$270^\circ$};
\fill[black] (-2.00000,0.00000) circle[radius=1.5pt];
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-3.00000,0.00000) (-2.46557,0.00000) (-2.45470,0.28826) (-2.42163,0.59222) (-2.37926,0.85692) (-2.24237,1.60700) (-2.17319,2.09709) (-2.12395,2.60859) (-2.08755,3.20000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-2.00000,0.00000) (-2.46557,0.00000) (-2.45470,-0.28826) (-2.42163,-0.59222) (-2.37926,-0.85692) (-2.24237,-1.60700) (-2.17319,-2.09709) (-2.12395,-2.60859) (-2.08755,-3.20000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(0.00000,0.00000) (-0.99998,0.00000)
};
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-1.00000,0.00000) {$\circ$};
\node[font=\small,below left] at (-2.00000,0.00000) {$\sigma$};
\fill[orange!80!black] (-2.46557,0.00000) circle[radius=2pt];
\node[font=\small,below left] at (-2.46557,0.00000) {$s\approx-2{,}46$};
\end{tikzpicture}
\end{document}
```

**Para casa: simular malha fechada.**

$$G(s)H(s)=\frac{1}{s(s+2)(s+3)}$$
$$G(s)H(s)=\frac{s+1}{s(s+2)(s+3)}$$
$$R(s)=\frac{1}{s}\quad\text{e}\quad\frac{1}{s^2}$$

## Exemplo 3 — Adição de dois zeros em (s − 2)²

$$G(s)H(s)=\frac{K(s-2)^2}{s(s+2)(s+3)}$$

**1. Polos e zeros:**

```tikz
\begin{document}
\begin{tikzpicture}[x=1.266cm,y=1.266cm]
\draw[->] (-4.60000,0.00000) -- (3.30000,0.00000);
\draw[->] (-0.00000,-0.65000) -- (0.00000,1.05000);
\node[font=\small,right] at (3.30000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,1.05000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.60000,-0.65000) rectangle (3.30000,1.05000);
\draw[blue!70!black,very thick] (-4.60000,0.00000) -- (-3.00000,0.00000);
\draw[blue!70!black,very thick] (-2.00000,0.00000) -- (0.00000,0.00000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (2.00000,0.00000) {$\circ$};
\node[font=\small,above right] at (2.00000,0.00000) {$m=2$};
\node[font=\small,below] at (-3.00000,0.00000) {$-3$};
\node[font=\small,below] at (-2.00000,0.00000) {$-2$};
\node[font=\small,below] at (2.00000,0.00000) {$2$};
\end{tikzpicture}
\end{document}
```

- $0$ a $+\infty$ e $-2$ a $-3$: não fazem parte do LGR.
- $0$ a $-2$ e $-3$ a $-\infty$: fazem parte do LGR.

**2. Assíntotas:** $n-m=1$.

$$\alpha_0=\frac{180^\circ}{1}\quad\longrightarrow\quad\boxed{\alpha_0=180^\circ}$$

**3. Pontos de saída/entrada:**

$$s^3+5s^2+6s+K(s^2-4s+4)=0$$
$$K=-\left(\frac{s^3+5s^2+6s}{s^2-4s+4}\right)$$
$$-(s^4-8s^3-14s^2+40s+24)=0$$

Raízes (conforme manuscrito):

$$9{,}27,\quad2,\quad\boxed{-0{,}53},\quad-2{,}49$$

```tikz
\begin{document}
\begin{tikzpicture}[x=1.111cm,y=1.111cm]
\draw[gray!18,very thin] (-4.00000,-2.70000) -- (-4.00000,2.70000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-2.70000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-2.70000) -- (-3.00000,2.70000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-2.70000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-2.70000) -- (-2.00000,2.70000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-2.70000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-2.70000) -- (-1.00000,2.70000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-2.70000) {$-1$};
\draw[gray!18,very thin] (1.00000,-2.70000) -- (1.00000,2.70000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-2.70000) {$1$};
\draw[gray!18,very thin] (2.00000,-2.70000) -- (2.00000,2.70000);
\node[font=\small,below,font=\scriptsize] at (2.00000,-2.70000) {$2$};
\draw[gray!18,very thin] (3.00000,-2.70000) -- (3.00000,2.70000);
\node[font=\small,below,font=\scriptsize] at (3.00000,-2.70000) {$3$};
\draw[gray!18,very thin] (-4.70000,-2.00000) -- (3.50000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-4.70000,-1.00000) -- (3.50000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-4.70000,1.00000) -- (3.50000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,1.00000) {$1j$};
\draw[gray!18,very thin] (-4.70000,2.00000) -- (3.50000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.70000,2.00000) {$2j$};
\draw[->] (-4.70000,0.00000) -- (3.50000,0.00000);
\draw[->] (-0.00000,-2.70000) -- (0.00000,2.70000);
\node[font=\small,right] at (3.50000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,2.70000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.70000,-2.70000) rectangle (3.50000,2.70000);
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-3.00000,0.00000) (-4.70000,0.00000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-2.00000,0.00000) (-0.59782,0.00000) (-0.53209,0.03877) (-0.52041,0.15314) (-0.49338,0.27134) (-0.45246,0.38453) (-0.39556,0.49763) (-0.34211,0.58103) (-0.27782,0.66399) (-0.20543,0.74201) (-0.12864,0.81188) (-0.03361,0.88438) (0.06703,0.94779) (0.17285,1.00225) (0.28330,1.04764) (0.40314,1.08512) (0.52050,1.11093) (0.63962,1.12673) (0.75921,1.13232) (0.87788,1.12773) (0.99961,1.11225) (1.11701,1.08644) (1.23341,1.04942) (1.34178,1.00353) (1.44498,0.94802) (1.54081,0.88419) (1.63052,0.81114) (1.71126,0.73113) (1.78498,0.64185) (1.84774,0.54782) (1.89956,0.45005) (1.94137,0.34699) (1.97244,0.23948) (1.99189,0.13045) (1.99981,0.02000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(0.00000,0.00000) (-0.47214,0.00000) (-0.53209,-0.03877) (-0.51746,-0.17022) (-0.48414,-0.30096) (-0.43282,-0.42751) (-0.36027,-0.55448) (-0.26606,-0.67763) (-0.15472,-0.78942) (-0.02426,-0.89081) (0.11680,-0.97484) (0.26727,-1.04172) (0.42531,-1.09079) (0.58843,-1.12120) (0.75353,-1.13229) (0.87227,-1.12818) (0.99415,-1.11318) (1.11179,-1.08783) (1.22850,-1.05122) (1.33725,-1.00569) (1.44089,-0.95046) (1.53721,-0.88683) (1.62745,-0.81389) (1.70873,-0.73389) (1.78300,-0.64450) (1.84629,-0.55025) (1.89857,-0.45217) (1.94077,-0.34870) (1.97215,-0.24070) (1.99180,-0.13113) (1.99981,-0.02000)
};
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (2.00000,0.00000) {$\circ$};
\node[font=\small,above right] at (2.00000,0.00000) {$m=2$};
\fill[orange!80!black] (-0.53000,0.00000) circle[radius=2pt];
\node[font=\small,below left] at (-0.53000,0.00000) {$s\approx-0{,}53$};
\end{tikzpicture}
\end{document}
```

**4. Cruzamento com o eixo imaginário**

$$s^3+5s^2+6s+K(s^2-4s+4)=0$$
$$s^3+5s^2+6s+Ks^2-4Ks+4K=0$$

Substituindo $s=j\omega$:

$$(j\omega)^3+5(j\omega)^2+6j\omega+K(j\omega)^2-4K(j\omega)+4K=0$$
$$-j\omega^3-5\omega^2+6j\omega-K\omega^2-4Kj\omega+4K=0$$

Parte real:

$$-5\omega^2-K\omega^2+4K=0$$

Parte imaginária:

$$-\omega^3+6\omega-4K\omega=0$$

**Exercício para casa:** encontrar $K$ e $\omega$.

$$s^3+(K+5)s^2+(6-4K)s+4K=0$$

| Potência | Primeira coluna | Segunda coluna |
|---|---|---|
| $s^3$ | 1 | $6-4K$ |
| $s^2$ | $K+5$ | $4K$ |
| $s^1$ | $c_1$ | |
| $s^0$ | $d_1$ | |

$$c_1=\frac{(K+5)(6-4K)-(4K\times1)}{K+5}$$
$$d_1=4K$$
$$6K-4K^2+30-20K-4K=0$$
$$-4K^2-18K+30=0$$
$$\boxed{K=1{,}29},\qquad K=-5{,}79$$

$$Q(s)=(K+5)s^2+4K=6{,}29s^2+5{,}16$$

Raízes: $s\approx\pm0{,}9j$.

## Exemplo 4 — Sistema com zeros complexos

Considere um sistema representado pela seguinte função de transferência e esboce o LGR:

$$G(s)H(s)=\frac{K(s^2+6s+5)}{s(s+2)^2}$$

- Zeros anotados: $z=-3\pm1{,}73j$ ($m=2$).
- Polos: $0,-2,-2$ ($n=3$).

**Solução:**

**1. Marcar polos e zeros:**

```tikz
\begin{document}
\begin{tikzpicture}[x=0.896cm,y=0.896cm]
\draw[gray!18,very thin] (-5.00000,-3.35000) -- (-5.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-5.00000,-3.35000) {$-5$};
\draw[gray!18,very thin] (-4.00000,-3.35000) -- (-4.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-3.35000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-3.35000) -- (-3.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-3.35000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-3.35000) -- (-2.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-3.35000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-3.35000) -- (-1.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-3.35000) {$-1$};
\draw[gray!18,very thin] (1.00000,-3.35000) -- (1.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-3.35000) {$1$};
\draw[gray!18,very thin] (-5.40000,-3.00000) -- (1.00000,-3.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,-3.00000) {$-3j$};
\draw[gray!18,very thin] (-5.40000,-2.00000) -- (1.00000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-5.40000,-1.00000) -- (1.00000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-5.40000,1.00000) -- (1.00000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,1.00000) {$1j$};
\draw[gray!18,very thin] (-5.40000,2.00000) -- (1.00000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,2.00000) {$2j$};
\draw[gray!18,very thin] (-5.40000,3.00000) -- (1.00000,3.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,3.00000) {$3j$};
\draw[->] (-5.40000,0.00000) -- (1.00000,0.00000);
\draw[->] (-0.00000,-3.35000) -- (0.00000,3.35000);
\node[font=\small,right] at (1.00000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,3.35000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-5.40000,-3.35000) rectangle (1.00000,3.35000);
\draw[blue!70!black,very thick] (-5.40000,0.00000) -- (0.00000,0.00000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[font=\small,above left] at (-2.00000,0.00000) {$\times 2$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-3.00000,1.73205) {$\circ$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-3.00000,-1.73205) {$\circ$};
\draw[gray,dotted] (-3.00000,1.73205) -- (0.00000,1.73205);
\draw[gray,dotted] (-3.00000,-1.73205) -- (-0.00000,-1.73205);
\end{tikzpicture}
\end{document}
```

- $0$ a $+\infty$: não faz parte do LGR.
- $0$ a $-2$ e $-2$ a $+\infty$: faz parte do LGR (como escrito).

> Obs.: no gráfico, o segundo intervalo é $-2$ a $-\infty$.

**2. Assíntotas: $n-m=3-2=1$, somente uma assíntota em $180^\circ$.**

$$\boxed{\alpha_0=180^\circ}$$

**3. Pontos de saída/entrada:**

$$D(s)+KN(s)=0$$
$$s^3+4s^2+4s+K(s^2+6s+12)=0$$
$$K=-\left[\frac{s^3+4s^2+4s}{s^2+6s+12}\right]$$

Aplicando $dK/ds=0$.

$$0=-\left[\frac{(3s^2+8s+4)(s^2+6s+12)-(s^3+4s^2+4s)(2s+6)}{(s^2+6s+12)^2}\right]$$

$$3s^4+18s^3+36s^2+8s^3+48s^2+96s+4s^2+24s+48-2s^4-8s^3-8s^2-6s^3-24s^2-24s=0$$

$$s^4+12s^3+56s^2+96s+48=0$$

*LGR para o numerador utilizado na resolução ($s^2+6s+12$).*

```tikz
\begin{document}
\begin{tikzpicture}[x=0.896cm,y=0.896cm]
\draw[gray!18,very thin] (-5.00000,-3.35000) -- (-5.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-5.00000,-3.35000) {$-5$};
\draw[gray!18,very thin] (-4.00000,-3.35000) -- (-4.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-3.35000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-3.35000) -- (-3.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-3.35000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-3.35000) -- (-2.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-3.35000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-3.35000) -- (-1.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-3.35000) {$-1$};
\draw[gray!18,very thin] (1.00000,-3.35000) -- (1.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-3.35000) {$1$};
\draw[gray!18,very thin] (-5.40000,-3.00000) -- (1.00000,-3.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,-3.00000) {$-3j$};
\draw[gray!18,very thin] (-5.40000,-2.00000) -- (1.00000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-5.40000,-1.00000) -- (1.00000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-5.40000,1.00000) -- (1.00000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,1.00000) {$1j$};
\draw[gray!18,very thin] (-5.40000,2.00000) -- (1.00000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,2.00000) {$2j$};
\draw[gray!18,very thin] (-5.40000,3.00000) -- (1.00000,3.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,3.00000) {$3j$};
\draw[->] (-5.40000,0.00000) -- (1.00000,0.00000);
\draw[->] (-0.00000,-3.35000) -- (0.00000,3.35000);
\node[font=\small,right] at (1.00000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,3.35000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-5.40000,-3.35000) rectangle (1.00000,3.35000);
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-2.00000,0.00000) (-5.40000,0.00000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-2.00000,0.00000) (-0.92247,0.00000) (-0.85045,0.04699) (-0.84827,0.81030) (-0.86236,1.05618) (-0.88833,1.27384) (-0.93242,1.49979) (-0.99265,1.71050) (-1.07102,1.91175) (-1.16707,2.10016) (-1.29896,2.29890) (-1.45270,2.47548) (-1.53403,2.55162) (-1.62365,2.62435) (-1.80488,2.74120) (-1.90649,2.79125) (-2.00149,2.82895) (-2.19241,2.87956) (-2.28621,2.89235) (-2.38286,2.89704) (-2.48146,2.89255) (-2.58072,2.87777) (-2.67892,2.85175) (-2.75829,2.82103) (-2.84821,2.77328) (-2.91663,2.72500) (-2.97729,2.67019) (-3.03796,2.59830) (-3.08438,2.52338) (-3.11707,2.44931) (-3.14041,2.36803) (-3.15253,2.28515) (-3.15393,2.19782) (-3.14434,2.10821) (-3.12413,2.01751) (-3.09342,1.92496) (-3.05214,1.83010) (-3.00002,1.73209)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(0.00000,0.00000) (-0.77889,0.00000) (-0.85045,-0.04699) (-0.84581,-0.69164) (-0.86236,-1.05618) (-0.88253,-1.23448) (-0.91254,-1.40983) (-0.95152,-1.57464) (-0.99851,-1.72773) (-1.05934,-1.88514) (-1.13211,-2.03701) (-1.21677,-2.18157) (-1.31278,-2.31684) (-1.41091,-2.43209) (-1.52459,-2.54331) (-1.64474,-2.63993) (-1.76869,-2.72081) (-1.91972,-2.79702) (-2.07277,-2.85172) (-2.22331,-2.88466) (-2.38286,-2.89704) (-2.53110,-2.88651) (-2.67892,-2.85175) (-2.80414,-2.79861) (-2.91663,-2.72500) (-3.00937,-2.63488) (-3.08438,-2.52338) (-3.12882,-2.41361) (-3.15253,-2.28515) (-3.15052,-2.15344) (-3.12413,-2.01751) (-3.07457,-1.87893) (-3.00002,-1.73209)
};
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[font=\small,above left] at (-2.00000,0.00000) {$\times 2$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-3.00000,1.73205) {$\circ$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-3.00000,-1.73205) {$\circ$};
\fill[orange!80!black] (-0.85000,0.00000) circle[radius=2pt];
\node[font=\small,below right] at (-0.85000,0.00000) {$s\approx-0{,}85$};
\end{tikzpicture}
\end{document}
```

**4. Ângulo de chegada sobre os zeros complexos:**

$$\phi_{z_j}=\sum_{i=1}^n\theta_{p_i}-\sum_{i\neq j}^m\theta_{z_i}+180^\circ$$

```tikz
\begin{document}
\begin{tikzpicture}[x=1.250cm,y=1.250cm]
\draw[gray!18,very thin] (-4.00000,-2.30000) -- (-4.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-2.30000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-2.30000) -- (-3.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-2.30000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-2.30000) -- (-2.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-2.30000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-2.30000) -- (-1.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-2.30000) {$-1$};
\draw[gray!18,very thin] (1.00000,-2.30000) -- (1.00000,2.50000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-2.30000) {$1$};
\draw[gray!18,very thin] (-4.40000,-2.00000) -- (1.00000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.40000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-4.40000,-1.00000) -- (1.00000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.40000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-4.40000,1.00000) -- (1.00000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-4.40000,1.00000) {$1j$};
\draw[gray!18,very thin] (-4.40000,2.00000) -- (1.00000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-4.40000,2.00000) {$2j$};
\draw[->] (-4.40000,0.00000) -- (1.00000,0.00000);
\draw[->] (-0.00000,-2.30000) -- (0.00000,2.50000);
\node[font=\small,right] at (1.00000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,2.50000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-4.40000,-2.30000) rectangle (1.00000,2.50000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[font=\small,above left] at (-2.00000,0.00000) {$\times 2$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-3.00000,1.73205) {$\circ$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-3.00000,-1.73205) {$\circ$};
\node[font=\small,above] at (-0.67000,0.20000) {$\phi_{p_0}$};
\node[font=\small,right] at (-2.05000,0.70000) {$\phi_{p_1}$};
\node[font=\small,left] at (-3.00000,-0.70000) {$\theta_{z_2}=90^\circ$};
\draw[orange!80!black,thick,->] (0.00000,0.00000) -- (-3.00000,1.73205);
\draw[orange!80!black,thick,->] (-2.00000,0.00000) -- (-3.00000,1.73205);
\draw[orange!80!black,thick,->] (-3.00000,-1.73205) -- (-3.00000,1.73205);
\end{tikzpicture}
\end{document}
```

$$\phi_{p_0}=180^\circ-\arctan\left(\frac{1{,}73}{3}\right)=150{,}03^\circ$$
$$\phi_{p_1}=180^\circ-\arctan\left(\frac{1{,}73}{1}\right)=120{,}03^\circ$$
$$\phi_{z_1}=(\phi_{p_0}+2\phi_{p_1})-\theta_{z_2}+180^\circ$$
$$=(150{,}03+120{,}03+120{,}03)-90+180$$

$$\phi_{z_1}=480{,}36^\circ$$

> Obs.: o valor final anotado difere ligeiramente da soma anterior.

*Traçado para os zeros indicados na resolução; a direção de chegada é representada pelo ângulo equivalente módulo $360^\circ$.*

```tikz
\begin{document}
\begin{tikzpicture}[x=0.896cm,y=0.896cm]
\draw[gray!18,very thin] (-5.00000,-3.35000) -- (-5.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-5.00000,-3.35000) {$-5$};
\draw[gray!18,very thin] (-4.00000,-3.35000) -- (-4.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-3.35000) {$-4$};
\draw[gray!18,very thin] (-3.00000,-3.35000) -- (-3.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-3.35000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-3.35000) -- (-2.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-3.35000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-3.35000) -- (-1.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-3.35000) {$-1$};
\draw[gray!18,very thin] (1.00000,-3.35000) -- (1.00000,3.35000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-3.35000) {$1$};
\draw[gray!18,very thin] (-5.40000,-3.00000) -- (1.00000,-3.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,-3.00000) {$-3j$};
\draw[gray!18,very thin] (-5.40000,-2.00000) -- (1.00000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-5.40000,-1.00000) -- (1.00000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-5.40000,1.00000) -- (1.00000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,1.00000) {$1j$};
\draw[gray!18,very thin] (-5.40000,2.00000) -- (1.00000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,2.00000) {$2j$};
\draw[gray!18,very thin] (-5.40000,3.00000) -- (1.00000,3.00000);
\node[font=\small,left,font=\scriptsize] at (-5.40000,3.00000) {$3j$};
\draw[->] (-5.40000,0.00000) -- (1.00000,0.00000);
\draw[->] (-0.00000,-3.35000) -- (0.00000,3.35000);
\node[font=\small,right] at (1.00000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,3.35000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-5.40000,-3.35000) rectangle (1.00000,3.35000);
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-2.00000,0.00000) (-5.40000,0.00000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-2.00000,0.00000) (-0.92247,0.00000) (-0.85045,0.04699) (-0.84827,0.81030) (-0.86236,1.05618) (-0.88833,1.27384) (-0.93242,1.49979) (-0.99265,1.71050) (-1.07102,1.91175) (-1.16707,2.10016) (-1.29896,2.29890) (-1.45270,2.47548) (-1.53403,2.55162) (-1.62365,2.62435) (-1.80488,2.74120) (-1.90649,2.79125) (-2.00149,2.82895) (-2.19241,2.87956) (-2.28621,2.89235) (-2.38286,2.89704) (-2.48146,2.89255) (-2.58072,2.87777) (-2.67892,2.85175) (-2.75829,2.82103) (-2.84821,2.77328) (-2.91663,2.72500) (-2.97729,2.67019) (-3.03796,2.59830) (-3.08438,2.52338) (-3.11707,2.44931) (-3.14041,2.36803) (-3.15253,2.28515) (-3.15393,2.19782) (-3.14434,2.10821) (-3.12413,2.01751) (-3.09342,1.92496) (-3.05214,1.83010) (-3.00002,1.73209)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(0.00000,0.00000) (-0.77889,0.00000) (-0.85045,-0.04699) (-0.84581,-0.69164) (-0.86236,-1.05618) (-0.88253,-1.23448) (-0.91254,-1.40983) (-0.95152,-1.57464) (-0.99851,-1.72773) (-1.05934,-1.88514) (-1.13211,-2.03701) (-1.21677,-2.18157) (-1.31278,-2.31684) (-1.41091,-2.43209) (-1.52459,-2.54331) (-1.64474,-2.63993) (-1.76869,-2.72081) (-1.91972,-2.79702) (-2.07277,-2.85172) (-2.22331,-2.88466) (-2.38286,-2.89704) (-2.53110,-2.88651) (-2.67892,-2.85175) (-2.80414,-2.79861) (-2.91663,-2.72500) (-3.00937,-2.63488) (-3.08438,-2.52338) (-3.12882,-2.41361) (-3.15253,-2.28515) (-3.15052,-2.15344) (-3.12413,-2.01751) (-3.07457,-1.87893) (-3.00002,-1.73209)
};
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-2.00000,0.00000) {$\times$};
\node[font=\small,above left] at (-2.00000,0.00000) {$\times 2$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-3.00000,1.73205) {$\circ$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-3.00000,-1.73205) {$\circ$};
\node[font=\small,above right] at (-2.70000,2.25205) {$\phi_{z_1}$};
\draw[orange!80!black,thick,->] (-3.00000,1.73205) -- (-3.57656,2.72708);
\end{tikzpicture}
\end{document}
```

## Exemplo 5 — Sistema de quarta ordem

Esboce o gráfico do LGR para o sistema:

$$G(s)H(s)=\frac{K}{s(s+3)(s^2+6s+64)}$$

- Zeros: nenhum ($m=0$).
- Polos: $0,-3,-3\pm7{,}4j$ ($n=4$).

```tikz
\begin{document}
\begin{tikzpicture}[x=0.333cm,y=0.333cm]
\draw[gray!18,very thin] (-6.00000,-9.00000) -- (-6.00000,9.00000);
\node[font=\small,below,font=\scriptsize] at (-6.00000,-9.00000) {$-6$};
\draw[gray!18,very thin] (-4.00000,-9.00000) -- (-4.00000,9.00000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-9.00000) {$-4$};
\draw[gray!18,very thin] (-2.00000,-9.00000) -- (-2.00000,9.00000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-9.00000) {$-2$};
\draw[gray!18,very thin] (2.00000,-9.00000) -- (2.00000,9.00000);
\node[font=\small,below,font=\scriptsize] at (2.00000,-9.00000) {$2$};
\draw[gray!18,very thin] (-6.50000,-8.00000) -- (3.50000,-8.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,-8.00000) {$-8j$};
\draw[gray!18,very thin] (-6.50000,-6.00000) -- (3.50000,-6.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,-6.00000) {$-6j$};
\draw[gray!18,very thin] (-6.50000,-4.00000) -- (3.50000,-4.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,-4.00000) {$-4j$};
\draw[gray!18,very thin] (-6.50000,-2.00000) -- (3.50000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-6.50000,2.00000) -- (3.50000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,2.00000) {$2j$};
\draw[gray!18,very thin] (-6.50000,4.00000) -- (3.50000,4.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,4.00000) {$4j$};
\draw[gray!18,very thin] (-6.50000,6.00000) -- (3.50000,6.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,6.00000) {$6j$};
\draw[gray!18,very thin] (-6.50000,8.00000) -- (3.50000,8.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,8.00000) {$8j$};
\draw[->] (-6.50000,0.00000) -- (3.50000,0.00000);
\draw[->] (-0.00000,-9.00000) -- (0.00000,9.00000);
\node[font=\small,right] at (3.50000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,9.00000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-6.50000,-9.00000) rectangle (3.50000,9.00000);
\draw[blue!70!black,very thick] (-3.00000,0.00000) -- (0.00000,0.00000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,7.41620) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,-7.41620) {$\times$};
\draw[gray,dotted] (-3.00000,7.41620) -- (0.00000,7.41620);
\draw[gray,dotted] (-3.00000,-7.41620) -- (-0.00000,-7.41620);
\end{tikzpicture}
\end{document}
```

- $0$ a $+\infty$ e $-3$ a $+\infty$ não fazem parte do LGR (como anotado).
- $0$ a $-3$ faz parte do LGR.

> Obs.: o intervalo à esquerda de $-3$ não pertence ao LGR.

**2. Assíntotas:** $n-m=4$.

$$\alpha_0=\frac{180^\circ}{4}=45^\circ$$
$$\alpha_1=\frac{3\times180^\circ}{4}=135^\circ$$
$$\alpha_2=\frac{5\times180^\circ}{4}=225^\circ$$
$$\alpha_3=\frac{7\times180^\circ}{4}=315^\circ$$

As assíntotas cruzam o eixo real em:

$$\sigma=\frac{(0-3-3-3)-0}{4}=-\frac94=-2{,}25$$

```tikz
\begin{document}
\begin{tikzpicture}[x=0.333cm,y=0.333cm]
\draw[gray!18,very thin] (-6.00000,-9.00000) -- (-6.00000,9.00000);
\node[font=\small,below,font=\scriptsize] at (-6.00000,-9.00000) {$-6$};
\draw[gray!18,very thin] (-4.00000,-9.00000) -- (-4.00000,9.00000);
\node[font=\small,below,font=\scriptsize] at (-4.00000,-9.00000) {$-4$};
\draw[gray!18,very thin] (-2.00000,-9.00000) -- (-2.00000,9.00000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-9.00000) {$-2$};
\draw[gray!18,very thin] (2.00000,-9.00000) -- (2.00000,9.00000);
\node[font=\small,below,font=\scriptsize] at (2.00000,-9.00000) {$2$};
\draw[gray!18,very thin] (-6.50000,-8.00000) -- (3.50000,-8.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,-8.00000) {$-8j$};
\draw[gray!18,very thin] (-6.50000,-6.00000) -- (3.50000,-6.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,-6.00000) {$-6j$};
\draw[gray!18,very thin] (-6.50000,-4.00000) -- (3.50000,-4.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,-4.00000) {$-4j$};
\draw[gray!18,very thin] (-6.50000,-2.00000) -- (3.50000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-6.50000,2.00000) -- (3.50000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,2.00000) {$2j$};
\draw[gray!18,very thin] (-6.50000,4.00000) -- (3.50000,4.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,4.00000) {$4j$};
\draw[gray!18,very thin] (-6.50000,6.00000) -- (3.50000,6.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,6.00000) {$6j$};
\draw[gray!18,very thin] (-6.50000,8.00000) -- (3.50000,8.00000);
\node[font=\small,left,font=\scriptsize] at (-6.50000,8.00000) {$8j$};
\draw[->] (-6.50000,0.00000) -- (3.50000,0.00000);
\draw[->] (-0.00000,-9.00000) -- (0.00000,9.00000);
\node[font=\small,right] at (3.50000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,9.00000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-6.50000,-9.00000) rectangle (3.50000,9.00000);
\draw[blue!70!black,very thick] (-3.00000,0.00000) -- (0.00000,0.00000);
\draw[gray,dashed,thick,->] (-2.25000,0.00000) -- (3.50000,5.75000);
\node[font=\small,above right] at (1.77500,4.02500) {$45^\circ$};
\draw[gray,dashed,thick,->] (-2.25000,0.00000) -- (-6.50000,4.25000);
\node[font=\small,above right] at (-5.22500,2.97500) {$135^\circ$};
\draw[gray,dashed,thick,->] (-2.25000,0.00000) -- (-6.50000,-4.25000);
\node[font=\small,below right] at (-5.22500,-2.97500) {$225^\circ$};
\draw[gray,dashed,thick,->] (-2.25000,0.00000) -- (3.50000,-5.75000);
\node[font=\small,below right] at (1.77500,-4.02500) {$315^\circ$};
\fill[black] (-2.25000,0.00000) circle[radius=1.5pt];
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,7.41620) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-3.00000,-7.41620) {$\times$};
\node[font=\small,below left] at (-2.25000,0.00000) {$\sigma$};
\end{tikzpicture}
\end{document}
```

**3. Ponto de saída/entrada:**

$$D(s)+KN(s)=0$$
$$s^4+6s^3+64s^2+3s^3+18s^2+192s+K=0$$
$$s^4+9s^3+82s^2+192s+K=0$$
$$K=-[s^4+9s^3+82s^2+192s]$$

$$\frac{dK}{ds}=0\quad\longrightarrow\quad4s^3+27s^2+164s+192=0$$

Raízes anotadas:

$$\underline{-1{,}43},\qquad-2{,}65\pm5{,}13j$$

## Exemplo 6 — Sistema com malha interna e externa

Considere o seguinte sistema:

```tikz
\begin{document}
\begin{tikzpicture}
\node[draw,circle,minimum size=7mm,inner sep=0pt] (sum) at (1.5,0) {};
\draw[->] (0,0) node[left] {$R(s)$} -- (sum.west);
\node[font=\scriptsize] at (1.03,.18) {$+$};
\node[font=\scriptsize] at (1.27,-.47) {$-$};

\node[draw,minimum width=10mm,minimum height=9mm] (gain) at (2.8,0) {$K$};
\node[draw,circle,minimum size=7mm,inner sep=0pt] (inner) at (4.2,0) {};
\node[font=\scriptsize] at (3.77,.18) {$+$};
\node[font=\scriptsize] at (3.95,-.47) {$-$};
\node[draw,minimum width=23mm,minimum height=12mm] (plant) at (6,0) {$\frac{s^2+1}{s(s+2)}$};
\node[draw,minimum width=17mm,minimum height=8mm] (feedback) at (6,-1.35) {$K_t s$};
\draw[->] (sum) -- (gain);
\draw[->] (gain) -- (inner);
\draw[->] (inner) -- (plant);
\draw[->] (plant) -- (8.3,0) node[right] {$Y(s)$};
\fill (7.5,0) circle (1.5pt);
\draw[->] (7.5,0) |- (feedback.east);
\draw[->] (feedback.west) -| (inner.south);
\draw[->] (7.5,0) -- (7.5,-2.35) -| (sum.south);
\draw[dashed,gray] (3.65,-1.9) rectangle (7.75,.8);
\node[gray] at (5.7,1.05) {$T_1(s)$};
\end{tikzpicture}
\end{document}
```

$$D(s)+KN(s)=0$$

**Solução — Malha interna:**

$$G_1(s)=\frac{s^2+1}{s(s+2)},\qquad H_1(s)=K_t s$$
$$T_1(s)=\frac{G_1(s)}{1+G_1(s)H_1(s)}$$
$$T_1(s)=\frac{\frac{s^2+1}{s(s+2)}}{1+\frac{K_t s(s^2+1)}{s(s+2)}}$$
$$T_1(s)=\frac{s^2+1}{s(s+2)+K_t s(s^2+1)}$$

**Malha externa:**

$$G_2(s)=\frac{K(s^2+1)}{s(s+2)+K_t s(s^2+1)},\qquad H_2(s)=1$$
$$T_2(s)=\frac{G_2(s)}{1+G_2(s)H_2(s)}$$
$$T_2(s)=\frac{K(s^2+1)}{s(s+2)+K_t s(s^2+1)+K(s^2+1)}$$

Equação característica:

$$s(s+2)+K_t s(s^2+1)+K(s^2+1)=0$$

Considerando $K_t=1$, temos:

$$s(s+2)+s(s^2+1)+K(s^2+1)=0$$
$$s^3+s^2+3s+K(s^2+1)=0$$
$$G(s)=\frac{K(s^2+1)}{s^3+s^2+3s}$$

- Zeros: $\pm j$, $m=2$.
- Polos: $0,-0{,}5\pm1{,}65j$, $n=3$.

**1. Segmentos:** o intervalo de $-\infty$ a $0$ faz parte do LGR; de $0$ a $+\infty$ não faz parte.

```tikz
\begin{document}
\begin{tikzpicture}[x=1.250cm,y=1.250cm]
\draw[gray!18,very thin] (-3.00000,-2.40000) -- (-3.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-2.40000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-2.40000) -- (-2.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-2.40000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-2.40000) -- (-1.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-2.40000) {$-1$};
\draw[gray!18,very thin] (1.00000,-2.40000) -- (1.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-2.40000) {$1$};
\draw[gray!18,very thin] (-3.00000,-2.00000) -- (1.30000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-3.00000,-1.00000) -- (1.30000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-3.00000,1.00000) -- (1.30000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,1.00000) {$1j$};
\draw[gray!18,very thin] (-3.00000,2.00000) -- (1.30000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,2.00000) {$2j$};
\draw[->] (-3.00000,0.00000) -- (1.30000,0.00000);
\draw[->] (-0.00000,-2.40000) -- (0.00000,2.40000);
\node[font=\small,right] at (1.30000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,2.40000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-3.00000,-2.40000) rectangle (1.30000,2.40000);
\draw[blue!70!black,very thick] (-3.00000,0.00000) -- (0.00000,0.00000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-0.50000,1.65831) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-0.50000,-1.65831) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (0.00000,1.00000) {$\circ$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-0.00000,-1.00000) {$\circ$};
\end{tikzpicture}
\end{document}
```

**2. Assíntotas:** $n-m=1$.

$$\alpha_0=\frac{180^\circ}{1}=180^\circ$$

**3. Pontos de saída/entrada:** a equação característica é dada por:

$$s^3+s^2+3s+K(s^2+1)=0$$
$$K=-\left(\frac{s^3+s^2+3s}{s^2+1}\right)$$

Aplicando $dK/ds=0$:

$$\frac{(3s^2+2s+3)(s^2+1)-(s^3+s^2+3s)(2s)}{(s^2+1)^2}=0$$
$$s^4+2s+3=0$$

Raízes anotadas (leitura aproximada da foto):

$$0{,}95\pm1{,}19j,\qquad-0{,}95\pm0{,}61j$$

**4. Ângulos de partida/chegada dos polos/zeros complexos:**

```tikz
\begin{document}
\begin{tikzpicture}[x=1.250cm,y=1.250cm]
\draw[gray!18,very thin] (-3.00000,-2.40000) -- (-3.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-2.40000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-2.40000) -- (-2.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-2.40000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-2.40000) -- (-1.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-2.40000) {$-1$};
\draw[gray!18,very thin] (1.00000,-2.40000) -- (1.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-2.40000) {$1$};
\draw[gray!18,very thin] (-3.00000,-2.00000) -- (1.30000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-3.00000,-1.00000) -- (1.30000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-3.00000,1.00000) -- (1.30000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,1.00000) {$1j$};
\draw[gray!18,very thin] (-3.00000,2.00000) -- (1.30000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,2.00000) {$2j$};
\draw[->] (-3.00000,0.00000) -- (1.30000,0.00000);
\draw[->] (-0.00000,-2.40000) -- (0.00000,2.40000);
\node[font=\small,right] at (1.30000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,2.40000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-3.00000,-2.40000) rectangle (1.30000,2.40000);
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-0.50000,1.65831) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-0.50000,-1.65831) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (0.00000,1.00000) {$\circ$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-0.00000,-1.00000) {$\circ$};
\node[font=\small,above left] at (-0.50000,1.65831) {$p_1$};
\node[font=\small,below left] at (-0.50000,-1.65831) {$p_2$};
\node[font=\small,right] at (0.00000,1.00000) {$z_1$};
\node[font=\small,right] at (-0.00000,-1.00000) {$z_2$};
\draw[orange!80!black,thick,->] (0.00000,0.00000) -- (-0.50000,1.65831);
\draw[orange!80!black,thick,->] (-0.50000,-1.65831) -- (-0.50000,1.65831);
\draw[orange!80!black,thick,->] (0.00000,1.00000) -- (-0.50000,1.65831);
\draw[orange!80!black,thick,->] (-0.00000,-1.00000) -- (-0.50000,1.65831);
\end{tikzpicture}
\end{document}
```

$$\phi_{p_2}=90^\circ$$
$$\phi_{p_0}=180^\circ-\tan^{-1}\left(\frac{1{,}65}{0{,}5}\right)=106{,}86^\circ$$
$$\theta_{z_1}=180^\circ-\tan^{-1}\left(\frac{0{,}65}{0{,}5}\right)=127{,}57^\circ$$
$$\theta_{z_2}=180^\circ-\tan^{-1}\left(\frac{2{,}65}{0{,}5}\right)=100{,}68^\circ$$
$$\phi_{p_1}=(\theta_{z_1}+\theta_{z_2})-(\phi_{p_0}+\phi_{p_2})+180^\circ$$
$$\phi_{p_1}=\sum_i^m\theta_{z_i}-\sum_{i\neq j}^n\phi_{p_i}\pm180^\circ$$
$$\phi_{p_1}=(127{,}57+100{,}68)-(106{,}86+90)+180$$
$$\phi_{p_1}=211{,}4^\circ,\qquad\phi_{p_2}=-211{,}4^\circ$$

> Obs.: alguns índices e algarismos do quadro têm leitura incerta.

### Exercícios para casa

```tikz
\begin{document}
\begin{tikzpicture}[x=1.250cm,y=1.250cm]
\draw[gray!18,very thin] (-3.00000,-2.40000) -- (-3.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (-3.00000,-2.40000) {$-3$};
\draw[gray!18,very thin] (-2.00000,-2.40000) -- (-2.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (-2.00000,-2.40000) {$-2$};
\draw[gray!18,very thin] (-1.00000,-2.40000) -- (-1.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (-1.00000,-2.40000) {$-1$};
\draw[gray!18,very thin] (1.00000,-2.40000) -- (1.00000,2.40000);
\node[font=\small,below,font=\scriptsize] at (1.00000,-2.40000) {$1$};
\draw[gray!18,very thin] (-3.00000,-2.00000) -- (1.30000,-2.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,-2.00000) {$-2j$};
\draw[gray!18,very thin] (-3.00000,-1.00000) -- (1.30000,-1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,-1.00000) {$-1j$};
\draw[gray!18,very thin] (-3.00000,1.00000) -- (1.30000,1.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,1.00000) {$1j$};
\draw[gray!18,very thin] (-3.00000,2.00000) -- (1.30000,2.00000);
\node[font=\small,left,font=\scriptsize] at (-3.00000,2.00000) {$2j$};
\draw[->] (-3.00000,0.00000) -- (1.30000,0.00000);
\draw[->] (-0.00000,-2.40000) -- (0.00000,2.40000);
\node[font=\small,right] at (1.30000,0.00000) {$\mathrm{Re}$};
\node[font=\small,above] at (0.00000,2.40000) {$\mathrm{Im}$};
\node[font=\small,below right] at (0.00000,0.00000) {$0$};
\begin{scope}
\clip (-3.00000,-2.40000) rectangle (1.30000,2.40000);
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-0.50000,1.65831) (-0.59154,1.59222) (-0.67020,1.51269) (-0.73338,1.42258) (-0.77826,1.32666) (-0.80427,1.22415) (-0.80787,1.12947) (-0.79134,1.04636) (-0.75173,0.97051) (-0.70678,0.92517) (-0.64458,0.89025) (-0.56790,0.87054) (-0.47783,0.86644) (-0.36799,0.87849) (-0.24578,0.90641) (-0.11800,0.94850) (-0.00001,1.00000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(-0.50000,-1.65831) (-0.59154,-1.59222) (-0.67020,-1.51269) (-0.73338,-1.42258) (-0.77826,-1.32666) (-0.80427,-1.22415) (-0.80787,-1.12947) (-0.79134,-1.04636) (-0.75173,-0.97051) (-0.70678,-0.92517) (-0.64458,-0.89025) (-0.56790,-0.87054) (-0.47783,-0.86644) (-0.36799,-0.87849) (-0.24578,-0.90641) (-0.11800,-0.94850) (-0.00001,-1.00000)
};
\draw[blue!70!black,very thick,line join=round] plot coordinates {
(0.00000,0.00000) (-3.00000,0.00000)
};
\end{scope}
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (0.00000,0.00000) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-0.50000,1.65831) {$\times$};
\node[red!75!black,font=\large\bfseries,inner sep=0pt] at (-0.50000,-1.65831) {$\times$};
\node[blue!65!black,font=\large,inner sep=0pt] at (0.00000,1.00000) {$\circ$};
\node[blue!65!black,font=\large,inner sep=0pt] at (-0.00000,-1.00000) {$\circ$};
\node[font=\small,above left] at (-0.50000,1.65831) {$p_1$};
\node[font=\small,below left] at (-0.50000,-1.65831) {$p_2$};
\node[font=\small,above right] at (0.00000,1.00000) {$z_1$};
\node[font=\small,below right] at (-0.00000,-1.00000) {$z_2$};
\end{tikzpicture}
\end{document}
```

$$\theta_{p_0}=90^\circ,\qquad\theta_{z_2}=90^\circ$$

Exercício para casa: determinar os ângulos indicados no quadro e esboçar o lugar geométrico das raízes (índices de leitura incerta).

Exercício para casa:

- $K_t=0$ ($K\geq0$).
- $K=1$ ($K_t\geq0$).
- $K=0$ ($K_t\geq0$).

