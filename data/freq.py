import json,collections
R=json.load(open("data/coded_reviews.json"))
CODES=["LENGTH","PAYWALL_TIMING","PRICE_SURPRISE","SIGNUP_BREAK","GENERIC","TONE","VALUE_UNCLEAR","TRUST","EMOTIONAL_FIT_NEG","EMOTIONAL_FIT_POS","FIRST_WIN"]
def F(sub):
    c=collections.Counter()
    for r in sub:
        for k in r["codes"]: c[k]+=1
    return c,max(len(sub),1)
groups=[("All reviews",R),("1-2 star",[r for r in R if r["rating"]<=2]),("3 star",[r for r in R if r["rating"]==3]),("4-5 star",[r for r in R if r["rating"]>=4])]
print("n by group:", {g:len(s) for g,s in groups})
hdr=f"{'CODE':20}"+"".join(f"{g:>18}" for g,_ in groups); print(hdr)
data={}
for g,s in groups: data[g]=F(s)
for k in CODES:
    line=f"{k:20}"
    for g,_ in groups:
        c,n=data[g]; line+=f"{c[k]:>8} {100*c[k]/n:>7.1f}%"
    print(line)
print()
# trend by year, share of 1-2star reviews carrying each code
print("TREND — % of 1-2★ reviews in that year carrying the code")
yrs=[str(y) for y in range(2021,2027)]
print(f"{'CODE':20}"+"".join(f"{y:>9}" for y in yrs))
low=[r for r in R if r["rating"]<=2]
byyr={y:[r for r in low if r["date"][:4]==y] for y in yrs}
print(f"{'(n 1-2★)':20}"+"".join(f"{len(byyr[y]):>9}" for y in yrs))
for k in CODES:
    line=f"{k:20}"
    for y in yrs:
        s=byyr[y]; c=sum(1 for r in s if k in r["codes"]); line+=f"{(100*c/len(s) if s else 0):>8.0f}%"
    print(line)
print()
print("VOLUME & RATING BY YEAR (all)")
print(f"{'year':6}{'n':>6}{'mean★':>8}{'%1-2★':>8}")
for y in ["2020"]+yrs:
    s=[r for r in R if r["date"][:4]==y]
    if not s: continue
    print(f"{y:6}{len(s):>6}{sum(r['rating'] for r in s)/len(s):>8.2f}{100*sum(1 for r in s if r['rating']<=2)/len(s):>7.0f}%")
print()
print("BY SOURCE")
for src in ["apple","google_play","trustpilot"]:
    s=[r for r in R if r["source"]==src]
    print(f"{src:12} n={len(s):>5}  mean★={sum(r['rating'] for r in s)/len(s):.2f}  %1-2★={100*sum(1 for r in s if r['rating']<=2)/len(s):.0f}%")
