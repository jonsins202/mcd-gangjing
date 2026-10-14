# 传播卡片模板

两种卡：《劝退卡》（用户被劝退时）与《通关卡》（用户扛过全部关卡下单成功时）。风格：麦门黄红配色、大字标语、截图友好（固定宽度 480px，适合手机竖屏截图转发）。

生成规则：
- 单文件 HTML，无外部依赖（样式内联），保存到 `./mcd-gangjing-data/cards/`
- 文件名：`劝退卡_YYYYMMDD_HHMM.html` / `通关卡_YYYYMMDD_HHMM.html`
- 卡片内容全部来自当场的 battle-log 记录与 MCP 真实数据，禁止编造数字

---

## 《劝退卡》模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>麦门劝退卡</title>
<style>
  body { margin:0; padding:24px; background:#f6f6f6; font-family:"PingFang SC","Microsoft YaHei",sans-serif; display:flex; justify-content:center; }
  .card { width:480px; background:#fff; border-radius:16px; overflow:hidden; box-shadow:0 8px 30px rgba(0,0,0,.12); }
  .head { background:linear-gradient(135deg,#ffc72c,#ff8200); padding:28px 24px; color:#292929; }
  .head .tag { display:inline-block; background:#da291c; color:#fff; font-size:12px; font-weight:700; padding:3px 10px; border-radius:99px; letter-spacing:2px; }
  .head h1 { margin:12px 0 4px; font-size:30px; letter-spacing:1px; }
  .head p { margin:0; font-size:13px; opacity:.85; }
  .body { padding:24px; }
  .row { display:flex; justify-content:space-between; padding:12px 0; border-bottom:1px dashed #eee; font-size:15px; }
  .row .k { color:#888; } .row .v { font-weight:700; }
  .money { text-align:center; padding:20px 0 8px; }
  .money .num { font-size:44px; font-weight:800; color:#da291c; }
  .money .cap { font-size:13px; color:#888; }
  .stamp { text-align:center; margin:18px 0 8px; color:#da291c; border:3px solid #da291c; border-radius:8px; display:inline-block; padding:8px 18px; font-weight:800; font-size:20px; transform:rotate(-8deg); letter-spacing:4px; }
  .foot { background:#fafafa; padding:14px 24px; font-size:12px; color:#999; text-align:center; }
  .center { text-align:center; }
</style>
</head>
<body>
<div class="card">
  <div class="head">
    <span class="tag">MCD OFFICIAL-ISH</span>
    <h1>麦门劝退卡</h1>
    <p>本次冲动已被麦门杠精天团依法拦截</p>
  </div>
  <div class="body">
    <div class="row"><span class="k">被拦截冲动</span><span class="v">{想吃的餐品}</span></div>
    <div class="row"><span class="k">迎战杠精</span><span class="v">{杠精名，顿号分隔}</span></div>
    <div class="row"><span class="k">拦截时间</span><span class="v">{YYYY-MM-DD HH:MM}</span></div>
    <div class="money">
      <div class="num">¥{金额}</div>
      <div class="cap">已存入巨无霸基金（虚拟）</div>
    </div>
    <div class="center"><span class="stamp">劝退成功</span></div>
  </div>
  <div class="foot">累计被劝退 {N} 次 · 累计省下 ¥{TOTAL} · 麦门杠精天团 监制</div>
</div>
</body>
</html>
```

---

## 《通关卡》模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>麦门通关卡</title>
<style>
  body { margin:0; padding:24px; background:#f6f6f6; font-family:"PingFang SC","Microsoft YaHei",sans-serif; display:flex; justify-content:center; }
  .card { width:480px; background:#fff; border-radius:16px; overflow:hidden; box-shadow:0 8px 30px rgba(0,0,0,.12); }
  .head { background:linear-gradient(135deg,#292929,#da291c); padding:28px 24px; color:#fff; }
  .head .tag { display:inline-block; background:#ffc72c; color:#292929; font-size:12px; font-weight:700; padding:3px 10px; border-radius:99px; letter-spacing:2px; }
  .head h1 { margin:12px 0 4px; font-size:30px; letter-spacing:1px; }
  .head p { margin:0; font-size:13px; opacity:.85; }
  .body { padding:24px; }
  .row { display:flex; justify-content:space-between; padding:12px 0; border-bottom:1px dashed #eee; font-size:15px; }
  .row .k { color:#888; } .row .v { font-weight:700; }
  .gates { display:flex; gap:8px; flex-wrap:wrap; padding:14px 0; }
  .gate { background:#f4f4f4; border-radius:8px; padding:8px 12px; font-size:13px; }
  .gate.beaten { background:#e8f5e9; color:#2e7d32; font-weight:700; }
  .money { text-align:center; padding:20px 0 8px; }
  .money .num { font-size:44px; font-weight:800; color:#2e7d32; }
  .money .cap { font-size:13px; color:#888; }
  .stamp { text-align:center; margin:18px 0 8px; color:#2e7d32; border:3px solid #2e7d32; border-radius:8px; display:inline-block; padding:8px 18px; font-weight:800; font-size:20px; transform:rotate(-8deg); letter-spacing:4px; }
  .foot { background:#fafafa; padding:14px 24px; font-size:12px; color:#999; text-align:center; }
  .center { text-align:center; }
</style>
</head>
<body>
<div class="card">
  <div class="head">
    <span class="tag">TEAM DEFEATED</span>
    <h1>麦门通关卡</h1>
    <p>杠精天团全员服气，按约定帮你打到了最优价</p>
  </div>
  <div class="body">
    <div class="row"><span class="k">最终订单</span><span class="v">{订单内容}</span></div>
    <div class="row"><span class="k">击败杠精</span><span class="v">{杠精名，顿号分隔}</span></div>
    <div class="row"><span class="k">支付时间</span><span class="v">{YYYY-MM-DD HH:MM}</span></div>
    <div class="gates">
      <div class="gate beaten">🏋️ 铁蛋 ✔</div>
      <div class="gate beaten">💼 钱总 ✔</div>
      <div class="gate beaten">💔 小艾 ✔</div>
      <div class="gate beaten">🎣 老六 ✔</div>
      <div class="gate beaten">👔 王总 ✔</div>
    </div>
    <div class="money">
      <div class="num">省 ¥{金额}</div>
      <div class="cap">券后实际支付 ¥{实付}（原价 ¥{原价}）</div>
    </div>
    <div class="center"><span class="stamp">批准食用</span></div>
  </div>
  <div class="foot">历史战绩：通关 {W} 次 · 被劝退 {R} 次 · 麦门杠精天团 监制</div>
</div>
</body>
</html>
```

**使用说明**：生成卡片时按当场实际出战杠精渲染 `.gate` 列表（未出战的不显示，被说服放行的显示 ✔，用户中途弃权的关卡显示「未迎战」灰色）。金额与省额必须来自 `calculate-price` 返回值。

**头像嵌入**：`.gate` 条目使用 base64 内联头像（assets/personas/ 下对应立绘，缩放至 64px 宽再编码），格式 `<img src="data:image/png;base64,{...}" style="width:24px;vertical-align:-6px;border-radius:50%;"> 铁蛋 ✔`。《通关卡》头部右侧放大展示用户击败的头像串（48px 圆形），让卡片有"收集勋章"感。
