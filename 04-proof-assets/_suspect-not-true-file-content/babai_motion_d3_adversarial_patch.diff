## Adversarial-review verdict

After reconstructing the proof independently rather than merely rerunning its audit scripts, I found:

\[
\boxed{\textbf{No fatal mathematical gap.}}
\]

My referee-style verdict is:

> **PROVISIONALLY VALID AFTER MINOR CORRECTIONS.**

That is stronger than âI could not disprove it,â but weaker than independent peer verification. I would **not retract the \(n/(12d^3)\) theorem on the evidence currently available**.

The original PDF is not literally valid as written because I found two genuine defects. Both are repairable without changing the theorem, proof strategy, or constant.

## The two real defects

### 1. Directed versus undirected boundary edges

The original manuscript mixes conventions when using the geodesic-load boundary estimate. The source argument counts a symmetric relation as \(nk\) **directed arcs**, while the manuscript sometimes calls the corresponding cut an undirected edge boundary. That creates an apparent factor-of-two problem.

I rederived the step from scratch. For a directed arc \(e\), let \(P_e\) be the total fractional load of all ordered-pair geodesics through \(e\). Coherent-configuration regularity makes this independent of \(e\), say \(P_e=P\). Then

\[
nkP=\sum_{x,y}\operatorname{dist}(x,y)\le dn^2,
\]

so

\[
P\le\frac{dn}{k}.
\]

For \(S\subset V\), every geodesic from \(x\in S\) to \(y\notin S\) uses an outward-directed crossing arc. Therefore

\[
|S|(n-|S|)
   \le |\partial^+(S)|P,
\]

and hence

\[
|\partial^+(S)|
\ge
|S|\frac{k}{d}\frac{n-|S|}{n}.
\]

Each undirected crossing edge corresponds to exactly one outward-directed crossing arc, so the numerical cut size is the same. **There is no lost factor of two.**

The published PyberâSkresanov argument supplies the coherent-configuration geodesic uniformity and associated expansion machinery used here. îciteîturn238390view0î

This is a mandatory notational correction, but not a mathematical failure.

### 2. Kivva theorem-number mismatch

Several citations use theorem numbers from Kivvaâs arXiv version while the bibliography points to the published journal version. The content matches, but the numbering does not.

The relevant corrections include:

\[
\begin{aligned}
\text{arXiv Lemma 2.16} &\longrightarrow \text{journal Lemma 2.17},\\
\text{arXiv Lemma 2.17} &\longrightarrow \text{journal Lemma 2.18},\\
\text{arXiv Lemma 2.19} &\longrightarrow \text{journal Lemma 2.20},\\
\text{arXiv Theorem 2.24} &\longrightarrow \text{journal Theorem 2.25}.
\end{aligned}
\]

The journal version contains the needed geometric identities, local-clique description, local-eigenvalue theorem, multiplicity machinery, and Hamming/Doob endpoint classification. îciteîturn321420view0îturn321420view1îturn321420view2îturn321420view3î

Again, this is a source-interface defect rather than a flaw in the deduction.

## What survived the hostile reconstruction

### The adjacent-pair identity

I independently derived

\[
D(1)=2+\frac{2}{k}\sum_{i=2}^{d}k_i c_i.
\]

Because \(c_i\ge c_2=\mu\) for \(i\ge2\), and because \(c_2\le b_1\) implies \(k_2\ge k_1=k\), one obtains

\[
D(1)>\frac{\mu}{k}n.
\]

I found no missing endpoint or monotonicity assumption here.

### Small support implies strong local structure

For an automorphism with support density \(\rho\le1/2\), the repaired boundary argument gives a moved vertex \(x\) having at least

\[
\frac{k}{d}(1-\rho)
\]

fixed neighbors.

Under the manuscriptâs small-support assumption, this exceeds \(\mu\), forcing

\[
x\sim x^g.
\]

Every fixed vertex is equidistant from \(x\) and \(x^g\), so the distinguishing set of the adjacent pair lies inside the support. Consequently,

\[
\mu<\rho k,
\qquad
\lambda>\frac{1-\rho}{d}k.
\]

This implication is sound.

### The full Metsch step and \(m\le d\)

I checked the ceiling term and all strict inequalities rather than using the usual coarse clique estimate. For

\[
\rho<\gamma=\frac1{12d^3},
\qquad
\alpha=\frac{1-\gamma}{d},
\]

the required scalar inequalities hold:

\[
\alpha^2>4\gamma,
\]

\[
\alpha-\frac{3\gamma}{2\alpha}>\frac1{d+1},
\]

and

\[
(d+1)^2\gamma<\alpha.
\]

The complete Metsch expression then produces a clique \(C\) satisfying

\[
|C|-1>\frac{k}{d+1}.
\]

Delsarteâs clique bound gives \(m<d+1\). BangâKoolenâs geometricity criterion applies in the correct order, after which \(m\) is integral, yielding

\[
m\le d.
\]

I found no circular use of geometricity in this step.

### The geodesic PoincarÃ© inequality

I reconstructed the proof with all orientations and factors of two exposed. It yields

\[
k-\theta_1
\ge
\frac{n^2k}
{\displaystyle\sum_{x,y}\operatorname{dist}(x,y)^2}
\ge\frac{k}{d^2}.
\]

For a mean-zero function \(f\), CauchyâSchwarz along each geodesic gives

\[
2n\lVert f\rVert_2^2
\le
Q\sum_{e\ {\rm directed}}(\nabla_e f)^2
=
2Q f^{\mathsf T}(kI-A)f,
\]

while

\[
nkQ=\sum_{x,y}\operatorname{dist}(x,y)^2.
\]

The factors cancel exactly as claimed.

This lemma is not ornamental. The weaker published spectral-gap constant would not close the manuscriptâs \(\mu=1\) branch at \(1/(12d^3)\).

### The difficult \(\mu=2\) branch

This received most of the audit.

I independently checked the exact recurrence

\[
y_{i+1}
=
\frac{k-\theta+c_i\,y_i/(1-y_i)}{b_i},
\qquad
y_i=\frac{u_{i-1}-u_i}{u_{i-1}}.
\]

I checked:

- the base case;
- the positivity range needed to divide by \(1-y_i\);
- the induction denominators;
- the product estimate for \(u_{t-1}\);
- the left and right distance-sphere tails;
- the concentration estimate \(k_t\ge(1-2m\varepsilon)n\);
- the complete multiplicity-certificate algebra;
- all branches in the \(R\)-factor argument;
- the case \(t=m<d\);
- the exact endpoint \(c_t=t=m=d\);
- the final deduction that every \(\psi_i=1\);
- exclusion of the Doob alternative by the valency inequality.

Outside the endpoint, the proof obtains

\[
k_{t-1}u_{t-1}^2
\ge
\frac nk\,FR
\]

with

\[
F>\frac{m}{m+1},
\qquad
R\ge\frac{m+1}{m}.
\]

Thus \(FR>1\), and Biggsâ multiplicity formula gives \(f_1<k\). The local-eigenvalue theorem then forces a local eigenvalue below \(-1\), contradicting the fact that the local graph is a disjoint union of cliques.

At the remaining endpoint, the intersection array is Hammingâs; Kivvaâs cited endpoint classification leaves Hamming or Doob, and the manuscriptâs large-valency estimate eliminates Doob. The relevant published Kivva results and their hypotheses are present in the cited source. îciteîturn321420view1îturn321420view2îturn321420view3î

Most importantly, I found **no hidden reliance on the earlier computer-generated list of admissible tuples**. The current proof treats the parameter cases analytically.

## Two smaller clarifications I patched

The manuscript originally allowed the reader to infer \(y_2<1\) from a bound that is insufficient when \(m=2\). This is harmless because:

- when \(t=2\), the relevant product is empty and only \(u_1>0\) is needed;
- when \(t\ge3\), strict growth forces \(m\ge3\), and the displayed bound does give \(y_2<1\).

I made that split explicit.

At the Hamming endpoint, I also replaced a compressed sentence about the \(\psi_i\) with a maximal-index argument: assuming some \(\psi_j\ge2\), take the largest such \(j\), use \(\psi_{d-1}=1\), and derive the required contradiction. This eliminates an avoidable logical jump.

## Independent computation

I wrote a separate exact-rational checker from scratch rather than modifying the supplied one. It reconstructs the scalar constraints and every relaxed \(FR\)-case independently.

It passed through \(d=120\). The smallest relaxed certificate encountered was approximately

\[
FR=1.0079777384\ldots,
\]

still strictly above \(1\).

That finite test is only regression evidence. The manuscriptâs infinite ranges are handled analyticallyâfor example, the central \(F\)-estimate reduces to

\[
6d^3-10d^2-8d-5>0,
\]

and after writing \(d=x+3\), this becomes

\[
6x^3+44x^2+94x+43>0.
\]

## Bottom line

My current assessment is:

\[
\boxed{
\begin{array}{c}
\text{The original manuscript needs two mandatory corrections,}\\[2mm]
\text{but I found no fatal gap in the corrected proof of}\\[2mm]
\operatorname{motion}(X)\ge \dfrac{n}{12d^3}.
\end{array}
}
\]

The theorem would improve the published diameter dependence in this direction from \(d^{-6}\) to \(d^{-3}\), while retaining Johnson and Hamming as the exceptional families. Pyber and Skresanovâs published result supplies the \(d^{-6}\)-scale benchmark and the structural framework on which the manuscript builds. îciteîturn572917search0îturn238390view0î

I would now send the **patched** version, not the preceding PDF, to Claude and to a human specialist. The four best targets for an independent attack are:

1. uniformity of the directed geodesic loads in the coherent configuration;
2. the exact hypotheses and order of Metsch plus BangâKoolen;
3. the passage \(FR>1\Rightarrow f_1<k\Rightarrow\) a forbidden local eigenvalue;
4. exhaustion of the \(R\)-factor cases and the Hamming/Doob endpoint.

Agreement between my audit and Claudeâs would be meaningful evidence. It would still not replace review by someone working in distance-regular graphs or association schemes.

## Audit files

[Hostile referee report](sandbox:/mnt/data/babai_motion_adversarial_referee_report.pdf)

[Referee report source](sandbox:/mnt/data/babai_motion_adversarial_referee_report.tex)

[Adversarially patched proof](sandbox:/mnt/data/babai_motion_d3_adversarially_patched.pdf)

[Patched LaTeX source](sandbox:/mnt/data/babai_motion_d3_adversarially_patched.tex)

[Exact patch diff](sandbox:/mnt/data/babai_motion_d3_adversarial_patch.diff)

[Independent exact-rational checker](sandbox:/mnt/data/adversarial_independent_check.py)