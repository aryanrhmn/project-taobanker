# 07-revision-r2 — the strengthened revision (n/(11.346 d^3)) and its provenance

**New share:** https://chatgpt.com/share/6a62ce8c-8a84-83ea-901d-d482a36cc56a
**Captured:** 2026-07-24 (raw HTML in `raw/`; extracted prose in `conversation-prose.md`)
**Trigger:** Kivva reviewed the manuscript and found it "exciting"; his one structural complaint, relayed by Babai by email, was:

> "Unfortunately, the writeup mixes restating claims from the previous papers with new sharper bounds without clean distinction which is which. ... Could you ask your LLM to annotate every statement and equation taken from a source with a pointer to the source, like [PS, Lemma 3.8] ... And if a result was not taken from a source, just write [LLM] or some such so we know a pointer to a source was not accidentally omitted."

The author fed that email into a new Codex/ChatGPT session together with the original 1/12 manuscript (uploaded as `babai_motion_d3_adversarially_patched.pdf` — the "adversarial patch" file Babai asked about), the PS and Kivva papers, and the Lv–Koolen 2026 preprint.

## What that session did (fully documented in the share's tool calls)

1. **Audited the 1/12 manuscript twice** (a full audit and a focused source-interface audit). Verdict: valid conditional on the published inputs; a handful of proof-preserving wording fixes (the "distinct vertices" sentence, a k=2 cycle dispatch, an explicit z<1 calculation, spelled-out tau_i = i endpoint chain, k/d integrality before Egawa, and the Kivva journal-vs-arXiv numbering concordance).
2. **Applied those corrections** -> `babai_motion_d3_revised.tex` (still 1/12).
3. **Answered Kivva's request** by adding a visible provenance system — `\prov{...}` tags on every displayed equation ([PS, ...], [K, ...], or [LLM]) plus a machine checker that fails if any displayed equation lacks a tag -> `babai_motion_d3_source_annotated.tex`.
4. **Strengthened the constant**: an exact scalar optimization showed the architecture's uniform limit is C_lim = (1 + 2/eps_K)/27 = 11.3453182..., set by Kivva's exact Johnson threshold (the Bussemaker–Neumaier root), not by the new mu=2 argument (which alone would allow ~6.08). It chose the rational C0 = 5673/500 = 11.346 just above the limit and retuned every scalar certificate -> `babai_motion_d3_source_annotated_strengthened.tex/pdf`, the manuscript now circulating:

   **motion(X) >= 500n/(5673 d^3) = n/(11.346 d^3)** outside Johnson/Hamming.

   Notable: at this constant, PS's published rounding "eps* > 0.0065" is NO LONGER sufficient (eps(3) = 0.0065496 > 0.0065). The strengthened manuscript correctly switches to Kivva's exact threshold definition (Thm 3.5 + Prop 3.6) with an exact rational bracket certificate. It also drops the earlier diameter-dependent ~4d^3 proposals as unauditable-in-one-pass, and uses no enumeration and no post-2021 classification theorem (the Lv–Koolen preprint was present in the session but is NOT used by the strengthened manuscript).

## What is and is not recoverable from the share (same glitch as before)

- **Recoverable and archived here:** all conversation prose (both audit reports in full), every sandbox tool call including the complete `apply_strengthening.py` patch script (whose old-string assertions quote the manuscript verbatim at every changed site), the exact certificates, the provenance-checker scripts, and the constant-optimization script.
- **NOT recoverable:** the actual bytes of any `.tex`/`.pdf`/`.zip` output (sandbox links only — the persistent ChatGPT-share limitation). The strengthened manuscript itself must be obtained from the author (he has the PDF and the bundle zip).
- The share page also leaks a number of unrelated ChatGPT system/advert prompts (blocks 4-6, 13-14, 16-19, 21, 27 of `conversation-prose.md`); these are share-format noise, not part of the math session.

## Files here

| File | What it is |
|---|---|
| `raw/raw-share-page.html`, `raw/stream-payloads-unescaped.txt` | Raw dump of the new share |
| `conversation-prose.md` | All 27 extracted text blocks (audits, patch scripts, notes); author's first name redacted from the relayed email — raw dumps kept verbatim since the source share page is public |
| `extracted_manuscript_raw.tex` | The one inlined TeX object (the PDF's "Verification status" box only) |
| `r2_exact_audit.py` + `r2_exact_audit_output.txt` | Fable's independent exact-arithmetic audit of the strengthened constant — 17/17 PASS |
| `REVIEW-STRENGTHENED.md` | Fable's review of the strengthened claim (start here) |
