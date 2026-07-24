# Provenance index for the strengthened manuscript

## Convention

- `[PS, ...]`: Pyber--Skresanov, journal numbering.
- `[K, ...]`: Kivva, journal numbering.
- `[LLM]`: proved, defined, or algebraically derived in the manuscript rather than copied from an identified source.
- Combined labels identify both the imported input and the manuscript's modification or hypothesis check.

`[LLM]` is a provenance marker, not by itself a claim of conceptual novelty.

## New source-sensitive interface introduced by the strengthening

The improved coefficient uses Kivva's exact Johnson threshold rather than only the coarser statement `epsilon > 0.0065` quoted in Pyber--Skresanov.

- Root equation: `[K, Theorem 3.5]`
- Exact threshold definition: `[K, Proposition 3.6]`
- Johnson characterization: `[K, Theorem 1.2]`
- Rational lower bracket `epsilon_K > 3/458`: `[K, Theorem 3.5 and Proposition 3.6; LLM exact root bracket]`
- Comparison with the manuscript parameter: `[LLM exact rational certificate]`

## Strengthened manuscript-derived blocks

The following portions are explicitly marked as strengthened manuscript calculations:

- `C_0=5673/500`, `gamma`, and `epsilon`.
- The closure identity and the basic small-parameter bounds.
- The three structural inequalities used before Metsch and Bang--Koolen.
- The high-second-eigenvalue scalar domination `m<(1-epsilon)b_1`.
- The exact Johnson-threshold comparison.
- The `mu=1` valency checks with `C_0d^3`.
- The `mu=2` small-parameter and final loss certificates with `C_0d^3`.
- The Doob exclusion and final theorem constant.

## Imported source blocks retained unchanged

The strengthened version retains the same source interfaces for:

- Pyber--Skresanov Lemmas 2.2--2.4 and Propositions 2.5, 2.8, 2.10, 2.12--2.15, and 2.20.
- Kivva Theorem 2.6, Theorem 2.10, Lemmas 2.17--2.20, Corollary 2.8, Lemma 3.10, Lemma 4.2, Theorem 4.1, Theorem 2.25, and the endpoint argument in Theorem 4.7.
- The original Delsarte, Koolen--Bang, Metsch, Biggs, Terwilliger, and Egawa references listed in the bibliography.

## Automated coverage result

The checker reports:

```text
Provenance tags: total=330, LLM-containing=284, PS-containing=50, K-containing=62
PASS: every displayed equation has an immediate \eqprov label.
PASS: every non-structural prose paragraph has a provenance label.
```
