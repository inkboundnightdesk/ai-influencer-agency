# Instagram Operator Packet
Inkbound Night Desk — AI Influencer Agency
Version 2026-09-11

This is the one file you run Instagram from.
The agency repo prepares work. A person posts.

## 0. How to use this packet
Do the sections in order. Do not skip 1–4.
1. Pick or spawn the influencer (chief.py new or use Vera / Archivist).
2. Build three stills from the look brief. Drop them in influencers/<slug>/refs/.
3. Sign Gate 1 (persona).
4. Create the Instagram account. Flip the labels in section 3 before you post anything.
5. Run Days 1–30 from section 6.
6. Sign Gate 2 on each week’s captions before they go up.
7. Post. File Gate 3. Track the link, not the likes.
Kids-channel content does not enter this packet.

## 1. Roster card
Fill slug, name, niche, @handle, AI-generated profile ON/OFF, offer this month, catalog status, destination URL, UTM, Gate 1 date, stills, owner who posts.
Starters: vera-ink (dark romantasy), night-archivist (press clerk). They do not share a face, a voice, or a grid.

## 2. What Instagram is for
Visual door. Needs stills. Sell with taste, not a fake life.
Do: house page, stay in character, disclose AI + house, one title per post, track sessions.
Do not: “I bought it last night,” pretend she lives in Tampa, bury #ad, seven buy-nows, worship ER.
If offer status is not live in products/catalog.yaml, no buy now.

## 3. Account setup — this order
1. Pro account. Email/phone off the repo.
2. Short handle.
3. Hero still as photo. Same crop forever.
4. Name field = persona name only.
5. Bio from section 4. First line is the AI line.
6. Flip Instagram’s AI-generated profile label (31 Aug 2026; replaced AI creator). Unlabeled synthetic-person accounts lose Explore reach.
7. Link in bio = house page + UTM.
8. Highlights: Desk · Books · Night · Who this is.
9. Who this is slide: “AI persona for Inkbound Night Desk.”
10. Do not follow the children’s YouTube account.
11. Write handle into influencers/<slug>/platforms.md.
Composer: AI content label + branded-content toggle on every promo post. Two toggles.

## 4. Copy you paste
Vera bio:
Vera Ink
AI persona for Inkbound Night Desk.
I read the dark ones.
inkboundnightdesk.com

Archivist bio:
Night Archivist
AI persona. Night clerk for Inkbound Night Desk.
inkboundnightdesk.com

Promo line: Ad · I am an AI persona for Inkbound Night Desk.
If asked are you real: No. AI persona for the press. The books are real. The page is in the bio.

## 5. Caption formula
Hook / beat / pointer / disclosure. 40–90 words. No fire emoji. If swapping names still works, rewrite.

## 6. First 30 days
1–7 face + who this is (5 posts, no offer).
8–14 taste (4, site soft).
15–21 desk + collection (4, no buy-now if slated).
22–30 one clean offer week (5, live only).
Week mix: 3 presence / 2 taste / 2 offer. Stills 14 days before motion.

## 7. Ready week — Vera × site
python3 scripts/chief.py campaign --influencer vera-ink --offer night-desk-site --days 7

## 8. Tracking
?utm_source=instagram&utm_medium=organic&utm_campaign=<slug>-<month>
Watch profile visits, link taps, sessions, checkout starts. Ignore is-she-real likes.
High comments + zero sessions = fix the pointer, not the face.

## 9. Gates
1 persona  2 content  3 you posted.
Until gate 3: packet built, not posted.

## 10. Hard stops
No clones, no is-she-real bait, no fake proof, no auto-post, no kids mix, no duplicate personas, no fake-stranger collabs, no file DMs, no testimonials of use from a body that does not exist.

## 11. When a title goes live
Flip status in catalog.yaml. Confirm checkout. Rebuild campaign. Keep the 3/2/2 mix.

## 12. Spawn another
python3 scripts/chief.py new --niche literary-press --name "Silas Rook"
Then repeat 1–4.
