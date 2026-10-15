# Puppy Chow — monthly issue runbook

You are producing one issue of **Puppy Chow**, a monthly digest for a San Diego shelter dog trainer. This file is the complete procedure. Follow it top to bottom without asking questions; nobody is watching the run. When something can't be done, record it in the issue footer and keep going.

Reference example of a finished issue: `docs/2026-10/index.html`. Match its structure, components, CSS, and voice exactly.

## 0. Set the window

- Window = the **previous calendar month** (e.g. a run on 2026-12-02 covers 2026-11-01 → 2026-11-30).
- Issue folder = `docs/YYYY-MM/` for that month. Issue number = previous highest number + 1 (read `docs/index.html`).
- Exception: issue No. 1 covered Sept 15 – Oct 15, 2026. Issue No. 2 covers **Oct 16 – Nov 30, 2026** so nothing falls in a gap.
- If `docs/YYYY-MM/` already exists, stop: this month is done.
- Read the previous issue so you don't repeat a story unless there's a real new development (then say what's new).

## 1. Reader and stance

- Reader: a working dog trainer at a San Diego shelter. Practitioner level; don't explain basics (LIMA, cortisol, length of stay).
- **Take no side** on training methods (aversive vs. reward-based). Report what each source says.
- **Call out bias**: funding/conflicts of interest, small n, no control group, owner-reported outcomes, single site, press release vs. independent reporting, advocacy framing from any side.
- A bias note must itself be supported by the source or by what you observed (e.g. "this is the organization's own press release", "the article cites KPBS for its figures"). **Never** characterize an outlet or group from memory ("trade outlet for landlords", "writes from the breeder side", "aggregator-style"). The pilot's critic rejected exactly these.

## 2. Zero-hallucination rules (non-negotiable)

- Every factual claim (number, date, n, odds ratio, chapter number, vote, who supported what) must appear on a page you actually fetched this run, and the card must link to that page.
- Quotes are verbatim, inside quotation marks, and appear on the linked page. Don't put a period inside a quote that continues in the source.
- Never report from memory or from search-result snippets alone. If you can only see a headline, say "only the headline/summary was readable" and use nothing beyond it.
- If sources conflict (e.g. press date vs. leginfo date), use the primary source and note the conflict in one line.
- Never pad. A thin section says "nothing found" plus what was checked.
- Never bypass a CAPTCHA, bot check, login, or paywall. Log the blocked URL in the footer.
- Anything published outside the window goes only in a clearly labeled "Just missed" / "Context" box, max 2–3 per section.

## 3. Research — run three subagents in parallel

Dispatch these as three parallel subagents (Agent tool). Give each the window dates and sections 1–2 of this file verbatim. Each returns structured markdown: per item, title, source, date as shown, URL, verbatim supporting quote(s), summary, bias/limits note, suggested "on the floor" line, plus a "what I checked / what was blocked" list.

**A. Research papers** (target 4–8 in window; prioritize shelter/rescue dogs)
- PubMed E-utilities (no cookie wall), date-bounded on entry date:
  `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&datetype=edat&mindate=YYYY/MM/DD&maxdate=YYYY/MM/DD&retmax=100&term=...` then `efetch.fcgi?db=pubmed&id=<PMIDs>&rettype=abstract&retmode=text` to read abstracts.
- Queries:
  1. `("shelter dog*"[tiab] OR "animal shelter"[tiab] OR "shelter dogs"[tiab]) AND (behavio*[tiab] OR welfare[tiab] OR stress[tiab] OR enrichment[tiab])`
  2. `(dog[tiab] OR dogs[tiab] OR canine[tiab]) AND (adoption[tiab] OR relinquish*[tiab] OR "training method*"[tiab] OR "behavio* assessment"[tiab] OR kennel[tiab] OR "length of stay"[tiab] OR foster*[tiab] OR playgroup*[tiab])`
  3. `(dog[ti] OR dogs[ti] OR canine[ti]) AND (behavio*[ti] OR welfare[ti] OR fear[ti] OR aggress*[ti] OR training[ti] OR cognition[ti] OR enrichment[ti] OR anxiety[ti])`
- Then check journal sites directly (PubMed indexes them slowly): Applied Animal Behaviour Science, Journal of Veterinary Behavior, Animal Cognition, Animals (MDPI), Frontiers in Veterinary Science, IAABC Journal (journal.iaabcfoundation.org).
- Per paper: design chips (study type, n, setting, journal + date, "Abstract only" or "Open access · abstract read").

**B. California law** (and federal only if enacted)
- Sources: gov.ca.gov signing/veto lists and press releases; leginfo bill status (`https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=20XX20XX0AB1234`) and text (`billTextClient.xhtml?...`) — try curl with a normal browser User-Agent if WebFetch is blocked; fallback CalMatters Digital Democracy (`calmatters.digitaldemocracy.org/bills/ca_20XX20XX0ab1234`); Social Compassion in Legislation; SDHS advocacy; CVMA bill chart.
- Calendar awareness: Jan–Feb bill introductions; spring/summer committee deadlines; Aug 31 last day to pass (even years); Sept 30 governor deadline; most statutes effective Jan 1. In quiet months, cover newly introduced bills and committee hearings affecting dogs/shelters/trainers, and laws taking effect.
- Per bill: number, author, status + date from leginfo or the governor's list, chapter number if signed, effective/operative date, digest quote, why it matters to a shelter trainer.

**C. San Diego local**
- Sources: sdhumane.org news center and press releases, County of San Diego Animal Services / countynewscenter.com, City of SD + County Board of Supervisors agendas, KPBS, Times of San Diego, Union-Tribune, NBC 7, 10News, Fox 5, CBS 8, Axios San Diego, Voice of San Diego, Hoodline, Patch; other shelters (Rancho Coastal Humane, Helen Woodward, PAWS of Coronado, Chula Vista Animal Care, Escondido Humane).
- Topics: capacity/intake, shelter policy and contracts, programs, ordinances (leash, dog parks, beaches, dangerous dogs), disease outbreaks, local trainer news/events/enforcement.

## 4. Assemble

- Copy `docs/2026-10/index.html` as the template: same `<head>`, CSS, and components (mast, TL;DR top 3, Research / California law / San Diego sections, cards with chips, quote, "Grain of salt", "On the floor", source line, context boxes, "How this issue was made" footer). Update the title (`Puppy Chow No. N`), mast (issue number, window dates), and content.
- "On the floor" lines must not claim more than the evidence supports. Hedge where the source is thin.
- Footer: list what was searched, what was blocked or unreadable, and known coverage gaps.
- Write it to `docs/YYYY-MM/index.html`.
- Add the issue to the top of the list in `docs/index.html` (newest first), matching the existing `<li>` format.

## 5. Critic pass (fresh context)

Dispatch one subagent with only: the draft path, sections 1–2 of this file, and the window. Instruct it to fetch every linked source and return a table of every claim → VERIFIED / WRONG / NOT ON SOURCE / UNFETCHABLE, plus "must fix" vs "nice to have", and any unlabeled out-of-window item or unsupported bias note.

Fix every "must fix" item by correcting it or cutting it. Never soften a claim into vagueness to keep it; cut it. If more than 3 must-fix items were found, run the critic once more on the fixed draft.

## 6. Publish and deliver (handled by the workflow)

Don't run git and don't send email. When you finish, the `Monthly issue` workflow (`.github/workflows/monthly-issue.yml`) commits `docs/`, pushes to `main`, rebuilds GitHub Pages (`https://tjreed15.github.io/puppy-chow/`), and calls `email-issue.yml`, which waits for the page to go live and emails the subscriber list from the personal Gmail account. Recipients live in a repo secret, never in this public repo.

The workflow refuses to publish if `docs/index.html` wasn't updated, so don't skip that step in section 4.

## 7. Dry runs and window overrides

The prompt may include a window override (use those dates instead of section 0's) or say DRY RUN (write to `docs/preview/index.html`, leave `docs/index.html` alone). Follow the prompt.

## 8. Finish

End the run with a short summary: issue URL, item counts per section, critic results (verified count, fixes made), and anything blocked.
