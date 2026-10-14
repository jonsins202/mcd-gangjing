# workbuddy.md · 开发对话上下文

本文档记录「麦门杠精天团 McAtheists」使用腾讯 WorkBuddy 完整开发的对话上下文，用于 McDonald's 程序员创意开发大赛 WorkBuddy 联动专项奖励核验。

## 开发环境

- 工具：腾讯 WorkBuddy（Agent 模式，全程 AI 结对开发）
- MCP：麦当劳中国官方 MCP Server（https://mcp.mcd.cn，Streamable HTTP）
- 时间：2026 年 10 月 14 日 20:55 — 22:18（GMT+8）

## 开发过程实录（按时间线）

### 阶段一：接入麦当劳 MCP（20:55-21:10）

**用户**：安装这个 skill：https://github.com/M-China/mcd-mcp-server

**WorkBuddy**：识别出该仓库为麦当劳中国官方远程托管 MCP 服务而非本地 Skill。引导用户在 open.mcd.cn/mcp 申请 Token → 写入 WorkBuddy MCP 配置（`~/.workbuddy/mcp.json`，streamablehttp + Bearer Token）→ 修复用户填 Token 时覆盖掉的 `Bearer ` 前缀 → curl 实测 initialize 返回 200 → 指引用户在连接器管理页信任 mcd-mcp。

**验证调用**：信任后实测 3 个工具全部连通——campaign-calendar（拉到当月 13 个活动）、available-coupons（7 张可领券）、query-my-account（积分账户）。

### 阶段二：赛事调研与选题（21:12-21:30）

**用户**：我正在参加这个比赛……帮我想想 idea 怎么把这个麦当劳 mcp 做成一个日常大家真的选麦当劳时会用的小项目，实用或者有趣，不要和市面上的雷同。

**WorkBuddy**：
1. 抓取比赛页面，提炼关键规则：排名 100% 按 GitHub Star 数、10/25 截止、必含 5 个指定文件、CONTEST_DECLARATION.md 须原样复制、mcp-config.example.json 仅允许环境变量占位符
2. 扫描 RANKING.md 全部 104 个上榜项目与最新报名 Issue，标注已饱和赛道（省钱/热量/联名雷达/团餐/MBTI/抽奖/游戏）
3. 产出 3 个未撞车方案：A 法庭审判（McCourt）、B 戒断所（McRehab）、C 杠精天团（McAtheists）

**用户**：方案C吧

### 阶段三：Skill 开发（21:26-21:33）

WorkBuddy 一次成型搭建全部项目文件：
- `SKILL.md`：核心玩法引擎——开场宣战 → 场景加权抽杠精（now-time-info 判断深夜/发薪日）→ 逐关拷问（每杠精绑定一个 MCP 数据源）→ 劝退结算 / 通关变脸点餐 → battle-log.json 战绩档案
- `references/personas.md`：五位杠精人格档案（铁蛋/钱总/小艾/老六/王总），每人含数据源、登场话术、拷问方向、放行条件、认输台词
- `references/cards.md`：《劝退卡》《通关卡》单文件 HTML 模板（480px 手机截图友好）
- `MCP_INTEGRATION.md`：12 个 MCP 工具完整映射表 + 守关/变脸两条调用流程
- `README.md` / `CONTEST_DECLARATION.md`（官方原样）/ `mcp-config.example.json`

### 阶段四：安装实测（21:33-21:41）

**用户**：可以，装吧

WorkBuddy 将 Skill 安装至 `~/.workbuddy/skills/mcd-gangjing/`，随即发起真实对局：
- 并行调用 now-time-info + list-nutrition-foods + order-list
- 基于真实数据即兴演出：21:34 未到深夜档（前任候场未上）、用户订单为空（钱总/小艾"弹尽粮绝退赛"）、巨无霸实拉数据 513 大卡/26g 脂肪/961mg 钠
- 第一关铁蛋发起拷问，用户答"没运动想犒劳自己"，铁蛋给出降级方案（巨无霸→麦乐鸡 5 块，省 300 大卡）

### 阶段五：视觉系统（21:41-22:04）

**用户**：感觉现在这个skill没有视觉物料，不够美观呀，能不能植入点视觉图片

WorkBuddy 方案：5 张透明底 chibi 贴纸立绘（每人对应数据武器道具）+ 1 张天团海报。生成过程发现 ImageGen 并行生成会因时间戳同名互相覆盖（首批 5 张覆盖只剩废片），改为**串行生成+立即重命名**解决，最终 6 张资产完好。随后：
- README 嵌入海报门头 + 立绘阵容表
- SKILL.md 新增「视觉物料」规则（登场展示立绘）
- cards.md 升级头像嵌入规范（base64 内联圆形头像）
- make_demo_card.py 生成嵌真实头像的《劝退卡》演示件

### 阶段六：发布准备（22:04-22:18）

盘点剩余步骤 → 用户提供 GitHub 账号（jonsins202）→ 本地 git init + commit（19 文件）→ push 因代理节点故障暂缓（commit 已完好保存）→ 本文档即该阶段产物。

## WorkBuddy 在本项目中的角色

| 环节 | WorkBuddy 做了什么 |
|---|---|
| MCP 接入 | 配置写入、Token 格式修复、连通性验证 |
| 赛事情报 | 规则提炼、104 项目赛道扫描、撞车规避 |
| 创意 | 3 案对比 → 杠精天团概念（反向下单守门人） |
| 开发 | 全部 7 个核心文件一次成型 |
| 测试 | 真实 MCP 数据驱动的半局对局实测 |
| 视觉 | 6 张角色资产生成与全项目视觉接线 |
| 发布 | git 初始化、提交、发布物料 |

## 复现指引

1. 申请麦当劳 MCP Token：https://open.mcd.cn/mcp
2. 按仓库 `mcp-config.example.json` 配置 WorkBuddy 自定义连接器并信任
3. `git clone https://github.com/jonsins202/mcd-gangjing.git ~/.workbuddy/skills/mcd-gangjing`
4. 在 WorkBuddy 中说「我想吃巨无霸」，天团自动开庭
