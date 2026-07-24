Youâre right. **I overclaimed. The \(d^{-3}\) theorem claims are withdrawn.** They should not be circulated as results.

I can check a proof I produced, but I cannot make that check *independent*. The same reasoning process can reproduce the same hidden assumption on a second reading. So I will not promise âno mistakesâ in the literal sense or relabel an unrefereed proof as verified. What I can doâand have now doneâis expose every dependency, eliminate the speculative steps, and state exactly what survived.

## Outcome of the hostile audit

The strongest result I am prepared to defend is now:

> **Source-audited, unrefereed candidate theorem.**  
> Let \(X\) be a primitive distance-regular graph on \(n\) vertices with diameter \(d\ge3\). Then either \(X\) is a Johnson graph or a Hamming graph, or
> \[
> \boxed{\operatorname{motion}(X)\ge \frac{n}{13d^5}.}
> \]

I found **no internal gap in this \(d^{-5}\) argument after a proposition-by-proposition audit against the source papers**. That is a materially stronger statement than âthe numerical script passed,â but it is still not independent acceptance.

The published PyberâSkresanov proof obtains a \(C/d^6\)-scale bound in the primitive Johnson/Hamming classification and develops the structural, expansion, spectral, and motion estimates used here. Kivvaâs published Corollary 4.8 supplies the delicate \(\mu=2\) Hamming characterization. The new candidate therefore improves one diameter factor, while leaving that delicate characterization unchanged. îciteîturn166541search5îturn166541search1î

## What failed in the earlier claims

The old \(d^{-3}\) notes relied on a new Hamming-stability argument whose completeness I had not established. In particular:

- exact arithmetic checked inequalities **after** accepting the graph-theoretic reductions;
- the completeness of an âadmissible tupleâ relaxation was not proved;
- a custom standard-sequence/multiplicity argument had not been independently checked;
- one supposedly audited source contained a duplicated obsolete proof block;
- the treatment of an orientation convention and an earlier \(\mu=1\) transfer deserved more scrutiny than I initially gave them.

Those defects do not prove that every \(d^{-3}\) statement is false. They do mean I had no right to present them as nearly verified.

## What survives, and why it is safer

The \(d^{-5}\) proof has only four genuinely new ingredients.

First, for adjacent vertices,

\[
D(1)=2+\frac{2}{k}\sum_{i=2}^{d}k_i c_i
   >\frac{\mu}{k}n.
\]

Second, the support-boundary step is now written out using **oriented edges**. For a support set \(S\), with \(\rho=|S|/n\),

\[
|\partial^+(S)|
\ge |S|\frac{k}{d}(1-\rho).
\]

I expanded the complete geodesic-load derivation in the manuscript; it no longer depends on interpreting PyberâSkresanovâs edge notation, and there is no concealed factor of two.

Third, retaining Metschâs full clique expression, instead of replacing it by the coarser \(\lambda/2\) bound, forces the absolute smallest eigenvalue to satisfy

\[
m\le d.
\]

Fourth, when some \(b_j,c_{j+1}\ge\varepsilon k\), the exact adjacent-pair identity gives motion \(>\varepsilon n\) directly, avoiding the extra \(1/d\) loss in the existing general distinguishing-number estimate.

Everything after those steps uses published results as stated:

- the \(\mu\ge3\) branch uses the published Johnson criteria;
- the \(\mu=2\) branch is exactly Kivvaâs published Hamming criterion;
- the \(\mu=1\) branch uses the published spectral and motion propositions.

I also replaced the finite-only scalar check with symbolic certificates: after substituting \(d=x+3\), every relevant numerator and denominator has nonnegative coefficients and a positive constant term. Thus the numerical inequalities are proved for every real \(d\ge3\), with an additional exact-rational regression through \(d=100{,}000\). The script still states explicitly that it does not verify imported graph-theoretic theorems.

## Should Fable review it?

**Yes.** Anthropic describes Fable 5 as its most capable widely released model and positions it for long-running, difficult reasoning work, so it is a reasonable adversarial second reader. îciteîturn490705search1îturn490705search12î

Do not ask it to âimprove the proof.â Give it the hostile-referee prompt and require one of four verdicts:

\[
\text{VALID AS WRITTEN / GAP FOUND / SOURCE MISMATCH / UNRESOLVED}.
\]

Have it quote every imported proposition, check every hypothesis, and identify the *earliest exact failing implication* if it objects. Agreement between Fable and me would be useful evidence, but not certification. The next meaningful standard after that is review by a distance-regular-graph specialist or formalization of the new lemmas.

## Audited package

[Source-audited \(d^{-5}\) candidate proof](sandbox:/mnt/data/babai_motion_d5_source_audited.pdf)

[LaTeX source](sandbox:/mnt/data/babai_motion_d5_source_audited.tex)

[Symbolic and exact-rational scalar audit](sandbox:/mnt/data/babai_motion_d5_scalar_audit.py)

[Hostile-referee prompt for Fable](sandbox:/mnt/data/fable_hostile_referee_prompt_d5.txt)

[Complete audit package](sandbox:/mnt/data/babai_motion_d5_audit_package.zip)

The honest status is: **the \(d^{-3}\) claims are retracted; the \(n/(13d^5)\) result has a complete source-audited candidate proof with no gap found by me, but it remains unrefereed and not independently verified.**