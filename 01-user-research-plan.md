# Reframe Onboarding — User Research Plan

**Author:** Iris Yan · **Date:** 2026-09-11 · **Status:** Draft v2 (24-hour constraint)
**Constraint:** 24 hours total for the whole challenge. Secondary data only — no primary participant research.

---

## 0. What the constraint changes

The deliverable is still a prototype, so research gets a hard budget of **4 hours**, not three days. Within that, the honest trade is: I lose the ability to watch a real person hesitate on a real screen, and I compensate with **volume and triangulation**. Instead of 5 opinions I code 500 of them, and I only carry forward a finding that shows up in at least two independent sources.

Two things I refuse to fake: I will not present secondary findings as if they were interviews, and I will not invent personas. What I will do is state the limitation plainly and pair every problem with the specific user test I would run to validate it. Naming what you could not do is stronger than pretending you did it.

## 1. Context

Reframe is a neuroscience-based alcohol reduction app (~$99.99/yr, 7-day free trial, 4.8★ on the App Store). Onboarding is the highest-leverage surface: it is where someone decides whether this app understands their relationship with alcohol, and it is where the paywall sits.

Two public signals give me a starting hypothesis rather than a blank page. Critical reviews cluster around trial and pricing surprises more than around the product itself. And a prior Reframe redesign case study reports users saying onboarding felt like taking a survey for the company rather than getting help.

This category also carries a distinct emotional load. A new user may be ambivalent, ashamed, or not ready to accept a label. Onboarding must collect enough to personalize without feeling like an intake form or a judgment.

## 2. Research goal

> Understand what a new user needs to feel understood, safe, and motivated in their first 10 minutes with Reframe — and where the current onboarding loses them — so I can identify three high-leverage problems to solve.

### Research questions

Each question is now tagged with the source that can actually answer it in 24 hours. A question no available source can answer is a question I should not pretend to answer.

| # | Question | Answerable by |
|---|---|---|
| RQ1 | What brings someone to download an alcohol app on the day they download it? | Reddit, review verbatims |
| RQ2 | Which onboarding questions feel caring versus intrusive or judgmental? | Own walkthrough + Reddit + competitor comparison |
| RQ3 | Where does the effort-to-reward ratio break down? | Own walkthrough, screen-by-screen count |
| RQ4 | Is the personalization legible — does a user see their answers reflected back? | Own walkthrough + reviews mentioning "generic" |
| RQ5 | At what point is someone willing to start a trial, and what has to be true by then? | Review mining on pricing/trial, competitor paywall placement |
| RQ6 | What do people say about the first session specifically, versus the app overall? | Filtered review coding |

### Out of scope

Post-onboarding daily use, coach quality, the content library, retention past day one, billing operations. Named so the scope stays defensible.

## 3. Methods — four passes in 4 hours

### Pass 1 — Own the flow: cold walkthrough (45 min) · *primary qualitative source*

Fresh install of Reframe. I record my screen and narrate as I go, then do the same for the web signup flow if one exists.

What I capture, screen by screen:
- Screen count, question count, and time to complete
- What each screen asks for, and whether it is used later
- Tone and framing of the copy
- The exact screen where the paywall appears and what has been given before it
- Whether my answers visibly change anything downstream
- Every moment I hesitate, re-read, or want to skip

Output: an annotated flow map with a timestamp per screen. This is the only place I see the real artifact rather than talk about it, so it anchors everything else.

A note on rigor: I am not a representative user, and my own walkthrough is a heuristic evaluation, not a usability test. I will label it as such and use it to generate hypotheses that the review data confirms or kills.

### Pass 2 — Review mining at volume (90 min) · *primary quantitative source*

This is where the comprehensiveness comes from. Target: **500–800 reviews scraped, ~150 onboarding-relevant reviews hand-coded.**

| Source | Method | Target N |
|---|---|---|
| Apple App Store | Public RSS JSON endpoint, 10 pages × 50 | ~500 |
| Google Play | `google-play-scraper` npm/py package, sorted newest and by rating | ~200 |
| Trustpilot | Paginated HTML parse | ~100 |

**Filter, then code.** Keyword-filter for first-session language: `sign up`, `signed up`, `onboarding`, `quiz`, `questions`, `trial`, `charged`, `cancel`, `first day`, `downloaded`, `too many`, `generic`, `deleted`. That cuts several hundred reviews to a readable set.

**Coding scheme** — every filtered review gets one or more tags:

| Code | Meaning |
|---|---|
| `LENGTH` | Onboarding too long / too many questions |
| `TONE` | Judgmental, clinical, shaming, or infantilizing language |
| `PAYWALL_TIMING` | Paywall arrived too early or before value |
| `PRICE_SURPRISE` | Unexpected charge, unclear trial terms, cancellation trouble |
| `GENERIC` | Personalization not felt; content same for everyone |
| `VALUE_UNCLEAR` | Did not understand what the app does or would do for them |
| `TRUST` | Credibility, science claims, data privacy |
| `FIRST_WIN` | Positive: something useful happened early |
| `EMOTIONAL_FIT` | Felt seen, or felt like the wrong fit for their drinking |

**Quantitative output:** code frequency overall, frequency within 1–2★ only, and trend over time (are complaints from 2026 different from 2023?). Rating distribution and volume by month for baseline context.

**Qualitative output:** a quote bank, 3–5 verbatims per code, with source and star rating attached so nothing is unattributable.

The star rating is a free severity proxy. A `LENGTH` complaint inside a 5★ review is an annoyance. The same complaint inside a 1★ review with "deleted it" is a churn event.

### Pass 3 — Community threads (45 min) · *the "why" behind the ratings*

Reviews tell you what broke. Reddit tells you what people were hoping for. Search r/stopdrinking, r/alcoholism, r/dryalcoholics, r/Sobriety for Reframe mentions and for app-shopping threads generally.

I am reading for three things reviews rarely give me:
1. The trigger moment. What happened the day they decided to do something.
2. Their own vocabulary for the goal. "Cut back," "take a break," "moderate," "quit." That vocabulary should show up in the redesigned copy.
3. Objections to the category itself, including people who tried and abandoned apps without ever leaving a review. This is the closest available proxy for the silent churned user.

Target: ~25 substantive posts or comments, pulled into the same quote bank.

### Pass 4 — Competitive onboarding teardown (60 min) · *the solution space*

Walk and record the full onboarding of four competitors, coded on one consistent frame.

| App | Why it's in the set |
|---|---|
| Sunnyside | Direct competitor, moderation-first framing |
| Cutback Coach | Direct competitor, coaching-led |
| Noom | Adjacent, a long quiz that people finish anyway |
| Finch | Adjacent, low-pressure emotional tone, no shame framing |

Coded per app: screen count, time to first value, paywall position as a fraction of total flow, what is asked before versus after value is given, how personalization is revealed, and tone of the hardest question.

Noom earns its slot specifically because its quiz is longer than Reframe's and people still complete it. If length alone were the problem, Noom would fail. That comparison should stop me from proposing "make it shorter" as a lazy answer.

Where the app store blocks a full walkthrough behind an account, I fall back to published flow captures on Mobbin, Page Flows, and UX Archive.

## 4. Synthesis (45 min)

1. Dump every coded review, Reddit quote, and walkthrough note onto one board.
2. Affinity cluster into themes.
3. Apply the **triangulation rule**: a theme is only promoted to a problem if it appears in **two or more independent sources** — for example, my walkthrough plus review codes, or review codes plus Reddit. Anything single-sourced goes into an "unvalidated hypotheses" appendix rather than being quietly dropped.
4. Prioritize with **frequency × severity × business impact**, cross-checked against effort.
5. Write three problem statements, each with a goal and a metric.

## 5. Success metrics

Two layers. The first says whether the research held up under the time constraint. The second is what the design solutions will be judged against.

### Research-quality signals

| Signal | Target |
|---|---|
| Reviews scraped | ≥ 500 |
| Onboarding-relevant reviews hand-coded | ≥ 150 |
| Community posts analyzed | ≥ 25 |
| Competitor flows torn down | 4 |
| Themes surviving the two-source triangulation rule | ≥ 3 |
| Problems traceable to a named product metric | 100% |

### Product metrics the three problems will be framed against

**Primary — Onboarding completion rate.** Share of app-opens that reach the end of onboarding. The clearest measure of whether the flow loses people.

**Secondary:**
- **Time to first value** — seconds from open to the first moment the app gives something back rather than only taking.
- **Step-level drop-off** — completion per screen, to locate the leak rather than merely detect it.
- **Trial start rate** and **trial-to-paid conversion** — the commercial consequence.
- **Day-1 and Day-7 return rate** — proof that a faster onboarding did not produce shallower commitment.
- **Perceived-understanding score** — one post-onboarding pulse question, "How well does Reframe understand your goal?" (1–5). Catches the emotional outcome funnel numbers miss.

**Guardrail.** Completion must not rise at the expense of Day-7 return. Cutting questions is easy; cutting the ones that make personalization work is the trap, and the Noom comparison is the evidence that length is not the real variable.

I have no access to Reframe's actual funnel. Every number above is framed as **what I would instrument and the baseline I would ask for on day one**, not as a measured result.

## 6. Timeline within the 24 hours

| Hours | Phase | Output |
|---|---|---|
| 0.0–0.75 | Cold walkthrough of Reframe | Annotated flow map |
| 0.75–2.25 | Review scrape + coding | Coded dataset, frequency table, quote bank |
| 2.25–3.0 | Community threads | Trigger moments, user vocabulary |
| 3.0–4.0 | Competitive teardown | Comparison matrix |
| 4.0–4.75 | Synthesis and prioritization | 3 problem statements with goals + metrics |
| 4.75–24 | Ideation → concept selection → prototype → deck | Challenge deliverable |

Research is capped at 5 hours including synthesis. If the scrape runs long I cut Pass 3 first, because Pass 2 covers some of the same ground at higher volume. Passes 1 and 2 are non-negotiable.

## 7. Ethics & data handling

- All data is publicly posted. No scraping behind a login, no private messages, no DMs to users.
- Rate-limit requests and respect each site's terms. This is read-only public data at modest volume.
- Anonymize every verbatim in the deliverable. No usernames, no profile links. Quote as "1★ review, Aug 2026" or "r/stopdrinking, 2026."
- No diagnosis, no clinical claims, no advice. I am a designer.
- If the deck quotes anyone in visible distress, paraphrase rather than reproduce.

## 8. Limitations — stated up front in the deliverable

Writing these down is part of the method, not an apology.

1. **No primary research.** No user was observed using the product. Review and forum data is self-selected toward strong opinions, positive and negative alike.
2. **Survivorship bias.** People who abandon onboarding in the first 60 seconds rarely write a review. The most important failure mode is the least visible one, and Reddit only partly covers it.
3. **No funnel data.** Drop-off is inferred from complaint volume, not measured.
4. **Heuristic evaluation, not usability testing.** My own walkthrough reflects one designer's reaction.
5. **Recency skew.** The app changes; some reviews describe an onboarding that no longer exists. Mitigated by weighting the last 12 months and coding trend over time.

**What I would do next with a week:** 6 moderated think-aloud sessions on the current flow plus the prototype, recruited from people who abandoned a drinking app in the last 12 months, plus an unmoderated first-click test at n=30 to size the drop-off points I could only infer.

---

## Sources

- [Reframe App Review 2026 — ChoosingTherapy](https://www.choosingtherapy.com/reframe-app-review/)
- [Reframe Drinking App Review — Oar Health](https://www.oarhealth.com/alcohol-use-disorder/treatment/reframe-drinking-app-review)
- [Reframe Trustpilot reviews](https://www.trustpilot.com/review/reframeapp.com)
- [Reframe app review — Healthline](https://www.healthline.com/health/mental-health/reframe-app-review)
- [Reframe Application Redesign — Bhanu Prathap (prior case study)](https://www.bhanuprathap.com/work/reframe-application-redesign)
- [Reframe — Sun Paik (prior case study)](https://www.sunpaik.com/reframe)
- [Reframe App official site](https://www.joinreframeapp.com/)
