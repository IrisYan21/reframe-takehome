import json, subprocess, time, sys
APP=1485756576
out={}
countries=["us","gb","ca","au","ie","nz"]
sorts=["mostrecent","mosthelpful"]
for c in countries:
    for s in sorts:
        for p in range(1,11):
            url=f"https://itunes.apple.com/{c}/rss/customerreviews/page={p}/id={APP}/sortby={s}/json"
            try:
                raw=subprocess.run(["curl","-sS","-A","Mozilla/5.0","--max-time","25",url],capture_output=True).stdout
                d=json.loads(raw)
            except Exception as e:
                print("ERR",c,s,p,e,file=sys.stderr); break
            entries=d.get("feed",{}).get("entry",[])
            if isinstance(entries,dict): entries=[entries]
            if not entries: break
            n=0
            for e in entries:
                if "im:rating" not in e: continue
                rid=e["id"]["label"]
                if rid in out: continue
                out[rid]={
                 "id":rid,"source":"apple","country":c,
                 "rating":int(e["im:rating"]["label"]),
                 "title":e["title"]["label"],
                 "text":e["content"]["label"],
                 "version":e.get("im:version",{}).get("label"),
                 "author":e.get("author",{}).get("name",{}).get("label"),
                 "date":e.get("updated",{}).get("label"),
                }
                n+=1
            time.sleep(0.25)
        print(c,s,"total so far",len(out),file=sys.stderr)
json.dump(list(out.values()),open("/Users/irisyan/Documents/Claude/Reframe Take-home Challenge/data/apple_reviews.json","w"),indent=1)
print("APPLE TOTAL",len(out))
