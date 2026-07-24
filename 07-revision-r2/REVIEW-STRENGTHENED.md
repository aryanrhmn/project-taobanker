# Fable review — the strengthened manuscript, motion(X) >= 500n/(5673 d^3) = n/(11.346 d^3)

**Referee:** Claude Fable 5 (same adversarial standard as `06-fable-brief/`)
**Date:** 2026-07-24
**Object:** `babai_motion_d3_source_annotated_strengthened.tex/pdf` — the provenance-annotated, strengthened revision produced in response to Kivva's feedback (see `CONTEXT.md`)

## Verdict

```
NO FLAW FOUND — CONDITIONALLY VALIDATED
(full VALID AS WRITTEN pending the manuscript file itself, which the
 ChatGPT share once again does not physically contain)
```

Everything about the strengthened claim that is recoverable has been verified, and all of it holds. What follows is exactly what was checked and what one remaining step separates this from the same unqualified verdict the 1/14 manuscript received.

## Why this claim is auditable without re-reviewing from scratch

The strengthened manuscript is, by construction, the earlier 1/12 manuscript plus (a) proof-preserving wording fixes, (b) provenance tags on every equation, and (c) **one numerical change**: the coefficient 12 becomes C0 = 5673/500 = 11.346. Its own scope box states: "no structural lemma, classification theorem, or source interface is changed." The complete patch script (`apply_strengthening.py`, recovered verbatim from the share) confirms this — every replacement it makes is a constant retuning, and its built-in occurrence assertions quote the surrounding manuscript text verbatim at every changed site.

The underlying architecture is therefore the one that has now been adversarially verified **three separate times**:

1. **Fable's line-by-line review of the sibling 1/14 manuscript** (`06-fable-brief/`): the identical D(1) identity, oriented geodesic boundary, full-Metsch => m <= d reduction, transition/low-theta machinery, the mu=2 Riccati/surplus argument (including the constant-free R >= 1+1/m case analysis, which carries over verbatim since it involves no epsilon), and the endpoint-to-Hamming endgame.
2. **The r2 session's two independent audits of the 1/12 manuscript itself** (recovered in full in `conversation-prose.md`, blocks 1 and 3). Notably, on every point where its audit and Fable's overlap — the PS 2.8 orientation conventions, the Metsch trigger, the Bang–Koolen ordering, the Kivva Cor. 4.8 trap being avoided, the mu=1 hypothesis checks — the two independent reviews reached identical conclusions.
3. **Fable's independent verification of the geodesic Poincare inequality** k - theta_1 >= k/d^2 (reconstructed and checked in the 2/(5d^3) review, `06-fable-brief/FINDINGS.md` F3), which the 1/12-lineage manuscripts use in the mu=1 branch (with PS Prop. 2.14 at eta = 1/d^2 — hypothesis k > 4md^2 verified below).

## The retuning layer — machine-verified, 17/17 exact checks pass

`r2_exact_audit.py` (output in `r2_exact_audit_output.txt`) verifies every constant-dependent inequality at C0 in exact rational arithmetic:

1. **The critical Johnson-threshold margin.** At d=3 the manuscript's eps = 1000/152671 = 0.00654959... — which EXCEEDS the rounded published bound "eps* > 0.0065" in PS Prop. 2.19, so that citation route would be insufficient. The manuscript correctly switches to Kivva's exact threshold (Thm. 3.5 = Bussemaker–Neumaier + Prop. 3.6): eps_K = (-2-theta_1)/(-1-theta_1) where theta_1 is the unique root below -2 of x^2(x^2-1)^2(x^2-3)(x^2-4) = 1. Verified exactly:
   - p(-913/455) = -12841664057813389062001/380289177849714310556640625 < 0 (reproduced digit-for-digit), and p is monotone below -2, so theta_1 < -913/455, hence eps_K > 3/458;
   - eps(3) = 1000/152671 < 3/458, margin exactly 13/69923318 as the manuscript claims;
   - the architecture's true limit C_lim = (1+2/eps_K)/27 = 11.34531821... < 919/81 < C0 = 11.346, margin exactly 13/40500. Sixty-digit numerics confirm the true threshold: eps(3) = 0.0065496 < eps_K = 0.0065504.
2. **All retuned scalar certificates** (closure identity exact; gamma < 1/2; eps < 2/(11d^3); d*eps < 1/50; eps < 1/d^2 <= 1/m^2 for the strict-growth lemma; the three structural inequalities alpha^2 > 4gamma, alpha - 3gamma/(2alpha) > 1/(d+1), alpha > (d+1)^2 gamma; b_1 > k/3; z < 1) — verified for 3 <= d <= 2000, plus the all-d shifted-polynomial certificate 2673d^3 - 5000d^2 - 4000d - 2500 = 2673x^3 + 19057x^2 + 38171x + 12671 (x = d-3, all coefficients positive).
3. **The mu=2 loss chain at the weaker smallness d*eps < 1/50** (the 1/14 manuscript used m*eps < 1/60): A < 6/5, delta < 3m*eps, q < 1, and the F-loss inequality (3d^2+2d+2)eps < 1/(d+1) — including the exact-harmonic version, stronger than the manuscript's H <= d/2 route. The surplus R >= 1 + 1/m needs no re-verification: it is constant-free.
4. **The mu=1 branch hypotheses at C0**: k > C0 d^3 > 4md^2 = 4m/eta with eta = 1/d^2 (PS Prop. 2.14; this needs only C0 > 4), motion floor n/(4d^2) > gamma n, k > m^2, k > 4 for the m=2 case, and the Doob exclusion k > 3d.
5. **Johnson branch valency checks**: k > C0 d^3 >= C0 m^3 > m^3 and C0*27 = 306.3 > 29.

## The one remaining step

The share page physically contains the session's words and tool calls but not its output files (the same ChatGPT-share limitation that affected the 1/12 manuscript — the author's diagnosis of a share glitch is confirmed: the strengthened .tex/.pdf/.zip exist only as dead sandbox links). So this review verified: the architecture (three independent passes), the patch (verbatim), and the numbers (17/17 exact). It could not lay eyes on the final assembled document, so a final check for assembly-level slips (a mis-pasted formula, a compile artifact) is still outstanding.

**To close it:** the author has the PDF and `babai_motion_d3_source_annotated_strengthened_bundle.zip`. Sending either (email, DM attachment, or committing it to this repo) upgrades this to the same full VALID AS WRITTEN as the 1/14 manuscript, likely within hours. Nothing found so far suggests that check will turn up anything.

## For Babai and Kivva, in one paragraph

The provenance annotation Kivva requested has been implemented as a machine-checked system (every displayed equation carries [PS, ...], [K, ...], or [LLM]; a checker script fails the build if any tag is missing). The strengthened constant n/(11.346 d^3) is not numerology: 11.346 = 5673/500 sits an exact 13/40500 above the architecture's provable limit (1 + 2/eps_K)/27, which is set by the Bussemaker–Neumaier constant behind Kivva's Theorem 1.2 threshold — i.e., the uniform constant in this approach is now pinned to a published spectral constant, and the binding constraint is Kivva's Johnson characterization, not the new mu=2 argument (which alone would tolerate a coefficient near 6.08). The fastest deep check of genuinely new mathematics remains the mu=2 surplus lemma (Lemma 6.6 of the 1/14 sibling in `04-proof-assets/babai_motion_d3_complete_proof.tex`, same lemma in the strengthened paper), followed by the geodesic Poincare inequality — both have survived every independent pass so far.

## Constant history, updated

| Constant | Status |
|---|---|
| n/(14 d^3) | VALID AS WRITTEN (full line-by-line, `06-fable-brief/VERDICT.md`) |
| **n/(11.346 d^3)** | **NO FLAW FOUND — conditionally validated; strongest current claim; awaiting file for final assembly check** |
| n/(12 d^3) | superseded by 11.346; the original manuscript was audited twice inside the r2 session (valid conditional) but its file remains unpublishable from the shares |
| 2n/(5 d^3) | conditional (Lv–Koolen preprint + enumeration); NOT used by the strengthened paper |
| n/(13 d^5) | VALID AS WRITTEN (conservative fallback) |
| ~n/(4 d^3) for d >= 9 (diameter-dependent) | sketched in the r2 session with a per-diameter table; deliberately NOT asserted in any manuscript; would need its own audit |
