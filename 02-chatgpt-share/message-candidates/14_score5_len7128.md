# One more candidate breakthrough

The additional progress is **not merely another constant optimization**. The fragile \(\mu=2\) Hamming branch now has a different proof mechanism: an exact multiplicative recurrence for the standard sequence, combined with rising-factorial control of the distance-sphere tails.

That gives the following new headline:

> **Machine-generated, unrefereed candidate theorem.**  
> Let \(X\) be a primitive distance-regular graph on \(n\) vertices, with diameter \(d\ge3\). Then either \(X\) is a Johnson graph or a Hamming graph, or
> \[
> \boxed{\operatorname{motion}(X)\ge \frac{2n}{5d^3}.}
> \]

This strengthens the preceding \(n/(8d^3)\) candidate by a factor of \(16/5=3.2\). It is **not yet an established theorem and should not be cited as proved**.

For context, PyberâSkresanovâs published general theorem gives \(Cn/d^6\) outside the Johnson, Hamming, and crown families. Kivva supplies the approximate spectral-characterization machinery, while the stronger candidate uses a January 2026 result of LvâKoolen at the endpoint \(\phi_1=\tau_2=2\), where their classification gives a Johnson graph. îciteîturn596365search3îturn596365search1îturn596365search7î

## What actually changed

For the standard sequence \(u_0,u_1,\ldots\), define its relative drops by

\[
y_i=\frac{u_{i-1}-u_i}{u_{i-1}}.
\]

Instead of replacing each recurrence step by a uniform worst-case error, retain the exact Riccati-type recurrence

\[
\boxed{
y_{i+1}
=
\frac{k-\theta+c_i\,y_i/(1-y_i)}{b_i}.
}
\]

This matters because a small preceding drop contributes only through \(y_i/(1-y_i)\); the earlier harmonic estimate discarded that information. The resulting lower bound is multiplicative:

\[
u_{t-1}\ge u_1\prod_{i=2}^{t-1}(1-Y_i),
\]

where the \(Y_i\) are explicit rational majorants.

At the same time, the distance-sphere mass is bounded using

\[
\boxed{
\frac{k_{t-h}}{k_t}
\le
\frac{q^h}{r(r+1)\cdots(r+h-1)},
}
\]

rather than a geometric bound \(q^h\). At the sensitive endpoint \(d=t+1\), the right tail is \(q/m\), not merely \(q\).

Together, these estimates produce the multiplicity certificate

\[
k_{t-1}u_{t-1}^{\,2}\ge \frac nk\,M.
\]

When \(M>1\), Biggsâ multiplicity formula gives \(f_1<k\), and the local-eigenvalue endpoint machinery forces the graph to be Hamming.

## Stress test

Every relaxed admissible tuple for \(3\le d\le16\) was evaluated using exact rational arithmetic. The worst case is

\[
d=7,\qquad (m,t,r,c_t)=(6,6,1,7),
\]

where

\[
M=
\frac{
116108034801868413182297308409682258079489
}{
115280354870777504601657083769030760079250
}
=
1.007179713594\ldots
\]

Thus the minimum audited margin is approximately \(0.718\%\).

For \(d\ge17\), the proof reduces to the positivity of

\[
P(d)=
55d^6-800d^5-1380d^4-292d^3
+1280d^2+1032d+300,
\]

which follows by writing

\[
P(d)=d^3Q(d)+1280d^2+1032d+300
\]

and observing that \(Q(17)>0\) and \(Q\) is increasing thereafter.

I also tested where the method breaks:

\[
\begin{array}{c|c}
\text{proposed coefficient of }d^{-3}
& \text{worst finite certificate}\\
\hline
2/5 & 1.007179713594\ldots\\
5/12 & 1.000829988423\ldots\\
1/2 & 0.964974047435\ldots
\end{array}
\]

The \(5/12\) finite relaxation passes by only \(0.083\%\), so I did **not** promote it to a theorem candidate. The \(1/2\) attempt genuinely fails under the present certificate. The coefficient \(2/5\) is therefore a deliberately conservative headline, not the largest number the computation could be made to display.

The exact-arithmetic audit verifies the scalar recurrences and inequalities. It does **not** verify that every imported graph-theoretic theorem has been applied under exactly the right hypotheses. The main target for specialist attack remains the completeness of the admissible \(\mu=2\) tuple list and its interface with Kivvaâs endpoint argument.

# Paste-ready Twitter thread

**1/10**

Proof-audit thread. New machine-generated candidate:

For primitive distance-regular \(X\) of diameter \(d\ge3\),  
\(X\) is Johnson/Hamming, or

\[
\operatorname{mot}(X)\ge 2n/(5d^3).
\]

Published benchmark: \(Cn/d^6\). This is NOT a theorem yet. Please try to break it.

**2/10**

Small support forces geometry. For adjacent vertices,

\[
D(1)=2+(2/k)\sum_{i\ge2}k_i c_i>(\mu/k)n.
\]

A support-sensitive geodesic boundary argument then gives, for support density \(\rho\),

\[
\mu<\rho k,\qquad \lambda>(1-\rho)k/d.
\]

**3/10**

Put \(\rho<2/(5d^3)\). Keeping the full Metsch clique expressionânot the usual \(\lambda/2\) shortcutâthen combining Delsarteâs clique bound with BangâKoolen yields Delsarte geometry and smallest eigenvalue \(-m\) with \(m\le d\).

**4/10**

The \(\mu\ge3\) branch collapses sharply.

\(\psi_1=1\) contradicts Kivvaâs \(\theta+1\le5b_1/7\). Otherwise

\[
2\le\psi_1\le\tau_2<\cdots<\tau_d=m\le d,
\]

so \(m=d,\ \psi_1=\tau_2=2\); a LvâKoolen endpoint theorem gives Johnson.

**5/10**

The new breakthrough is the \(\mu=2\) branch. For the standard sequence, track relative drops

\[
y_i=(u_{i-1}-u_i)/u_{i-1}
\]

and retain the exact Riccati recurrence, instead of replacing every step by one uniform additive error.

**6/10**

Also retain exact sphere tails:

\[
k_{t-h}/k_t\le
q^h/[r(r+1)\cdots(r+h-1)].
\]

At the endpoint \(d=t+1\), the right tail is \(q/m\), not \(q\). These two changes turn the previous harmonic/coarse loss into a multiplicative certificate.

**7/10**

The certificate is

\[
k_{t-1}u_{t-1}^2\ge(n/k)M.
\]

Exact rational audit over every relaxed case for \(3\le d\le16\) gives \(\min M=1.007179713\ldots\) at

\[
d=7,\quad(m,t,r,c_t)=(6,6,1,7).
\]

For \(d\ge17\), one explicit degree-6 polynomial is positive.

**8/10**

Robustness check: the same finite relaxation barely supports coefficient \(5/12\) (minimum margin \(0.083\%\)), while coefficient \(1/2\) fails (\(M=0.96497\ldots\)). I headline \(2/5\) because its worst audited margin is \(0.718\%\), not because it is numerically maximal.

**9/10**

The \(\mu=1\) branch is cleaner. A geodesic PoincarÃ© inequality gives

\[
k-\theta_1
\ge
\frac{n^2k}{\sum_{x,y}\operatorname{dist}(x,y)^2}
\ge\frac{k}{d^2}.
\]

Dualization + Babaiâs spectral motion estimate then gives

\[
\operatorname{mot}(X)>3n/(10d^2).
\]

**10/10**

Status: unrefereed machine proof. Most attackable point: the \(\mu=2\) recurrence/multiplicity interface. Recent-preprint dependency: \(\psi_1=\tau_2=2\Rightarrow\) Johnson.

There is also a source-conservative fallback

\[
\operatorname{mot}(X)\ge n/(15d^3).
\]

## Research files

[Candidate proof â PDF](sandbox:/mnt/data/babai_motion_d3_final_candidate.pdf)

[LaTeX source](sandbox:/mnt/data/babai_motion_d3_final_candidate.tex)

[Exact-rational audit script](sandbox:/mnt/data/babai_motion_d3_final_audit.py)

[Paste-ready Twitter thread â every post checked to be at most 280 characters](sandbox:/mnt/data/babai_motion_twitter_thread.txt)

The defensible public claim is: **a reproducible and fairly sharp candidate \(d^{-3}\) motion bound, with a precise failure boundary and a clearly identified place for experts to attackânot a proved theorem.**