# 06 Vertiefende Themen zu MeriToken

> Einleitung: Dieses Dokument ist der Erweiterungsslot der MeriToken-Themengruppe. Aufbauend auf jeder vorausgehenden Vereinbarung in [01-meritoken-overview.md](./01-meritoken-overview.md) bis [05-meritoken-credential.md](./05-meritoken-credential.md) entwickelt es als eigenständige vertiefende Themen zwei hochdichte Nutzungssituationen von MeriToken in der neuen Gesellschaft — „hochdichter Einsatz über mehrere Subjekte hinweg" und „Rolling-Szenarien". Jedes Thema wiederholt nicht die bereits auf der Hauptlinie behandelten Konzepte; es stellt die Hauptlinienmechanismen in ein konkretes Drucksetting zurück, um sie ein weiteres Mal zu betrachten.

## Hintergrund

Die Hauptlinie, Dokumente 01 bis 05, hat die Position von MeriToken, seine technischen Prinzipien, seine gesellschaftliche Bedeutung, seine Bezugnahme und Anwendungen sowie seine Grenze zu `credential` geklärt. Sobald die neue Gesellschaft jedoch tatsächlich aufschlägt, treten zwei Klassen „hochbelasteter" Settings auf, die die Hauptliniendiskussion nicht direkt abdecken kann:

- **Hochdichter Einsatz über mehrere Subjekte hinweg**: Wenn mehrere `Fay`-Subjekte und mehrere persönliche Subjekte zum selben Thema fortlaufend MeriToken in Bezug nehmen, wirkt eine einzelne Bezugnahme einfach, doch die Aggregation bringt drei Probleme — Last, Offenlegung und Aggregation.
- **Rolling-Szenarien**: Wenn der Lebenszyklus einer Zusammenarbeit lang genug ist, hört MeriToken auf, die Spur einer einmaligen Lieferung zu sein, und muss stattdessen über mehrere Runden Zyklen aus Akkumulation, Revision, Rücknahme und Archivierung durchlaufen. Das verlangt vom MeriToken-Mechanismus, auf langer Zeitskala selbstkonsistent zu bleiben, statt nur bei einer einzelnen Bezugnahmehandlung vernünftig auszusehen.

Dieses Dokument entwickelt die zwei Themen. Jedes Thema skizziert zunächst die Druckquelle, betrachtet dann die Hauptlinienmechanismen (Abruf, Offenlegung, Spur, Eigentum und Nutzungsrechte, Grenze zu `credential` und so weiter) unter diesem Druck erneut und weist auf offene Fragen hin, die weiterer Argumentation oder Entwicklungsarbeit bedürfen. Dieses Dokument führt auf der Protokollebene keine neuen Konzepte ein; alles ist eine fortgesetzte Ableitung bereits auf der Hauptlinie definierter Mechanismen, angewandt in neuen Settings.

## Zentrale Inhalte

### Thema A: Hochdichter Einsatz über mehrere Subjekte hinweg

**Druckquelle**: In der realen Zusammenarbeit der neuen Gesellschaft ist „ein `Fay`-Subjekt nimmt einen MeriToken in Bezug" ein zu idealisiertes minimales Setting. Häufiger ist, dass zum selben Thema drei Klassen von Bezugnehmenden gleichzeitig auftreten:

- **Mehrere `Fay`-Subjekte**: zum Beispiel Kollaborierende aus verschiedenen Branchen und Regionen, die jeweils im Namen ihrer eigenen Mitglieder die einschlägigen MeriToken in Bezug nehmen;
- **Mehrere persönliche Subjekte**: zum Beispiel zentrale Beteiligte am Thema, die jeweils die MeriToken-Einträge aus ihren eigenen vergangenen einschlägigen Zusammenarbeiten zitieren;
- **Verschachtelte Bezugnahme**: Die obigen `Fay`-Subjekte selbst nehmen einige MeriToken-Einträge persönlicher Subjekte als Grundlage ihrer Vertretungsbefugnis in Bezug.

Diese hochdichte Bezugnahme geschieht innerhalb desselben Themas, desselben Zeitfensters und derselben Offenlegungsfläche und bringt mehrere Eigenschaften des MeriToken-Mechanismus gleichzeitig an ihre Belastungsgrenzen.

**Mechanismen erneut betrachtet**:

- **Die Grenze der Bezugnahmeaggregation**: Die Bezugnahme durch Aggregation eines einzelnen `Fay`-Subjekts ist bereits eine zusammengesetzte Bezugnahmefläche (siehe den Abschnitt „Bezugnahmemethoden und Anwendungsszenarien von Fay-Subjekten" von [04-meritoken-usage.md](./04-meritoken-usage.md)). Stapeln sich die zusammengesetzten Bezugnahmeflächen mehrerer `Fay`-Subjekte zum selben Thema, braucht die externe prüfende Person nicht „dass jeder MeriToken aufgeschlüsselt wird", sondern „die Bestätigung, dass diese aggregierten Flächen einander nicht widersprechen, ohne die Details aufzuschlüsseln". Das bedeutet, Bezugnahme durch Aggregation muss „Abgleichbarkeit auf der Aggregationsebene" unterstützen, nicht nur Verifizierbarkeit auf der Ebene einzelner Einträge.
- **Koordination der gestuften Offenlegung**: Bei hochdichtem Einsatz kann jede in Bezug genommene Partei (ein persönliches Subjekt oder ein untergeordnetes `Fay`-Subjekt) eine andere Offenlegungsstufenberechtigung haben. Die aggregierende Stelle darf hochstufige und niedrigstufige Offenlegungen nicht zu einer einzigen externen Vorlage vermischen; sonst gleicht das einer erzwungenen Eskalation einer niedrigstufigen Offenlegung. Thema A erfordert den Grundsatz „minimale Offenlegungsstufe als Rückfallebene": Die Offenlegungsstufe einer aggregierten Fläche ist nicht höher als die niedrigste Berechtigungsstufe unter allen darin enthaltenen in Bezug genommenen Einträgen und wird nur dann als Ganzes eskaliert, wenn jede in Bezug genommene Partei aktiv zustimmt.
- **Echo des Widerrufspfades**: Wenn ein zugrundeliegendes persönliches Subjekt seine Offenlegungserlaubnis widerruft, muss der diesem Eintrag entsprechende Anteil unverzüglich in jeder aggregierten Fläche eines `Fay`-Subjekts, die darauf beruhte, ungültig werden. Es darf keine Situation geben, in der „die vorgelagerte Stelle widerrufen hat, doch die nachgelagerte Aggregation weiterhin über Caches offenlegt". Das erweitert die Semantik „Widerruf und Ungültigkeit" aus dem Abschnitt „Datenschutzgarantien" von [02-meritoken-technical.md](./02-meritoken-technical.md) auf das verschachtelte Setting.
- **Lesbarkeit der Abrufspur**: Im hochdichten Setting lässt das Verzeichnen jeder Bezugnahme unter `GMC` das Spurvolumen eines einzelnen Themas schnell anschwellen. Die Spur auf der Mechanismusebene ist weiterhin notwendig, doch für die menschliche Darstellung muss sie entlang der drei Achsen „Thema — Subjekt — Zeit" gefaltet werden, um zu vermeiden, dass der Prüfprozess in rohen Spureinträgen ertrinkt.

**Offene Fragen**:

- Welche Reihe von Bindungsmechanismen die Abgleichbarkeit auf Aggregationsebene genau trägt, muss gemeinsam mit den Regeln der höheren Ebene von `GMC` entworfen werden;
- Der Verhandlungsablauf zwischen „minimale Offenlegungsstufe als Rückfallebene" und dem Wunsch einzelner Beteiligter, das Ganze zu eskalieren, sollte selbst als MeriToken-Einträge protokolliert werden;
- Die Darstellungsregeln für das Falten von Spuren sind kein Problem der Protokollebene, doch sie müssen vom unterstützenden Werkzeugbestand des Blueprints einheitlich vereinbart werden.

> ⏳ **Ausstehende Illustration** (Slot: `meritoken-deep-cases-density`)
> Beschreibung: Ein konzeptionelles Schaubild, das Bezugnahmeaggregation, gestufte Offenlegung und Widerrufspfade von MeriToken in subjektübergreifenden hochdichten Kollaborationsszenarien zeigt.
> Geplante Datei: `illustration/meritoken-deep-cases-density.png`

### Thema B: Rolling-Szenarien

**Druckquelle**: In Projekten mit langem Lebenszyklus bleibt MeriToken nicht bei der minimalen Einheit „ein Beitrag — eine Bewertung — eine Spur". Er kehrt auf langer Zeitskala in Zyklen aus Akkumulation, Revision, Rücknahme und Archivierung wieder. Typische Settings sind generationenübergreifende öffentliche Projekte, langgestreckte Open-Source-Zusammenarbeiten und Steuerung von Gemeinschaften, die mehreren Kohorten von Beteiligten gegenübersteht. Der durch solche Projekte erzeugte Druck ist nicht mehr die Komplexität einer einzelnen Bezugnahmehandlung, sondern die Selbstkonsistenz des Mechanismus auf langer Zeitskala.

**Mechanismen erneut betrachtet**:

- **Akkumulation**: Jede Stufe des Projekts legt neue MeriToken-Einträge ab, die unter `GMC` protokolliert werden und beim Stufenwechsel nicht verloren gehen. Doch das nach außen gerichtete „Gesamtbild" des Projekts muss vermeiden, jeden Eintrag undifferenziert zu stapeln; eine Schichtung nach Stufe, Rolle und Thema ist notwendig. Das ist konsistent mit „von einzelner Fähigkeit zu mehrdimensionalem Profil" im Abschnitt „Abbildung der persönlichen Entwicklung" von [03-meritoken-social.md](./03-meritoken-social.md), doch auf der Projektseite muss ein `Fay`-Subjekt die Verantwortung für die geschichtete Aggregation übernehmen.
- **Revision**: Wenn ein bestehender MeriToken-Eintrag auf der Faktebene neue Bezeugung, neue Bewertung oder neuen Vergleich erhält, ist die angemessene Reaktion, einen Revisionseintrag anzufügen, statt das Original zu überschreiben. Der Revisionseintrag ist selbst ein MeriToken-Eintrag, der den Grund der Revision und die mehrseitige Mit-Signatur enthält. Entlang der Zeitachse können Lesende sowohl den ursprünglichen Eintrag als auch die nachfolgenden Revisionen sehen, was die Situation vermeidet, in der „ein einzelner Eintrag wiederholt umgeschrieben und die Geschichte abgeflacht wird".
- **Rücknahme**: In einem langen Lebenszyklus bezieht sich Rücknahme nicht nur auf die Rücknahme von Offenlegungserlaubnissen, sondern auch auf die Rücknahme der Wirkung des ursprünglichen Eintrags (zum Beispiel scheidet die ausstellende Stelle aus oder die Vorbedingung der Zusammenarbeit ändert sich). Die Rücknahme der Wirkung löscht die Spur nicht; sie markiert den Zustand des Eintrags als „zurückgenommen", sodass spätere Bezugnehmende „vor der Rücknahme erfolgte Bezugnahmen" von „nach der Rücknahme erfolgten Bezugnahmen" unterscheiden können. Der Akt der Rücknahme folgt dem im Abschnitt „Die Grenze und Entsprechung" von [05-meritoken-credential.md](./05-meritoken-credential.md) definierten unabhängigen Widerrufspfad und kompensiert nicht den Rücknahmepfad von `credential`.
- **Archivierung**: Wenn eine Projektstufe endet oder das Projekt insgesamt abschließt, sollen die einschlägigen MeriToken-Einträge in einen archivierten Zustand übergehen, statt vernichtet zu werden. Im archivierten Zustand können die Einträge weiterhin unabhängig verifiziert und zitiert werden, doch die voreingestellte Offenlegungsstufe sinkt auf die niedrigste, um die Situation zu vermeiden, in der die Einträge Jahre nach dem Ende eines langlaufenden Projekts die Beteiligten weiterhin auf hoher Offenlegungsstufe exponieren. Der Archivierungsübergang selbst wird unter `GMC` verzeichnet, was jegliche Undurchsichtigkeit vermeidet, „dass sich nach einem bestimmten Zeitpunkt die Sichtbarkeit eines Eintrags stillschweigend ändert".

**Selbstkonsistenz des Mechanismus**: Akkumulation / Revision / Rücknahme / Archivierung bilden einen vollständigen Zyklus, und jede Aktion hinterlässt eine Spur als neuen Eintrag. Das stellt sicher, dass die Dimension „Zeit" selbst in den MeriToken-Mechanismus hineingezogen wird, anstatt einseitig von außen durch die Projektinhabenden gesteuert zu werden. Jede Zustandsänderung entlang der Zeitdimension muss unabhängig verifizierbar sein, ohne von der Auslegung der Projektinhabenden abhängen zu müssen.

**Offene Fragen**:

- Ob der Umfang der mehrseitigen Mit-Signatur eines Revisionseintrags exakt mit dem des ursprünglichen Eintrags übereinstimmen sollte, muss szenariobezogen verfeinert werden;
- Ob die voreingestellte Offenlegungsstufe des Archivierungsübergangs gemeinsam von Projektinhabenden und Beteiligten angepasst werden kann und welcher Verhandlungsablauf dafür nötig ist;
- Ob das Gewicht stufenübergreifender Bezugnahmen mit der Zeit abklingt, ist eine projektbezogene Strategieentscheidung und sollte vom Werkzeugbestand unterstützt und nicht von der Protokollebene vorgeschrieben werden.

## Verhältnis zu anderen Themen

| Thema | Bezug zu diesem Dokument |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Liefert die Definitionen der zwei grundlegenden Rollen. Thema A und Thema B bauen beide auf „Vertragsbaustein / Verbinder gesellschaftlicher Beziehungen" auf. |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Liefert die konkrete technische Semantik von Abruf, Offenlegung, Rücknahme sowie Eigentums- und Nutzungsrechten, die die hier behandelten Themen unter hoher Dichte und auf langer Zeitskala wiederverwenden. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Liefert die Grundlage gesellschaftlicher Bedeutung der „Diskursgewicht-Abbildung". Thema A verwendet sie in subjektübergreifender Zusammenarbeit wieder; Thema B verwendet sie in Rolling-Szenarien wieder. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Liefert die Bezugnahmemethoden und Anwendungsszenarien für beide Klassen von Bezugnehmenden — persönliche Subjekte und `Fay`-Subjekte. Thema A hier ist deren Erweiterung unter hochdichter Stapelung. |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Liefert die Grenze und Entsprechung zu `credential`. Thema B hier verwendet im Rücknahmepfad den Grundsatz „unabhängige Widerrufspfade" wieder. |
| [07-related-projects.md](./07-related-projects.md) | Liefert die offiziellen externen Verweise zu vorgelagerten Themen wie ifay, `GMC`, `Fay`, `agent`, `phase` und Gesamtrahmen. |

## Begriffsfußnoten

In diesem Dokument auftretende `Reserved_Term`s:

- **GMC**: Global Merit Chain, das übergeordnete System, dem MeriToken zugeordnet ist; siehe [glossary.md](./glossary.md).
- **Fay**: Ein nicht-persönliches Subjekt, das MeriToken in Bezug nimmt; siehe [glossary.md](./glossary.md).
- **credential**: Ein credential, das heißt ein Identitäts- und Eigentumsnachweis eines persönlichen oder `Fay`-Subjekts; siehe [glossary.md](./glossary.md).
- **ifay**: Name des Projektsystems; siehe [glossary.md](./glossary.md).
- **agent**: Eine agent-Entität in herkömmlichen LLM-Frameworks; siehe [glossary.md](./glossary.md).
- **phase**: Eine Entwicklungsstufennummer im Blueprint; siehe [glossary.md](./glossary.md).

Die chinesische Hauptbezeichnung von MeriToken wird ausschließlich im Fließtext der Blueprints `zh-CN` und `zh-TW` als gewöhnliche Bezeichnung von MeriToken verwendet. Siehe den Abschnitt `Localized_Term` von [glossary.md](./glossary.md) für die Lokalisierungsregeln von MeriToken in den verschiedenen Sprachen.
