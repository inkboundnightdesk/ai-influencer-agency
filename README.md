# AI Influencer Agency

Plug-and-play Grok Bot agency for [Inkbound Night Desk](https://inkboundnightdesk.com).

It creates **multiple AI influencers**, keeps them distinct, and writes the packets they use to promote the press site and house products. A person posts. The agency never logs in.

Sister desks:
- Press / ebooks — `inkboundnightdesk/Inkboundnightdesk-agency`
- Children's YouTube — `inkboundnightdesk/Children-s-YouTube-channel-agencycode` (do not mix)

## What you get

| Piece | Job |
|---|---|
| `GROKBOT.md` | Paste into Grok Bot. That is the plug. |
| `AGENTS.md` | Eight desks and three human gates. |
| `AGENT_RULES.md` | Operating contract. Load as system prompt. |
| `scripts/chief.py` | Create influencers, list the roster, build campaigns. |
| `influencers/` | One folder per persona. Spawn as many as you want. |
| `products/catalog.yaml` | What they are allowed to promote. |
| `review/` | Persona gate, content gate, publish gate. |

## Quick commands

```bash
python3 scripts/chief.py products
python3 scripts/chief.py new --niche dark-romantasy --name "Mara Vesper"
python3 scripts/chief.py list
python3 scripts/chief.py show mara-vesper
python3 scripts/chief.py campaign --influencer mara-vesper --offer the-cartographers-bond --days 7
python3 scripts/chief.py week --influencer vera-ink
```

## Starter roster

| Slug | Niche | Sells |
|---|---|---|
| `vera-ink` | dark-romantasy | Romantasy line + book pages |
| `night-archivist` | literary-press | Site, salon, catalog |

## The three gates

1. **Persona** — a human signs that the face, name, bio, and disclosure are approved.
2. **Content** — a human reads the week's packet.
3. **Publish** — a human posts. The files never claim a post went up.

Every persona is synthetic. Every owned relationship to Inkbound Night Desk is disclosed. House tool only — not a client agency for strangers.
