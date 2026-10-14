# 麦门杠精天团 · 标准战斗 UI 规范（v1，2026-10-14 实测定型）

所有场景（关卡登场、裁决反馈、结算、终局点餐）统一「双件套」：视觉卡片（预览面板）+ 操作面板（对话内按钮组件）。

## 配色令牌（McDonald's 官方色）

| 用途 | 色值 |
|---|---|
| 暗色卡背景 | `#1A1A1A` |
| 卡内次级面板 | `#262626` / `#1F1F1F` |
| 边框（暗卡） | `#333` / `#3A3A3A` |
| 麦门红（主行动/强调） | `#DA291C` |
| 薯条黄（主按钮/标题/M标） | `#FFC72C` |
| 黄色渐变尾 | `#FFAB00` |
| 正文白 | `#FFFFFF` |
| 次级文本 | `#BBBBBB` / `#9A9A9A` |
| 弱文本 | `#777777` |
| 危险/热量红 | `#FF6B6B` |
| 蛋白质绿 | `#6BCB77` |

字体：`"Microsoft YaHei", system-ui, sans-serif`；标题用 Arial Black 系 M 标。

## 操作面板（show_widget 按钮组件模板）

```html
<style>
.mcard{background:#1A1A1A;border-radius:16px;padding:16px;font-family:"Microsoft YaHei",system-ui,sans-serif;}
.mhead{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
.mlogo{color:#FFC72C;font-weight:800;font-size:20px;font-family:Arial Black,Arial,sans-serif;letter-spacing:-1px;}
.mtitle{color:#fff;font-size:14px;font-weight:500;}
.msub{color:#9a9a9a;font-size:12px;margin-left:auto;}
.mbtn{display:flex;align-items:center;gap:12px;width:100%;box-sizing:border-box;border:none;border-radius:999px;padding:12px 18px;margin-bottom:10px;cursor:pointer;font-size:14px;font-weight:700;font-family:inherit;text-align:left;transition:transform .1s;}
.mbtn:active{transform:scale(.98);}
.chip{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;flex-shrink:0;}
.arrow{margin-left:auto;font-size:16px;font-weight:700;}
</style>
<div class="mcard">
<h2 class="sr-only">（无障碍一句话摘要）</h2>
<div class="mhead"><span class="mlogo">M</span><span class="mtitle">（标题）</span><span class="msub">（提示语）</span></div>
<button class="mbtn" style="background:#FFC72C;color:#1A1A1A;" onclick="sendPrompt('（选项A发出的消息）')">
<span class="chip" style="background:#DA291C;color:#fff;">A</span>（选项文案）<span class="arrow">›</span>
</button>
<button class="mbtn" style="background:#DA291C;color:#fff;" onclick="sendPrompt('（选项B）')">
<span class="chip" style="background:#FFC72C;color:#1A1A1A;">B</span>（选项文案）<span class="arrow">›</span>
</button>
<button class="mbtn" style="background:#DA291C;color:#fff;" onclick="sendPrompt('（选项C）')">
<span class="chip" style="background:#FFC72C;color:#1A1A1A;">C</span>（选项文案）<span class="arrow">›</span>
</button>
<button class="mbtn" style="background:#1A1A1A;color:#FFC72C;border:2px solid #FFC72C;" onclick="sendPrompt('（选项D·快捷出口）')">
<span class="chip" style="background:#FFC72C;color:#1A1A1A;">D</span>（快捷出口文案）<span class="arrow">›</span>
</button>
</div>
```

规则：
- 第一个（推荐/主）按钮用薯条黄底红 chip；其余麦门红底黄 chip；快捷出口（"少废话直接点"）用描边幽灵按钮
- 选项即消息：onclick sendPrompt 的文案要能独立成句（用户点了就等于替他发言）
- 覆盖当前杠精的裁决分支 + 始终保留快捷出口

## 视觉卡片（登场卡/结算卡，present_files 打开）

- 结构参照 `McGangJing/gate-cards/gate1_tiedan.html`（34KB）：头部「第 N 关/共 M 关」黄 tag + 麦门黄标题；左列立绘（**base64 内嵌**，520px 缩略 quantize 160 色，约 30KB）+ 人设 tag；右列台词气泡（黄字高亮关键数据）+ 数据 cell 三连（红/绿/黄着色）+ 渐变拷问条
- 结算卡沿用 `references/cards.md` 模板 + base64 头像
- 立绘内嵌生成代码模式（Python/Pillow）：

```python
def b64_png(path, max_w=520):
    im = Image.open(path).convert("RGBA")
    im.thumbnail((max_w, max_w), Image.LANCZOS)
    q = im.quantize(colors=160, method=Image.FASTOCTREE)
    buf = io.BytesIO(); q.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
```

## 严禁

- ❌ show_widget 内用 `<img>` 引任何本地文件（全通道被拦，实测）
- ❌ present_files 页面外链本地图片（静态服务器只代理页面本身）
- ❌ 系统默认样式按钮直接裸奔（用户已明确嫌弃）
