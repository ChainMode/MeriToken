# 07 與 ifay 體系的關係

> 本文以「最小必要位置說明 + 指向官方文件頁的外鏈清單」的形態，收斂 ifay 體系內若干上游議題與美譽值（MeriToken）藍圖的關係，避免在本儲存庫內對上游議題做長篇闡述。

## 背景

本儲存庫藍圖以美譽值的深度分析為主軸。ifay、GMC、Fay、agent、phase、整體框架等議題，定位為美譽值分析所必需的支撐性背景，而非本儲存庫的寫作目標。

為了避免維護成本與版本漂移，本藍圖不在儲存庫內對上述上游議題展開長篇敘述：每項議題僅給出與美譽值有關的最小必要位置說明，再透過指向 ifay.ai 上對應官方文件頁的外鏈，把讀者引導到上游專案的權威敘述。

讀者如果首次接觸 ifay 體系，建議把本文作為「外鏈入口頁」使用：先按官方文件外鏈清單中的連結快速建立上游背景，再回到 [01-meritoken-overview.md](./01-meritoken-overview.md) 進入主線。

## 與本藍圖的關係

下列上游術語在本藍圖中以「最小說明」出現，與美譽值的最小連接如下：

- **ifay**：專案體系名，是美譽值所依託的整體技術與社會執行環境。本藍圖不展開 ifay 體系本身，僅在描述美譽值的執行環境時按需引用。
- **GMC**：Global Merit Chain，是美譽值的上位體系。本藍圖在 [01-meritoken-overview.md](./01-meritoken-overview.md) 中說明美譽值與 GMC 的從屬關係，不展開 GMC 的整體設計。
- **Fay**：ifay 體系內承擔「引用 MeriToken」職責的非個人主體，與個人主體並列作為美譽值的兩類引用者之一。本藍圖在 [04-meritoken-usage.md](./04-meritoken-usage.md) 中獨立討論 Fay 主體的引用方式與應用場景。
- **agent**：傳統 LLM 框架下自主執行任務的程式實體，在 ifay 範式中與個人主體／Fay 主體形成對照。本藍圖不展開 agent 與 ifay 範式的差異討論，僅在外鏈中提供權威定義入口。
- **phase**：藍圖所屬專案的演進階段編號。具體階段語義、時間線與里程碑由 ifay.ai 文件維護，本儲存庫不覆述。
- **整體框架**：ifay 專案的整體架構與各組件互動關係。本儲存庫藍圖聚焦美譽值這一組件，整體框架請直接前往 ifay.ai 上對應官方文件頁。

## 官方文件外鏈清單

下表給出本藍圖所需的最小外鏈集合，連結形態固定為「指向 ifay.ai 上對應官方文件頁」。具體 URL 由設計層固定，不允許替換為非 `ifay.ai` 域名。

| 上游術語 | 在本藍圖中的最小說明 | Upstream_Project_Doc_Link |
|----------|-----------------------|---------------------------|
| ifay     | 美譽值所依託的整體專案體系 | https://ifay.ai/docs/ifay |
| GMC      | 美譽值的上位體系（Global Merit Chain） | https://ifay.ai/docs/gmc |
| Fay      | 非個人主體的美譽值引用者，與個人主體並列 | https://ifay.ai/docs/fay |
| agent    | 與 ifay 範式形成對照的傳統代理程式範式 | https://ifay.ai/docs/agent |

phase、整體框架等其餘上游議題在 ifay.ai 網站內有專門頁面承載，由讀者按需在網站導覽中檢索瀏覽；本藍圖不在此清單內固化其連結，以避免連結漂移。

## 術語腳註

本文出現的 `Reserved_Term`：

- **ifay**：專案體系名稱，詳見 [glossary.md](./glossary.md)。
- **GMC**：Global Merit Chain，美譽值的上位體系，詳見 [glossary.md](./glossary.md)。
- **Fay**：非個人主體的美譽值引用者，詳見 [glossary.md](./glossary.md)。
- **agent**：傳統 LLM 框架下的代理體，詳見 [glossary.md](./glossary.md)。
- **phase**：藍圖中的演進階段編號，詳見 [glossary.md](./glossary.md)。

「美譽值」為 MeriToken 的中文主用名，僅在 `zh-CN` 與 `zh-TW` 藍圖正文中作為該概念的常規稱謂使用，詳見 [glossary.md](./glossary.md) 的 `Localized_Term` 段。
