# 实施计划：multilingual-blueprint-workflow

## 概览

本计划把已批准的需求与设计拆解为四个阶段的可执行任务清单，对应设计文档中的阶段链路 `A → B → C → D`，每个阶段以一道阶段门（`G_A / G_B / G_C / G_D`）收口。蓝图主轴为 **MeriToken（中文主用名「美誉值」）的深度分析**，每种语言的 `blueprint/` 下固定为 10 份 `.md`：`README.md` + `glossary.md` + 8 份主题文档（`00-readers-guide.md` 至 `07-related-projects.md`）。任务全部落在「文档撰写、Git 操作、shell 校验脚本」三类具体动作上，校验脚本（P1–P10）作为可选项。

文档语言：中文简体。

## 任务清单

- [x] 1. 阶段 A — 仓库清理与 Git 追踪面收敛
  - [x] 1.1 盘点九处 `start.md` 并验证字节数
    - 在仓库根执行 `for f in docs/*/start.md; do printf '%6s  %s\n' "$(wc -c < "$f" | tr -d ' ')" "$f"; done`，将输出粘入 PR 描述
    - 仅当 9 个文件 size 全部为 0 才进入下一步；任一文件 size > 0 则停手并把路径与字节数登记在 PR 中等待 `Human_Reviewer` 决策
    - _Validates: Requirements 1.2, 1.3_
  
  - [x] 1.2 删除全部 9 个空白 `start.md`
    - 对九种语言（`de / en / es / fr / ja / ko / ru / zh-CN / zh-TW`）执行 `git rm docs/{lang}/start.md`（已追踪）或 `rm`（未追踪）
    - 删除后用 `find docs -name 'start.md' -type f` 验证输出为空
    - _Validates: Property 1, Requirements 1.1, 1.4_
  
  - [x] 1.3 写入仓库根 `.gitignore`
    - 按设计文档「Git 追踪策略数据模型」章节的草案内容写 `.gitignore`：先 `*` 全忽略，再反向放行 `.gitignore / README.md / LICENSE / .kiro/ / .kiro/** / docs/ / docs/**`，最后追加 `docs/**/.DS_Store` 等杂项屏蔽规则
    - _Validates: Requirements 2.1, 2.2, 2.3_
  
  - [x] 1.4 收敛已追踪文件至白名单
    - 执行 `git ls-files` 列出当前追踪面，对每个不在 `Tracked_Path_Whitelist = {docs/, README.md, LICENSE, .gitignore, .kiro/}` 内的路径执行 `git rm --cached -r <path>`（保留工作区文件）
    - 提交一次 commit message 含 `shrink tracked surface` 的提交
    - _Validates: Requirements 2.6_
  
  - [x] 1.5 用 `git check-ignore` 验证白名单/黑名单两类样本
    - 白名单样本（应不命中、退出码 1）：`docs/zh-CN/blueprint/00-readers-guide.md`、`README.md`、`.kiro/specs/multilingual-blueprint-workflow/design.md`、`LICENSE`
    - 黑名单样本（应命中、退出码 0）：`scratch.txt`、`build/output.json`、`docs/en/blueprint/node_modules/foo.js`、`tmp/secret.env`
    - 把每个 `git check-ignore -v` 调用与退出码记录到 PR 描述中
    - _Validates: Requirements 2.4, 2.5_
  
  - [ ]* 1.6 编写 P1 校验脚本
    - 在 `scripts/check/p1-no-startmd.sh` 中实现：`find docs -name 'start.md' -type f` 输出非空时退出码非 0
    - _Validates: Property 1, Requirements 1.1_
  
  - [ ]* 1.7 编写 P2 校验脚本
    - 在 `scripts/check/p2-tracked-surface.sh` 中实现：对设计文档列举的白/黑样本数组逐项 `git check-ignore -v` 并断言退出码；同时断言 `git ls-files` 全集是白名单展开后的子集
    - _Validates: Property 2, Requirements 2.1, 2.2, 2.3, 2.4, 2.5, 2.6_
  
  - [x] 1.8 阶段门 G_A 校验与签字
    - 重新跑一次 `find docs -name 'start.md' -type f` 与样本 `git check-ignore -v` 套件，记录全部通过
    - 在合并 commit 中加入 trailer：`Stage-Gate: G_A-passed` 和 `Reviewed-by: <Reviewer Name> <email>`
    - _Validates: Property 1, Property 2, Requirements 1.1, 2.1, 2.4, 2.5, 2.6_

- [x] 2. 阶段 B — 撰写 zh-CN 蓝图（MeriToken 为主轴）
  - [x] 2.1 建立 `docs/zh-CN/blueprint/` 目录骨架
    - 确认 `docs/zh-CN/blueprint/illustration/` 已存在且 14 张既有 PNG 在位（`credential-management.png`、`ifay-title-banner.png`、`ifay-vs-agent.png`、`ifay-framework-alpha1.png`、`human-operation-era.png`、`phase{1..4}-{concept,architecture}.png`、`phase5-concept.png`）
    - 在 `docs/zh-CN/blueprint/` 下预创建 10 个 `.md` 占位（`README.md`、`glossary.md`、`00-readers-guide.md`、`01-meritoken-overview.md`、`02-meritoken-technical.md`、`03-meritoken-social.md`、`04-meritoken-usage.md`、`05-meritoken-credential.md`、`06-meritoken-deep-cases.md`、`07-related-projects.md`）
    - 备注：本任务在旧 design 下创建过 16 份 `.md` 占位；2.4 会清理旧主题文件，2.5–2.7 按新骨架重新撰写
    - _Validates: Requirements 4.1, 4.2_
  
  - [x] 2.2 撰写 `docs/zh-CN/blueprint/glossary.md`
    - 按设计文档「`glossary.md` 模板」重写为三段结构：
      - 「Reserved_Term」表（4 列）：覆盖 6 个 `Reserved_Term`（`ifay / agent / phase / credential / GMC / Fay`，**不含 `MeriToken`**），并填入 `Upstream_Project_Doc_Link` 钉死表的 4 行（ifay → `https://ifay.ai/docs/ifay`；agent → `https://ifay.ai/docs/agent`；GMC → `https://ifay.ai/docs/gmc`；Fay → `https://ifay.ai/docs/fay`），`phase` 与 `credential` 的参考链接列填 `—`
      - 「Localized_Term」表（3 列）：单行，英文原词 `MeriToken` / 中文主用名「美誉值」/ 处理规则（zh-CN/zh-TW 主用「美誉值」并允许首次括注 `MeriToken`；其他 7 种语言主用 `MeriToken` 不出现「美誉值」字样）
      - 「MeriToken_Chinese_Name 备注」段：明确「美誉值」仅出现在 zh-CN / zh-TW 蓝图正文
      - 「非 Reserved 词条」表：含「蓝图」「校对」「凭证管理」等本地化词条
    - 为 `GMC` 行写明 `Global Merit Chain` 全称、与 `MeriToken` 的从属关系
    - 为 `Fay` 行写明「在 ifay 体系内承担『引用 MeriToken』职责的非个人主体」角色定位
    - _Validates: Property 4, Property 4', Property 10, Requirements 3.1, 3.2, 3.3, 3.4, 3.5, 3.8, 3.9, 3.11_
  
  - [x] 2.3 撰写 `docs/zh-CN/blueprint/README.md`（Blueprint_Index）
    - 按设计文档「`Blueprint_Index`（README.md）模板」生成「阅读顺序」表：8 行，覆盖 `Topic_Slug` 集合（00–07），列含序号 / 文件链接 / 主题 / 关联插图
      - 00 行关联 `ifay-title-banner.png`（可选）
      - 01–04 行关联各自的「待补图」slot（`meritoken-overview-contract` / `meritoken-technical-flow` / `meritoken-social-mapping` / `meritoken-usage-comparison`）
      - 05 行关联 `credential-management.png`（暂复用），并登记待补图 `meritoken-credential-boundary`
      - 06 行登记「待补图（slot 由本篇按需登记）」
      - 07 行关联 `ifay-framework-alpha1.png` 等可选辅助
    - 增加「相关项目（外链）」段，简述 `07-related-projects.md` 收敛 ifay / GMC / Fay / agent / phase / 整体框架等上游议题，外链指向 ifay.ai
    - 「待补图清单」按 6 项 slot（01 / 02 / 03 / 04 / 05 / 06）逐项列出
    - 末尾保留「术语表」入口链接
    - _Validates: Property 9, Property 10, Requirements 4.1, 4.3, 4.7, 4.8_
  
  - [x] 2.4 删除旧蓝图主题文档
    - 删除 13 个旧主题 `.md`：`docs/zh-CN/blueprint/00-overview.md`、`01-human-operation-era.md`、`02-ifay-vs-agent.md`、`03-framework.md`、`04-phase1.md`、`05-phase2.md`、`06-phase3.md`、`07-phase4.md`、`08-phase5.md`、`09-credential-management.md`、`10-meritoken-overview.md`、`11-meritoken-technical.md`、`12-meritoken-social.md`、`13-meritoken-usage.md`
    - 用 `ls docs/zh-CN/blueprint/*.md` 验证剩余 `.md` 集合恰为新 `Topic_Slug` 集合 + `README.md` + `glossary.md`，共 10 项
    - _Validates: Property 5, Property 9, Requirements 4.2_
  
  - [x] 2.5 撰写 `00-readers-guide.md` 与 `07-related-projects.md`（外围 / 阅读指南组）
    - `00-readers-guide.md`：按通用骨架（背景 / 核心内容 / 与其他主题的关系 / 术语脚注）极简撰写，定位蓝图、刻画读者画像、给出阅读路径建议，引导读者直接进入 MeriToken 主线（01–06）；可选在章首引用 `./illustration/ifay-title-banner.png` 作横幅
    - `07-related-projects.md`：按设计中的专用变体骨架撰写，二级标题集合 = `{背景, 与本蓝图的关系, 官方文档外链清单, 术语脚注}`；「官方文档外链清单」表 4 行，对 ifay / GMC / Fay / agent 各给「一句话定位」并填入 `https://ifay.ai/docs/{ifay,gmc,fay,agent}`；可选引用 1–3 张 ifay/phase 系列既有 PNG 作辅助
    - 全部 `Reserved_Term` 出现处保留英文原词；`MeriToken` 概念按 `Localized_Term` 规则在 zh-CN 中主用「美誉值」
    - _Validates: Property 3, Property 9, Property 10, Requirements 4.7, 4.8_
  
  - [x] 2.6 撰写 MeriToken 主题集合主体（`01-meritoken-overview.md` 至 `04-meritoken-usage.md`）
    - `01-meritoken-overview.md`：按设计中的固定骨架（`## 背景` / `## 核心内容` → `### 美誉值（MeriToken）与 GMC 的从属关系` / `### 独立成项目的两项理由` 下含 `#### 作为新社会的契约部件` 与 `#### 作为新社会的社会关系连接器` / `## 与其他主题的关系` / `## 术语脚注`）撰写；正文文本须同时包含「美誉值」「MeriToken」「GMC」「契约部件」「社会关系连接器」五个关键短语；按「⏳ 待补图」占位符样式登记 slot `meritoken-overview-contract`
    - `02-meritoken-technical.md`：三级标题集合 = `{加密, 存储, 取用, 隐私保证, 所有权与使用权保证}`；登记待补图 slot `meritoken-technical-flow`
    - `03-meritoken-social.md`：三级标题集合 = `{社会关系, 政治逻辑, 经济结构, 个人成长映射, 个人贡献与社会话语权的映射含义}`；登记待补图 slot `meritoken-social-mapping`
    - `04-meritoken-usage.md`：三级标题 = `{个人主体的引用方式与应用场景, Fay 主体的引用方式与应用场景}`，每个三级标题下含 `#### 引用方式` 与 `#### 应用场景示例`；登记待补图 slot `meritoken-usage-comparison`
    - 全文使用「美誉值」作为 MeriToken 的中文主用名（首次出现处可括注 `MeriToken`，全文再使用「美誉值」）
    - 全部 `Reserved_Term` 出现处保留英文原词
    - _Validates: Property 3, Property 4', Property 6, Property 8, Requirements 4.4, 4.5, 4.6, 4.11_
  
  - [x] 2.7 撰写 MeriToken 主题集合支撑面（`05-meritoken-credential.md`、`06-meritoken-deep-cases.md`）
    - `05-meritoken-credential.md`：三级标题集合 = `{credential 的角色定位, 美誉值（MeriToken）的角色定位, 边界与对位关系}`；强制引用 `./illustration/credential-management.png`；登记待补图 slot `meritoken-credential-boundary`（过渡期可暂复用 `credential-management.png`）
    - `06-meritoken-deep-cases.md`：扩展位骨架（`## 背景` / `## 核心内容` 下至少两个 `###` 专题，例如「跨主体协作中的高密度使用」「滚动场景」 / `## 与其他主题的关系` / `## 术语脚注`）；待补图 slot 由本篇按需登记
    - 「美誉值」为主用名；`Reserved_Term` 保留英文原词
    - _Validates: Property 3, Property 4', Property 6, Requirements 4.4, 4.5_
  
  - [ ]* 2.8 编写 P3 校验脚本
    - 在 `scripts/check/p3-image-path.sh` 中实现：用 ripgrep 提取所有 Markdown 图片路径，逐项 `realpath -m` 解析，断言落入 `docs/zh-CN/blueprint/illustration/` 且文件存在
    - 输入是 `.md` 中实际出现的图片引用，**不要求 `illustration/` 下所有图片都被引用**（孤立 PNG 允许存在）
    - _Validates: Property 3, Requirements 4.9, 5.8, 6.7, 7.4_
  
  - [ ]* 2.9 编写 P5 校验脚本
    - 在 `scripts/check/p5-filename-set.sh` 中实现：对每种已扇出语言取 `ls docs/{lang}/blueprint/*.md` basename 排序后 `diff` 比较 `zh-CN`
    - 基准 `Topic_Slug` 集合为 10 项：`README.md / glossary.md / 00-readers-guide.md / 01-meritoken-overview.md / 02-meritoken-technical.md / 03-meritoken-social.md / 04-meritoken-usage.md / 05-meritoken-credential.md / 06-meritoken-deep-cases.md / 07-related-projects.md`
    - _Validates: Property 5, Requirements 4.2, 5.2, 6.3, 7.1_
  
  - [ ]* 2.10 编写 P6 校验脚本
    - 在 `scripts/check/p6-heading-sequence.sh` 中实现：对每个同名文件抽取 ATX 标题层级序列后 `diff` 比较 `zh-CN`
    - _Validates: Property 6, Requirements 4.3, 7.2, 7.3_
  
  - [ ]* 2.11 编写 P8 校验脚本
    - 在 `scripts/check/p8-meritoken-subtopics.sh` 中实现：对 `01/02/03/04-meritoken-*.md` 四篇文档分别 grep 三级标题集合与关键短语断言（`01` 检查「GMC」「契约部件」「社会关系连接器」三个关键短语 + 二级骨架；`02/03/04` 检查各自三级标题集合）
    - _Validates: Property 8, Requirements 4.5, 4.6_
  
  - [x] 2.12 阶段门 G_B 校验与签字
    - 跑一遍 P3 / P5（仅 zh-CN 文件名集合自检 10 项）/ P6（仅 zh-CN 自检）/ P8 / P9（仅 zh-CN）/ P10（仅 zh-CN）的人工断言；不依赖 2.8–2.11 / 2.13–2.15 的脚本，可用 `find`、`ls`、`grep` 临时验证
    - `Human_Reviewer` 通读 `docs/zh-CN/blueprint/` 全部 10 份文档
    - 在合并 commit 中加入 trailer：`Stage-Gate: G_B-passed` 与 `Reviewed-by: <Reviewer Name> <email>`
    - _Validates: Property 3, Property 5, Property 6, Property 8, Property 9, Property 10, Requirements 4.1, 4.2, 4.3, 4.7, 4.8, 8.2_
  
  - [ ]* 2.13 编写 P4' 校验脚本（Localized_Term 命名规则）
    - 在 `scripts/check/p4prime-localized-term.sh` 中实现 `Localized_Term_Guard` 逻辑：对每个同名文件计算 `concept_count = count("美誉值") + count("MeriToken")`，按三个分支断言
      - zh-CN：`count("美誉值") ≥ count("MeriToken")` 且当 `concept_count > 0` 时「美誉值」≥ 1
      - zh-TW：同 zh-CN 规则；且 `concept_count(zh-TW) ≥ concept_count(zh-CN)`
      - 其他 7 种语言（en / de / es / fr / ja / ko / ru）：`count("MeriToken") ≥ concept_count(zh-CN)` 且 `count("美誉值") == 0`
    - 显式跳过 `glossary.md`（按 Property 4' 适用范围豁免）
    - _Validates: Property 4', Requirements 3.3, 3.4, 3.5, 4.11, 5.5, 5.6, 6.5, 7.6_
  
  - [ ]* 2.14 编写 P9 校验脚本（Topic_Slug 集合分配）
    - 在 `scripts/check/p9-topic-slug-allocation.sh` 中实现：对 `docs/{lang}/blueprint/*.md` 文件名做前缀分类计数，断言 `M(lang) ≥ O(lang)` 且 `M(lang) ≥ 3`，且文件名以 `07-related-` 开头的主题文件计数 == 1
    - `M(lang)` = 文件名以 `01-meritoken-` / `02-meritoken-` / `03-meritoken-` / `04-meritoken-` / `05-meritoken-` / `06-meritoken-` 开头的计数；`O(lang)` = 其余主题文件计数（`00-readers-guide.md` 与 `07-related-projects.md`）
    - _Validates: Property 9, Requirements 4.4, 4.5, 4.8_
  
  - [ ]* 2.15 编写 P10 校验脚本（Upstream_Project_Doc_Link 跨语言完整性）
    - 在 `scripts/check/p10-upstream-doc-link.sh` 中实现：对每种语言 `glossary.md` 解析 ifay / GMC / Fay / agent 四行的「参考链接」列，断言均含 `https://ifay.ai/` 前缀；并对同语言 `07-related-projects.md` 用 `grep -c 'https://ifay\.ai/'` 断言出现次数 ≥ 4
    - _Validates: Property 10, Requirements 3.8, 3.9, 3.11, 4.7, 4.8, 7.7_

- [x] 3. 阶段 C — 一级扇出 zh-CN → {zh-TW, ja, ko, en}
  - [x] 3.1 扇出至 zh-TW
    - 按设计「翻译流水线设计」的 system prompt 模板，把 `docs/zh-CN/blueprint/glossary.md` 与「大陆—台湾用语对照表」一同注入 `Translation_Tool`
    - 逐文件翻译 10 份 `.md`（`README.md`、`glossary.md`、`00-readers-guide.md` 至 `07-related-projects.md`）至 `docs/zh-TW/blueprint/`
    - 保持文件名集合、章节层级、Mermaid / 表格 / 图片语法不变；图片相对路径改写为 `../../zh-CN/blueprint/illustration/{filename}.png`
    - `Reserved_Term`（`ifay / agent / phase / credential / GMC / Fay`，6 项，**不含 MeriToken**）保留英文原词
    - 按 `Localized_Term` 规则处理 MeriToken / 美誉值：zh-TW 主用「美誉值」，并允许首次括注 `MeriToken`
    - 完成「大陆—台湾用语对照检查」：用对照表（軟體 / 網路 / 程式 / 資訊 / 使用者 / 列印 / 檔案 / 資料 / 預設 / 影片 / 伺服器 / 記憶體 / 函式 / 滑鼠 / 選單 / 字元 / 最佳化 等）逐项替换；对全目录扫描简体差异字符黑名单，命中数为 0 才放行
    - `Human_Reviewer` 通读 `docs/zh-TW/blueprint/`
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [x] 3.2 扇出至 ja
    - 按 system prompt 模板注入 `glossary.md`，逐文件翻译 10 份 `.md` 至 `docs/ja/blueprint/`
    - 保持文件名集合、章节层级、Mermaid / 表格 / 图片语法不变；图片相对路径改写为 `../../zh-CN/blueprint/illustration/{filename}.png`
    - `Reserved_Term`（6 项，不含 MeriToken）保留英文原词
    - 按 `Localized_Term` 规则处理 MeriToken / 美誉值：ja 主用 `MeriToken`，正文不出现「美誉值」字样
    - `Human_Reviewer` 通读 `docs/ja/blueprint/`
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 5.1, 5.2, 5.3, 5.5, 5.6, 5.7, 5.8, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [x] 3.3 扇出至 ko
    - 按 system prompt 模板注入 `glossary.md`，逐文件翻译 10 份 `.md` 至 `docs/ko/blueprint/`
    - 保持文件名集合、章节层级、Mermaid / 表格 / 图片语法不变；图片相对路径改写为 `../../zh-CN/blueprint/illustration/{filename}.png`
    - `Reserved_Term`（6 项，不含 MeriToken）保留英文原词
    - 按 `Localized_Term` 规则处理 MeriToken / 美誉值：ko 主用 `MeriToken`，正文不出现「美誉值」字样
    - `Human_Reviewer` 通读 `docs/ko/blueprint/`
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 5.1, 5.2, 5.3, 5.5, 5.6, 5.7, 5.8, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [x] 3.4 扇出至 en（同时是阶段 D 的中转源）
    - 按 system prompt 模板注入 `glossary.md`，逐文件翻译 10 份 `.md` 至 `docs/en/blueprint/`
    - 保持文件名集合、章节层级、Mermaid / 表格 / 图片语法不变；图片相对路径改写为 `../../zh-CN/blueprint/illustration/{filename}.png`
    - `Reserved_Term`（6 项，不含 MeriToken）保留英文原词；对 `agent` 仅在专有名词语义下保留英文原形（日常用语段落允许出现额外的 `agent`）
    - 按 `Localized_Term` 规则处理 MeriToken / 美誉值：en 主用 `MeriToken`，正文不出现「美誉值」字样
    - `Human_Reviewer` 通读 `docs/en/blueprint/`，因 `en` 作为二级源校对必须充分
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 5.1, 5.2, 5.3, 5.5, 5.6, 5.7, 5.8, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [ ]* 3.5 编写 P4 校验脚本
    - 在 `scripts/check/p4-reserved-term.sh` 中实现：对每个 `Reserved_Term`（`ifay / agent / phase / credential / GMC / Fay`，6 项，**不含 MeriToken**）与每个非 `zh-CN` 同名文件做 `grep -c` 计数比较，目标语言计数 `<` 源语言计数即报 `DRIFT`
    - _Validates: Property 4, Requirements 3.2, 4.11, 5.7, 6.6, 7.5_
  
  - [ ]* 3.6 编写 P7 校验脚本
    - 在 `scripts/check/p7-zhtw-and-no-illustration.sh` 中实现：基于「繁简差异字符」黑名单扫描 `docs/zh-TW/blueprint/*.md` 命中数；并对 8 个非 `zh-CN` 语言断言 `[ ! -d "docs/$lang/blueprint/illustration" ]`
    - _Validates: Property 7, Requirements 5.4, 7.4_
  
  - [x] 3.7 阶段门 G_C 校验与签字
    - 跑一遍 P3 / P4 / P4' / P5 / P6 / P7 / P9 / P10 的人工断言（用临时 shell 一次性验证即可），全部通过
    - 验证 `docs/{zh-TW, ja, ko, en}/blueprint/` 各自含 10 份 `.md` 文件
    - 在合并 commit 中加入 trailer：`Stage-Gate: G_C-passed` 与四份 `Reviewed-by:` trailer，其中 `en` 的 `Reviewed-by:` 必须存在
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 8.2, 8.3_

- [x] 4. 阶段 D — 二级扇出 en → {de, es, fr, ru}
  - [x] 4.1 冻结 `en` 中转源
    - 在 G_C 通过的合并 commit 上打 git tag `en/blueprint@review-passed`
    - 阶段 D 后续翻译均以该 tag 指向的 `docs/en/blueprint/` 为唯一输入源
    - _Validates: Requirements 6.1, 6.2, 8.3_
  
  - [x] 4.2 扇出至 de
    - 以 `en/blueprint@review-passed` 标签下的 `docs/en/blueprint/` 为源，按 system prompt 模板注入 `docs/en/blueprint/glossary.md`
    - 逐文件翻译 10 份 `.md` 至 `docs/de/blueprint/`，保持文件名集合、章节层级、Mermaid / 表格 / 图片语法不变；图片相对路径保持 `../../zh-CN/blueprint/illustration/{filename}.png`
    - `Reserved_Term`（6 项，不含 MeriToken）保留英文原词
    - 按 `Localized_Term` 规则处理 MeriToken / 美誉值：de 主用 `MeriToken`，正文不出现「美誉值」字样
    - `Human_Reviewer` 通读 `docs/de/blueprint/`
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 6.1, 6.3, 6.4, 6.5, 6.6, 6.7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [x] 4.3 扇出至 es
    - 以 `en/blueprint@review-passed` 标签下的 `docs/en/blueprint/` 为源，按 system prompt 模板注入 `docs/en/blueprint/glossary.md`
    - 逐文件翻译 10 份 `.md` 至 `docs/es/blueprint/`，保持文件名集合、章节层级、Mermaid / 表格 / 图片语法不变；图片相对路径保持 `../../zh-CN/blueprint/illustration/{filename}.png`
    - `Reserved_Term`（6 项，不含 MeriToken）保留英文原词
    - 按 `Localized_Term` 规则处理 MeriToken / 美誉值：es 主用 `MeriToken`，正文不出现「美誉值」字样
    - `Human_Reviewer` 通读 `docs/es/blueprint/`
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 6.1, 6.3, 6.4, 6.5, 6.6, 6.7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [x] 4.4 扇出至 fr
    - 以 `en/blueprint@review-passed` 标签下的 `docs/en/blueprint/` 为源，按 system prompt 模板注入 `docs/en/blueprint/glossary.md`
    - 逐文件翻译 10 份 `.md` 至 `docs/fr/blueprint/`，保持文件名集合、章节层级、Mermaid / 表格 / 图片语法不变；图片相对路径保持 `../../zh-CN/blueprint/illustration/{filename}.png`
    - `Reserved_Term`（6 项，不含 MeriToken）保留英文原词
    - 按 `Localized_Term` 规则处理 MeriToken / 美誉值：fr 主用 `MeriToken`，正文不出现「美誉值」字样
    - `Human_Reviewer` 通读 `docs/fr/blueprint/`
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 6.1, 6.3, 6.4, 6.5, 6.6, 6.7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [x] 4.5 扇出至 ru
    - 以 `en/blueprint@review-passed` 标签下的 `docs/en/blueprint/` 为源，按 system prompt 模板注入 `docs/en/blueprint/glossary.md`
    - 逐文件翻译 10 份 `.md` 至 `docs/ru/blueprint/`，保持文件名集合、章节层级、Mermaid / 表格 / 图片语法不变；图片相对路径保持 `../../zh-CN/blueprint/illustration/{filename}.png`
    - `Reserved_Term`（6 项，不含 MeriToken）保留英文原词
    - 按 `Localized_Term` 规则处理 MeriToken / 美誉值：ru 主用 `MeriToken`，正文不出现「美誉值」字样
    - `Human_Reviewer` 通读 `docs/ru/blueprint/`
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 6.1, 6.3, 6.4, 6.5, 6.6, 6.7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [x] 4.6 阶段门 G_D 校验与签字
    - 跑一遍 P3 / P4 / P4' / P5 / P6 / P7 / P9 / P10 的人工断言（针对 `de / es / fr / ru` 四种语言），全部通过
    - 验证 `docs/{de, es, fr, ru}/blueprint/` 各自含 10 份 `.md` 文件
    - 在合并 commit 中加入 trailer：`Stage-Gate: G_D-passed` 与四份 `Reviewed-by:` trailer（`de / es / fr / ru` 各一）
    - _Validates: Property 3, Property 4, Property 4', Property 5, Property 6, Property 7, Property 9, Property 10, Requirements 6.1, 6.3, 6.4, 6.5, 6.6, 6.7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 8.1, 8.4_

## 备注

- 标 `*` 的子任务为可选，主要是 P1–P10 校验脚本的工程化落地；阶段门可先用临时 shell 命令完成等价断言，脚本化可作为后续工程化补强。
- 阶段 C 内部 `3.1 / 3.2 / 3.3 / 3.4` 与阶段 D 内部 `4.2 / 4.3 / 4.4 / 4.5` 在阶段门未启动前可并行推进。
- 每个阶段门任务都要求 commit trailer 留痕（`Stage-Gate: G_X-passed` 与 `Reviewed-by:`），是阶段切换的硬约束。
- 上游修订的下游同步策略详见设计文档「风险与权衡」章节，本计划在初次扇出完成后再按需触发，不作为常规任务列出。
