## The deeper audit produced a stronger candidate result

The first draft has been superseded. After reconstructing the cited arguments from the source papers, redoing the algebra, and deliberately searching for endpoint failures, I arrived at the following:

> **Revised candidate theorem.**  
> Let \(X\) be a primitive distance-regular graph on \(n\) vertices with diameter \(d\ge3\). Then either \(X\) is a Johnson graph or a Hamming graph, or
> \[
> \boxed{\operatorname{motion}(X)\ge \frac{n}{32d^{3}}.}
> \]

This improves the first draftâs explicit constant by a factor of \(48\):

\[
\frac{1}{1536d^{3}}
\quad\longrightarrow\quad
\frac{1}{32d^{3}}.
\]

More importantly, the revised proof replaces the weakest part of the original argument with a genuinely sharper recurrence estimate. The published PyberâSkresanov result gives the global \(n/(\log n)^6\) scale outside the Johnson, Hamming, and crown families; Kivvaâs characterization supplies the Johnson/Hamming endgame. îciteîturn695708search0îturn695708search1î

**This remains a machine-generated candidate proof, not an established theorem.** It has survived a much more serious internal audit, but it still needs an expert referee.

## The three breakthroughs

### 1. An exact formula for adjacent distinguishing sets

For adjacent vertices in a distance-regular graph, I derived

\[
\boxed{
D(1)=2+\frac{2}{k}\sum_{i=2}^{d}k_i c_i
}
\]

and therefore, with \(\mu=c_2\),

\[
\boxed{
D(1)>\frac{\mu}{k}n.
}
\]

This is stronger and cleaner than the estimate in the first draft and has no auxiliary assumption such as \(\mu\le k/3\).

Combining it with the support-sensitive final line of the PyberâSkresanov expansion proof gives the following. If an automorphism has support density

\[
\rho=\frac{|\operatorname{supp}(g)|}{n}\le\frac12,
\]

then some moved vertex has at least

\[
\frac{k}{d}(1-\rho)
\]

fixed neighbors. In the small-\(\mu\) regime, this forces the vertex and its image to be adjacent, yielding simultaneously

\[
\lambda\ge\frac{k}{d}(1-\rho),
\qquad
\mu<\rho k.
\]

Thus a hypothetical very-small-support automorphism itself supplies the unusually large clique parameter needed later.

### 2. The full Metsch expression forces \(m\le d\)

The first draft used a simplified clique lower bound. The actual expression appearing in the PyberâSkresanov proof is

\[
L\ge
\lambda+2-
\left(
\left\lceil\frac{3k}{2(\lambda+1)}\right\rceil-1
\right)(\mu-1).
\]

Retaining this full expression, including its rounding, is much stronger.

Set

\[
\gamma=\frac1{32d^3}
\]

and suppose an automorphism has support density \(\rho<\gamma\). The preceding estimates give

\[
\mu<\gamma k,
\qquad
\lambda>\frac{1-\gamma}{d}k.
\]

Writing \(\alpha=(1-\gamma)/d\), the full Metsch bound gives

\[
L-1>
k\left(\alpha-\frac{3\gamma}{2\alpha}\right)
>
\frac{k}{d+1}.
\]

The Delsarte clique bound \(L\le1+k/m\) then implies

\[
m<d+1.
\]

The BangâKoolen criterion makes the graph Delsarte-geometric, at which point \(m\) is an integer. Hence

\[
\boxed{m\le d.}
\]

This is substantially better than the \(m<4d\) estimate in the first note. It is also what makes the explicit constant \(32\) possible.

### 3. Harmonic rather than linear error accumulation

The most delicate case is \(\mu=2\). Kivvaâs original standard-sequence argument accumulated an error at every recurrence step, producing a loss linear in \(d\).

The recurrence can instead be arranged so that, with \(x=m\varepsilon\) and \(r_i=m-\tau_i\),

\[
u_{i+1}
\ge
u_i\left(1-\frac{1+6x}{r_i}\right).
\]

The key factorization is

\[
1-\frac{1+6x}{r_i}
=
\frac{r_i-1}{r_i}
\left(1-\frac{6x}{r_i-1}\right).
\]

The first factors telescope, while the second factors accumulate according to a harmonic sum:

\[
\boxed{
u_j\ge
\left(1-6m\varepsilon H_{j-1}\right)
\frac{m-\tau_j}{m-\tau_j+j-1}
\frac{\theta}{k}.
}
\]

Thus the relevant error is \(O(m\varepsilon\log t)\), rather than \(O(m^2\varepsilon d)\).

This produces the candidate Hamming criterion

\[
\varepsilon<
\min\left\{
\frac1{18m},
\frac1{(m+1)\left(m(4+12H_{t-2})+2\right)}
\right\}.
\]

Its scale is approximately

\[
\frac{1}{m^2\log t},
\]

rather than Kivvaâs published \(1/(6m^4d)\) threshold. The underlying Kivva characterization and multiplicity framework are in the primary paper. îciteîturn695708search9î

Since the structural argument now gives \(m\le d\), the choice

\[
\varepsilon=\frac1{8d^3}
\]

satisfies the new threshold. The finite small-diameter cases are:

\[
\begin{array}{c|cccc}
d&3&4&5&6\\
\hline
(d+1)\bigl(d(4+12H_{d-2})+2\bigr)
&200&450&792&1232\\
8d^3&216&512&1000&1728
\end{array}
\]

and for \(d\ge7\), the estimate \(H_{d-2}\le d/3\) completes the check.

## Verification performed

I checked the argument at four distinct levels.

First, I checked the exact source statements directly rather than relying on summaries: the support-sensitive end of the expansion proof, the full Metsch expression, the BangâKoolen criterion, the spectral motion theorem, the \(\mu=1\) propositions, Kivvaâs strict-growth lemma, the Biggs multiplicity formula, the local-eigenvalue theorem, and the Johnson/Hamming characterizations. These are precisely the ingredients developed in the PyberâSkresanov and Kivva papers. îciteîturn695708search12îturn695708search9î

Second, every new identity was rederived symbolically. The computational checks are not being used as substitutes for proofs.

Third, I wrote an exact-rational-arithmetic audit script. It verifies:

- all structural and Hamming scalar inequalities for \(3\le d\le10{,}000\);
- every abstract \(R\)-factor case for \(2\le m\le120\) and all admissible \(t,r\);
- the worst recurrence coefficient and the small-diameter threshold cases.

The script reports:

```text
All exact-arithmetic audit checks passed.
Checked structural and Hamming constants for 3 <= d <= 10000.
Checked the R-factor for 2 <= m <= 120 and all admissible t,r.
```

Fourth, I tried to push the method to \(d^{-2}\). This exposed a genuine barrier rather than merely a failure to optimize constants. Small support of density \(\rho\) gives

\[
\mu\lesssim \rho k,
\qquad
m=O(d),
\qquad
\lambda\gtrsim\frac{k}{d}.
\]

The BangâKoolen geometricity condition

\[
m^2\mu<\lambda
\]

then naturally requires

\[
\rho=O(d^{-3}).
\]

A \(d^{-2}\) theorem will probably require a stronger route to geometricity or a way to bypass BangâKoolen altogether.

## What remains uncertain

The most delicate point is the new harmonic multiplicity criterion. Its recurrence estimates, rational-factor inequality, and exceptional endpoint have all been checked repeatedly, but the argument compresses several pages of Kivvaâs proof. That is the first section a distance-regular-graph specialist should examine.

The second inspection point is the use of the full Metsch expression to infer \(m\le d\). The ceiling and strict inequalities are preserved explicitly in the revised note so this can be audited line by line.

I now regard the result as a **serious candidate suitable for specialist review**, rather than an exploratory sketch. I do not yet regard it as a theorem suitable for citation, and I have not established priority or novelty through an exhaustive literature review.

### Files

[Revised candidate proof â PDF](sandbox:/mnt/data/babai_motion_d3_revised_candidate.pdf)

[Revised LaTeX source](sandbox:/mnt/data/babai_motion_d3_revised_candidate.tex)

[Exact-arithmetic audit script](sandbox:/mnt/data/babai_motion_d3_audit.py)