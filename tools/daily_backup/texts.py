"""Writes all text files for the 30-day backup next to the rendered PNGs."""
import json, os, sys
plan, out = sys.argv[1], sys.argv[2]
days = json.load(open(plan))
DAYIDX = {d["date"]: i for i, d in enumerate(days)}
HT = "#GTA6 #GTAVI #GrandTheftAuto #RockstarGames #GTA6News"
DISC = "Independent fan account, not affiliated with Rockstar Games or Take-Two."
SUBS = ["r/GTA6", "r/GTA", "r/gaming"]

def w(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w", encoding="utf-8").write(s.strip() + "\n")

def story_text(i, s):
    if s["type"] == "countdown": return f"{s['big']} {s['sub']}. {s['head']}: {s['detail']}. Source: {s['source']}."
    if s["type"] == "quiz": return f"QUIZ: {s['q']} " + " / ".join(f"{chr(65+k)}. {o}" for k, o in enumerate(s['opts'])) + f"  (correct: {s['opts'][s['answer']]})"
    if s["type"] == "poll": return f"POLL: {s['q']} {s['opts'][0]} vs {s['opts'][1]}"
    if s["type"] == "card": return f"{s['kind']}: {s['head']} – {s['detail']} (OFFICIAL · Rockstar)"
    if s["type"] == "promo": return f"PROMO: {s['head']} – {s['detail']} + FOLLOW @gta6_intelligence"
    return f"QUESTION: {s['q']}"

index = ["# DAILY CONTENT INDEX – GTA 6 Intelligence", "", "Každá složka DAILY_CONTENT_BACKUP/<datum> obsahuje vše k ručnímu zveřejnění. TIME-SENSITIVE = před zveřejněním ověřit Rockstar Newswire.", "",
         "| Datum | Instagram Stories | TikTok | YouTube | Ostatní sítě | Stav |", "|---|---|---|---|---|---|"]
for d in days:
    D = os.path.join(out, d["date"]); st = d["stories"]; yt = d["youtube"]
    s1, s3, poll, s4, promo = st[0], st[2], st[3], st[4], st[5]
    # ---------------- INSTAGRAM ----------------
    cap = [f"INSTAGRAM – {d['date']}", ""]
    for i, s in enumerate(st, 1):
        cap += [f"STORY_0{i}.png · post at {s['time']} CET", f"  Content: {story_text(i, s)}", f"  Interaction: {s['note']}", ""]
    if d.get("ig_feed"):
        cap += ["FEED: " + d["ig_feed"]]
    else:
        cap += ["FEED (optional, 12:00): post STORY_03.png as a 4:5 feed image (crop to 4:5 in the app).",
                f"  Caption: {s3['head'].title()} – {s3['detail']}. Officially shown by Rockstar Games. {s4['q']} Comment below 👇 Follow @gta6_intelligence for fact-checked GTA 6 news daily. {DISC} {HT}"]
    w(os.path.join(D, "INSTAGRAM", "CAPTIONS.txt"), "\n".join(cap))
    w(os.path.join(D, "INSTAGRAM", "PUBLISHING_GUIDE.txt"), f"""
HOW TO POST THESE STORIES MANUALLY (Instagram app, account @gta6_intelligence)
1. Check you are logged in as gta6_intelligence (NOT a personal account).
2. Tap + → Story → pick STORY_0X.png (6 per day, order in DAILY_CHECKLIST.txt) from this folder (save to phone via OneDrive app first).
3. Add the interactive sticker described in CAPTIONS.txt (Quiz / Poll / Questions) over the option area.
4. STORY_01 is TIME-SENSITIVE: open https://www.rockstargames.com/newswire first. If Rockstar announced something new, post that instead.
5. Post at the times in CAPTIONS.txt (CET). Don't post all 4 at once.
6. After posting, tick DAILY_CHECKLIST.txt and move used files to READY_TO_PUBLISH → PUBLISHED if you track them.
7. Add to Highlights: NEWS/COUNTDOWN (01), CONFIRMED or MAPS (03), COMMUNITY (02, 04, 05).
""")
    # ---------------- TIKTOK ----------------
    if d.get("tiktok"):
        tt = f"TIKTOK – {d['date']}\nSTATUS: {d['tiktok']}\nNothing to do except check it went public in TikTok Studio → Obsah."
    else:
        tt = f"""TIKTOK – {d['date']} · PHOTO POST (post 18:00 CET)
Photos (in this order): ../INSTAGRAM/STORY_03.png, ../INSTAGRAM/STORY_01.png, ../INSTAGRAM/STORY_04.png
Title (max 90): {s3['head'].title()}: what Rockstar confirmed
Description: {s3['head'].title()} – {s3['detail']}. {s1['head']}: {s1['detail']}. {s4['q']} Comment 👇 Follow for fact-checked GTA 6 news. {DISC} #gta6 #gtavi #grandtheftauto #rockstargames #gaming
How: tiktok.com/tiktokstudio/upload → Fotky → upload → paste texts → Zveřejnit (or Plán).
Optional sound: add a trending sound from TikTok's library in the app."""
    w(os.path.join(D, "TIKTOK", "TIKTOK_POST.txt"), tt)
    # ---------------- YOUTUBE ----------------
    if "link" in yt:
        ytt = f"YOUTUBE SHORT – {d['date']} {yt['time']} CET\nSTATUS: {yt['status']}\nTitle: {yt['title']}\nLink/file: {yt['link']}\nThumbnail: THUMBNAIL.png (reference; Shorts covers are chosen from a frame in the YouTube app)."
    else:
        ytt = f"""YOUTUBE SHORT – {d['date']} {yt['time']} CET
STATUS: {yt['status']}
Title: {yt['title']}
Script (voice-over lines, ~20–30 s):
""" + "\n".join(f"  {i+1}. {l}" for i, l in enumerate(yt["script"])) + f"""
Description: {' '.join(yt['script'])} Source: Rockstar Games official media. Footage: Rockstar Games (official media kit). {DISC} {HT}
Thumbnail/cover: THUMBNAIL.png
Production: new folder in 02_GTA6_INTELLIGENCE/project_files with vo_lines.json + shots.json (official screenshots in ASSETS/IMAGES/official) → python3 04_SHARED_TOOLS/gta_build.py <dir> all
Fallback without video: post THUMBNAIL.png + script as a YouTube Community post (once the channel is verified)."""
    w(os.path.join(D, "YOUTUBE", "SHORT.txt"), ytt)
    # ---------------- FACEBOOK / THREADS / X / REDDIT ----------------
    w(os.path.join(D, "FACEBOOK", "FACEBOOK_POST.txt"), f"""FACEBOOK PAGE – {d['date']} (post 13:00 CET) · NEEDS: Facebook Page "GTA 6 Intelligence" (not created yet; never post on the personal profile)
Image: ../INSTAGRAM/STORY_03.png
Text: {s3['head'].title()} – {s3['detail']}. This is officially shown by Rockstar Games, no rumours. {s4['q']} Tell us in the comments 👇
{s1['big']} {s1['sub'].lower()}: {s1['head']} ({s1['detail']}).
{DISC} {HT}""")
    w(os.path.join(D, "THREADS", "THREADS_POST.txt"), f"""THREADS – {d['date']} · NEEDS: Threads profile (threads.com → "Use Instagram account")
Post 1 (09:30): {s1['big']} {s1['sub'].lower()}. Verified: {s1['head']} – {s1['detail']}. Source: {s1['source']}.
Post 2 (15:00, attach ../INSTAGRAM/STORY_03.png): {s3['head'].title()}: {s3['detail']}. [OFFICIAL]
Post 3 (20:30, native poll): {poll['q']} {' / '.join(poll['opts'])}""")
    w(os.path.join(D, "X", "X_POST.txt"), f"""X (TWITTER) – {d['date']} · NEEDS: X account for the brand
Tweet 1 (09:30): [OFFICIAL] {s1['head']} – {s1['detail']}. {s1['big']} {s1['sub'].lower()}. #GTA6
Tweet 2 (16:00, image ../INSTAGRAM/STORY_03.png): {s3['head'].title()}: {s3['detail']}. Confirmed by Rockstar. #GTA6 #GTAVI
Tweet 3 (20:00, native poll): {poll['q']}  Options: {' / '.join(poll['opts'])}""")
    w(os.path.join(D, "REDDIT", "REDDIT_POST.txt"), f"""REDDIT – {d['date']} · NEEDS: Reddit account with some karma. READ EACH SUB'S RULES FIRST.
Suggested sub: {SUBS[0]} (discussion flair). Most GTA subs ban self-promotion: NO links to our profiles, NO watermark promo.
Title: {s4['q']}
Body: Discussion question for today. For context, here's what Rockstar has officially confirmed so far: {s1['head']} ({s1['detail']}); {s3['head'].title()} ({s3['detail']}). What's your take?
Alternative: answer existing threads with sourced facts (link Rockstar Newswire, not us).""")
    # ---------------- ENGAGEMENT ENGINE ----------------
    k = DAYIDX[d["date"]]
    LIKE = ["Like if you're excited for GTA 6!", "Drop a like if you want more GTA 6 updates.", "Double tap if Vice City is your dream location.", "Like if you're counting down with us."]
    COMM = ["What do you think?", "Which location would you visit first?", "Tell us your theory in the comments.", "Agree or disagree?", "What should we investigate next?"]
    SHARE = ["Send this to your GTA friend.", "Share this with someone waiting for GTA 6.", "Tag a friend who needs to see this."]
    SAVE = ["Save this guide for later.", "Save this map before GTA 6 launches.", "Keep this for your next GTA session."]
    FOLLOW = ["Follow GTA 6 Intelligence for daily updates.", "Follow so you don't miss the next reveal.", "More GTA 6 investigations coming tomorrow."]
    pick = lambda a, o=0: a[(k + o) % len(a)]
    w(os.path.join(D, "CTA_CAPTIONS.txt"), f"""CTA CAPTIONS – {d['date']}  (goal of the day: {['COMMENTS','SAVES','SHARES','FOLLOWS'][k % 4]})
INSTAGRAM FEED/CAROUSEL: {pick(SAVE)} {pick(COMM, 1)} {pick(FOLLOW)}
INSTAGRAM STORIES: vote in the poll · answer the quiz · reply to the question box · tap the link sticker
TIKTOK PHOTO/VIDEO: {pick(COMM)} {pick(SHARE)} {pick(FOLLOW, 1)}  → reply to the best comment with a NEW video/photo post ("Replying to @user")
YOUTUBE SHORT: {pick(LIKE)} Comment: {s4['q']} Subscribe for the next part of the series.
FACEBOOK: {pick(COMM, 2)} {pick(SHARE, 1)}
THREADS: {s4['q']} (reply chain) · {pick(SHARE, 2)}
X: {pick(COMM, 3)} Retweet if you agree.
REDDIT: no CTA to follow/like (against most subs' rules) – end the post with a genuine discussion question: {s4['q']}
Rotate: don't reuse yesterday's lines. Every post states ONE main action we want.""")
    w(os.path.join(D, "STORY_INTERACTIONS.txt"), f"""STORY INTERACTIONS – {d['date']} (stickers only in the Instagram app; web = post image + ask for DM replies)
STORY_02 QUIZ ({st[1]['time']}): Question: "{st[1]['q']}"  Options: {' / '.join(st[1]['opts'])}  Correct: {st[1]['opts'][st[1]['answer']]}
   How: Sticker → QUIZ → type the question + options → mark the correct one → place over the option boxes.
STORY_04 POLL ({poll['time']}): "{poll['q']}"  Options: {poll['opts'][0]} / {poll['opts'][1]}
   How: Sticker → POLL → type options exactly → place over the two boxes.
STORY_05 QUESTION BOX ({s4['time']}): "{s4['q']}"
   How: Sticker → QUESTIONS → paste the question. Tomorrow reshare 2–3 best answers (credit the user, ask permission for DMs).
   Same story: add text "Quiz answer: {st[1]['opts'][st[1]['answer']]} ✅".
STORY_06 PROMO ({promo['time']}): {promo['head']} – {promo['detail']}
   How: Sticker → LINK → link to the new post/Short; add MENTION @gta6_intelligence.
STORY_01 / STORY_03: add EMOJI SLIDER "🔥 hype level" (optional).""")
    w(os.path.join(D, "COMMENT_REPLIES.txt"), f"""COMMENT REPLIES – {d['date']} (reply as GTA 6 Intelligence, natural English, max 1–2 sentences, no copy-paste spam)
• Agreement: "Same here! Which part of {s3['head'].title()} are you most curious about?"
• Disagreement / criticism: "Fair point, thanks for calling it out. Here's what Rockstar has confirmed so far: {s1['head']} ({s1['detail']}). Anything we missed?"
• Rumour asked as fact: "We only label things OFFICIAL when Rockstar confirms them. Right now that one's a RUMOUR, we'll update you if that changes."
• Question we can answer: answer with the fact + source (e.g. "{s1['head']}: {s1['detail']}, source: {s1['source']}.") + "Want a full breakdown post?"
• Question we can't answer: "Rockstar hasn't said yet. We'll post as soon as it's official. Follow so you don't miss it."
• Great idea for content: "Love this, we're making a post about it. 🔥" → add to NEXT IDEAS and make a reply-video/photo on TikTok.
• Hate/spam: don't argue; hide/report per platform rules.
NEVER: fake accounts, bought comments, auto-generated fake replies.""")
    w(os.path.join(D, "ENGAGEMENT_STRATEGY.txt"), f"""ENGAGEMENT STRATEGY – {d['date']}
Main goal today: {['COMMENTS','SAVES','SHARES','FOLLOWS'][k % 4]}
Per post – the ONE reaction we want:
- IG Story 01 (news): profile visit / emoji slider
- IG Story 02 (quiz): quiz answers
- IG Story 03 (card): SAVE + share to friends
- IG Story 04 (poll): votes
- IG Story 05 (question): question-box replies (→ tomorrow's content)
- IG Story 06 (promo): link taps + follows
- TikTok: comments (opinion) + shares
- YouTube Short: comments + subscribe
- FB/Threads/X: replies in the thread; Reddit: genuine discussion
Track (log in ANALYTICS/post_metrics.csv): comments/1k views, shares/1k, saves/1k, like rate, new followers per post, story replies & votes.
Reply window: check comments at 12:00, 18:00, 21:00. Reply to every genuine comment in the first 2 hours.
Weekly (Sunday): compare CTA variants, keep the top 2 per platform.""")
    # ---------------- CHECKLIST ----------------
    w(os.path.join(D, "DAILY_CHECKLIST.txt"), f"""DAILY CHECKLIST – {d['date']}  (T-minus: {d['tminus']} days to launch)
[ ] 09:00 Story 1 (STORY_01.png) – NEWS/COUNTDOWN · TIME-SENSITIVE, check Rockstar Newswire first
[ ] 12:30 Story 2 (STORY_02.png) – QUIZ sticker
[ ] 13:30 Story 3 (STORY_03.png) – CONFIRMED / MAP card (save CTA)
[ ] 14:30 Story 4 (STORY_04.png) – POLL sticker
[ ] 16:45 Story 5 (STORY_06.png) – PROMO + link sticker
[ ] 20:00 Story 6 (STORY_05.png) – QUESTIONS sticker + quiz answer reveal
[ ] Replied to new comments on IG / TikTok / YouTube (see COMMENT_REPLIES.txt)
[ ] Instagram Feed checked ({'planned: ' + d['ig_feed'] if d.get('ig_feed') else 'optional feed post in CAPTIONS.txt'})
[ ] TikTok checked ({d['tiktok'] or 'photo post 18:00, see TIKTOK_POST.txt'})
[ ] YouTube checked ({yt['status']})
[ ] Facebook checked (needs Page)
[ ] Threads checked (needs profile)
[ ] X checked (needs account)
[ ] Reddit checked (rules first, no self-promo)
Links published today:
-
""")
    oth = "texty FB/Threads/X/Reddit"
    stav = "TIME-SENSITIVE story 1" + (" · YT naplánováno" if "link" in yt and yt["status"] == "SCHEDULED" else "")
    index.append(f"| {d['date']} | 6× PNG + popisky + engagement | {d['tiktok'] or 'foto post (texty)'} | {yt['status'].split(' –')[0]}: {yt['title'].split(' #')[0]} | {oth} | {stav} |")

w(os.path.join(out, "..", "DAILY_CONTENT_INDEX.md"), "\n".join(index))
w(os.path.join(out, "..", "CONTENT_TEMPLATES", "README.txt"), """CONTENT TEMPLATES
- Story generator (cloud): 04_SHARED_TOOLS/daily_backup/ (content_bank.py → plan.json → render.js PNG → texts.py)
- In-page generators (IG/TikTok web): 04_SHARED_TOOLS/motion/gta_carousels_inpage.js, gta_brand_inpage.js
- Highlight covers: CONTENT_TEMPLATES/HIGHLIGHT_COVERS/*.png (set in the Instagram app: Highlight → Edit → Edit cover)
- Rules: only verified facts (2 sources), label OFFICIAL / REPORTED / RUMOUR, never present old news as new.""")
w(os.path.join(out, "..", "READY_TO_PUBLISH", "README.txt"), "Move files here when you decide to post them today. Then move to PUBLISHED after posting.")
w(os.path.join(out, "..", "PUBLISHED", "README.txt"), "Posted content archive. Add the public link to 02_GTA6_INTELLIGENCE/ANALYTICS/post_metrics.csv.")
print("texts ok")
