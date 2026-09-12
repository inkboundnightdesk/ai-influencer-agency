# Instagram Operator Packet
Inkbound Night Desk — AI Influencer Agency
Version 2026-09-11

This is the one file you run Instagram from.
The agency repo prepares work. A person posts.

---

## 0. How to use this packet

Do the sections in order. Do not skip 1–4.

1. Pick or spawn the influencer (`chief.py new` or use Vera / Archivist).
2. Build three stills from the look brief. Drop them in `influencers/<slug>/refs/`.
3. Sign Gate 1 (persona).
4. Create the Instagram account. Flip the labels in section 3 before you post anything.
5. Run Days 1–30 from section 6.
6. Sign Gate 2 on each week’s captions before they go up.
7. Post. File Gate 3. Track the link, not the likes.

Kids-channel content does not enter this packet.

---

## 1. Roster card (fill this)

| Field | Write it here |
|---|---|
| Slug | |
| Name | |
| Niche | dark-romantasy / literary-press / mind-presence / thriller-night / catalog-host |
| Instagram handle | @ |
| Profile label | AI-generated profile  ON / OFF |
| Offer this month | night-desk-site / the-cartographers-bond / romantasy-line / literary-line / mind-presence-line |
| Offer status in catalog.yaml | live / slated / packet |
| Destination URL | |
| UTM template | `?utm_source=instagram&utm_medium=organic&utm_campaign=<slug>-<month>` |
| Gate 1 signed | date + file in audit/ |
| Stills in refs/ | hero / three-quarter / environment |
| Owner who posts | |

Starter roster already built:

- `vera-ink` — dark-romantasy reader. Sells the romantasy line and the site.
- `night-archivist` — press night clerk. Sells the site and the catalog.

They do not share a face, a voice, or a grid.

---

## 2. What Instagram is for (and is not)

Instagram is the visual door. It needs stills. X can run text. This packet assumes stills exist.

Sell with taste, not with a fake life.

| Do | Do not |
|---|---|
| Point at the house page | Say “I bought it last night” |
| Stay in character | Pretend she lives in Tampa and you could meet her |
| Disclose AI + house relationship | Bury #ad in hashtags |
| One title or one page per post | Seven buy-nows in a row |
| Track sessions and checkout | Worship engagement rate |

Research pattern to remember: virtual accounts often get **more comments** than humans and **fewer purchases** in high-trust categories. Books sit in the middle — covers and night-mood convert; “this healed me” does not.

If offer `status` is not `live` in `products/catalog.yaml`, the caption may talk about the work. It may not say buy now.

---

## 3. Account setup — do this once, in this order

1. Create a professional Instagram account. Business or creator. Email and phone stay off the repo.
2. Username: short, pronounceable, not a string of underscores. Examples of shape: `@veraink` / `@nightarchivist` — pick what is free.
3. Profile photo: the approved hero still. Same crop forever.
4. Name field: persona name only. Not “Vera Ink AI BookTok 18+”.
5. Bio: paste from section 4. First line is the AI line.
6. Flip Instagram’s **AI-generated profile** label (as of 31 Aug 2026 this replaced “AI creator”). Unlabeled synthetic-person accounts get reach cut on Explore / recommendations.
7. Link in bio: the house page with UTM, or a simple Linktree that only lists house URLs.
8. Highlights, in this order: Desk · Books · Night · Who this is
9. “Who this is” highlight: one slide, large type — “AI persona for Inkbound Night Desk.”
10. Close Friends lists and personal phone contacts stay off this account.
11. Do not follow the children’s YouTube account from this profile.
12. Write the public handle into `influencers/<slug>/platforms.md`. Nothing else.

Composer toggles on every promo post:

- AI content / synthetic label when the face or scene is generated
- Paid partnership / branded content when a title or a link appears

Two toggles. Not one.

---

## 4. Copy you actually paste

### Bio — Vera Ink

```
Vera Ink
AI persona for Inkbound Night Desk.
I read the dark ones.

inkboundnightdesk.com
```

### Bio — Night Archivist

```
Night Archivist
AI persona. Night clerk for Inkbound Night Desk.

inkboundnightdesk.com
```

### Bio — any new persona

```
<Name>
AI persona for Inkbound Night Desk.
<one taste line>

inkboundnightdesk.com
```

### Promo post (owned relationship — use when a title or a link appears)

Pick one. Top or bottom. Never missing.

```
Ad · I am an AI persona for Inkbound Night Desk.
```

```
#ad AI persona. I work for the press that made this book.
```

### Presence post (no title, no link)

Profile already discloses AI. You do not need #ad. If you hesitate, use the promo line.

### Story text overlay

```
AI persona · Inkbound Night Desk
```

### Comment reply, if asked “are you real?”

```
No. AI persona for the press. The books are real. The page is in the bio.
```

Do not turn that question into a game.

---

## 5. Caption formula

Every IG caption has four beats. Cut any beat and the post gets sloppy.

1. **Hook** — one breath. First line is the only line most people read.
2. **Beat** — one image or one standard. In that persona’s voice.
3. **Pointer** — house page, or nothing. Never a raw Amazon search.
4. **Disclosure** — the promo line if this post sells.

Length: 40–90 words. No fire emoji. No “unputdownable.” No ALL CAPS sell.

Read it aloud in the persona’s register. If it still works after you swap the name with the other roster name, rewrite. That is house-voice leaking.

---

## 6. First 30 days

Do not launch with a sale week. Novelty comments will look like demand. They are not.

| Days | Job | Posts | Offer |
|---|---|---|---|
| 1–7 | Face lock + who this is | 5 feed or Reels stills | none |
| 8–14 | Taste | 4 | site only, soft |
| 15–21 | Desk + one collection | 4 | site, or a slated title with no buy-now |
| 22–30 | One clean offer week | 5 | live offer only; else keep pointing at the site |

Mix inside any week of 7:

- 3 presence (no sell)
- 2 taste / craft
- 2 offer or offer-soft

Seven offer posts is a farm. Instagram already punishes farms.

Grid rule: same palette, same face lock, same time-of-day. If a still drifts (new nose, new locs pattern, new glasses), it does not ship.

Reels vs feed: stills first for 14 days. Add a Reel only when the face is stable in motion. Slideshow Reels from three locked stills beat a warped talking head.

Stories: 3–5 a week after day 7. One is always “Who this is.” The rest can be a crop of the day’s still plus the overlay line.

---

## 7. Ready week — Vera Ink × site (safe while titles are slated)

Use this if you have not flipped `the-cartographers-bond` to `live`.

**Day 1 presence.** Hook: The lamp is still on.
Caption: I reread the map pages. Not because I was lost. Because the cost was on the paper.

**Day 2 taste.** Hook: I do not want love that leaves no mark.
Caption: A bond that costs something. That is the whole taste. Everything else is costume.

**Day 3 presence.** Hook: Ink on the finger. Work.
Caption: If the caption needs a fire emoji it is not my book.

**Day 4 offer-soft.** Hook: The desk.
Caption: Inkbound Night Desk. Finished ebooks, direct from the press. The page is in the bio.
Disclosure: Ad · I am an AI persona for Inkbound Night Desk.

**Day 5 craft.** Hook: Reread is a standard.
Caption: I will not call a book finished in a caption if I have not finished it.

**Day 6 presence.** Hook: Night window.
Caption: The press is in Tampa. I am a persona. That is already in the bio.

**Day 7 offer-soft.** Hook: If you want the door.
Caption: House page first. I will not stack seven buy-nows on you.
Disclosure: Ad · I am an AI persona for Inkbound Night Desk.

Generate the week instead of typing it:

```bash
python3 scripts/chief.py campaign --influencer vera-ink --offer night-desk-site --days 7
```

Then edit until it sounds like her.

---

## 8. Tracking — the only numbers that matter

Put UTM on every bio link and every caption link.

```
https://inkboundnightdesk.com/?utm_source=instagram&utm_medium=organic&utm_campaign=vera-ink-2026-09
```

Scoreboard per week:

| Metric | Target for month 1 | Ignore |
|---|---|---|
| Profile visits | rising | vanity likes from “is she real” |
| Link taps | rising | follower count spikes after a face-reveal comment |
| Sessions on house page from IG | any number > 0, then up | raw ER vs human influencers |
| Checkout starts | even one is a real signal | comments that do not click |

If comments are high and sessions are zero, the still is winning and the pointer is losing. Fix the last two lines of the caption. Do not generate a new face.

---

## 9. Gates (do not route around)

**Gate 1 — persona.** Face lock distinct. Voice distinct. No real-person likeness. Bio discloses AI + Night Desk. Stills approved. File in `audit/`.

**Gate 2 — content.** Disclosure present on promo posts. Links match `catalog.yaml`. No buy-now on a non-live offer. No fake proof. Sounds like this influencer. File in `audit/`.

**Gate 3 — publish.** You posted. AI-generated profile is on. Per-post labels flipped. Destination URL correct. File in `audit/`.

Until Gate 3 is signed, the correct sentence is: packet built, not posted.

---

## 10. Hard stops

- No real-person clone. No celebrity. No scraped face.
- No “is she real?” bait.
- No fake ranks, reviews, follower counts, or “now live.”
- No login by the agent. No auto-post.
- No children’s channel. No young-readers hard-sell from these accounts.
- No near-duplicate persona. If you can swap the names and the caption still works, rewrite or kill it.
- No collab between roster accounts that pretends they “just found” each other. If they share a frame, the packet says so and both bios stay honest.
- No DMs that attach files. No “comment BOOK and I’ll send the PDF.”

---

## 11. When a title goes live

1. Change `status: live` on that offer in `products/catalog.yaml`.
2. Confirm the URL loads and checkout works. A person does this.
3. Rebuild the week: `chief.py campaign --influencer vera-ink --offer the-cartographers-bond --days 7`
4. Captions may now say the page is up. They still do not invent reviews.
5. Keep 3 presence / 2 taste / 2 offer.

---

## 12. Spawn another influencer

```bash
python3 scripts/chief.py new --niche literary-press --name "Silas Rook"
```

Then repeat sections 1–4 for that slug. Two grids. Two faces. Same house.

Niches: `dark-romantasy` · `literary-press` · `mind-presence` · `thriller-night` · `catalog-host`
