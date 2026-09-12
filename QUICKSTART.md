# QUICKSTART — first influencer, first week

Goal: spawn one persona, lock a look, write seven posts, **stop before posting**.

## 0. Point Grok Bot here
Paste `GROKBOT.md`. That is the whole onboarding.

## 1. See what you can sell
```bash
python3 scripts/chief.py products
```

## 2. Spawn an influencer — or use a starter
```bash
python3 scripts/chief.py show vera-ink
python3 scripts/chief.py new --niche dark-romantasy --name "Mara Vesper"
```

Niches: `dark-romantasy` · `literary-press` · `mind-presence` · `thriller-night` · `catalog-host`

## 3. Gate 1 — persona
Fill `review/persona-gate.md`. Save to `audit/`. Generate three look stills from `handoffs/grok-imagine/` and drop them in `influencers/<slug>/refs/`.

## 4. Build a week
```bash
python3 scripts/chief.py campaign --influencer vera-ink --offer the-cartographers-bond --days 7
```

## 5. Gate 2 — content
Read every post out loud. Sign `review/content-gate.md`.

## 6. Gate 3 — you post
You create the accounts. You post. You file `review/publish-gate.md`.
Until then: **packet built, not posted.**

## 7. Make a second influencer
```bash
python3 scripts/chief.py new --niche literary-press --name "Silas Rook"
python3 scripts/chief.py campaign --influencer silas-rook --offer night-desk-site --days 7
```
Two people. Two voices. Two looks. Same house, different doors.
