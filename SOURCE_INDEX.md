# Source index & provenance

All paths relative to `<package-root>` (this folder).

| Path | Type | Provenance | Notes |
|------|------|------------|-------|
| `01-x-post/POST.md` | markdown | X API + web fetch of status `2080394270826205555` | Includes replies asking for Fable review |
| `01-x-post/POST-0-CODEX-SPURTS.md` | markdown | Live X recheck 2026-07-23 | Pre-main-claim Codex/Fable-limit posts + abstract media |
| `01-x-post/POST-2-BABAI-REPLY.md` | markdown | X status `2080422087882104956` | Babai email + ASAP Fable ask |
| `01-x-post/POST-3-GROK-REVIEW.md` | markdown | X status `2080441684983226448` | Grok 7/10 framing — **not math evidence** |
| `01-x-post/X-CROSSREF-2026-07-23.md` | markdown | Live X vs package cross-check | Timeline + accuracy matrix |
| `05-media/x-post-photo-HN8LGIPWMAE_Kj1.jpg` | image | `pbs.twimg.com/media/...` | Main claim post photo |
| `05-media/x-codex-spurts-HN6jNLPXEAAAHNp.png` | image | X media | Codex “MAKE NO MISTAKES” / candidate framing |
| `05-media/x-waiting-claude-HN79ANpWAAAtAmI.jpg` | image | X media | Abstract with \(n/(12d^3)\) |
| `05-media/x-fable-limits-HN7-5FpXcAAn1kJ.jpg` | image | X media | Claude max-length during proofread |
| `05-media/x-no-claude-credit-HN8FU7cWwAAsI8S.jpg` | image | X media | Hostile prompt UI + usage limit |
| `05-media/x-post-babai-email-HN8k20DXkAAhV0b.png` | image | X media | Babai email body |
| `05-media/x-grok-review-1-HN82fFnWsAAuRjk.png` | image | X media | Grok on Babai GI masterpiece |
| `05-media/x-grok-review-2-HN82rZTXIAAE13y.png` | image | X media | Grok ~7/10 candidate ratings |
| `02-chatgpt-share/raw/raw-share-page.html` | html | `chatgpt.com/share/6a627d97-c470-83ea-8fab-fba44b51d3a0` | ~4.3 MB raw page |
| `02-chatgpt-share/raw/stream-payloads-unescaped.txt` | text/json | RSC stream from share page | ~3.3 MB; source of asset extraction |
| `02-chatgpt-share/conversation-prose.md` | markdown | Extracted prose strings from RSC | Multi-turn evolution of claims |
| `02-chatgpt-share/conversation-stitched.md` | markdown | Candidate blocks | Approximate order |
| `02-chatgpt-share/message-candidates/*.md` | markdown | Scored long strings | Useful for chronology |
| `04-proof-assets/babai_motion_d3_complete_proof.tex` | LaTeX | sandbox heredoc `/mnt/data/...` | Main complete writeup; claim \(n/14d^3\) |
| `04-proof-assets/babai_motion_d3_final_candidate.tex` | LaTeX | sandbox heredoc | Aggressive claim \(2n/5d^3\) |
| `04-proof-assets/babai_motion_d5_source_audited.tex` | LaTeX | sandbox heredoc | Conservative \(n/13d^5\) |
| `04-proof-assets/babai_motion_d3_complete_audit.py` | Python | sandbox heredoc | Exact scalar audit |
| `04-proof-assets/babai_motion_d3_final_audit.py` | Python | sandbox heredoc | Audit for \(2/5\) candidate |
| `04-proof-assets/babai_motion_d3_sharpened_audit.py` | Python | sandbox heredoc | Audit for \(1/8\)-scale candidate |
| `04-proof-assets/babai_motion_d3_audited_scalar_check.py` | Python | sandbox heredoc | Scalar check for \(n/12d^3\) **candidate naming** in docstring |
| `04-proof-assets/motion_d4_sanity_checks.py` | Python | sandbox heredoc | Related intermediate checks |
| `04-proof-assets/babai_motion_d3_README.txt` | text | sandbox heredoc | README for complete proof package |
| `04-proof-assets/README_babai_motion_d5_audit.md` | markdown | sandbox heredoc | **Retracts** earlier \(d^{-3}\) claims |
| `04-proof-assets/babai_motion_twitter_thread.txt` | text | sandbox heredoc | 10-post draft thread |
| `04-proof-assets/_suspect-not-true-file-content/` | mixed | failed filename→content match | Chat prose mislabeled as files — **ignore for math** |
| `03-source-papers/pyber-skresanov-2312.00383.pdf` | PDF | arXiv pdf | Published baseline \(n/d^6\)-scale results |
| `03-source-papers/kivva-1912.11427.pdf` | PDF | arXiv pdf | Geometric DRG / spectral tools |
| `03-source-papers/kivva-clique-geom-mindeg.pdf` | PDF | math.uchicago.edu/~bkivva | Journal/PDF version of clique geometry work |
| `03-source-papers/kivva-drg-spectral-gap.pdf` | PDF | math.uchicago.edu/~bkivva | Spectral gap paper |
| `03-source-papers/kivva-thesis.pdf` | PDF | math.uchicago.edu/~bkivva | Thesis (broader background) |
| `03-source-papers/arxiv-abs-*.html` | html | arXiv abs pages | Metadata snapshots |
| `06-fable-brief/FABLE_TASK.md` | markdown | assembled for this project | Primary tasking |
| `06-fable-brief/HOSTILE_REFEREE_PROMPT.md` | markdown | reconstructed | Replaces missing sandbox prompts |

## External URLs (for citation; not required at runtime)

| Resource | URL |
|----------|-----|
| X post | https://x.com/taobanker/status/2080394270826205555 |
| t.co short link | https://t.co/PVqJk5RtgT |
| ChatGPT share | https://chatgpt.com/share/6a627d97-c470-83ea-8fab-fba44b51d3a0 |
| Pyber–Skresanov | https://arxiv.org/abs/2312.00383 |
| Kivva | https://arxiv.org/abs/1912.11427 |

## Not recovered (listed in share UI only)

- `babai_motion_d3_complete_proof.pdf`  
- `babai_motion_d3_final_candidate.pdf` and other intermediate PDFs  
- `babai_motion_d3_c12_audit_package.zip`  
- `babai_motion_d5_audit_package.zip`  
- True bodies of `fable_hostile_referee_prompt_d3_c12.txt`, `fable_hostile_referee_prompt_d5.txt`  
- Various intermediate `.tex` only referenced by path (not heredoc-inlined)


## Additions after the first review cycle (2026-07-24)

| Path | Type | Provenance | Notes |
|------|------|------------|-------|
| `03-source-papers/extracted-text/*.txt` | text | Fable PDF extraction | Referee text extractions of the four source PDFs |
| `07-revision-r2/` | mixed | Second ChatGPT share `6a62ce8c-...` (curl capture) + Fable review | r2 forensics, session audits, exact-arithmetic audit, REVIEW-STRENGTHENED.md, verbatim session transcript |
| `08-strengthened-manuscript/` | tex/pdf/zip/py/md | Author-supplied (sandbox links were dead in the share) | **Manuscript of record**, n/(11.346 d^3); bundle hash-consistent; checkers re-run |
| `09-first-session-originals/` | tex/pdf/diff/py | Author-supplied | True bytes of the quarantined filenames: c12 manuscript, adversarial patch, self-referee report, checker — all cross-referenced |
| `01-x-post/POST-4-*.md`, `POST-5-*.md` | markdown | Grok live sweep / operator DM relay | Post-freeze freshness sweep; Kivva-feedback event record |
| `MANIFEST-PACKAGE.json` | json | Fable | Package-wide sha256 fingerprints, refreshed at every commit |
