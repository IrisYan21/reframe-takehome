# Pass 4: Onboarding comparison table

Source: `*_onboarding_screens.csv` (one per app). Reframe is included as the baseline.

| Metric | Reframe | Cutback | Finch | Noom | Sunnyside |
|---|---|---|---|---|---|
| **1. Onboarding screens before paywall** | 48 | **15** | 30 | 89 | 22 |
| **2. Questions** | 35 | **9** | 16 (+6 pet setup) | 49 | 10 |
| **3. First value, screen #** | 35 (8-week estimate) | 11 (savings estimate on commitment card) | **3** (pet hatches); plan at 30 | 26 (weight projection) | 17 (14 → 9 drinks projection) |
| **4. Paywall, screen #** | 49 | **16** | 31 | 90 | 23 |
| **5. Supportive language** | ◐ | ✅ | ✅ | ✅ | ✅ |
| **6. Survey explanation** | ❌ | ✅ | ◐ | ✅ | ✅ |
| **7. Personalization perception** | 3 | 4 | 2 | **5** | 3 |
| **8. Value perception** | 3 | 4 | 3 | **5** | 3 |
| **9. Price–service match** | 2 | 2 | 1 | **5** | 4 |
| **Pros** | Strong research and social-proof framing; shows year-ahead outcomes ($780 saved, calories, REM) before the paywall; 200% money-back promise | Shortest path to a real plan; every question says what it's used for; helpline and safety note built in; core plan is free | Pet hatches 13s in, an instant emotional reward; no account needed; shame-free wording; free tier stated up front | Long quiz but gives something back every few questions (lessons, knowledge checks, humour); goal date moves earlier as you answer; paywall restates your goal | Very short quiz; projection built from your own week; account is asked only after value; tiers differ by level of support; results guarantee |
| **Cons** | Account wall at screen 4; ~35 questions with no reason given; many answers (sleep, family, eating) aren't visibly reflected back; paywall is about trial length and billing, not outcomes | Paywall sells convenience features (widgets, Siri, room décor), not outcomes; plans differ only by billing period; currency mismatch ($ vs ¥) | Sensitive questions (depression, body image, fear of failure) lead only to generic micro-goals; paywall is all discount pressure ("50% OFF", "expires when you exit"), no feature or outcome shown | Two permission prompts in the first 5s; account before the quiz; very long (~11 min to paywall); fake-urgency 15-min countdown | 4-step account (incl. phone and SMS code) just before the paywall; before paying, only a group-average projection; the real plan is locked behind payment; guilt-trip popup when you decline messaging |

## How each metric was scored

- **Screen #** counts distinct screens: iOS home screen, splash, loaders, and extra states of the same screen (typed, scrolled, selected, went back) are left out. So the numbers are lower than the CSV row numbers. CSV rows for the paywall: Reframe 57, Cutback 23, Finch 40, Noom 123, Sunnyside 43.
- **Questions** counts answer screens in the quiz. It leaves out account fields (name, email, phone) and permission prompts. Noom's count includes 3 questions asked inside the plan-building loader, and Reframe's includes 1.
- **First value** is the first screen that gives the user something back built from their own answers (a projection, estimate, plan, or reward). Reframe's live spend total inside the drinks slider (CSV row 15) doesn't count, because it sits inside a question.
- **Supportive language:** ✅ = reassuring or non-judgmental wording on the questions themselves. ◐ = reassurance appears only on separate cards between questions.
- **Survey explanation:** ✅ = questions say why they're asked or how the answer is used. ◐ = only a generic "helps us personalize" line.
- **Personalization perception (1–5):** how clearly your own answers show up in what's shown back to you before the paywall.
- **Value perception (1–5):** how much real, usable benefit you've received or can clearly see by the time you reach the paywall.
- **Price–service match (1–5):** whether the price screen ties the plan to an outcome or service level you'd get, rather than just a billing period or discount.
