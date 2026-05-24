# 04 Bezugnahme auf MeriToken und dessen Anwendungen

> Einleitung: Dieses Dokument knüpft an die Position aus [01-meritoken-overview.md](./01-meritoken-overview.md), den Abrufablauf aus [02-meritoken-technical.md](./02-meritoken-technical.md) und die gesellschaftliche Bedeutung aus [03-meritoken-social.md](./03-meritoken-social.md) an. Es klärt die drei Fragen „wer nimmt MeriToken in Bezug", „wie wird die Bezugnahme vollzogen" und „in welchen Szenarien wird MeriToken in Bezug genommen" jeweils gesondert für die zwei Klassen von Bezugnehmenden — persönliche Subjekte und `Fay`-Subjekte.

## Hintergrund

Die zwei grundlegenden Rollen von MeriToken — „Vertragsbaustein" und „Verbinder gesellschaftlicher Beziehungen" — kommen erst dann zum Tragen, wenn auf MeriToken tatsächlich Bezug genommen wird. Dieser Blueprint teilt MeriToken-Bezugnehmende ausdrücklich in zwei Klassen ein:

- **Persönliche Subjekte**: natürliche Personen, die als Bezugnehmende handeln und MeriToken nutzen, um sich an Zusammenarbeit zu beteiligen, Bewertungen auszudrücken und ihre Rechte geltend zu machen.
- **`Fay`-Subjekte**: nicht-persönliche Subjekte innerhalb des ifay-Systems, die die Verantwortung tragen, „MeriToken in Bezug zu nehmen" — zum Beispiel Organisationen, Projekte, Kollaborationseinheiten und Fay-isierte Dienstinstanzen. In der neuen Gesellschaft übernehmen `Fay`-Subjekte die Rolle des Bezugnehmenden parallel zu persönlichen Subjekten, doch ihre Bezugnahmemethoden und Anwendungsszenarien unterscheiden sich strukturell von denen persönlicher Subjekte.

Der Grund, die zwei Klassen von Bezugnehmenden parallel zu erörtern, besteht darin, zwei häufige Schieflagen in der neuen Gesellschaft zu vermeiden: MeriToken als bloße Erweiterung eines persönlichen Lebenslaufs zu behandeln oder MeriToken als bloß internes Bewertungswerkzeug innerhalb einer Organisation zu behandeln. Erst wenn die zwei Klassen von Bezugnehmenden nebeneinandergestellt werden, ergibt sich ein vollständiges Bild von MeriToken als gesellschaftlicher Infrastruktur.

Die Unterschiede zwischen `Fay` und dem traditionellen `agent` werden durch die offiziellen externen Links in [07-related-projects.md](./07-related-projects.md) getragen und hier nicht erneut erläutert.

## Zentrale Inhalte

### Bezugnahmemethoden und Anwendungsszenarien persönlicher Subjekte

Das persönliche Subjekt ist in der neuen Gesellschaft der direkteste Bezugnehmende auf MeriToken. Ein persönliches Subjekt ist sowohl Erzeuger von MeriToken (Beitragender, Bezeugender, Bewertender) als auch Nutzer von MeriToken (das in Zusammenarbeit, Einsprüchen und Beratung bestehende Einträge zitiert).

#### Bezugnahmemethoden

Die konkrete Weise, wie ein persönliches Subjekt MeriToken in Bezug nimmt, folgt dem in [02-meritoken-technical.md](./02-meritoken-technical.md) beschriebenen dreischrittigen Ablauf „Verweis → Verifizieren → Offenlegen" und mündet in vier Klassen konkreter Handlungen:

- **Bezugnahme durch Halten**: Das persönliche Subjekt hält die Menge seiner eigenen MeriToken in seinem Entwicklungsprofil, Kollaborationsarchiv und Beteiligungsarchiv und legt bestimmten Gegenstellen bei Bedarf eine Teilmenge vor. Der Akt der Vorlage erzeugt nur einen Bezugnahmedatensatz auf der niedrigsten Offenlegungsstufe und erzwingt keine Offenlegung der Details.
- **Bezugnahme durch Zitation**: In Argumentation, Vorschlägen und Einsprüchen zitiert das Subjekt bestehende MeriToken-Einträge — die eigenen oder die anderer — als Belege. Eine Zitation muss ein verifizierbares Verweis-Handle mitführen, sodass das Publikum Existenz und Eigentum am Eintrag unabhängig verifizieren kann, anstatt sich auf die einseitige Aussage des zitierenden Subjekts zu verlassen.
- **Beziehungsbezogene Bezugnahme**: Bei der Zusammenarbeit mit einer Gegenseite verwendet das Subjekt die bestehenden MeriToken-Einträge der Gegenseite als Vertrauensgrundlage und legt das Ergebnis der gegenwärtigen Zusammenarbeit als neue MeriToken-Einträge ab. Das ist die häufigste Umsetzung der Semantik „Verbinder gesellschaftlicher Beziehungen" auf der Seite des persönlichen Subjekts.
- **Bezugnahme durch Widerruf**: Das Subjekt widerruft eine zuvor einer bestimmten bezugnehmenden Partei gewährte hochstufige Offenlegungsautorisierung. Ein Widerruf löscht nicht die Spur des ursprünglichen Bezugnahmeakts, entzieht der bezugnehmenden Partei aber das Recht, den Inhalt weiterhin offenzulegen.

Diese vier Methoden teilen dasselbe technische Substrat (mehrseitige Mit-Signatur, Bindungen in der Kette, gestufte Offenlegung) und unterscheiden sich nur in den Auslöseszenarien und der Wahl der Offenlegungsstufe.

#### Anwendungsszenarien

Im Folgenden werden mehrere typische Anwendungsszenarien aufgeführt, die zeigen, wie ein persönliches Subjekt in der alltäglichen Zusammenarbeit der neuen Gesellschaft MeriToken nutzt:

- **Erste Begegnung in einer organisationsübergreifenden Zusammenarbeit**: Wenn ein persönliches Subjekt einer brandneuen Kollaborationsgruppe beitritt, kann es eine für das Thema der Gruppe relevante Teilmenge von MeriToken auf der niedrigsten Offenlegungsstufe vorlegen, sodass die Gruppe eine erste Prüfung vornehmen kann, ohne das persönliche Profil offenzulegen.
- **Sprechqualifikation in öffentlichen Fragen**: Wenn ein persönliches Subjekt in einer öffentlichen Frage spricht, zitiert es eigene MeriToken-Einträge zu benachbarten Fragen als Beleg seines Diskursgewichts, und das Publikum kann sie nach Bedarf unabhängig verifizieren.
- **Bildungs- und Vermittlungsszenarien**: Wenn ein persönliches Subjekt als Mentor handelt, wird das Mentorenverhältnis als entsprechende MeriToken-Einträge abgelegt. Die langfristige Akkumulation auf Seiten der mentorierten Person ergibt ein unabhängig verifizierbares Entwicklungsarchiv, das nicht durch eine Bildungseinrichtung eingesperrt ist.
- **Einspruchs- und Korrekturszenarien**: Wenn ein persönliches Subjekt einen bestehenden MeriToken-Eintrag für unfair hält, kann es einen Einspruchseintrag anstoßen, um den Hinterfragungsprozess selbst in `GMC` zu verzeichnen. Das Endergebnis (sei es bestätigt oder abgewiesen) wird ebenfalls als neuer Eintrag abgelegt.
- **Wechsel zwischen Identitäten**: Wenn ein persönliches Subjekt zwischen gesellschaftlichen Rollen wechselt (Beruf, Gemeinschaft, öffentliche Beteiligung), kann es selektiv die für die aktuelle Rolle relevante Teilmenge von MeriToken vorlegen und so eine Überbelichtung unverwandter Profile vermeiden.

Diese Szenarien folgen alle dem gemeinsamen Grundsatz „Standard der minimalen Offenlegung, szenariogetriebene Eskalation, jederzeit präsenter Widerruf", konsistent mit den Datenschutzgarantien aus [02-meritoken-technical.md](./02-meritoken-technical.md).

### Bezugnahmemethoden und Anwendungsszenarien von Fay-Subjekten

`Fay`-Subjekte sind die nicht-persönlichen Subjekte innerhalb des ifay-Systems, die die Verantwortung tragen, „MeriToken in Bezug zu nehmen". Ein `Fay`-Subjekt ist kein Ersatz für ein persönliches Subjekt; es ist ein Verstärker der Zusammenarbeit persönlicher Subjekte. Es übernimmt die Rollen Bezugnahme, Aggregation und Koordination in Kollaborationen größeren Maßstabs, mit mehr Beteiligten und längerem Lebenszyklus.

#### Bezugnahmemethoden

Die Bezugnahmemethoden von `Fay`-Subjekten teilen denselben grundlegenden Ablauf wie die persönlicher Subjekte, unterscheiden sich jedoch strukturell in Nutzungsszenarien und der Grenze der Befugnisse:

- **Bezugnahme durch Stellvertretung**: Ein `Fay`-Subjekt übt die Bezugnahmebefugnis im Namen einer Gruppe persönlicher Subjekte oder untergeordneter `Fay`-Subjekte innerhalb seines Autorisierungsrahmens einheitlich aus. Das Stellvertretungsverhältnis selbst wird als MeriToken-Eintrag protokolliert, wobei Autorisierungsumfang, Gültigkeitsdauer und Widerrufsbedingungen im Eintrag ausdrücklich genannt sind.
- **Bezugnahme durch Aggregation**: Ein `Fay`-Subjekt kann die MeriToken-Einträge mehrerer persönlicher Subjekte aggregieren, um eine nach außen gerichtete zusammengesetzte Bezugnahmefläche zu bilden. Aggregation ist kein Besitz: Jeder aggregierte Eintrag wird weiterhin von seinem ursprünglichen Eigentümer gehalten; das `Fay`-Subjekt hält nur das Nutzungsrecht, „diese Einträge in einem bestimmten Szenario in Bezug zu nehmen".
- **Bezugnahme durch Protokoll**: Wenn ein `Fay`-Subjekt mit einem anderen `Fay`-Subjekt zusammenarbeitet, beruht das Bezugnahmeverhältnis im Allgemeinen auf einem zuvor unterzeichneten Protokoll. Das Protokoll selbst wird ebenfalls als MeriToken-Einträge protokolliert und bildet ein Kollaborationshauptbuch zwischen `Fay`-Subjekten.
- **Bezugnahme zur Lebenszyklusverwaltung**: Ein `Fay`-Subjekt kann auf die MeriToken-Einträge zu seinem eigenen Lebenszyklus (Bildung, phase-Übergänge, Auflösung) Bezug nehmen, sodass externe Subjekte seinen Verlauf und seine Veränderungen einsehen können.

Die Bezugnahmebefugnis eines `Fay`-Subjekts ist technisch homolog zu der eines persönlichen Subjekts, doch institutionell stärker eingeschränkt: Die Grenze der Aggregation, der Umfang der Stellvertretung und die Sichtbarkeit des Protokolls erfordern relativ klare verifizierbare Datensätze, um das Ungleichgewicht zu vermeiden, „dass ein `Fay`-Subjekt seine Größenordnung ausnutzt, um persönliche Subjekte zu überstimmen".

#### Anwendungsszenarien

Typische Anwendungsszenarien von `Fay`-Subjekten in der neuen Gesellschaft sind die folgenden:

- **Kollaborationssubjekte öffentlicher Projekte**: Regions- und organisationsübergreifende öffentliche Projekte arbeiten nach außen als `Fay`-Subjekte zusammen und aggregieren die Beiträge vieler persönlicher Subjekte zu einer einheitlichen, nach außen gerichteten Bezugnahmefläche, die das Gesamt-MeriToken-Profil des Projekts darstellt.
- **Branchenweite Kollaborationshauptbücher**: Mehrere `Fay`-Subjekte einer Branche errichten über Bezugnahme durch Protokoll ein gemeinsames Hauptbuch, erkennen die MeriToken-Einträge der jeweils anderen wechselseitig an und vermeiden wiederholte organisationsübergreifende Abstimmungen.
- **Ausführungseinheiten in der Steuerung von Gemeinschaften**: `Fay`-Subjekte, die als Ausführungseinheiten innerhalb einer Gemeinschaft handeln, setzen Beschlüsse um, die durch Beratung gefasst wurden, und legen die Beschlusshandlungen als nachverfolgbare MeriToken-Einträge ab. Mitglieder der Gemeinschaft können diese Einträge jederzeit zitieren, um die Ausführungseinheit zu hinterfragen oder zu loben.
- **Generationenübergreifende Kontinuität von Projekten**: Langlaufende Projekte existieren in der Form von `Fay`-Subjekten, sodass das Kollaborationsarchiv auch nach dem Ausscheiden gründender Mitglieder erhalten bleibt. Neue Mitglieder erschließen sich den Verlauf des Projekts über Bezugnahme durch Halten und vermeiden so die Wissensbrüche eines „Projektneustarts".
- **Tragen von Verantwortung und Bezeugen der Einlösung**: Ein `Fay`-Subjekt in der neuen Gesellschaft ist sowohl Kollaborationsverstärker als auch Träger von Verantwortung. Wenn ein `Fay`-Subjekt nach außen ein Versprechen abgibt, wird das Versprechen selbst als MeriToken-Eintrag protokolliert, und Einlösung oder Verzug werden durch den entsprechenden Eintrag verankert.

Die Anwendungsszenarien von `Fay`-Subjekten ersetzen nicht jene persönlicher Subjekte. Vielmehr sind sie „zwei Maßstäbe derselben Infrastruktur": Persönliche Subjekte handhaben lokale, persönliche, einzelne Zusammenarbeit, während `Fay`-Subjekte regions-, organisations- und langzeitübergreifende Zusammenarbeit handhaben. Die zwei Klassen von Bezugnehmenden nehmen wechselseitig auf einander Bezug und tragen über MeriToken-Einträge wechselseitig Verantwortung, was die Kollaborationsökologie der neuen Gesellschaft ausmacht.

> ⏳ **Ausstehende Illustration** (Slot: `meritoken-usage-comparison`)
> Beschreibung: Ein Vergleichsschaubild, das beide Klassen von Bezugnehmenden — persönliche Subjekte und `Fay`-Subjekte — zusammen mit ihren Bezugnahmemethoden (Halten / Zitation / Beziehungsbezogen / Widerruf gegenüber Stellvertretung / Aggregation / Protokoll / Lebenszyklus) und typischen Anwendungsszenarien zeigt, mit Anmerkungen, die kennzeichnen, dass die zwei Klassen von Bezugnehmenden über MeriToken-Einträge wechselseitig auf einander Bezug nehmen und wechselseitig Verantwortung tragen.
> Geplante Datei: `illustration/meritoken-usage-comparison.png`

## Verhältnis zu anderen Themen

| Thema | Bezug zu diesem Dokument |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Liefert die Definitionen der zwei grundlegenden Rollen, auf denen die Bezugnahme und Anwendungen dieses Dokuments anschließend aufsetzen. |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Liefert den Abrufablauf und die Datenschutz- / Eigentumssemantik, die jede hier behandelte Bezugnahmemethode untermauern. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Liefert den Hintergrund der gesellschaftlichen Bedeutung für die hier behandelten Anwendungsszenarien (gesellschaftliche Beziehungen, politische Logik, ökonomische Struktur, Abbildung der persönlichen Entwicklung). |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Stellt auf der Schicht der Semantik „Identität und Eigentum" einen Kontrast zur hier vorgenommenen Semantik „Beitrag und Bewertung" her und verhindert eine Vermischung beider. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Erweitert die hier behandelten Anwendungsszenarien in subjektübergreifenden hochdichten Kollaborationen und Rolling-Szenarien. |
| [07-related-projects.md](./07-related-projects.md) | Liefert die offiziellen externen Verweise zu vorgelagerten Themen wie `Fay`, `agent`, ifay, `GMC` und Gesamtrahmen. |

## Begriffsfußnoten

In diesem Dokument auftretende `Reserved_Term`s:

- **Fay**: Ein nicht-persönliches Subjekt, das MeriToken in Bezug nimmt; siehe [glossary.md](./glossary.md).
- **agent**: Eine agent-Entität in herkömmlichen LLM-Frameworks; siehe [glossary.md](./glossary.md).
- **ifay**: Name des Projektsystems; siehe [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, das übergeordnete System, dem MeriToken zugeordnet ist; siehe [glossary.md](./glossary.md).
- **credential**: Ein credential, das heißt ein Identitäts- und Eigentumsnachweis eines persönlichen oder `Fay`-Subjekts; siehe [glossary.md](./glossary.md).

Die chinesische Hauptbezeichnung von MeriToken wird ausschließlich im Fließtext der Blueprints `zh-CN` und `zh-TW` als gewöhnliche Bezeichnung von MeriToken verwendet. Siehe den Abschnitt `Localized_Term` von [glossary.md](./glossary.md) für die Lokalisierungsregeln von MeriToken in den verschiedenen Sprachen.
