import json,re,textwrap
R=json.load(open("data/coded_reviews.json"))
SRC={"apple":"App Store","google_play":"Google Play","trustpilot":"Trustpilot"}
def find(key,limit=1):
    out=[r for r in R if key.lower() in r["text"].lower()]
    return out[:limit]
BANK=[
 ("LENGTH — onboarding too long / too many questions",[
  "Wastes your time with a million questions before revealing",
  "Tell us the price before making someone fill out a 1 hour questionnaire",
  "Spent about 20 minutes going through the questions",
  "intentionally beginning with a very long questionnaire to draw you in and create sunk cost",
  "Absolutely hate apps that ask you a million questions",
  "the onboarding is too long for an app that crashes",
 ]),
 ("PAYWALL_TIMING — paywall arrived before any value",[
  "How nice of you guys to bring users through a long and detailed survey about their personal lives",
  "The first 10 minutes seem very promising considering the questions it asks you",
  "There is no free version. The problem with this kind of a business model",
  "If you’re actually helping people quit or cut back, then help them FIRST",
  "Download app > Answer Lots of Questions",
  "after a long questionnaire, they do not offer even a single free simple version",
  "Only got the paywall after going through all the forms and giving up all my data",
 ]),
 ("PRICE_SURPRISE — unexpected charge, unclear trial terms, cancellation trouble",[
  "I had no idea if I didn’t cancel my free trial subscription in time I would be charged for a WHOLE YEAR",
  "I downloaded this app awhile back just to see what it was about, although I’m sober",
  "I wish I had read reviews about unfair charging",
  "I was supposed to be on a 7 day trial and I was to be reminded before the trial ended",
  "Signed up for the free-trial which I never even used",
 ]),
 ("SIGNUP_BREAK — first session blocked by a technical failure (emergent code)",[
  "Can’t even get started with this app. I tried creating an account",
  "trying to sign up for weeks. I'm not getting the confirmation code",
  "Tried multiple times to get started, but the app would freeze on",
  "couldn't even make it thru the questions section as it wouldn't scroll",
  "I can't get past the signup process because of how uncontrollable the sliders are",
  "it kept saying it was creating my plan, but never finished. So I closed it out and it was asking all the same questions",
 ]),
 ("GENERIC — personalization not felt; answers did not carry forward",[
  "I poured my heart out during the intake questions",
  "taking you through the answering of surveys (where frankly most the responses are not nearly as personalized",
  "Filled in all the questionnaire online, signed up then installed the app and after logging in had to go through the questionnaire all over again",
  "Lost all survey data once app purchased",
  "the messages are generic, rather than being tailored based on the data the user inputs",
  "First it skipped the quiz for unknown reasons and created its own program for me that had nothing to do with what I actually want to do",
 ]),
 ("TONE — judgmental, clinical, shaming or infantilizing language",[
  "odd that they chose the verbiage",
  "Some good info but I sure didn’t need to see frowning faces",
  "The app is patronising, judgemental and very heterosexual oriented",
  "When you skip a day or two, it assumes you just magically stopped drinking",
  "That is the 1st thing you want me to click on. A belief that this will work",
 ]),
 ("VALUE_UNCLEAR — did not understand what the app does or would do for them",[
  "Downloaded the app due to an ad had no clue what it was about",
  "Requires log-in before giving a single reason why that would be necessary",
  "What ever happened to a flat fee purchase? What services are you actually providing",
  "This app is not easy to navigate. Couldn’t find quizzes that were advertised",
 ]),
 ("TRUST — credibility, science claims, data handling",[
  "There are some very personal questions they ask you at the beginning that makes you think you’ll be able to see what this app offers",
  "Why must we go through a quiz, give you our data then get charged for it",
  "Financial hardship is one of the main causes of alcoholism",
  "you should produce a policy that supports your “money back 200%” claim",
  "It's not a useful app: it's more like a normal generic 'streaks' app",
 ]),
 ("EMOTIONAL_FIT (negative) — felt like the wrong fit for their drinking",[
  "the reason for removing two stars is the question about how often I feel regrets about drinking",
  "all the daft questions beforehand made me think my problem isn't that bad",
  "Bait & Switch... advertises as a way to cut down... nope. Pure AA sobriety app",
  "I found that the guidance for wanting to cut back seemed odd",
  "I wouldn’t label myself an alcoholic (yet!) but more of a grey area drinker",
 ]),
 ("EMOTIONAL_FIT (positive) — felt seen; what the product gets right",[
  "There are no rigid (judgmental) rules- you evolve in your own time",
  "Reframe has taken me from shame and desperation to an enthusiastic",
  "The best part about Reframe is that it's not the slightest bit \"judgy\"",
  "It doesn’t make you feel like you’ve failed if you drink",
  "An amazing program that is tailored to your comfort level and personality",
 ]),
 ("FIRST_WIN — something useful happened early",[
  "My first day on this app I joined a zoom meeting",
  "The first 10 minutes seem very promising",
  "8 days in and it’s made a massive difference",
  "I almost never give reviews but signed up for the trial with intention to cancel but liked it so much",
 ]),
]
out=[]
out.append("# Pass 2 — Quote bank\n")
out.append("Every verbatim below is an unedited excerpt from a public review in `data/coded_reviews.csv`. Star rating, source and month are attached to each one so nothing here is unattributable. Ellipses mark trimmed text; nothing else is changed.\n")
for head,keys in BANK:
    out.append(f"\n## {head}\n")
    seen=set()
    for k in keys:
        got=find(k,1)
        if not got: out.append(f"- _(not found: {k[:40]})_\n"); continue
        r=got[0]
        if r["id"] in seen: continue
        seen.add(r["id"])
        t=" ".join(r["text"].split())
        i=t.lower().find(k.lower().split("…")[0][:40])
        s=max(0,i-0); e=min(len(t),i+430)
        ex=t[s:e]+("…" if e<len(t) else "")
        out.append(f"> {ex}\n>\n> — **{r['rating']}★**, {SRC[r['source']]}, {r['date'][:7]}\n")
open("pass2-quote-bank.md","w").write("\n".join(out))
print("wrote", sum(1 for l in out if l.startswith(">")), "quote blocks")
