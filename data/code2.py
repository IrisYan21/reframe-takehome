import json,re,collections,csv
R=json.load(open("data/all_reviews.json"))
Q=r"(?:question(?:s|naire)?|quiz|survey|form(?:s)?|onboarding|set ?-?up|setup|sign ?-?up|signing up|profile|intake|details|info(?:rmation)?|data)"
PAY=r"(?:pay(?:ing|ment|wall)?|price|pricing|cost(?:s)?|subscri\w+|money|\$|£|€|charge|fee|free)"
P={
"LENGTH":[
 r"(?:too|so|a lot of|lots of|dozens of|hundreds? of|a million|100|thousand|endless|extensive|lengthy|long|longest|whole|entire|all the|bunch of|loads of|tons of)\s+(?:\w+\s+){0,2}(?:question|quiz|survey|questionnaire|form)",
 r"(?:question|quiz|survey|questionnaire|onboarding|sign ?-?up|set ?-?up|setup|initiation)\w*\s+(?:process\s+)?(?:is|was|are|were|seems?|felt|feels)\s+(?:\w+\s+){0,2}(?:too\s+)?(?:long|lengthy|daunting|endless|tedious|overwhelming)",
 r"(?:long|lengthy|extensive|endless|daunting|tedious|drawn ?out)\s+(?:\w+\s+){0,2}(?:question|quiz|survey|questionnaire|onboarding|sign ?-?up|set ?-?up|setup)",
 r"(?:long|lengthy|extensive|endless|daunting|tedious)\s+(?:\w+\s+){0,2}(?:process|profile)\b[^.!?]{0,60}(?:question|quiz|survey|sign|pay|cost|subscri)",
 r"question after question|page after page|never ?ending|interrogat|grill(?:ed|ing)",
 rf"(?:spent|spend|spending|wast\w+|took)\s+(?:about\s+|around\s+|over\s+|up to\s+)?(?:\d+|\d+/\d+|a few|several|ten|twenty|thirty|an?)\s*(?:min(?:ute)?s?|hours?)\b[^.!?]{{0,90}}{Q}",
 rf"{Q}[^.!?]{{0,60}}(?:spent|spend|took)\s+(?:about\s+|around\s+)?(?:\d+|a few|several|an?)\s*(?:min(?:ute)?s?|hours?)\b",
 r"gave up (?:before|during|half ?way|part ?way)",
 r"1 hour questionnaire|hour questionnaire|20 minutes going through",
],
"TONE":[
 r"(?<!non-)(?<!non )(?<!not )(?<!never )judg(?:e|ed|es|ing|ment|ement|mental)",
 r"sham(?:e|ed|es|ing|eful)\b", r"condescend", r"patroniz|patronis", r"preachy", r"lectur(?:e|ed|ing)",
 r"made me feel (?:bad|guilty|worse|like a)", r"guilt ?trip", r"infantil", r"talk(?:s|ing)? down",
 r"like a child|potty", r"frowning face", r"demoraliz|demoralis", r"nagging", r"pushy",
 r"assumes? (?:you|i|that)\w*\s*(?:are|am|'?re|'?m)\s*(?:an?\s*)?alcoholic",
 r"label(?:l)?(?:ed|ing|s) me", r"AA mantra|AA type|demon rum|\bcults?\b|cult-?like",
],
"PAYWALL_TIMING":[
 rf"(?:after|once|then|only to|before)\b[^.!?]{{0,80}}{Q}[^.!?]{{0,80}}(?:paywall|pay ?wall|have to pay|has to pay|must pay|force\w* (?:you|me) to pay|want\w* (?:your |my )?money|subscri\w+|charge|cost|price|credit card|\$\d|£\d)",
 rf"{Q}[^.!?]{{0,90}}(?:then|before)[^.!?]{{0,60}}(?:paywall|pay|subscri|money|credit card|\$|£)",
 r"(?:hit|hits|hitting|met|slapped|springs?|sprung|slide in|revealing|reveal)\s+(?:you |me |us )?(?:with )?(?:a |the )?pay ?wall",
 r"paywall|pay ?wall",
 r"tell (?:us|me|people|you) the (?:price|cost)[^.!?]{0,30}before",
 r"(?:up ?front|upfront)[^.!?]{0,40}(?:cost|price|pay|charge)|(?:cost|price)[^.!?]{0,30}up ?front",
 r"before (?:you|i|we)[^.!?]{0,30}(?:even )?(?:know|see|try|browse|use|get|access)",
 r"no (?:free|non ?-?subscri)[^.!?]{0,20}(?:version|option|tier|plan)|not (?:even )?(?:a )?free (?:version|option|trial)",
 r"can'?t (?:even |do )?(?:try|use|see|access|get into|open)[^.!?]{0,40}(?:without|unless|before)[^.!?]{0,20}pay",
 r"sunk cost|bait and switch|bait ?& ?switch|bait-and-switch",
 r"help them first|help (?:people|users) first",
 r"waste of (?:my |your )?(?:time|morning)",
],
"PRICE_SURPRISE":[
 r"charg\w+ (?:me|us|my|without|the (?:full |whole )?year)", r"unexpected|unauthoriz|unauthoris|without my (?:consent|permission|knowledge)",
 r"didn'?t (?:know|realiz|realis|agree|sign up|want|ask)[^.!?]{0,50}(?:charg|bill|subscri|renew|year)",
 r"auto(?:matic\w*)?[ -]?renew|automatically charg|immediately charg|charged immediately",
 r"free trial[^.!?]{0,70}(?:charg|bill|took|taken|\$\d|£\d|deduct)",
 r"cancel\w*[^.!?]{0,60}(?:still |but |and |yet )?[^.!?]{0,20}charg",
 r"can'?t cancel|cannot cancel|impossible to cancel|hard to cancel|difficult to cancel|trouble cancel|unable to cancel|no way to cancel",
 r"no refund|refus\w+[^.!?]{0,25}refund|want (?:my|a) refund|refund[^.!?]{0,20}(?:denied|refused)",
 r"\bscam\b|\brip ?off\b|\bfraud|\bcon\b|thieves|thief|stole|steal|ponzi|grift|daylight robbery|took my money|money grab|cash grab",
 r"hidden (?:fee|charge|cost)|sneak|dodgy|shady|dark pattern|mis-?sell|false advertis|misleading",
 r"billed me|billed for|charged \$|charged £",
],
"GENERIC":[
 r"generic", r"not (?:really )?personali[sz]|isn'?t personali[sz]|nearly as personali[sz]|lack\w* personali[sz]",
 r"not (?:really |very )?(?:tailored|customi[sz]ed|individuali[sz]ed)", r"same for everyone|one ?size ?fits ?all|one-size|cookie ?cutter|boiler ?plate",
 r"(?:didn'?t|doesn'?t|don'?t|never)[^.!?]{0,30}(?:use|read|reflect|look at|consider|match)[^.!?]{0,25}(?:my )?answer",
 r"answers?[^.!?]{0,30}(?:didn'?t|don'?t|doesn'?t)[^.!?]{0,25}(?:matter|change|affect|count)",
 r"nothing to do with (?:me|what i|my)", r"must represente me|doesn'?t represent me",
 r"skipped the quiz", r"lost all survey data", r"go through the question\w*[^.!?]{0,30}again|questionnaire (?:all )?over again|same questions it already asked",
 r"poured my heart out", r"just wants your data|scrapes all (?:your|my) data|feed their database|data mining|give (?:you|them) our data|collects all your data",
 r"chat ?gpt|\bAI[- ]generated|all ai|AI driven|AI-driven",
],
"VALUE_UNCLEAR":[
 r"(?:no clue|no idea|not sure|didn'?t know|don'?t know|didn'?t realis\w+ |unclear|didn'?t tell (?:me|us)|can'?t (?:even )?see|couldn'?t see)[^.!?]{0,40}what (?:it|this|the app|they)[^.!?]{0,25}(?:was|is|does|offers|about|do)\b",
 r"know what (?:i'?m|we'?re|you'?re) getting|what i'?m getting into|a single reason why|what services are you actually providing|what good does that do",
 r"confusing[^.!?]{0,40}(?:app|navigate|pricing|sign|setup|set ?up|to use)|(?:app|pricing|sign ?-?up|setup|it) (?:is |was )?(?:just |honestly )?(?:confusing|not easy to navigate)",
 r"not easy to navigate|hard to navigate|couldn'?t figure out|unclear how to use|non-?intuitive",
],
"TRUST":[
 r"pseudo ?-?scienc|questionable|no evidence|bogus|not (?:even )?(?:very )?scienc|nothing '?neuroscienc",
 r"privacy|my data|sells? (?:my|your) (?:data|information)|phishing|less intrusive|intrusive",
 r"gaslighting|lacks transparency|lack(?:s)? transparency|not transparent|fake (?:support|reviews)|five star reviews are genuine",
 r"money back (?:guarantee|promise)|200% (?:money )?back|where is their money back",
 r"prey(?:s|ing)? on|take advantage of|taking advantage of|exploit|predatory|vulnerable population|manipulate an addict|monetizing someone",
 r"unethical|shame on you|should be ashamed|disgusting business|disgraceful",
],
"FIRST_WIN":[
 r"first (?:day|week|days|10 minutes|ten minutes)[^.!?]{0,60}(?:help|better|noticed|less|change|amazing|great|impressed|promising|meeting)",
 r"(?:day one|day 1)[^.!?]{0,50}(?:help|easy|great|joined|changed)",
 r"from the (?:first day|start|get ?-?go)[^.!?]{0,50}(?:help|better|noticed)",
 r"immediately (?:help|noticed|felt|impressed|started)",
 r"seem(?:ed|s) (?:very )?promising|gain a sense of security|navigates your mind",
],
"EMOTIONAL_FIT_POS":[
 r"non ?-?judg(?:e)?ment|without judg|no judg|no shame|not preachy|doesn'?t make you feel like you'?ve failed",
 r"felt (?:seen|understood|heard)|feel(?:s)? (?:seen|understood|heard)|really feel heard",
 r"meets? (?:you|me) where|at your own pace|go at my own pace|not one size fits all",
 r"for those of us who|for (?:people|someone) like me|not AA|without (?:the )?religious",
],
"EMOTIONAL_FIT_NEG":[
 r"(?:just |simply )?not (?:really )?for me\b|isn'?t for me|wasn'?t for me|not what i was looking for|wrong (?:app|fit) for",
 r"i'?m not an alcoholic|wouldn'?t label myself an alcoholic|never regret (?:drinking|it)|i actually enjoy drinking|my problem isn'?t that bad|didn'?t feel out of control",
 r"(?:geared|aimed|targeted|designed)\s+(?:very much\s+)?(?:towards?|to|for)\s+(?:a\s+)?(?:young|20|a younger|american|men|heterosexual|US)",
 r"too (?:US|american)[ -]?(?:centric|focused)|US customer focused|built for america|not relatable",
 r"(?:pure|just another|century old) AA|AA (?:type|mantra|rhetoric)|only (?:want|for) (?:you )?(?:to )?(?:quit|stop completely)|geared (?:for|to) quitting|not really set up for those people|do not sign up unless you want to stop completely",
 r"triggered (?:some issues|me|my)|made me drink more|led to more drinks|worsened (?:my )?(?:anxiety|cravings)|more anxious when i started|drives you to drink",
 r"homophobic|heterosexual oriented",
 r"enough shame in my life|frowning face",
],
"SIGNUP_BREAK":[
 r"can'?t (?:even )?(?:log ?in|sign ?up|sign ?in|create an account|get started|set ?up|register)",
 r"couldn'?t (?:log ?in|sign ?up|sign ?in|create|get past|even make it)",
 r"(?:won'?t|wouldn'?t|doesn'?t|didn'?t) (?:even )?(?:let|allow) (?:me|you) (?:to )?(?:sign ?up|log ?in|register|create)",
 r"confirmation code|auth code|verification code|mfa code|code (?:never|didn'?t) (?:come|arrive|work)",
 r"stuck (?:on|in)[^.!?]{0,30}(?:sign ?up|enrol|loading|creating|plan|paywall|loop)",
 r"crash\w*|freez\w*|glitch\w*|bug\b|infinite loop|keeps? (?:spinning|loading)|never finished|wouldn'?t scroll|lagging",
 r"unable to (?:sign ?up|log ?in|open|access|use the app)",
 r"password[^.!?]{0,40}(?:incorrect|wrong|can'?t see|doesn'?t|confirm)",
 r"building my personalized plan but nothing|creating (?:a |my )?personali[sz]ed plan",
],
}
C={k:[re.compile(p,re.I) for p in v] for k,v in P.items()}
PRAISE=re.compile(r"(?:non ?-?|no |not |never |without |free of |zero |anti-?)\s?(?:judg\w*|sham\w*)|(?:judg\w*|sham\w*)[ -]?free|(?:judgement|judgment|shame)[ -]free", re.I)
for r in R:
    t=r["text"]
    tn=PRAISE.sub(" __PRAISE__ ", t)     # strip praise forms before negative-tone matching
    cs=[]
    for k,ps in C.items():
        src = tn if k=="TONE" else t
        if any(p.search(src) for p in ps): cs.append(k)
    if "__PRAISE__" in tn and "EMOTIONAL_FIT_POS" not in cs: cs.append("EMOTIONAL_FIT_POS")
    r["codes"]=sorted(cs)
json.dump(R,open("data/coded_reviews.json","w"),indent=1)
with open("data/coded_reviews.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["id","source","country","rating","date","codes","text"])
    for r in R: w.writerow([r["id"],r["source"],r["country"],r["rating"],r["date"],"|".join(r["codes"]),r["text"]])
print("coded",len(R),"tagged",sum(1 for r in R if r["codes"]))
