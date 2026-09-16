# Math Club site

A small Python program that builds your club's website. You edit one Python
file, run one command, and get a single `index.html` you can host anywhere for
free.

```
content.py            <- the only file you need to edit
build.py              <- run this to rebuild the site
templates/
  base.html           <- shared masthead, nav, footer
  index.html          <- Home page (problem of the week)
  about.html          <- About page (description, officers)
  schedule.html       <- Schedule page (meetings, competitions)
  archive.html        <- Archive page (past problems)
  join.html           <- Join page (how to join, resources)
  style.css.j2        <- colors, fonts, layout
docs/
  *.html              <- generated. Do not edit by hand; it gets overwritten.
```

The site is five separate pages (Home, About, Schedule, Archive, Join) sharing
one masthead and navigation bar, styled in a plain classic-minimalist look:
one serif typeface, no boxes or shadows, thin hairline rules between
sections.

## Running it

You need Python 3.9 or newer.

```bash
pip install -r requirements.txt
python build.py --serve
```

Then open http://localhost:8000. Stop it with Ctrl+C. Click through Home,
About, Schedule, Archive, and Join to check each page.

To rebuild without the preview server, just run `python build.py`.

## Changing the content

Open `content.py`. Everything on the page comes from that file: the club name,
the problem of the week, meeting times, the competition calendar, officers,
resources. Change a value, save, run `python build.py` again, refresh.

Posting a new problem each week is three edits:

1. Move the current problem into the top of the `ARCHIVE` list.
2. Replace `PROBLEM_OF_THE_WEEK` with the new one.
3. Run `python build.py` and push (see below).

Math symbols can be pasted straight into the text: √ π ≤ ≥ ≠ ∑ ∞ ° ² ³ ₁ ₂.
If you ever need real equation layout, add MathJax by putting this line just
before `</head>` in `templates/base.html` (it's shared by every page):

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js"></script>
```

Then you can write `\(x^2 + y^2 = r^2\)` inside any content string.

## Putting it online, free

**GitHub Pages** is the recommendation. It's free with no time limit, it never
sleeps, and it works with a school-owned domain later if you want one.

1. Make a free GitHub account and create a repository named `math-club`.
2. Upload this whole folder to it (the web uploader at
   **Add file → Upload files** is fine; you don't need to learn git yet).
3. In the repo, go to **Settings → Pages**.
4. Under "Build and deployment", set Source to **Deploy from a branch**,
   branch to **main**, and folder to **/docs**. Save.
5. Wait a minute. Your site is at
   `https://YOUR-USERNAME.github.io/math-club/`.

After that, every time you change `content.py`, run `python build.py` and
re-upload the changed files. The site updates within a minute.

### Other free options

- **Netlify** or **Cloudflare Pages** — drag the `docs` folder onto their
  dashboard. Also free and permanent. Good if you want a nicer URL.
- **PythonAnywhere** — free tier, and it runs actual Python on a server. Only
  worth it if you later want features that need a server, like a form members
  submit solutions through. A plain club site does not need this.

## One thing to check before launching

Ask your advisor before publishing student names or photos. Many schools have
rules about it. Listing first names and grade levels is usually fine; last
names and personal emails often aren't.
