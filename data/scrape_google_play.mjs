import gplay from 'google-play-scraper';
const g = gplay.default ?? gplay;
const APP='com.glucobit.reframe';
try{
  const info = await g.app({appId:APP});
  console.error('APP OK', info.title, info.score, info.ratings, info.reviews);
}catch(e){ console.error('APP ERR', e.message); }
const out=new Map();
for (const [sname,sval] of [['newest',g.sort.NEWEST],['rating',g.sort.RATING],['helpful',g.sort.HELPFULNESS]]){
  try{
    const r = await g.reviews({appId:APP, sort:sval, num:600, country:'us', lang:'en'});
    for(const rv of r.data){ if(!out.has(rv.id)) out.set(rv.id,{id:rv.id,source:'google_play',country:'us',rating:rv.score,title:null,text:rv.text,version:rv.version,author:rv.userName,date:rv.date,thumbsUp:rv.thumbsUp}); }
    console.error(sname, r.data.length, 'total', out.size);
  }catch(e){ console.error('ERR',sname,e.message); }
}
import fs from 'fs';
fs.writeFileSync('/Users/irisyan/Documents/Claude/Reframe Take-home Challenge/data/google_play_reviews.json', JSON.stringify([...out.values()],null,1));
console.log('GP TOTAL', out.size);
