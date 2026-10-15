## Plan Card — puppy-chow (monthly dog-behavior newsletter, pilot issue)
Date: 2026-10-15

**Goal** (one sentence): Produce a single October 2026 issue (window 2026-09-15 → 2026-10-15) of a research + policy + local-news digest for a San Diego shelter dog trainer, published as a private Claude HTML Artifact, with every claim linked to the source it came from.

**Reader**: TJ — dog trainer at a San Diego shelter. Write for a practitioner: each research item ends with a "what this changes on the floor" line. No explaining basics (LIMA, cortisol, LOS).

**Editorial stance**: Take no side in the training-methods debate. Report findings as stated; explicitly call out bias — funding/conflicts of interest, small n, no control, owner-reported outcomes, advocacy-org framing (both AKC-side and welfare-org-side), press-release spin vs. the paper.

**Initial success criteria**:
- Zero hallucinations: every factual claim carries an inline link to the exact source it was taken from; a fresh-context critic opens every link and confirms the claim appears there. Any unverifiable claim is cut, not softened.
- Every item is dated inside the 30-day window (or explicitly labeled as context, e.g. "signed Sept 30, effective Jan 1, 2027").
- Coverage: ≥4 research items (≥2 shelter/rescue-specific), ≥1 CA/SD legal item, ≥1 SD local item — or an explicit "nothing found this month, here's what we checked" for that section.
- Each research item has a bias/limitations note.
- TJ would forward it to a coworker unedited.

**Non-goals**:
- Recurring schedule / cron / cloud routine (decided after pilot passes).
- Email delivery, mailing list, subscriber management, hosting.
- Taking a position on training methodology.
- Coverage outside CA (except research, which is global).

**Initial stream decomposition**:
1. Research — PubMed date-bounded queries (shelter dogs; kennel stress/enrichment/LOS; adoption/returns/assessment/training methods) + journal recent-article pages (AABS, J Vet Behav, Animal Cognition, Animals, Frontiers Vet Sci, IAABC Journal). Shortlist → read abstracts/full text → distill. — verifier: each item links to DOI/PubMed page; critic confirms stats/quotes match source.
2. CA legislation — governor's 2026 signed/vetoed lists (deadline was Sept 30) filtered for animal/dog/shelter bills; verify each on leginfo; note effective dates. — verifier: leginfo link per bill with status matching.
3. SD local — SDHS news center, County Animal Services / County News Center, City of SD + County Board agendas, local outlets (KPBS, Times of SD, 10News, Fox5, Union-Tribune). — verifier: dated article/agenda link per item.
4. Assemble — HTML Artifact: TL;DR top 3, Research, Law, Local, "What we checked" footer listing sources searched. — verifier: critic agent pass against this card; link check.

**Depends on**: nothing external (WebSearch/WebFetch + Artifact tool only).

**Known unknowns / residual risks**:
- Paywalled papers → distill from abstract only; label as such.
- 30-day window may leave research thin → fine; say so rather than pad with out-of-window items.
- 2026 CA bill outcomes not yet verified by prelim research.
- Current SDHS / County contract status unverified.
- Press coverage of studies often misstates findings — always trace to the paper.

**Reference / prior art**:
- Companion Animal Psychology (Zazie Todd) — owner-facing research translation
- IAABC Journal (quarterly) — https://journal.iaabcfoundation.org/
- Pet Professional Guild — Pet Training Science Alliance
- Gap: none combine shelter-floor research + CA/SD policy + SD local news.
