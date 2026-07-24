bash -lc python - <<'PY'
from pathlib import Path
p=Path('/mnt/data/research_note_motion_d4.tex')
s=p.read_text()
s=s.replace('We give a candidate refinement to $c n/d^4$.', 'We present a proof draft for a candidate refinement to $c n/d^4$.')
s=s.replace('Rearranging \\eqref{eq:standard} gives\n\\begin{equation}\\label{eq:recurrence}\n u_{i+1}\\ge\n \\left(1-\\frac{k-\\theta_1}{b_i}\\right)u_i\n -\\frac{c_i}{b_i}u_{i-1}.\n\\end{equation}', r'''Rearranging \eqref{eq:standard} gives the exact identity
\begin{equation}\label{eq:recurrence-exact}
 u_{i+1}=
 \left(1-\frac{k-\theta_1}{b_i}\right)u_i
 +\frac{c_i}{b_i}(u_i-u_{i-1}).
\end{equation}
Consequently, whenever $u_i\ge0$,
\begin{equation}\label{eq:recurrence}
 u_{i+1}\ge
 \left(1-\frac{k-\theta_1}{b_i}\right)u_i
 -\frac{c_i}{b_i}u_{i-1}.
\end{equation}''')
s=s.replace("If $c_t=t-1$, equality holds throughout, so $r=t-1$ and $c_t=c_{t-1}$. The standard consequences recorded in Kivva's proof are $4\\le t\\le m-1$. In this case", r'''If $c_t=t-1$, equality holds throughout, so $r=t-1$ and $c_t=c_{t-1}$. We now justify the resulting range of $t$. Since
$c_1=1<c_2=2$ and, for $\mu\ge2$, one has $c_3>c_2$, the equality
$c_t=c_{t-1}$ forces $t\ge4$. A geometric distance-regular graph with
$\mu\ge2$ contains an induced quadrangle, so Terwilliger's inequality applies. It gives
\[
 b_{t-1}\ge c_{t-1}-c_t+b_t+\lambda+2\ge\lambda+2\ge\frac{k}{m}+1.
\]
On the other hand, \eqref{eq:basic} and $r=t-1$ give
$b_{t-1}\le(m-t+1)k/m$. Hence $t\le m-1$. In this case''')
s=s.replace('Finally, suppose $c_t=t=m$. If $t<d$, then $b_t\\ge1$.', 'Finally, suppose $c_t=t=m$. Since a geometric distance-regular graph with $\\mu\\ge2$ contains an induced quadrangle, Terwilliger\'s inequality is available. If $t<d$, then $b_t\\ge1$.')
s=s.replace('The strict increase of the $\\tau_i$, together with $\\tau_1=1$ and $\\tau_d=m=d$, gives\n$\\tau_i=i$. Since $c_d=\\tau_d\\psi_{d-1}=d$, we have $\\psi_{d-1}=1$. The same monotonicity argument as in \\cite[Theorem 4.7]{Kivva2021} then gives $\\psi_i=1$ for every $i$. Thus', r'''The strict increase of the $\tau_i$ up to index $d-1$, together with
$\tau_1=1$ and $\tau_d=m=d$, gives $\tau_i=i$. Since
$c_d=\tau_d\psi_{d-1}=d$, we have $\psi_{d-1}=1$. If some
$\psi_j\ge2$, choose $i\in\{2,\ldots,d-1\}$ with
$\psi_{i-1}\ge2$ and $\psi_i=1$. Then monotonicity of the intersection
numbers would give
\[
 i+1=c_{i+1}=\tau_{i+1}\psi_i
 \ge c_i=\tau_i\psi_{i-1}\ge2i,
\]
a contradiction. Hence $\psi_i=1$ for every $i$. Thus''')
s=s.replace('Moreover, geometricity gives $\\lambda\\ge k/m-1$, and \\eqref{eq:geodata} then implies $\\mu<\\lambda$.', r'''Moreover, geometricity gives $\lambda\ge k/m-1$. Since
$m<5d$ and $k\ge256d^3$,
\[
 \lambda>\frac{k}{5d}-1>rac{k}{256d^3}\ge\mu,
\]
so $\mu<\lambda$.''')
p.write_text(s)
PY

grep -n -A16 -B5 "recurrence-exact\|resulting range\|contains an induced quadrangle\|If some.*psi\|lambda>" /mnt/data/research_note_motion_d4.tex