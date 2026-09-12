#!/usr/bin/env python3
"""Inkbound Night Desk AI Influencer Agency CLI. Stdlib only."""
from __future__ import annotations
import argparse, csv, datetime as dt, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INFLUENCERS = ROOT / "influencers"
PRODUCTS = ROOT / "products" / "catalog.yaml"
CAMPAIGNS = ROOT / "campaigns"
HANDOFFS = ROOT / "handoffs" / "grok-imagine"
AUDIT = ROOT / "audit"

NICHES = {
    "dark-romantasy": {"age_band": "26-34", "offers": ["night-desk-site", "the-cartographers-bond", "romantasy-line"], "want": "A bond story that costs something.", "taste": "Dark romantasy with consequence. Quiet maps.", "always": "the cost, the map, the reread", "register": "low, precise", "palette": "black, oxblood, paper-white", "setting": "one desk lamp, night window"},
    "literary-press": {"age_band": "34-42", "offers": ["night-desk-site", "literary-line", "romantasy-line", "mind-presence-line"], "want": "A press that ships finished work and does not shout.", "taste": "Literary night books, quiet thrillers.", "always": "the desk, finished, the page", "register": "press-adjacent, low", "palette": "charcoal, ink, brass", "setting": "banker lamp, dark shelves"},
    "mind-presence": {"age_band": "28-40", "offers": ["night-desk-site", "mind-presence-line"], "want": "Attention that survives the night.", "taste": "Short chapters. No clinical claims.", "always": "one small attention", "register": "calm, not a coach", "palette": "slate, warm paper", "setting": "bare table, window at 1 a.m."},
    "thriller-night": {"age_band": "30-42", "offers": ["night-desk-site", "literary-line"], "want": "A clock that is fair.", "taste": "Quiet thrillers. No operational how-to.", "always": "the second key", "register": "clipped, nocturnal", "palette": "black, sodium-lamp amber", "setting": "empty newsroom glass, Tampa night"},
    "catalog-host": {"age_band": "30-45", "offers": ["night-desk-site", "the-cartographers-bond", "romantasy-line", "literary-line", "mind-presence-line"], "want": "A catalog a stranger can trust.", "taste": "The whole house, one shelf at a time.", "always": "the catalog, the page", "register": "clear, host-like", "palette": "ink, bone, brass", "setting": "salon table, low light"},
}
BANNED = {"the-lantern-kids", "marlow-and-the-paper-map", "the-tuesday-club", "childrens-youtube-channel"}

def die(msg):
    print("BLOCK:", msg, file=sys.stderr); raise SystemExit(1)

def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    if not s: die("empty slug")
    return s

def today():
    return dt.date.today().isoformat()

def parse_yaml(path):
    data, current = {}, None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if line.strip().startswith("- ") and current and isinstance(data.get(current), list):
            data[current].append(line.strip()[2:].strip().strip('"\''))
            continue
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1); k, v = k.strip(), v.strip().strip('"\'')
            if v in ("", "[]"):
                data[k] = []; current = k
            else:
                data[k] = v; current = None
        elif line.startswith("  - ") and current and isinstance(data.get(current), list):
            data[current].append(line.strip()[2:].strip().strip('"\''))
    return data

def load_products():
    offers, cur = [], None
    for raw in PRODUCTS.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if line.strip().startswith("- slug:"):
            if cur: offers.append(cur)
            cur = {"slug": line.split(":", 1)[1].strip(), "niches": [], "titles": []}
            continue
        if not cur: continue
        m = re.match(r"^\s+(name|type|url|status|collection|fallback):\s*(.*)$", line)
        if m:
            cur[m.group(1)] = m.group(2).strip(); continue
        if line.strip().startswith("niches:"):
            inline = line.split(":", 1)[1].strip()
            if inline.startswith("["):
                cur["niches"] = [x.strip() for x in inline[1:-1].split(",") if x.strip()]
        if line.strip().startswith("- ") and "niches:" not in line and "titles:" not in line:
            item = line.strip()[2:].strip()
            (cur["niches"] if item in NICHES else cur.setdefault("titles", [])).append(item)
    if cur: offers.append(cur)
    return offers

def find_offer(slug):
    for o in load_products():
        if o["slug"] == slug: return o
    die("offer not in products/catalog.yaml: " + slug)

def persona_dirs():
    if not INFLUENCERS.exists(): return []
    return [p for p in sorted(INFLUENCERS.iterdir()) if p.is_dir() and p.name != "_template" and (p / "persona.yaml").exists()]

def load_persona(slug):
    path = INFLUENCERS / slug
    if not (path / "persona.yaml").exists():
        die("no influencer " + slug)
    return path, parse_yaml(path / "persona.yaml")

def cmd_products(_):
    print("HOUSE  Inkbound Night Desk")
    print("SITE   https://inkboundnightdesk.com\n")
    print(f"{'SLUG':28} {'STATUS':10} {'TYPE':12} NAME")
    for o in load_products():
        print(f"{o['slug']:28} {o.get('status','?'):10} {o.get('type','?'):12} {o.get('name','')}")
    print("\nBanned:", ", ".join(sorted(BANNED)))
    print("If status is not live, do not say buy now.")

def cmd_list(_):
    rows = persona_dirs()
    if not rows:
        print('Roster empty. python3 scripts/chief.py new --niche dark-romantasy --name "Mara Vesper"'); return
    print(f"{'SLUG':22} {'NICHE':18} {'STATUS':10} NAME")
    for path in rows:
        d = parse_yaml(path / "persona.yaml")
        print(f"{d.get('slug', path.name):22} {d.get('niche','?'):18} {d.get('status','?'):10} {d.get('name','')}")
    print(f"\n{len(rows)} influencer(s).")

def cmd_show(a):
    path, d = load_persona(a.slug)
    print(f"{d.get('name')}  [{d.get('slug')}]\nniche {d.get('niche')}\nstatus {d.get('status')}\nbio {d.get('disclosure_bio')}\nfolder {path}")

def cmd_new(a):
    if a.niche not in NICHES: die("bad niche")
    name = a.name.strip(); slug = a.slug.strip() if a.slug else slugify(name)
    dest = INFLUENCERS / slug
    if dest.exists() and not a.force: die(str(dest) + " exists")
    spec = NICHES[a.niche]
    dest.mkdir(parents=True, exist_ok=True); (dest / "refs").mkdir(exist_ok=True)
    lines = [f"slug: {slug}", f"name: {name}", f"niche: {a.niche}", "status: draft", f"created: {today()}", f"age_band: {spec['age_band']}", "offers_allowed:"]
    lines += [f"  - {o}" for o in spec["offers"]]
    lines += ['disclosure_bio: "AI persona for Inkbound Night Desk."']
    (dest / "persona.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (dest / "bible.md").write_text(f"# Bible — {name}\n\n## Who they are\nEdit this. Specific. Not loves-books-and-rain.\n\n## Want\n{spec['want']}\n\n## Taste\n{spec['taste']}\n\n## Always says\n- {spec['always']}\n\n## Never says\n- unputdownable\n- is she real though\n\n## How they sell\nThey point. One title per post.\n", encoding="utf-8")
    (dest / "voice.md").write_text(f"# Voice — {name}\n\nRegister: {spec['register']}\nPalette: {spec['palette']}\nCaption: hook / beat / pointer / disclosure\n", encoding="utf-8")
    (dest / "look-brief.md").write_text(f"# Look brief — {name}\n\nAge band {spec['age_band']}. Distinct from every other roster face.\nSetting: {spec['setting']}\nPalette: {spec['palette']}\nHard negatives: no real-person likeness, no celebrity, no readable text, no logos, no extra limbs, no warped hands.\nStills: hero, three-quarter, environment.\n", encoding="utf-8")
    (dest / "platforms.md").write_text(f"# Platforms — {name}\n\nHandles pending. Owner creates accounts.\n", encoding="utf-8")
    HANDOFFS.mkdir(parents=True, exist_ok=True)
    (HANDOFFS / f"{slug}-hero.txt").write_text(f"Cinematic still of {name}, age band {spec['age_band']}. {spec['setting']}. Palette {spec['palette']}. Photorealistic 35mm.\nHard negatives: no real-person likeness, no celebrity, no readable text, no logos, no extra limbs.\n", encoding="utf-8")
    print(f"Created influencers/{slug}/")
    print(f"Next: edit the bible, generate stills into refs/, sign review/persona-gate.md")
    print(f"Then: python3 scripts/chief.py campaign --influencer {slug} --offer {spec['offers'][0]} --days 7")

def week_plan(niche, offer):
    dest = offer.get("url", "https://inkboundnightdesk.com")
    title = offer.get("name", "Inkbound Night Desk")
    live = offer.get("status") == "live"
    pointer = f"The page: {dest}" if live else f"The desk: https://inkboundnightdesk.com  ({title} is not marked live — no buy-now.)"
    disc = "Ad · I am an AI persona for Inkbound Night Desk."
    def P(kind, hook, body):
        return {"kind": kind, "hook": hook, "caption": body + "\n\n" + pointer + "\n\n" + disc}
    tables = {
        "dark-romantasy": [
            P("presence", "The lamp is still on.", "I reread the map pages. Not because I was lost. Because the cost was on the paper."),
            P("taste", "I do not want love that leaves no mark.", "A bond that costs something. That is the whole taste."),
            P("presence", "Ink on the finger. Work.", "If the caption needs a fire emoji it is not my book."),
            P("offer", title + ".", "One image I keep: a chart that behaves like a vow. " + title + " lives at the desk."),
            P("craft", "Reread is a standard.", "I will not call a book finished in a caption if I have not finished it."),
            P("presence", "Night window.", "The press is in Tampa. I am a persona. That is already in the bio."),
            P("offer-soft", "If you want the door.", "House page first. " + title + ". I will not stack seven buy-nows on you."),
        ],
        "literary-press": [
            P("presence", "The desk is open.", "Finished work. No shouting."),
            P("taste", "A catalog a stranger can trust.", "I do not perform volume."),
            P("presence", "Shelves in the dark.", "Readable spines would be a lie in a generated still."),
            P("offer", title + ".", "The desk keeps this page. " + title + "."),
            P("craft", "Signed means a person signed.", "If I cannot point at a gate, I do not say live."),
            P("presence", "Banker lamp.", "I am an AI clerk for the press."),
            P("offer-soft", "The site is the door.", title + ". Page first. Store second."),
        ],
    }
    return tables.get(niche) or [
        P("presence", "One shelf at a time.", "I host the catalog. I do not pretend I found it in the wild."),
        P("taste", "Four collections. Not a pile.", "Named, not dumped."),
        P("presence", "Salon table.", "Family-safe out here. The book page can be darker."),
        P("offer", title + ".", title + " is the stop tonight. House page first."),
        P("craft", "The catalog is a promise.", "I will not list a title I cannot point at."),
        P("presence", "Ink and bone.", "AI persona. Night Desk. Already in the bio."),
        P("offer-soft", "If you want a door.", title + ". Then the rest of the shelf."),
    ]

def cmd_campaign(a):
    path, persona = load_persona(a.influencer)
    if a.offer in BANNED: die("NN-6 banned offer " + a.offer)
    offer = find_offer(a.offer)
    niche = str(persona.get("niche", ""))
    allowed = offer.get("niches") or []
    if allowed and niche not in allowed:
        die("offer does not list niche " + niche)
    days = int(a.days)
    if days < 1 or days > 14: die("days must be 1-14")
    plan = week_plan(niche, offer)[:days]
    folder = CAMPAIGNS / f"{today()}-{a.influencer}-{a.offer}"
    if folder.exists() and not a.force: die(str(folder) + " exists")
    (folder / "posts").mkdir(parents=True, exist_ok=True)
    (folder / "briefs").mkdir(parents=True, exist_ok=True)
    look = (path / "look-brief.md").read_text(encoding="utf-8") if (path / "look-brief.md").exists() else ""
    rows = [f"# Campaign — {persona.get('name')} x {offer.get('name')}", "", f"Offer status: {offer.get('status')}", f"URL: {offer.get('url')}", "", "A slot is a plan. Nothing here is posted.", ""]
    for i, item in enumerate(plan, 1):
        rows.append(f"- Day {i} [{item['kind']}] {item['hook']}")
        (folder / "posts" / f"day-{i:02d}-{item['kind']}.md").write_text(f"# Day {i} — {item['kind']}\n\n**Hook:** {item['hook']}\n\n## Caption\n\n{item['caption']}\n", encoding="utf-8")
        (folder / "briefs" / f"day-{i:02d}.txt").write_text(f"Still for {persona.get('name')}, day {i}, {item['kind']}.\n{item['hook']}\n\n{look}\n\nHard negatives: no real-person likeness, no celebrity, no readable text.\n", encoding="utf-8")
    (folder / "plan.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    (folder / "CHECKLIST.md").write_text("Read posts/. Sign content-gate. Generate stills. You post. Sign publish-gate.\nTHIS SYSTEM DOES NOT LOG IN AND DOES NOT POST.\n", encoding="utf-8")
    print("Wrote", folder)

def cmd_week(a):
    _, persona = load_persona(a.influencer)
    spec = NICHES.get(str(persona.get("niche"))) or NICHES["catalog-host"]
    a.offer = spec["offers"][0]; a.days = 7; a.force = getattr(a, "force", False)
    cmd_campaign(a)

def cmd_log(a):
    AUDIT.mkdir(parents=True, exist_ok=True)
    csv_path = AUDIT / "decisions.csv"
    new = not csv_path.exists()
    if not a.reason.strip(): die("reason required")
    with csv_path.open("a", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        if new: w.writerow(["date", "stage", "decision", "actor", "ref", "reason"])
        w.writerow([dt.datetime.now().isoformat(timespec="seconds"), a.stage, a.decision, a.actor, a.ref, a.reason.strip()])
    print("logged", a.decision, a.stage, a.ref)

def main():
    p = argparse.ArgumentParser(prog="chief.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("products"); sub.add_parser("list")
    s = sub.add_parser("show"); s.add_argument("slug")
    n = sub.add_parser("new"); n.add_argument("--niche", required=True, choices=sorted(NICHES)); n.add_argument("--name", required=True); n.add_argument("--slug", default=""); n.add_argument("--force", action="store_true")
    c = sub.add_parser("campaign"); c.add_argument("--influencer", required=True); c.add_argument("--offer", required=True); c.add_argument("--days", type=int, default=7); c.add_argument("--force", action="store_true")
    w = sub.add_parser("week"); w.add_argument("--influencer", required=True); w.add_argument("--force", action="store_true")
    lg = sub.add_parser("log"); lg.add_argument("--stage", required=True); lg.add_argument("--decision", required=True); lg.add_argument("--reason", required=True); lg.add_argument("--actor", default="grokbot"); lg.add_argument("--ref", default="-")
    args = p.parse_args()
    {"products": cmd_products, "list": cmd_list, "show": cmd_show, "new": cmd_new, "campaign": cmd_campaign, "week": cmd_week, "log": cmd_log}[args.cmd](args)

if __name__ == "__main__":
    main()
