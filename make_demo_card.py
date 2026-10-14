# -*- coding: utf-8 -*-
"""生成嵌头像的演示《劝退卡》HTML"""
import base64
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def b64(p):
    with open(p, 'rb') as f:
        return base64.b64encode(f.read()).decode()

tiedan = b64('assets/personas/tiedan.png')
wangzong = b64('assets/personas/wangzong.png')

def avatar(b, size=24):
    return '<img src="data:image/png;base64,%s" style="width:%dpx;vertical-align:-6px;border-radius:50%%;">' % (b, size)

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>麦门劝退卡</title>
<style>
  body { margin:0; padding:24px; background:#f6f6f6; font-family:"PingFang SC","Microsoft YaHei",sans-serif; display:flex; justify-content:center; }
  .card { width:480px; background:#fff; border-radius:16px; overflow:hidden; box-shadow:0 8px 30px rgba(0,0,0,.12); }
  .head { background:linear-gradient(135deg,#ffc72c,#ff8200); padding:28px 24px; color:#292929; position:relative; }
  .head .tag { display:inline-block; background:#da291c; color:#fff; font-size:12px; font-weight:700; padding:3px 10px; border-radius:99px; letter-spacing:2px; }
  .head h1 { margin:12px 0 4px; font-size:30px; letter-spacing:1px; }
  .head p { margin:0; font-size:13px; opacity:.85; }
  .head .hero { position:absolute; right:18px; bottom:-14px; width:96px; height:96px; border-radius:50%; background:#fff; border:3px solid #da291c; overflow:hidden; display:flex; align-items:center; justify-content:center; }
  .head .hero img { width:88px; }
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
    <div class="hero"><img src="data:image/png;base64,__TIEDAN__"></div>
  </div>
  <div class="body">
    <div class="row"><span class="k">被拦截冲动</span><span class="v">巨无霸</span></div>
    <div class="row"><span class="k">迎战杠精</span><span class="v">__AV_TIEDAN__ 铁蛋 · __AV_WANGZONG__ 王总</span></div>
    <div class="row"><span class="k">拦截时间</span><span class="v">2026-10-14 21:40</span></div>
    <div class="money">
      <div class="num">¥24.5</div>
      <div class="cap">已存入巨无霸基金（虚拟）</div>
    </div>
    <div class="center"><span class="stamp">劝退成功</span></div>
  </div>
  <div class="foot">累计被劝退 1 次 · 累计省下 ¥24.5 · 麦门杠精天团 监制</div>
</div>
</body>
</html>"""

html = html.replace('__TIEDAN__', tiedan)
html = html.replace('__AV_TIEDAN__', avatar(tiedan))
html = html.replace('__AV_WANGZONG__', avatar(wangzong))

os.makedirs('demo', exist_ok=True)
with open('demo/劝退卡_demo.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('demo card written, bytes:', len(html))
