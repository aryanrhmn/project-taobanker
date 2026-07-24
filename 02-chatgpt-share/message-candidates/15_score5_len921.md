bash -lc set -euo pipefail
printf '%s\n' '--- manuscript headings ---'
grep -nE '^\\(section|subsection|begin\{(candidate|theorem|lemma|proposition|corollary))' /mnt/data/babai_motion_d3_audited.tex
printf '%s\n' '--- bibliography ---'
tail -100 /mnt/data/babai_motion_d3_audited.tex
printf '%s\n' '--- PS relevant phrases ---'
for pat in 'Proposition 2.12' 'Proposition 2.13' 'Proposition 2.14' 'Proposition 2.15' 'Proposition 2.19' 'Proposition 2.20' 'Theorem 2.21' 'Theorem 2.22' 'Theorem 2.23' 'Theorem 3.12' 'Metsch' 'Bang' 'motion'; do echo "### $pat"; grep -n -m 5 "$pat" /mnt/data/source_pyber_skresanov.txt || true; done
printf '%s\n' '--- Kivva relevant phrases ---'
for pat in 'Lemma 2.17' 'Lemma 2.18' 'Lemma 2.20' 'Theorem 2.25' 'Theorem 4.1' 'Theorem 4.6' 'Proposition 4.6' 'Biggs' 'Terwilliger' 'standard sequence'; do echo "### $pat"; grep -n -m 8 "$pat" /mnt/data/source_kivva_published.txt || true; done