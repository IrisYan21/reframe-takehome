# Pass 2 — Where the first session breaks

**n = 3,164 reviews** · App Store + Google Play + Trustpilot · 2020-06 → 2026-09 · whole corpus coded

## 1. The flow breaks at three gates, all inside the first session

**48% of every 1–2★ review in the corpus names one of them.** Nothing else in the negative set comes close.

| Gate | Where it sits | Share of 1–2★ | Mean ★ | What they say |
| --- | --- | ---: | ---: | --- |
| **Can't get in** | Before the survey — account creation, verification code, crash, stuck plan-generation screen | **10%** | 2.13 | *"Can’t even get started… I still never received the confirmation code"* |
| **Paid in effort, handed a bill** | At the paywall | **8%** | 1.36 | *"a long and detailed survey about their personal lives before you tell them an expensive, $120 subscription is required"* |
| **Charged for a trial they thought was free** | At / after trial conversion | **33%** | 1.23 | *"I had no idea if I didn’t cancel my free trial subscription in time I would be charged for a WHOLE YEAR"* |

**Two supporting facts.** `FIRST_WIN` appears in **4 of 3,164** reviews — nothing in the free portion is ever remembered as valuable. And of the 37 reviews that describe the intake survey, **28 are 1–2★ and none are positive.**

**Diagnosis.** The break is sequence, not content. Users price the survey as a payment — *"sunk cost"*, *"waste of my morning"* — and the first thing returned for it is a price. The things the product is loved for (community, meetings, the science) all sit behind that wall. Gate 3's volume is downstream: the trial is started at the paywall, at minute 12, by someone fatigued and already invested.

## 2. Pass 1 hypotheses — verdicts

| # | Hypothesis | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | **Too long to finish.** 35 questions, 6 sections, progress bar shows position inside a section only | **Confirmed — but length is not the variable** | `LENGTH` = 38 reviews, only 1.2%. **21 of those 38 also carry `PAYWALL_TIMING`**, mean ★ 1.24. Nobody complains the survey is long; they complain it was long *and then they were billed*. A shorter survey ending at the same paywall moves this less than expected. |
| 2 | **Heavy to read.** Up to 10 sentence-length options per screen, scroll-to-Submit, 5 identical rating screens in a row | **Not testable in this source — neither confirmed nor killed** | Zero reviews discuss per-screen text density. Reviews record outcomes, not micro-friction. Do not carry forward as evidenced. Needs a moderated usability session. |
| 3 | **Answers don't carry forward.** 14 drinks set pre-paywall; tracker re-asks and derives 19 | **Confirmed — a product defect, not a perception** | `GENERIC` = 29 reviews describing the same failure from outside: *"Lost all survey data once app purchased"* (2★); *"had to go through the questionnaire all over again"* (1★); and from a **paying 4★**: *"the messages are generic, rather than being tailored based on the data the user inputs. For example, I set my goal at 15 drinks…"* |
| 4 | **The plan reveal is swamped by the price.** 22s of personalization, most concrete output 4s before the paywall | **Confirmed — and it is the headline** | `PAYWALL_TIMING` = 8% of 1–2★, mean ★ 1.36, the second-lowest of any code. The mechanism appears verbatim: *"The first 10 minutes seem very promising… You gain a sense of security with the way it navigates your mind. At the end of all of that, you’ll feel like you got the help you wanted until they ask you for $100 a month."* (1★). The survey does build trust. It is spent entirely on conversion, banked as nothing. |

**One finding Pass 1 could not see:** Gate 1 was not in the hypothesis set. `SIGNUP_BREAK` is the fastest-rising code in the corpus — **14% of 2026's 1–2★ reviews**, up from 6% in 2024 — and its mean ★ of 2.13 says these are people who wanted the product and were locked out. It is the only item here fixable without a design decision.

**Read with one caveat:** people who abandoned mid-survey have no account and no charge, so they rarely review. This channel under-counts hypothesis 1 by construction. Reddit (Pass 3) is the only available proxy for them.
