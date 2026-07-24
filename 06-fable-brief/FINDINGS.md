# FINDINGS — ordered by severity

Scope: hostile line-by-line review of the three trusted manuscripts in `04-proof-assets/`, imports checked against `03-source-papers/pyber-skresanov-2312.00383.pdf` (PS) and `03-source-papers/kivva-1912.11427.pdf` (Kivva). `_suspect-not-true-file-content/` ignored for mathematics per instructions. "PS x.y"/"Kivva x.y" numbering below matches the arXiv PDFs in the package, which agree with the numbering the manuscripts cite.

---

## F0. No fatal flaw found in the primary manuscript (n/(14 d^3))

**File:** `babai_motion_d3_complete_proof.tex` — **Severity: none (result of the audit).**

Every step was independently rederived. In particular, each of the generator's own "most breakable" targets was attacked and held:

- **Exact adjacent-pair identity** (Lemma 2.1): D(1) = 2 + (2/k) sum_{i>=2} k_i c_i. Rederived from k p^1_{i,i} = k_i a_i and the telescoping k_i b_i = k_{i+1} c_{i+1}. The consequence D(1) > (mu/k) n uses c_2 <= b_1 (proved inline, correct) to get k_2 >= k, hence sum_{i>=2} k_i >= (n-1)/2. Correct.
- **Support-sensitive oriented geodesic boundary** (Lemma 2.2): the load P_e = sum_{a,b} N_e(a,b)/p(a,b) is edge-independent because it decomposes into intersection numbers (p^1_{j-1,j} counts of sources, p^j_{j+s,s} counts of sinks, and geodesic counts C_i = c_1...c_i depend only on distance). Everything is done in *oriented* edges (nk of them); no hidden factor of two. This sharpens the final inequality inside the proof of PS Prop. 2.8 exactly as claimed, and PS's own proof contains the support-sensitive form |delta(S)| >= |S| (k/d)(n-|S|)/n verbatim before their final weakening.
- **mu < k/(2d) preliminary step** (Prop. 3.1): uses PS Props. 2.10 + 2.12 (Dmin >= (n-k_max)/d for primitive configurations with relation diameters <= d, motion >= Dmin). Hypotheses verified: PS p.6 note that primitive DRG relations have diameter <= d. Correct.
- **Full Metsch => m <= d** (Prop. 3.1): the clique expression lambda + 2 - (ceil(3k/(2(lambda+1))) - 1)(mu - 1) appears verbatim inside the proof of PS Prop. 2.6, valid under lambda^2 >= 4 k mu (which implies Metsch's condition (lambda+1)^2 > (3k+lambda+1)(mu-1), as PS themselves derive). The three scalar certificates (alpha^2 > 4 gamma; alpha - 3gamma/(2 alpha) > 1/(d+1); alpha > (d+1)^2 gamma) were re-verified symbolically and by exact arithmetic. Delsarte bound gives m < d+1 with m real; Bang–Koolen (PS 2.5: lambda > m^2 mu => Delsarte-geometric) applies; integrality (PS Lemma 2.3) then gives m <= d. Correct.
- **Transition without diameter loss** (Lemma 4.1): D(1) >= n - (1-eps)(n-1) > eps n when a_i <= (1-eps)k for all i. Correct; strictly sharper than PS Prop. 2.11 (which loses a factor d) and proved independently.
- **High second eigenvalue** (Lemma 4.2): the chain rho > (1 + eps b_1)/k = (1-eps)/k + eps(k-lambda)/k >= ... > (eps/2)(1-gamma) = gamma is exact; uses 2 lambda <= k + mu (published: Kivva Lemma 2.5 = PS Lemma 2.4) and Babai's spectral bound (PS 2.13) with q = lambda (valid since lambda > mu). Correct.
- **mu=2 Riccati / relative-drop recurrence** (Lemma 6.4): y_{i+1} = (k - theta + c_i y_i/(1-y_i))/b_i is exactly equivalent to the standard-sequence three-term recurrence (rederived). Base case y_2 < C/(m-1) < A/(m-1) and induction y_{i+1} <= A/(m - tau_i) verified, including positivity of all u_i used, the requirement tau_{i-1} <= m-3 on the induction range (follows from strict growth), and the product/telescoping bound u_{t-1} >= u_1 (r/(r+t-2))(1 - delta H_{t-2}). Correct.
- **Multiplicity surplus R >= 1 + 1/m** (Lemma 6.6): the case analysis over (c_t, t, r) is *complete*: c_t >= c_{t-1} = tau_{t-1} psi_{t-2} >= t-1 always; c_t = t-1 forces r = m-t+1, t >= 4 (t=2 contradicts c_2 = 2, t=3 contradicts Kivva Cor. 2.8: c_3 > mu), and the quadrangle-Terwilliger inequality (Kivva Thm. 2.6, quadrangle supplied by Kivva Lemma 3.10(2)) forces r >= 2, so R = (t-1)(m-t+1)/m >= (m+1)/m on 4 <= t <= m-1; c_t >= t with t <= m-1 reduces to the two endpoint checks in r (the interior critical point of r/(r+t-2)^2 is a maximum), both verified; t = m forces r = 1 and either c_t >= m+1 (R >= (m+1)/m) or c_t = m, which the Terwilliger argument shows is impossible unless t = d (the designated endpoint c_t = t = m = d). The m = 2 corner (t = m = 2 < d) is killed by the same Terwilliger contradiction, so it cannot arise. Correct and gap-free.
- **Loss factor F > m/(m+1)** (Lemma 6.7): F >= 1 - 2(m+1) eps - 2 delta H_{t-2} > 1 - eps(6d^2 - 10d + 2) > d/(d+1); the polynomial certificate 2d^3 + 8d^2 + 16d - 5 > 0 and delta < 3 m eps, m eps < 1/60 all re-verified exactly. Correct.
- **Endpoint c_t = t = m = d => Hamming** (Prop. 6.1 end): Kivva Cor. 4.3 (assumptions of Lemma 4.2 hold at t = d; tau_d = m definitional) plus integrality gives tau_i = i, then psi_i = 1 for all i by the backward-monotonicity argument (identical to Kivva's own published Thm. 4.7 endgame), giving the H(d, 1+k/d) array; Egawa (Kivva Thm. 2.24) leaves Hamming or Doob, and Doob (k = 3d) is excluded by k > 14 d^3 - 1 (derivable from c_t >= 2, c_t < eps k). Correct.
- **mu >= 3 branch** (Prop. 5.1): disconnected local graphs contradict Kivva Prop. 3.11 (= PS 2.20; needs mu >= 3, d > 2, geometric — all present) since eps < 2/7; connected case applies PS Prop. 2.19, whose published absolute constant is eps* ~ 0.006551 > 0.0065, with eps = 2/(14 d^3 - 1) <= 2/377 ~ 0.00531 < 0.0065 and k > 14 d^3 >= max(m^3, 29). Hypotheses match exactly. Correct.
- **mu = 1 branch** (Prop. 7.1): dual-graph route rebuilt to avoid PS Prop. 2.14's hypothesis k >= 32 m d^2 (which n/(14 d^3) does *not* guarantee — the manuscript correctly noticed this and did not import 2.14). Dual degree (Kivva Lemma 2.26), spectral inclusion (Kivva Lemma 2.27, needs k >= m^2, satisfied), max common neighbors q = m-2 (Kivva Sec. 5.1 discussion, published), PS Prop. 2.9 spectral gap (unconditional), Babai bound on the dual, and Kivva Cor. 5.6 transfer with its published factor 1/2. Chain 3/(112 d^2) > 1/(14 d^3) for d >= 3. m=2 via Kivva Prop. 5.13 (mu=1, k>4, eigenvalue -2 — all hold); m=1 correctly excluded. Correct.

**Conclusion:** no gap. The remark in the manuscript's Section 9 accurately describes the relation to Kivva's published Prop. 4.6 (whose coarser surplus 1 + 1/(m^2-1) is what forced the published eps < 1/(6 m^4 d)).

---

## F1. `babai_motion_d3_final_candidate.tex` (2n/(5 d^3)): earliest unverifiable step is the Lv–Koolen import

**Severity: blocking for this manuscript's constant as stated. Location: Section 6, Proposition 6.1 ("The mu >= 3 collapse").**

> "Lemma 17 of Lv and Koolen [LK] gives 2 <= psi_1 <= tau_2 < tau_3 < ... < tau_d = m. ... Their Theorem 32 then identifies X as a Johnson graph."

arXiv:2601.10330 is a January 2026 **preprint**, is **not included** in `03-source-papers/`, and cannot be hypothesis-checked offline. The manuscript itself flags this ("The mu >= 3 endpoint uses a January 2026 preprint"). This is the earliest step of the 2/(5 d^3) proof that cannot be verified against a published source. It is not replaceable by the published route at this constant: PS Prop. 2.19 requires eps < eps* ~ 0.0065, but here eps = 4/(5 d^3 - 2) = 0.0301 (d=3) and 0.0126 (d=4); only for d >= 5 does eps fall below 0.0065. Verdict for this manuscript: **conditional on LK**, exactly as its own status box says. (Everything else in it that I could check verifies — see F2, F3.)

## F2. `final_candidate` d <= 16 rests on declared computer enumeration

**Severity: medium (methodological, disclosed). Location: Section 7.1.**

The mu=2 certificate for 3 <= d <= 16 is an exact-rational enumeration over relaxed admissible tuples (m, t, r, c_t). I verified (i) the tuple relaxation is logically complete (every graph-theoretically possible non-endpoint case is dominated by an enumerated tuple; monotonicity in c_t is correct; the m=2 corner is correctly excluded by the published Terwilliger argument), and (ii) `babai_motion_d3_final_audit.py` reproduces the manuscript's table exactly (min M = 1.007179713595 at d=7, (m,t,r,c_t) = (6,6,1,7); 5/12 margin 0.083%; 1/2 fails at 0.9650; analytic tail certified for 17 <= d <= 10000). This is acceptable as machine-checkable mathematics but contradicts nothing: note the *complete_proof* (1/14) genuinely eliminates the enumeration, as it claims.

## F3. `final_candidate`'s geodesic Poincare inequality k - theta_1 >= k/d^2 is correct

**Severity: none (positive finding on a designated attack surface). Location: Section 4, Proposition 4.1.**

The directed-geodesic load Q_e is edge-independent by the same intersection-number decomposition as PS Prop. 2.8 (with a distance weight, which is relation-determined); nkQ = sum dist^2; the Cauchy–Schwarz-along-geodesics step and the test-function step (theta_1-eigenvector is mean-zero) are standard and correctly executed; orientation bookkeeping is clean (sum over directed edges = 2 f^T (kI - A) f). This removes PS 2.9's Cheeger factor 8 legitimately. The manuscript's modest remark that this may be known (canonical paths) is appropriate.

## F4. Public claim n/(12 d^3) is not proved anywhere in the trusted package and is self-retracted

**Severity: high for the *social* claim (not for the manuscripts). Locations:** docstring of `babai_motion_d3_audited_scalar_check.py`; ChatGPT share narrative; `README_babai_motion_d5_audit.md` ("The earlier d^-3 coefficients 2/5, 1/8, 1/12 ... are withdrawn as theorem claims").

No trusted extracted `.tex` states or proves n/(12 d^3). The only manuscript-shaped occurrences are inside `_suspect-not-true-file-content/` (mis-extracted chat prose, excluded per instructions). Anyone publicizing this work should quote **n/(14 d^3)** (the strongest fully-written claim in the package) and not 1/12. Note the retraction README's reasoning ("new standard-sequence argument ... not independently verified") is *provenance-based*, not error-based: this review found no error in the successor 1/14 argument, but the retraction of 1/12 as a *claim* stands because no complete 1/12 manuscript exists in the package to audit.

## F5. Minor imprecisions in `complete_proof` (non-fatal, worth fixing before circulation)

**Severity: low.**

1. **Lemma 3.3 ("A small support moves an adjacent pair"):** "If x and x^g were nonadjacent, then they would be at distance two and would have exactly mu common neighbors." Distance could exceed two; then they have 0 common neighbors and the contradiction is even stronger. Harmless, but the sentence as written is false as a dichotomy. Same wording in the other two manuscripts.
2. **Uncited step tau_2 >= psi_1** (Section 6, before eq. (6.2)): this is exactly Kivva Lemma 2.17 and should carry the citation.
3. **Doob exclusion wording** (end of Prop. 6.1): "contrary to k > 14 d^3" — inside Prop. 6.1's hypotheses only k > 14 d^3 - 1 is derivable (from 2 <= c_t < eps k); this still excludes k = 3d with a huge margin, and in the main-theorem application k > 14 d^3 does hold. Cosmetic.
4. **PS Prop. 2.10 provenance:** PS prove it via Babai's unpublished lecture notes ("uni-update.pdf", their [5]). The import is from a published JCTB paper, so this is standard practice, but a referee may wish to note the second-order dependency.

## F6. Audit-script defects (supporting layer only; no mathematical impact)

**Severity: low.**

1. `babai_motion_d3_complete_audit.py` **crashes under Python 3.13 defaults**: `require(cond, f"...{loss}")` eagerly formats a giant exact Fraction into the (unused) failure message, hitting CPython's 4300-digit int-to-str limit (ValueError, not a failed check). It also recomputes an O(d) harmonic sum per d up to d = 100000, making the shipped script impractically slow. A faithful trimmed re-implementation of *all* its checks passes (see AUDIT_RUN_LOG.txt). Same performance pattern in `babai_motion_d3_audited_scalar_check.py` and `motion_d4_sanity_checks.py` (trimmed runs pass).
2. Scripts check scalar/integer claims only, as they themselves state; agreement of self-audits was given no evidential weight in this review.

## F7. Package/provenance notes

**Severity: informational.**

- `MANIFEST.json` shows the `_suspect-not-true-file-content/` files are byte-identical duplicates of one another under different names (e.g. `adversarial_independent_check.py` = `babai_motion_adversarial_referee_report.tex` = `..._patch.diff`, sha bdfc30d4...), with UTF-8 mojibake — confirming they are mis-extracted chat prose, correctly quarantined.
- The three trusted manuscripts cite PS and Kivva by their journal versions (JCTB 172 (2025) / JCTB 151 (2021)); every proposition/lemma number used matches the arXiv PDFs supplied in `03-source-papers/`. No numbering mismatch survives (the share narrative mentions an arXiv-vs-journal numbering fix during self-audit; the extracted final texts are consistent).
