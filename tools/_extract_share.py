"""Extract conversation text and metadata from ChatGPT share HTML."""
from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
HTML_PATH = BASE / "02-chatgpt-share" / "raw" / "raw-share-page.html"
OUT_DIR = BASE / "02-chatgpt-share"
RAW_DIR = OUT_DIR / "raw"


def main() -> None:
    raw = HTML_PATH.read_text(encoding="utf-8", errors="replace")
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", raw, re.S)
    print(f"scripts: {len(scripts)}")

    blob = None
    for s in scripts:
        if s.strip().startswith("{") and "authStatus" in s[:300]:
            blob = s
            break

    data = None
    if blob:
        data = json.loads(blob)
        state_path = RAW_DIR / "share-state.json"
        # Keep full dump if reasonable size
        text = json.dumps(data, indent=2, ensure_ascii=False)
        state_path.write_text(text, encoding="utf-8")
        print(f"saved share-state.json ({len(text)} chars), top keys: {list(data.keys())}")
        walk_interesting(data)

    # Stream payload often holds the actual conversation RSC payload
    stream = None
    for s in scripts:
        if "streamController.enqueue" in s and len(s) > 100_000:
            stream = s
            break
    if stream:
        (RAW_DIR / "stream-script.js").write_text(stream, encoding="utf-8")
        print(f"saved stream-script.js ({len(stream)} chars)")
        extract_from_stream(stream)

    # Also extract readable plain text chunks around key phrases from HTML
    extract_text_blocks(raw)

    # Build best-effort full markdown from state if mapping exists
    if data:
        md = build_markdown_from_state(data)
        if md:
            (OUT_DIR / "conversation-from-state.md").write_text(md, encoding="utf-8")
            print(f"saved conversation-from-state.md ({len(md)} chars)")


def walk_interesting(obj, path: str = "", depth: int = 0, max_depth: int = 8) -> None:
    if depth > max_depth:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}.{k}" if path else str(k)
            if k in {
                "mapping",
                "linear_conversation",
                "title",
                "messages",
                "content",
                "parts",
                "serverResponse",
                "data",
                "sharedConversation",
                "continue_conversation_url",
                "conversation_id",
                "share_id",
                "current_node",
                "moderation_results",
            }:
                if isinstance(v, (dict, list)):
                    print(f"KEY {p} {type(v).__name__} len={len(v)}")
                else:
                    print(f"KEY {p} = {str(v)[:200]}")
            walk_interesting(v, p, depth + 1, max_depth)
    elif isinstance(obj, list) and obj and depth < 4:
        walk_interesting(obj[0], path + "[0]", depth + 1, max_depth)


def extract_from_stream(stream: str) -> None:
    # Unescape common JS string escapes in enqueue payloads
    # Collect large JSON-looking substrings with message content
    # Extract all \"role\" occurrences near content
    roles = list(re.finditer(r'\\"role\\":\\"(user|assistant|system|tool)\\"', stream))
    print(f"escaped roles in stream: {len(roles)}")
    roles2 = list(re.finditer(r'"role"\s*:\s*"(user|assistant|system|tool)"', stream))
    print(f"plain roles in stream: {len(roles2)}")

    # Pull text fragments that look like markdown body parts
    # ChatGPT share often embeds message text as JSON strings
    candidates = []
    for m in re.finditer(r'"(Proposed theorem|## The result|Hostile referee|VALID AS WRITTEN|motion\\?\(X\\?\))', stream):
        start = max(0, m.start() - 200)
        end = min(len(stream), m.start() + 400)
        candidates.append(stream[start:end])
    (OUT_DIR / "stream-key-snippets.txt").write_text(
        "\n\n====\n\n".join(candidates[:50]), encoding="utf-8"
    )
    print(f"wrote stream-key-snippets ({len(candidates)} hits)")

    # Attempt to extract Flight/RSC string payloads
    payloads = re.findall(r'streamController\.enqueue\("((?:\\.|[^"\\])*)"\)', stream)
    print(f"enqueue payloads: {len(payloads)}")
    if payloads:
        joined = "\n\n---PAYLOAD---\n\n".join(payloads)
        # Unescape
        unescaped = bytes(joined, "utf-8").decode("unicode_escape", errors="replace")
        (RAW_DIR / "stream-payloads-unescaped.txt").write_text(unescaped, encoding="utf-8", errors="replace")
        print(f"saved stream-payloads-unescaped.txt ({len(unescaped)} chars)")


def extract_text_blocks(raw: str) -> None:
    # Visible page often has markdown-ish content; save a cleaned-ish dump
    # Remove script/style
    cleaned = re.sub(r"<script[^>]*>.*?</script>", "\n", raw, flags=re.S | re.I)
    cleaned = re.sub(r"<style[^>]*>.*?</style>", "\n", cleaned, flags=re.S | re.I)
    cleaned = re.sub(r"<[^>]+>", "\n", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = re.sub(r"[ \t]+\n", "\n", cleaned)
    (RAW_DIR / "page-text-dump.txt").write_text(cleaned, encoding="utf-8", errors="replace")
    print(f"saved page-text-dump.txt ({len(cleaned)} chars)")


def build_markdown_from_state(data: dict) -> str | None:
    """Try common ChatGPT share state shapes for conversation mapping."""
    # Search for a mapping dict with message nodes
    mapping = find_first_mapping(data)
    if not mapping:
        return None

    # Prefer linear order via current_node parent chain if possible
    nodes = []
    for node_id, node in mapping.items():
        if not isinstance(node, dict):
            continue
        msg = node.get("message")
        if not isinstance(msg, dict):
            continue
        author = (msg.get("author") or {}).get("role") or "unknown"
        create_time = msg.get("create_time")
        content = msg.get("content") or {}
        parts = content.get("parts") if isinstance(content, dict) else None
        text = ""
        if isinstance(parts, list):
            chunks = []
            for p in parts:
                if isinstance(p, str):
                    chunks.append(p)
                elif isinstance(p, dict):
                    # multimodal / attachments
                    chunks.append(json.dumps(p, ensure_ascii=False)[:2000])
            text = "\n".join(chunks)
        elif isinstance(content, dict) and "text" in content:
            text = str(content.get("text") or "")
        if not text.strip() and author in ("system",):
            continue
        parent = node.get("parent")
        children = node.get("children") or []
        nodes.append(
            {
                "id": node_id,
                "parent": parent,
                "children": children,
                "author": author,
                "create_time": create_time,
                "text": text,
            }
        )

    if not nodes:
        return None

    # Order by create_time when available
    def sort_key(n):
        t = n.get("create_time")
        return (t is None, t or 0)

    nodes_sorted = sorted(nodes, key=sort_key)

    lines = [
        "# Advancing Babai's Graph Theory",
        "",
        "_Extracted offline from ChatGPT shared conversation state._",
        "",
    ]
    for i, n in enumerate(nodes_sorted, 1):
        role = n["author"].upper()
        lines.append(f"## Message {i} — {role}")
        lines.append("")
        lines.append(n["text"] if n["text"].strip() else "_(empty or non-text content)_")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def find_first_mapping(obj):
    if isinstance(obj, dict):
        if "mapping" in obj and isinstance(obj["mapping"], dict):
            # heuristic: values look like chat nodes
            sample = next(iter(obj["mapping"].values()), None)
            if isinstance(sample, dict) and ("message" in sample or "parent" in sample):
                return obj["mapping"]
        for v in obj.values():
            found = find_first_mapping(v)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for v in obj:
            found = find_first_mapping(v)
            if found is not None:
                return found
    return None


if __name__ == "__main__":
    main()
