# @taobanker X cross-reference for Fable 5

**Purpose:** Live re-check of `x.com/taobanker` against the offline package so the adversarial review does not miss social/context facts.  
**Checked:** 2026-07-23 / early 2026-07-24 UTC (Grok Build).  
**Operator note:** Do **not** treat this file as a math source. Math stays in `04-proof-assets/` + `03-source-papers/`.

---

## Verdict on package accuracy

| Area | Status | Notes |
|------|--------|-------|
| Core public claim post | **Accurate** | `POST.md` matches live text of `2080394270826205555` |
| Babai email + ASAP ask | **Accurate** | `POST-2-BABAI-REPLY.md` + email OCR match live screenshot |
| Proof/prompt share URL | **Accurate** | t.co → ChatGPT share `6a627d97-c470-83ea-8fab-fba44b51d3a0` |
| Version / constant drift | **Accurate** | Social “6→3 degree” ≠ single boxed constant; matrix is correct |
| Fable mission framing | **Accurate** | Hostile review ASAP; not coauthorship; Claude not credited for generation |
| Full day-of-X timeline | **Partial** | Media mostly present; several posts only partially / not archived as markdown (fixed below + `POST-3`/`POST-0`) |
| Grok “92% legit / 7/10” post | **Was missing as archive** | Media already in `05-media/`; now `POST-3-GROK-REVIEW.md` |
| Deliverables yet | **Not done** | No `VERDICT.md` / `FINDINGS.md` etc.; prior run status was still “running” |

---

## Chronological X timeline (2026-07-23, relevant only)

Times UTC. IDs are status IDs.

| Time | ID | Summary | Offline home |
|------|-----|---------|--------------|
| 13:11 | `2080279590627393558` | Codex in 90-min spurts; “make no mistakes”; threaten Fable for final effort | Media: `05-media/x-codex-spurts-*.png`; archive: `POST-0-CODEX-SPURTS.md` |
| 19:43 | `2080378276657176825` | “1 in 3 chance” contribution; waiting on Claude; Wikipedia joke | Media: `x-waiting-claude-*.jpg` (shows **public abstract** \(n/(12d^3)\)); `POST-0` thread notes |
| 19:49 | `2080379850280321050` | Self-reply: not “just counterexample” — would be epic | Reply under waiting post |
| 19:51 | `2080380343706636565` | Fable/Claude length limits screenshot — “why only one significant Fable math solve” | Media: `x-fable-limits-*.jpg` |
| 19:54 | `2080381024236708253` | `@claudeai what are you guys doing fr` | Reply under limits post |
| 20:19 | `2080387418767679665` | Burned whole Fable session; releasing **without** Claude verification; **Claude gets no credit** | Media: `x-no-claude-credit-*.jpg` (hostile prompt UI) |
| 20:20 | `2080387721428623392` | One-shotted Fable session limit (1.5 questions) | Text only |
| 20:22 | `2080387980556902501` | `@doodlestein do you want to hand off my proof to your fable?` | Text only |
| 20:31 | `2080390465967227085` | Inspiration = act like “retarded manager,” tell bot work harder | Reply under credit post |
| **20:47** | **`2080394270826205555`** | **Main claim post** — 6th→3rd degree; Codex “PhD advisor”; link to share; Wikipedia joke | **`POST.md`** + main photo |
| 20:47 | `2080394321073668502` | `@mean_field_zane` forward to someone who knows | In `POST.md` |
| 21:06 | `2080399167575191882` | “get Fable to do an adversarial review” | In `POST.md` |
| **22:37** | **`2080422087882104956`** | **Babai emailed back**; Fable ASAP; email screenshot | **`POST-2-BABAI-REPLY.md`** |
| **23:55** | **`2080441684983226448`** | Grok says ~92%+ legit; Babai masterpiece vs this paper **7/10** technical refinement | Media present; **`POST-3-GROK-REVIEW.md`** |

Non-substantive replies (Fields medal joke, “Super cool”, identity joke, etc.) — ignore for math.

---

## Facts Fable must internalize from X (epistemic, not math)

1. **Author is non-expert on the domain.** Publicly: does not understand the bound; method was crude Codex supervision (“WorK HaRDeR” / “MakE No MisTakEs”).  
2. **Generation stack:** Codex / ChatGPT share. Fable/Claude was attempted for **verification**, hit **usage / max-length limits**, and was **explicitly denied credit**.  
3. **Public social claim** is informal “degree 6 → degree 3,” not a specific constant. The screenshot abstract and late share narrative push **\(n/(12d^3)\)**; TeX drafts use other constants — already in `VERSION_MATRIX.md`.  
4. **Independent review is the product.** Author asked twice for adversarial Fable review (21:06 general; 22:37 ASAP after Babai).  
5. **Babai is engaged.** Forwarded manuscript to **Bohdan Kivva only (so far)**; asked for: author name/email/affiliation, LLM disclosure (role + which model + public vs privileged access), explanation of “adversarial patch” filename, and personal background (UChicago bachelor’s).  
6. **“Adversarial patch”** = self-hostile / patched manuscript naming from the share pipeline, **not** an attack on Babai — answer meta only after math.  
7. **Grok pre-score is non-evidence.** Author’s “92%+ legit / 7/10 refinement” post is social framing of a prior Grok read; Fable must **not** rubber-stamp from it. Grok screenshots rate significance/elegance under an **assumed** \(n/(12d^3)\) storyline — they do not substitute for a line-by-line gap hunt.  
8. **Author’s own Codex screenshot** already frames a “defensible public claim” as a **candidate** with a **precise failure boundary**, not a proved theorem — align with hostile standard.

---

## Media inventory vs posts

| Media file | Matches post |
|------------|--------------|
| `x-codex-spurts-HN6jNLPXEAAAHNp.png` | Codex spurts + “MAKE NO MISTAKES” / Fable threat |
| `x-waiting-claude-HN79ANpWAAAtAmI.jpg` | Abstract claiming \(n/(12d^3)\) |
| `x-fable-limits-HN7-5FpXcAAn1kJ.jpg` | Claude max-length while proofreading |
| `x-no-claude-credit-HN8FU7cWwAAsI8S.jpg` | Hostile-referee UI + usage limit |
| `x-post-photo-HN8LGIPWMAE_Kj1.jpg` | Main claim post |
| `x-post-babai-email-HN8k20DXkAAhV0b.png` | Babai email body |
| `x-grok-review-1-HN82fFnWsAAuRjk.png` | Grok on Babai GI masterpiece ratings |
| `x-grok-review-2-HN82rZTXIAAE13y.png` | Grok on candidate paper ~7/10; cites constant 12, \(\mu=2\), Metsch, geodesic |

---

## What does **not** change the Fable math job

- Wikipedia / Fields medal jokes  
- Credit fights with Claude product limits  
- Requests to @doodlestein / @mean_field_zane  
- Grok probability language  
- Author’s emotional “scared I’m wasting Babai’s time”

Still: **urgency + audience (Kivva reading)** remain real operational context.

---

## Gaps that remain (honest; not blockers for offline math)

- True PDF/zip bodies never in share HTML (already documented).  
- No full Babai email headers / prior author email in package (body only via screenshot).  
- Grok’s full multi-turn chat beyond the two screenshots is not archived.  
- Whether author sent `adversarially_patched` vs `complete_proof` to Babai is not visible from X alone — Fable still audits **all** TeX variants per `VERSION_MATRIX.md`.

---

## Operator checklist before **manual** Fable start

1. Do **not** skip `VERSION_MATRIX.md` because of the Grok 7/10 or 92% posts.  
2. Primary social boxed form for the public claim: **\(n/(12d^3)\)** (abstract screenshot + late share); primary full TeX: **`babai_motion_d3_complete_proof.tex`** at \(n/(14d^3)\).  
3. Prefer earliest fatal flaw; if \(d^{-3}\) dies and \(d^{-5}\) lives, say so.  
4. Meta Babai questions (disclosure, “adversarial” filename) are secondary to `VERDICT.md`.
