Fair. I did another full pass, found an **actual mathematical error**, repaired it, removed the computer-enumerated case split entirely, and rebuilt the argument into a complete proof manuscript.

## The result

> **Proposed theorem.**  
> Let \(X\) be a primitive distance-regular graph on \(n\) vertices with diameter \(d\ge3\). Then either \(X\) is a Johnson graph or a Hamming graph, or
> \[
> \boxed{\operatorname{motion}(X)\ge \frac{n}{12d^{3}}.}
> \]

The published PyberâSkresanov theorem gives a lower bound on the scale \(n/d^{6}\), together with the structural dichotomy

\[
\operatorname{motion}(X)\ge \frac{n}{40d^5}
\]

or Delsarte geometry with smallest eigenvalue at least \(-5d\). îciteîturn335649view0î

So, if the proof survives independent review, this improves the diameter dependence from \(d^{-6}\) to \(d^{-3}\) and gives the explicit constant \(1/12\).

I cannot honestly guarantee the absence of mistakes solely through self-review. I **can** now say something materially stronger than before:

> **There is no unresolved implication or acknowledged proof gap left in the manuscript after the final source, algebra, endpoint, and dependency audit.**

That was not true of the earlier \(d^{-3}\) drafts.

## What finally closed the proof

### 1. Exact adjacent-pair distinguishing identity

For two adjacent vertices, the number \(D(1)\) of vertices distinguishing them satisfies

\[
\boxed{
D(1)=2+\frac{2}{k}\sum_{i=2}^{d}k_i c_i
}
\]

and hence

\[
\boxed{
D(1)>\frac{\mu}{k}n.
}
\]

This turns an automorphism moving an adjacent pair into a sharp motion estimate without the usual extra \(1/d\) loss.

### 2. Small support forces strong intersection parameters

For an automorphism with support density

\[
\rho=\frac{|\operatorname{supp}(g)|}{n}<\frac1{12d^3},
\]

a support-sensitive version of the geodesic boundary argument produces a moved vertex \(x\) with at least

\[
\frac{k}{d}(1-\rho)
\]

fixed neighbors. It follows that \(x\sim x^g\) and

\[
\boxed{
\mu<\rho k,\qquad
\lambda>\frac{1-\rho}{d}k.
}
\]

The oriented-edge convention and the factor of two were both rederived from scratch rather than inferred from the source notation.

### 3. Full Metsch, not the \(\lambda/2\) shortcut

Keeping Metschâs complete clique-size expression gives a clique \(C\) satisfying

\[
|C|-1>\frac{k}{d+1}.
\]

The Delsarte clique bound therefore implies

\[
m<d+1,
\]

where \(-m\) is the smallest eigenvalue. BangâKoolenâs criterion then yields Delsarte geometry, and integrality gives

\[
\boxed{m\le d.}
\]

This is the structural step that turns the rest of the argument from a \(5d\)-scale problem into a \(d\)-scale problem.

### 4. Direct geodesic PoincarÃ© inequality

For a connected symmetric basis relation of valency \(k\) and diameter \(D\) in a homogeneous coherent configuration, the manuscript proves

\[
\boxed{
k-\theta_1
\ge
\frac{n^2k}
{\displaystyle\sum_{x,y}\operatorname{dist}(x,y)^2}
\ge
\frac{k}{D^2}.
}
\]

PyberâSkresanov obtain \(k-\theta_1\ge k/(8D^2)\) by combining geodesic expansion with Cheegerâs inequality. îciteîturn335649view0î

The new proof applies CauchyâSchwarz directly along every geodesic and retains the path lengths. This removes the factor \(8\), and its directed-edge normalization has been checked explicitly.

### 5. The difficult \(\mu=2\) branch is now analytic

This was the gap in the withdrawn drafts.

Kivvaâs work supplies the geometric identities, standard-sequence machinery, Biggsâ multiplicity formula, local-eigenvalue theorem, and Hamming/Doob endpoint classification. His published characterization handles geometric distance-regular graphs under an approximate eigenvalue constraint. îciteîturn846784search0îturn699135search3î

The new proof keeps the exact relative-drop recurrence. For

\[
y_i=\frac{u_{i-1}-u_i}{u_{i-1}},
\]

one has

\[
\boxed{
y_{i+1}
=
\frac{k-\theta+c_i\,y_i/(1-y_i)}{b_i}.
}
\]

Rather than replacing each step by a uniform additive error, this gives a multiplicative estimate

\[
u_{t-1}
\ge
u_1\frac{r}{r+t-2}
\left(1-\delta H_{t-2}\right).
\]

A separate direct sphere-concentration argument gives

\[
k_t\ge(1-2m\varepsilon)n.
\]

Together these produce

\[
k_{t-1}u_{t-1}^2
\ge
\frac nk\,F R.
\]

The proof then establishes **analytically**, with no tuple enumeration,

\[
F>\frac{m}{m+1},
\qquad
R\ge\frac{m+1}{m},
\]

except at the exact endpoint

\[
c_t=t=m=d.
\]

Outside that endpoint, \(FR>1\), so Biggsâ formula implies that the multiplicity of \(\theta_1\) is smaller than \(k\). Terwilligerâs local-eigenvalue theorem then forces a neighborhood eigenvalue strictly below \(-1\), contradicting the fact that each neighborhood is a disjoint union of cliques.

At the endpoint, the geometric parameters force

\[
c_i=i,\qquad
b_i=(d-i)\frac{k}{d},
\]

the Hamming intersection array. The only alternative in the endpoint classification is a Doob graph, but that would have \(k=3d\), whereas the small-support assumption implies \(k>12d^3\). Hence the graph is Hamming.

## A real error found and repaired

An earlier draft asserted

\[
B\le1+\varepsilon,
\qquad
B=1+(m-1)\varepsilon,
\]

which is false for \(m>2\).

The correct inequality is

\[
\boxed{
\frac{B}{m-1}
=
\frac1{m-1}+\varepsilon
\le1+\varepsilon.
}
\]

The rewritten recurrence proof uses only this valid normalized inequality.

I also repaired or made explicit:

- the induced-quadrangle hypothesis required by Terwilligerâs inequality;
- the \(t=m<d\) endpoint inequality;
- the final deduction that every \(\psi_i=1\);
- the orientation convention in both geodesic arguments;
- the complete list of hypotheses for every imported proposition.

The previous finite âadmissible tupleâ computation has been deleted from the proof.

## Verification performed

Two independent audit scripts now accompany the manuscript.

The exact-rational audit reports:

```text
All exact-arithmetic scalar checks passed.
Parameter inequalities: 3 <= d <= 20,000.
Local mu=2 constants: 2 <= m <= d <= 300.
R-gain branches: 3 <= m <= 1,000, every admissible t endpoint.
Exact unrelaxed F margin: 3 <= d <= 80 at m=t=d.
All infinite tails also have explicit polynomial/inductive certificates.
```

The independent symbolic audit rederives and factors:

- the structural margins;
- the parameter-closing identity;
- the corrected \(A-B\) relation;
- the Riccati recurrence;
- the sphere-concentration identity;
- the multiplicity-certificate algebra.

It reports:

```text
All independent symbolic identity checks passed.
```

The infinite portions are not justified by finite computation. They have explicit polynomial certificates; for example, the central \(F\)-estimate reduces to

\[
6d^3-10d^2-8d-5>0.
\]

Writing \(d=x+3\) gives

\[
6x^3+44x^2+94x+43>0,
\]

so it holds transparently for every \(d\ge3\).

## Give it to Fable

Absolutely. The right competition now is not âmake it prettierâ; it is:

> Find the earliest invalid implication, missing hypothesis, reversed inequality, or source mismatch. Return `VALID AS WRITTEN`, `GAP FOUND`, `SOURCE MISMATCH`, or `UNRESOLVED`.

I prepared exactly that hostile-referee prompt. Agreement from another model would still not equal peer review, but a genuinely adversarial independent derivation is the correct next filter.

## Files

[Complete proof manuscript â PDF](sandbox:/mnt/data/babai_motion_d3_complete_proof.pdf)

[LaTeX source](sandbox:/mnt/data/babai_motion_d3_complete_proof.tex)

[Complete reproducibility and audit package](sandbox:/mnt/data/babai_motion_d3_c12_audit_package.zip)

[Exact-rational audit script](sandbox:/mnt/data/babai_motion_d3_c12_audit.py)

[Independent symbolic audit script](sandbox:/mnt/data/babai_motion_d3_c12_symbolic_audit.py)

[Hostile-referee prompt for Fable](sandbox:/mnt/data/fable_hostile_referee_prompt_d3_c12.txt)

The current status is therefore:

\[
\boxed{
\text{complete internally audited proof of }\
\operatorname{motion}(X)\ge \frac{n}{12d^3},
\text{ awaiting independent verification.}
}
\]