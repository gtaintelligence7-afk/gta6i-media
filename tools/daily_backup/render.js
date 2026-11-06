// Renders plan.json -> <out>/<date>/INSTAGRAM/STORY_0X.png + YOUTUBE/THUMBNAIL.png (1080x1920), GTA 6 Intelligence style
const { chromium } = require("playwright"); const fs = require("fs"); const path = require("path");
const [plan, out] = [process.argv[2], process.argv[3]];
const PAGE = `<html><body><script>
const W=1080,H=1920;const F=(w,s,it=true)=>(it?'italic ':'')+w+' '+s+'px Inter';
const C={pink:'#ff3d8b',cyan:'#29e3ff',yellow:'#ffe14d',green:'#2bff88',red:'#ff3b3b',amber:'#ffb000',violet:'#b48bff'};
const PAL=[['#14072e','#3a0f5c',C.pink],['#06121f','#14304a',C.cyan],['#1f0a1a','#5c0f3a',C.yellow],['#0b1a12','#123a2e',C.green],['#1a0730','#2a1060',C.violet]];
function cv(top,mid,seed){const c=document.createElement('canvas');c.width=W;c.height=H;const x=c.getContext('2d');const g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,top);g.addColorStop(.6,mid);g.addColorStop(1,'#06030d');x.fillStyle=g;x.fillRect(0,0,W,H);
 x.strokeStyle='rgba(41,227,255,0.14)';x.lineWidth=2;for(let i=-12;i<=12;i++){x.beginPath();x.moveTo(540+i*30,1500);x.lineTo(540+i*220,H);x.stroke();}for(let k=0;k<6;k++){const y=1500+420*Math.pow(k/5,1.8);x.beginPath();x.moveTo(0,y);x.lineTo(W,y);x.stroke();}
 T(x,'GTA 6 INTELLIGENCE',250,38,C.pink);return [c,x];}
function T(x,s,y,size,col,w=900,max=760,cx=540){let z=size;x.font=F(w,z);while(x.measureText(s).width>max&&z>22){z-=2;x.font=F(w,z);}x.textAlign='center';x.textBaseline='middle';x.fillStyle=col;x.fillText(s,cx,y);}
function wrap(x,s,y,size,col,max=720,lh=1.2,w=900){x.font=F(w,size);const words=s.split(' ');const lines=[];let cur='';for(const wd of words){const t=cur?cur+' '+wd:wd;if(x.measureText(t).width>max&&cur){lines.push(cur);cur=wd}else cur=t}if(cur)lines.push(cur);lines.forEach((l,i)=>T(x,l,y+i*size*lh,size,col,w,max));return lines.length;}
function N(x,s,y,size,col){x.save();let z=size;x.font=F(900,z);while(x.measureText(s).width>860&&z>40){z-=4;x.font=F(900,z);}x.textAlign='center';x.textBaseline='middle';x.shadowColor=col;x.shadowBlur=z*.35;x.fillStyle=col;x.fillText(s,540,y);x.shadowBlur=0;x.lineWidth=3;x.strokeStyle='rgba(255,255,255,.9)';x.strokeText(s,540,y);x.restore();}
function badge(x,label,col,y){x.font=F(900,34,false);const w=x.measureText(label).width+84;x.fillStyle='rgba(6,4,14,.85)';x.beginPath();x.roundRect(540-w/2,y-34,w,68,12);x.fill();x.lineWidth=4;x.strokeStyle=col;x.stroke();x.beginPath();x.arc(540-w/2+30,y,9,0,7);x.fillStyle=col;x.fill();x.fillStyle=col;x.textAlign='left';x.textBaseline='middle';x.fillText(label,540-w/2+48,y+2);}
function box(x,y,h,col){x.fillStyle='rgba(6,4,14,.82)';x.beginPath();x.roundRect(160,y,760,h,26);x.fill();x.lineWidth=5;x.strokeStyle=col;x.stroke();}
function foot(x){T(x,'Follow @gta6_intelligence · fact-checked GTA 6 news',1700,30,'rgba(255,255,255,.75)',700,800);}
const R={
 countdown(s,i){const p=PAL[i%PAL.length];const [c,x]=cv(p[0],p[1]);N(x,s.big,520,s.big.length>5?190:260,p[2]);T(x,s.sub,700,56,'#fff');
  box(x,820,330,C.green);badge(x,'OFFICIAL',C.green,820);T(x,s.head,930,64,'#fff',900,700);wrap(x,s.detail,1030,38,C.yellow,680,1.25,800);
  T(x,'Source: '+s.source,1230,28,'rgba(255,255,255,.7)',700,760);foot(x);return c;},
 quiz(s,i){const p=PAL[(i+1)%PAL.length];const [c,x]=cv(p[0],p[1]);N(x,'QUIZ',430,170,C.yellow);wrap(x,s.q,640,60,'#fff',780);
  s.opts.forEach((o,k)=>{box(x,860+k*170,130,[C.cyan,C.pink,C.violet][k]);T(x,String.fromCharCode(65+k)+'.  '+o,925+k*170,52,'#fff',900,660);});
  T(x,'Answer revealed at 20:00 👀',1430,40,C.yellow,800);foot(x);return c;},
 poll(s,i){const p=PAL[(i+2)%PAL.length];const [c,x]=cv(p[0],p[1]);N(x,'VOTE',430,190,C.pink);wrap(x,s.q,640,72,'#fff',800);
  [[285,s.opts[0],C.cyan],[795,s.opts[1],C.pink]].forEach(([cx,o,col])=>{x.fillStyle='rgba(6,4,14,.85)';x.beginPath();x.roundRect(cx-190,880,380,200,30);x.fill();x.lineWidth=6;x.strokeStyle=col;x.stroke();T(x,o,980,60,col,900,330,cx);});
  T(x,'VS',980,50,'#fff');T(x,'Tap to vote 👆',1200,44,C.yellow,800);foot(x);return c;},
 card(s,i){const p=PAL[(i+3)%PAL.length];const [c,x]=cv(p[0],p[1]);T(x,s.kind==='PLACE'?'LEONIDA · PLACE':s.kind==='CHARACTER'?'MEET THE CAST':'CONFIRMED',420,48,p[2]);
  N(x,s.head,620,s.head.length>14?96:130,p[2]);box(x,780,260,p[2]);wrap(x,s.detail,880,48,'#fff',680);badge(x,'OFFICIAL · ROCKSTAR',C.green,1130);
  T(x,'Save this for launch week 📌',1300,40,C.yellow,800);foot(x);return c;},
 question(s,i){const p=PAL[(i+4)%PAL.length];const [c,x]=cv(p[0],p[1]);N(x,'YOUR TURN',460,150,C.cyan);box(x,620,420,C.cyan);wrap(x,s.q,760,66,'#fff',680);
  T(x,'Reply 👇 best answers get reshared',1120,40,C.yellow,800);if(s.teaser){box(x,1220,170,C.pink);wrap(x,s.teaser,1280,36,'#fff',700,1.3,800);}foot(x);return c;},
 promo(s,i){const p=PAL[(i+1)%PAL.length];const [c,x]=cv(p[0],p[1]);N(x,'DON’T MISS IT',470,120,C.yellow);box(x,620,420,C.pink);T(x,s.head,720,52,C.pink,900,680);wrap(x,s.detail,830,54,'#fff',680);T(x,'Tap the link · turn on notifications 🔔',1130,38,C.yellow,800);N(x,'FOLLOW',1330,110,C.cyan);T(x,'@gta6_intelligence · new drop every day',1440,38,'#fff',800);foot(x);return c;},
 thumb(t,i){const p=PAL[(i+2)%PAL.length];const [c,x]=cv(p[0],p[1]);N(x,'GTA 6',520,230,p[2]);wrap(x,t.replace(/ #.*$/,'').toUpperCase(),800,80,'#fff',860);badge(x,'FACT-CHECKED',C.green,1300);return c;}
};
window.render=(kind,data,i)=>R[kind](data,i).toDataURL('image/png');
</script></body></html>`;
(async () => {
  const days = JSON.parse(fs.readFileSync(plan)); const b = await chromium.launch(); const pg = await b.newPage();
  await pg.setContent(PAGE); await pg.evaluate(() => document.fonts.load("italic 900 40px Inter"));
  for (const [di, d] of days.entries()) {
    const ig = path.join(out, d.date, "INSTAGRAM"), yt = path.join(out, d.date, "YOUTUBE"); fs.mkdirSync(ig, { recursive: true }); fs.mkdirSync(yt, { recursive: true });
    for (const [k, s] of d.stories.entries()) {
      const url = await pg.evaluate(([kind, data, i]) => window.render(kind, data, i), [s.type, s, di + k]);
      fs.writeFileSync(path.join(ig, `STORY_0${k + 1}.png`), Buffer.from(url.split(",")[1], "base64"));
    }
    const t = await pg.evaluate(([kind, data, i]) => window.render(kind, data, i), ["thumb", d.youtube.title, di]);
    fs.writeFileSync(path.join(yt, "THUMBNAIL.png"), Buffer.from(t.split(",")[1], "base64"));
  }
  await b.close(); console.log("rendered", days.length);
})();
