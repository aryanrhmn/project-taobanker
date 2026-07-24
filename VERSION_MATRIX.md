# Version matrix — do not collapse these claims

Machine drafts in the share **evolved and sometimes retracted**. Treat each row as a separate object of review.

| Label | Claim | Where it appears | Self-status in package |
|-------|-------|------------------|------------------------|
| Social / X | “6th degree → 3rd degree” | `01-x-post/POST.md` | Informal public claim |
| Share narrative (late) | \(\operatorname{motion}(X)\ge n/(12d^3)\) | ChatGPT share prose; docstring of `babai_motion_d3_audited_scalar_check.py` | “complete internally audited… awaiting independent verification” |
| complete_proof | \(\mathrm{mot}(X)\ge n/(14d^3)\) | `babai_motion_d3_complete_proof.tex`, `babai_motion_d3_README.txt` | “Complete unrefereed proof draft” |
| final_candidate | \(\mathrm{mot}(X)\ge 2n/(5d^3)\) | `babai_motion_d3_final_candidate.tex`, twitter thread 1/10 | “machine-generated candidate” |
| sharpened (script) | \(n/(8d^3)\) scale | `babai_motion_d3_sharpened_audit.py` docstring | Intermediate |
| d5 conservative | \(\mathrm{mot}(X)\ge n/(13d^5)\) | `babai_motion_d5_source_audited.tex`, `README_babai_motion_d5_audit.md` | Source-conservative candidate |
| d5 README retraction | Withdraws \(d^{-3}\) constants including **\(1/12\)**, \(2/5\), \(1/8\) | `README_babai_motion_d5_audit.md` | Explicit retraction of some \(d^{-3}\) theorem claims |
| twitter fallback | \(n/(15d^3)\) | `babai_motion_twitter_thread.txt` | Mentioned as source-conservative fallback |

## Published baseline (not a candidate)

| Result | Form | Source |
|--------|------|--------|
| Pyber–Skresanov | motion lower bounds on scale \(n/d^6\); structural dichotomy involving ~\(n/(40d^5)\) or Delsarte geometry with eigenvalue scale \(-5d\) | `03-source-papers/pyber-skresanov-2312.00383.pdf` |
| Kivva | geometric DRG tools, local eigenvalues, Hamming/Doob endpoints, etc. | Kivva PDFs in `03-source-papers/` |

## How Fable should report

In `CONSTANT_AUDIT.md`, fill a row for each label above with:

- **Supported by its own manuscript?** (yes / no / partial)  
- **Earliest failure (if any)**  
- **Relation to public \(n/(12d^3)\) claim**


---

## Update (2026-07-24) — final state after the full review cycle

The matrix above is the historically accurate pre-review state. Final scoreboard after the Fable review, Kivva's feedback round, and the file recoveries:

| Label | Claim | Final status |
|-------|-------|--------------|
| strengthened (r2) | motion >= 500n/(5673 d^3) = n/(11.346 d^3) | **VALID AS WRITTEN — the validated headline claim.** Manuscript of record in `08-strengthened-manuscript/`; review in `07-revision-r2/REVIEW-STRENGTHENED.md` |
| complete_proof | motion >= n/(14 d^3) | VALID AS WRITTEN (validated fallback) |
| d5 conservative | motion >= n/(13 d^5) | VALID AS WRITTEN (bulletproof fallback) |
| c12 / share narrative | motion >= n/(12 d^3) | Manuscript recovered from the author (`09-first-session-originals/`), audited twice in the r2 session, chain of custody verified; superseded by 11.346 |
| final_candidate | motion >= 2n/(5 d^3) | Still conditional (unpublished Lv-Koolen preprint + enumeration); the open upgrade path |
| sharpened / twitter fallback | 1/8, 1/15 | Historical iterations; superseded |

Full lineage (every arrow byte-verified): 12-draft -> adversarial patch -> c12 (sent to Babai/Kivva) -> r2 corrections + provenance tags -> strengthened 11.346.
