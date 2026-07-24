"""Extract /mnt/data proof assets (tex/py/md) from ChatGPT RSC payload strings."""
from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
IN_PATH = BASE / "02-chatgpt-share" / "raw" / "stream-payloads-unescaped.txt"
PROOF_DIR = BASE / "04-proof-assets"
SHARE_DIR = BASE / "02-chatgpt-share"

# Patterns for sandbox file writes
HEREDOC_RE = re.compile(
    r"cat\s+>\s+(/mnt/data/[\w.\-]+)\s+<<['\"]?(\w+)['\"]?\n(.*?)(?:\n)\2\b",
    re.S,
)
# Also capture python - <<'PY' that writes files internally - secondary
CP_RE = re.compile(r"cp\s+(/mnt/data/[\w.\-]+)\s+(/mnt/data/[\w.\-]+)")


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


def main() -> None:
    PROOF_DIR.mkdir(parents=True, exist_ok=True)
    data = json.loads(IN_PATH.read_text(encoding="utf-8", errors="replace"))
    strings: list[str] = []
    walk_strings(data, strings)
    print(f"strings: {len(strings)}")

    # Index by basename -> best content (prefer longest for same path)
    files: dict[str, tuple[str, str]] = {}  # basename -> (path, content)
    all_hits: list[tuple[str, int]] = []

    for s in strings:
        if "/mnt/data/" not in s and "cat >" not in s:
            continue
        for m in HEREDOC_RE.finditer(s):
            path, _tag, content = m.group(1), m.group(2), m.group(3)
            # content may still have trailing shell
            content = content.rstrip() + "\n"
            base = Path(path).name
            prev = files.get(base)
            if prev is None or len(content) > len(prev[1]):
                files[base] = (path, content)
            all_hits.append((path, len(content)))

    print(f"unique basenames from heredocs: {len(files)}")
    for base, (path, content) in sorted(files.items(), key=lambda x: -len(x[1][1])):
        out = PROOF_DIR / base
        out.write_text(content, encoding="utf-8", errors="replace")
        print(f"  WROTE {base:50s} {len(content):7d} chars  from {path}")

    # Also extract assistant narrative messages that are pure prose (not shell)
    prose = []
    for s in strings:
        if len(s) < 400:
            continue
        if s.lstrip().startswith("bash") or "cat > /mnt/data" in s[:200]:
            continue
        if s.count("\\") > len(s) / 10 and "documentclass" not in s:
            # likely escaped junk
            pass
        score = sum(
            1
            for t in (
                "Proposed theorem",
                "Strengthened candidate",
                "Adversarial-review",
                "How significant",
                "Hostile referee",
                "VALID AS WRITTEN",
                "motion",
                "Pyber",
                "Kivva",
                "Fable",
                "complete proof",
                "actual mathematical error",
            )
            if t.lower() in s.lower()
        )
        if score >= 2:
            prose.append((score, len(s), s))

    prose.sort(key=lambda x: (-x[0], -x[1]))
    # Dedup near-identical by first 200 chars
    seen = set()
    uniq = []
    for score, length, s in prose:
        key = s[:240]
        if key in seen:
            continue
        seen.add(key)
        uniq.append((score, length, s))

    conv_parts = [
        "# Advancing Babai's Graph Theory — Conversation Prose Blocks",
        "",
        "Extracted offline from ChatGPT share RSC payload.",
        "Shell/tool blocks with proof assets were extracted separately into `04-proof-assets/`.",
        "",
        "Source URL: https://chatgpt.com/share/6a627d97-c470-83ea-8fab-fba44b51d3a0",
        "",
    ]
    for i, (score, length, s) in enumerate(uniq[:30], 1):
        conv_parts.append(f"\n---\n\n## Prose block {i} (score={score}, len={length})\n\n")
        conv_parts.append(s)
        conv_parts.append("\n")
    conv_path = SHARE_DIR / "conversation-prose.md"
    conv_path.write_text("".join(conv_parts), encoding="utf-8")
    print(f"saved {conv_path.name} with {min(30, len(uniq))} prose blocks")

    # Manifest
    manifest = {
        "proof_assets": [
            {"filename": b, "source_path": p, "bytes": len(c.encode("utf-8", errors="replace"))}
            for b, (p, c) in sorted(files.items())
        ],
        "prose_blocks": len(uniq),
        "heredoc_hits": [{"path": p, "chars": n} for p, n in sorted(all_hits, key=lambda x: -x[1])],
    }
    (PROOF_DIR / "MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("saved MANIFEST.json")

    # List directory
    print("\n04-proof-assets contents:")
    for p in sorted(PROOF_DIR.iterdir()):
        print(f"  {p.name:50s} {p.stat().st_size:8d}")


if __name__ == "__main__":
    main()
