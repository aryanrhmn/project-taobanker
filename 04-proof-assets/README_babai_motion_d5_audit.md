# Babai motion-bound audit package

## Current claim

Unrefereed, source-audited candidate:

> If `X` is a primitive distance-regular graph on `n` vertices of diameter `d >= 3`, then `X` is Johnson or Hamming, or
> `motion(X) >= n/(13 d^5)`.

## Retraction

The earlier `d^{-3}` coefficients `2/5`, `1/8`, `1/12`, and related variants are withdrawn as theorem claims. Their Hamming branch uses a new standard-sequence argument that has not been independently verified.

## Why this version is more robust

The `mu = 2` branch now invokes the published Hamming characterization exactly as stated (Pyber--Skresanov Proposition 2.21 / Kivva Corollary 4.8). No finite parameter enumeration, recent preprint, or new multiplicity recurrence is used.

The new content is confined to:

1. the exact adjacent-pair identity `D(1) = 2 + (2/k) sum_{i=2}^d k_i c_i`;
2. a support-sensitive adjacent-pair reduction with an explicitly directed boundary;
3. an exact transition bound with no extra factor of `d`;
4. retention of the full Metsch clique expression, yielding `m <= d`.

## Files

- `babai_motion_d5_source_audited.pdf`: manuscript.
- `babai_motion_d5_source_audited.tex`: LaTeX source.
- `babai_motion_d5_scalar_audit.py`: exact rational and symbolic checks for every new numerical inequality. It does not verify graph-theoretic reductions.
- `fable_hostile_referee_prompt_d5.txt`: prompt for an adversarial independent-model audit.

## Verification standard

A second model's agreement is useful evidence, not certification. Before citation as a theorem, the argument should be checked by a specialist or formalized sufficiently to remove the remaining human-level dependency matching.
