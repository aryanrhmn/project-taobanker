# Timeline update — Kivva feedback, provenance annotation, strengthened manuscript (2026-07-24)

Context files: full technical detail in `../07-revision-r2/` (CONTEXT.md, REVIEW-STRENGTHENED.md). This file is the event record.

## Sequence of events (all 2026-07-23/24)

1. **Kivva reviewed the manuscript and found it "exciting."** Babai relayed his one structural comment to the author by email (screenshot shared by the author via DM; content verbatim, name withheld here since this repo is public):

   > "Unfortunately, the writeup mixes restating claims from the previous papers with new sharper bounds without clean distinction which is which." [Kivva]
   >
   > "This makes checking much more time-consuming. Could you ask your LLM to annotate every statement and equation taken from a source with a pointer to the source, like [PS, Lemma 3.8] or [PS, Equation 4.2)]? And if a result was not taken from a source, just write [LLM] or some such so we know a pointer to a source was not accidentally omitted." [Babai]

2. **The author ran a new Codex/ChatGPT session** (share: `chatgpt.com/share/6a62ce8c-8a84-83ea-901d-d482a36cc56a`), feeding it the original 1/12 manuscript (the "adversarial patch" PDF), the PS/Kivva papers, the Lv–Koolen preprint, and Babai's email. The session audited the 1/12 paper twice, applied proof-preserving fixes, implemented the requested provenance-tag system with a machine checker, and then strengthened the constant to the architecture's near-optimal value:

   **motion(X) >= 500n/(5673 d^3) = n/(11.346 d^3)**

3. **The author emailed the strengthened, annotated paper onward** (with this repo's README linked as the verification record) and asked, via DM, for a Fable review of the latest paper.

4. **Fable r2 review completed 2026-07-24** (`../07-revision-r2/REVIEW-STRENGTHENED.md`): NO FLAW FOUND — conditionally validated; 17/17 exact-arithmetic certificate checks pass, including the razor-thin exact Johnson-threshold margin; final unconditional verdict awaits the manuscript file itself, which the new share (same glitch as the first) does not physically contain.

## Corrections this update makes to earlier repo statements

- Earlier repo language said no manuscript supporting 1/12 was recoverable **from the first public share** — still true, but the 1/12 manuscript exists as a file on the author's side: it was uploaded into the r2 session and audited there (valid conditional per that session's two audits). The 1/12 constant is in any case now superseded by 11.346.
- The "adversarial patch" filename Babai asked about is confirmed to be the self-hostile-audit revision of the manuscript — it was the exact PDF fed into the r2 session.
- Kivva's requested source/[LLM] distinction is precisely what this repo's `06-fable-brief/DEPENDENCY_LEDGER.md` provides independently; the two artifacts (his requested annotations inside the paper, this repo's external ledger) now cross-corroborate.
