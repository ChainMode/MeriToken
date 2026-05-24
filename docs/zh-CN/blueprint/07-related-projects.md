# 07 与 ifay 体系的关系

> 本文以「最小必要位置说明 + 指向官方文档页的外链清单」的形态，收敛 ifay 体系内若干上游议题与美誉值（MeriToken）蓝图的关系，避免在本仓库内对上游议题做长篇阐述。

## 背景

本仓库蓝图以美誉值的深度分析为主轴。ifay、GMC、Fay、agent、phase、整体框架等议题，定位为美誉值分析所必需的支撑性背景，而非本仓库的写作目标。

为了避免维护成本与版本漂移，本蓝图不在仓库内对上述上游议题展开长篇叙述：每项议题仅给出与美誉值有关的最小必要位置说明，再通过指向 ifay.ai 上对应官方文档页的外链，把读者引导到上游项目的权威叙述。

读者如果首次接触 ifay 体系，建议把本文作为「外链入口页」使用：先按官方文档外链清单中的链接快速建立上游背景，再回到 [01-meritoken-overview.md](./01-meritoken-overview.md) 进入主线。

## 与本蓝图的关系

下列上游术语在本蓝图中以「最小说明」出现，与美誉值的最小连接如下：

- **ifay**：项目体系名，是美誉值所依托的整体技术与社会运行环境。本蓝图不展开 ifay 体系本身，仅在描述美誉值的运行环境时按需引用。
- **GMC**：Global Merit Chain，是美誉值的上位体系。本蓝图在 [01-meritoken-overview.md](./01-meritoken-overview.md) 中说明美誉值与 GMC 的从属关系，不展开 GMC 的整体设计。
- **Fay**：ifay 体系内承担「引用 MeriToken」职责的非个人主体，与个人主体并列作为美誉值的两类引用者之一。本蓝图在 [04-meritoken-usage.md](./04-meritoken-usage.md) 中独立讨论 Fay 主体的引用方式与应用场景。
- **agent**：传统 LLM 框架下自主执行任务的程序实体，在 ifay 范式中与个人主体 / Fay 主体形成对照。本蓝图不展开 agent 与 ifay 范式的差异讨论，仅在外链中提供权威定义入口。
- **phase**：蓝图所属项目的演进阶段编号。具体阶段语义、时间线与里程碑由 ifay.ai 文档维护，本仓库不复述。
- **整体框架**：ifay 项目的整体架构与各组件互动关系。本仓库蓝图聚焦美誉值这一组件，整体框架请直接访问 ifay.ai 上对应官方文档页。

## 官方文档外链清单

下表给出本蓝图所需的最小外链集合，链接形态固定为「指向 ifay.ai 上对应官方文档页」。具体 URL 由设计层钉死，不允许替换为非 `ifay.ai` 域名。

| 上游术语 | 在本蓝图中的最小说明 | Upstream_Project_Doc_Link |
|----------|-----------------------|---------------------------|
| ifay     | 美誉值所依托的整体项目体系 | https://ifay.ai/docs/ifay |
| GMC      | 美誉值的上位体系（Global Merit Chain） | https://ifay.ai/docs/gmc |
| Fay      | 非个人主体的美誉值引用者，与个人主体并列 | https://ifay.ai/docs/fay |
| agent    | 与 ifay 范式形成对照的传统代理程序范式 | https://ifay.ai/docs/agent |

phase、整体框架等其余上游议题在 ifay.ai 站点内有专门页面承载，由读者按需在站点导航中检索访问；本蓝图不在此清单内固化其链接，以避免链接漂移。

## 术语脚注

本文出现的 `Reserved_Term`：

- **ifay**：项目体系名称，详见 [glossary.md](./glossary.md)。
- **GMC**：Global Merit Chain，美誉值的上位体系，详见 [glossary.md](./glossary.md)。
- **Fay**：非个人主体的美誉值引用者，详见 [glossary.md](./glossary.md)。
- **agent**：传统 LLM 框架下的代理体，详见 [glossary.md](./glossary.md)。
- **phase**：蓝图中的演进阶段编号，详见 [glossary.md](./glossary.md)。

「美誉值」为 MeriToken 的中文主用名，仅在 `zh-CN` 与 `zh-TW` 蓝图正文中作为该概念的常规称谓使用，详见 [glossary.md](./glossary.md) 的 `Localized_Term` 段。
