# 08-strengthened-manuscript — the actual files (obtained from the author, 2026-07-24)

These are the output files of the r2 session that the ChatGPT share could not serve (see `../07-revision-r2/CONTEXT.md`), downloaded directly by the operator while the session's sandbox links were live. Their arrival closed the single remaining condition on the r2 review.

| File | What it is |
|---|---|
| `babai_motion_d3_source_annotated_strengthened.tex` | **The manuscript of record** (44 KB, 982 lines): motion(X) >= 500n/(5673 d^3), fully provenance-annotated |
| `babai_motion_d3_source_annotated_strengthened.pdf` | Compiled PDF (14 pages) — hash-consistent with the bundle copy |
| `babai_motion_d3_source_annotated_strengthened_bundle.zip` | The bundle the author circulated: tex + pdf + both checkers + their output logs + notes (every member hash-matches the loose files) |
| `verify_scalar_inequalities_strengthened.py` | Exact-arithmetic checker for all displayed scalar certificates — **re-run by Fable: ALL PASS** (sweep d <= 500) |
| `verify_provenance_annotations_strengthened.py` | Annotation-coverage checker — **re-run by Fable: PASS** (330 tags; every displayed equation and prose paragraph labeled) |
| `PROVENANCE_INDEX_STRENGTHENED.md` | The author-side map of [PS]/[K]/[LLM] tags (Kivva's requested distinction) |
| `STRENGTHENED_REVISION_NOTES.md` | Author-side notes on the 12 -> 11.346 retuning |
| `STRONGER_RESULT_STATUS.md` | Author-side memo (extracted from the bundle): why the earlier revision deliberately kept 12 |
| `scalar_check_output_strengthened.txt`, `provenance_check_output_strengthened.txt` | The session's own checker logs (extracted from the bundle) — consistent with Fable's re-runs |

**Not in this archive:** the original 1/12 "adversarial patch" files are now archived in `../09-first-session-originals/`; still author-side are only the intermediate r2 outputs (`babai_motion_d3_revised.*`, the non-strengthened `source_annotated.*`, `REVISION_NOTES.md`, `PROVENANCE_INDEX.md`). None are needed for the verdict — the strengthened manuscript supersedes them all — but the author can add them here any time for lineage completeness.

**Fable's final verdict on this manuscript: VALID AS WRITTEN** — see `../07-revision-r2/REVIEW-STRENGTHENED.md` (upgraded after the full line-by-line read of this exact file) and `../06-fable-brief/VERDICT.md` Addendum 3.
