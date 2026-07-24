# Event record — the unit-coefficient manuscript (2026-07-24)

The author DM'd "UNIT CONSTANT" and attached `babai_motion_d3_unit_coefficient_source_crosswalk.pdf` (18 pages), a new manuscript claiming

**motion(X) >= n/d^3** (coefficient exactly 1) for every primitive DRG of diameter d >= 3, outside Johnson/Hamming.

This goes past the previously certified architecture limit (the 11.346 constant was pinned to Kivva's Johnson threshold) via four new modules: a Metsch-to-geometric parameter split, a local-grid Johnson argument replacing the spectral threshold entirely, exact dual-spectrum/incidence factors in the mu=1 branch, and an exact-envelope mu=2 certificate (19 refined rows + analytic tail). The document carries per-equation provenance tags pointing to original sources (Delsarte/Metsch/Koolen-Bang/Biggs/Terwilliger/Egawa) at each point of use — the fully matured response to Kivva's annotation request — and explicitly flags two audit corrections from its own exploratory draft.

**Fable review (same day): VALID AS WRITTEN** — see `../10-unit-coefficient/REVIEW-UNIT-COEFFICIENT.md`. The absent C++ checker was independently re-implemented from the displayed formulas; it reproduced the 19-row exception table, all nineteen beta_0 values, the worst certificate margin (1.0000005977102229, sixteen digits), and all three exact tail margins digit-for-digit.

Artifacts still on the author's side: the .tex source, `verify_unit_coefficient.cpp`/`.out`, and the intermediate 2n/(3d^3) draft referenced in the abstract. None affect the verdict; requested for lineage completeness.

Remaining relation to Babai's conjecture: the conjecture asks for motion >= gamma*n with gamma an absolute constant; the validated result now reads motion >= n/d^3 with coefficient 1 — the diameter dependence itself remains the open gap, and the manuscript's Remark 9.1 identifies exactly where the present architecture's coefficient saturates.
