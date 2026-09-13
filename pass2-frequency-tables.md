# Pass 2 — Frequency tables

Corpus, coding scheme and every number below are reproducible from `data/coded_reviews.csv`.

## Corpus

| Source | Method | Reviews | Date range | Mean ★ | % 1–2★ |
| --- | --- | ---: | --- | ---: | ---: |
| Apple | Public RSS JSON, 6 storefronts × 2 sorts × 10 pages | 2044 | 2020-06 → 2026-09 | 3.85 | 27% |
| Google Play | `google-play-scraper`, 3 sorts × 600 | 951 | 2023-06 → 2026-09 | 3.30 | 39% |
| Trustpilot | Paginated JSON parse, reframeapp.com | 169 | 2021-05 → 2026-09 | 3.60 | 34% |
| **Total (deduplicated)** | | **3164** | 2020-06 → 2026-09 | 3.68 | 31% |

Target was 500–800 scraped. Actual is 3,164 after deduplication, which let me code the whole corpus rather than a filtered sample.

## Rating distribution

| ★ | n | % |
| --- | ---: | ---: |
| 5★ | 1912 | 60.4% |
| 4★ | 155 | 4.9% |
| 3★ | 114 | 3.6% |
| 2★ | 124 | 3.9% |
| 1★ | 859 | 27.1% |

The distribution is U-shaped, which is normal for app stores. Mean rating in the corpus is 3.68 against a 4.73 App Store lifetime average, because I deliberately over-sampled recent reviews and two sort orders.

## Code frequency

| Code | All n | All % | 1–2★ n | 1–2★ % | 3★ n | 4–5★ n | Mean ★ of tagged |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `LENGTH` | 38 | 1.2% | 37 | 3.8% | 0 | 1 | 1.24 |
| `PAYWALL_TIMING` | 90 | 2.8% | 80 | 8.1% | 7 | 3 | 1.36 |
| `PRICE_SURPRISE` | 339 | 10.7% | 320 | 32.6% | 5 | 14 | 1.23 |
| `SIGNUP_BREAK` *(emergent)* | 143 | 4.5% | 95 | 9.7% | 13 | 35 | 2.13 |
| `GENERIC` | 29 | 0.9% | 22 | 2.2% | 0 | 7 | 2.07 |
| `TONE` | 78 | 2.5% | 21 | 2.1% | 4 | 53 | 3.83 |
| `VALUE_UNCLEAR` | 10 | 0.3% | 10 | 1.0% | 0 | 0 | 1.20 |
| `TRUST` | 72 | 2.3% | 62 | 6.3% | 1 | 9 | 1.57 |
| `EMOTIONAL_FIT` neg | 29 | 0.9% | 21 | 2.1% | 5 | 3 | 1.97 |
| `EMOTIONAL_FIT` pos | 99 | 3.1% | 1 | 0.1% | 3 | 95 | 4.89 |
| `FIRST_WIN` | 4 | 0.1% | 1 | 0.1% | 0 | 3 | 4.00 |

n = 3164 all, 983 at 1–2★, 114 at 3★, 2067 at 4–5★. A review can carry more than one code. 777 reviews carry at least one.

Mean star of the tagged set is the severity proxy. A code whose mean sits near 1.2 is attached to churn, not to annoyance.

## Trend over time

Share of that year's 1–2★ reviews carrying each code.

| Code | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| *(n of 1–2★)* | 16 | 71 | 104 | 158 | 248 | 386 |
| `LENGTH` | 0% | 0% | 0% | 5% | 4% | 5% |
| `PAYWALL_TIMING` | 25% | 13% | 5% | 7% | 10% | 7% |
| `PRICE_SURPRISE` | 19% | 20% | 38% | 33% | 33% | 34% |
| `SIGNUP_BREAK` *(emergent)* | 6% | 8% | 10% | 6% | 6% | 14% |
| `GENERIC` | 0% | 4% | 1% | 1% | 3% | 2% |
| `TONE` | 0% | 3% | 5% | 3% | 0% | 2% |
| `VALUE_UNCLEAR` | 0% | 3% | 0% | 1% | 1% | 1% |
| `TRUST` | 12% | 7% | 4% | 7% | 6% | 7% |
| `EMOTIONAL_FIT` neg | 6% | 3% | 5% | 1% | 0% | 3% |
| `EMOTIONAL_FIT` pos | 0% | 1% | 0% | 0% | 0% | 0% |
| `FIRST_WIN` | 0% | 0% | 0% | 0% | 0% | 0% |

## Volume and rating by year

| Year | n | Mean ★ | % 1–2★ |
| --- | ---: | ---: | ---: |
| 2020 | 7 | 5.00 | 0% |
| 2021 | 80 | 4.16 | 20% |
| 2022 | 401 | 4.22 | 18% |
| 2023 | 481 | 4.05 | 22% |
| 2024 | 649 | 3.92 | 24% |
| 2025 | 679 | 3.46 | 37% |
| 2026 | 867 | 3.14 | 45% |

**Read this table with care.** Both scrapers return recent reviews preferentially, so 2025 and 2026 are over-represented and the apparent decline in mean rating is partly a sampling artifact. The within-year code shares in the previous table are the safer trend signal, because they are ratios inside each year rather than across years.

## Co-occurrence

| Pair | Overlap |
| --- | --- |
| `LENGTH` also `PAYWALL_TIMING` | 21 of 38 |
| `PAYWALL_TIMING` also `PRICE_SURPRISE` | 17 of 90 |
| `LENGTH` also `GENERIC` | 4 of 38 |
| `SIGNUP_BREAK` also `PRICE_SURPRISE` | 8 of 143 |
| `PAYWALL_TIMING` also `TRUST` | 6 of 90 |
