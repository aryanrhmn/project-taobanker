# MEMO — Adversarial review of your Babai-motion manuscript

| | |
|---|---|
| **To** | @taobanker (X) |
| **From** | project-taobanker operators; adversarial referee: **Claude Fable 5** (`claude-fable-5`, xhigh effort) |
| **Date** | 2026-07-23; updated 2026-07-24 (strengthened revision validated) |
| **Re** | Your public ask — "get Fable to do an adversarial review" / "ASAP" after Prof. Babai's reply |
| **Bottom line** | **VALID AS WRITTEN** for the strengthened manuscript of record (`08-strengthened-manuscript/`): **motion(X) ≥ 500n/(5673d³) = n/(11.346d³)** — no gap, no misused import, all certificates exact. The 1/14 and 1/13d⁵ versions are validated fallbacks. Full trail: `06-fable-brief/` + `07-revision-r2/` + `09-first-session-originals/`. See §6. |

---

## 1. The task

You posted a Codex-generated candidate improvement of the Pyber–Skresanov motion bound for primitive distance-regular graphs (d⁻⁶ → d⁻³ diameter dependence, Babai's conjecture line) and asked the public to have Fable adversarially review it. Urgency escalated when László Babai replied and forwarded the manuscript to Bohdan Kivva — whose published theorems are exactly the ones your proof imports. The review standard requested (and applied) was hostile refereeing: find the earliest invalid implication, missing hypothesis, reversed inequality, or source mismatch — or state VALID AS WRITTEN under strict standards. Not co-authoring, no repairs.

## 2. How we prepped it

Fable was given no X or web access, so we froze everything offline first:

- **Your X posts** (claim post, replies, Babai-reply post, Grok posts) captured verbatim into `01-x-post/`, with day-of screenshots in `05-media/`.
- **The ChatGPT share** behind your t.co link was forensically dumped (`02-chatgpt-share/raw/`) and the manuscripts and audit scripts were extracted from the RSC stream's sandbox heredocs (`tools/_extract_*.py` → `04-proof-assets/`), sha-fingerprinted in `MANIFEST.json`. Mis-extracted chat prose masquerading as files was quarantined in `_suspect-not-true-file-content/` and excluded from mathematics.
- **The published ground truth** — Pyber–Skresanov arXiv:2312.00383 and Kivva arXiv:1912.11427 (plus three supporting Kivva PDFs) — was downloaded into `03-source-papers/` so every import could be checked against the actual published statements, not your manuscripts' paraphrases.
- **Version drift was mapped first** (`VERSION_MATRIX.md`): your drafts claim 2/5, 1/8, 1/12, 1/14, 1/15 at d⁻³ and 1/13 at d⁻⁵, and your own d5 README retracts three of them. Each manuscript was audited against its *own* boxed constant; the public n/(12d³) claim was scored separately.
- The referee mission, rules of engagement, and your generator's own "most breakable points" list were written into `06-fable-brief/` (the original hostile-prompt files were not recoverable from the share, so the standard was reconstructed from the share's own prose).

## 3. How the review was completed

One Fable 5 session, launched via `06-fable-brief/Launch-Fable5.ps1`, working only inside this folder. Method:

1. **Independent rederivation** of every new implication in the manuscripts — the adjacent-pair identity D(1), the oriented geodesic-load boundary, the μ=2 Riccati relative-drop recurrence and its induction, the surplus case analysis, the loss bounds, the endpoint-to-Hamming endgame, the μ=1 dual-graph chain, and all scalar/polynomial certificates.
2. **Verbatim import verification**: all four source PDFs were text-extracted (copies now in `03-source-papers/extracted-text/`) and every cited proposition/lemma was read from the published papers and hypothesis-matched at its point of use — 32 imports in total.
3. **Script runs as supporting evidence only**: the exact-arithmetic audit scripts were executed (or faithfully re-implemented where a Python 3.13 formatting bug crashed the shipped script); outputs in `06-fable-brief/AUDIT_RUN_LOG.txt`. Script agreement was given no weight on graph theory.
4. Grok's "7/10, 92%" posts were treated as social framing, per the brief, and played no role.

## 4. Findings

| Version | Boxed claim | Verdict |
|---|---|---|
| `babai_motion_d3_complete_proof.tex` | motion ≥ n/(14d³) | **VALID AS WRITTEN** — no invalid implication, no missing hypothesis, no reversed inequality, no source mismatch. All 20+ imports used within published hypotheses (including the tight ones: PS 2.19's ε* > 0.0065 vs your ε ≈ 0.0053 at d=3; the full Metsch expression; Kivva Lemma 4.2's ε < 1/m²). |
| `babai_motion_d5_source_audited.tex` | motion ≥ n/(13d⁵) | **VALID AS WRITTEN** — every import is a published PS statement, hypothesis-matched, including PS 2.21 (ε < 1/(6m⁴d)) and PS 2.14 (k ≥ 32md²). Cleanest dependency profile; bulletproof fallback. |
| `babai_motion_d3_final_candidate.tex` | motion ≥ 2n/(5d³) | **UNRESOLVED (conditional)** — the μ≥3 branch imports Lemma 17 / Theorem 32 of an unpublished Jan-2026 Lv–Koolen preprint that is not in this package and cannot replace the published route for d ∈ {3,4}; d ≤ 16 also rests on (declared, script-reproduced) computer enumeration. Everything checkable verifies, including the new geodesic Poincaré inequality k−θ₁ ≥ k/d². |
| Public / social claim | motion ≥ n/(12d³) | **UNSUPPORTED / WITHDRAWN** *as of the first share* — no trusted extracted manuscript proved 1/12; it survived only in a script docstring and quarantined mis-extractions, and your own `README_babai_motion_d5_audit.md` withdrew it. **[Updated 2026-07-24: the 1/12 manuscript file has since surfaced — you uploaded it to your r2 session, where it was audited twice (valid conditional) — and the whole question is now moot: 1/12 is superseded by the validated n/(11.346d³); see §6.]** |

The genuinely new mathematics in the 1/14 manuscript is real: it replaces Kivva's published μ=2 surplus 1 + 1/(m²−1) (which forces the d⁻⁵-scale hypothesis in his Cor. 4.8) with a sharper analytic surplus R ≥ 1 + 1/m and a sharper Riccati loss, relaxing the smallness parameter to d⁻³ scale with no enumeration. That lemma (Lemma 6.6, "Exact surplus factor") is the load-bearing novelty — and the right thing for Kivva to check first.

Minor, non-fatal items (details in `FINDINGS.md`, F5–F7): a "distance two" imprecision in the adjacent-pair lemma, one uncited use of Kivva Lemma 2.17 (τ₂ ≥ ψ₁), a cosmetic Doob-exclusion wording, and the shipped `complete_audit.py` crash/performance bug.

## 5. Conclusions and recommended next steps

1. **Publicly claim n/(14d³), not n/(12d³) and not 2n/(5d³).** The 1/14 manuscript is the strongest fully-written, fully-audited claim in the package; 1/12 is withdrawn and unwritten; 2/5 is conditional on an unpublished preprint. **[Updated 2026-07-24: superseded — the strengthened n/(11.346d³) is now fully validated and is the claim to quote; see §6.]**
2. **Answer Babai's asks**: put your name, email, and affiliation on the paper; add an account of your role vs. the LLM's role and which model generated it (Codex; Claude verification hit rate limits; this Fable review is documented here). His "adversarial patch" question: the filename refers to a *self*-hostile audit pass over the draft — adversarial toward the proof, not toward him.
3. **Hand Kivva the shortcut**: `06-fable-brief/DEPENDENCY_LEDGER.md` (all 32 imports vs. his and PS's published statements) and `FINDINGS.md` F0 (what was rederived and how). His time is best spent on Lemma 6.6 and Section 6 of the 1/14 manuscript.
4. **If you want 2/(5d³) upgraded**, obtain and include the Lv–Koolen preprint (arXiv:2601.10330) so its Lemma 17 / Theorem 32 can be hypothesis-checked; for d ≥ 5 the published PS 2.19 route already suffices at that constant.
5. Standard caveat: this is a machine adversarial pass under strict standards, not peer review. Every attack in the hostile-referee checklist was mounted and failed; specialist confirmation is still the bar.

Deliverables: `06-fable-brief/VERDICT.md`, `FINDINGS.md`, `DEPENDENCY_LEDGER.md`, `CONSTANT_AUDIT.md`, `AUDIT_RUN_LOG.txt` (index: `OUTPUTS_INDEX.md`). Package integrity: `MANIFEST-PACKAGE.json` (root, sha256 fingerprints of every file at delivery).

## 6. Update (2026-07-24) — the strengthened n/(11.346 d³) revision

After Kivva reviewed the paper ("exciting") and asked, via Babai, for source-vs-new annotations on every equation, your new session produced the provenance-annotated, strengthened manuscript claiming **motion(X) ≥ 500n/(5673d³) = n/(11.346d³)**. The Fable review lives in **`07-revision-r2/REVIEW-STRENGTHENED.md`**; the actual manuscript files you supplied are archived in **`08-strengthened-manuscript/`**.

**Final verdict: `VALID AS WRITTEN`.** The review ran in two stages the same day. First, everything recoverable from your new share was verified: the architecture (already line-by-line validated at 1/14, and independently audited twice inside your own session at 1/12, with matching conclusions), the complete strengthening patch (recovered verbatim), and all 17 exact-arithmetic certificates — including the deliberately razor-thin Johnson margin, where 11.346 = 5673/500 sits exactly 13/40500 above the architecture's provable limit set by Kivva's threshold constant. Then, once you supplied the actual files (the share had the same dead-links glitch as the first), the closing assembly check was completed: a full 982-line read of the manuscript of record (every derivation verifies — and it also fixes the two cosmetic nits flagged on the 1/14 version), zero old-constant remnants, your bundled verification scripts re-run and passing (330 provenance tags, every equation labeled — exactly what Kivva asked for), and zip/tex/PDF hash-consistent.

**Bottom line: quote n/(11.346d³) — it is now the package's validated headline claim,** with n/(14d³) and n/(13d⁵) as fully validated fallbacks beneath it. Standard caveat unchanged: this is strict machine adversarial review, not peer review; Kivva's check of the μ=2 surplus lemma remains the decisive human step, and the provenance tags plus `06-fable-brief/DEPENDENCY_LEDGER.md` are built to make that check fast. (Note for readers using Kivva's journal paper: the ledger cites arXiv numbering and states the journal concordance at the top; the manuscript itself uses journal numbering.)

### Quotable verdict (for correspondence)

> An independent adversarial review by Claude Fable 5 (Anthropic) examined the manuscript "An explicit d⁻³ motion bound for primitive distance-regular graphs" (motion(X) ≥ 500n/(5673d³) = n/(11.346d³)) line by line: every imported theorem was checked verbatim against the published Pyber–Skresanov and Kivva papers with hypotheses verified at each point of use, every new derivation was independently reconstructed, and all scalar certificates — including the exact Johnson-threshold comparison against the Bussemaker–Neumaier constant — were re-verified in exact rational arithmetic. The verdict is VALID AS WRITTEN: no invalid implication, missing hypothesis, reversed inequality, or source mismatch was found. This is a strict machine referee pass, not peer review; the full audit trail, dependency ledger, and verification scripts are public at github.com/aryanrhmn/project-taobanker.

If you only mention one thing: **"Fable adversarially reviewed every version of this proof and endorsed the core result at each stage — the earlier 1/14 unconditionally, and the strengthened 1/11.346 unconditionally after receiving the final files."**

---

## Appendix A — Package map

```
project-taobanker/
├── README.md                          ← this memo
├── SOURCE_INDEX.md                    ← inventory + provenance
├── VERSION_MATRIX.md                  ← conflicting constants across drafts
├── MANIFEST-PACKAGE.json              ← package-wide sha256 fingerprints
├── 01-x-post/                         ← X captures (POST, Babai reply, Codex spurts, Grok, cross-ref)
├── 02-chatgpt-share/                  ← curated share evidence (summary, prose, stitched, candidates)
│   └── raw/                           ← raw HTML/RSC dumps + intermediate extraction outputs
├── 03-source-papers/                  ← published baselines (PDF)
│   └── extracted-text/                ← referee text extractions of the PDFs
├── 04-proof-assets/                   ← extracted TeX manuscripts + Python audits (MANIFEST.json)
│   └── _suspect-not-true-file-content/  ← quarantine; mis-extracted chat prose; not sources
├── 05-media/                          ← day-of screenshots
├── 06-fable-brief/                    ← task brief + referee deliverables (VERDICT, FINDINGS, ledgers)
│   └── runs/ (└── archive/)           ← session logs
├── 07-revision-r2/                    ← r2 share forensics + review of the strengthened claim
├── 08-strengthened-manuscript/        ← THE validated manuscript of record (tex/pdf/bundle/checkers)
├── 09-first-session-originals/        ← true c12 files: adversarial patch, self-referee report (chain of custody)
└── tools/                             ← extraction pipeline used during assembly
```

## Appendix B — Recovery record (from assembly)

**Recovered as true files:** the three LaTeX manuscripts (`babai_motion_d3_complete_proof.tex` n/(14d³); `babai_motion_d3_final_candidate.tex` 2n/(5d³); `babai_motion_d5_source_audited.tex` n/(13d⁵)); five audit/helper scripts (`complete_audit`, `final_audit`, `sharpened_audit`, `audited_scalar_check`, `motion_d4_sanity_checks`); full X post text + replies; ChatGPT share prose (multi-turn claim evolution including retractions); draft Twitter thread; published papers Pyber–Skresanov arXiv:2312.00383, Kivva arXiv:1912.11427, plus Kivva clique-geometry / spectral-gap PDFs and thesis.

**Not recoverable as true files** (linked in the ChatGPT UI but not inlined in the public share HTML): compiled PDFs of the candidate manuscripts; zip "audit packages"; the original `fable_hostile_referee_prompt_*.txt` bodies. Mitigation: TeX sources are present; the hostile prompt was reconstructed from the share's stated adversarial standard (`06-fable-brief/HOSTILE_REFEREE_PROMPT.md`).

**Version-drift warning (unchanged):** the package contains several mutually inconsistent constants (2/5, 1/12, 1/14, 1/13·d⁻⁵, …) and one README explicitly retracts earlier d⁻³ claims. See `VERSION_MATRIX.md`; each draft must be audited against its own boxed theorem.

## Appendix C — Reproducing the review

Claude Code on this machine defaults to `claude-fable-5[1m]`. From this folder:

```powershell
cd "<package-root>"
pwsh -File .\06-fable-brief\Launch-Fable5.ps1          # non-interactive, logs to 06-fable-brief/runs/
pwsh -File .\06-fable-brief\Launch-Fable5.ps1 -Interactive
```

Or manually:

```powershell
claude --model "claude-fable-5[1m]" --effort xhigh --dangerously-skip-permissions
# then paste 06-fable-brief/FABLE_LAUNCH_PROMPT.md
```

Operator handoff text: work only inside this folder; follow `06-fable-brief/FABLE_TASK.md` + `HOSTILE_REFEREE_PROMPT.md`; produce `VERDICT.md`, `FINDINGS.md`, `DEPENDENCY_LEDGER.md`, `CONSTANT_AUDIT.md` in `06-fable-brief/`; no network or X access required.

## Appendix D — Assembly notes

Captured with live access to X + the ChatGPT share (Grok Build). Proof assets were extracted from the ChatGPT RSC stream (`cat > /mnt/data/...` heredocs) via `tools/_extract_*.py`, which now read/write the raw dumps under `02-chatgpt-share/raw/`.
