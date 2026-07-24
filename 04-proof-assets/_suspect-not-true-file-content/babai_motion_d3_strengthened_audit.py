## A strongerâand materially more robustâcandidate

The revised argument now gives:

> **Strengthened candidate theorem.**  
> Let \(X\) be a primitive distance-regular graph on \(n\) vertices with diameter \(d\ge 3\). Then either \(X\) is a Johnson graph or a Hamming graph, or
> \[
> \boxed{\operatorname{motion}(X)\ge \frac{n}{8d^{3}}.}
> \]

This improves the previous candidate

\[
\frac{n}{32d^{3}}
\]

by a factor of \(4\).

There is also a deliberately more conservative version:

> **Source-conservative candidate.**  
> Using only the published structural inputs from PyberâSkresanov and Kivva,
> \[
> \boxed{\operatorname{motion}(X)\ge \frac{n}{15d^{3}}.}
> \]

The \(1/(8d^3)\) version additionally uses a January 2026 preprint of Lv and Koolen, but only in the narrow case \(d=3\) and \(\mu=c_2\ge3\). Their structural theorem classifies the relevant geometric possibilities into Johnson, Grassmann, locally disconnected, and two residual parameter configurations; the inequalities obtained from small motion eliminate every case except Johnson. îciteîturn417751view3îturn417751view4î

Both statements remain **machine-generated candidate theorems**, not established results. The published benchmark is \(C n/d^6\), outside the Johnson, Hamming, and crown families, so even the conservative version would improve the known diameter exponent from \(6\) to \(3\). îciteîturn341760view0îturn341760view1îturn341760view3î

## The most robust breakthrough: an exact geodesic PoincarÃ© inequality

The strongest standalone contribution is independent of the delicate Johnson/Hamming classification.

> **Geodesic spectral-gap lemma.**  
> Let \(G\) be the graph of a connected symmetric basis relation of valency \(k\) in a homogeneous coherent configuration on \(n\) points. If \(d\) is its diameter and \(\theta_1\) its second adjacency eigenvalue, then
> \[
> \boxed{
> k-\theta_1\ge
> \frac{n^2k}
> {\displaystyle\sum_{x,y\in V(G)}
> \operatorname{dist}(x,y)^2}
> \ge\frac{k}{d^2}.
> }
> \]

For a distance-regular graph this specializes to

\[
\boxed{
k-\theta_1\ge
\frac{nk}{\displaystyle\sum_{i=0}^{d}k_i i^2}.
}
\]

Pyber and Skresanov proved

\[
k-\theta_1\ge\frac{k}{8d^2}
\]

by first obtaining edge expansion \(k/(2d)\) from uniform geodesic loads and then applying Cheegerâs inequality. The new proof uses the same uniformity phenomenon but applies CauchyâSchwarz directly along the geodesics, retaining their lengths rather than discarding them. This removes the factor \(8\). îciteîturn417751view1îturn341760view2î

### Proof in one page

For every ordered pair \(x,y\), let \(p(x,y)\) be the number of geodesics from \(x\) to \(y\). For a directed edge \(e\), define

\[
Q_e=
\sum_{x,y}
\frac{\operatorname{dist}(x,y)}{p(x,y)}
\#\{P:P\text{ is an }x\text{--}y
\text{ geodesic containing }e\}.
\]

The coherent-configuration intersection-number identities imply that \(Q_e\) is independent of the directed edge \(e\); call the common value \(Q\). Summing over all \(nk\) directed edges gives

\[
nkQ=\sum_{x,y}\operatorname{dist}(x,y)^2.
\]

For a mean-zero function \(f\), CauchyâSchwarz along each geodesic gives

\[
(f(x)-f(y))^2
\le
\frac{\operatorname{dist}(x,y)}{p(x,y)}
\sum_{P:x\to y}\sum_{e\in P}(\nabla_e f)^2.
\]

Summing over all ordered \(x,y\),

\[
2n\lVert f\rVert_2^2
\le
Q\sum_{e\text{ directed}}(\nabla_e f)^2
=
2Q\,f^{\mathsf T}(kI-A)f.
\]

Taking \(f\) in the \(\theta_1\)-eigenspace yields

\[
k-\theta_1\ge\frac nQ
=
\frac{n^2k}{\sum_{x,y}\operatorname{dist}(x,y)^2}.
\]

I did not locate this exact coherent-configuration formulation in the literature I checked. It may be subsumed by a known canonical-path or multicommodity-flow inequality, so I am not claiming novelty without a broader search. The proof itself is short and comparatively easy to audit.

## A cleaner small-support structural lemma

The argument now begins with an exact identity for the number \(D(1)\) of vertices distinguishing an adjacent pair:

\[
\boxed{
D(1)=2+\frac2k\sum_{i=2}^{d}k_i c_i.
}
\]

Consequently,

\[
\boxed{
D(1)>\frac{\mu}{k}n,
\qquad \mu=c_2.
}
\]

Now suppose an automorphism \(g\) has support \(S\), with density

\[
\rho=\frac{|S|}{n}\le\frac12.
\]

The support-sensitive final inequality in PyberâSkresanovâs geodesic expansion proof gives

\[
|\delta(S)|
\ge
|S|\frac{k}{d}(1-\rho).
\]

Thus some moved vertex \(x\) has at least \(k(1-\rho)/d\) fixed neighbors. In the relevant small-\(\mu\) regime, those fixed neighbors force \(x\) and \(x^g\) to be adjacent. Since every fixed vertex is equidistant from \(x\) and \(x^g\),

\[
D(1)\le |S|.
\]

It follows immediately that

\[
\mu<\rho k,
\qquad
\lambda>\frac{1-\rho}{d}k.
\]

This is a particularly useful conversion:

\[
\text{small automorphism support}
\quad\Longrightarrow\quad
\text{small }\mu\text{ and large }\lambda.
\]

Keeping the **full** clique-size expression from Metschâs theorem, rather than replacing it by the coarser \(L\ge\lambda/2\), then gives a clique with

\[
L-1>\frac{k}{d+1}.
\]

The Delsarte clique bound forces the absolute value \(m\) of the smallest eigenvalue to satisfy

\[
m<d+1.
\]

Once the BangâKoolen criterion produces Delsarte geometry, \(m\) is integral, so

\[
\boxed{m\le d.}
\]

The published ingredients are exactly the full Metsch expression, the Delsarte clique bound, and the BangâKoolen condition \(m^2\mu<\lambda\). îciteîturn417751view0î

## A sharper Hamming-stability argument

The remaining difficult branch is

\[
\mu=2,\qquad
\theta_1\ge(1-\varepsilon)b_1.
\]

Kivvaâs published proof uses a sufficiently small \(\varepsilon\) on the scale

\[
\frac{1}{m^4d}.
\]

That threshold is one reason the published motion argument loses several powers of \(d\). îciteîturn417751view2î

The new argument retains the exact standard-sequence recurrence

\[
u_{i+1}
=
u_i-\frac{k-\theta}{b_i}u_i
-\frac{c_i}{b_i}(u_{i-1}-u_i)
\]

rather than repeatedly applying a uniform worst-case loss. With

\[
A=\frac{1+(3m-1)\varepsilon}{1-m\varepsilon},
\qquad
\delta=A-1,
\]

one obtains

\[
u_{i+1}\ge
u_i\left(1-\frac{A}{m-\tau_i}\right).
\]

The key factorization is

\[
1-\frac{A}{r}
=
\frac{r-1}{r}
\left(1-\frac{\delta}{r-1}\right).
\]

The first factor telescopes; the second accumulates only harmonically. The result is

\[
\boxed{
u_j\ge
\left(1-\delta H_{j-1}\right)
\frac{m-\tau_j}
     {m-\tau_j+j-1}
\frac{\theta}{k}.
}
\]

The previous linear-in-\(d\) accumulation is thereby replaced by \(H_d=O(\log d)\).

A second exact estimate improves the size of the dominant distance sphere from the earlier coarse bound to

\[
\boxed{k_t\ge(1-2m\varepsilon)n.}
\]

Together these give enough multiplicity to force the Hamming endpoint for

\[
\varepsilon=\frac{1}{4d^3-1}
\]

in the \(1/(8d^3)\) theorem, and for

\[
\varepsilon=\frac{2}{15d^3-2}
\]

in the source-conservative theorem.

This is still the **least robust portion** of the candidate proofânot because any scalar inequality failed, but because it compresses and modifies several interacting pieces of Kivvaâs multiplicity argument.

## What was verified

The accompanying audit uses exact rational arithmetic, not floating point. It checks:

- all structural inequalities for \(3\le d\le10{,}000\);
- the \(1/(8d^3)\) and \(1/(15d^3)\) parameter choices;
- every exceptional \(d=3,4\) Hamming product case;
- the exact \(d=5,6\) losses;
- the endpoint inequalities in the multiplicity factor;
- the polynomial inequalities used for the infinite \(d\ge7\) tail.

Its output is:

```text
All strengthened-candidate audit checks passed.
Structural and threshold checks: 3 <= d <= 10000
(exact rational arithmetic).
Hamming finite products and finite losses:
exact rational arithmetic.
Analytic tail inequalities:
boundary polynomials and 7 <= d <= 1000 checked.
```

The checks establish that the written numerical implications are internally consistent. They do **not** replace verification that every imported theorem has precisely the required hypotheses.

## Current confidence assessment

I would separate the result into four layers:

1. **Geodesic PoincarÃ© inequality:** high confidence. It is self-contained and short enough for direct line-by-line checking.

2. **Adjacent distinguishing identity and small-support reduction:** high confidence.

3. **Full-Metsch argument giving \(m\le d\):** moderately high confidence. The strict inequalities and ceiling term have been retained explicitly.

4. **Hamming multiplicity argument:** moderate confidence. This is the first part that should be sent to a specialist. The exact recurrence is convincing, but the interface with Kivvaâs local-eigenvalue and endpoint machinery deserves independent scrutiny.

The \(1/(15d^3)\) version is institutionally more robust because it avoids relying on a very recent preprint. Kivva explicitly records the inequality \(1/200<\varepsilon^\ast\) used by that version. îciteîturn417751view2î

## Why the proof still stops at \(d^{-3}\)

The obstruction is now sharply identifiable. Small support density \(\rho\) gives approximately

\[
\mu\lesssim\rho k,
\qquad
m=O(d),
\qquad
\lambda\gtrsim\frac{k}{d}.
\]

The BangâKoolen geometricity condition is

\[
m^2\mu<\lambda.
\]

Substitution gives

\[
d^2\rho k\lesssim\frac{k}{d},
\]

or

\[
\rho=O(d^{-3}).
\]

So improving the exponent to \(d^{-2}\) probably requires a new geometricity theorem that uses more of the clique structure than the scalar condition \(m^2\mu<\lambda\), or an argument that bypasses exact Delsarte geometry.

## Updated files

[Strengthened candidate proof â PDF](sandbox:/mnt/data/babai_motion_d3_strengthened_candidate.pdf)

[LaTeX source](sandbox:/mnt/data/babai_motion_d3_strengthened_candidate.tex)

[Exact-arithmetic audit script](sandbox:/mnt/data/babai_motion_d3_strengthened_audit.py)

The most defensible item to circulate first is the geodesic PoincarÃ© proposition by itself. The full \(1/(8d^3)\) statement should be labeled a candidate until the \(\mu=2\) multiplicity section receives independent specialist review.