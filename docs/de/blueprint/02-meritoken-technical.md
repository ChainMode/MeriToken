# 02 Technische Prinzipien von MeriToken

> Einleitung: Aufbauend auf der in [01-meritoken-overview.md](./01-meritoken-overview.md) etablierten Position entfaltet dieses Dokument die technischen Invarianten, die MeriToken unter den zwei Rollen „Vertragsbaustein" und „Verbinder gesellschaftlicher Beziehungen" erfüllen muss, entlang von fünf Strängen — Verschlüsselung, Speicherung, Abruf, Datenschutzgarantien sowie Eigentums- und Nutzungsrechtsgarantien. Dieses Dokument wiederholt nicht das Gesamtdesign von `GMC`; wo Verhalten der höheren Ebene berührt wird, verweist es stattdessen auf die externen Links in [07-related-projects.md](./07-related-projects.md).

## Hintergrund

Sobald MeriToken die Rolle eines wiederholt in Bezug nehmbaren Vertragsbausteins und Verbinders gesellschaftlicher Beziehungen in der neuen Gesellschaft übernimmt, können seine technischen Prinzipien nicht mehr beim „Schreiben eines einzelnen Hauptbucheintrags" stehenbleiben. Jede Erzeugung, Übertragung und Bezugnahme eines MeriToken wird entlang zweier nicht verhandelbarer Dimensionen geprüft: Erstens Verifizierbarkeit — jeder in Bezug genommene Eintrag muss von jedem Dritten unabhängig verifizierbar sein; zweitens Datenschutzgarantien — der Inhalt eines in Bezug genommenen Eintrags braucht beim Akt der Bezugnahme nicht vollständig gegenüber Nichtbeteiligten offengelegt zu werden.

Dieses Dokument nimmt diese beiden nicht verhandelbaren Bedingungen als Ausgangspunkt und entwickelt die Erörterung entlang der fünf Stränge Verschlüsselung, Speicherung, Abruf, Datenschutzgarantien sowie Eigentums- und Nutzungsrechtsgarantien. Jeder Strang entspricht einer Reihe konkreter technischer Prinzipien, die unter den Vorgaben des übergeordneten Systems `GMC` arbeiten; die Details der Protokollebene von `GMC` selbst entfaltet dieses Dokument jedoch nicht.

## Zentrale Inhalte

### Verschlüsselung

Über den gesamten Lebenszyklus von Erzeugung und Übertragung verwendet MeriToken dasselbe asymmetrische Schlüsselsystem wie `GMC`, um Einträge auszustellen und gegenzuzeichnen:

- **Mehrseitige Mit-Signatur**: Ein MeriToken-Eintrag trägt mindestens zwei Signaturklassen — „Beitragender und Bezeugender". Weitere Signaturen können angefügt werden, wenn Drittbewertung oder Schiedsentscheidung beteiligt sind. Mehrseitige Mit-Signatur ist der minimale technische Träger der Semantik „Vertragsbaustein"; eine fehlende Signatur bedeutet einen fehlenden Beweis der Einlösung.
- **Inhaltsbindung**: Die substantiellen Inhalte eines Eintrags (Beitragsbeschreibung, Kontext, Fingerabdrücke der Lieferungen usw.) werden in Form einer Bindung in der Kette geführt; der Originalinhalt selbst muss nicht in die Kette wandern. Das wahrt sowohl die Verifizierbarkeit als auch verhindert die Offenlegung irrelevanter Inhaltsdetails an das gesamte `GMC`-Netz.
- **Prüfbar, aber verbergbar**: In Prüfungsszenarien kann der Inhalt hinter einer Bindung selektiv offengelegt werden, und der Akt der Offenlegung hinterlässt selbst eine Spur. Ohne Offenlegung können Dritte weiterhin die Existenz und das Eigentum am Eintrag verifizieren, die Inhaltsdetails jedoch nicht lesen.

Das Ziel des Verschlüsselungsdesigns ist nicht, MeriToken in ein „leckfreies" Inhaltsarchiv zu verwandeln. Es ist sicherzustellen, dass unter der Semantik „Vertragsbaustein" jedes Versprechen und jeder Akt der Einlösung eine eigenständige kryptografische Absicherung trägt und dass kein Akt der Bezugnahme erneut die Originalinhalte preisgeben muss.

### Speicherung

Die zentrale Frage auf der Speicherebene lautet nicht „wo speichern", sondern „in welcher Granularität organisieren und durch wen persistieren":

- **Bindungen in der Kette, Inhalte außerhalb der Kette**: Die kryptografischen Bindungen und Signaturen von MeriToken-Einträgen werden in der `GMC`-Kette persistiert; die Originalinhalte (etwa Lieferungen eines Beitrags, Bewertungstexte) verbleiben außerhalb der Kette beim Subjekt gemäß seiner lokalen Richtlinie. Bindungen in der Kette gewährleisten netzweite Konsistenz der Einträge, und Inhalte außerhalb der Kette wahren die Hoheit des Subjekts über die eigenen Daten.
- **Aggregation nach Subjekt**: Speicherung außerhalb der Kette wird mit der Granularität persönlicher Subjekte oder `Fay`-Subjekte aggregiert. Jedes Subjekt entscheidet selbst über Speichermedium, Sicherungsstrategie und Zugänglichkeitsfenster, ohne von einem zentralisierten Dienstleister abhängig zu sein.
- **Redundanz und Wiederherstellbarkeit**: Ein Subjekt kann eine verschlüsselte Kopie seines außerhalb der Kette gehaltenen Inhalts einer vertrauten Gegenseite anvertrauen (was ebenfalls als MeriToken-Eintrag protokolliert wird), sodass eine Wiederherstellung möglich ist, wenn die lokale Kopie verloren geht. Der Akt der Anvertrauung selbst wird ebenfalls in `GMC` eingetragen, was jeden verdeckten Pfad einer „Wiederherstellung aus dem Nichts" verhindert.

Die Aufteilung der Speicherung in die zwei Schichten „Bindung in der Kette / Inhalt außerhalb der Kette" soll die Ziele „netzweite Verifizierbarkeit" und „subjektkontrollierte Verwahrung" ausbalancieren. Ohne eines davon würde MeriToken entweder zu einem öffentlichen Archiv degenerieren, das jeder lesen kann, oder zu einem lokalen Punktesystem schrumpfen, auf das nicht subjektübergreifend Bezug genommen werden kann.

### Abruf

Abruf bezeichnet den konkreten Ablauf, dem jedes Subjekt (persönlich oder `Fay`) folgt, wenn es auf einen MeriToken Bezug nimmt:

- **Per Verweis statt per Kopie**: Die in Bezug genommene Partei reicht der bezugnehmenden Partei keine Kopie des MeriToken-Eintrags. Stattdessen stellt sie ein unabhängig verifizierbares Verweis-Handle bereit. Mit dem Handle verifiziert die bezugnehmende Partei Existenz und Eigentum am Eintrag gegenüber `GMC` und kann anschließend bei Bedarf weitere Offenlegung von der in Bezug genommenen Partei anfordern.
- **Gestufte Offenlegung**: Die anfragende Partei kann drei Stufen der Offenlegung anfordern — „Existenz + Eigentum" (niedrigste Offenlegung), „semantische Zusammenfassung des Eintrags" (mittlere Offenlegung) und „Details des Originalinhalts" (höchste Offenlegung). Jede Stufe ist eine eigenständige Handlung; es gibt kein Standardverhalten, wonach „der Empfang des Handles automatisch Zugang zum Inhalt gewährt".
- **Abrufe hinterlassen eine Spur**: Jeder Abrufvorgang (einschließlich Abrufe ohne Offenlegung, die nur die Existenz prüfen) hinterlässt unter den Regeln der höheren Ebene von `GMC` eine Spur. Die Spur dient sowohl als Prüfbeleg als auch als Kantendaten im späteren Beziehungsgraphen, der festhält, „wer wessen Eintrag in Bezug genommen hat".

Die Aufteilung des Abrufs in die drei Schritte „Verweis → Verifizieren → Offenlegen" erlaubt es MeriToken, unter der Semantik „Verbinder gesellschaftlicher Beziehungen" stark genutzt zu bleiben: In den meisten Kollaborationen sind nur die ersten beiden Schritte nötig, um Vertrauen zu liefern; nur wenn Details wirklich geprüft werden müssen, kommt der dritte Schritt zum Tragen.

### Datenschutzgarantien

Datenschutzgarantien sind kein einzelnes Feature, sondern die aus den Schichten Verschlüsselung, Speicherung und Abruf jeweils extrahierte Datenschutzsemantik:

- **Standard der minimalen Offenlegung**: Standard jeder Bezugnahmebeziehung ist die niedrigste Offenlegungsstufe; jeder Abruf oberhalb des Minimums erfordert die aktive Zustimmung der in Bezug genommenen Partei, und diese Zustimmung wird selbst als MeriToken-Eintrag protokolliert.
- **Beziehungen sind durch Außenstehende nicht rekonstruierbar**: Ein Dritter kann allein aus den in `GMC` eingetragenen Bindungen den vollständigen sozialen Graphen „wer hat wen wozu in Bezug genommen" nicht rekonstruieren. Die Sichtbarkeit jedes Bezugnahmeakts ist auf die bezugnehmende und die in Bezug genommene Partei beschränkt und kann optional auf bestimmte Dritte erweitert werden.
- **Widerruf und Ungültigkeit**: Im Rahmen der ursprünglichen Vereinbarung kann die in Bezug genommene Partei die Offenlegungserlaubnis widerrufen, woraufhin der hochstufige Eintrag für die bezugnehmende Partei ab diesem Zeitpunkt ungültig wird. Die bereits erfolgten Bezugnahmehandlungen bleiben unabhängig verifizierbar, der zuvor offengelegte Inhalt darf jedoch nicht erneut in Bezug genommen werden.

Der Punkt der Datenschutzgarantie ist nicht „Daten erscheinen niemals in der Kette" — das stünde im Widerspruch zur Verifizierbarkeit. Er lautet „nur Bindungen liegen in der Kette, und Inhalt wird nur dann offengelegt, wenn er autorisiert ist". Das ist eine notwendige Folge der Semantik „Vertragsbaustein" auf der Datenschutzdimension.

### Eigentums- und Nutzungsrechtsgarantien

Eigentum und Nutzungsrechte sind zwei Angelegenheiten, die getrennt erörtert werden müssen:

- **Eigentum wird durch die Signaturbeziehung definiert**: Das Eigentum an einem MeriToken-Eintrag wird gemeinsam durch die frühesten „Beitragender- und Bezeugender-Signaturen" auf dem Eintrag definiert und ist in `GMC` unveränderlich verankert. Eigentum wird durch wiederholte Bezugnahme nicht verwässert und driftet nicht über Übertragungsvereinbarungen zu nicht signierenden Subjekten ab.
- **Nutzungsrechte werden durch die in Bezug genommene Partei gewährt**: Anders als Eigentum beschreibt das „Nutzungsrecht" „wer in welchen Szenarien diesen MeriToken in Bezug nehmen und in seine Argumentationskette einbinden darf". Nutzungsrechte werden von der in Bezug genommenen Partei szenariobezogen gewährt und bilden eine Autorisierungsmatrix aus „Szenario × Nutzer", die unabhängig von Eigentumsänderungen ist.
- **Vorrang im Konflikt**: Wenn Eigentum und Nutzungsrechte in Konflikt geraten (zum Beispiel will die Inhaberin des Nutzungsrechts den Originalinhalt offenlegen, während die Eigentümerin sich verweigert), hat das Widerrufsrecht der Eigentümerin Vorrang. Dieser Vorrang ist die direkte Folge des Grundsatzes „das Versprechen geht der Zitation voraus" unter der Semantik „Vertragsbaustein".

Die Aufteilung von Eigentum und Nutzungsrechten in zwei Schichten verhindert die Mehrdeutigkeit „dass jemand auf Ihren MeriToken Bezug genommen hat, bedeutet, dass er ihm jetzt gehört". Eigentum ist ein institutionelles Bit; Nutzungsrecht ist ein Beziehungsbit. Die Unterscheidung zwischen beiden wird in den Kollaborationen der neuen Gesellschaft wiederholt aufgerufen.

> ⏳ **Ausstehende Illustration** (Slot: `meritoken-technical-flow`)
> Beschreibung: Ein Ablaufschaubild des geschlossenen Kreislaufs aus Verschlüsselung / Speicherung / Abruf von MeriToken: mehrseitige Mit-Signatur durch Beitragenden und Bezeugenden → Bindung in der Kette in `GMC` → außerhalb der Kette gehaltener Inhalt beim Subjekt → Abruf durch die bezugnehmende Partei mittels Handle → gestufte Offenlegung → Rückschreiben der Abrufspur in `GMC`.
> Geplante Datei: `illustration/meritoken-technical-flow.png`

## Verhältnis zu anderen Themen

| Thema | Bezug zu diesem Dokument |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Liefert die Definitionen der zwei Rollen, die dieses Dokument anschließend technisiert. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Erweitert „Abruf / Datenschutzgarantie / Nutzungsrecht" dieses Dokuments um die Bedeutung auf den Schichten gesellschaftliche Beziehungen, politische Logik und ökonomische Struktur. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Konkretisiert den „Abruf"-Ablauf dieses Dokuments in Anwendungsszenarien für die zwei Klassen von Bezugnehmenden — persönliche Subjekte und `Fay`-Subjekte. |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Stellt die „Eigentums- und Nutzungsrechte" dieses Dokuments neben den Identitäts- und Eigentumsnachweis (credential), den `credential` trägt, und gibt die Entsprechung an. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Verwendet die in diesem Dokument definierten Abruf- und Offenlegungsabläufe unter hochdichten Nutzungs- und Rolling-Szenarien wieder. |
| [07-related-projects.md](./07-related-projects.md) | Liefert die offiziellen externen Links für vorgelagerte Themen wie die Gesamtprotokollebene von `GMC` und die Betriebsumgebung des ifay-Systems. |

## Begriffsfußnoten

In diesem Dokument auftretende `Reserved_Term`s:

- **GMC**: Global Merit Chain, das übergeordnete System, dem MeriToken zugeordnet ist; siehe [glossary.md](./glossary.md).
- **Fay**: Ein nicht-persönliches Subjekt, das MeriToken in Bezug nimmt; siehe [glossary.md](./glossary.md).
- **credential**: Ein credential, das heißt ein Identitäts- und Eigentumsnachweis eines persönlichen oder `Fay`-Subjekts; siehe [glossary.md](./glossary.md).
- **ifay**: Name des Projektsystems; siehe [glossary.md](./glossary.md).

Die chinesische Hauptbezeichnung von MeriToken wird ausschließlich im Fließtext der Blueprints `zh-CN` und `zh-TW` als gewöhnliche Bezeichnung von MeriToken verwendet. Siehe den Abschnitt `Localized_Term` von [glossary.md](./glossary.md) für die Lokalisierungsregeln von MeriToken in den verschiedenen Sprachen.
