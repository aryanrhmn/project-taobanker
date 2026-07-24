"""Reconstruct ChatGPT share conversation from RSC/Flight stream payload."""
from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
IN_PATH = BASE / "02-chatgpt-share" / "raw" / "stream-payloads-unescaped.txt"
OUT_DIR = BASE / "02-chatgpt-share"
RAW_DIR = OUT_DIR / "raw"


def main() -> None:
    text = IN_PATH.read_text(encoding="utf-8", errors="replace").strip()
    # Payload is one big JSON array of mixed values with cross-refs like {"_1":2}
    data = json.loads(text)
    print(f"top-level items: {len(data)}")

    # Build id -> value map for numeric indices as they appear
    # In this format, the array is a flat list: [obj, str, obj, ...]
    # References like {"_31":32} point to array index 32 (1-based? 0-based?)
    # Let's inspect patterns around known content.

    # Collect all plain strings longer than 80 chars that look like message body
    strings = []
    walk_collect_strings(data, strings)
    strings = sorted(set(strings), key=len, reverse=True)
    print(f"unique long strings: {len(strings)}")
    for s in strings[:15]:
        print("---", len(s), s[:120].replace("\n", " "))

    # Save all long strings as candidates
    long_md = []
    for s in strings:
        if len(s) < 200:
            continue
        # Prefer markdown-ish content
        score = 0
        for token in ("## ", "### ", "\\boxed", "theorem", "motion", "proof", "Lemma", "arXiv", "Fable", "VALID", "GAP"):
            if token.lower() in s.lower():
                score += 1
        if score >= 2 or len(s) > 2000:
            long_md.append((score, len(s), s))

    long_md.sort(key=lambda x: (-x[0], -x[1]))
    print(f"markdown-ish candidates: {len(long_md)}")

    # Write individual message candidates
    msgs_dir = OUT_DIR / "message-candidates"
    msgs_dir.mkdir(exist_ok=True)
    for i, (score, length, s) in enumerate(long_md[:40], 1):
        (msgs_dir / f"{i:02d}_score{score}_len{length}.md").write_text(s, encoding="utf-8")
    print(f"wrote {min(40, len(long_md))} message candidate files")

    # Try to find conversation linear structure: look for mapping-like dicts
    mapping = find_mapping(data)
    if mapping:
        print(f"found mapping with {len(mapping)} nodes")
        md = render_mapping(mapping)
        (OUT_DIR / "conversation-full.md").write_text(md, encoding="utf-8")
        print(f"saved conversation-full.md ({len(md)} chars)")
        # attachments
        attachments = extract_attachments(mapping)
        (OUT_DIR / "attachments-index.json").write_text(
            json.dumps(attachments, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"attachments: {len(attachments)}")
    else:
        # Fallback: stitch top candidates into one dossier
        print("no mapping found; writing stitched fallback")
        parts = ["# Advancing Babai's Graph Theory\n", "_Reconstructed from RSC string candidates (order approximate)._\n"]
        for i, (score, length, s) in enumerate(long_md[:20], 1):
            parts.append(f"\n\n---\n\n## Candidate block {i} (score={score}, len={length})\n\n")
            parts.append(s)
        (OUT_DIR / "conversation-stitched.md").write_text("".join(parts), encoding="utf-8")
        print("saved conversation-stitched.md")

    # Also dump a flat list of all strings > 40 with roles nearby by searching original
    dump_role_context(text)


def walk_collect_strings(obj, out: list[str], depth: int = 0) -> None:
    if depth > 40:
        return
    if isinstance(obj, str):
        if len(obj) >= 80:
            out.append(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            walk_collect_strings(v, out, depth + 1)
    elif isinstance(obj, list):
        for v in obj:
            walk_collect_strings(v, out, depth + 1)


def find_mapping(obj):
    """Find chat mapping dict: keys are node ids, values have message/parent/children."""
    if isinstance(obj, dict):
        # direct hit
        if looks_like_mapping(obj):
            return obj
        for v in obj.values():
            found = find_mapping(v)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for v in obj:
            found = find_mapping(v)
            if found is not None:
                return found
    return None


def looks_like_mapping(d: dict) -> bool:
    if len(d) < 3:
        return False
    sample_vals = list(d.values())[:5]
    hits = 0
    for v in sample_vals:
        if not isinstance(v, dict):
            return False
        if "message" in v or ("parent" in v and "children" in v):
            hits += 1
    return hits >= 2


def render_mapping(mapping: dict) -> str:
    nodes = []
    for nid, node in mapping.items():
        if not isinstance(node, dict):
            continue
        msg = node.get("message")
        if not isinstance(msg, dict):
            continue
        author = ((msg.get("author") or {}) if isinstance(msg.get("author"), dict) else {}).get("role", "unknown")
        content = msg.get("content") or {}
        text = content_to_text(content)
        # also check metadata for attachments
        meta = msg.get("metadata") or {}
        nodes.append(
            {
                "id": nid,
                "parent": node.get("parent"),
                "author": author,
                "create_time": msg.get("create_time"),
                "text": text,
                "metadata": meta,
                "content_type": content.get("content_type") if isinstance(content, dict) else None,
            }
        )

    nodes.sort(key=lambda n: (n["create_time"] is None, n["create_time"] or 0))

    lines = [
        "# Advancing Babai's Graph Theory",
        "",
        "Source: ChatGPT shared conversation",
        "URL: https://chatgpt.com/share/6a627d97-c470-83ea-8fab-fba44b51d3a0",
        "t.co: https://t.co/PVqJk5RtgT",
        "",
        "---",
        "",
    ]
    for i, n in enumerate(nodes, 1):
        lines.append(f"## Message {i} — {n['author'].upper()}")
        lines.append("")
        lines.append(f"- node_id: `{n['id']}`")
        if n["create_time"] is not None:
            lines.append(f"- create_time: `{n['create_time']}`")
        if n["content_type"]:
            lines.append(f"- content_type: `{n['content_type']}`")
        lines.append("")
        lines.append(n["text"] if n["text"].strip() else "_(empty / non-text)_")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def content_to_text(content) -> str:
    if not isinstance(content, dict):
        return str(content)
    parts = content.get("parts")
    if isinstance(parts, list):
        chunks = []
        for p in parts:
            if isinstance(p, str):
                chunks.append(p)
            elif isinstance(p, dict):
                # file / image / code
                name = p.get("name") or p.get("file_name") or p.get("asset_pointer") or ""
                chunks.append(f"[attachment/object] {name}\n```json\n{json.dumps(p, ensure_ascii=False)[:5000]}\n```")
            else:
                chunks.append(str(p))
        return "\n\n".join(chunks)
    if "text" in content:
        return str(content.get("text") or "")
    return json.dumps(content, ensure_ascii=False)[:10000]


def extract_attachments(mapping: dict) -> list[dict]:
    out = []
    for nid, node in mapping.items():
        if not isinstance(node, dict):
            continue
        msg = node.get("message")
        if not isinstance(msg, dict):
            continue
        content = msg.get("content") or {}
        parts = content.get("parts") if isinstance(content, dict) else None
        if not isinstance(parts, list):
            continue
        for p in parts:
            if isinstance(p, dict):
                out.append({"node_id": nid, "part": p})
        meta = msg.get("metadata") or {}
        if isinstance(meta, dict):
            for key in ("attachments", "files", "file_ids"):
                if key in meta:
                    out.append({"node_id": nid, "metadata_key": key, "value": meta[key]})
    return out


def dump_role_context(text: str) -> None:
    # Search for "assistant" / "user" near "content"
    hits = []
    for m in re.finditer(r'"role"\s*:\s*"(user|assistant|system|tool)"', text):
        start = max(0, m.start() - 100)
        end = min(len(text), m.end() + 300)
        hits.append(text[start:end])
    (RAW_DIR / "role-contexts.txt").write_text("\n\n====\n\n".join(hits[:100]), encoding="utf-8")
    print(f"role contexts: {len(hits)}")

    # Search for file names that look like proof assets
    names = set(re.findall(r'[\w\-./]+\.(?:pdf|tex|py|zip|md|txt|json)', text, re.I))
    interesting = sorted(
        n for n in names if any(k in n.lower() for k in ("proof", "audit", "hostile", "babai", "motion", "manuscript", "latex", "fable", "repro"))
        or n.lower().endswith((".tex", ".py", ".pdf"))
    )
    (RAW_DIR / "filename-hits.txt").write_text("\n".join(sorted(names)), encoding="utf-8")
    print(f"filename hits: {len(names)}; interesting: {len(interesting)}")
    for n in interesting[:50]:
        print(" file:", n)


if __name__ == "__main__":
    main()
