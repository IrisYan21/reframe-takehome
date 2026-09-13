# Pass 1 — Own the flow: first-hand insights

**Method.** Fresh install of Reframe on iPhone, screen recorded with narration, one continuous session on 2026-09-11. The recording runs 28:49 and covers signup through the first day of in-app activity. Every screen is timestamped in `reframe_onboarding_screens.csv` (220 screens).

**Status of this evidence.** This is a heuristic evaluation by a single non-representative user, not a usability test. n=1. Everything below is a hypothesis with a timestamp attached. Pass 2 review data confirms or kills each one; nothing here ships as a finding on its own.

---

## Baseline facts

| Measure | Value |
| --- | --- |
| Total recording | 28:49 |
| Screens before the paywall | 61 |
| Distinct questions before the paywall | 35 |
| Time from launch to paywall | 12:25 |
| Time from launch to first personalized content | 12:03 (22 s before the price) |
| Quiz sections | 6, plus 4 social-proof interstitials |
| Questions asked *after* payment | 9 (Day 1 check-in) + 4 (coping strategies) + tracker setup |

Section-by-section timing:

| Section | Start | Screens | On-screen time |
| --- | --- | --- | --- |
| Pre-signup value props | 0:00 | 3 | 21 s |
| Account creation | 0:21 | 4 | 25 s |
| About You | 0:46 | 5 | 66 s |
| Your Habits | 1:59 | 7 | 139 s |
| Your Lifestyle | 4:27 | 5 | 82 s |
| Your Patterns | 5:52 | 8 | 195 s |
| Your Journey | 9:07 | 3 | 36 s |
| Your Mindset | 9:47 | 8 | 111 s |
| Plan generation | 11:38 | 3 | 25 s |
| Plan reveal | 12:03 | 3 | 22 s |
| **Paywall** | **12:25** | 5 | 32 s |

---

## Finding 1 — The intake survey outlasts the motivation that brought me in

**What I experienced.** Twelve and a half minutes of questions before anything happened. I hit a wall somewhere in the third section: bored, tired, aware that more than half the questions were still ahead. That was the first moment I genuinely wanted to quit, and I would have if I were not evaluating the product.

**Evidence from the recording.**
- 35 questions across 6 named sections, 10:52 of continuous form-filling from 0:46 to 11:38.
- The drop-off risk point matches the recording's slowest stretch. Your Patterns alone is 8 screens and 195 s, the longest section, and it arrives at 5:52 — right at the point where I reported wanting out.
- The two longest single-screen dwells are both mid-survey: 60 s on "How would you describe your typical eating patterns?" at 5:59, and 53 s on "How often do you drink in a typical week?" at 1:59. These include narration pauses, so treat them as soft signals, not measured hesitation.

**On the progress indicator.** There is a segmented progress bar, but it resets its framing at each new section label (About You, Your Habits, Your Lifestyle, Your Patterns, Your Journey, Your Mindset). It tells me where I am inside the current section, not how much of the whole intake remains. Knowing a section is nearly done does not help when I cannot see how many sections are left.

**Hypothesis.** Perceived length, not actual length, drives abandonment here. The survey reads as open-ended because completion is unknowable from inside it.

**Confirm or kill in Pass 2.** Look for review language about signing up: "endless questions", "gave up before", "took forever". If abandonment complaints cluster before the paywall rather than at it, this is the primary problem and the paywall is secondary.

---

## Finding 2 — The reading load is heavier than the answering load

**What I experienced.** The text is tiring to read. Not the number of questions alone, but the density of each one: a heading, a sub-explanation, and then 5 to 10 long option labels, several of which are full sentences.

**Evidence from the recording.**
- Multi-select screens carry 7 to 10 options with sentence-length labels. "In the last two weeks, have you been experiencing any of these consistently?" at 5:24 lists 8 clinical-sounding items. "What influences your choice of alcoholic beverages?" at 3:23 lists 8.
- Several screens require scrolling before the Submit button is reachable, so the option list cannot be taken in at a glance. Visible in the recording at 3:23, 7:47, 8:13 and 10:24.
- Five consecutive Likert screens run from 9:48 to 10:24 in Your Mindset. Same layout, same scale, different sentence each time. The format gives no signal that any individual answer matters.

**Hypothesis.** The cost per question is reading comprehension, not decision-making. Cutting the question count without cutting per-screen text would not fix the fatigue.

**Confirm or kill in Pass 2.** Check whether reviews mention wording, confusion, or reading effort as distinct from length. Also check accessibility-adjacent complaints, which would raise severity.

---

## Finding 3 — I could not tell what any answer was buying me

**What I experienced.** No idea how any question or section would change what the product does for me. I was supplying input to a black box and asked to trust that it mattered.

**Evidence from the recording.**
- A business-attribution question sits inside the user-goal survey: "How did you hear about us?" at 1:03, second question in, before anything has been asked about drinking. It is asked for the company, not for me, and it sets the tone that these questions are extraction.
- **The clearest case of an answer not carrying forward.** At 2:53 I set my weekly consumption to 14 drinks and my weekly spend, and the app computed $224.75/month and $2,860/year. At 3:09 I set my target to 14 drinks. Then at 23:31, after payment, the tracker setup asks me to enter my drinks per day again, day by day, and derives a baseline of **19 drinks/week** and a target of **15**. The number I entered before the paywall neither pre-filled this screen nor matched its output.
- Answers do change the *next question* in three places. The intro at 4:40 references "time between jobs", the partner question at 5:03 follows "In a relationship", and "What was the longest period…?" at 8:49 switches between three follow-up versions depending on the answer. Branching exists inside the survey; what never appears is an answer shaping the *plan*.
- Only 4 of 35 questions say why they are being asked (0:46, 1:25, 2:52, 3:46).
- The four interstitials at 1:52, 4:18, 5:49 and 9:43 are the only mid-survey feedback, and none of them reflects my answers. Three are generic social proof (users, reviews, press). One at 4:18 claims "43% of our users shared similar alcohol consumption patterns", which gestures at personalization without showing what it read from me.

**Hypothesis.** The survey is positioned as personalization but functions as qualification and data capture. The 2:53 versus 23:31 contradiction is the strongest evidence I have that at least some answers do not drive downstream behavior, and it is checkable rather than felt.

**Confirm or kill in Pass 2.** Re-run the flow with deliberately extreme answers and diff the resulting plan. If the plan text is identical, this moves from hypothesis to fact and becomes the sharpest finding in the report.

---

## Finding 4 — Ambiguous options force self-diagnosis I am not qualified to do

**What I experienced.** Hard to choose between several options. Worse, on some questions I could not tell whether I was assessing myself accurately, which made me anxious about answering wrongly and slowed me down.

**Evidence from the recording.**
- Self-categorization with no defined boundaries: "How would you describe your typical drinking patterns during a regular day?" at 5:53 asks me to pick between "occasionally, usually in social settings", "regularly, but in moderate amounts", "heavily or binge", and "I have a dependency". These are clinical distinctions presented as casual self-description, with no definition of moderate or heavy.
- The mental-health screen at 5:24 asks about sadness, loss of interest and concentration in the last two weeks. That is close to a depression screener, presented without framing about what happens with the answer.
- "Have you previously tried to reduce or stop drinking alcohol?" at 8:30 mixes number of attempts ("once or twice", "multiple") with current state ("currently trying for the first time") in one list.

**Hypothesis.** Ambiguity carries an emotional cost specific to this category. For a person whose relationship with alcohol is the thing under review, an unanswerable self-assessment is not merely a UX friction. It is a moment of being asked to judge yourself and not knowing the answer.

**Confirm or kill in Pass 2.** Look for reviews expressing anxiety or defensiveness about the questions themselves, and for anything about feeling labeled or misjudged.

---

## Finding 5 — I paid the effort price for a plan and was handed a price tag

**What I experienced.** After finishing the survey I expected a tailored behavior-change plan. Instead I got a payment screen. It felt like a bait-and-switch.

**Evidence from the recording.**
- Sequence: plan-building progress at 11:38, "Iris's Plan" at 12:03, then the trial paywall at 12:25. The personalized artifact is on screen for **22 seconds** before the price appears.
- What the "plan" actually contains at 12:03 is three goal chips ("Cut back your drinking", "Get fit and feel healthier", "Improve my overall health"), a generic list of what the program includes, a money-back promise, then reviews and press logos at 12:18. None of it is derived visibly from 35 answers. It is a pitch wearing the plan's clothes.
- The plan-building screen itself is doing persuasion work: five fake-granular progress bars ("Identifying Your Triggers", "Understanding Your Motivation", "Creating Your Support Plan") with a Harvard Medical School badge pinned below them, running 11:38 to 12:03.
- One more question is inserted **into** the loading screen at 11:51 as a modal: "And lastly, how often do you drink more than you intend to?" It is a severity question, asked at the last possible moment before pricing.
- The projection screen at 12:21, "$780 saved, 111,384 empty calories, 1825 REM cycles", is the most concrete personalized output in the whole flow, and it appears 4 seconds before the paywall.

**Hypothesis.** The perceived betrayal comes from sequence, not from the existence of a paywall. Twelve minutes of disclosure built an expectation of reciprocity, and the first thing returned was a bill. A paywall at minute 2 with the same price would likely feel more honest than this one at minute 12.

**Confirm or kill in Pass 2.** This should be the loudest signal in review data if it is real. Look for "scam", "bait and switch", "makes you answer everything then wants money", and check whether these cluster in low-star reviews specifically.

---

## Finding 6 — The survey does not end at payment

**What I experienced.** Not in my original notes, but visible in the map and worth flagging: I assumed paying would end the questioning. It did not.

**Evidence from the recording.**
- A second 9-question survey, the Day 1 check-in, starts at 24:13, roughly 11 minutes after payment.
- A third 4-question flow, coping strategies, starts at 27:36.
- Tracker setup at 23:31 re-asks drinking volume day by day, as covered in Finding 3.
- By the end of the recording I have answered roughly 50 questions in total.

**Hypothesis.** Total question load is worse than the pre-paywall count suggests. Any recommendation to trim the intake survey should account for what the post-purchase flows re-ask, or the questions will simply move rather than disappear.

**Confirm or kill in Pass 2.** Check whether review complaints about questions come from paying users describing the app, not only from people describing signup.

---

## What I would take into Pass 2

Ranked by how much the answer would change the recommendation:

1. Does the plan actually vary with the answers? Directly testable, and it decides whether Finding 3 is a perception problem or a product one.
2. Do abandonment complaints cluster before the paywall or at it? Decides whether Finding 1 or Finding 5 is the headline.
3. Is the emotional cost of ambiguous self-assessment (Finding 4) visible in review language, or is it particular to me?
4. Do paying users complain about continued questioning (Finding 6)?
