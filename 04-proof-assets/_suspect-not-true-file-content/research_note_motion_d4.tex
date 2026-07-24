bash -lc python - <<'PY'
from pathlib import Path
p=Path('/mnt/data/research_note_motion_d4.tex')
s=p.read_text()

s=s.replace(
"The last assertion follows because $\\mu=\\tau_2\\psi_1$, $\\tau_2\\ge\\psi_1$, and the parameters are positive integers.",
"Indeed, $\\mu=\\tau_2\\psi_1$, $\\tau_2\\ge\\psi_1$, and integrality give $\\tau_2=2$ and $\\psi_1=1$; the description of the local graphs then follows from \\cite[Lemma 2.20]{Kivva2021}."
)

s=s.replace(
"Because $t\\le d$ and $m\\ge2$,\n\\begin{equation}\\label{eq:Ebound}\n E\\ge(1-6x)^{2d}\\ge1-12dm\\eps.\n\\end{equation}",
"Because $x=m\\eps\\ge\\eps$, we have $1-4x\\ge1-6x$ and $(1-\\eps)^2\\ge(1-6x)^2$. Hence\n\\[\n E\\ge(1-6x)^{2t-1}\\ge(1-6x)^{2d}.\n\\]\nBernoulli's inequality now gives\n\\begin{equation}\\label{eq:Ebound}\n E\\ge(1-6x)^{2d}\\ge1-12dm\\eps.\n\\end{equation}"
)

s=s.replace(
"Finally, suppose $c_t=t=m$. If $t<d$, then $b_t\\ge1$. Since $r\\ge t-1=m-1$, formula \\eqref{eq:basic} and the Terwilliger intersection-number inequality used in \\cite[Theorem 4.6]{Kivva2021} give\n\\[\n \\frac{k}{m}\\ge b_{t-1}\n \\ge c_{t-1}-c_t+b_t+\\lambda+2\n \\ge\\lambda+2\\ge\\frac{k}{m}+1,\n\\]",
"Finally, suppose $c_t=t=m$. If $t<d$, then $b_t\\ge1$. Since $r\\ge t-1=m-1$ and $r\\le m-1$, we have $r=m-1$ and hence $b_{t-1}\\le k/m$. Also $c_{t-1}\\ge r=m-1=c_t-1$, so $c_{t-1}-c_t+b_t\\ge0$. The Terwilliger intersection-number inequality used in \\cite[Theorem 4.6]{Kivva2021} therefore gives\n\\[\n \\frac{k}{m}\\ge b_{t-1}\n \\ge c_{t-1}-c_t+b_t+\\lambda+2\n \\ge\\lambda+2\\ge\\frac{k}{m}+1,\n\\]"
)

s=s.replace(
"The sphere-size ratios satisfy\n\\[\n \\frac{k}{c_2}>\\frac{b_1}{c_2}=\\frac{k_2}{k_1}\n \\ge\\cdots\\ge\\frac{k_d}{k_{d-1}},\n\\]\nso $k_i<Ad^3k_{i-1}$ for $i\\ge2$. Let $k_{\\max}$ be the largest nontrivial relation valency. Since $k_1\\le k_2$, it occurs at some $i\\ge2$, and",
"The sphere-size ratios satisfy\n\\[\n Ad^3>\\frac{k}{c_2}>\\frac{b_1}{c_2}=\\frac{k_2}{k_1}\n \\ge\\cdots\\ge\\frac{k_d}{k_{d-1}},\n\\]\nso $k_i<Ad^3k_{i-1}$ for $i\\ge2$. The standard inequality $b_1\\ge c_2$ for distance-regular graphs of diameter at least three gives $k_1\\le k_2$. Thus, if $k_{\\max}$ is the largest nontrivial relation valency, it occurs at some $i\\ge2$, and"
)

s=s.replace(
"Also $\\mu<\\lambda$. The common-neighbor motion bound in",
"Moreover, geometricity gives $\\lambda\\ge k/m-1$, and \\eqref{eq:geodata} then implies $\\mu<\\lambda$. The common-neighbor motion bound in"
)

old = r"""\begin{proof}[Proof of Corollary \ref{cor:all}]
Pyber and Skresanov reduce the imprimitive case to primitive halved or folded graphs, using their Propositions 2.16--2.18 and a finite list of diameter-three and diameter-four cases; see \cite[Section 3]{PyberSkresanov2025}. This reduction changes the number of vertices and the diameter by only absolute factors. More explicitly, a primitive lower bound $\gamma_r N$ at diameter $r$ enters their argument only through quantities such as $\gamma_{\lfloor d/2\rfloor}/2$, together with fixed positive constants. Substituting
\[
 \gamma_r=\frac{1}{4800r^4}
\]
therefore preserves the exponent four. The same case analysis tracks the exceptional families and adds only the crown graphs.

Finally, the diameter of a distance-regular graph of valency greater than two is at most $5\log_2 n$ \cite[Proposition 2.1]{PyberSkresanov2025}. Substitution gives the logarithmic form.
\end{proof}"""
new = r"""\begin{proof}[Proof of Corollary \ref{cor:all}]
Pyber and Skresanov reduce the imprimitive case to primitive halved or folded graphs, using their Propositions 2.16--2.18 and a finite list of diameter-three and diameter-four cases; see \cite[Section 3]{PyberSkresanov2025}. Their reduction is stated for an arbitrary primitive lower-bound function $\gamma_r$. In their notation it introduces
\[
 \gamma'_s=\frac{\gamma_{\lfloor s/2\rfloor}}2
\]
and concludes with the minimum of terms of the form
\[
 \gamma_d,\quad \gamma'_d,\quad
 \gamma'_{\lfloor d/2\rfloor},\quad
 \gamma_{\lfloor d/2\rfloor},
\]
together with fixed positive constants arising from the small-diameter cases. Define $\gamma_r=1/(4800r^4)$ for $r\ge3$ and absorb the diameter-two case into a fixed positive $\gamma_2$. Every displayed term is then at least $C/d^4$ for an absolute $C>0$. Thus their case analysis is exponent-preserving. It also tracks the exceptional families and adds only the crown graphs.

Finally, the diameter of a distance-regular graph of valency greater than two is at most $5\log_2 n$ \cite[Proposition 2.1]{PyberSkresanov2025}. Substitution gives the logarithmic form.
\end{proof}"""
if old not in s:
    raise SystemExit('imprimitive proof block not found')
s=s.replace(old,new)

s=s.replace(
"The calculations above have been checked symbolically and against the published proof structure, but the argument has not been vetted by specialists.",
"The scalar inequalities above have been checked symbolically and by finite endpoint tests, and the argument has been compared line by line with the published proof structure. These checks do not replace expert review of the graph-theoretic inputs, and the argument has not been vetted by specialists."
)

p.write_text(s)
print('updated',p)
PY
# Show changed snippets
grep -n -E 'Indeed, \\$\\mu|Because \\$x|Finally, suppose \\$c_t|sphere-size ratios|geometricity gives|arbitrary primitive|scalar inequalities' /mnt/data/research_note_motion_d4.tex