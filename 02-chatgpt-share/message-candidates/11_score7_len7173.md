# Result to share

I have a result worth sharing, with an important qualification: **this is a machine-generated candidate proof, not yet an established theorem**. It needs independent checking by a specialist in distance-regular graphs before it should be cited or presented as proved.

> **Candidate theorem.**  
> Let \(X\) be a primitive distance-regular graph on \(n\) vertices, of diameter \(d\ge 3\). Then either \(X\) is a Johnson graph or a Hamming graph, or
> \[
> \boxed{\operatorname{motion}(X)\ge \frac{n}{1536d^{3}}.}
> \]

Here, motion is the minimum number of vertices moved by a nonidentity automorphism.

The published PyberâSkresanov theorem gives a global lower bound of order \(n/d^{6}\), while their principal primitive structural step gives either motion at least \(n/(40d^{5})\), or Delsarte-geometric structure with smallest eigenvalue at least \(-5d\). The candidate theorem therefore improves the final diameter exponent from \(6\) to \(3\), and the structural dichotomy from \(5\) to \(3\). îciteîturn761563view2îturn761563view3î

## The three new ingredients

### 1. An exact adjacent-pair estimate

Let \(D(1)\) be the number of vertices that distinguish two adjacent vertices, let \(k_i\) be the size of a distance-\(i\) sphere, and put \(\lambda=a_1\), \(\mu=c_2\). A direct intersection-number count gives

\[
D(1)=n-\frac1k\sum_{i=1}^{d}k_i a_i.
\]

From \(a_i\le k-\mu\) for \(i\ge2\) and the standard inequality \(2\lambda\le k+\mu\), this yields the clean bound

\[
\boxed{\mu\le \frac{k}{3}\quad\Longrightarrow\quad
D(1)\ge \frac{\mu}{k}n.}
\]

This is stronger than the general distinguishing-number estimate needed in the relevant parameter range.

### 2. A minimum-motion automorphism moves an adjacent pair

Suppose \(\mu<k/(2d)\), and let \(g\) be a nonidentity automorphism with support \(S\), where \(|S|\le n/2\). PyberâSkresanovâs coherent-configuration expansion bound says that \(S\) has at least \(k|S|/(2d)\) outgoing boundary edges. Consequently, some moved vertex \(x\) has at least \(k/(2d)\) fixed neighbors. Each is a common neighbor of \(x\) and \(x^g\).

If \(x\) and \(x^g\) were nonadjacent, those common neighbors would force them to be at distance two, contradicting the fact that distance-two pairs have exactly \(\mu<k/(2d)\) common neighbors. Hence

\[
x\sim x^g.
\]

Moreover, every vertex outside the support is equidistant from \(x\) and \(x^g\), so

\[
\operatorname{motion}(X)=|S|\ge D(1).
\]

This removes a standard loss of one factor of \(d\): one no longer has to pass from a moved pair at arbitrary distance to an adjacent pair using \(D(i)\ge D(1)/d\). The expansion input itself is the published \(k/(2d)\) bound. îciteîturn984992view1îturn761563view3î

It also gives a sharper transition lemma:

\[
b_j,c_{j+1}\ge \alpha k
\quad\Longrightarrow\quad
\operatorname{motion}(X)\ge\alpha n
\]

in the small-\(\mu\) regime, with no additional division by \(d\).

### 3. A stronger Hamming stability threshold

Kivvaâs Hamming characterization uses the condition

\[
\varepsilon<\frac{1}{6m^{4}d},
\]

where \(-m\) is the smallest eigenvalue. îciteîturn761563view0îturn761563view1î

In the specific \(\mu=2\) branch, geometricity gives the exact identities

\[
\tau_2=2,\qquad \psi_1=1,\qquad
b_1=\frac{m-1}{m}k.
\]

Using those identities in Kivvaâs standard-sequence recurrence improves the accumulated error from order \(m^{2}\varepsilon\) to order \(m\varepsilon\). A sharper treatment of the final multiplicity factor gives the following candidate replacement:

> **Improved Hamming criterion.**  
> A Delsarte-geometric distance-regular graph with \(\mu=2\), satisfying
> \[
> b_t,c_t\le\varepsilon k,\qquad
> \theta\ge(1-\varepsilon)b_1,
> \]
> is Hamming provided
> \[
> \boxed{\varepsilon<
> \frac{1}{24m(m+1)d}.}
> \]

The key multiplicity estimate in the proof is

\[
k_{t-1}u_{t-1}^{2}\ge \frac nk\,F R,
\]

where

\[
F>\frac{m}{m+1},
\qquad
R\ge 1+\frac1m
\]

except in the endpoint case \(m=t=d,\ c_d=d\). That endpoint has the Hamming intersection array; the possible Doob alternative is excluded by the small-\(\varepsilon\) hypothesis.

Because the structural argument gives \(m<4d\), this new threshold is of order \(d^{-3}\), rather than the previous order \(d^{-5}\).

## How the pieces combine

The sharpened structural reduction says that either

\[
\operatorname{motion}(X)\ge\frac{n}{128d^{3}},
\]

or

\[
\mu\le\frac{k}{128d^{3}},\qquad
\lambda\ge\frac{k}{2d},\qquad
X\text{ is Delsarte-geometric},\qquad
m<4d.
\]

Set

\[
\varepsilon=\frac{1}{384d^{3}}.
\]

Since geometricity makes \(m\) an integer, \(m\le4d-1\), and consequently

\[
\varepsilon<
\frac{1}{24m(m+1)d}.
\]

There are then three cases:

1. A transition \(b_j,c_{j+1}\ge\varepsilon k\) gives motion at least \(\varepsilon n\).

2. In the low-second-eigenvalue case, Babaiâs spectral motion bound gives
   \[
   \operatorname{motion}(X)>
   \frac{\varepsilon n}{4}
   =\frac{n}{1536d^{3}}.
   \]

3. In the high-second-eigenvalue case, Kivvaâs characterization gives Johnson when \(\mu\ge3\), the improved criterion gives Hamming when \(\mu=2\), and the published \(\mu=1\) arguments give the stronger bound \(\Omega(n/d^{2})\).

That proves the displayed candidate theorem, conditional only on the correctness of the new lemmas.

## Significance if verified

The same imprimitive reductions would give

\[
\operatorname{motion}(X)\ge C\frac{n}{d^{3}}
\]

outside the Johnson, Hamming, and crown families. Since distance-regular graphs of valency greater than two satisfy \(d\le5\log_2 n\), this would improve the logarithmic motion bound from

\[
\frac{Cn}{(\log n)^6}
\quad\text{to}\quad
\frac{Cn}{(\log n)^3}.
\]

Following the same downstream arguments, the thickness estimate would improve from \(O((\log n)^7)\) to \(O((\log n)^4)\), and the edge-transitive base-size estimate from \(O((\log n)^9)\) to \(O((\log n)^6)\). The published baseline and its existing consequences are stated by Pyber and Skresanov. îciteîturn761563view2îturn761563view3î

## Confidence and remaining risk

I performed a line-by-line algebra and constant audit and did not find a contradiction. The adjacent-pair lemmas and structural reduction are short and, in my assessment, relatively robust.

The **highest-risk point is Proposition 4.2**, the improved multiplicity threshold. It compresses and sharpens several parts of Kivvaâs standard-sequence argument. In particular, a specialist should verify:

\[
F>\frac m{m+1},
\qquad
R\ge1+\frac1m,
\]

the treatment of \(c_t=t-1\), and the exceptional \(c_t=t=m\) endpoint. A targeted literature search through July 2026 did not reveal an indexed follow-up advertising a \(d^{-3}\) motion bound, but that search is not sufficient to establish novelty or priority.

I wrote the complete argument as an eight-page preliminary note:

[Download the candidate proof note (PDF)](sandbox:/mnt/data/babai_motion_d3_candidate_note.pdf)

[Download the LaTeX source](sandbox:/mnt/data/babai_motion_d3_candidate_note.tex)

The right next step is an independent expert audit of Proposition 4.2 before making any public theorem or priority claim.