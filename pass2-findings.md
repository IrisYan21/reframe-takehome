# Pass 2 — Review mining at volume: findings

**Method.** 3,164 deduplicated public reviews scraped on 2026-09-11 from the Apple App Store (6 storefronts, 2 sort orders, 2020-06 to 2026-09), Google Play (3 sort orders, 2023-06 to 2026-09) and Trustpilot (reframeapp.com, 2021-05 to 2026-09). Every review in the corpus was machine-coded against the nine-code scheme from the research plan plus one emergent code. All 277 negative reviews that survived a first-session keyword filter were read by hand, and the coding rules were rewritten from that reading rather than from prior assumptions. Every hit in the small codes was then hand-audited for precision.

**Files.** `data/coded_reviews.csv` is the coded corpus. `pass2-frequency-tables.md` holds the counts. `pass2-quote-bank.md` holds 58 attributed verbatims.

---

## What this source can and cannot see

Three limits, stated up front, because they change how the numbers should be read.

**Survivorship.** People who abandon mid-survey almost never write a review. They have no account, no charge and no relationship with the product. The review channel measures what happened to people who got far enough to feel wronged, which systematically under-counts the failure mode Pass 1 was most worried about.

**Channel skew.** App store reviews are where billing disputes get filed. That inflates `PRICE_SURPRISE` relative to its true share of first-session experience, and deflates everything that produces a shrug rather than a charge.

**Recency over-sampling.** Both scrapers return recent reviews preferentially, so the year-on-year decline in mean rating is partly an artifact. Within-year code shares are the safer trend signal.

---

## Finding 1 — Length is never the complaint on its own

`LENGTH` appears in 38 reviews, 1.2% of the corpus. On the face of it, Pass 1's headline worry looks small.

It is not small, it is misread. **21 of those 38 reviews also carry `PAYWALL_TIMING`**, and the mean star rating of a `LENGTH` review is **1.24** — the second-lowest of any code. Nobody writes in to say the survey was long. They write in to say the survey was long *and then they were asked for money*. The two ideas arrive inside one sentence, over and over, across all three platforms and five years.

> Tell us the price before making someone fill out a 1 hour questionnaire
> — **1★**, App Store, 2026-05

> intentionally beginning with a very long questionnaire to draw you in and create sunk cost before eventually revealing expensive subscription requirement
> — **1★**, Google Play, 2026-07

That second review names the mechanism without being asked to. The survey is not experienced as effort, it is experienced as investment. Investment creates an expectation of return, and the return is a price tag.

**Verdict on Pass 1 Finding 1: confirmed, and reframed.** Perceived length does drive abandonment, but length is not the independent variable. Unreciprocated length is. A shorter survey that still ended at a paywall would move this number less than the same survey ending in something free and useful.

**Verdict on Pass 1 Finding 5: confirmed, and it is the headline.** `PAYWALL_TIMING` carries a mean rating of 1.36 and appears in 8.1% of all 1–2★ reviews. This was the question Pass 1 said would decide the report, and the data answers it: complaints cluster *at* the paywall, not before it.

---

## Finding 2 — Nobody has ever praised the intake survey

37 reviews in 3,164 reference the intake questions in a first-session context. **28 of them are 1–2★. Not one review in the corpus praises the survey.**

The closest thing to a positive mention is a 5★ review that criticises it anyway:

> I was very hesitant about this app because after all of the questions it makes you sign up for a subscription. After I declined I went on my olde drunken merry way until about a week later I was looking for a way out again.
> — **5★**, App Store, 2023-02

That person came back a week later and became a paying, satisfied customer. They are the only recovered abandoner in the corpus, and they recovered by accident, through a discount email. Everyone else who bounced at that screen is invisible here.

The survey is a pure cost centre in user memory. It is the longest single stretch of the first session and it generates no goodwill at all.

---

## Finding 3 — A tenth of angry users never reached the survey

This is the emergent code, and it was not in the research plan.

`SIGNUP_BREAK` — account creation, login, verification codes, crashes and stuck loading screens during the first session — appears in **143 reviews, 9.7% of all 1–2★ reviews, and 14% of 2026's 1–2★ reviews**. That is the fastest-rising code in the corpus and in 2026 it is second only to billing.

> Can’t even get started with this app. I tried creating an account, but after waiting over 30 minutes, I still never received the confirmation code.
> — **1★**, App Store, 2026-06

> Tried multiple times to get started, but the app would freeze on "creating a personalized plan" every time.
> — **1★**, Google Play, 2024-10

The plan-generation screen — the persuasion moment Pass 1 flagged at 11:38 — is a named failure point in the reviews. Several people describe the survey completing and the plan never arriving.

Its mean rating is 2.13, notably higher than the paywall codes, because many of these people liked the product and were just locked out. That makes it the cheapest win in the set: it is a reliability problem wearing an onboarding costume, and fixing it recovers users who already wanted to pay.

---

## Finding 4 — The personalization contradiction is real and users can see it

`GENERIC` is small at 29 reviews, but its content matches the Pass 1 hypothesis almost exactly, including the specific mechanism.

> I poured my heart out during the intake questions. Just to be met with, “We are sorry you feel this way. How can we help?”
> — **1★**, App Store, 2026-06

> Filled in all the questionnaire online, signed up then installed the app and after logging in had to go through the questionnaire all over again.
> — **1★**, Google Play, 2025-12

> Lost all survey data once app purchased
> — **2★**, Google Play, 2026-05

> the messages are generic, rather than being tailored based on the data the user inputs. For example, I set my goal at 15 drinks…
> — **4★**, App Store, 2022-09

Pass 1 recorded a 14-drinks answer at 2:53 that did not pre-fill the tracker at 23:31. These reviews describe the same class of failure from the outside: answers given before payment do not survive into the product. The 4★ review is the most damaging of the four, because it comes from someone who stayed.

**Verdict on Pass 1 Finding 3: confirmed.** It is a product problem, not a perception problem.

---

## Finding 5 — Billing is louder than everything else combined, and it is the same wound

`PRICE_SURPRISE` appears in **32.6% of all 1–2★ reviews** with a mean rating of 1.23. It is three times the size of every onboarding code put together, and it has been stable at roughly a third of negative reviews since 2023.

It is tempting to call this out of scope. It is not, for two reasons.

First, most of these charges originate in the first session. The trial is started at the paywall, at minute 12, by someone who has just spent ten minutes answering personal questions. The decision is made under exactly the conditions the onboarding created: sunk cost, fatigue, and a countdown.

Second, the category makes it worse. A surprise charge is an annoyance for a productivity app. Here, reviewers consistently connect it to their own vulnerability, and that is what turns a billing complaint into a trust collapse.

> Financial hardship is one of the main causes of alcoholism, someone seeking help, does not need to be reminded they do not have money after completing a long questionnaire.
> — **1★**, Google Play, 2026-06

`TRUST` at 6.3% of 1–2★ reviews is the downstream effect. People do not just want their money back, they revise their view of what the survey was for.

> There are some very personal questions they ask you at the beginning that makes you think you’ll be able to see what this app offers (I suppose for data mining) but then nope!
> — **1★**, App Store, 2022-03

---

## Finding 6 — The tone problem is not where Pass 1 looked

Pass 1 worried about clinical and judgmental framing inside the survey. The data does not support that as a volume problem. `TONE` appears in 21 of 983 1–2★ reviews, and the negative instances are almost all about the *product* after purchase — frowning faces on the drink log, "I stayed dry today" phrasing, congratulation messages that fire after a relapse.

The opposite signal is much stronger. **99 reviews explicitly praise Reframe for being non-judgmental, shame-free or not-AA, and 95 of them are 4–5★.** Being safe to be honest with is the single most-praised attribute in the corpus.

> There are no rigid (judgmental) rules- you evolve in your own time, gently, with unconditional support
> — **5★**, App Store, 2026-01

That is the finding worth acting on. The product has a voice people love and the onboarding does not use it. The intake survey asks a person to self-classify as "heavily or binge" or "I have a dependency" with no definitions, and the one review that engages with that experience says:

> the reason for removing two stars is the question about how often I feel regrets about drinking. Choices were: always, often, somewhat often. I very rarely regret drinking, if ever. I actually enjoy drinking. So I felt the app wasn't for me, even though I would like to cut down.
> — **3★**, Google Play, 2026-03

**Verdict on Pass 1 Finding 4: weakly confirmed, low volume, high specificity.** It is rare in reviews and it should be tested directly, but when it appears it produces exactly the predicted outcome: a person who wants the product concludes the product is not for them, inside the survey, because of an answer option.

**Verdict on Pass 1 Finding 2 (reading load):** not visible in this channel. Neither confirmed nor killed. Reviews do not discuss per-screen text density. This one needs a moderated usability session and should not be carried forward as an evidenced problem.

**Verdict on Pass 1 Finding 6 (questions continue after payment):** not confirmed. Paying users complain about repeated *surveys and feedback prompts* inside the product, but not about the post-purchase check-in flows specifically. Treat as unsupported.

---

## Finding 7 — There is no first win anywhere in the free experience

`FIRST_WIN` appears in **4 reviews out of 3,164.**

The positive reviews are detailed, long and numerous, and they praise four things: the community forum, the daily zoom meetings, the neuroscience content, and the coaches. All four sit behind the paywall. Nothing a non-paying user touches in the first twelve minutes is ever remembered as valuable.

The one near-exception is instructive:

> The first 10 minutes seem very promising considering the questions it asks you. You gain a sense of security with the way it navigates your mind. At the end of all of that, you’ll feel like you got the help you wanted until they ask you for $100 a month.
> — **1★**, App Store, 2025-12

The survey does create a feeling of being taken seriously. That feeling is real, it is generated by the questions themselves, and it is currently spent entirely on the paywall conversion rather than banked as a reason to come back tomorrow.

---

## What broke the flow: the hypothesis

The first session fails in one place, and it fails because of sequence rather than content.

**A person arrives on the day they decided to do something about their drinking.** That is a high-motivation, high-vulnerability state with a short half-life. Reframe spends that state on twelve minutes of disclosure, which the person supplies willingly because disclosure feels like the beginning of help. The survey is well-made enough to deepen the feeling: reviewers describe a sense of being understood.

**Then the transaction reverses.** The first thing returned for the disclosure is a bill. Every code in the data converges on this moment. Length only hurts because of it. Trust only collapses because of it. The billing complaints that dominate the corpus are made by people who agreed to a trial in that exact state and regretted it later.

**And the product that would have justified all of it is on the other side of the wall.** The things reviewers love — the non-judgmental community, the science, the meetings — are precisely the things that would have earned the disclosure if any of them had been reachable first.

Three corollaries, each testable:

1. **The survey is a payment, not a form.** Users price it that way in their own language: "waste of my morning", "sunk cost", "wastes your time". Any redesign that shortens it without returning something at the end will move the numbers less than expected.
2. **Personalization has to be visibly spent, not just collected.** The answers already fail to carry forward into the tracker and the plan. Users notice, and noticing converts a personalization story into a data-harvesting story.
3. **A tenth of the angriest users never got that far.** Before any of the above matters, account creation, verification and plan generation have to work. This is the only finding in the set that can be fixed without a design decision.

## What I would carry into Pass 3 and Pass 4

- **Reddit (Pass 3)** is now the only available source for the silent abandoner. Reviews cannot see them. Search specifically for people who tried Reframe and stopped before paying.
- **The vocabulary gap.** Reviewers who reject the product say "I just wanted to cut back", "I wouldn't label myself an alcoholic (yet)", "grey area drinker". The survey's own options do not contain those phrases. Pass 3 should collect the real vocabulary and Pass 4 should check which competitors use it.
- **Noom's quiz** earns its slot even more now. If length is not the variable, the question for Pass 4 is what Noom returns at the end of its quiz that Reframe does not.
- **Sunnyside specifically.** One 1★ Trustpilot reviewer switched and named it. Its paywall position as a fraction of total flow is the single most useful comparative number I can collect.
