"""GTA 6 Intelligence – 30-day offline content bank (verified facts only).
Builds plan.json: per day 4 stories + texts for TikTok / YouTube / IG feed / Facebook / Threads / X / Reddit.
Every fact here was verified from Rockstar/Take-Two via >=2 outlets (see 02_GTA6_INTELLIGENCE/SOURCES.md, VERIFICATION_RULES.md).
"""
import json, datetime as dt, sys

START = dt.date(2026, 11, 6); DAYS = 30; LAUNCH = dt.date(2026, 11, 19)

# ---------- verified fact bank ----------
FACTS = [  # (headline, detail, source)
    ("LAUNCH: NOV 19, 2026", "PS5 + Xbox Series X|S", "Rockstar / Take-Two"),
    ("PRE-LOAD: NOV 10", "PS5 at midnight local time · Xbox at 00:00 GMT", "Rockstar Newswire"),
    ("UP TO 212 GB", "Make room before pre-load day", "Rockstar Pre-Load FAQ"),
    ("$79.99 / $99.99", "Standard / Ultimate · US prices", "Rockstar via Shacknews, Windows Central"),
    ("NO DISC", "The physical box contains a download code", "Rockstar via Shacknews, Windows Central"),
    ("SCORE BY JUSTICE", "An adaptive score that shifts with how you play", "Rockstar Newswire (Oct 29)"),
    ("SCORE ALBUM: DEC 11", "30 tracks from the original score", "Rockstar Newswire (Oct 29)"),
    ("WELCOME TO LEONIDA", "The state where GTA 6 is set", "Rockstar Games"),
    ("JASON & LUCIA", "The two lead characters", "Rockstar Games"),
    ("PRE-ORDER BONUS", "Vintage Vice City Pack · digital pre-orders before Nov 20", "Rockstar pre-order announcement"),
    ("2 MOD SHOPS", "Rideout Customs + One-Eyed Willie's (Ultimate Edition)", "Rockstar via Shacknews, Windows Central"),
    ("TAME IMPALA · SZA", "+ King Gizzard & The Lizard Wizard on the score album", "Rockstar Newswire (Oct 29)"),
    ("\"PUSHER\"", "New single with Gesaffelstein", "Rockstar Newswire (Oct 29)"),
    ("PC: NOT ANNOUNCED", "Take-Two: consoles first. No PC date yet", "Take-Two (May 2026)"),
    ("6 PLACES SHOWN", "Vice City · Keys · Grassrivers · Port Gellhorn · Ambrosia · Kalaga", "Rockstar Games"),
]
PLACES = [("VICE CITY", "Neon, beaches and the skyline"), ("LEONIDA KEYS", "Islands, boats and open water"),
          ("GRASSRIVERS", "Swamps, airboats and gators"), ("PORT GELLHORN", "Motels and late nights"),
          ("AMBROSIA", "Bikers and industry"), ("MOUNT KALAGA", "National park: forests, rivers and trails")]
CHARS = [("JASON DUVAL", "Ex-Army, running jobs for smugglers in the Keys"), ("LUCIA CAMINOS", "Fresh out of the Leonida Penitentiary"),
         ("CAL HAMPTON", "Jason's friend: conspiracy theories and Coast Guard radio"), ("BOOBIE IKE", "Vice City legend: real estate, a club, a studio"),
         ("DRE'QUAN PRIEST", "Hustler turned music boss at Only Raw Records"), ("REAL DIMEZ", "Viral rap duo signed to Only Raw"),
         ("RAUL BAUTISTA", "Seasoned bank robber, always recruiting"), ("BRIAN HEDER", "Old-school smuggler and Jason's landlord")]
EXTRA = [("ULTIMATE EDITION", "Adds 2 mod shops + extra clothing, hair & tattoo stores (story mode)"),
         ("VINTAGE VICE CITY PACK", "'55 Vapid Stanier, vintage outfits, palm-tree weapon pattern"),
         ("ADAPTIVE SCORE", "Justice's music reacts to how you play")]
CARDS = [("PLACE", *p) for p in PLACES] + [("CHARACTER", *c) for c in CHARS] + [("CONFIRMED", *e) for e in EXTRA]  # 17

# ---------- quizzes (verified answers) and polls (opinion) ----------
QUIZ = [
    ("Who composed GTA 6's original score?", ["Justice", "Daft Punk", "Hans Zimmer"], 0),
    ("What's the max GTA 6 download size?", ["150 GB", "212 GB", "300 GB"], 1),
    ("In which state is GTA 6 set?", ["San Andreas", "Leonida", "Liberty"], 1),
    ("When does GTA 6 launch?", ["Nov 19, 2026", "Oct 26, 2026", "Dec 3, 2026"], 0),
    ("Ultimate Edition US price?", ["$89.99", "$99.99", "$119.99"], 1),
    ("Which record label do Real Dimez sign to?", ["Only Raw", "Death Row", "Vice Records"], 0),
    ("Where was Lucia before the story starts?", ["The Army", "Leonida Penitentiary", "Liberty City"], 1),
    ("Which car is in the Vintage Vice City Pack?", ["'55 Vapid Stanier", "'82 Infernus", "'90 Banshee"], 0),
    ("Who is Jason's landlord?", ["Brian Heder", "Cal Hampton", "Raul Bautista"], 0),
    ("What does the physical box contain?", ["A disc", "A download code", "Nothing"], 1),
    ("Which artist is on the new single 'Pusher'?", ["Gesaffelstein", "The Weeknd", "Skrillex"], 0),
    ("How many tracks on the score album?", ["12", "30", "50"], 1),
    ("Which place is a national park?", ["Ambrosia", "Mount Kalaga", "Port Gellhorn"], 1),
    ("Jason used to be in…", ["The Army", "The police", "A band"], 0),
]
POLL = [
    ("Pre-load ready?", ["READY", "NOT YET"]), ("Taking launch day off?", ["YES", "NO"]),
    ("Jason or Lucia?", ["JASON", "LUCIA"]), ("Standard or Ultimate?", ["STANDARD", "ULTIMATE"]),
    ("PS5 or Xbox?", ["PS5", "XBOX"]), ("Day-one player?", ["YES", "LATER"]),
    ("First stop in Leonida?", ["VICE CITY", "THE KEYS"]), ("Story first or explore first?", ["STORY", "EXPLORE"]),
    ("Car or boat?", ["CAR", "BOAT"]), ("Radio on or off?", ["ON", "OFF"]),
    ("Grassrivers or Mount Kalaga?", ["GRASSRIVERS", "KALAGA"]), ("Night or day driving?", ["NIGHT", "DAY"]),
    ("Favourite side character?", ["CAL", "BOOBIE"]), ("Best GTA hero ever?", ["TOMMY", "CJ"]),
    ("Solo heists or crew heists?", ["SOLO", "CREW"]),
]
QUESTIONS = [
    "What's the first thing you'll do in GTA 6?", "Which GTA 6 trailer moment lives in your head?", "What GTA 6 rumour do you want to be TRUE?",
    "Which old GTA city should get a cameo?", "Name your dream GTA 6 radio station.", "What car are you buying first?",
    "Which character do you trust least?", "What's your GTA 6 launch-night snack?", "How many hours on day one?",
    "Best GTA soundtrack moment ever?", "What would make GTA 6 a 10/10 for you?", "Which Leonida place looks most fun?",
    "Your GTA 6 hot take?", "What did GTA 5 do better than any game?", "Who are you playing GTA 6 with?",
    "What's one GTA rule you always break?", "Favourite GTA protagonist so far?", "Which mission type do you hope to see?",
    "What should we fact-check next?", "Describe GTA 6 in 3 words.", "What's your ideal first heist target?",
    "Which side activity are you most hyped for?", "Pick your Leonida home base.", "What GTA 6 detail did you spot first?",
    "How did you find this page?", "What would you name your boat?", "Which GTA game got you into the series?",
    "What are you most worried about in GTA 6?", "One word for Vice City.", "What should our next carousel be about?",
]

# already-planned items (keep, don't duplicate)
YT_PLANNED = {
    "2026-11-07": ("SCHEDULED", "GTA 6 isn't just Vice City: 6 places in Leonida #GTA6 #Shorts", "https://youtube.com/shorts/cMwq_nuYows", "17:00"),
    "2026-11-08": ("SCHEDULED", "Rockstar got a Grammy-winning duo to score GTA 6 #GTA6 #Shorts", "https://youtube.com/shorts/RRcFcIbUmOM", "17:00"),
    "2026-11-09": ("SCHEDULED", "GTA 6 pre-load starts TONIGHT: exact times (PS5 & Xbox) #GTA6 #Shorts", "https://youtube.com/shorts/uYpJROwVX4A", "17:00"),
    "2026-11-10": ("SCHEDULED", "GTA 6 needs up to 212 GB: free up space in 3 steps #GTA6 #Shorts", "https://youtube.com/shorts/DDqBt58wNLQ", "12:00"),
    "2026-11-11": ("SCHEDULED", "This GTA 6 bonus expires after Nov 19: what's inside #GTA6 #Shorts", "https://youtube.com/shorts/R2jJO_HWQWA", "17:00"),
    "2026-11-12": ("READY – upload blocked until channel verification", "GTA 6 on PC at launch? True or false – 3 claims fact-checked #GTA6 #Shorts", "PUBLISH/gta_009_true_or_false_YT_IG.mp4", "17:00"),
    "2026-11-13": ("READY – upload blocked until channel verification", "GTA 6 Ultimate Edition: what does +$20 actually get you? #GTA6 #Shorts", "PUBLISH/gta_010_ultimate_worth_it_YT_IG.mp4", "17:00"),
}
TT_PLANNED = {"2026-11-06": "PUBLISHED 09:45 – OFFICIAL vs RUMOUR photo post", "2026-11-07": "SCHEDULED 18:00 – Leonida 6 places (photo)",
              "2026-11-08": "SCHEDULED 18:00 – Editions & prices (photo)", "2026-11-09": "SCHEDULED 18:00 – 5 things Rockstar confirmed (photo)"}
IG_FEED = {"2026-11-06": "PUBLISHED – OFFICIAL vs RUMOUR carousel https://www.instagram.com/p/DfZNHT4kVsL/",
           "2026-11-07": "Carousel: Leonida 6 places (generator set 'leonida')", "2026-11-08": "Carousel: Editions & prices (set 'editions')",
           "2026-11-09": "Carousel: 5 things Rockstar confirmed (set 'top5')"}
SHORT_IDEAS = [  # evergreen Short scripts for days without a produced video (need production with gta_build.py)
    ("Meet Cal Hampton: Jason's conspiracy-theory friend", ["Cal Hampton is Jason's friend.", "Beers, conspiracy theories and Coast Guard radio.", "Rockstar confirmed him as one of 8 main faces.", "Is Cal the funniest character? Comment."]),
    ("Who is Boobie Ike? The Vice City legend explained", ["Boobie Ike is a Vice City legend.", "Real estate, a club and a recording studio.", "One of 8 main faces Rockstar revealed.", "Hustler or mogul? Comment."]),
    ("Grassrivers: GTA 6's swamp region", ["Grassrivers: swamps, airboats and gators.", "One of six places Rockstar showed in Leonida.", "Would you explore it first? Comment."]),
    ("Mount Kalaga National Park in GTA 6", ["Mount Kalaga is a national park.", "Forests, rivers and trails.", "Off-road or hiking? Comment."]),
    ("Port Gellhorn: motels and late nights", ["Port Gellhorn: motels and late nights.", "One of six places in Leonida.", "Would you live here? Comment."]),
    ("Ambrosia: bikers and industry", ["Ambrosia: bikers and industry.", "Shown by Rockstar as part of Leonida.", "Biker gang or not? Comment."]),
    ("Real Dimez: GTA 6's viral rap duo", ["Real Dimez are a viral rap duo.", "Signed to Only Raw Records.", "Chasing one more hit.", "Would you stream them? Comment."]),
    ("Raul Bautista: the bank robber recruiting talent", ["Raul Bautista is a seasoned bank robber.", "Always recruiting new talent.", "Would you join his crew? Comment."]),
    ("Brian Heder: Jason's smuggler landlord", ["Brian Heder: an old-school smuggler from the Keys.", "He's also Jason's landlord.", "Trust him? Comment."]),
    ("Dre'Quan Priest and Only Raw Records", ["Dre'Quan Priest went from hustler to music boss.", "He runs Only Raw Records.", "Best music storyline yet? Comment."]),
    ("GTA 6 score album: what we know", ["Justice composed GTA 6's adaptive score.", "The 30-track album lands December 11.", "Features Tame Impala, SZA and King Gizzard.", "Would you buy it? Comment."]),
    ("Leonida Keys: islands and open water", ["Leonida Keys: islands, boats and open water.", "Jason runs jobs for smugglers here.", "Boat life? Comment."]),
]


def build():
    days = []
    qi = pi = ci = fi = si = 0
    for d in range(DAYS):
        date = START + dt.timedelta(days=d); ds = date.isoformat(); tminus = (LAUNCH - date).days
        # ---- story 1: news / countdown (time-sensitive) ----
        EXP = {1: dt.date(2026, 11, 10), 2: dt.date(2026, 11, 19), 9: dt.date(2026, 11, 19), 0: dt.date(2026, 11, 19)}  # fact index -> last valid day
        EVERGREEN = [5, 7, 8, 10, 11, 12, 13, 14, 4, 3]
        pool = [i for i in range(len(FACTS)) if date <= EXP.get(i, date)] if tminus > 0 else EVERGREEN
        f = FACTS[pool[fi % len(pool)]]; fi += 1
        if tminus > 0: s1 = {"type": "countdown", "big": f"T-{tminus}", "sub": "DAYS UNTIL GTA 6" if tminus > 1 else "DAY UNTIL GTA 6", "head": f[0], "detail": f[1], "source": f[2]}
        elif tminus == 0: s1 = {"type": "countdown", "big": "TODAY", "sub": "GTA 6 LAUNCH DAY", "head": "PS5 + XBOX SERIES X|S", "detail": "Check Rockstar Newswire for live updates", "source": "Rockstar Games"}
        else: s1 = {"type": "countdown", "big": f"DAY {-tminus + 1}", "sub": "OF GTA 6", "head": f[0], "detail": f[1], "source": f[2]}
        if ds == "2026-11-10": s1.update(head="PRE-LOAD DAY", detail="Up to 212 GB · PS5 midnight local · Xbox 00:00 GMT", source="Rockstar Newswire")
        s1["time"] = "09:00"; s1["note"] = "TIME-SENSITIVE: check Rockstar Newswire for new announcements before posting. Fact line is verified."
        # ---- story 2: quiz (every day) ----
        q = QUIZ[qi % len(QUIZ)]; qi += 1
        s2 = {"type": "quiz", "q": q[0], "opts": q[1], "answer": q[2], "time": "12:30",
              "note": f"App: add QUIZ sticker over the options, correct = {q[1][q[2]]}. Web: post as is, reveal the answer in the 20:00 story."}
        # ---- story 3: confirmed card (place / character / edition) ----
        c = CARDS[ci % len(CARDS)]; ci += 1
        s3 = {"type": "card", "kind": c[0], "head": c[1], "detail": c[2], "time": "16:30", "note": "Verified (Rockstar Games). Link sticker to latest post in the app if available."}
        # ---- story 4: poll, story 5: open question, story 6: promo / follow ----
        p = POLL[pi % len(POLL)]; pi += 1
        s4 = {"type": "poll", "q": p[0], "opts": p[1], "time": "14:30", "note": "App: add POLL sticker over the two options. Web: ask to reply via DM."}
        s5 = {"type": "question", "q": QUESTIONS[d % len(QUESTIONS)], "time": "20:00", "note": "App: add QUESTIONS sticker. Reshare the best answers tomorrow (credit the user)."}
        if ds in YT_PLANNED: promo = f"NEW SHORT TODAY {YT_PLANNED[ds][3]}", YT_PLANNED[ds][1].split(" #")[0]
        elif TT_PLANNED.get(ds, "").startswith("SCHEDULED"): promo = "NEW ON TIKTOK 18:00", TT_PLANNED[ds].split("– ")[-1]
        else: promo = "NEW POST TODAY", "Fresh fact-checked GTA 6 drop on our feed"
        s6 = {"type": "promo", "head": promo[0], "detail": promo[1], "time": "16:45", "note": "App: add LINK sticker to the new post/Short if available + MENTION @gta6_intelligence. Goal: follows + profile visits."}
        # ---- YouTube ----
        if ds in YT_PLANNED:
            st, title, link, tm = YT_PLANNED[ds]; yt = {"status": st, "title": title, "link": link, "time": tm}
        else:
            idea = SHORT_IDEAS[si % len(SHORT_IDEAS)]; si += 1
            yt = {"status": "SCRIPT READY – needs production (04_SHARED_TOOLS/gta_build.py) + upload", "title": idea[0] + " #GTA6 #Shorts", "script": idea[1], "time": "17:00"}
        days.append({"date": ds, "tminus": tminus, "stories": [s1, s2, s3, s4, s5, s6], "youtube": yt,
                     "tiktok": TT_PLANNED.get(ds), "ig_feed": IG_FEED.get(ds)})
    return days


if __name__ == "__main__":
    json.dump(build(), open(sys.argv[1], "w"), indent=1, ensure_ascii=False); print("ok")
