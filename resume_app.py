"""
# AN6100 Programming Essential 
# Assignment & Presentation Part 1 ——streamlit resume app
# 2026

# Class Number             :Section B
# Name                     :Xu Jie                     
# Presentation Video link  :https://www.dropbox.com/scl/fi/nu4v98gjgoao42kcceb4t/SB_Xu_Jie.mp4?rlkey=dqbxyini89w78gf83qezs5jct&st=9p7yv226&dl=0
"""

from pathlib import Path

import streamlit as st
# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------
SECTION_TOTAL = 5
MODES = ["Full story", "Quick scan"]

INK = "#1a1a2e"
CORAL = "#f2542d"
TEAL = "#0b6e77"
PEACH = "#ffb199"
YELLOW = "#ffd23f"
INDIGO = "#35365f"

SECTION_COLORS = [(CORAL, "#ffffff"), (TEAL, "#ffffff"), (PEACH, INK), (YELLOW, INK), (INDIGO, "#ffffff")]

CARD_COLORS = ["coral", "teal", "yellow", "indigo"]

CARD_PILLS = [(CORAL, "#ffffff"), (TEAL, "#ffffff"), (YELLOW, INK), (INDIGO, "#ffffff")]

CARD_TINTS = [PEACH, "#a8dcd9", "#ffe58a", "#c9c9ea"]

PAGE_CSS = """<style>
.block-container{max-width:1100px;padding-top:4.6rem;padding-bottom:4rem;}
[data-testid="stHeader"]{border-top:6px solid;border-image:linear-gradient(90deg,#f2542d,#ffd23f,#0b6e77,#35365f) 1;}
[data-testid="stMain"] hr{border:none !important;height:4px;border-radius:4px;background:ACCENT;opacity:1;}
[data-testid="stSidebar"]{background:#35365f;border-right:3px solid #1a1a2e;}
[data-testid="stSidebar"] h1{color:#ffd23f;font-weight:800;}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p{color:#d9d6ee;}
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p{color:#ffd23f;font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.78rem;}
[data-testid="stSidebar"] [data-testid="stRadio"] label p{color:#fbf6ec;}
[data-testid="stSidebar"] [data-testid="stProgress"] p{color:#fbf6ec;}
[data-testid="stSidebar"] hr{border-color:rgba(251,246,236,.25);}
[data-testid="stImage"] img{border-radius:20px;border:3px solid #1a1a2e;box-shadow:8px 8px 0 #f2542d;}
.heroname{font-size:4.2rem;font-weight:800;line-height:1.05;color:#1a1a2e;display:inline-block;background:linear-gradient(transparent 62%,#ffd23f 62%);}
.herorole{font-size:1.7rem;font-weight:700;color:#0b6e77;margin:.4rem 0 .8rem 0;}
.sectionband{background:ACCENT;color:BANDTEXT;border:2px solid #1a1a2e;border-radius:18px;box-shadow:6px 6px 0 #1a1a2e;padding:1.1rem 1.5rem 1.2rem 1.5rem;margin:.2rem 0 1.6rem 0;}
.sectionband .kicker{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.72rem;letter-spacing:.08em;font-weight:700;opacity:.9;}
.sectionband .headline{font-size:2.3rem;font-weight:800;line-height:1.15;margin:.35rem 0 0 0;}
.sectionband .blurb{font-size:1.02rem;margin:.55rem 0 0 0;}
[class*="st-key-card_"] [data-testid="stExpander"] details{border:1.5px solid #1a1a2e;border-radius:12px;background:#ffffff;}
[class*="st-key-card_"] [data-testid="stExpander"] summary{font-weight:700;color:#0b6e77;}
[class*="st-key-card_"] [data-testid="stExpander"] summary:hover{color:#f2542d;}
[class*="st-key-card_"]{background:#fffdf8;border:2px solid #1a1a2e !important;border-radius:14px !important;box-shadow:5px 5px 0 #f2542d;}
[class*="st-key-card_teal"]{box-shadow:5px 5px 0 #0b6e77;}
[class*="st-key-card_yellow"]{box-shadow:5px 5px 0 #ffd23f;}
[class*="st-key-card_indigo"]{box-shadow:5px 5px 0 #35365f;}
.cardtitle{font-size:1.2rem;font-weight:800;line-height:1.25;margin-bottom:.25rem;}
.cardsub{font-size:1.05rem;font-weight:600;color:#35365f;}
.entryhead{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem .8rem;}
.entrylogo{width:2.6rem;height:2.6rem;border:2px solid #1a1a2e;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;font-weight:800;box-shadow:3px 3px 0 #1a1a2e;}
.entrytitle{flex:1 1 auto;font-size:1.55rem;font-weight:800;line-height:1.2;}
.entrytitle.small{font-size:1.2rem;flex-basis:100%;}
.entryperiod{border:2px solid #1a1a2e;border-radius:999px;padding:.15rem .85rem;font-size:.82rem;font-weight:700;max-width:100%;}
.entryrole{color:#0b6e77;font-weight:700;margin:.5rem 0 .3rem 0;}
[class*="st-key-card_"] li{margin-bottom:.35rem;}
[class*="st-key-card_"] li strong{background:linear-gradient(transparent 58%,rgba(255,210,63,.65) 58%);}
[data-testid="stLayoutWrapper"]:has(> [class*="st-key-tags_"]){margin-top:auto;}
[data-testid="stColumn"]:has([class*="st-key-card_"][class*="_entry"]) > [data-testid="stVerticalBlock"],[data-testid="stColumn"]:has([class*="st-key-card_"][class*="_strength"]) > [data-testid="stVerticalBlock"],[data-testid="stColumn"]:has([class*="st-key-card_"][class*="_skill"]) > [data-testid="stVerticalBlock"]{height:100%;}
[data-testid="stLayoutWrapper"]:has(> [class*="st-key-card_"][class*="_entry"]),[data-testid="stLayoutWrapper"]:has(> [class*="st-key-card_"][class*="_strength"]),[data-testid="stLayoutWrapper"]:has(> [class*="st-key-card_"][class*="_skill"]){flex:1 1 auto;}
[class*="st-key-card_"][class*="_entry"],[class*="st-key-card_"][class*="_strength"],[class*="st-key-card_"][class*="_skill"]{height:100% !important;}
.grouptitle{font-size:1.25rem;font-weight:800;line-height:1.2;}
.grouptitle::after{content:"";display:block;width:2.4rem;height:4px;border-radius:4px;margin-top:.45rem;background:var(--bar,#f2542d);}
.skillrow{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem;padding-bottom:1.1rem;}
.skill{display:inline-block;border-radius:8px;padding:.25rem .75rem;font-weight:600;font-size:.93rem;background:#f2ead8;color:#1a1a2e;}
.skill.hot{font-weight:800;}
.tilelabel{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.72rem;letter-spacing:.1em;font-weight:700;color:#4a4a63;}
.tilevalue{font-size:1rem;font-weight:800;margin:.25rem 0 .9rem 0;overflow-wrap:anywhere;}
.paneltitle{font-size:1.7rem;font-weight:800;line-height:1.2;margin-bottom:.4rem;}
.chips{display:flex;flex-wrap:wrap;gap:.6rem;margin:.4rem 0 1.1rem 0;}
.chip{border:2px solid #1a1a2e;border-radius:999px;padding:.3rem 1rem;font-weight:700;font-size:.9rem;box-shadow:3px 3px 0 #1a1a2e;}
.closing{position:relative;background:#ffd23f;border:2px solid #1a1a2e;border-radius:18px;box-shadow:8px 8px 0 #1a1a2e;padding:2.2rem 2rem 1.6rem 2rem;margin-bottom:2rem;overflow:hidden;}
.closing .paneltitle{font-size:2.4rem;}
.closing .closingsub{font-size:1.1rem;margin:.2rem 0 1.2rem 0;max-width:34rem;}
@keyframes fadein{from{opacity:0;transform:translateY(24px);}to{opacity:1;transform:none;}}
@keyframes pop{from{opacity:0;transform:scale(.5);}to{opacity:1;transform:scale(1);}}
.sectionband{animation:fadein .6s ease-out both;}
[class*="st-key-next_button"]{display:flex;justify-content:flex-end;}
.closing{animation:fadein .9s ease-out both;}
.closing .pop{animation:pop .5s ease-out both;animation-delay:calc(.5s + var(--i) * .15s);}
@media (prefers-reduced-motion: reduce){.sectionband,.closing,.closing .pop{animation:none;}}
</style>"""


def page_css(number):
    """Return the page CSS."""
    band, text = SECTION_COLORS[number - 1]
    return PAGE_CSS.replace("ACCENT", band).replace("BANDTEXT", text)


def card_key(kind, index):
    """Return a unique card key."""
    return "card_" + CARD_COLORS[index % len(CARD_COLORS)] + "_" + kind + str(index)


def default_resume():
    """Build the resume data."""
    return {
        "profile": {
            "name": "Xu Jie",
            "role": "Aspiring Business & Data Analyst",
            "summary": "I connect data with real business problems: understanding not only what the numbers show, but how insights can support better decisions. My hands-on experience spans data analytics, BI dashboards and sales operations across automotive, technology and esports.",
            "degree": "MSc in Business Analytics",
            "school": "Nanyang Technological University · Singapore",
            "location": "Singapore",
            "status": "Open to analytics roles",
            "email": "XUJI0030@e.ntu.edu.sg",
            "email_subject": "Business Analytics Enquiry",
            "linkedin": "https://www.linkedin.com/in/ntu-xujie",
            "photo": "assets/profile.jpeg",
        },
        "intro": "Learn about my background, skills and experience.",
        "sections": [
            {
                "name": "About",
                "covers": "Profile & education",
                "headline": "From questions to clarity.",
                "blurb": "My work sits where commercial priorities, analytical structure and cross-functional execution meet. I translate business questions into measurable insights.",
            },
            {
                "name": "Experience",
                "covers": "Work history",
                "headline": "Analysis in the real world.",
                "blurb": "Three roles across automotive, technology and esports. Use Reading mode in the sidebar for a quick scan, or pick skills there to highlight where I used them.",
            },
            {
                "name": "Projects",
                "covers": "Selected work",
                "headline": "Hands-on projects.",
                "blurb": "Three projects spanning customer conversion, product development and market strategy.",
            },
            {
                "name": "Skills",
                "covers": "Toolkit",
                "headline": "Skills with purpose.",
                "blurb": "A practical toolkit for moving from raw commercial data to a clear, decision-ready story.",
            },
            {
                "name": "Contact",
                "covers": "Get in touch",
                "headline": "Turn data into direction.",
                "blurb": "If you have a business problem worth solving with data, I would love to hear about it.",
            },
        ],
        "strengths": [
            {
                "title": "Commercial & Sales Analytics",
                "text": "Built a 180-day, five-stage lead conversion analysis at NIO and ran KPI reviews for 15 sales representatives at Ricoh, turning commercial questions into metrics teams can act on.",
                "short": "180-day funnel analysis at NIO. KPI reviews for 15 sales reps at Ricoh.",
            },
            {
                "title": "Dashboards & Data Systems",
                "text": "Power BI dashboards and Trino / Spark SQL workflows with drill-down by region, area, squad and sales Fellow, so performance is visible to the people who act on it.",
                "short": "Power BI dashboards and Trino / Spark SQL, with drill-down by region and squad.",
            },
            {
                "title": "Cross-functional Execution",
                "text": "Worked across automotive, technology and esports, with sales teams, 20+ sponsor clients and fan communities, translating between business questions and data.",
                "short": "Automotive, technology and esports. 20+ sponsor clients.",
            },
        ],
        "focus_areas": [
            "Business Analytics",
            "Data Analytics",
            "Business Intelligence",
            "Sales & Commercial Analytics",
        ],
        "education": [
            {
                "school": "Nanyang Technological University",
                "degree": "MSc in Business Analytics · Nanyang Business School",
                "meta": "Singapore · Aug 2026 — Dec 2027 (expected)",
                "notes": [],
            },
            {
                "school": "Donghua University",
                "degree": "Bachelor of Management in Information Management and Information Systems",
                "meta": "China · Sep 2022 — Jun 2026 · GPA 4.06 / 5.0",
                "notes": [
                    "**Relevant coursework:** Applied Statistics · Data Analytics and Data Mining · Big Data Technologies and Applications · Management Information Systems · Customer Relationship Analytics and Management",
                    "**Leadership:** Deputy Director, Public Relations Department, School Student Union · Organizational Officer, University Student Union · Member, Undergraduate Admissions Office Media Center",
                ],
            },
        ],
        "languages": [
            {
                "name": "Chinese",
                "level": "Native",
            },
            {
                "name": "English",
                "level": "Business",
            },
        ],
        "interests": [
            "Business intelligence and data visualisation for commercial decisions",
            "Esports, digital content creation and online communities",
            "Technology for education and social impact",
        ],
        "experience": [
            {
                "name": "NIO Inc.",
                "role": "Data Analyst Intern · Digitalization Team",
                "place": "Shanghai, China",
                "period": "Oct 2025 — Jun 2026",
                "quick": "Built a **180-day, five-stage lead conversion analysis** and the **BI dashboards** around it with Trino and Spark SQL.",
                "bullets": [
                    "Cleaned and unified sales lead, channel, test-drive and lock-order data, including reclassifying Ledao campaign channels, to enable **sales conversion analysis** and dashboard development.",
                    "Developed and iterated **BI dashboards** for call-list pools, in-stock vehicles, new model launches, store traffic and eATV user value, enabling drill-down analysis by region, area, squad and sales Fellow.",
                    "Leveraged **Trino and Spark SQL** to create a **180-day lead conversion analysis** across browsing, follow-up, connection, test-drive and lock-order stages, producing key metrics for sales effectiveness evaluation.",
                ],
                "tags": [
                    "SQL",
                    "Trino",
                    "Spark SQL",
                    "Conversion analysis",
                    "Dashboard development",
                    "Sales operations",
                ],
            },
            {
                "name": "Ricoh (China) Investment Co., Ltd.",
                "role": "Data Analyst Intern",
                "place": "Shanghai, China",
                "period": "Jul 2025 — Aug 2025",
                "quick": "Tracked monthly results of **15 sales representatives** and built **Power BI dashboards** for market coverage.",
                "bullets": [
                    "Calculated monthly machine volume and sales revenue for **15 sales representatives** with **Excel XLOOKUP and SUMIFS**, enabling KPI review and underperformance diagnosis.",
                    "Created **Power BI dashboards** by industry and region to monitor monthly coverage and inform new-market expansion decisions.",
                    "Monitored maintenance contracts for **35 companies** and consolidated monthly trend reports to inform sales strategy refinement.",
                ],
                "tags": ["Excel", "Power BI", "KPI analysis", "Dashboard development", "Sales operations"],
            },
            {
                "name": "Hero Esports (formerly VSPO)",
                "role": "Commercial Client Execution Intern",
                "place": "Shanghai, China",
                "period": "Apr 2024 — Sep 2024",
                "quick": "Coordinated **20+ sponsor clients** for the 2024 KPL events and grew fan-community engagement by **25%**.",
                "bullets": [
                    "Executed commercial operations for the **2024 KPL Spring and Summer events**, coordinating with **20+ sponsor clients** to collect requirements and protect client entitlements.",
                    "Evaluated sponsorship data and prepared **5+ reports** to identify growth opportunities and inform commercial strategy improvement.",
                    "Expanded **18 core fan communities**, achieved **25% engagement growth**, and added **3,000+ followers** through Douyin and Xiaohongshu content operations.",
                ],
                "tags": [
                    "Client coordination",
                    "Cross-functional collaboration",
                    "Reporting",
                    "Content operations",
                ],
            },
        ],
        "projects": [
            {
                "name": "NIO – 180-Day Lead Conversion Analysis",
                "period": "Mar 2026 — Jun 2026",
                "role": "Customer journey analytics · Trino · Spark SQL",
                "quick": "A **180-day lead conversion flow** from browsing to lock-order.",
                "bullets": [
                    "Built a **180-day lead conversion flow** covering browsing, follow-up, connection, test-drive and lock-order stages.",
                    "Integrated **customer journey data** across multiple stages and developed conversion metrics for sales-effectiveness evaluation and business drill-downs.",
                ],
                "tags": ["SQL", "Trino", "Spark SQL", "Conversion analysis"],
            },
            {
                "name": "Qingmang Wuyu – Science Education Platform",
                "period": "Jul 2024 — May 2025",
                "role": "Team Leader · Django · MySQL · Neo4j",
                "quick": "Led a science-education web platform; won **Third Prize** in the Shanghai Collegiate Computer Application Competition.",
                "bullets": [
                    "Led **architecture design, core development and team coordination** for a science-education web platform.",
                    "Integrated **Neo4j knowledge graphs** to improve information retrieval and knowledge connectivity; won **Third Prize** in the Shanghai Collegiate Computer Application Competition.",
                ],
                "tags": ["Python", "Django", "MySQL", "Neo4j"],
            },
            {
                "name": "Nestlé CEO Challenge – Marketing Innovation Track",
                "period": "Mar 2024 — Jun 2024",
                "role": "Team Member · Key-account research · Top 5",
                "quick": "Key-account research and a channel-expansion proposal that placed **Top 5**.",
                "bullets": [
                    "Conducted **key-account market research** across Nestlé Professional food-service channels, customer needs and competitor strategies.",
                    "Evaluated commercial potential and refined an actionable channel-expansion proposal that achieved a **Top 5 placement**.",
                ],
                "tags": ["Market research"],
            },
        ],
        "skills": {
            "Data Analysis & BI": ["Excel", "Power BI", "Tableau", "SPSS"],
            "Querying & Databases": ["SQL", "SQL Server", "MySQL", "Trino", "Spark SQL"],
            "Programming": ["Python", "Django", "Neo4j"],
            "Business Analytics": [
                "KPI analysis",
                "Conversion analysis",
                "CRM analysis",
                "Sales operations",
                "Dashboard development",
            ],
        },
        "highlight_skills": ["Power BI", "Tableau", "SQL", "Trino", "Spark SQL", "Python", "Conversion analysis"],
    }


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------
def join_parts(parts):
    """Join the non-empty pieces with a middle dot."""
    return " · ".join([part for part in parts if part != ""])


def clean_name(text):
    """Keep letters, digits and spaces only (max 30), so a typed name is safe to show and to put in a link."""
    letters = [ch for ch in text.strip() if ch.isalnum() or ch == " "]
    return "".join(letters)[:30]


def email_link(profile, reader):
    """mailto: link. If the visitor typed a name, it is added to the subject."""
    subject = profile.get("email_subject", "")
    if reader != "":
        subject = subject + " from " + reader
    return "mailto:" + profile["email"] + "?subject=" + subject.replace(" ", "%20")


def esc(text):
    """Make a text safe to place inside our own HTML."""
    return text.replace("&", "&amp;").replace("<", "&lt;")


def plain(text):
    """Remove the ** marks (used for the downloadable text resume)."""
    return text.replace("**", "")


def badges(items, hot_items, colour="gray"):
    """Streamlit badges in one line. Items found in hot_items are orange, the rest use colour."""
    pieces = []
    for item in items:
        if item in hot_items:
            pieces.append(":orange-badge[" + item + "]")
        else:
            pieces.append(":" + colour + "-badge[" + item + "]")
    return " ".join(pieces)


def bullet_text(bullets):
    """A markdown bullet list. **word** in the text becomes bold automatically."""
    return "\n".join(["- " + bullet for bullet in bullets])


def collect_toolkit(data):
    """Every skill named in the skills section or tagged on a job or project."""
    toolkit = set()
    for group in data["skills"].values():
        for skill in group:
            toolkit.add(skill)
    for entry in data["experience"] + data["projects"]:
        for tag in entry.get("tags", []):
            toolkit.add(tag)
    return toolkit


def build_text_resume(data):
    """The whole resume as plain text, built from the same data as the page."""
    profile = data["profile"]
    lines = [profile["name"], profile["role"], profile["degree"] + ", " + profile["school"]]
    lines.append("Email: " + profile["email"])
    lines.append("LinkedIn: " + profile["linkedin"])
    lines.append("")

    sections = [("EXPERIENCE", data["experience"]), ("PROJECTS", data["projects"])]
    for title, entries in sections:
        lines.append(title)
        lines.append("=" * len(title))
        for entry in entries:
            lines.append(entry["name"] + "  (" + entry["period"] + ")")
            for bullet in entry["bullets"]:
                lines.append("  - " + plain(bullet))
            lines.append("")

    lines.append("SKILLS")
    lines.append("======")
    for group, skills in data["skills"].items():
        lines.append(group + ": " + ", ".join(skills))
    lines.append("")

    lines.append("EDUCATION")
    lines.append("=========")
    for item in data["education"]:
        lines.append(item["school"] + " - " + item["degree"] + " (" + item["meta"] + ")")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Page pieces (one function per piece)
# ---------------------------------------------------------------------------
def section_header(number, section, mode_name):
    """A coloured band: small section label, the headline and (in Full story) a short blurb."""
    kicker = ("SECTION " + f"{number:02d}" + " OF " + f"{SECTION_TOTAL:02d}" + " · " + section["name"].upper()
              + " · " + section["covers"].upper() + " · READING MODE: " + mode_name.upper())
    band = '<div class="sectionband"><div class="kicker">' + kicker.replace("&", "&amp;") + '</div>'
    band = band + '<div class="headline">' + section["headline"].replace("&", "&amp;") + '</div>'
    if mode_name != "Quick scan":
        band = band + '<div class="blurb">' + section["blurb"].replace("&", "&amp;") + '</div>'
    st.markdown(band + '</div>', unsafe_allow_html=True)


def show_hero(profile, reader):
    left, right = st.columns([1.6, 1], gap="large")
    with left:
        if reader != "":
            st.caption("Hello " + reader + ", I'm")
        else:
            st.caption("Hello, I'm")
        st.markdown('<div class="heroname">' + profile["name"] + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="herorole">' + profile["role"].replace("&", "&amp;") + '</div>', unsafe_allow_html=True)
        st.write(profile["summary"])
        st.caption(profile["degree"] + " · " + profile["school"])
        button_left, button_right, spare = st.columns([1, 1, 1.4])
        button_left.link_button("Email me", email_link(profile, reader), type="primary")
        button_right.link_button("LinkedIn", profile["linkedin"])
    with right:
        # The photo is read with open(); if it is missing the page still works.
        try:
            photo_path = Path(__file__).resolve().parent / profile.get("photo", "")
            with open(photo_path, "rb") as photo_file:
                photo_bytes = photo_file.read()
            st.image(photo_bytes)
        except FileNotFoundError:
            st.caption("(profile photo not found: keep the assets folder next to resume_app.py)")
        st.markdown(":orange-badge[" + profile["status"] + "] :green-badge[Based in " + profile["location"] + "]")


def show_about(data, section, quick_mode, mode_name, reader):
    show_hero(data["profile"], reader)
    st.divider()
    section_header(1, section, mode_name)

    st.subheader("What I bring")
    strengths = data["strengths"]
    columns = st.columns(max(len(strengths), 1))
    for i in range(len(strengths)):
        item = strengths[i]
        text = item["text"]
        if quick_mode:
            text = item.get("short", item["text"])
        with columns[i]:
            with st.container(border=True, key=card_key("strength", i)):
                st.markdown('<div class="cardtitle">' + f"{i + 1:02d}" + " · " + esc(item["title"]) + '</div>', unsafe_allow_html=True)
                st.write(text)

    st.subheader("Where I want to grow")
    st.markdown(badges(data["focus_areas"], data["focus_areas"][::2], "violet"))

    left, right = st.columns([1.3, 0.7], gap="large")
    with left:
        st.subheader("Education")
        for i in range(len(data["education"])):
            item = data["education"][i]
            with st.container(border=True, key=card_key("edu", i + 1)):
                st.markdown('<div class="cardtitle">' + esc(item["school"]) + '</div>', unsafe_allow_html=True)
                st.markdown('<div class="cardsub">' + esc(item["degree"]) + '</div>', unsafe_allow_html=True)
                st.caption(item["meta"])
                if not quick_mode:
                    for note in item.get("notes", []):
                        st.markdown(note)
    with right:
        st.subheader("Languages")
        with st.container(border=True, key=card_key("lang", 2)):
            for lang in data["languages"]:
                st.markdown("**" + lang["name"] + "** · " + lang["level"])
        if not quick_mode:
            st.subheader("Interests")
            st.markdown(bullet_text(data["interests"]))


def show_entry(index, title, subtitle, period, quick_text, bullets, tags, quick_mode, chosen, colour, compact, collapse):
    """One bordered card for a job or a project. Quick scan: one line, no tags.
    compact=True is used for the narrow project cards (smaller title, no logo square).
    collapse=True puts ALL the bullets (equal weight) inside one click-to-open expander;
    the header and the skill tags stay visible."""
    pill_background, pill_text = CARD_PILLS[index % len(CARD_PILLS)]
    with st.container(border=True, key=card_key("entry", index)):
        head = '<div class="entryhead">'
        if not compact:
            head = head + '<span class="entrylogo" style="background:' + pill_background + ';color:' + pill_text + '">' + esc(title[0]) + '</span>'
        if compact:
            head = head + '<div class="entrytitle small">' + esc(title) + '</div>'
        else:
            head = head + '<div class="entrytitle">' + esc(title) + '</div>'
        head = head + '<span class="entryperiod" style="background:' + pill_background + ';color:' + pill_text + '">' + esc(period) + '</span></div>'
        st.markdown(head + '<div class="entryrole">' + esc(subtitle) + '</div>', unsafe_allow_html=True)
        if quick_mode:
            if quick_text == "" and len(bullets) > 0:
                quick_text = bullets[0]
            st.markdown(quick_text)
        else:
            if collapse:
                with st.expander("What I did"):
                    st.markdown(bullet_text(bullets))
            else:
                st.markdown(bullet_text(bullets))
            if len(tags) > 0:
                # its own container, so the CSS can keep the tags at the bottom of the card
                with st.container(key="tags_" + str(index)):
                    st.markdown(badges(tags, chosen, colour))
        hits = [skill for skill in chosen if skill in tags]
        if len(hits) > 0:
            st.markdown(":green-badge[Matches your skill filter: " + ", ".join(hits) + "]")


def split_by_filter(entries, chosen):
    """(entries that use a chosen skill, the other entries). No filter: everything matches."""
    if len(chosen) == 0:
        return entries, []
    matching = [entry for entry in entries if len([s for s in chosen if s in entry.get("tags", [])]) > 0]
    others = [entry for entry in entries if entry not in matching]
    return matching, others


def show_experience(data, section, quick_mode, mode_name, chosen):
    section_header(2, section, mode_name)

    matching, others = split_by_filter(data["experience"], chosen)
    for i in range(len(matching)):
        entry = matching[i]
        show_entry(i, entry["name"], join_parts([entry["role"], entry.get("place", "")]), entry["period"],
                   entry.get("quick", ""), entry["bullets"], entry.get("tags", []), quick_mode, chosen, "blue", False, True)
    if len(others) > 0:
        st.caption("Not using your selected skills: " + ", ".join([entry["name"] for entry in others]))


def show_projects(data, section, quick_mode, mode_name, chosen):
    section_header(3, section, mode_name)
    matching, others = split_by_filter(data["projects"], chosen)
    if len(matching) > 0:
        columns = st.columns(len(matching))
        for i in range(len(matching)):
            project = matching[i]
            with columns[i]:
                show_entry(i, project["name"], project["role"], project["period"], project.get("quick", ""),
                           project["bullets"], project.get("tags", []), quick_mode, chosen, "violet", True, False)
    elif len(others) == 0:
        st.info("No projects yet. Add one inside default_resume().")
    if len(others) > 0:
        st.caption("Not using your selected skills: " + ", ".join([entry["name"] for entry in others]))


def skill_chip(skill, hot, index):
    """One skill as a small rounded tag. Tools I use most are tinted in the colour of their group."""
    if hot:
        return '<span class="skill hot" style="background:' + CARD_TINTS[index % len(CARD_TINTS)] + '">' + esc(skill) + '</span>'
    return '<span class="skill">' + esc(skill) + '</span>'


def show_skills(data):
    """Skill groups, in two columns. Coloured tags are the tools I use most."""
    groups = list(data["skills"].items())
    for start in range(0, len(groups), 2):
        row = st.columns(2)
        for offset in range(2):
            if start + offset < len(groups):
                index = start + offset
                name, skills = groups[index]
                bar_colour = CARD_PILLS[index % len(CARD_PILLS)][0]
                chips = ""
                for skill in skills:
                    chips = chips + skill_chip(skill, skill in data["highlight_skills"], index)
                with row[offset]:
                    with st.container(border=True, key=card_key("skill", index)):
                        st.markdown('<div class="grouptitle" style="--bar:' + bar_colour + '">' + esc(name) + '</div><div class="skillrow">' + chips + '</div>', unsafe_allow_html=True)
    st.caption("Coloured tags are the tools I use most in my analyst work.")


def show_skills_section(data, section, mode_name):
    section_header(4, section, mode_name)
    show_skills(data)


def section_chips(sections):
    """One coloured chip per section. On the last section every chip is shown: the resume is complete."""
    chips = ""
    for i in range(len(sections)):
        band, text = SECTION_COLORS[i]
        chips = chips + '<span class="chip pop" style="--i:' + str(i) + ';background:' + band + ';color:' + text + '">' + f"{i + 1:02d}" + " · " + sections[i]["name"] + '</span>'
    return '<div class="chips">' + chips + '</div>'


def show_contact(data, section, mode_name, reader):
    profile = data["profile"]
    section_header(5, section, mode_name)

    # Three "ways to reach me" tiles, each with its own colour
    email_tile, linkedin_tile, resume_tile = st.columns(3)
    with email_tile:
        with st.container(border=True, key=card_key("tile", 0)):
            st.markdown('<div class="tilelabel">EMAIL</div><div class="tilevalue">' + profile["email"] + '</div>', unsafe_allow_html=True)
            st.link_button("Write to me", email_link(profile, reader), type="primary")
    with linkedin_tile:
        with st.container(border=True, key=card_key("tile", 1)):
            st.markdown('<div class="tilelabel">LINKEDIN</div><div class="tilevalue">' + profile["linkedin"].replace("https://www.linkedin.com/", "") + '</div>', unsafe_allow_html=True)
            st.link_button("Open my profile", profile["linkedin"])
    with resume_tile:
        with st.container(border=True, key=card_key("tile", 2)):
            st.markdown('<div class="tilelabel">RESUME</div><div class="tilevalue">Plain-text copy</div>', unsafe_allow_html=True)
            st.download_button(
                "Download .txt",
                data=build_text_resume(data),
                file_name="Xu_Jie_resume.txt",
                mime="text/plain",
            )

    # The closing card fades in and its chips pop in one by one. Plain CSS animation (see PAGE_CSS).
    st.write("")
    closing = '<div class="closing">'
    closing = closing + '<div class="paneltitle">Thanks for reading' + (", " + reader if reader != "" else "") + '.</div>'
    closing = closing + '<div class="closingsub">You have read the whole resume. If you have a business problem worth solving with data, I would love to hear about it.</div>'
    closing = closing + section_chips(data["sections"]) + '</div>'
    st.markdown(closing, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Moving between sections
# ---------------------------------------------------------------------------
def go_to(label):
    """Button callback: select this section in the sidebar (session_state remembers it)."""
    st.session_state["section"] = label


def show_nav_buttons(sections, number):
    """Previous / Next buttons under every section."""
    left, right = st.columns(2)
    if number > 1:
        name = sections[number - 2]["name"]
        left.button("← " + name, on_click=go_to, args=(f"{number - 1:02d} · {name}",), key="prev_button")
    if number < len(sections):
        name = sections[number]["name"]
        right.button(name + " →", on_click=go_to, args=(f"{number + 1:02d} · {name}",), type="primary", key="next_button")


# ---------------------------------------------------------------------------
# Main program
# ---------------------------------------------------------------------------
def main():
    data = default_resume()
    profile = data["profile"]
    sections = data["sections"]

    st.set_page_config(page_title=profile["name"] + " · " + profile["role"], layout="wide")

    # The sidebar is the control panel
    st.sidebar.title(profile["name"])
    st.sidebar.caption(profile["role"])
    labels = [f"{i + 1:02d} · {sections[i]['name']}" for i in range(len(sections))]
    choice = st.sidebar.radio("Section", labels, key="section")
    number = labels.index(choice) + 1

    # session_state remembers which sections this visitor has opened
    if "visited" not in st.session_state:
        st.session_state.visited = []
    if number not in st.session_state.visited:
        st.session_state.visited.append(number)
    read = len(st.session_state.visited)
    st.sidebar.progress(read / SECTION_TOTAL, text="Read " + str(read) + " of " + str(SECTION_TOTAL) + " sections")
    if read == SECTION_TOTAL:
        st.sidebar.caption("You have read every section. Thank you!")
    else:
        st.sidebar.caption(data["intro"])
    st.sidebar.divider()

    mode = st.sidebar.radio("Reading mode", MODES, key="reading_mode")
    quick_mode = mode == "Quick scan"
    st.sidebar.caption("Quick scan: one short line per item. Full story: every detail.")

    all_tags = list(collect_toolkit(data))
    all_tags.sort()
    chosen = st.sidebar.multiselect("Highlight my experience by skill", all_tags, key="skill_filter")
    st.sidebar.caption("Pick skills to highlight them on the Experience and Projects sections.")

    reader = clean_name(st.sidebar.text_input("Your name (optional)", key="reader_name"))
    st.sidebar.caption("Type your name and the page will greet you and add it to the email subject.")

    st.markdown(page_css(number), unsafe_allow_html=True)
    if number == 1:
        show_about(data, sections[0], quick_mode, mode, reader)
    elif number == 2:
        show_experience(data, sections[1], quick_mode, mode, chosen)
    elif number == 3:
        show_projects(data, sections[2], quick_mode, mode, chosen)
    elif number == 4:
        show_skills_section(data, sections[3], mode)
    else:
        show_contact(data, sections[4], mode, reader)

    st.divider()
    show_nav_buttons(sections, number)
    st.caption(profile["name"] + " · " + profile["role"] + " · " + profile["location"] + " · 2026")


if __name__ == "__main__":
    main()
