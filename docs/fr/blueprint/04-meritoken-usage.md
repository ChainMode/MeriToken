# 04 Référencement et applications de MeriToken

> Introduction : ce document poursuit la position de [01-meritoken-overview.md](./01-meritoken-overview.md), le flux de récupération de [02-meritoken-technical.md](./02-meritoken-technical.md) et la signification sociale de [03-meritoken-social.md](./03-meritoken-social.md). Il fait atterrir séparément les trois questions « qui référence MeriToken », « comment le référencement s'effectue » et « dans quels scénarios MeriToken est référencé » pour les deux classes d'entités effectuant des références — sujets personnels et sujets `Fay`.

## Contexte

Les deux rôles fondamentaux de MeriToken — « composant contractuel » et « connecteur des relations sociales » — n'entrent en jeu que lorsque MeriToken est effectivement référencé. Ce blueprint divise explicitement les entités effectuant des références à MeriToken en deux classes :

- **Sujets personnels** : personnes physiques agissant comme entités effectuant des références, utilisant MeriToken pour participer à la collaboration, exprimer des évaluations et faire valoir leurs droits.
- **Sujets `Fay`** : sujets non personnels au sein du système ifay qui assument la responsabilité de « référencer MeriToken » — par exemple organisations, projets, unités de collaboration et instances de service Fay-isées. Dans la nouvelle société, les sujets `Fay` assument le rôle d'entité effectuant des références en parallèle avec les sujets personnels, mais leurs modes de référencement et leurs scénarios d'application diffèrent structurellement de ceux des sujets personnels.

La raison de discuter les deux classes d'entités effectuant des références en parallèle est d'éviter deux dérives courantes dans la nouvelle société : traiter MeriToken comme une simple extension d'un CV personnel, ou traiter MeriToken comme un simple outil de notation interne au sein d'une organisation. Ce n'est qu'en plaçant côte à côte les deux classes d'entités effectuant des références que l'on peut présenter une image complète de MeriToken comme infrastructure sociale.

Les différences entre `Fay` et le `agent` traditionnel sont portées par les liens externes officiels de [07-related-projects.md](./07-related-projects.md) et ne sont pas reformulées ici.

## Contenu central

### Modes de référencement et scénarios d'application des sujets personnels

Le sujet personnel est l'entité la plus directe effectuant des références à MeriToken dans la nouvelle société. Un sujet personnel est à la fois un producteur de MeriToken (contributeur, témoin, évaluateur) et un utilisateur de MeriToken (citant des entrées existantes dans la collaboration, les recours et la délibération).

#### Modes de référencement

La manière concrète dont un sujet personnel référence MeriToken suit le flux en trois étapes « référence → vérification → divulgation » décrit dans [02-meritoken-technical.md](./02-meritoken-technical.md), et atterrit sur quatre classes d'actions concrètes :

- **Référencement par détention** : le sujet personnel détient l'ensemble de ses propres MeriToken dans son portrait de développement, son archive de collaboration et son archive de participation communautaire, et présente un sous-ensemble à des homologues spécifiques en cas de besoin. L'acte de présentation ne génère qu'un enregistrement de référencement au palier de divulgation le plus faible et n'oblige pas à la divulgation des détails.
- **Référencement par citation** : dans l'argumentation, les propositions et les recours, le sujet cite des entrées MeriToken existantes — les siennes ou celles d'autrui — comme preuves. Une citation doit être accompagnée d'une poignée de référence vérifiable, afin que l'auditoire puisse vérifier de manière indépendante l'existence et la propriété de l'entrée, plutôt que de s'appuyer sur la déclaration unilatérale de la partie citante.
- **Référencement relationnel** : lors d'une collaboration avec une autre partie, le sujet utilise les entrées MeriToken existantes de l'homologue comme base de confiance, et dépose le résultat de la collaboration présente sous forme de nouvelles entrées MeriToken. C'est l'atterrissage le plus courant de la sémantique de « connecteur des relations sociales » du côté du sujet personnel.
- **Référencement par retrait** : le sujet révoque une autorisation de palier de divulgation élevé précédemment accordée à une entité spécifique effectuant une référence. Un retrait n'efface pas la trace de l'action de référencement initiale, mais il supprime le droit de cette entité de continuer à exposer le contenu.

Ces quatre modes partagent le même substrat technique (co-signature multipartite, engagements en chaîne, divulgation par paliers), et ne diffèrent que par les scénarios déclencheurs et le choix du palier de divulgation.

#### Exemples de scénarios d'application

Voici plusieurs scénarios d'application typiques montrant comment un sujet personnel utilise MeriToken dans la collaboration quotidienne de la nouvelle société :

- **Première poignée de main d'une collaboration inter-organisations** : lorsqu'un sujet personnel rejoint un groupe de collaboration entièrement nouveau, il peut présenter un sous-ensemble de MeriToken pertinents pour le sujet du groupe au palier de divulgation le plus faible, permettant au groupe d'effectuer un examen initial sans exposer le portrait personnel.
- **Qualification de prise de parole sur les questions publiques** : lorsqu'un sujet personnel s'exprime sur une question publique, il cite ses propres entrées MeriToken sur des questions adjacentes comme preuves du poids de son discours, et l'auditoire peut les vérifier de manière indépendante au besoin.
- **Scénarios d'éducation et de transmission** : lorsqu'un sujet personnel agit comme mentor, la relation de mentorat est déposée sous forme d'entrées MeriToken correspondantes. L'accumulation à long terme par le mentoré produit une archive de développement vérifiable de manière indépendante qui n'est emprisonnée par aucune institution éducative.
- **Scénarios de recours et de correction** : lorsqu'un sujet personnel considère qu'une entrée MeriToken existante est injuste, il peut initier une entrée de recours pour enregistrer le processus de questionnement lui-même dans `GMC`. Le résultat final (qu'il soit retenu ou rejeté) est également déposé sous forme de nouvelle entrée.
- **Bascule entre identités** : lorsqu'un sujet personnel se déplace entre rôles sociaux (profession, communauté, participation publique), il peut présenter sélectivement le sous-ensemble de MeriToken pertinent pour le rôle actuel, évitant la sur-exposition de portraits non pertinents.

Ces scénarios suivent tous le principe partagé de « divulgation minimale par défaut, escalade pilotée par le scénario, révocation toujours présente », cohérent avec les garanties de confidentialité de [02-meritoken-technical.md](./02-meritoken-technical.md).

### Modes de référencement et scénarios d'application des sujets Fay

Les sujets `Fay` sont les sujets non personnels au sein du système ifay qui assument la responsabilité de « référencer MeriToken ». Un sujet `Fay` n'est pas un substitut au sujet personnel ; c'est un amplificateur de la collaboration des sujets personnels. Il assume le rôle de référencement, d'agrégation et de coordination dans des collaborations à plus grande échelle, avec plus de participants et un cycle de vie plus long.

#### Modes de référencement

Les modes de référencement des sujets `Fay` partagent le même flux sous-jacent que ceux des sujets personnels, mais diffèrent structurellement quant aux scénarios d'usage et à la frontière de l'autorité :

- **Référencement par procuration** : un sujet `Fay` exerce de manière unifiée l'autorité de référencement au nom d'un groupe de sujets personnels ou de sous-sujets `Fay` situés dans son périmètre d'autorisation. La relation de procuration elle-même est enregistrée sous forme d'entrée MeriToken, le périmètre d'autorisation, la durée de validité et les conditions de révocation étant tous explicitement énoncés dans l'entrée.
- **Référencement par agrégation** : un sujet `Fay` peut agréger les entrées MeriToken de plusieurs sujets personnels pour former une surface de référencement composite tournée vers l'extérieur. L'agrégation n'est pas la possession : chaque entrée agrégée est encore détenue par son propriétaire d'origine ; le sujet `Fay` ne détient que le droit d'usage de « référencer ces entrées dans un scénario particulier ».
- **Référencement par protocole** : lorsqu'un sujet `Fay` collabore avec un autre sujet `Fay`, la relation de référencement repose généralement sur un protocole pré-signé. Le protocole lui-même est également enregistré sous forme d'entrées MeriToken, constituant un registre de collaboration entre sujets `Fay`.
- **Référencement de gestion du cycle de vie** : un sujet `Fay` peut référencer les entrées MeriToken concernant son propre cycle de vie (formation, transitions de phase, dissolution), permettant aux sujets externes de voir son histoire et ses changements.

L'autorité de référencement d'un sujet `Fay` est techniquement homologue à celle d'un sujet personnel, mais à la couche institutionnelle elle est plus étroitement contrainte : la frontière de l'agrégation, le périmètre de la procuration et la visibilité du protocole exigent tous des enregistrements vérifiables relativement clairs, afin d'éviter le déséquilibre selon lequel « un sujet `Fay` exploiterait son échelle pour passer outre les sujets personnels ».

#### Exemples de scénarios d'application

Les scénarios d'application typiques des sujets `Fay` dans la nouvelle société sont les suivants :

- **Sujets de collaboration de projets publics** : les projets publics interrégionaux et inter-organisations collaborent vers l'extérieur en tant que sujets `Fay`, agrégeant les contributions de nombreux sujets personnels en une surface de référencement extérieure unifiée qui affiche le profil MeriToken global du projet.
- **Registres de collaboration au niveau de l'industrie** : plusieurs sujets `Fay` d'une industrie établissent un registre partagé via le référencement par protocole, reconnaissant mutuellement les entrées MeriToken les uns des autres et évitant la réconciliation répétée entre organisations.
- **Unités d'exécution dans la gouvernance communautaire** : les sujets `Fay` agissant comme unités d'exécution au sein d'une communauté mettent en œuvre les décisions prises par délibération, et déposent les actions décisionnelles sous forme d'entrées MeriToken traçables. Les membres de la communauté peuvent à tout moment citer ces entrées pour questionner ou féliciter l'unité d'exécution.
- **Continuité intergénérationnelle des projets** : les projets de longue durée existent sous la forme de sujets `Fay`, de sorte que l'archive de collaboration est préservée même après le départ des membres fondateurs. Les nouveaux membres accèdent à l'histoire du projet via le référencement par détention, évitant les ruptures de connaissance d'un « redémarrage de projet ».
- **Porter la responsabilité et témoigner de l'exécution** : un sujet `Fay` dans la nouvelle société est à la fois un amplificateur de collaboration et un porteur de responsabilité. Lorsqu'un sujet `Fay` fait une promesse externe, la promesse elle-même est enregistrée sous forme d'entrée MeriToken, et l'exécution ou le défaut sont ancrés par l'entrée correspondante.

Les scénarios d'application des sujets `Fay` ne remplacent pas ceux des sujets personnels. Ils constituent plutôt « deux échelles d'une même infrastructure » : les sujets personnels gèrent la collaboration locale, en face à face et ponctuelle, tandis que les sujets `Fay` gèrent la collaboration interrégionale, inter-organisations et à long terme. Les deux classes d'entités effectuant des références se référencent mutuellement et se portent mutuellement responsabilité à travers les entrées MeriToken, constituant l'écologie de collaboration de la nouvelle société.

> ⏳ **Illustration en attente** (créneau : `meritoken-usage-comparison`)
> Description : un schéma comparatif présentant les deux classes d'entités effectuant des références — sujets personnels et sujets `Fay` — ainsi que leurs modes de référencement (détention / citation / relationnel / retrait vs procuration / agrégation / protocole / cycle de vie) et leurs scénarios d'application typiques, avec des annotations montrant que les deux classes d'entités effectuant des références se référencent mutuellement et se portent mutuellement responsabilité à travers les entrées MeriToken.
> Fichier prévu : `illustration/meritoken-usage-comparison.png`

## Relation avec d'autres sujets

| Sujet | Relation avec ce document |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Fournit les définitions des deux rôles fondamentaux sur lesquels atterrissent ensuite le référencement et les applications de ce document. |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Fournit le flux de récupération et la sémantique de confidentialité / propriété qui sous-tendent chaque mode de référencement présenté ici. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Fournit l'arrière-plan de signification sociale pour les scénarios d'application présentés ici (relations sociales, logique politique, structure économique, cartographie du développement personnel). |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Au niveau de la sémantique « identité et propriété », contraste avec la sémantique « contribution et évaluation » présentée ici, empêchant les deux d'être mélangées. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Étend les scénarios d'application présentés ici dans la collaboration inter-sujets à haute densité et les scénarios à reconduction. |
| [07-related-projects.md](./07-related-projects.md) | Fournit les liens externes officiels pour les sujets en amont tels que `Fay`, `agent`, ifay, `GMC` et le cadre global. |

## Notes terminologiques

`Reserved_Term` apparaissant dans ce document :

- **Fay** : un sujet non personnel qui référence MeriToken ; voir [glossary.md](./glossary.md).
- **agent** : une entité agent dans les frameworks LLM traditionnels ; voir [glossary.md](./glossary.md).
- **ifay** : nom du système du projet ; voir [glossary.md](./glossary.md).
- **GMC** : Global Merit Chain, le système de niveau supérieur auquel appartient MeriToken ; voir [glossary.md](./glossary.md).
- **credential** : un credential, c'est-à-dire un justificatif d'identité et de propriété pour un sujet personnel ou `Fay` ; voir [glossary.md](./glossary.md).

La forme principale chinoise de MeriToken n'est utilisée comme désignation conventionnelle de MeriToken que dans le corps de texte des blueprints `zh-CN` et `zh-TW`. Voir la section `Localized_Term` de [glossary.md](./glossary.md) pour les règles de localisation de MeriToken dans les différentes langues.
