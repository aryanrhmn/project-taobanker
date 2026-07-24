# Fable 5 setup status

**Updated:** 2026-07-23 (after Babai-reply post)

## Trigger

| Item | Detail |
|------|--------|
| Urgency post | https://x.com/taobanker/status/2080422087882104956 |
| Ask | “Can someone please have Fable do an adversarial review ASAP?” |
| Babai action | Forwarded manuscript to **Bohdan Kivva**; requested author/LLM disclosure |
| Offline archive | `01-x-post/POST-2-BABAI-REPLY.md` + email screenshot in `05-media/` |

## Runtime on this machine

| Component | Value |
|-----------|--------|
| Claude Code | `<user-home>\.local\bin\claude.exe` (v2.1.218) |
| Model | `claude-fable-5[1m]` (verified: responds as Claude Fable 5) |
| Project CLAUDE.md | `../CLAUDE.md` |
| Project settings | `../.claude/settings.local.json` (model + xhigh effort) |
| Launch script | `Launch-Fable5.ps1` |
| Launch prompt | `FABLE_LAUNCH_PROMPT.md` |
| Task spec | `FABLE_TASK.md` |
| Hostile standard | `HOSTILE_REFEREE_PROMPT.md` |

## How to run

```powershell
cd "<package-root>"
pwsh -File .\06-fable-brief\Launch-Fable5.ps1
```

## Expected outputs

After a successful run, these should appear in this folder:

- `VERDICT.md`
- `FINDINGS.md`
- `DEPENDENCY_LEDGER.md`
- `CONSTANT_AUDIT.md`
- `runs/fable5-*.log`
