// GTA 6 INTELLIGENCE – in-page carousel generator (no external assets; works inside IG/TikTok pages under CSP)
// window.__gtaCarousel(set, H) -> Promise<File[]>   set: "leonida" | "editions" | "top5"; H: 1350 (IG 4:5) or 1440 (TikTok 3:4)
(() => {
  const W = 1080;
  const F = (w, s, it = true) => `${it ? "italic " : ""}${w} ${s}px "Segoe UI Black","Segoe UI","Arial Black",Arial,sans-serif`;
  const C = { pink: "#ff3d8b", cyan: "#29e3ff", yellow: "#ffe14d", green: "#2bff88", red: "#ff3b3b", amber: "#ffb000", violet: "#b48bff" };
  function canvas(H, top, mid) {
    const c = document.createElement("canvas"); c.width = W; c.height = H; const x = c.getContext("2d");
    const g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, top); g.addColorStop(0.6, mid); g.addColorStop(1, "#06030d"); x.fillStyle = g; x.fillRect(0, 0, W, H);
    x.font = F(900, 32); x.fillStyle = C.pink; x.textAlign = "left"; x.textBaseline = "middle"; x.fillText("GTA 6 INTELLIGENCE", 70, 80);
    return [c, x];
  }
  function T(x, s, y, size, col, w = 900, max = 900, cx = 540, al = "center") {
    let z = size; x.font = F(w, z); while (x.measureText(s).width > max && z > 22) { z -= 2; x.font = F(w, z); }
    x.textAlign = al; x.textBaseline = "middle"; x.fillStyle = col; x.fillText(s, cx, y);
  }
  function N(x, s, y, size, col, cx = 540) {
    x.save(); x.font = F(900, size); x.textAlign = "center"; x.textBaseline = "middle"; x.shadowColor = col; x.shadowBlur = size * 0.35;
    x.fillStyle = col; x.fillText(s, cx, y); x.shadowBlur = 0; x.lineWidth = 3; x.strokeStyle = "rgba(255,255,255,.9)"; x.strokeText(s, cx, y); x.restore();
  }
  function badge(x, label, col, y, cx = 540) {
    x.font = F(900, 36, false); const w = x.measureText(label).width + 84;
    x.fillStyle = "rgba(6,4,14,.85)"; x.beginPath(); x.roundRect(cx - w / 2, y - 36, w, 72, 12); x.fill(); x.lineWidth = 4; x.strokeStyle = col; x.stroke();
    x.beginPath(); x.arc(cx - w / 2 + 32, y, 10, 0, 7); x.fillStyle = col; x.fill(); x.fillStyle = col; x.textAlign = "left"; x.textBaseline = "middle"; x.fillText(label, cx - w / 2 + 52, y + 2);
  }
  function footer(x, H, s = "Follow @gta6_intelligence for fact-checked GTA 6 news") { T(x, s, H - 70, 32, "rgba(255,255,255,.7)", 700, 940); }
  // ---------- LEONIDA: map-pin style, sunset palette ----------
  function pin(x, cx, cy, r, col, n) {
    x.save(); x.shadowColor = col; x.shadowBlur = 40; x.beginPath(); x.arc(cx, cy, r, Math.PI, 0); x.lineTo(cx, cy + r * 1.9); x.closePath(); x.fillStyle = col; x.fill(); x.restore();
    x.beginPath(); x.arc(cx, cy, r * 0.62, 0, 7); x.fillStyle = "#14072e"; x.fill(); T(x, String(n), cy + 4, r * 0.8, "#fff", 900, r, cx);
  }
  function leonida(H) {
    const out = [], places = [
      ["VICE CITY", "Neon, beaches and the skyline", C.pink],
      ["LEONIDA KEYS", "Islands, boats and open water", C.cyan],
      ["GRASSRIVERS", "Swamps, airboats and gators", C.green],
      ["PORT GELLHORN", "Motels and late nights", C.amber],
      ["AMBROSIA", "Bikers and industry", C.red],
      ["MOUNT KALAGA", "National park: forests, rivers, trails", C.violet]];
    { const [c, x] = canvas(H, "#2a0a3f", "#ff6a3d");
      // sunset sun + water lines
      const sy = H * 0.62; x.save(); x.beginPath(); x.arc(540, sy, 300, Math.PI, 0); x.fillStyle = "rgba(255,225,77,.85)"; x.fill(); x.restore();
      x.fillStyle = "rgba(20,7,46,.55)"; for (let i = 0; i < 8; i++) x.fillRect(0, sy + i * 26, W, 10);
      T(x, "YOU THINK GTA 6", 260, 76, "#fff"); T(x, "IS JUST VICE CITY?", 350, 76, "#fff");
      N(x, "6 PLACES", 560, 150, C.yellow);
      T(x, "Rockstar showed across Leonida", 700, 48, "#fff", 800);
      badge(x, "OFFICIAL", C.green, sy + 260); T(x, "Swipe →", H - 150, 44, C.yellow, 800); footer(x, H); out.push(c); }
    places.forEach(([n, d, col], i) => {
      const [c, x] = canvas(H, "#14072e", "#3a0f5c");
      T(x, `PLACE ${i + 1}/6`, 190, 40, col);
      pin(x, 540, 420, 110, col, i + 1);
      N(x, n, 760, 110, col); T(x, d, 880, 48, "#fff", 800, 900);
      badge(x, "OFFICIAL · ROCKSTAR", C.green, 1010); footer(x, H); out.push(c);
    });
    { const [c, x] = canvas(H, "#2a0a3f", "#3a0f5c");
      T(x, "WHERE ARE YOU", 420, 96, "#fff"); T(x, "GOING FIRST?", 530, 96, C.yellow);
      T(x, "Comment the number 1–6 👇", 690, 52, "#fff", 800);
      T(x, "Save this for launch day: Nov 19", 820, 42, C.cyan, 800); footer(x, H); out.push(c); }
    return out;
  }
  // ---------- EDITIONS: price-tag + receipt style, light paper ----------
  function editions(H) {
    const out = [];
    { const [c, x] = canvas(H, "#0b0618", "#123a2e");
      T(x, "GTA 6 COSTS", 300, 90, "#fff"); N(x, "$79.99", 500, 190, C.green);
      T(x, "...but what does +$20 get you?", 690, 54, C.yellow, 800);
      badge(x, "OFFICIAL US PRICES", C.green, 820); T(x, "Swipe →", H - 150, 44, C.yellow, 800); footer(x, H); out.push(c); }
    { const [c, x] = canvas(H, "#0b0618", "#3a0f5c");
      for (const [cx, name, price, col, r] of [[300, "STANDARD", "$79.99", C.yellow, -0.05], [780, "ULTIMATE", "$99.99", C.pink, 0.05]]) {
        x.save(); x.translate(cx, 520); x.rotate(r); x.fillStyle = "rgba(6,4,14,.9)"; x.beginPath(); x.roundRect(-210, -170, 420, 340, 26); x.fill(); x.lineWidth = 6; x.strokeStyle = col; x.stroke();
        x.beginPath(); x.arc(0, -130, 14, 0, 7); x.fillStyle = col; x.fill(); T(x, name, -50, 52, "#fff", 900, 380, 0); T(x, price, 60, 100, col, 900, 380, 0); x.restore();
      }
      T(x, "PS5 & Xbox Series X|S · US prices", 820, 44, "#fff", 800); badge(x, "OFFICIAL", C.green, 920); footer(x, H); out.push(c); }
    { const [c, x] = canvas(H, "#0b0618", "#3a0f5c");
      x.fillStyle = "rgba(250,247,238,.97)"; x.beginPath(); x.roundRect(120, 200, 840, 760, 16); x.fill();
      T(x, "ULTIMATE ADDS (STORY MODE)", 270, 44, "#16111f", 900, 760);
      const rows = ["Rideout Customs mod shop", "One-Eyed Willie's mod shop", "Extra clothing stores", "Hair salon + tattoo parlour"];
      rows.forEach((r, i) => { T(x, "✓  " + r, 400 + i * 110, 46, "#16111f", 800, 720, 170, "left"); });
      T(x, "TOTAL  +$20.00", 880, 56, "#d4246b", 900, 700);
      badge(x, "OFFICIAL", C.green, 1050); footer(x, H); out.push(c); }
    { const [c, x] = canvas(H, "#0b0618", "#3a0f5c");
      x.save(); x.translate(540, 470); x.lineWidth = 18; x.strokeStyle = C.red; x.beginPath(); x.arc(0, 0, 170, 0, 7); x.stroke();
      x.lineWidth = 6; x.strokeStyle = "rgba(255,255,255,.8)"; x.beginPath(); x.arc(0, 0, 50, 0, 7); x.stroke(); x.beginPath(); x.arc(0, 0, 115, 0, 7); x.stroke();
      x.lineWidth = 20; x.strokeStyle = C.red; x.beginPath(); x.moveTo(-120, -120); x.lineTo(120, 120); x.stroke(); x.restore();
      N(x, "NO DISC", 780, 120, C.red); T(x, "The physical box = a download code", 900, 46, "#fff", 800);
      badge(x, "OFFICIAL", C.green, 1020); footer(x, H); out.push(c); }
    { const [c, x] = canvas(H, "#0b0618", "#3a0f5c");
      T(x, "STANDARD", 420, 100, C.yellow); T(x, "or", 520, 60, "#fff"); T(x, "ULTIMATE?", 620, 100, C.pink);
      T(x, "Comment S or U 👇", 790, 54, "#fff", 800); footer(x, H); out.push(c); }
    return out;
  }
  // ---------- TOP 5: big neon numbers, cyan/violet ----------
  function top5(H) {
    const out = [], facts = [
      ["NOV 19, 2026", "Launch on PS5 + Xbox Series X|S", C.green],
      ["NOV 10", "Pre-load opens · up to 212 GB", C.cyan],
      ["JUSTICE", "Grammy-winning duo · original score", C.violet],
      ["VINTAGE VICE CITY PACK", "Bonus for digital pre-orders before Nov 20", C.pink],
      ["NO DISC", "Physical box contains a download code", C.red]];
    { const [c, x] = canvas(H, "#06121f", "#14304a");
      N(x, "5", 430, 360, C.cyan); T(x, "THINGS ROCKSTAR", 700, 84, "#fff"); T(x, "ACTUALLY CONFIRMED", 800, 84, C.yellow);
      T(x, "No leaks. No rumours.", 920, 46, "#fff", 800); T(x, "Swipe →", H - 150, 44, C.yellow, 800); footer(x, H); out.push(c); }
    facts.forEach(([h, d, col], i) => {
      const [c, x] = canvas(H, "#06121f", "#14304a");
      N(x, String(5 - i), 360, 300, col);
      x.fillStyle = "rgba(6,4,14,.82)"; x.beginPath(); x.roundRect(90, 600, 900, 300, 26); x.fill(); x.lineWidth = 4; x.strokeStyle = col; x.stroke();
      T(x, h, 700, 84, "#fff", 900, 820); T(x, d, 810, 42, col, 800, 820);
      badge(x, "OFFICIAL", C.green, 1000); footer(x, H); out.push(c);
    });
    { const [c, x] = canvas(H, "#06121f", "#14304a");
      T(x, "WHICH ONE ARE", 440, 96, "#fff"); T(x, "YOU HYPED FOR?", 550, 96, C.yellow);
      T(x, "Comment 1–5 👇", 710, 54, "#fff", 800); T(x, "Follow so you don't miss launch week", 830, 42, C.cyan, 800); footer(x, H); out.push(c); }
    return out;
  }
  const SETS = { leonida, editions, top5 };
  window.__gtaCarousel = async (set, H = 1350) => {
    const cs = SETS[set](H), files = [];
    for (let i = 0; i < cs.length; i++) { const b = await new Promise(r => cs[i].toBlob(r, "image/jpeg", 0.92)); files.push(new File([b], `gta6_${set}_${i + 1}.jpg`, { type: "image/jpeg" })); }
    window.__carouselPreview = cs.map(c => c.toDataURL("image/jpeg", 0.25)); return files;
  };
})();
