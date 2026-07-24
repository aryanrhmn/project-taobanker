# For mathematical reviewers

This page is the entry point for anyone evaluating the mathematics. It assumes no knowledge of the project's history and routes around the archival material.

## The claim

Let X be a primitive distance-regular graph on n vertices of diameter d >= 3. Then X is a Johnson graph, a Hamming graph, or

    motion(X) >= 500n/(5673 d^3) = n/(11.346 d^3).

This sharpens the diameter dependence of Pyber-Skresanov (JCTB 172 (2025), 94-114; motion >= Cn/d^6 outside Johnson/Hamming/crown) in the primitive case, toward Babai's conjecture of a uniform linear bound.

**Manuscript of record:** [`08-strengthened-manuscript/babai_motion_d3_source_annotated_strengthened.pdf`](08-strengthened-manuscript/babai_motion_d3_source_annotated_strengthened.pdf) (14 pages; [LaTeX source](08-strengthened-manuscript/babai_motion_d3_source_annotated_strengthened.tex)). Machine-generated (OpenAI Codex lineage), machine-refereed (Claude Fable 5, adversarial standard), **not yet human-peer-reviewed** — which is where you come in.

## What is new vs. imported

Per the annotation convention requested during correspondence, every displayed equation and assertion in the manuscript carries a provenance tag: **[PS, ...]** (Pyber-Skresanov, journal numbering), **[K, ...]** (Kivva, JCTB 151 (2021), journal numbering), or **[LLM]** (derived in the manuscript). Coverage is machine-enforced: [`verify_provenance_annotations_strengthened.py`](08-strengthened-manuscript/verify_provenance_annotations_strengthened.py) fails if any displayed equation lacks a tag (330 tags; independently re-verified).

An external cross-index of all 34 imports — each published statement, its hypotheses, and the point of use — is in [`06-fable-brief/DEPENDENCY_LEDGER.md`](06-fable-brief/DEPENDENCY_LEDGER.md). Note the Kivva arXiv-vs-journal numbering concordance at its top (the ledger cites arXiv numbering; the manuscript cites journal numbering; the shift is journal Lemmas 2.17-2.20 = arXiv 2.16-2.19 and journal Theorem 2.25 = arXiv 2.24).

## Where to spend your time (fastest path to a decision)

1. **The one genuinely new lemma — the mu=2 multiplicity surplus** (manuscript Section 7). Everything else is either a published import used within its stated hypotheses or elementary. The new step replaces the surplus 1 + 1/(m^2-1) implicit in Kivva's Proposition 4.6 with the uniform R >= 1 + 1/m (manuscript inequality (39), with a four-case integer analysis over (c_t, t, r)), against the loss factor F > m/(m+1) (inequality (41)). This is what relaxes the dominant-distance smallness parameter from the eps < 1/(6m^4 d) of Kivva's Corollary 4.8 to eps ~ d^-3 with no enumeration.
2. **The geodesic Poincare inequality** (Section 3): k - theta_1 >= k/D^2 for a connected symmetric basis relation of a homogeneous coherent configuration, via distance-weighted uniform geodesic loads (a canonical-path argument riding on the uniformity in Pyber-Skresanov's Lemma 2.7 / Proposition 2.8). Used only in the mu=1 branch, where it feeds Pyber-Skresanov Proposition 2.14 at eta = 1/d^2.
3. **The exact Johnson-threshold certificate** (Section 6): the constant is deliberately tuned near the limit of Kivva's Theorem 1.2. At d = 3 the manuscript's eps = 1000/152671 ~ 0.0065496 exceeds the rounded bound "eps_* > 0.0065" quoted in Pyber-Skresanov, so the manuscript instead brackets the exact Bussemaker-Neumaier threshold: 455^10 p(-913/455) = -12841664057813389062001 < 0 gives eps_K > 3/458, and eps < 3/458 with exact margin 13/69923318. The coefficient 5673/500 sits exactly 13/40500 above the architecture's limiting value (1 + 2/eps_K)/27.

## Independent verification you can run yourself

All exact-arithmetic layers re-verify in seconds with standard Python (fractions; sympy for one script):

    python 08-strengthened-manuscript/verify_scalar_inequalities_strengthened.py
    python 08-strengthened-manuscript/verify_provenance_annotations_strengthened.py 08-strengthened-manuscript/babai_motion_d3_source_annotated_strengthened.tex
    python 07-revision-r2/r2_exact_audit.py

The third is the independent referee's audit (17 checks, including a 60-digit cross-check of the threshold root). These verify scalar/integer claims only; they do not verify graph-theoretic reasoning — that is the human step.

## The referee record

An independent adversarial review (Claude Fable 5) examined this manuscript and its two validated predecessors line by line: every new implication independently rederived, every import checked verbatim against the published PDFs (archived in [`03-source-papers/`](03-source-papers/), with text extractions), all certificates re-verified in exact arithmetic. Verdict: **VALID AS WRITTEN** — no invalid implication, missing hypothesis, reversed inequality, or source mismatch found. Full findings: [`07-revision-r2/REVIEW-STRENGTHENED.md`](07-revision-r2/REVIEW-STRENGTHENED.md) (this manuscript) and [`06-fable-brief/VERDICT.md`](06-fable-brief/VERDICT.md) + [`FINDINGS.md`](06-fable-brief/FINDINGS.md) (the full review of all versions). A machine verdict is not peer review; it is offered as a map of what has already been checked and how.

Weaker, independently validated fallbacks with simpler dependency profiles: motion >= n/(14 d^3) ([`04-proof-assets/babai_motion_d3_complete_proof.tex`](04-proof-assets/babai_motion_d3_complete_proof.tex) — its mu=1 branch avoids the new Poincare inequality via a dual-graph argument) and motion >= n/(13 d^5) ([`04-proof-assets/babai_motion_d5_source_audited.tex`](04-proof-assets/babai_motion_d5_source_audited.tex) — every import a published Pyber-Skresanov statement, including Corollary 4.8 within its stated eps-range).

## Version history and provenance

The manuscript evolved publicly and every stage is archived with sha-256 fingerprints ([`MANIFEST-PACKAGE.json`](MANIFEST-PACKAGE.json)): the initial 1/12 draft and its self-audit patch ([`09-first-session-originals/`](09-first-session-originals/), including the "adversarially patched" file's referee report — the filename refers to a self-hostile audit of the draft), the correction and provenance-annotation round ([`07-revision-r2/`](07-revision-r2/), including the session transcript), and the final strengthening. [`VERSION_MATRIX.md`](VERSION_MATRIX.md) has the complete claim ladder, including one stronger candidate (2n/(5 d^3)) that remains unvalidated pending a 2026 Lv-Koolen preprint and is not asserted.

Known limits of the approach are stated in the manuscript's closing remark: the exponent 3 is intrinsic to the Bang-Koolen geometricity route (rho = O(d^-3)); improving it requires a different route to exact Delsarte geometry, not better constants.
