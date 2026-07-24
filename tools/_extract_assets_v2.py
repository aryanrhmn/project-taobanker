"""Broader extraction of sandbox text files from RSC payload."""
from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
IN_PATH = BASE / "02-chatgpt-share" / "raw" / "stream-payloads-unescaped.txt"
PROOF_DIR = BASE / "04-proof-assets"
EXTRA_DIR = PROOF_DIR / "extracted-extra"
EXTRA_DIR.mkdir(parents=True, exist_ok=True)

TARGET_NAMES = [
    "fable_hostile_referee_prompt_d3_c12.txt",
    "fable_hostile_referee_prompt_d5.txt",
    "babai_motion_d3_adversarially_patched.tex",
    "babai_motion_adversarial_referee_report.tex",
    "babai_motion_d3_audited.tex",
    "babai_motion_d3_audited_pre_hostile.tex",
    "babai_motion_d3_revised_candidate.tex",
    "babai_motion_d3_sharpened_candidate.tex",
    "babai_motion_d3_strengthened_candidate.tex",
    "babai_motion_d3_candidate_note.tex",
    "research_note_motion_d4.tex",
    "babai_motion_d3_c12_symbolic_audit.py",
    "babai_motion_d3_c12_audit.py",
    "babai_motion_d5_scalar_audit.py",
    "adversarial_independent_check.py",
    "babai_motion_d3_strengthened_audit.py",
    "babai_motion_d3_audit.py",
    "babai_motion_d3_adversarial_patch.diff",
]


def walk_strings(obj, out: list[str], depth: int = 0) -> None:
    if depth > 50:
        return
    if isinstance(obj, str):
        out.append(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            walk_strings(v, out, depth + 1)
    elif isinstance(obj, list):
        for v in obj:
            walk_strings(v, out, depth + 1)


def extract_heredocs(s: str) -> list[tuple[str, str]]:
    results = []
    # cat > path <<'TAG' ... TAG
    for m in re.finditer(
        r"cat\s+>\s+(/mnt/data/[\w.\-]+)\s+<<['\"]?(\w+)['\"]?\n(.*?)(?:\n)\2\b",
        s,
        re.S,
    ):
        results.append((Path(m.group(1)).name, m.group(3).rstrip() + "\n"))
    # tee path <<'TAG'
    for m in re.finditer(
        r"tee\s+(/mnt/data/[\w.\-]+)\s+<<['\"]?(\w+)['\"]?\n(.*?)(?:\n)\2\b",
        s,
        re.S,
    ):
        results.append((Path(m.group(1)).name, m.group(3).rstrip() + "\n"))
    return results


def extract_python_write(s: str) -> list[tuple[str, str]]:
    """Catch Path(...).write_text('''...''') and open(...).write patterns."""
    results = []
    for m in re.finditer(
        r"""(?:Path\(['\"](/mnt/data/[\w.\-]+)['\"]\)\.write_text\(|open\(['\"](/mnt/data/[\w.\-]+)['\"].*?\)\.write\()(['\"]){1,3}(.*?)(['\"]){1,3}""",
        s,
        re.S,
    ):
        path = m.group(1) or m.group(2)
        content = m.group(4)
        results.append((Path(path).name, content))
    # f = open/write with triple quotes simpler
    for m in re.finditer(
        r"""open\(['\"](/mnt/data/[\w.\-]+)['\"],\s*['\"]w['\"].*?\)\s*\.write\((['\"]{3})(.*?)(['\"]{3})\)""",
        s,
        re.S,
    ):
        results.append((Path(m.group(1)).name, m.group(3)))
    return results


def extract_name_near_content(s: str, name: str) -> str | None:
    """If a string is the file content itself labeled by filename nearby."""
    if name not in s and f"/mnt/data/{name}" not in s:
        return None
    # If the entire string is mostly the file body after a header
    # Try: after first occurrence of filename, take remaining if long
    idx = s.find(name)
    if idx < 0:
        idx = s.find(f"/mnt/data/{name}")
    if idx < 0:
        return None
    # For prompt files, content often starts after the path line
    after = s[idx + len(name) :]
    # strip leading punctuation/newlines
    after = re.sub(r"^[\s:=\-]+", "", after)
    if len(after) > 500 and ("VALID" in after or "referee" in after.lower() or "\\documentclass" in after or "import " in after or "Theorem" in after):
        return after
    return None


def main() -> None:
    data = json.loads(IN_PATH.read_text(encoding="utf-8", errors="replace"))
    strings: list[str] = []
    walk_strings(data, strings)
    print(f"strings: {len(strings)}")

    best: dict[str, str] = {}

    for s in strings:
        for name, content in extract_heredocs(s) + extract_python_write(s):
            if name not in best or len(content) > len(best[name]):
                best[name] = content

    # Targeted name search for missing files
    for name in TARGET_NAMES:
        if name in best and len(best[name]) > 200:
            continue
        candidates = []
        for s in strings:
            if name not in s and f"/mnt/data/{name}" not in s:
                continue
            # Prefer strings that look like the body of that file
            if name.endswith(".txt") and ("You are" in s or "VALID AS WRITTEN" in s or "hostile" in s.lower() or "adversarial" in s.lower()):
                candidates.append(s)
            elif name.endswith(".tex") and "\\documentclass" in s:
                candidates.append(s)
            elif name.endswith(".py") and ("import " in s or "def " in s):
                candidates.append(s)
            elif name.endswith(".diff") and ("---" in s or "+++" in s):
                candidates.append(s)
            else:
                # store full string if it contains path and is long
                if len(s) > 400:
                    candidates.append(s)
        if candidates:
            # pick longest that isn't a bash wrapper listing many files
            candidates.sort(key=len, reverse=True)
            chosen = candidates[0]
            # If it's a heredoc wrapper, try extract again
            h = extract_heredocs(chosen)
            for n, c in h:
                if n == name:
                    chosen = c
                    break
            else:
                # strip bash preamble if present
                if "cat >" in chosen and "<<'" in chosen:
                    m = re.search(
                        rf"cat\s+>\s+/mnt/data/{re.escape(name)}\s+<<['\"]?(\w+)['\"]?\n(.*?)(?:\n)\1\b",
                        chosen,
                        re.S,
                    )
                    if m:
                        chosen = m.group(2).rstrip() + "\n"
            best[name] = chosen
            print(f"targeted hit: {name} ({len(chosen)} chars)")

    # Write all newly found that are not already in PROOF_DIR or improve them
    wrote = []
    for name, content in sorted(best.items()):
        # skip tiny junk
        if len(content) < 50:
            continue
        # Prefer writing known targets and any .tex/.py/.txt/.md/.diff
        if not name.endswith((".tex", ".py", ".txt", ".md", ".diff", ".log")):
            continue
        dest = PROOF_DIR / name
        if dest.exists() and dest.stat().st_size >= len(content.encode("utf-8", errors="replace")):
            # keep existing better version; still save to extra if different target list
            alt = EXTRA_DIR / name
            if name in TARGET_NAMES and not dest.exists():
                pass
            continue
        dest.write_text(content, encoding="utf-8", errors="replace")
        wrote.append((name, len(content)))
        print(f"WROTE {name:55s} {len(content):7d}")

    print(f"\nTotal unique text assets now in best map: {len(best)}")
    print(f"Wrote/updated: {len(wrote)}")

    # Special: dump any string that looks like the d3_c12 hostile prompt
    for key in ("fable_hostile_referee_prompt_d3_c12.txt", "fable_hostile_referee_prompt_d5.txt"):
        path = PROOF_DIR / key
        if path.exists():
            print(f"PRESENT {key} size={path.stat().st_size}")
            print(path.read_text(encoding="utf-8", errors="replace")[:400])
        else:
            print(f"MISSING {key}")

    # List final proof dir
    print("\nFinal 04-proof-assets:")
    for p in sorted(PROOF_DIR.rglob("*")):
        if p.is_file():
            print(f"  {p.relative_to(PROOF_DIR)}  ({p.stat().st_size})")


if __name__ == "__main__":
    main()
