# 07 Verhältnis zum ifay-System

> Dieses Dokument bündelt in Form von „minimal notwendigen verortenden Hinweisen plus einer Liste externer Verweise, die auf die offiziellen Dokumentationsseiten zeigen", das Verhältnis zwischen mehreren vorgelagerten Themen im ifay-System und dem MeriToken-Blueprint und vermeidet so eine ausführliche Behandlung vorgelagerter Themen innerhalb dieses Repositorys.

## Hintergrund

Der Blueprint dieses Repositorys nimmt die vertiefte Analyse von MeriToken als Hauptachse. Themen wie ifay, GMC, Fay, agent, phase und Gesamtrahmen sind als unterstützender Hintergrund verortet, der für die Analyse von MeriToken notwendig ist, nicht als Schreibziel dieses Repositorys.

Um Pflegeaufwand und Versionsdrift zu vermeiden, entfaltet dieser Blueprint zu diesen vorgelagerten Themen keine ausführlichen Erzählungen innerhalb des Repositorys. Zu jedem Thema werden nur die für MeriToken minimal notwendigen verortenden Hinweise geliefert; anschließend werden Leserinnen und Leser über externe Verweise zu der entsprechenden offiziellen Dokumentationsseite auf ifay.ai geleitet, wo die maßgebliche Erzählung des vorgelagerten Projekts liegt.

Für Leserinnen und Leser, die dem ifay-System zum ersten Mal begegnen, empfehlen wir, dieses Dokument als „Einstiegsseite für externe Verweise" zu nutzen: zunächst über die Verweise in der offiziellen externen Verweisliste den vorgelagerten Hintergrund aufzubauen und dann zu [01-meritoken-overview.md](./01-meritoken-overview.md) zurückzukehren, um die Hauptlinie zu betreten.

## Verhältnis zu diesem Blueprint

Jeder vorgelagerte Begriff unten erscheint in diesem Blueprint in Form einer „minimalen Notiz", wobei seine minimale Verbindung zu MeriToken folgendermaßen ausgesprochen wird:

- **ifay**: der Name des Projektsystems, die technische und gesellschaftliche Gesamtbetriebsumgebung, von der MeriToken abhängt. Dieser Blueprint entfaltet das ifay-System selbst nicht und zitiert es nur dort, wo es bei der Beschreibung der Betriebsumgebung von MeriToken nötig ist.
- **GMC**: Global Merit Chain, das übergeordnete System, dem MeriToken zugeordnet ist. Dieser Blueprint erklärt die Zugehörigkeit von MeriToken zu GMC in [01-meritoken-overview.md](./01-meritoken-overview.md) und entfaltet das Gesamtdesign von GMC nicht.
- **Fay**: ein nicht-persönliches Subjekt innerhalb des ifay-Systems, das die Verantwortung trägt, „MeriToken in Bezug zu nehmen", und das neben persönlichen Subjekten als eine der beiden Klassen von MeriToken-Bezugnehmenden steht. Dieser Blueprint erörtert die Bezugnahmemethoden und Anwendungsszenarien von Fay-Subjekten gesondert in [04-meritoken-usage.md](./04-meritoken-usage.md).
- **agent**: eine Programmentität in herkömmlichen LLM-Frameworks, die Aufgaben autonom ausführt; im ifay-Paradigma stellt der agent einen Kontrast zum persönlichen Subjekt und zum Fay-Subjekt dar. Dieser Blueprint entfaltet die Erörterung der Unterschiede zwischen dem agent und dem ifay-Paradigma nicht; er liefert nur über externe Verweise den Einstieg zu maßgeblichen Definitionen.
- **phase**: eine Entwicklungsstufennummer für das Projekt, zu dem der Blueprint gehört. Die konkrete Stufensemantik, der Zeitplan und die Meilensteine werden von der ifay.ai-Dokumentation gepflegt; dieses Repository wiederholt sie nicht.
- **Gesamtrahmen**: die Gesamtarchitektur des ifay-Projekts und die Wechselwirkungen zwischen seinen Komponenten. Der Blueprint dieses Repositorys konzentriert sich auf MeriToken als eine Komponente; für den Gesamtrahmen besuchen Sie bitte direkt die entsprechende offizielle Dokumentationsseite auf ifay.ai.

## Liste offizieller externer Verweise

Die folgende Tabelle gibt das von diesem Blueprint geforderte minimale externe Verweis-Set wieder. Die Form der Verweise ist auf „auf die entsprechende offizielle Dokumentationsseite auf ifay.ai zeigen" festgelegt. Die konkreten URLs sind auf der Designebene fixiert; das Ersetzen durch eine andere Domain als `ifay.ai` ist nicht zulässig.

| Vorgelagerter Begriff | Minimaler Hinweis in diesem Blueprint | Upstream_Project_Doc_Link |
|----------|-----------------------|---------------------------|
| ifay     | Das gesamte Projektsystem, von dem MeriToken abhängt | https://ifay.ai/docs/ifay |
| GMC      | Das übergeordnete System, dem MeriToken zugeordnet ist (Global Merit Chain) | https://ifay.ai/docs/gmc |
| Fay      | Ein nicht-persönliches Subjekt, das MeriToken in Bezug nimmt, parallel zu persönlichen Subjekten | https://ifay.ai/docs/fay |
| agent    | Das traditionelle agent-Programm-Paradigma im Kontrast zum ifay-Paradigma | https://ifay.ai/docs/agent |

Andere vorgelagerte Themen wie phase und Gesamtrahmen haben eigene Seiten auf der ifay.ai-Site; Leserinnen und Leser navigieren bei Bedarf selbst zu ihnen. Dieser Blueprint fixiert diese Verweise hier nicht, um einer Linkdrift vorzubeugen.

## Begriffsfußnoten

In diesem Dokument auftretende `Reserved_Term`s:

- **ifay**: Name des Projektsystems; siehe [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, das übergeordnete System, dem MeriToken zugeordnet ist; siehe [glossary.md](./glossary.md).
- **Fay**: Ein nicht-persönliches Subjekt, das MeriToken in Bezug nimmt; siehe [glossary.md](./glossary.md).
- **agent**: Eine agent-Entität in herkömmlichen LLM-Frameworks; siehe [glossary.md](./glossary.md).
- **phase**: Eine Entwicklungsstufennummer im Blueprint; siehe [glossary.md](./glossary.md).

Die chinesische Hauptbezeichnung von MeriToken wird ausschließlich im Fließtext der Blueprints `zh-CN` und `zh-TW` als gewöhnliche Bezeichnung von MeriToken verwendet. Siehe den Abschnitt `Localized_Term` von [glossary.md](./glossary.md) für die Lokalisierungsregeln von MeriToken in den verschiedenen Sprachen.
