# Glossar (de)

Dieses Glossar ist das einzig maßgebliche Wörterbuch für die mehrsprachige Dokumentation des iFay-Blueprints. Einträge in der Tabelle `Reserved_Term` behalten in allen Sprachversionen ihre ursprüngliche englische Form bei und werden nicht übersetzt. Einträge in der Tabelle `Localized_Term` wechseln ihre Hauptform je nach Zielsprache. Einträge, die weder zu `Reserved_Term` noch zu `Localized_Term` gehören, werden in jeder Sprache nach lokaler Konvention lokalisiert.

## Reserved_Term (englische Originalform in allen Sprachen beibehalten)

| Englisches Original | Definition | Übersetzungsregel | Referenzlink (Upstream_Project_Doc_Link) |
|----------|----------|----------|-----------------------------------|
| iFay / ifay | Name des iFay-Projektökosystems; im Avatar-Kontext bezeichnet `iFay` (Individual Fay) einen persönlichen digitalen Avatar, der 1:N an einen einzelnen `Human Prime` gebunden ist | Reserved: in allen Sprachen englische Originalform beibehalten | https://ifay.ai |
| agent | Agent (Agentenentität, in herkömmlichen LLM-Frameworks eine Programmentität, die Aufgaben autonom ausführt) | Reserved: in allen Sprachen englische Originalform beibehalten | https://ifay.ai |
| phase | Stufe (eine Entwicklungsstufennummer im Blueprint) | Reserved: in allen Sprachen englische Originalform beibehalten, mit der Nummer unmittelbar dahinter (zum Beispiel `phase 1`) | — |
| credential | Credential (Identitäts- und Eigentumsnachweis eines `Human Prime` oder `Fay`-Subjekts) | Reserved: in allen Sprachen englische Originalform beibehalten | ./05-meritoken-credential.md |
| GMChain | Global Merit Chain, das nicht-monetäre System zur Messung gesellschaftlicher Beiträge und zur Governance, dem MeriToken zugeordnet ist | Reserved: kanonische Abkürzung `GMChain` in allen Sprachen beibehalten | ./01-meritoken-overview.md |
| Fay | Oberbegriff für autonome digitale Avatare im iFay-System (`Fay = iFay + coFay`), wobei `iFay` der an einen einzelnen `Human Prime` verankerte persönliche Avatar und `coFay` der nicht-persönliche kollaborative Avatar einer öffentlichen Rolle in einschichtiger Zuordnung zu einer verantwortlichen natürlichen Person oder Organisation ist | Reserved: in allen Sprachen englische Originalform beibehalten | ./04-meritoken-usage.md |
| Human Prime | Die im iFay-System abgebildete und letztverantwortliche natürliche Person | Reserved: `Human Prime` beibehalten | https://ifay.ai |
| Host | Endgerät-Hardware, Client-Anwendung oder Laufzeitumgebung, in der ein `Fay` ausgeführt wird oder autorisierte Kontrolle ausübt (bezeichnet niemals eine natürliche Person) | Reserved: `Host` beibehalten | https://ifay.ai |

## Localized_Term (Hauptform wechselt je nach Zielsprache)

| Englisches Original | 中文主用名 | Handhabungsregel |
|----------|------------|----------|
| MeriToken | 美誉值 | Der Fließtext von `zh-CN` und `zh-TW` verwendet „美誉值" (`zh-TW`: „美譽值") als Hauptform und darf bei der ersten Erwähnung in dieser Sprachversion in Klammern die englische Originalform `MeriToken` annotieren. Der Fließtext von `en`, `de`, `es`, `fr`, `ja`, `ko`, `ru` verwendet die englische Originalform `MeriToken` und darf keine lokalisierte Übersetzung einsetzen. |

## Anmerkung zu MeriToken_Chinese_Name

„美誉值" ist die chinesische Hauptbezeichnung von MeriToken und wird ausschließlich im Fließtext der Blueprints `zh-CN` und `zh-TW` als gewöhnliche Bezeichnung von MeriToken verwendet. MeriToken ist ein strikt nicht-monetärer Maßstab für gesellschaftliche Beiträge — weder auszahlbar noch spekulativ oder übertragbar. Die Zeichenfolge „美誉值" erscheint in keiner anderen Sprachversion (auch nicht in `en`).

## Nicht-Reserved-Einträge

| Quellbegriff | Vorgeschlagene Übersetzung | Anmerkungen |
|------|----------|------|
| 蓝图 | Blueprint | In jeder Sprache nach lokaler Konvention zu übersetzen. |
| 校对 | Korrektur | — |
| 凭证管理 | credential-Verwaltung | Wird „credential" in seiner Originalform beibehalten, wird die Wendung als Ganzes als „credential-Verwaltung" wiedergegeben. |
