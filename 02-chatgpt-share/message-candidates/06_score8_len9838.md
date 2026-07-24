## How significant would this be?

Assuming Fable performs a genuinely adversarial, line-by-line reviewâchecking the imported theorems and not merely rerunning the algebraâand finds no error, I would describe the manuscript as:

> **A substantial quantitative advance toward Babaiâs motion conjecture, with potentially reusable techniques, but not a resolution of the conjecture.**

Babaiâs conjecture asks for a universal constant \(c>0\) such that every primitive distance-regular graph outside the Johnson and Hamming families has motion at least \(cn\), independent of its diameter. Kivva proved the bounded-diameter form, with diameter-dependent constants. Pyber and Skresanovâs published advance replaced the earlier exponential dependence with a polynomial bound on the scale \(n/d^6\). The proposed theorem improves that to the explicit bound \(n/(12d^3)\). îciteîturn222988search1îturn222988search12îturn222988search0î

That matters for four reasons.

### 1. It removes three powers of the principal parameter

The headline is not the constant \(1/12\). It is

\[
d^{-6}\longrightarrow d^{-3}.
\]

This is a genuine exponent improvement, not cosmetic constant chasing. Since distance-regular graphs of valency greater than two satisfy \(d\le 5\log_2 n\), the theorem would imply

\[
\operatorname{motion}(X)
\ge
\frac{n}{1500(\log_2 n)^3},
\]

rather than a bound on the scale \(n/(\log n)^6\). It still falls short of Babaiâs desired \(cn\), because the logarithmic denominator remains. îciteîturn222988search12î

### 2. It strengthens downstream permutation-group bounds

PyberâSkresanov use motion to control the **thickness** of the automorphism groupâthe largest alternating degree occurring as a section. Their cited Wielandt bound says that motion at least \(\alpha n\) yields thickness at most roughly \(3\alpha^{-1}\log n\). Substituting \(\alpha=1/(12d^3)\) gives

\[
\text{thickness}\le 36d^3\log n,
\]

and therefore \(O((\log n)^4)\) when \(d=O(\log n)\), improving their \(O((\log n)^7)\) consequence. Running the rest of their argument under the same extra edge-transitivity hypotheses would improve the associated base-size exponent from \(O((\log n)^9)\) to \(O((\log n)^6)\). This is an inference obtained by inserting the proposed theorem into their published pipeline, not a separate theorem currently written in the manuscript. îciteîturn165221view0îturn165221view2î

### 3. The techniques may outlive the numerical theorem

The most reusable pieces appear to be:

- the exact adjacent-pair distinguishing formula;
- the support-sensitive conversion from a small automorphism to strong local intersection inequalities;
- retaining the full Metsch expression to force \(m\le d\);
- the direct geodesic PoincarÃ© inequality
  \[
  k-\theta_1\ge
  \frac{n^2k}{\sum_{x,y}\operatorname{dist}(x,y)^2}
  \ge \frac{k}{d^2};
  \]
- the multiplicative standard-sequence argument in the difficult \(\mu=2\) case.

Even if a later argument improves \(1/12\), these mechanisms could be the enduring contribution. The PoincarÃ© lemma in particular should be separated, literature-checked, and possibly circulated as a standalone proposition for coherent configurations.

### 4. It identifies the next real obstruction

The proof explains why its structural route naturally stops at \(d^{-3}\): small support gives roughly \(\mu\lesssim \rho k\), the clique argument gives \(m=O(d)\), and local overlap gives \(\lambda\gtrsim k/d\). The BangâKoolen condition \(m^2\mu<\lambda\) then asks for \(\rho=O(d^{-3})\).

That is conceptually useful. It says that getting from \(d^{-3}\) to Babaiâs diameter-independent constant will probably require a stronger route to geometricityânot merely another round of optimizing constants.

## How I would position it publicly

The best posture is:

> **Theorem first, provenance immediately afterward. Not AI-first, and not AI-hidden.**

Do not headline it as âAI solves Babaiâs conjecture.â It does not solve the conjecture, and that framing would cause mathematicians to dismiss the announcement before reading the proof.

Do not say âverified by Fable.â Say:

> âA separate adversarial model audit of the frozen manuscript found no error; the full report is public. The preprint remains unrefereed.â

Before posting, the paper should also have a responsible human author and contact address on the title page, a frozen version number, a changelog, and a clear contribution statement describing the AI assistance. The current anonymous âMACHINE-ASSISTED PROOF DEVELOPMENTâ presentation will make readers wonder who is taking responsibility for the mathematics.

The public package should contain:

- a stable preprint link, ideally arXiv;
- LaTeX source;
- the exact and symbolic audit scripts;
- the complete Fable prompt and report;
- a one-page proof dependency map;
- a clearly labeled section titled âMost delicate point,â identifying Proposition 7.1.

For the visual, use a clean theorem card rather than a screenshot of the first PDF page:

> **How much must a symmetry move?**  
> Primitive distance-regular graph  
>   
> Published: \(\Omega(n/d^6)\)  
> Proposed: \(\ge n/(12d^3)\)  
>   
> Exceptions: Johnson and Hamming graphs  
> Status: unrefereed; independently adversarially model-audited

## Paste-ready Twitter thread

All ten posts below are within Twitterâs 280-character limit. The published comparison points come from Kivva and PyberâSkresanov. îciteîturn222988search1îturn222988search12îturn165221view0î

> **1/10** How much of a highly regular network can a genuine symmetry leave untouched?
>
> New unrefereed preprint: for primitive distance-regular \(X\) on \(n\) vertices, diameter \(d\ge3\), either \(X\) is Johnson/Hamming or
>
> motion(\(X\)) \(\ge n/(12d^3)\).
>
> Published dependence: \(d^{-6}\).

> **2/10** âMotionâ is the fewest vertices moved by any nontrivial symmetry of a graph.
>
> So the theorem says: outside two exceptionally structured families, a symmetry cannot make a tiny local change. It must rearrange a quantitatively large part of the whole network.

> **3/10** Distance-regular graphs are networks whose distance statistics look the same from every vertex. The exceptions are coordinate-like: Hamming graphs encode strings; Johnson graphs encode fixed-size subsets. Their abundant coordinate symmetries are why they stand apart.

> **4/10** Babai conjectured a diameter-independent bound motion(\(X\))\(\ge cn\), apart from Johnson and Hamming graphs.
>
> This does NOT settle that conjecture. It advances the published diameter dependence from \(n/d^6\) to the explicit \(n/(12d^3)\).

> **5/10** The proofâs spine:
>
> a symmetry with tiny support  
> \(\Rightarrow\) adjacent pairs share many neighbors while distance-2 pairs share few  
> \(\Rightarrow\) large clique geometry  
> \(\Rightarrow m\le d\)  
> \(\Rightarrow\) Johnson/Hamming structure, or contradiction.
>
> This removes three separate losses of \(d\).

> **6/10** Two ingredients may be useful beyond this theorem:
>
> â¢ an exact count of vertices distinguishing an adjacent pair;  
> â¢ a direct geodesic PoincarÃ© bound  
> \(k-\theta_1\ge n^2k/\sum_{x,y}\mathrm{dist}(x,y)^2\ge k/d^2\)
>
> for symmetric relations in homogeneous coherent configurations.

> **7/10** In the valency \(>2\) regime, \(d\le5\log_2 n\), so the theorem gives
>
> motion(\(X\)) \(\ge n/[1500(\log_2 n)^3]\).
>
> Through PyberâSkresanovâs pipeline, thickness improves \(\log^7\to\log^4\); with their extra transitivity hypotheses, base size \(\log^9\to\log^6\).

> **8/10** Proof status matters: this was developed with AI assistance. The manuscript identifies every imported theorem and includes exact-rational and symbolic audits. A separate hostile model review found no error.
>
> That is meaningful evidence. It is not peer review.

> **9/10** The place to attack is Proposition 7.1: the \(\mu=2\) standard-sequence/multiplicity argument and its interfaces with Kivvaâs results.
>
> The most useful response is not âlooks good/badâ; it is the earliest exact line where a hypothesis, inequality or citation fails.

> **10/10** PDF, LaTeX, audit scripts and the independent review are all public here: [LINK]
>
> Iâm looking especially for readers in distance-regular graphs, association schemes, algebraic combinatorics and permutation groups. Corrections will be versioned openly.

## A separate quote-tweet for the AI angle

Post this only after the mathematical thread, so the model story does not eclipse the theorem:

> Yes, AI was materially involved in developing and auditing this proof. No, agreement between models is not peer review. That is why the PDF, LaTeX, dependency ledger, audit code and full adversarial report are public. Judge the mathematicsâand show the first line that fails.

## What not to say

Avoid all of these:

- âBabaiâs conjecture has been solved.â
- âFable verified the theorem.â
- âAI has surpassed graph theorists.â
- âThis is the first AI-generated major theorem.â
- âNo mistakes are possible.â
- âThe constant \(1/12\) is optimal.â

The strongest credible message is:

> **An explicit \(d^{-3}\) advance toward Babaiâs motion conjecture has survived two adversarial machine audits. The complete proof and audit trail are public, and specialists are being invited to attack the most delicate proposition.**

That framing is ambitious enough to attract attention, precise enough for mathematicians, and transparent enough that a later correction would not destroy trust.

[Complete proof manuscript](sandbox:/mnt/data/babai_motion_d3_complete_proof.pdf)

[LaTeX source](sandbox:/mnt/data/babai_motion_d3_complete_proof.tex)

[Complete audit package](sandbox:/mnt/data/babai_motion_d3_c12_audit_package.zip)