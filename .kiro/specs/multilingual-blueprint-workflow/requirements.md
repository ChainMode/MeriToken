# 需求文档

## 简介

本功能为 ifay 项目搭建一条「以中文简体为源、按指定链路扇出至九种语言」的蓝图（blueprint）多语言文档生产流水线，并为仓库建立「仅放行 `docs/` 与少量根文件」的 Git 追踪策略。

本蓝图的中心议题是 **MeriToken（中文主用名「美誉值」）的深度分析**。MeriToken 在新社会中承担「契约部件」与「社会关系连接器」两类基础角色，是本仓库蓝图文档的主轴。

ifay 体系、Global Merit Chain（GMC）、Fay、agent 对照、phase 演进路线、整体框架等议题，定位为 MeriToken 分析所需的**支撑性背景**：仅在 MeriToken 的展开必须涉及时给出最小必要的位置说明，并通过外链将读者引导至 ifay.ai 上对应的官方文档页，本仓库内不再对这些上游/外围议题做长篇阐述。

工作链路按阶段串行：

1. 仓库清理与 Git 追踪范围收敛；
2. 在 `docs/zh-CN/blueprint/` 下产出按主题拆分的中文简体蓝图文档集，引用既有插图，并以 MeriToken 为主题中心组织内容；
3. 严格按依赖关系扇出至其他八种语言：`zh-CN → {zh-TW, ja, ko, en}`，待 `en` 完成后再扇出 `en → {de, es, fr, ru}`；
4. 全程使用统一术语表（Glossary）保证专有名词跨语言一致，并对 MeriToken 实施按语言区分的命名规则。

MeriToken 深度分析的最小骨架包含三大子主题：

- **技术原理**：加密、存储、取用、隐私保证、所有权与使用权保证；
- **社会内涵**：MeriToken 延伸出的社会关系、政治逻辑、经济结构、个人成长映射，及其作为「个人贡献与社会话语权」的载体含义；
- **引用与应用**：个人主体如何引用、如何在实际场景中应用，以及 Fay 主体如何引用、如何在实际场景中应用。

## 术语表

- **Repository**：本 Git 仓库（即工作区根目录）。
- **Docs_Root**：仓库内 `docs/` 目录，所有语言文档的根。
- **Language_Code**：受支持的九种语言目录代号集合 `{de, en, es, fr, ja, ko, ru, zh-CN, zh-TW}`。
- **Source_Language**：内容写作的原始语言，固定为 `zh-CN`。
- **Pivot_Language**：在二级扇出阶段充当中转源语言，固定为 `en`。
- **Blueprint_Dir**：某一语言下的蓝图目录，路径形如 `docs/{Language_Code}/blueprint/`。
- **Illustration_Dir**：唯一的插图存放目录，路径为 `docs/zh-CN/blueprint/illustration/`，所有语言文档以相对路径引用。
- **Blueprint_Document_Set**：单一语言下蓝图目录中的所有 `.md` 文件集合，按主题拆分。
- **Blueprint_Index**：蓝图目录入口文件 `README.md`，串联同语言下的全部主题文档。
- **Glossary_File**：术语表文件 `docs/zh-CN/blueprint/glossary.md`（中文简体源），其他语言版本以 `docs/{Language_Code}/blueprint/glossary.md` 存放。
- **Reserved_Term**：术语表中标注「在所有语言版本均保持英文原词不翻译」的专有名词集合，初始包含 `ifay`、`agent`、`phase`、`credential`、`GMC`、`Fay`。该集合不包含 `MeriToken`，`MeriToken` 的命名规则由 `Localized_Term` 单独约束。
- **Localized_Term**：术语表中按语言适用不同呈现形式的专有名词集合。初始成员为 `MeriToken / 美誉值`，规则为「在 `zh-CN` 与 `zh-TW` 蓝图正文中使用中文主用名 `美誉值`，在 `en`、`de`、`es`、`fr`、`ja`、`ko`、`ru` 蓝图正文中使用英文原词 `MeriToken`」。
- **MeriToken_Chinese_Name**：MeriToken 的中文主用名 `美誉值`，仅在 `zh-CN` 与 `zh-TW` 蓝图正文中作为该概念的常规称谓使用。
- **GMC**：Global Merit Chain 的缩写，作为 MeriToken 的上位体系。
- **Fay**：在 ifay 体系内承担「引用 MeriToken」职责的非个人主体，与个人主体并列作为 MeriToken 的两类引用者之一。
- **Upstream_Project_Doc_Link**：指向 ifay.ai 上对应官方文档页的外链集合，用于在本仓库蓝图中替代对上游/外围议题（包括但不限于 `ifay`、`GMC`、`Fay`、`agent`、`phase`、整体框架）的长篇阐述。其链接形态固定为「指向对应官方文档页」，但具体 URL 不在本需求文档中约束，由设计阶段定稿。
- **Translation_Tool**：执行机器翻译的 AI/LLM 辅助工具（具体实现由设计阶段决定）。
- **Human_Reviewer**：完成机器翻译后承担通读校对的人。
- **Gitignore_File**：仓库根目录下的 `.gitignore` 文件。
- **Tracked_Path_Whitelist**：允许被 Git 追踪的路径集合，固定为 `docs/`、`README.md`、`LICENSE`、`.gitignore` 自身、`.kiro/`。
- **Topic_Slug**：蓝图主题文件的命名片段，受控值集合由设计阶段定稿；本需求文档不枚举具体取值，仅约束其命名格式与主题优先级。

## 需求

### 需求 1：清理空白起始文件

**用户故事：** 作为仓库维护者，我希望删除所有语言目录下的空白 `start.md` 文件，以便仓库结构反映实际可见的文档资产，而不是占位符。

#### 验收标准

1. THE Repository SHALL 不包含任何 `docs/{Language_Code}/start.md` 文件，其中 `Language_Code` 取自九种受支持语言目录。
2. WHEN 执行清理操作时，THE Repository SHALL 仅删除大小为 0 字节、且文件名严格等于 `start.md` 的文件。
3. IF 任一 `docs/{Language_Code}/start.md` 文件大小大于 0 字节，THEN THE Repository SHALL 在删除该文件前停止操作并报告该文件的路径与大小。
4. THE Repository SHALL 在清理完成后保留所有非 `start.md` 的现有文件与目录结构不变。

### 需求 2：限定 Git 追踪范围

**用户故事：** 作为仓库维护者，我希望仅将 `docs/` 与少量根级文件推送到 GitHub，以便在文档定稿前避免暴露其他在建内容。

#### 验收标准

1. THE Gitignore_File SHALL 存在于仓库根目录。
2. THE Gitignore_File SHALL 采用「先全量忽略再反向放行」的黑名单兜底策略，对 `Tracked_Path_Whitelist` 之外的所有路径生效忽略。
3. THE Tracked_Path_Whitelist SHALL 至少包含 `docs/`、`README.md`、`LICENSE`、`.gitignore` 自身、`.kiro/`。
4. WHEN 在仓库根目录执行 `git check-ignore -v <path>` 对任一不在 `Tracked_Path_Whitelist` 内的新增路径进行检查时，THE Gitignore_File SHALL 命中该路径为已忽略。
5. WHEN 在仓库根目录执行 `git check-ignore -v <path>` 对 `Tracked_Path_Whitelist` 内任一路径进行检查时，THE Gitignore_File SHALL 不命中该路径为已忽略。
6. IF 已被 Git 追踪的文件位于 `Tracked_Path_Whitelist` 之外，THEN THE Repository SHALL 通过显式取消追踪（如 `git rm --cached`）将其从索引中移除。

### 需求 3：建立蓝图术语表

**用户故事：** 作为多语言译者，我希望有一份权威术语表，以便所有语言版本对专有名词保持一致表达，并对 MeriToken 实施按语言区分的命名规则。

#### 验收标准

1. THE Repository SHALL 在 `docs/zh-CN/blueprint/glossary.md` 存放中文简体源术语表。
2. THE Glossary_File SHALL 至少为 `Reserved_Term` 中的每一个条目（`ifay`、`agent`、`phase`、`credential`、`GMC`、`Fay`）记录英文原词、中文释义与「在所有语言版本保持英文原词」的处理标记。
3. THE Glossary_File SHALL 为 `MeriToken / 美誉值` 单列一条 `Localized_Term` 条目，记录英文原词 `MeriToken`、中文主用名 `美誉值`、以及「`zh-CN` 与 `zh-TW` 正文使用 `美誉值`，其余语言正文使用 `MeriToken`」的处理规则。
4. WHEN 在 `zh-CN` 或 `zh-TW` 蓝图正文中出现 MeriToken 这一概念时，THE Blueprint_Document_Set SHALL 使用 `美誉值` 作为主用名，并允许在该概念于该语言版本首次出现的位置以括注形式标注英文原词 `MeriToken`。
5. WHEN 在 `en`、`de`、`es`、`fr`、`ja`、`ko`、`ru` 蓝图正文中出现该概念时，THE Blueprint_Document_Set SHALL 使用英文原词 `MeriToken`。
6. THE Glossary_File SHALL 为 `GMC` 条目记录其全称 `Global Merit Chain` 与其作为 `MeriToken` 上位体系的从属关系。
7. THE Glossary_File SHALL 为 `Fay` 条目说明其作为「非个人主体的 MeriToken 引用者」的角色定位，以与个人主体相区分。
8. THE Glossary_File SHALL 至少为 `ifay`、`GMC`、`Fay`、`agent` 各记录一条 `Upstream_Project_Doc_Link`，指向 ifay.ai 上对应的官方文档页。
9. THE Glossary_File 中的 `Upstream_Project_Doc_Link` SHALL 在链接形态层面满足「指向对应官方文档页」的要求，具体 URL 路径由设计阶段在 `design.md` 中定稿，本需求文档不约束具体路径。
10. THE Glossary_File SHALL 为非 `Reserved_Term`、非 `Localized_Term` 的关键概念词条提供中文释义并允许各语言按本地习惯翻译。
11. WHEN 任一非 `zh-CN` 的语言版本生成 `docs/{Language_Code}/blueprint/glossary.md` 时，THE Blueprint_Document_Set SHALL 对每个 `Reserved_Term` 条目保留英文原词不翻译，并按 `Localized_Term` 规则呈现 `MeriToken / 美誉值`。

### 需求 4：撰写中文简体蓝图文档集（以 MeriToken 为主题中心）

**用户故事：** 作为蓝图作者，我希望以中文简体先产出按主题拆分的蓝图文档集，并以 MeriToken（美誉值）的深度分析为内容主轴，作为后续翻译的唯一源头。

#### 验收标准

1. THE Blueprint_Dir 在 `docs/zh-CN/blueprint/` 下 SHALL 包含一份 `README.md` 作为 `Blueprint_Index`。
2. THE Blueprint_Document_Set 在 `docs/zh-CN/blueprint/` 下 SHALL 按主题拆分为多份 Markdown 文件，每份主题文件名采用「`{两位序号}-{Topic_Slug}.md`」格式，具体 `Topic_Slug` 集合与排序由 `design.md` 定稿。
3. THE Blueprint_Index SHALL 按定稿后的序号顺序列出当前语言下的全部主题文档，并提供指向同目录每份主题文档的相对链接。
4. THE Blueprint_Document_Set SHALL 把 MeriToken（美誉值）作为主题中心；在主题数量分配上，与 MeriToken 直接相关的主题数量 SHALL 不少于其他所有主题数量之和。
5. THE Blueprint_Document_Set SHALL 至少包含三份 MeriToken 相关主题文档，分别独立承载下列三块内容，构成 MeriToken 主题集合的最小骨架：
   - **技术原理**：覆盖加密、存储、取用、隐私保证、所有权与使用权保证；
   - **社会内涵**：覆盖社会关系、政治逻辑、经济结构、个人成长映射，并阐述 MeriToken 作为「个人贡献与社会话语权」映射载体的含义；
   - **引用与应用**：分别覆盖个人主体的引用方式与应用场景、以及 `Fay` 主体的引用方式与应用场景。
6. THE Blueprint_Document_Set SHALL 在至少一份 MeriToken 相关主题文档中明确说明 MeriToken 与 `GMC` 的从属关系，并陈述 MeriToken 独立成项目的两项理由（作为新社会的「契约部件」与「社会关系连接器」）。
7. WHERE 蓝图涉及 ifay 体系、`GMC`、`Fay`、`agent` 对照、`phase` 演进路线、整体框架等上游/外围议题，THE Blueprint_Document_Set SHALL 仅给出为定位 MeriToken 所必需的最小说明，并通过 `Upstream_Project_Doc_Link` 将读者引导至 ifay.ai 上对应的官方文档页，而不在本仓库内对这些议题做长篇阐述。
8. THE Blueprint_Document_Set SHALL 将上述上游/外围议题在主题层面收敛为单一的「与 ifay 体系的关系」类主题（具体主题名由 `design.md` 定稿），该主题的主体内容形态 SHALL 是「最小必要的位置说明 + 指向官方文档页的外链」。
9. WHERE 主题文档对应有插图，THE Blueprint_Document_Set 在该文档中 SHALL 以相对路径 `./illustration/{filename}.png` 引用 `Illustration_Dir` 下的文件，且不复制图片到其他位置。
10. IF 某主题文档计划引用的插图在 `Illustration_Dir` 下不存在，THEN THE Blueprint_Document_Set SHALL 在该文档对应位置以可见的「待补图」占位符标注，并在 `Blueprint_Index` 中列出待补图清单。
11. THE Blueprint_Document_Set 在 `zh-CN` 版本中 SHALL 在所有 `Reserved_Term` 出现处使用术语表中的英文原词，并对 MeriToken 这一概念按 `Localized_Term` 规则使用 `美誉值` 作为主用名。

### 需求 5：第一级翻译扇出（zh-CN → zh-TW / ja / ko / en）

**用户故事：** 作为多语言文档维护者，我希望在中文简体蓝图定稿后，按指定链路并行产出繁体中文、日文、韩文、英文版本，以便覆盖第一批目标语言。

#### 验收标准

1. WHEN `docs/zh-CN/blueprint/` 的 `Blueprint_Document_Set` 与 `Glossary_File` 已完成且经过 `Human_Reviewer` 校对，THE Repository SHALL 启动从 `zh-CN` 到 `{zh-TW, ja, ko, en}` 的翻译扇出。
2. THE Blueprint_Dir 在 `docs/{Language_Code}/blueprint/` 下（`Language_Code ∈ {zh-TW, ja, ko, en}`）SHALL 产出与 `zh-CN` 同名、同顺序、同数量的 `.md` 文件集合（含 `README.md`、`glossary.md` 与全部主题文档）。
3. THE Blueprint_Document_Set 在每个目标语言版本中 SHALL 通过 `Translation_Tool` 完成首轮翻译，并由 `Human_Reviewer` 完成一次通读校对。
4. THE Blueprint_Document_Set 在 `docs/zh-TW/blueprint/` 下 SHALL 使用台湾地区惯用语（如以「軟體」「網路」「程式」「資訊」「使用者」等台湾常用译法替代大陆用语），不得使用中文简体字形。
5. THE Blueprint_Document_Set 在 `docs/zh-TW/blueprint/` 下 SHALL 与 `zh-CN` 同步使用 `美誉值` 作为 MeriToken 这一概念的中文主用名（按 `Localized_Term` 规则）。
6. THE Blueprint_Document_Set 在 `docs/ja/blueprint/`、`docs/ko/blueprint/`、`docs/en/blueprint/` 下 SHALL 对 MeriToken 这一概念使用英文原词 `MeriToken`，不得替换为本地化译名。
7. THE Blueprint_Document_Set 在所有目标语言版本中 SHALL 对每个 `Reserved_Term` 出现处保留英文原词，与术语表一致。
8. THE Blueprint_Document_Set 在所有目标语言版本中 SHALL 以相对路径 `../../zh-CN/blueprint/illustration/{filename}.png` 引用 `Illustration_Dir` 下的同名插图，不在其他位置复制图片。
9. IF `zh-CN` 的 `Blueprint_Document_Set` 在第一级扇出启动后发生内容修订，THEN THE Repository SHALL 将相应修订重新同步至 `{zh-TW, ja, ko, en}` 各目标语言版本。

### 需求 6：第二级翻译扇出（en → de / es / fr / ru）

**用户故事：** 作为多语言文档维护者，我希望在英文版定稿后，再以英文为中转源完成德、西、法、俄四种语言版本，以便覆盖第二批目标语言。

#### 验收标准

1. WHEN `docs/en/blueprint/` 的 `Blueprint_Document_Set` 与 `Glossary_File` 已完成首轮翻译且经过 `Human_Reviewer` 校对，THE Repository SHALL 启动从 `en` 到 `{de, es, fr, ru}` 的翻译扇出。
2. IF `docs/en/blueprint/` 的校对尚未完成，THEN THE Repository SHALL 不得启动 `{de, es, fr, ru}` 任一语言的翻译。
3. THE Blueprint_Dir 在 `docs/{Language_Code}/blueprint/` 下（`Language_Code ∈ {de, es, fr, ru}`）SHALL 产出与 `en` 同名、同顺序、同数量的 `.md` 文件集合（含 `README.md`、`glossary.md` 与全部主题文档）。
4. THE Blueprint_Document_Set 在每个目标语言版本中 SHALL 通过 `Translation_Tool` 以 `en` 为源完成首轮翻译，并由 `Human_Reviewer` 完成一次通读校对。
5. THE Blueprint_Document_Set 在 `docs/de/blueprint/`、`docs/es/blueprint/`、`docs/fr/blueprint/`、`docs/ru/blueprint/` 下 SHALL 对 MeriToken 这一概念使用英文原词 `MeriToken`，不得替换为本地化译名。
6. THE Blueprint_Document_Set 在所有目标语言版本中 SHALL 对每个 `Reserved_Term` 出现处保留英文原词，与术语表一致。
7. THE Blueprint_Document_Set 在所有目标语言版本中 SHALL 以相对路径 `../../zh-CN/blueprint/illustration/{filename}.png` 引用 `Illustration_Dir` 下的同名插图，不在其他位置复制图片。
8. IF `docs/en/blueprint/` 的 `Blueprint_Document_Set` 在第二级扇出启动后发生内容修订，THEN THE Repository SHALL 将相应修订重新同步至 `{de, es, fr, ru}` 各目标语言版本。

### 需求 7：跨语言结构与命名对齐

**用户故事：** 作为文档读者，我希望各语言版本的蓝图目录结构、文件命名、入口与导航完全一致，以便跨语言切换阅读时不产生歧义。

#### 验收标准

1. THE Repository SHALL 使每个 `docs/{Language_Code}/blueprint/` 在已扇出语言间拥有相同的 `.md` 文件名集合（含 `README.md`、`glossary.md` 与全部主题文档），主题文档数量与命名以 `zh-CN` 版本为基准。
2. THE Blueprint_Index 在每个语言版本中 SHALL 按相同的序号顺序列出全部主题文档，并指向同目录下对应的相对链接。
3. THE Blueprint_Document_Set 在每个语言版本中 SHALL 保持与 `zh-CN` 一致的章节级标题层级（`#`、`##`、`###` 的相对层级与数量）。
4. THE Illustration_Dir SHALL 仅存在于 `docs/zh-CN/blueprint/illustration/`，不在其他语言目录下出现重复存储的同名图片。
5. THE Blueprint_Document_Set 在所有语言版本中 SHALL 对 `Reserved_Term` 集合按术语表保留英文原词。
6. THE Blueprint_Document_Set 在所有语言版本中 SHALL 对 MeriToken 这一概念按 `Localized_Term` 规则呈现：`zh-CN` 与 `zh-TW` 使用 `美誉值`，`en`、`de`、`es`、`fr`、`ja`、`ko`、`ru` 使用 `MeriToken`。
7. WHERE 蓝图涉及上游/外围议题（`ifay`、`GMC`、`Fay`、`agent`、`phase`、整体框架等），THE Blueprint_Document_Set 在所有语言版本中 SHALL 通过 `Upstream_Project_Doc_Link` 引导至 ifay.ai 官方文档页，而不在本仓库内做长篇阐述；该约束在跨语言版本之间保持一致。

### 需求 8：链路依赖控制

**用户故事：** 作为流程管理者，我希望流水线严格按指定依赖顺序执行，以便上游变更可被一致地传播到下游。

#### 验收标准

1. THE Repository SHALL 按以下顺序执行四个阶段：阶段 A（清理与 Git 追踪范围）→ 阶段 B（撰写 `zh-CN` 蓝图）→ 阶段 C（一级扇出至 `{zh-TW, ja, ko, en}`）→ 阶段 D（二级扇出至 `{de, es, fr, ru}`）。
2. IF 阶段 B 的 `zh-CN` `Blueprint_Document_Set` 未通过 `Human_Reviewer` 校对，THEN THE Repository SHALL 不得启动阶段 C 的任一语言翻译。
3. IF 阶段 C 的 `en` `Blueprint_Document_Set` 未通过 `Human_Reviewer` 校对，THEN THE Repository SHALL 不得启动阶段 D 的任一语言翻译。
4. WHERE 同一阶段内存在多个并行目标语言（如阶段 C 的 `zh-TW`、`ja`、`ko`、`en`，或阶段 D 的 `de`、`es`、`fr`、`ru`），THE Repository SHALL 允许这些目标语言并行推进且互不阻塞。
