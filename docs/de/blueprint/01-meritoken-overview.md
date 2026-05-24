# 01 MeriToken-Überblick

> Einleitung: Dieses Dokument ist der Ausgangspunkt der Hauptlinie des Blueprints. Es verortet MeriToken innerhalb des ifay-Systems und nennt die zwei Gründe, weshalb MeriToken aus der gesamten ifay-Diskussion als eigenständiger Gegenstand herausgelöst wird — als Vertragsbaustein und als Verbinder gesellschaftlicher Beziehungen der neuen Gesellschaft. Die Dokumente 02 bis 06 bauen alle auf der hier etablierten Position auf.

## Hintergrund

Der „MeriToken", über den dieser Blueprint spricht, ist nicht ein weiteres allgemeines Treuepunktesystem oder Werkzeug zur Buchführung über Beiträge. Er ist ein Stück Basisinfrastruktur innerhalb der Betriebsumgebung der von ifay entworfenen „neuen Gesellschaft". MeriToken übernimmt zugleich grundlegende Rollen in zwei verschiedenen Richtungen: Auf der institutionellen Ebene wirkt er als „Vertragsbaustein" an Versprechen und deren Einlösung zwischen Personen und Organisationen mit; auf der Beziehungsebene verknüpft er als „Verbinder gesellschaftlicher Beziehungen" verstreute persönliche Beiträge, Kollaborationsdaten und gesellschaftliche Bewertungen.

Diese beiden Richtungen sind keine zwei parallelen Geschäftsbereiche. Sie sind Projektionen desselben Gegenstands auf unterschiedliche Abstraktionsebenen. Dieser Blueprint hebt MeriToken gerade deshalb zu einem Hauptlinienthema, weil zwischen den beiden Projektionen eine nicht zu vernachlässigende Spannung besteht: Wenn die institutionelle Strenge zunimmt, darf sie nicht ihrerseits die Elastizität der Beziehungsebene auffressen; wenn der Reichtum der Beziehungsebene wächst, darf er die Verifizierbarkeit der Vertragsebene nicht destabilisieren. Erst wenn die Position von MeriToken und die Gründe, ihn als eigenständigen Gegenstand zu behandeln, klar formuliert sind, können die Dokumente 02 bis 06 von einem gemeinsamen Ausgangspunkt aus arbeiten.

## Zentrale Inhalte

### Die Zugehörigkeit von MeriToken zu GMC

MeriToken ist kein eigenständiges Vermögensprotokoll. Er ist eine Klasse konkreter Buchungsobjekte unter einem übergeordneten System namens `GMC` (Global Merit Chain). `GMC` stellt globale kettenbasierte Buchführung, subjektübergreifende Verifizierbarkeit und letztendliche Konsistenz bereit. MeriToken sitzt darauf auf und trägt die konkrete Semantik aus „Beitrag — Bewertung — Bezugnahme".

Diese Unterordnung hat drei direkte Folgen:

- **Konsistenz des Datensubstrats**: Eigentumsübertragungen, Bezugnahmedatensätze, Widerrufe und Aktualisierungen von MeriToken folgen sämtlich der Kettensemantik von `GMC`. Es gibt kein separates Hauptbuch, was den Aufwand übergreifender Abstimmung vermeidet.
- **Externalität des Lebenszyklus**: MeriToken erstreckt sich nicht zwingend über den gesamten Lebenszyklus eines persönlichen Subjekts. Sichtbarkeit, Bezugnehmbarkeit und Akkumulierbarkeit innerhalb von `GMC` können stufenweise gemäß den Regeln der höheren Ebene geöffnet oder zurückgenommen werden, ohne die Definition von MeriToken selbst zu ändern.
- **Auslagerung der Deutungshoheit**: Die konkrete Bedeutung von MeriToken in der neuen Gesellschaft entwickelt sich mit dem übergeordneten System weiter. Dieser Blueprint überlässt mehr vorgelagerte Themen wie „Gesamtrahmen / `phase`-Entwicklung" der offiziellen Dokumentation auf ifay.ai (siehe [07-related-projects.md](./07-related-projects.md)), anstatt sie in diesem Repository erneut zu erläutern.

Der Grund, das Verhältnis zwischen MeriToken und `GMC` derart explizit auszusprechen, besteht darin, zu verhindern, dass MeriToken als isolierte begriffliche Erfindung verstanden wird. Es ist der Aufschlagpunkt des übergeordneten Systems auf der Ebene des „konkreten Buchungsobjekts" und zugleich der gemeinsame Ausgangspunkt für jede nachfolgende technische und gesellschaftliche Erörterung.

### Die zwei Gründe, MeriToken als eigenständigen Gegenstand zu behandeln

Obwohl MeriToken datentechnisch `GMC` untergeordnet ist, entscheidet sich dieses Repository, ihn aus der gesamten Diskussion über ifay als eigenständigen Blueprint herauszulösen, weil MeriToken zugleich zwei Klassen grundlegender Rollen in der neuen Gesellschaft trägt, von denen jede gewichtig genug ist, um eine eigene Untersuchungslinie zu rechtfertigen. Beide Rollen in die übergeordnete `GMC`-Diskussion zu falten würde ihre jeweiligen Grenzen verschwimmen lassen; sie getrennt zu behandeln erlaubt es, die doppelte Bedeutung von MeriToken in der neuen Gesellschaft präziser zu charakterisieren.

#### Als Vertragsbaustein der neuen Gesellschaft

Der erste Grund kommt aus der institutionellen Ebene. In der neuen Gesellschaft kann MeriToken als verifizierbarer Datensatz von „was ich getan habe, wem gegenüber ich rechenschaftspflichtig bin und wer es bezeugt hat" in Bezug genommen werden und trägt damit auf natürliche Weise die Rolle eines „Vertragsbausteins":

- **Verifizierbares Bit für Versprechen und Einlösung**: In subjektübergreifender Zusammenarbeit ist genau der Vorgang, durch den ein MeriToken erzeugt wird — ein Beitrag wird bezeugt, bewertet und in die Bücher eingetragen — eine minimale Einheit. Sie dient als verifizierbares Bit für Versprechen und Einlösung und nicht als nachträgliche subjektive Beurteilung durch einen Dritten.
- **Grobe Bonität wird durch feinkörnige Datensätze ersetzt**: Das „Vertrauensangebot", das die traditionelle Gesellschaft über grobe Objekte wie Bonitätsbewertungen, Reputation und persönliche Verbindungen trägt, kann in der neuen Gesellschaft in eine Reihe feinkörniger, nachverfolgbarer und verifizierbarer MeriToken-Einträge zerlegt werden. Die institutionelle Logik wandert dadurch von „Gesamtreputation" zu „spezifischen Datensätzen".
- **Grenze zu `credential`**: MeriToken ist ein verifizierbarer Datensatz von „was jemand getan hat", nicht ein Identitäts- und Eigentumsnachweis (credential) von „wer ich bin und was ich halte". Letzteres ist die Aufgabe von `credential`. Die Grenze und Entsprechung zwischen beiden wird in [05-meritoken-credential.md](./05-meritoken-credential.md) gesondert entfaltet und hier nicht wiederholt.

Die wesentliche Implikation der Sicht auf MeriToken als Vertragsbaustein lautet: Institutionelle Regeln hängen nicht mehr von einer zentralisierten Bonitätsmaschine ab. Die drei Dinge — „Vertragsabschluss, Einlösung, nachvollziehbarer Verzug" — beruhen jeweils auf konkreten MeriToken-Datensätzen. Ein Vertrag ist nicht mehr ein textuelles Versprechen; er wird zu einem strukturierten, in Bezug nehmbaren, prüfbaren Objekt.

#### Als Verbinder gesellschaftlicher Beziehungen der neuen Gesellschaft

Der zweite Grund kommt aus der Beziehungsebene. Derselbe MeriToken-Eintrag ist zusätzlich zur Rolle als Vertragsbaustein zugleich ein Knoten gesellschaftlicher Beziehungen, der verstreute Subjekte miteinander verbindet:

- **Minimale Kanten des Beziehungsgraphen**: Jeder MeriToken-Datensatz enthält die mehrseitige Beziehung „Beitragender — Bewertender — Leistungsempfangender". Diese ternären Beziehungen bilden auf natürliche Weise den Beziehungsgraphen der neuen Gesellschaft. Der Graph als Ganzes muss von keinem zentralen Knoten gepflegt werden; er setzt sich aus den lokalen Beziehungen zusammen, die in jedem MeriToken-Eintrag eingebettet sind.
- **Verbindung über Subjekttypen hinweg**: Der Verbinder ist gegenüber der Subjektform indifferent. Persönliche Subjekte untereinander, persönliche Subjekte mit `Fay`-Subjekten und `Fay`-Subjekte untereinander können alle über Bezugnahmebeziehungen von MeriToken stabile Kollaborationsketten bilden. Die Einzelheiten, wie `Fay`-Subjekte MeriToken in Bezug nehmen, sind in [04-meritoken-usage.md](./04-meritoken-usage.md) ausgeführt.
- **Migrationspfad von Fremder zu Bekanntem**: MeriToken ist nicht nur ein Datensatz von „bereits gebildeten Beziehungen"; er ist auch ein Einstiegspunkt für „noch nicht gebildete Beziehungen". Fremde können ein Anfangsmaß an Vertrauen herstellen, indem sie auf bestehende MeriToken-Einträge der Gegenseite verweisen, und das Ergebnis der gegenwärtigen Zusammenarbeit anschließend in neu erzeugten MeriToken-Einträgen ablegen. Gesellschaftliche Beziehungen in der neuen Gesellschaft erhalten dadurch einen strukturierten Pfad von Fremder zu Bekanntem.

Die wesentliche Implikation der Sicht auf MeriToken als Verbinder gesellschaftlicher Beziehungen lautet: Gesellschaftliche Beziehungen hängen nicht mehr von Plattformalgorithmen-Empfehlungen und Black-Box-Bewertungen ab. Sie kehren zu einem lokalisierten Erzeugungsmechanismus zurück, der in „konkreter Zusammenarbeit, konkretem Bezeugen und konkreter Bezugnahme" wurzelt.

> ⏳ **Ausstehende Illustration** (Slot: `meritoken-overview-contract`)
> Beschreibung: Ein konzeptionelles Schaubild, das gleichzeitig zeigt, wie MeriToken in der neuen Gesellschaft die zwei grundlegenden Rollen „Vertragsbaustein" und „Verbinder gesellschaftlicher Beziehungen" trägt, und kennzeichnet, dass er dem übergeordneten System `GMC` untergeordnet ist.
> Geplante Datei: `illustration/meritoken-overview-contract.png`

## Verhältnis zu anderen Themen

Dieses Dokument ist der Ausgangspunkt der Hauptlinie 01–06. Sein Bezug zu nachfolgenden Themen ist im Folgenden zusammengefasst:

| Nachfolgendes Thema | Bezug zu diesem Dokument |
|----------|-------------|
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Setzt die zwei Rollen „Vertragsbaustein" und „Verbinder gesellschaftlicher Beziehungen" auf die technischen Prinzipien von Verschlüsselung, Speicherung, Abruf, Privatsphäre, Eigentums- und Nutzungsrechten auf. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Entfaltet die zwei Rollen weiter in vier Stränge gesellschaftlicher Bedeutung: gesellschaftliche Beziehungen, politische Logik, ökonomische Struktur und Abbildung der persönlichen Entwicklung. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Konkretisiert die zwei Rollen in den Bezugnahmemethoden und Anwendungsszenarien der zwei Klassen von Bezugnehmenden — „persönliche Subjekte" und „`Fay`-Subjekte". |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Definiert unter der Semantik „Vertragsbaustein" die Grenze und Entsprechung zwischen MeriToken und `credential`. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Entwickelt vertiefende Untersuchungen der zwei Rollen in hochdichten Szenarien wie subjektübergreifender Zusammenarbeit und Rolling-Szenarien. |
| [07-related-projects.md](./07-related-projects.md) | Liefert die minimal verortenden Hinweise und die externen Verweise auf die offizielle Dokumentation für vorgelagerte und periphere Themen wie `GMC`, ifay, `Fay`, `agent`, `phase` und den Gesamtrahmen. |

Wenn Sie [00-readers-guide.md](./00-readers-guide.md) noch nicht gelesen haben, empfehlen wir, dort zunächst die Gesamtsicht zu etablieren und dann hierher zurückzukehren, um auf der Hauptlinie fortzufahren.

## Begriffsfußnoten

In diesem Dokument auftretende `Reserved_Term`s:

- **GMC**: Global Merit Chain, das übergeordnete System, dem MeriToken zugeordnet ist; siehe [glossary.md](./glossary.md).
- **Fay**: Ein nicht-persönliches Subjekt, das MeriToken in Bezug nimmt; siehe [glossary.md](./glossary.md).
- **credential**: Ein credential, das heißt ein Identitäts- und Eigentumsnachweis eines persönlichen oder `Fay`-Subjekts; siehe [glossary.md](./glossary.md).
- **ifay**: Name des Projektsystems; siehe [glossary.md](./glossary.md).
- **agent**: Eine agent-Entität in herkömmlichen LLM-Frameworks; siehe [glossary.md](./glossary.md).
- **phase**: Eine Entwicklungsstufennummer im Blueprint; siehe [glossary.md](./glossary.md).

Die chinesische Hauptbezeichnung von MeriToken wird ausschließlich im Fließtext der Blueprints `zh-CN` und `zh-TW` als gewöhnliche Bezeichnung von MeriToken verwendet. Siehe den Abschnitt `Localized_Term` von [glossary.md](./glossary.md) für die Lokalisierungsregeln von MeriToken in den verschiedenen Sprachen.
