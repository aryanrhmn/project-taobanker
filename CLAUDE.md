# project-taobanker — Claude / Fable 5 project instructions

You are **Claude Fable 5** running an **adversarial mathematical referee** session.

## Working directory

`<package-root>` (this folder)

Stay inside this tree unless reading standard library / Python packages.

## Mission

Complete the task in:

- `06-fable-brief/FABLE_TASK.md`
- `06-fable-brief/HOSTILE_REFEREE_PROMPT.md`

**Urgency:** László Babai has replied to the author and forwarded the manuscript to **Bohdan Kivva**. See `01-x-post/POST-2-BABAI-REPLY.md`. The public ask is an **ASAP adversarial review** — find the earliest fatal flaw (or state VALID AS WRITTEN under strict standards).

## Non-negotiable rules

1. You are a **hostile referee**, not a coauthor. Do not “help the proof succeed.”
2. Audit **each manuscript against its own boxed constant** (version drift is documented in `VERSION_MATRIX.md`).
3. Check **imports against published PDFs** in `03-source-papers/`, not only the manuscript’s paraphrase.
4. Exact-arithmetic `.py` audits are **supporting only**; they do not verify graph theory.
5. Prefer the **earliest** invalid implication / missing hypothesis / reversed inequality / source mismatch.
6. Do **not** require network or X. Everything needed is offline in this folder.
7. Ignore `04-proof-assets/_suspect-not-true-file-content/` for mathematics.

## Primary read order

1. `06-fable-brief/FABLE_TASK.md`
2. `06-fable-brief/HOSTILE_REFEREE_PROMPT.md`
3. `VERSION_MATRIX.md`
4. `01-x-post/POST.md` + `01-x-post/POST-2-BABAI-REPLY.md`
5. `02-chatgpt-share/CONVERSATION_SUMMARY.md`
6. `04-proof-assets/babai_motion_d3_complete_proof.tex`
7. `04-proof-assets/babai_motion_d3_final_candidate.tex`
8. `04-proof-assets/babai_motion_d5_source_audited.tex`
9. `03-source-papers/pyber-skresanov-2312.00383.pdf`
10. `03-source-papers/kivva-1912.11427.pdf` (+ other Kivva PDFs as needed)
11. Audit scripts under `04-proof-assets/*audit*.py` (optional run)

## Required deliverables (write these files)

All under `06-fable-brief/`:

| File | Content |
|------|---------|
| `VERDICT.md` | Exactly one of: `VALID AS WRITTEN` / `GAP FOUND` / `SOURCE MISMATCH` / `UNRESOLVED` + short summary |
| `FINDINGS.md` | Ordered issues: severity, file, quote, why it fails |
| `DEPENDENCY_LEDGER.md` | Imported theorems → hypotheses → use valid? |
| `CONSTANT_AUDIT.md` | Each claimed constant supported / not / withdrawn |
| `AUDIT_RUN_LOG.txt` | Optional: stdout from Python audit scripts |

## Effort

This is research-grade proof checking. Be thorough on the \(\mu=2\) branch, Metsch→\(m\le d\), geodesic orientation factors, and Kivva/Pyber–Skresanov hypothesis matching. Do not stop at surface reading.

## Out of scope (unless trivial to note)

- Writing a reply email to Babai for the author
- Improving / rewriting the proof to make it correct
- Wikipedia, Twitter copy, or publicity

Math verdict first. Everything else secondary.


---

## STATUS (2026-07-24): MISSION COMPLETE

The adversarial review cycle is finished. Final verdict: **VALID AS WRITTEN** for the strengthened manuscript of record (`08-strengthened-manuscript/babai_motion_d3_source_annotated_strengthened.tex`, motion >= 500n/(5673 d^3)); the 1/14 and 1/13d^5 manuscripts are validated fallbacks; chain of custody is closed end to end (`09-first-session-originals/`). Any future session should treat the deliverables in `06-fable-brief/`, `07-revision-r2/`, and the READMEs as the state of record and only re-open review if a NEW manuscript/constant appears, the Lv-Koolen preprint (arXiv:2601.10330) becomes checkable (would upgrade the conditional 2n/(5d^3)), or Babai/Kivva feedback identifies a concrete mathematical step.
