#!/usr/bin/env python3
r"""Verify provenance annotations in the source-annotated LaTeX manuscript.

Checks performed:
1. Every displayed equation (\[...\] or equation/align environment) is followed
   by an \eqprov{...} label.
2. Every non-structural prose paragraph outside the bibliography contains at
   least one \prov{...} or \eqprov{...} label.
3. Reports counts of LLM, PS, and K provenance labels.

This is a syntactic guardrail for this manuscript, not a semantic proof that
an individual source pointer is correct.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def next_nonblank(lines: list[str], start: int) -> tuple[int, str] | None:
    for idx in range(start, len(lines)):
        if lines[idx].strip():
            return idx, lines[idx].strip()
    return None


def check_displays(lines: list[str]) -> list[str]:
    errors: list[str] = []
    closers = {r"\]", r"\end{equation}", r"\end{align}", r"\end{gather}"}
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped not in closers:
            continue
        nxt = next_nonblank(lines, idx + 1)
        if nxt is None or not nxt[1].startswith(r"\eqprov{"):
            where = "EOF" if nxt is None else f"line {nxt[0] + 1}: {nxt[1][:80]}"
            errors.append(
                f"Displayed equation ending at line {idx + 1} lacks an immediate "
                f"\\eqprov label (next nonblank: {where})."
            )
    return errors


def is_structural_paragraph(paragraph: str, in_bibliography: bool) -> bool:
    if in_bibliography:
        return True
    structural_tokens = (
        r"\documentclass", r"\usepackage", r"\newtheorem", r"\theoremstyle",
        r"\DeclareMathOperator", r"\newcommand", r"\definecolor", r"\title",
        r"\author", r"\date", r"\begin{document}", r"\end{document}",
        r"\maketitle", r"\section{", r"\begin{center}", r"\end{center}",
        r"\begin{tabular}", r"\end{tabular}", r"\toprule", r"\midrule",
        r"\bottomrule", r"\renewcommand", r"\begin{thebibliography}",
        r"\end{thebibliography}", r"\bibitem",
    )
    return any(token in paragraph for token in structural_tokens)


def check_paragraphs(text: str) -> list[str]:
    errors: list[str] = []
    in_bibliography = False
    for number, paragraph in enumerate(text.split("\n\n"), start=1):
        if r"\begin{thebibliography}" in paragraph:
            in_bibliography = True
        compact = " ".join(line.strip() for line in paragraph.splitlines()).strip()
        if not compact or is_structural_paragraph(compact, in_bibliography):
            if r"\end{thebibliography}" in paragraph:
                in_bibliography = False
            continue
        # Ignore paragraphs that are only environment delimiters or labels.
        visible = re.sub(r"\\(?:begin|end)\{[^}]+\}", "", compact)
        visible = re.sub(r"\\label\{[^}]+\}", "", visible).strip()
        if len(visible) < 15:
            continue
        if r"\prov{" not in compact and r"\eqprov{" not in compact:
            errors.append(
                f"Paragraph {number} has no provenance label: {compact[:180]}"
            )
        if r"\end{thebibliography}" in paragraph:
            in_bibliography = False
    return errors


def count_tags(text: str) -> dict[str, int]:
    tags = re.findall(r"\\(?:eq)?prov\{([^}]*)\}", text)
    return {
        "total": len(tags),
        "LLM": sum("LLM" in tag for tag in tags),
        "PS": sum(re.search(r"(?:^|; )PS,", tag) is not None for tag in tags),
        "K": sum(re.search(r"(?:^|; )K,", tag) is not None for tag in tags),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tex", nargs="?", default="babai_motion_d3_source_annotated_strengthened.tex")
    args = parser.parse_args()

    path = Path(args.tex)
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors = check_displays(lines) + check_paragraphs(text)
    counts = count_tags(text)

    print(
        "Provenance tags: "
        f"total={counts['total']}, LLM-containing={counts['LLM']}, "
        f"PS-containing={counts['PS']}, K-containing={counts['K']}"
    )
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("PASS: every displayed equation has an immediate \\eqprov label.")
    print("PASS: every non-structural prose paragraph has a provenance label.")
    print("NOTE: this checker verifies annotation coverage, not source correctness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
