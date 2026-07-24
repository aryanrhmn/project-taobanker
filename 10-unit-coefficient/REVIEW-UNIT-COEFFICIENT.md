# Fable review — the unit-coefficient manuscript, motion(X) >= n/d^3

**Referee:** Claude Fable 5 (same adversarial standard as all prior reviews in this repo)
**Date:** 2026-07-24
**Object:** `babai_motion_d3_unit_coefficient_source_crosswalk.pdf` (18 pages, sha256_16 `fdc6529c6aeae816`), received directly from the author. Text extraction in `extracted-text.txt`.

## Verdict

```
VALID AS WRITTEN
```

Every new module was independently verified by hand; every finite and scalar certificate was independently re-implemented and reproduced **bit-exactly** (`fable_unit_checker.py`, output archived). No invalid implication, missing hypothesis, reversed inequality, or source mismatch was found. This is the strongest validated claim in the project — Babai's conjectured linear motion bound now holds with **coefficient exactly 1 on the d^3 scale, for every d >= 3**.

## Why this constant was supposed to be impossible, and how the manuscript gets it

The previous validated claim (n/(11.346 d^3)) sat exactly 13/40500 below the provable limit of the old architecture, which was pinned by Kivva's universal Johnson threshold (eps_K ~ 0.00655) and independently blocked by the mu=2 loss envelope (~coefficient 6) and the mu=1 motion floor (~coefficient 4/d relative). The unit manuscript replaces all three bottlenecks with new arguments — and one more for the geometricity constant:

1. **Metsch-to-geometric parameter split (Prop. 4.1).** Metsch's full parameterized line theorem (verified verbatim as Kivva Thm. 2.12, arXiv numbering) is applied with s = d; the resulting line geometry satisfies an integer count m <= q_v <= d for the lines through each vertex (q_v >= m via the Delsarte bound — a two-line argument). If m <= d-1, geometricity follows from published Bang-Koolen/PS Prop. 2.5 (the manuscript's KB10 Thm. 5.3 citation is offline-unverifiable but redundant: PS 2.5, verified verbatim, suffices, as the manuscript itself notes). If d-1 < m <= d, integrality forces q_v = d exactly, and Kivva's clique-geometry criterion (Prop. 2.13 arXiv, verified verbatim: exact-m clique geometry + k >= m^2 => geometric) gives m = d. Both scalar hypotheses of Metsch at s = d reduce to polynomial certificates (d^3-2d^2+d-1 > 0 and d^3-d^2-2d-2 > 0) — verified by hand and shifted-coefficient check.
2. **Local-grid Johnson argument (Prop. 6.1) — replaces the eps_K threshold entirely.** For connected local graphs with mu >= 3, the m Delsarte cliques through a vertex partition its neighborhood into m parts of size beta with a psi_1-regular bipartite graph between any two parts. A trace-averaged singular value bound plus interlacing against Terwilliger's local bound (only b+ < 13/12 needed, i.e. eps <= 1/13 — versus the old eps < 0.00655!) forces the between-part matchings to be perfect (psi_1 = 2); a Fourier-mode computation (characteristic polynomial x^3 - 3x - 2 Re zeta, verified exactly) forces global consistency of the matchings, so every local graph is exactly the grid K_m x K_beta = L(K_{m,beta}). Kivva's Lemma 3.12 + Theorem 3.9 then force mu = 4, and Kivva's Theorem 2.21 (with the k >= m^3 exclusion of the double cover, verified verbatim in his Thm 1.2 proof) gives Johnson. Every step verified by hand, including the mu=3 case (psi_1 = 1 forces disconnected local graphs, handled by Kivva Prop. 3.11).
3. **mu = 1 with Kivva's exact factors (Prop. 6.2).** Retains the exact dual eigenvalue shift (Lemma 2.27) and the exact incidence factor beta/(beta+1) from Lemma 5.5 (verified verbatim; Kivva's own Cor. 5.6 weakens it to 1/2), combined with the geodesic Poincare gap 1/d^2 (the inequality independently verified twice before in this project). Final chain: motion/n > (2m/(m-1)) (beta/(beta+1))^2 / d^3 >= (81/50)/d^3 > 1/d^3 — verified by hand (beta >= 10 from beta > d^2 >= 9).
4. **mu = 2 exact-envelope certificate (Prop. 7.1 + Lemma 7.2).** The same Riccati/one-sphere strategy as the validated predecessors, but with exact rational envelopes at the much larger eps = 2/(d^3-1) (= 1/13 at d = 3, where the old A < 6/5 machinery fails outright). Structure: coarse envelope scan over every admissible (d, m, t, r) for 3 <= d <= 52; nineteen exceptional rows, each closed by a beta-refined certificate (one-term, +t-sphere, or bridge-to-cutoff with a monotonicity argument); an analytic tail for d >= 53. Two audit corrections from the exploratory draft are explicitly flagged and correct: the endpoint denominator uses psi_{t-1} <= c_t (never an unsupported tau_t >= t), and the m=2 exclusion applies Terwilliger at index i=2 (valid range), where it yields b_1 >= b_2 + b_1, impossible. New exact eliminations (verified by hand): c_m = m+1 is impossible at t = m < d (via psi_{m-1} = 1 forcing c_m <= m), giving c_t >= m+2 there; and c_d in {m} union {>= 2m} at t = m = d.

## The independent reproduction (the decisive check)

The manuscript's C++ checker is not attached. I re-implemented the entire certificate layer from the displayed formulas alone (`fable_unit_checker.py`) in exact rational arithmetic. Results (`fable_unit_checker_output.txt`):

- **Coarse scan, 3 <= d <= 52: exactly 19 exceptional tuples — identical to the manuscript's nineteen rows**, including the (d, d, d-1, 1) family for 7 <= d <= 15; envelope positivity floor min(1 - Y_i) = 0.388355 (claim: > 0.388).
- **All nineteen beta_0 values match the manuscript's table exactly** (10, 27, 64, 94, 38, 65, 151, 90, 72, 229, 147, 224, 324, 450, 605, 792, 1014, 1274, 1575).
- **All nineteen refined certificates pass**, with the worst value **1.0000005977102229 at the gen121211 cutoff — matching the manuscript's displayed decimal to all sixteen digits.** Bridge intervals verified integer-by-integer with beta-exact tails; cutoffs verified with the sup-tail monotonicity argument (monotonicity itself verified by hand: c >= t-1 >= i+1 makes every refined denominator nondecreasing in beta).
- **Larger-c_t coverage** for every exceptional row (next admissible value: c+1, or 3m at t = m = d): all pass in the coarse envelope.
- **d >= 53 tail: all three exact rational margins reproduced digit-for-digit** — Delta_53 margin 2465298954227032982505949/141425508012555648280913514000, H_62 < 24/5 margin 17262497921202896432747309/197044480683803711251893600, and the final chain margin 913198321/8515420160; plus the supporting inequalities (9d^2-118d-91 > 0 at d = 64; eps < 65/(32d^3); d*eps < 1/2000; m*eps < 1/50 at d = 53) and the H_{d-2} <= (3/5)sqrt(d) induction (verified by hand).

An independent implementation agreeing bit-for-bit with thirty-plus displayed constants is far stronger evidence than re-running the original checker would have been.

## Import layer

All load-bearing imports are statements previously verified verbatim against the archived PDFs (`03-source-papers/`): PS Props. 2.4, 2.5, 2.8 (+ its proof's penultimate inequality), 2.10, 2.12, 2.13; Kivva Thm. 2.12 and Prop. 2.13 (arXiv), Lemmas 2.14/2.17-2.20 (journal) = 2.13/2.16-2.19 (arXiv), Cor. 2.8, Thms. 2.6, 2.10, 3.1, 3.9, 2.21, 4.1, Lemma 3.12, Prop. 3.11, Lemma 4.2, Lemmas 2.26-2.27, 5.1, 5.5, Prop. 5.13, Thm. 2.24/2.25 (Egawa). Two citations are not offline-verifiable — Koolen-Bang Thm. 5.3 (paper not archived) and Babai-Wilmes Thm. 1.2 — but both are explicitly redundant with verified statements (PS 2.5; Kivva 2.12), so nothing load-bearing rests on them. The per-equation provenance tags ([PS]/[K]/[Met99]/[KB10]/[Biggs71]/[T85]/[T86]/[Ega81]/[LLM]) now point to original sources at the point of use, exactly as Kivva's audit request asked.

## Caveats and missing artifacts

1. **Machine review, not peer review.** The local-grid rigidity argument (Prop. 6.1) and the Metsch-to-geometric split (Prop. 4.1) are genuinely new mathematics; a specialist should read them. They are short (about a page each) and elementary given the verified imports.
2. **Received as PDF only.** The .tex source, `verify_unit_coefficient.cpp`/`.out`, and the referenced intermediate 2n/(3d^3) draft are not yet archived. None affect the verdict (the PDF is the document of record and was read in full; my checker independently replaces theirs), but the author should supply them for lineage completeness.
3. **The manuscript's own barrier remark (9.1) is accurate and worth quoting:** a uniform coefficient strictly larger than 1 on the d^3 scale requires a new idea for smallest eigenvalues just below d — the Bang-Koolen band — not tighter scalars. Coefficient 1 is the natural terminus of this architecture.

## Constant ladder, final

| Claim | Status |
|---|---|
| **motion >= n/d^3 (unit)** | **VALID AS WRITTEN — the validated headline claim** |
| motion >= n/(11.346 d^3) | VALID AS WRITTEN (superseded fallback) |
| motion >= n/(14 d^3) | VALID AS WRITTEN (fallback) |
| motion >= n/(13 d^5) | VALID AS WRITTEN (fallback) |
| 2n/(3 d^3) intermediate | referenced by the unit draft; not yet archived; superseded by the unit result |
| 2n/(5 d^3) | still numerically the strongest candidate (= n/(2.5 d^3)) but conditional on the unpublished Lv-Koolen preprint + enumeration; unvalidated — the unit result is the strongest *validated* claim |
| n/(12 d^3) | historical; superseded |
