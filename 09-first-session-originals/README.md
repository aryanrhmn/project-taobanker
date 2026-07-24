# 09-first-session-originals — the true bytes behind the quarantined filenames (obtained from the author, 2026-07-24)

These are the original first-session output files, downloaded by the operator directly from the author. They are the REAL versions of exactly the filenames that `04-proof-assets/_suspect-not-true-file-content/` quarantined as mis-extractions — all four hash-comparisons confirm the true files are distinct from the quarantined chat-prose artifacts (the quarantine was correct, and these fill the gap it left).

| File | What it is | Cross-reference result |
|---|---|---|
| `babai_motion_d3_adversarially_patched.tex/pdf` | **The c12 manuscript (n/(12 d^3)) — the file Babai received and forwarded to Kivva, and the seed of the r2 session** | 7/7 pre-fix states match the r2 audits exactly (the missing "distinct", no k=2 dispatch, unsafe eigenvalue phrasing, the z<1 attribution, boxed 1/12, journal numbering, mu=1 via the Poincare eta = 1/d^2 route); all r2-audit content anchors found in the PDF in order; text lineage to the validated strengthened manuscript fully classified (constant retuning + the 13 documented fixes + provenance tags + pure cosmetics — zero unexplained mathematical changes) |
| `babai_motion_d3_adversarial_patch.diff` | **The actual "adversarial patch" Babai asked about**: the first session's self-hostile audit produced two mandatory repairs (spelled-out directed-edge orientation bookkeeping in the boundary lemma; Kivva arXiv-to-journal renumbering) applied to the 12-draft | All 6 hunks verified against the c12 file: every added line present, every removed line absent, all context intact. Header shows the 20:09 UTC base was a 12-draft then named `complete_proof.tex` — same *filename* as the later-extracted n/(14d^3) manuscript, different content (parallel drafts sharing a sandbox name; this explains part of the version drift documented in `VERSION_MATRIX.md`) |
| `babai_motion_adversarial_referee_report.tex/pdf` | The first session's self-referee report: "Hostile Referee Audit ... Adversarial machine review", verdict **"PROVISIONALLY VALID AFTER MINOR CORRECTIONS"** (no fatal gap at 1/12; the two mandatory repairs = the patch above) | This document is the definitive answer to Babai's question "what is adversarial about it?" — adversarial toward the proof, not toward him |
| `adversarial_independent_check.py` | The first session's exact-arithmetic F*R checker for the 12-based mu=2 constants | **Re-run by Fable: PASSES** (all exact checks through d = 120; minimum FR ~ 1.0080) |

## What this closes

This was the last chain-of-custody gap in the public record. The full lineage is now byte-auditable end to end:

```
12-draft ("complete_proof.tex", 20:09 UTC)
  --[adversarial_patch.diff, 6/6 hunks verified]-->
c12 = adversarially_patched (.tex/.pdf here; sent to Babai -> Kivva)
  --[r2 session: audited twice; 13 fixes; provenance tags (Kivva's request); retune 12 -> 5673/500]-->
strengthened manuscript (08-strengthened-manuscript/, VALID AS WRITTEN)
```

Every arrow is backed by recovered scripts or diffs verified against the actual files, and every endpoint is hash-fingerprinted in `MANIFEST-PACKAGE.json`.

Still author-side only (optional, lowest value): the r2 intermediates (`babai_motion_d3_revised.*`, non-strengthened `source_annotated.*`) and the first session's compiled n/(14d^3) PDF and audit-package zips.
