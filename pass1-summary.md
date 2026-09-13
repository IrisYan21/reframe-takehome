# Pass 1 — Summary

Source: one cold walkthrough of Reframe, iPhone, 28:49 recorded with narration. Screen-level timing in `reframe_onboarding_screens.csv`. Full write-up in `pass1-first-hand-insights.md`.

Status: heuristic evaluation, n=1. Hypotheses to be confirmed or killed by Pass 2 review data, not findings in their own right.

---

## 1. Hypothesis

**Central hypothesis.** Reframe's onboarding is built to qualify and convert, not to deliver value. The intake survey works as an effort-justification device: it takes 35 questions and 12 minutes of disclosure, returns nothing that visibly depends on those answers, and cashes the accumulated investment at a paywall. The cost is paid twice — in people who quit mid-survey, and in people who reach the end and feel extracted from rather than helped.

Four sub-hypotheses, each independently testable:

| # | Sub-hypothesis | If true |
| --- | --- | --- |
| H1 | Abandonment is driven by *perceived* open-endedness, not actual length. Completion is unknowable from inside the survey. | Fix the progress model before cutting questions. |
| H2 | The per-question cost is reading comprehension, not decision-making. | Cutting question count alone will not reduce fatigue. |
| H3 | The survey is positioned as personalization but functions as data capture. At least some answers do not drive downstream behavior. | The trust problem is real, not a perception gap. |
| H4 | The sense of betrayal at the paywall comes from sequence, not from the paywall's existence. | Moving the price earlier beats discounting it. |

---

## 2. Key findings

### F1 — The intake survey outlasts the motivation that brought me in
Twelve and a half minutes of questions before anything happens. I hit a wall in the third section and would have quit if I were not evaluating the product.

- 35 distinct questions, 6 sections, continuous form-filling from 0:46 to 11:38.
- Your Patterns is the longest section (8 screens, 195 s) and starts at 5:52, matching the point where I wanted out.
- The progress bar tracks position inside the current section, not the whole intake. Section labels change six times, so finishing one reveals nothing about what remains.

### F2 — The reading load is heavier than the answering load
Density per screen, not question count, is what tires the reader.

- Multi-select screens carry 7 to 10 options with sentence-length labels (5:24, 3:23).
- Several screens require scrolling before Submit is reachable (3:23, 7:47, 8:13, 10:24).
- Five consecutive Likert screens run 9:48 to 10:24, identical in layout, giving no signal that any single answer matters.

### F3 — An answer given before the paywall did not carry forward after it
The strongest checkable evidence that the survey is not driving the product.

- At 2:53 I set weekly consumption to 14 drinks; the app computed $224.75/month and $2,860/year. At 3:09 I set my target to 14.
- At 23:31, after payment, tracker setup re-asks drinks day by day and derives a baseline of **19/week** and a target of **15**. The pre-paywall number neither pre-filled the screen nor matched its output.
- Supporting: "How did you hear about us?" is the second question at 1:03, a business-attribution question inside a user-goal survey.
- Answers do change the next question in three places (4:40, 5:03, and three versions of a follow-up at 9:07–9:33). Branching exists inside the survey; no answer visibly shapes the plan.
- Only 4 of 35 questions say why they are being asked.
- The four mid-survey interstitials (1:52, 4:18, 5:49, 9:43) are the only feedback offered, and none reflects my answers.

### F4 — Ambiguous options force self-diagnosis I am not qualified to do
Choosing was hard, and I could not tell whether I was assessing myself correctly.

- Clinical distinctions presented as casual self-description, with no definitions of "moderate" or "heavy" (5:53).
- A depression-screener-adjacent question at 5:24, asked with no framing about what the answer is used for.
- One option list mixes number of past attempts with current state (8:30).

In this category the cost is emotional, not just procedural. Being asked to judge your own drinking and not knowing the answer is a different experience from being asked to pick a shipping option.

### F5 — I paid the effort price for a plan and was handed a price tag
The expectation set by the survey is a tailored behavior-change plan. What arrives is a payment screen.

| Moment | Time |
| --- | --- |
| Plan-building progress begins | 11:38 |
| "Iris's Plan" appears | 12:03 |
| Paywall | 12:25 |

- The personalized artifact is on screen for **22 seconds** before the price.
- What the plan contains is three goal chips, a generic program description, a money-back promise, then reviews and press logos at 12:18. None of it is visibly derived from 35 answers.
- The loading screen is doing persuasion work: five granular progress bars under a Harvard Medical School badge, 11:38 to 12:03.
- A severity question is inserted into that loading screen as a modal at 11:51: "And lastly, how often do you drink more than you intend to?"
- The most concrete personalized output in the entire flow ($780 saved, 111,384 calories, 1825 REM cycles) appears at 12:21, four seconds before the paywall.

### F6 — The questioning does not stop at payment
Not in my original notes; visible in the flow map.

- Day 1 check-in: 9 questions, starting 24:13, about 11 minutes after payment.
- Coping strategies: 4 questions, starting 27:36.
- Tracker setup re-asks drinking volume at 23:31 (see F3).
- Roughly 50 questions answered across the recording.

Any recommendation to trim the intake must account for these, or the questions will move rather than disappear.

---

## What Pass 2 has to settle

Ranked by how much the answer changes the recommendation:

1. **Does the plan vary with the answers?** Directly testable by re-running with extreme inputs and diffing the output. Decides whether F3 is a perception problem or a product one.
2. **Do abandonment complaints cluster before the paywall or at it?** Decides whether F1 or F5 is the headline.
3. **Is the emotional cost of ambiguous self-assessment visible in review language,** or particular to me?
4. **Do paying users complain about continued questioning** (F6)?
