# Fable 5 task brief — adversarial review of taobanker / Codex Babai-motion claim

**Working root:** `<package-root>` (this folder)  
**Status of this package:** offline mirror assembled so Fable does **not** need X or live web access to the original post.  
**Public call from author:** “get Fable to do an adversarial review”  
  — X: https://x.com/taobanker/status/2080394270826205555  
  — Proof/prompt share: https://chatgpt.com/share/6a627d97-c470-83ea-8fab-fba44b51d3a0  

---

## Mission (do this, not “improve the proof”)

Perform a **hostile, line-by-line mathematical referee review** of the candidate proof(s). Reconstruct critical steps independently where possible. Do **not** polish prose, do **not** invent a stronger theorem, and do **not** rubber-stamp the audit scripts.

### Required verdict (choose exactly one primary)

| Code | Meaning |
|------|---------|
| `VALID AS WRITTEN` | Every implication in the **target manuscript** is sound under the stated hypotheses; imported theorems are used within their published hypotheses. |
| `GAP FOUND` | There is a missing implication, reversed inequality, unjustified case, or broken step (give earliest failure). |
| `SOURCE MISMATCH` | A cited lemma/theorem is misquoted, wrong-numbered, or applied outside its hypotheses. |
| `UNRESOLVED` | Could not finish a full adversarial pass; state blockers. |

Also return **secondary notes** on version conflicts across drafts (see Version matrix).

---

## Primary mathematical claim (as sold publicly)

On X and in the linked ChatGPT share’s late narrative, the headline is:

> For a **primitive distance-regular graph** \(X\) on \(n\) vertices with diameter \(d \ge 3\), either \(X\) is **Johnson** or **Hamming**, or  
> \[
> \operatorname{motion}(X) \ge \frac{n}{12 d^{3}}.
> \]

This would improve the diameter dependence in the Pyber–Skresanov line from roughly \(d^{-6}\) toward \(d^{-3}\).

**Important:** extracted LaTeX drafts do **not** all state \(1/12\). Treat the public \(n/(12d^3)\) claim as the **social claim**, and audit each manuscript’s **own** theorem statement against its own proof.

---

## Version matrix (read before auditing)

| Asset | Theorem constant / form | Role |
|-------|-------------------------|------|
| ChatGPT share late narrative (`02-chatgpt-share/…`) | \(\operatorname{motion}(X)\ge n/(12d^3)\) | Public package summary; “awaiting independent verification” |
| `04-proof-assets/babai_motion_d3_complete_proof.tex` | \(\ge n/(14d^3)\) | Full amsart manuscript; strongest **complete-writeup** extracted |
| `04-proof-assets/babai_motion_d3_final_candidate.tex` | \(\ge 2n/(5d^3)\) | Aggressive candidate; matches some twitter-thread numbers |
| `04-proof-assets/babai_motion_d3_README.txt` | \(\ge n/(14d^3)\) | README for complete_proof |
| `04-proof-assets/babai_motion_d5_source_audited.tex` | \(\ge n/(13d^5)\) | **Conservative** fallback; uses published \(\mu=2\) steps only |
| `04-proof-assets/README_babai_motion_d5_audit.md` | Retracts earlier \(d^{-3}\) constants including \(1/12\) | Explicit self-retraction of some \(d^{-3}\) claims |
| `04-proof-assets/babai_motion_twitter_thread.txt` | Headlines \(2n/(5d^3)\); fallback \(n/(15d^3)\) | Marketing / audit thread draft |

### Recommended audit order

1. **`babai_motion_d3_complete_proof.tex`** (own claim \(n/(14d^3)\)) — primary full writeup.  
2. **`babai_motion_d3_final_candidate.tex`** (own claim \(2n/(5d^3)\)) — check whether stronger constant is supported or overclaimed.  
3. Reconcile with share narrative \(n/(12d^3)\) — is \(1/12\) ever proved in extracted sources, or only asserted in chat prose?  
4. **`babai_motion_d5_source_audited.tex`** — if \(d^{-3}\) fails, does the conservative \(d^{-5}\) candidate survive?  
5. Run exact-arithmetic scripts in `04-proof-assets/*audit*.py` as **supporting checks only** (they do not verify graph theory).

---

## Hostile-referee checklist (from generator’s own standard)

Search for the **earliest**:

1. Invalid implication (A does not entail B).  
2. Missing hypothesis on an imported theorem (Kivva / Pyber–Skresanov / Metsch / Bang–Koolen / Terwilliger / Biggs / Lv–Koolen, etc.).  
3. Reversed or non-sharp inequality that breaks a constant.  
4. Edge-orientation / factor-of-two error in geodesic cut or Poincaré arguments.  
5. Hidden reliance on computer enumeration that was supposedly removed.  
6. Endpoint classification gaps (Hamming vs Doob; Johnson; crown graphs if relevant).  
7. \(\mu=2\) branch: Riccati / relative-drop recurrence and multiplicity surplus.  
8. Citation number mismatches (arXiv vs journal numbering for Kivva).

### Suggested attack surface (generator’s own “most breakable” points)

- \(\mu=2\) standard-sequence / multiplicity interface.  
- Support-sensitive geodesic boundary → \(\mu < \rho k\), \(\lambda > (1-\rho)k/d\).  
- “Full Metsch” step ⇒ \(m \le d\) and Delsarte geometry.  
- Direct geodesic Poincaré \(k-\theta_1 \ge k/D^2\) (vs published weaker constants).  
- Any use of recent preprint endpoint results beyond published Kivva / Pyber–Skresanov.

---

## Sources available offline

### Proof package
- `04-proof-assets/*.tex` — manuscripts  
- `04-proof-assets/*audit*.py`, `motion_d4_sanity_checks.py` — scalar audits  
- `04-proof-assets/babai_motion_twitter_thread.txt`  
- `04-proof-assets/_suspect-not-true-file-content/` — **do not trust**; mis-extracted chat prose labeled as files  

### Published baselines (PDFs)
- `03-source-papers/pyber-skresanov-2312.00383.pdf` — arXiv:2312.00383  
- `03-source-papers/kivva-1912.11427.pdf` — arXiv:1912.11427  
- `03-source-papers/kivva-clique-geom-mindeg.pdf`  
- `03-source-papers/kivva-drg-spectral-gap.pdf`  
- `03-source-papers/kivva-thesis.pdf`  

### Origin context
- `01-x-post/POST.md` — main public claim + first Fable ask  
- `01-x-post/POST-2-BABAI-REPLY.md` — Babai→Kivva forward; ASAP Fable ask; disclosure meta  
- `01-x-post/POST-0-CODEX-SPURTS.md` — pre-release Codex/Fable-limit timeline; abstract \(n/(12d^3)\) screenshot  
- `01-x-post/POST-3-GROK-REVIEW.md` — **non-evidence** social Grok 7/10 / “92%” framing  
- `01-x-post/X-CROSSREF-2026-07-23.md` — full live X cross-check  
- `02-chatgpt-share/conversation-prose.md` (and message-candidates/)  
- `05-media/*` — all day-of screenshots (Codex, Claude limits, Babai email, Grok ratings)  

### Gaps in this offline package (honest)

The ChatGPT sandbox also listed binaries that **were not recoverable** as true file bytes from the public share HTML:

- `babai_motion_d3_complete_proof.pdf`  
- `babai_motion_d3_c12_audit_package.zip` / `babai_motion_d5_audit_package.zip`  
- True contents of `fable_hostile_referee_prompt_d3_c12.txt` / `…_d5.txt` (only linked, not inlined)  
- Some intermediate `.tex` / adversarial patch variants  

Use extracted **`.tex` sources** as the manuscripts of record. The reconstructed referee instructions in this folder replace the missing prompt files.

---

## Deliverable format (write under `06-fable-brief/`)

Create:

1. **`VERDICT.md`** — primary code + 1-paragraph summary.  
2. **`FINDINGS.md`** — ordered list of issues (severity, location in file, quote, why it fails, minimal counterexample or fix if known).  
3. **`DEPENDENCY_LEDGER.md`** — each imported theorem → stated hypothesis → whether use is valid.  
4. **`CONSTANT_AUDIT.md`** — for each claimed constant (\(2/5\), \(1/12\), \(1/14\), \(1/13 d^{-5}\), …): supported / unsupported / withdrawn.  
5. Optional: rerun Python audits; paste outputs into `AUDIT_RUN_LOG.txt`.

---

## Tone / standard of evidence

- Treat this as **unrefereed machine-generated mathematics**.  
- Agreement of self-audits is **not** verification.  
- Prefer **earliest fatal flaw** over a long list of nits.  
- If the \(d^{-3}\) claim dies but \(d^{-5}\) survives, say so explicitly — that is still a useful result for the author.
