import json,collections,re
R=json.load(open("data/coded_reviews.json"))
CODES=["LENGTH","PAYWALL_TIMING","PRICE_SURPRISE","SIGNUP_BREAK","GENERIC","TONE","VALUE_UNCLEAR","TRUST","EMOTIONAL_FIT_NEG","EMOTIONAL_FIT_POS","FIRST_WIN"]
LBL={"LENGTH":"`LENGTH`","PAYWALL_TIMING":"`PAYWALL_TIMING`","PRICE_SURPRISE":"`PRICE_SURPRISE`","SIGNUP_BREAK":"`SIGNUP_BREAK` *(emergent)*","GENERIC":"`GENERIC`","TONE":"`TONE`","VALUE_UNCLEAR":"`VALUE_UNCLEAR`","TRUST":"`TRUST`","EMOTIONAL_FIT_NEG":"`EMOTIONAL_FIT` neg","EMOTIONAL_FIT_POS":"`EMOTIONAL_FIT` pos","FIRST_WIN":"`FIRST_WIN`"}
o=[]
w=o.append
w("# Pass 2 — Frequency tables\n")
w("Corpus, coding scheme and every number below are reproducible from `data/coded_reviews.csv`.\n")
w("## Corpus\n")
w("| Source | Method | Reviews | Date range | Mean ★ | % 1–2★ |")
w("| --- | --- | ---: | --- | ---: | ---: |")
for src,meth in [("apple","Public RSS JSON, 6 storefronts × 2 sorts × 10 pages"),("google_play","`google-play-scraper`, 3 sorts × 600"),("trustpilot","Paginated JSON parse, reframeapp.com")]:
    s=[r for r in R if r["source"]==src]
    w(f"| {src.replace('_',' ').title()} | {meth} | {len(s)} | {min(r['date'] for r in s)[:7]} → {max(r['date'] for r in s)[:7]} | {sum(r['rating'] for r in s)/len(s):.2f} | {100*sum(1 for r in s if r['rating']<=2)/len(s):.0f}% |")
w(f"| **Total (deduplicated)** | | **{len(R)}** | {min(r['date'] for r in R)[:7]} → {max(r['date'] for r in R)[:7]} | {sum(r['rating'] for r in R)/len(R):.2f} | {100*sum(1 for r in R if r['rating']<=2)/len(R):.0f}% |")
w("\nTarget was 500–800 scraped. Actual is 3,164 after deduplication, which let me code the whole corpus rather than a filtered sample.\n")
w("## Rating distribution\n")
w("| ★ | n | % |")
w("| --- | ---: | ---: |")
c=collections.Counter(r["rating"] for r in R)
for k in [5,4,3,2,1]: w(f"| {k}★ | {c[k]} | {100*c[k]/len(R):.1f}% |")
w("\nThe distribution is U-shaped, which is normal for app stores. Mean rating in the corpus is 3.68 against a 4.73 App Store lifetime average, because I deliberately over-sampled recent reviews and two sort orders.\n")
w("## Code frequency\n")
groups=[("All",R),("1–2★",[r for r in R if r["rating"]<=2]),("3★",[r for r in R if r["rating"]==3]),("4–5★",[r for r in R if r["rating"]>=4])]
w("| Code | All n | All % | 1–2★ n | 1–2★ % | 3★ n | 4–5★ n | Mean ★ of tagged |")
w("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
for k in CODES:
    row=[LBL[k]]
    for g,s in groups:
        n=sum(1 for r in s if k in r["codes"])
        if g=="All": row += [str(n), f"{100*n/len(s):.1f}%"]
        elif g=="1–2★": row += [str(n), f"{100*n/len(s):.1f}%"]
        else: row.append(str(n))
    tagged=[r for r in R if k in r["codes"]]
    row.append(f"{sum(r['rating'] for r in tagged)/len(tagged):.2f}")
    w("| "+" | ".join(row)+" |")
w(f"\nn = {len(R)} all, {len(groups[1][1])} at 1–2★, {len(groups[2][1])} at 3★, {len(groups[3][1])} at 4–5★. A review can carry more than one code. {sum(1 for r in R if r['codes'])} reviews carry at least one.\n")
w("Mean star of the tagged set is the severity proxy. A code whose mean sits near 1.2 is attached to churn, not to annoyance.\n")
w("## Trend over time\n")
yrs=[str(y) for y in range(2021,2027)]
low=[r for r in R if r["rating"]<=2]
byyr={y:[r for r in low if r["date"][:4]==y] for y in yrs}
w("Share of that year's 1–2★ reviews carrying each code.\n")
w("| Code | "+" | ".join(yrs)+" |")
w("| --- | "+" | ".join(["---:"]*len(yrs))+" |")
w("| *(n of 1–2★)* | "+" | ".join(str(len(byyr[y])) for y in yrs)+" |")
for k in CODES:
    w(f"| {LBL[k]} | "+" | ".join(f"{100*sum(1 for r in byyr[y] if k in r['codes'])/len(byyr[y]):.0f}%" if byyr[y] else "–" for y in yrs)+" |")
w("\n## Volume and rating by year\n")
w("| Year | n | Mean ★ | % 1–2★ |")
w("| --- | ---: | ---: | ---: |")
for y in ["2020"]+yrs:
    s=[r for r in R if r["date"][:4]==y]
    if not s: continue
    w(f"| {y} | {len(s)} | {sum(r['rating'] for r in s)/len(s):.2f} | {100*sum(1 for r in s if r['rating']<=2)/len(s):.0f}% |")
w("\n**Read this table with care.** Both scrapers return recent reviews preferentially, so 2025 and 2026 are over-represented and the apparent decline in mean rating is partly a sampling artifact. The within-year code shares in the previous table are the safer trend signal, because they are ratios inside each year rather than across years.\n")
w("## Co-occurrence\n")
w("| Pair | Overlap |")
w("| --- | --- |")
for a,b in [("LENGTH","PAYWALL_TIMING"),("PAYWALL_TIMING","PRICE_SURPRISE"),("LENGTH","GENERIC"),("SIGNUP_BREAK","PRICE_SURPRISE"),("PAYWALL_TIMING","TRUST")]:
    s=[r for r in R if a in r["codes"]]
    w(f"| `{a}` also `{b}` | {sum(1 for r in s if b in r['codes'])} of {len(s)} |")
w("")
open("pass2-frequency-tables.md","w").write("\n".join(o))
print("ok")
