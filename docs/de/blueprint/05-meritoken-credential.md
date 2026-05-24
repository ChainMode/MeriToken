# 05 Verhältnis zwischen credential und MeriToken

> Einleitung: Dieses Dokument knüpft an die in [01-meritoken-overview.md](./01-meritoken-overview.md) etablierte Position an. Unter der Semantik „Vertragsbaustein" behandelt es eigens die Grenze und Entsprechung zwischen MeriToken und `credential`. Die beiden werden oft verwechselt, doch in der Kollaborationspraxis der neuen Gesellschaft schwächt eine fehlende Unterscheidung sowohl die Stabilität von Identität und Eigentum als auch die Akkumulierbarkeit von Beitrag und Bewertung.

## Hintergrund

Mehrere Fragen in der neuen Gesellschaft — „wer bin ich", „darf ich dies tun", „was habe ich getan", „wie wurde ich bewertet" — müssen von Objekten getragen werden, die strukturell unabhängig voneinander, aber miteinander zusammensetzbar sind. Werden alle Fragen auf eine einzige Klasse von Objekten gehäuft, treten zwei typische Schieflagen auf:

- **Credential bloat (credential-Aufblähung)**: „Was ich getan habe und wie ich bewertet wurde" — also Inhalte, die zu MeriToken gehören sollten — in `credential` zu schreiben, zwingt Identitäts- und Eigentumsnachweise dazu, fortlaufend ausgestellt und aktualisiert zu werden. Die ausstellende Stelle wird überlastet, und die haltende Person verliert die Hoheit über die eigenen Bewertungsdatensätze.
- **Bewertungsdrift**: „Wer ich bin und was ich halte" in MeriToken zu schreiben, lässt Identitätsattribute den Behälter der Beitragsbewertung zerquetschen. Die MeriToken-Bewertungsdatensätze, die in der Zusammenarbeit durch mehrseitige Mit-Signatur getragen werden sollten, werden vom Recht zur credential-Ausstellung verdünnt.

Dieser Blueprint teilt die zwei Klassen von Objekten zwischen zwei verschiedenen Trägern auf und legt die Zuordnung explizit fest: `credential` löst die Seite „Identität und Eigentum"; MeriToken löst die Seite „Beitrag und Bewertung". Die zwei sind unabhängig voneinander und entsprechen einander dennoch. Aufgabe dieses Dokuments ist es, die Grenze zwischen MeriToken und `credential` klar zu machen, sodass die Dokumente 06–07 und die verschiedenen sprachlichen Fan-outs die zwei beim Bezugnehmen nicht vermischen.

Die Details der Protokollebene von `credential` werden von der offiziellen Dokumentation des ifay-Systems getragen. Dieses Dokument liefert nur die minimal erforderliche Erklärung für „die Grenze zu MeriToken".

## Zentrale Inhalte

![credential-Verwaltung](../../zh-CN/blueprint/illustration/credential-management.png)

Das obige Schaubild (vorläufig wiederverwendet) skizziert die grundlegenden Aktionen von `credential` entlang der Kette aus Ausstellung, Verifizierung und Widerruf. Die Erörterung in diesem Dokument baut auf dieser Reihe von Aktionen auf und stellt sie neben die Semantik „Beitrag–Bewertung" von MeriToken.

### Die Rolle von credential

`credential` löst die Frage „wer ist das Subjekt, und welches Eigentum hält es an welchem Objekt", und ist der Nachweisträger von Identität und Eigentum in der neuen Gesellschaft:

- **Verifizierbares Bit von Identität und Eigentum**: `credential` wird von einem Subjekt mit Ausstellungsbefugnis ausgestellt und protokolliert die Identitätsattribute des ausgestellten Subjekts (Zugehörigkeit, Rolle, Qualifikation usw.) oder dessen Eigentum an einem bestimmten Objekt (Kontrolle über eine Ressource, ein Protokollbit, eine Protokollrolle). Es beantwortet, „in welchem Eigentumszustand sich dieses Subjekt zu einem bestimmten Zeitpunkt in Bezug auf ein bestimmtes Objekt befindet".
- **Auf der credential-und-token-Schicht ausgestellt, verifiziert und widerrufen**: Der Lebenszyklus von `credential` ist durch die Protokollregeln der credential-und-token-Schicht eingeschränkt. Der Akt der Ausstellung definiert seinen Gültigkeitsbereich. Der Akt der Verifizierung erlaubt es jedem Dritten, Existenz und Eigentum am credential unabhängig zu bestätigen. Der Akt des Widerrufs ermöglicht es der ausstellenden Stelle, ein credential bei einer Eigentumsänderung umgehend zurückzunehmen, um zu verhindern, dass das credential weiterhin zitiert wird, nachdem es sich vom tatsächlichen Eigentum gelöst hat.
- **Konzentriert auf die Eintrittsqualifikation „was jemand tun darf"**: In subjektübergreifender Zusammenarbeit wird `credential` typischerweise als Eintrittsqualifikation geprüft. Hält ein Subjekt das entsprechende `credential`, bedeutet das institutionell, dass es die Qualifikation hat, eine bestimmte Kollaborationsfläche zu betreten, ein bestimmtes Protokollbit zu zitieren oder eine bestimmte Ressourcenschnittstelle aufzurufen. `credential` bewertet nicht direkt, wie das Subjekt sich in der Vergangenheit verhalten hat.
- **Stabilität an erster Stelle**: Die semantische Stabilität von `credential` ist seine grundlegende Eigenschaft. Eine langlebige Mitgliedschaft oder ein langlebiges Kontrollrecht über eine Ressource schwankt nicht ständig mit der kurzfristigen Kollaborationsleistung der haltenden Person. Der schwankende Anteil sollte von MeriToken getragen werden, nicht zurück in `credential` gespiegelt.

Die Rolle von `credential` auf „den Nachweis von Identität und Eigentum" festzunageln, hält die Pfade von Ausstellung und Widerruf einfach und prüfbar, ungestört von häufigen Bewertungsdatensätzen.

### Die Rolle von MeriToken

MeriToken löst die Frage „was hat das Subjekt getan und wie wurde es bewertet" und ist in der neuen Gesellschaft der Träger von Beitrags- und Bewertungsdatensätzen:

- **Akkumulierbares Bit von Beitrag und Bewertung**: MeriToken wird durch mehrseitige Mit-Signatur unter Mitwirkenden erzeugt (siehe die Abschnitte „Verschlüsselung" und „Abruf" von [02-meritoken-technical.md](./02-meritoken-technical.md)) und protokolliert in einer bestimmten Zusammenarbeit „wer was beigetragen hat, wer was bezeugt hat und wie sich die Beteiligten gegenseitig bewertet haben". Es beantwortet, „in welchen konkreten vergangenen Zusammenarbeiten dieses Subjekt sich verhalten hat und wie".
- **Untergeordnet dem übergeordneten System `GMC`**: Anders als die Ausstellungs- und Widerrufskette von `credential` wird die Erzeugungs-, Bezugnahme- und Widerrufskette von MeriToken einheitlich unter dem übergeordneten System `GMC` geführt, mit Kettensemantik, die netzweite Konsistenz und Unveränderlichkeit gewährleistet (siehe den Abschnitt „Die Zugehörigkeit von MeriToken zu GMC" von [01-meritoken-overview.md](./01-meritoken-overview.md)).
- **Konzentriert auf die Verlaufsspur „was getan wurde und wie es getan wurde"**: MeriToken fungiert nicht als Verifizierung einer Eintrittsqualifikation; es wird im Verlauf der Zusammenarbeit fortlaufend erzeugt. Nach außen kann es zitiert, aggregiert und verglichen werden, doch jeder Eintrag entspricht einem konkreten Kollaborationsfakt und kann nicht beliebig erzeugt oder entfernt werden.
- **Akkumulierbar, widerrufbar, mit gestufter Offenlegung**: MeriToken akkumulieren über langfristige Zusammenarbeit zu einem mehrdimensionalen Entwicklungsprofil. Wenn sich die ursprüngliche Vereinbarung ändert, kann die in Bezug genommene Partei die entsprechende Offenlegungserlaubnis widerrufen. Jede Bezugnahme hinterlässt unter `GMC` eine Spur (siehe den Abschnitt „Datenschutzgarantien" von [02-meritoken-technical.md](./02-meritoken-technical.md)).

Die Rolle von MeriToken auf „den Datensatz von Beitrag und Bewertung" festzunageln, lässt die feinkörnige Bewertung des Kollaborationsverlaufs über die Zeit akkumulieren und unabhängig kontrolliert bleiben, ohne von der credential-Ausstellungsbefugnis annektiert zu werden.

### Die Grenze und Entsprechung

`credential` und MeriToken übernehmen jeweils eine nicht ersetzbare Rolle in der Zusammenarbeit der neuen Gesellschaft. Die folgende Tabelle stellt sie entlang von fünf semantischen Achsen nebeneinander:

| Semantische Achse | `credential` | MeriToken |
|--------|--------------|---------------------|
| Semantischer Schwerpunkt | Credential der Identität und des Eigentums; beantwortet „wer das Subjekt ist und was es an welchem Objekt hält" | Datensatz von Beitrag und Bewertung; beantwortet „in welchen Zusammenarbeiten das Subjekt was getan hat und wie es bewertet wurde" |
| Lebenszyklus | Auf der credential-und-token-Schicht ausgestellt, verifiziert und widerrufen; betont Zustandsübergänge der Eintrittsqualifikation | Unter dem übergeordneten System `GMC` geführt; die Erzeugungs-, Bezugnahme- und Widerrufskette hinterlässt unter Kettensemantik eine Spur |
| Halteform | Ein zwischen ausstellender Stelle und haltender Person beidseitig verankertes Zustandsobjekt; betont Stabilität | Ein durch mehrseitige Mit-Signatur der Mitwirkenden geprägtes Verlaufsobjekt; betont Akkumulierbarkeit |
| Methode der Bezugnahme | Beim Eintritt in die Zusammenarbeit geprüft, um zu verifizieren, „ob die Qualifikation gehalten wird" | Im Verlauf oder nach der Zusammenarbeit zitiert, aggregiert und verglichen, um „wie Dinge in der Vergangenheit getan wurden" zu zeigen |
| Subjektübergreifende Semantik | Dasselbe Subjekt hält auf verschiedenen Kollaborationsflächen unterschiedliche `credential`s, die einander nicht zwingend vergleichbar sind | Vom selben Subjekt zu verschiedenen Themen akkumulierte MeriToken können wechselseitig zitiert werden, doch Bewertungsgewicht wandert nicht automatisch |

Die Grenze hält auf vier Ebenen, die sich gegenseitig verstärken, und stellt sicher, dass die zwei Klassen von Objekten nicht vermischt werden:

- **Nicht ersetzbar**: `credential` darf nicht verwendet werden, um „was ich getan habe und wie ich bewertet wurde" zu protokollieren; sonst gibt es credential-Aufblähung und eine unausgewogene Last bei der ausstellenden Stelle. MeriToken darf nicht verwendet werden, um „wer ich bin und was ich halte" zu protokollieren; sonst gibt es Bewertungsdrift und eine Verdünnung des Eigentums. Beide tragen jeweils unterschiedliche institutionelle Aufgaben.
- **Wechselseitig voraussetzend und erweiternd**: In vielen Kollaborationen liefert `credential` die Eintrittsqualifikation, und MeriToken legt die Verlaufsspur ab, sobald das Subjekt drinnen ist. Zum Beispiel entscheidet `credential` in einer organisationsübergreifenden Beratung, ob ein Teilnehmender die Qualifikation hat, das Wort zu ergreifen, während MeriToken den Beitrag und die Bewertung jeder Wortmeldung protokolliert und über die Zeit das Diskursgewicht zu späteren Themen beeinflusst (siehe den Abschnitt „Politische Logik" von [03-meritoken-social.md](./03-meritoken-social.md)).
- **Gemeinsam zitiert, getrennt getragen**: In der Bezugnahme durch Stellvertretung und Aggregation von `Fay`-Subjekten (siehe den Abschnitt „Bezugnahmemethoden und Anwendungsszenarien von Fay-Subjekten" von [04-meritoken-usage.md](./04-meritoken-usage.md)) werden typischerweise eine Reihe von `credential`s und eine Reihe von MeriToken-Einträgen gleichzeitig nach außen vorgelegt. Erstere belegen, dass das `Fay`-Subjekt die Vertretungsbefugnis hat; letztere MeriToken-Reihe stellt seine Kollaborationsgeschichte dar. Die zwei werden nebeneinander zitiert, nicht zusammengeführt.
- **Unabhängige Widerrufspfade**: Der Widerruf von `credential` wird von der ausstellenden Stelle bei einer Eigentumsänderung ausgelöst; der Widerruf von MeriToken wird von der in Bezug genommenen Partei als Rücknahme der Offenlegungserlaubnis ausgelöst. Diese zwei Widerrufspfade dürfen einander nicht kompensieren: Die ausstellende Stelle darf die Rücknahme von `credential` nicht nutzen, um einen bereits bezeugten MeriToken-Eintrag zu löschen; die in Bezug genommene Partei darf nicht ausgehend von einer Rücknahme der MeriToken-Offenlegung die ausstellende Stelle dazu zwingen, `credential` zurückzunehmen. Die Unabhängigkeit der Widerrufspfade folgt dem im Abschnitt „Die Grenze und Entsprechung" dieses Dokuments definierten Grundsatz.

> ⏳ **Ausstehende Illustration** (Slot: `meritoken-credential-boundary`)
> Beschreibung: Ein Vergleichsschaubild, das die Grenze und Entsprechung zwischen `credential` und MeriToken entlang der zwei semantischen Achsen „Identität und Eigentum" und „Beitrag und Bewertung" zeigt. In der Übergangsphase darf `credential-management.png` vorläufig wiederverwendet werden.
> Geplante Datei: `illustration/meritoken-credential-boundary.png`

## Verhältnis zu anderen Themen

| Thema | Bezug zu diesem Dokument |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Liefert die Definitionen der zwei grundlegenden Rollen, auf denen dieses Dokument anschließend aufsetzt, sowie die Zugehörigkeit von MeriToken zu `GMC`. |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Liefert die technische Semantik von MeriToken auf der Schicht von Eigentum und Nutzungsrechten, neben der dieses Dokument die Ausstellungs- und Widerrufskette von `credential` in Entsprechung setzt. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Verwendet in „politischer Logik" und „ökonomischer Struktur" die hier gezogene Grenze wieder, um zu verhindern, dass Themen von Identität und Eigentum den Raum von Beitrag und Bewertung zerquetschen. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | In der Bezugnahme durch Stellvertretung und Aggregation von `Fay`-Subjekten wird der hier formulierte Grundsatz „gemeinsam zitiert, getrennt getragen" wiederverwendet. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Übt die hier formulierte Grenzziehung in subjektübergreifenden hochdichten Kollaborationen und Rolling-Szenarien konkret ein. |
| [07-related-projects.md](./07-related-projects.md) | Liefert die offiziellen externen Verweise zu `credential`, `GMC`, ifay, `Fay` und weiteren vorgelagerten Themen. |

## Begriffsfußnoten

In diesem Dokument auftretende `Reserved_Term`s:

- **credential**: Ein credential, das heißt ein Identitäts- und Eigentumsnachweis eines persönlichen oder `Fay`-Subjekts; siehe [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, das übergeordnete System, dem MeriToken zugeordnet ist; siehe [glossary.md](./glossary.md).
- **Fay**: Ein nicht-persönliches Subjekt, das MeriToken in Bezug nimmt; siehe [glossary.md](./glossary.md).
- **ifay**: Name des Projektsystems; siehe [glossary.md](./glossary.md).

Die chinesische Hauptbezeichnung von MeriToken wird ausschließlich im Fließtext der Blueprints `zh-CN` und `zh-TW` als gewöhnliche Bezeichnung von MeriToken verwendet. Siehe den Abschnitt `Localized_Term` von [glossary.md](./glossary.md) für die Lokalisierungsregeln von MeriToken in den verschiedenen Sprachen.
