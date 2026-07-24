# VERDICT

**Referee:** Claude Fable 5 (adversarial independent review, offline package only)
**Date:** 2026-07-23
**Primary target:** `04-proof-assets/babai_motion_d3_complete_proof.tex` (boxed claim: motion(X) >= n/(14 d^3))

## Primary verdict

```
VALID AS WRITTEN
```

After a full hostile line-by-line pass — every new implication independently rederived, every imported theorem checked verbatim against the published PDFs in `03-source-papers/` (not against the manuscript's paraphrase) — I found **no invalid implication, no missing hypothesis, no reversed inequality, and no source mismatch** in `babai_motion_d3_complete_proof.tex` under its own boxed constant n/(14 d^3). The same holds for the conservative fallback `babai_motion_d5_source_audited.tex` (n/(13 d^5)), whose delicate mu=2 branch is a pure application of the published Hamming characterization (Pyber–Skresanov Prop. 2.21 / Kivva Cor. 4.8) with all hypotheses explicitly satisfied.

This is a machine adversarial review, not specialist peer review or formal verification. "Valid as written" means: I attacked every step listed in the hostile-referee checklist (mu=2 standard-sequence/multiplicity interface, support-sensitive geodesic boundary, full Metsch => m<=d, transition and spectral branches, endpoint eliminations, orientation/factor-of-two accounting, constant bookkeeping) and every attack failed. Residual risk is confined to (a) my own fallibility and (b) the correctness of the published imported theorems themselves, which were audited only as stated in the PS/Kivva PDFs supplied.

## Per-version sub-verdicts (see CONSTANT_AUDIT.md)

| Asset | Own claim | Sub-verdict |
|---|---|---|
| `babai_motion_d3_complete_proof.tex` | n/(14 d^3) | **VALID AS WRITTEN** (no flaw found; all imports published and hypothesis-matched) |
| `babai_motion_d5_source_audited.tex` | n/(13 d^5) | **VALID AS WRITTEN** (imports are published PS statements only) |
| `babai_motion_d3_final_candidate.tex` | 2n/(5 d^3) | **UNRESOLVED (conditional)** — the mu>=3 branch imports Lemma 17 and Theorem 32 of an unpublished Jan-2026 Lv–Koolen preprint (arXiv:2601.10330) that is *not in the offline package*; for d in {3,4} the published route (PS Prop. 2.19, eps* ~ 0.0065) cannot replace it at this constant. Additionally d<=16 rests on declared exact-rational computer enumeration (reproduced successfully; see AUDIT_RUN_LOG.txt). Everything I *could* check verifies, including the new geodesic Poincare inequality k - theta_1 >= k/d^2. |
| Public / social claim | n/(12 d^3) | **WITHDRAWN / UNSUPPORTED IN PACKAGE** — no trusted extracted TeX proves 1/12; it survives only in a script docstring and in the untrusted `_suspect-not-true-file-content/` extractions, and the package's own `README_babai_motion_d5_audit.md` explicitly withdraws it. The defensible public statement is n/(14 d^3), not n/(12 d^3). |

## Headline significance (if the above survives specialist review)

The manuscript's principal new content is real and checkable: it replaces Kivva's published mu=2 surplus 1 + 1/(m^2-1) (Prop. 4.6, which forces eps < 1/(6 m^4 d), i.e. d^-5 scale) with a sharper analytic surplus R >= 1 + 1/m and a sharper per-step Riccati loss (delta ~ 3 m eps instead of 3 m^2 eps), which together relax the dominant-distance smallness parameter to eps ~ d^-3 with no finite enumeration. Combined with the exact adjacent-pair identity and the support-sensitive oriented geodesic boundary, this yields the d^-3 diameter dependence — a genuine improvement over the published Cn/d^6 (PS Thm. 1.4) for the primitive case, short of Babai's conjectured n/C.

## Secondary meta notes (not mathematics)

1. **Babai's disclosure requests** (name/affiliation/LLM role/model identity) are unaddressed in all manuscripts; the author line reads "Machine-assisted proof draft". These should be answered before further circulation.
2. **"Adversarial patch" filename:** within the ChatGPT share this refers to a *self*-hostile audit pass over the draft (hostile-referee prompt applied to its own manuscript, then patched) — adversarial toward the proof, not toward Babai. Nothing in the package suggests otherwise.
3. Grok's "92% / 7 out of 10" posts are social framing and played no role in this review.

---

## Addendum (2026-07-24): post-freeze completeness + freshness check

An independent external audit (Grok, with live X access; report archived as `01-x-post/POST-4-FRESHNESS-SWEEP-2026-07-24.md`) checked this review's coverage against the mission spec and swept @taobanker's timeline from the package freeze to ~2026-07-24 01:40+ UTC. Results:

- **Coverage:** no material gaps found; all mission checks (per-constant audits, separate 1/12 scoring, verbatim import verification, all designated attack surfaces, deliverables) confirmed covered.
- **Freshness:** zero tangible math-package deltas after the freeze — no new manuscript, constant, or retraction; no further Babai correspondence; no Kivva or specialist response; the Lv–Koolen preprint (arXiv:2601.10330) was not posted or linked; no disclosure post answering Babai.
- **Impact:** all four sub-verdicts above stand **UNCHANGED**.
- **Clarifications prompted by the audit's soft notes:** (i) the author handoff memo exists as the package `README.md`; (ii) the three supporting Kivva PDFs were unused because every manuscript citation resolved to the two primary papers; (iii) crown graphs are intentionally absent as a finding — they are bipartite (imprimitive) and all three manuscripts assume primitivity, so the crown exception only arises in PS's imprimitive reduction, outside scope.
- **Re-review triggers:** new TeX/constants; arXiv:2601.10330 added to `03-source-papers/` (upgrades `final_candidate` only, if its hypotheses check out); concrete Babai/Kivva feedback.

---

## Addendum 2 (2026-07-24): the strengthened revision — motion(X) >= 500n/(5673 d^3)

Both re-review triggers fired: Kivva responded (feedback relayed by Babai — requesting per-equation source/[LLM] provenance annotations), and a new manuscript appeared (`babai_motion_d3_source_annotated_strengthened`, produced in a new session share `6a62ce8c-...`). Full review: `07-revision-r2/REVIEW-STRENGTHENED.md`; provenance: `07-revision-r2/CONTEXT.md`; event record: `01-x-post/POST-5-KIVVA-FEEDBACK-R2-2026-07-24.md`.

**Sub-verdict (initial, same day): NO FLAW FOUND — CONDITIONALLY VALIDATED.** The strengthened claim is the 1/12-lineage architecture (independently audited twice inside the new session, with conclusions matching this review's on every overlapping point) plus a single numerical retuning to C0 = 5673/500 = 11.346, recovered verbatim via the session's patch script. All 17 exact-arithmetic certificate checks pass (`07-revision-r2/r2_exact_audit.py`), including the critical exact Johnson-threshold comparison eps(3) = 1000/152671 < 3/458 < eps_K — note the published rounded bound "eps* > 0.0065" of PS Prop. 2.19 is insufficient at this constant, and the manuscript correctly imports Kivva's exact threshold (Thm. 3.5 + Prop. 3.6, Bussemaker–Neumaier) instead. The constant-free surplus lemma R >= 1+1/m carries over verbatim from the validated 1/14 manuscript.

**Sub-verdict (final, upgraded 2026-07-24): `VALID AS WRITTEN`.** The author supplied the actual files (`08-strengthened-manuscript/`: .tex, 14-page PDF, bundle zip — all hash-consistent) and the session's verbatim transcript. The full assembly check was completed: complete 982-line read of the manuscript of record (every derivation verifies; it also repairs the F5 cosmetic nits of the 1/14 sibling), zero old-constant remnants, both bundled checkers re-run and passing (330 provenance tags, matching the transcript's claim exactly), and all exact certificates confirmed against the text as written. Details: `07-revision-r2/REVIEW-STRENGTHENED.md`, "Final assembly check".

The 1/14 and 1/13d^5 verdicts above are unaffected. **The validated headline claim of this package is now motion(X) >= 500n/(5673 d^3) = n/(11.346 d^3).**


---

## Addendum 3 (2026-07-24): the unit-coefficient manuscript — motion(X) >= n/d^3

The author supplied a new 18-page manuscript (`10-unit-coefficient/`) claiming the unit constant on the d^-3 scale — beyond the previously certified limit of the old architecture. It replaces all three prior bottlenecks with new modules (Metsch-to-geometric split; local-grid Johnson argument in place of Kivva's universal spectral threshold; exact mu=1 dual-spectrum/incidence factors; exact-envelope mu=2 certificate with 19 refined rows plus a d >= 53 analytic tail).

**Sub-verdict: `VALID AS WRITTEN`.** Every new module verified by hand; the absent C++ checker independently re-implemented from the displayed formulas (`10-unit-coefficient/fable_unit_checker.py`) and reproduced bit-exactly: the 19-row exception table, all nineteen beta_0 values, the worst certificate margin 1.0000005977102229 (sixteen digits), and all three exact rational tail margins. All load-bearing imports previously verified verbatim; the two offline-unverifiable citations (KB10 Thm 5.3, BW Thm 1.2) are redundant with verified statements. Full review: `10-unit-coefficient/REVIEW-UNIT-COEFFICIENT.md`.

**The package's validated headline claim is now motion(X) >= n/d^3.** The 11.346, 14, and 13d^-5 results become validated fallbacks. Still outstanding on the author's side: the .tex, the C++ checker files, and the 2n/(3d^3) intermediate draft (lineage only; verdict unaffected).
