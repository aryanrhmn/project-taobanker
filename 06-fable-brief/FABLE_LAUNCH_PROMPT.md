# Fable 5 launch prompt (paste / CLI)

You are Claude Fable 5. Execute the adversarial referee mission for project-taobanker.

## Urgency context

@taobanker publicly asked for Fable ASAP after **Professor László Babai emailed back** and **forwarded the manuscript to Bohdan Kivva** (see `01-x-post/POST-2-BABAI-REPLY.md`). Babai also asked about LLM disclosure and what is “adversarial” about the “adversarial patch” filename — answer the **math** first; meta notes secondary.

## Your job

1. Read `CLAUDE.md`, `06-fable-brief/FABLE_TASK.md`, and `06-fable-brief/HOSTILE_REFEREE_PROMPT.md`.
2. Perform a hostile, line-by-line review of the candidate motion proofs in `04-proof-assets/`, checking imports against `03-source-papers/`.
3. Account for **version drift** (`VERSION_MATRIX.md`): different drafts claim \(2n/(5d^3)\), \(n/(12d^3)\), \(n/(14d^3)\), \(n/(13d^5)\), etc. Audit each draft under **its own** theorem; separately score the public \(n/(12d^3)\) claim.
4. Optionally run the Python exact-arithmetic scripts; treat them as non-authoritative for graph theory.
5. Write deliverables:

   - `06-fable-brief/VERDICT.md`
   - `06-fable-brief/FINDINGS.md`
   - `06-fable-brief/DEPENDENCY_LEDGER.md`
   - `06-fable-brief/CONSTANT_AUDIT.md`
   - optional `06-fable-brief/AUDIT_RUN_LOG.txt`

6. Primary verdict must be exactly one of:
   `VALID AS WRITTEN` | `GAP FOUND` | `SOURCE MISMATCH` | `UNRESOLVED`

Prefer the **earliest fatal flaw**. Do not polish the proof. Do not require network access.

Begin now. Work until deliverables are written.
