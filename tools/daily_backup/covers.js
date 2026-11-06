const { chromium } = require("playwright"); const fs = require("fs");
const out = process.argv[2]; fs.mkdirSync(out, { recursive: true });
(async () => { const b = await chromium.launch(); const p = await b.newPage(); await p.setContent("<html><body></body></html>");
await p.evaluate(() => document.fonts.load("italic 900 40px Inter"));
const items = [["NEWS","#29e3ff","📰","N"],["CONFIRMED","#2bff88","✓","✓"],["MAPS","#ffb000","📍","M"],["COUNTDOWN","#ff3d8b","T-","T"],["COMMUNITY","#b48bff","💬","C"],["DEALS","#ffe14d","$","$"]];
for (const [name, col, , glyph] of items) {
 const url = await p.evaluate(([name,col,glyph]) => { const c=document.createElement('canvas');c.width=1080;c.height=1920;const x=c.getContext('2d');
  const g=x.createRadialGradient(540,960,0,540,960,700);g.addColorStop(0,'#3a0f5c');g.addColorStop(1,'#0b0618');x.fillStyle=g;x.fillRect(0,0,1080,1920);
  x.beginPath();x.arc(540,960,330,0,7);x.lineWidth=22;x.strokeStyle=col;x.shadowColor=col;x.shadowBlur=60;x.stroke();x.shadowBlur=0;
  // icon
  x.save();x.translate(540,960);x.strokeStyle=col;x.fillStyle=col;x.lineWidth=26;x.lineCap='round';x.lineJoin='round';
  if(name==='NEWS'){x.strokeRect(-150,-120,300,240);x.beginPath();x.moveTo(-100,-60);x.lineTo(100,-60);x.moveTo(-100,0);x.lineTo(100,0);x.moveTo(-100,60);x.lineTo(40,60);x.stroke();}
  else if(name==='CONFIRMED'){x.beginPath();x.moveTo(-140,10);x.lineTo(-40,110);x.lineTo(150,-100);x.stroke();}
  else if(name==='MAPS'){x.beginPath();x.arc(0,-50,110,Math.PI*0.85,Math.PI*2.15);x.lineTo(0,170);x.closePath();x.stroke();x.beginPath();x.arc(0,-50,38,0,7);x.fill();}
  else if(name==='COUNTDOWN'){x.beginPath();x.arc(0,0,150,0,7);x.stroke();x.beginPath();x.moveTo(0,0);x.lineTo(0,-100);x.moveTo(0,0);x.lineTo(80,40);x.stroke();}
  else if(name==='COMMUNITY'){x.beginPath();x.roundRect(-160,-120,320,190,50);x.stroke();x.beginPath();x.moveTo(-60,70);x.lineTo(-100,150);x.lineTo(10,70);x.stroke();}
  else {x.font='italic 900 300px Inter';x.textAlign='center';x.textBaseline='middle';x.fillText('$',0,10);}
  x.restore();
  x.font='italic 900 64px Inter';x.textAlign='center';x.fillStyle='#fff';x.fillText(name,540,1400);
  return c.toDataURL('image/png'); }, [name, col, glyph]);
 fs.writeFileSync(`${out}/HIGHLIGHT_${name}.png`, Buffer.from(url.split(",")[1], "base64")); }
await b.close(); console.log("covers ok"); })();
