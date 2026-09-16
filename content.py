# =============================================================
#  EDIT THIS FILE TO CHANGE YOUR SITE.
#  Everything below is placeholder content - swap in your own,
#  then run:  python build.py
# =============================================================

SITE = {
    "club_name": "Math Club",
    "school": "Anderson CVI",
    "tagline": "Anderson CVI's very own Math Club.",
    "email": "mathclub@riverside.edu",
    "instagram": "",          # e.g. "AndersonMathCkub" - leave "" to hide
    "year": "2026-27",
    "founded": "1960",     # shown in the small line above the club name
}

# ---- The problem that opens the site -------------------------
# Keep it short enough to read in one breath. Unicode symbols work
# fine here: √ π ≤ ≥ ≠ ∑ ∞ ° ⌊ ⌋ ² ³ ₁ ₂
PROBLEM_OF_THE_WEEK = {
    "number": 6,
    "posted": "September 14, 2026",
    "due": "Friday at 3:30 PM",
    "difficulty": "Medium",      # Warm-up / Medium / Hard
    "statement": (
        "A 3 × 3 grid is filled with the numbers 1 through 9, each used once. "
        "Call a filling <em>balanced</em> if every row and every column has the "
        "same sum. How many balanced fillings are there?"
    ),
    "hint": (
        "Every row must sum to 15, since the nine numbers total 45. Start by "
        "asking which number has to sit in the center."
    ),
    "how_to_submit": "IN PROGRESS (HOW TO SUMBIT)",
}

# ---- Past problems (newest first) ----------------------------
ARCHIVE = [
    {"number": 5, "title": "The seven bridges of the cafeteria", "topic": "Graph theory",
     "answer": "No such walk exists - four corners have odd degree."},
    {"number": 4, "title": "A rope around the equator", "topic": "Geometry",
     "answer": "About 16 cm, and it does not depend on the size of the planet."},
    {"number": 3, "title": "Three dice, one suspicious total", "topic": "Probability",
     "answer": "25/216"},
    {"number": 2, "title": "Why 1 is not prime", "topic": "Number theory",
     "answer": "Unique factorization would fail."},
    {"number": 1, "title": "Folding a strip of paper", "topic": "Sequences",
     "answer": "The dragon curve."},
]

# ---- What the club actually does -----------------------------
ABOUT = {
    "lead": (
        "Math Club is open to every student at "
        + SITE["school"]
        + ", whether you are in Algebra 1 or finishing BC Calculus. "
        "You do not need to be fast, and you do not need to compete."
    ),
    "activities": [
        ("Problem sessions", "We put one problem on the board and work it out together. "
                             "Wrong turns are the useful part."),
        ("Contest practice", "Timed sets from old AMC and ARML papers for anyone who wants them."),
        ("Talks", "Short student talks on something you found interesting. "
                  "Fifteen minutes, no slides required."),
        ("Peer tutoring", "Members tutor underclassmen during lunch on Wednesdays."),
    ],
}

# ---- Meetings ------------------------------------------------
MEETINGS = {
    "when": "Wednesdays, 12:15 - 12:50",
    "where": "Room 205",
    "next_date": "Wednesday, September 23",
    "next_topic": "WORK IN PROGRESS (next topic)",
    "note": "WORK IN PROGRESS",
}

# ---- Competition calendar (a real sequence, so it is dated) ---
COMPETITIONS = [
    {"date": "Nov 6", "name": "WORK IN PROGRESS", "detail": "WORK IN PROGRESS"},
    {"date": "Nov 12", "name": "WORK IN PROGRESS", "detail": "WORK IN PROGRESS"},
    {"date": "Feb 5", "name": "WORK IN PROGRESS", "detail": "WORK IN PROGRESS"},
    {"date": "Mar 21", "name": "WORK IN PROGRESS", "detail": "WORK IN PROGRESS"},
    {"date": "May 30", "name": "WORK IN PROGRESS", "detail": "WORK IN PROGRESS"},
]

# ---- Officers ------------------------------------------------
OFFICERS = [
    {"name": "WORK IN PROGRESS", "role": "President", "note": "WORK IN PROGRESS"},
    {"name": "WORK IN PROGRESS", "role": "Vice president", "note": "WORK IN PROGRESS"},
    {"name": "WORK IN PROGRESS", "role": "Treasurer", "note": "WORK IN PROGRESS"},
    {"name": "WORK IN PROGRESS", "role": "Faculty advisor", "note": "Room 205"},
]

# ---- Resources -----------------------------------------------
RESOURCES = [
    {"name": "Art of Problem Solving", "url": "https://artofproblemsolving.com",
     "note": "Forums, textbooks, and every past AMC problem with solutions."},
    {"name": "Past AMC problems", "url": "https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions",
     "note": "Sorted by year and difficulty."},
    {"name": "Project Euler", "url": "https://projecteuler.net",
     "note": "Math problems you solve by writing code."},
    {"name": "3Blue1Brown", "url": "https://www.3blue1brown.com",
     "note": "Visual explanations of ideas you will meet later in high school."},
    {"name": "Our shared folder", "url": "#",
     "note": "Replace this link with your club's Drive folder of notes and past sets."},
]

# ---- Joining -------------------------------------------------
JOIN = {
    "steps": [
        "Show up to any Thursday meeting in Room 214. That is the whole process.",
        "Add your name to the roster sheet so you get the weekly email.",
        "Optional: pay the $5 yearly dues, which cover contest fees and snacks.",
    ],
    "closing": "If you would rather ask a question first, email us.",
}
