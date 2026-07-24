# Strengthened source-annotated revision notes

## Main result

The source-annotated manuscript now proves the uniform bound

\[
\operatorname{motion}(X)\ge \frac{500n}{5673d^3}
=\frac{n}{11.346\,d^3}
\]

outside the Johnson and Hamming families.

The earlier denominator `12 d^3` is replaced by the exact rational coefficient

\[
C_0=\frac{5673}{500}=11.346.
\]

## Scope of the strengthening

This is a scalar retuning only. It does not alter the structural reduction, the geodesic Poincare argument, the analytic `mu=2` endgame, or any classification interface.

The diameter-dependent proposal approaching a denominator `4 d^3` was not incorporated. It would require a piecewise optimization section and would make Bohdan Kivva's source audit substantially less readable.

## Exact Johnson-threshold certificate

The only source interface requiring more precision than in the `12 d^3` version is the connected-neighborhood Johnson theorem.

The revision now points directly to Kivva's Theorem 3.5, Proposition 3.6, and Theorem 1.2. If `theta_1` is Kivva's smallest root of

\[
x^2(x^2-1)^2(x^2-3)(x^2-4)=1,
\]

then Kivva defines

\[
\epsilon_K=\frac{-2-\theta_1}{-1-\theta_1}.
\]

The manuscript supplies the exact rational bracket

\[
\epsilon_K>\frac{3}{458}.
\]

It is certified by monotonicity on the interval below `-2` and the exact evaluation

\[
455^{10}p(-913/455)=-12841664057813389062001<0.
\]

At `d=3`, the new proof parameter satisfies

\[
\epsilon\le \frac{1000}{152671}<\frac{3}{458},
\qquad
\frac{3}{458}-\frac{1000}{152671}=\frac{13}{69923318}.
\]

This is the tightest source-dependent comparison introduced by the strengthening.

## Other changed scalar certificates

The structural inequalities were rechecked with `C_0=5673/500`. The final loss estimate is now certified by

\[
2673d^3-5000d^2-4000d-2500>0,
\]

and, after writing `d=x+3`,

\[
2673x^3+19057x^2+38171x+12671>0.
\]

All other source hypotheses remain unchanged and are displayed at their application points.

## Provenance standard

Every displayed equation has an immediate provenance label. Every non-structural mathematical paragraph contains a provenance label. New material introduced by the retuning is marked with labels such as

- `[LLM; strengthened scalar retuning]`
- `[LLM exact rational certificate]`
- `[K, Theorem 3.5 and Proposition 3.6; LLM exact root bracket]`

The final source contains 330 provenance tags:

- 284 containing `LLM`
- 50 containing `PS`
- 62 containing `K`

Mixed labels are counted in more than one category.

## Verification completed

- The strengthened exact-arithmetic checker passed every symbolic and rational test.
- The provenance checker found no untagged displayed equation or non-structural prose paragraph.
- LaTeX compiled twice without overfull boxes, underfull boxes, undefined references, or LaTeX errors.
- The final PDF contains 14 text-based pages and passed PDF preflight.
- The PDF was rendered at 180 dpi and visually inspected, including the title page, exact Johnson-threshold page, completion/dependency page, and bibliography page.
