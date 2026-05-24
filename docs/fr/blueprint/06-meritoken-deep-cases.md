# 06 Sujets avancés sur MeriToken

> Introduction : ce document est le créneau d'extension de l'ensemble thématique MeriToken. En s'appuyant sur tous les accords antérieurs présents dans [01-meritoken-overview.md](./01-meritoken-overview.md) à [05-meritoken-credential.md](./05-meritoken-credential.md), il développe en sujets avancés autonomes deux configurations d'usage à haute densité de MeriToken dans la nouvelle société — « utilisation à haute densité entre plusieurs sujets » et « scénarios à reconduction ». Chaque sujet ne reformule pas les concepts déjà couverts sur la ligne principale ; il replace les mécanismes de la ligne principale dans un scénario de pression concret pour un nouvel examen.

## Contexte

La ligne principale, des documents 01 à 05, a clarifié la position de MeriToken, ses principes techniques, sa signification sociale, son référencement et ses applications, ainsi que sa frontière avec `credential`. Une fois la nouvelle société effectivement déployée, cependant, deux classes de configurations « à forte charge » émergent que la discussion de la ligne principale ne peut pas couvrir directement :

- **Utilisation à haute densité entre plusieurs sujets** : lorsque plusieurs sujets `Fay` et plusieurs sujets personnels référencent MeriToken en continu sur le même sujet, une référence individuelle paraît simple, mais l'agrégat soulève trois problèmes — surcoût, divulgation et agrégation.
- **Scénarios à reconduction** : lorsque le cycle de vie d'une collaboration est suffisamment long, MeriToken cesse d'être la trace d'un livrable ponctuel pour devoir traverser, sur plusieurs cycles, des phases d'accumulation, de révision, de retrait et d'archivage. Cela exige du mécanisme MeriToken qu'il reste cohérent à long terme, et pas seulement qu'il paraisse raisonnable sur un acte unique de référencement.

Ce document développe les deux sujets. Chaque sujet esquisse d'abord la source de la pression, puis revisite sous cette pression les mécanismes de la ligne principale (récupération, divulgation, trace, propriété et droits d'usage, frontière avec `credential`, etc.), et signale les questions ouvertes méritant un argumentaire supplémentaire ou un travail d'ingénierie. Ce document n'introduit pas de nouveaux concepts à la couche protocolaire ; tout est une dérivation continue de mécanismes déjà définis sur la ligne principale, appliqués dans de nouvelles configurations.

## Contenu central

### Sujet A : utilisation à haute densité entre plusieurs sujets

**Source de la pression** : dans la collaboration réelle de la nouvelle société, « un sujet `Fay` référence un MeriToken » est une configuration minimale trop idéalisée. Plus courant est le cas où, sur un même sujet, trois classes d'entités effectuant des références apparaissent simultanément :

- **Plusieurs sujets `Fay`** : par exemple des collaborateurs de différentes industries et régions qui référencent chacun les MeriToken pertinents au nom de leurs propres membres ;
- **Plusieurs sujets personnels** : par exemple les participants clés sur le sujet citent chacun les entrées MeriToken issues de leurs propres collaborations passées pertinentes ;
- **Référencement imbriqué** : les sujets `Fay` ci-dessus référencent eux-mêmes les entrées MeriToken de certains sujets personnels comme base de leur autorité de représentation.

Ce référencement à haute densité se produit dans le même sujet, la même fenêtre temporelle et la même surface de divulgation, et pousse simultanément plusieurs propriétés du mécanisme MeriToken jusqu'à leurs limites de pression.

**Mécanismes revisités** :

- **La frontière de l'agrégation des références** : le référencement par agrégation par un seul sujet `Fay` est déjà une surface de référencement composite (voir la section « Modes de référencement et scénarios d'application des sujets Fay » de [04-meritoken-usage.md](./04-meritoken-usage.md)). Lorsque les surfaces de référencement composites de plusieurs sujets `Fay` se superposent sur le même sujet, le relecteur externe n'a pas besoin que « chaque MeriToken soit déplié » mais qu'il « confirme que ces surfaces agrégées ne se contredisent pas, sans déplier les détails ». Cela signifie que le référencement par agrégation doit prendre en charge la « réconciliabilité au niveau de l'agrégation », et pas seulement la vérifiabilité au niveau des entrées individuelles.
- **Coordination de la divulgation par paliers** : en utilisation à haute densité, chaque partie référencée (un sujet personnel ou un sujet `Fay` de niveau inférieur) peut avoir une autorisation de palier de divulgation différente. L'agrégateur ne peut pas mélanger des divulgations de palier élevé et de palier faible dans une présentation externe unique ; sinon cela équivaut à forcer une divulgation de palier faible à monter en gamme. Le sujet A exige le principe « palier minimal de divulgation comme sécurité » : le palier de divulgation d'une surface agrégée n'est pas supérieur au palier d'autorisation le plus bas parmi les entrées référencées qu'elle contient, et n'est élevé dans son ensemble que lorsque chaque partie référencée y consent activement.
- **Écho du chemin de révocation** : lorsqu'un sujet personnel sous-jacent révoque son autorisation de divulgation, la part correspondant à cette entrée doit immédiatement devenir invalide dans toute surface agrégée d'un sujet `Fay` qui en dépendait. Il ne doit y avoir aucune situation où « l'amont a révoqué mais l'agrégation en aval continue à exposer au moyen de caches ». Cela étend la sémantique de « révocation et invalidation » de la section « Garanties de confidentialité » de [02-meritoken-technical.md](./02-meritoken-technical.md) au cadre imbriqué.
- **Lisibilité de la trace de récupération** : dans le cadre à haute densité, enregistrer chaque référence sous `GMC` fait gonfler rapidement le volume de traces d'un sujet unique. La trace à la couche du mécanisme reste nécessaire, mais pour la présentation humaine, elle doit être pliée selon les trois axes « sujet — sujet — temps », afin d'éviter que le processus d'audit ne soit noyé sous les entrées de trace brutes.

**Questions ouvertes** :

- L'ensemble exact de mécanismes d'engagement qui porte la réconciliabilité au niveau de l'agrégation doit être conçu de pair avec les règles de niveau supérieur de `GMC` ;
- Le flux de négociation entre « palier minimal de divulgation comme sécurité » et le souhait d'un participant individuel d'élever l'ensemble doit être lui-même enregistré sous forme d'entrées MeriToken ;
- Les règles de présentation pour le pliage des traces ne sont pas une question de couche protocolaire, mais elles doivent être convenues à l'unisson par la chaîne d'outils accompagnant le blueprint.

> ⏳ **Illustration en attente** (créneau : `meritoken-deep-cases-density`)
> Description : un schéma conceptuel présentant l'agrégation de références / la divulgation par paliers / les chemins de révocation de MeriToken dans des scénarios de collaboration inter-sujets à haute densité.
> Fichier prévu : `illustration/meritoken-deep-cases-density.png`

### Sujet B : scénarios à reconduction

**Source de la pression** : dans les projets à long cycle de vie, MeriToken ne reste pas à l'unité minimale « une contribution — une évaluation — une trace ». Il revient sur une longue échelle de temps à travers des cycles d'accumulation, de révision, de retrait et d'archivage. Les configurations typiques incluent les projets publics intergénérationnels, les collaborations open source en évolution longue et la gouvernance communautaire confrontée à plusieurs cohortes de participants. La pression apportée par de tels projets n'est plus la complexité d'un seul acte de référencement, mais la cohérence du mécanisme à long terme.

**Mécanismes revisités** :

- **Accumulation** : chaque étape du projet dépose de nouvelles entrées MeriToken qui sont enregistrées sous `GMC` et ne sont pas perdues lors des changements d'étape. Mais l'« image globale » du projet vers l'extérieur doit éviter d'empiler chaque entrée sans distinction ; un découpage par étape, par rôle et par sujet est nécessaire. Cela rejoint « de la capacité ponctuelle au portrait multidimensionnel » de la section « Cartographie du développement personnel » de [03-meritoken-social.md](./03-meritoken-social.md), mais du côté du projet, un sujet `Fay` doit assumer la responsabilité de l'agrégation par couches.
- **Révision** : lorsqu'une entrée MeriToken existante reçoit, à la couche factuelle, un nouveau témoignage, une nouvelle évaluation ou une nouvelle comparaison, la réponse appropriée est d'ajouter une entrée de révision plutôt que d'écraser l'original. L'entrée de révision est elle-même une entrée MeriToken, contenant la raison de la révision et la co-signature multipartite. Le long de la chronologie, une lectrice ou un lecteur peut voir à la fois l'entrée originale et les révisions ultérieures, évitant la situation où « une seule entrée est réécrite à plusieurs reprises et l'histoire est aplatie ».
- **Retrait** : dans un long cycle de vie, le retrait désigne non seulement le retrait des autorisations de divulgation, mais aussi le retrait de l'effet de l'entrée originale (par exemple, l'émetteur quitte, ou la précondition de la collaboration change). Le retrait d'effet ne supprime pas la trace ; il marque l'état de l'entrée comme « retiré » afin que les entités effectuant ultérieurement des références puissent distinguer « les références faites avant le retrait » des « références faites après le retrait ». L'acte de retrait suit le chemin de révocation indépendant défini dans la section « La frontière et la correspondance » de [05-meritoken-credential.md](./05-meritoken-credential.md), sans compenser le chemin de récupération de `credential`.
- **Archivage** : lorsqu'une étape du projet se termine ou que le projet dans son ensemble s'achève, les entrées MeriToken pertinentes doivent passer à l'état archivé plutôt qu'être détruites. À l'état archivé, les entrées peuvent encore être vérifiées et citées de manière indépendante, mais le palier de divulgation par défaut tombe au plus bas, évitant la situation où, des années après la fin d'un projet de longue durée, les entrées continuent à exposer les participants à un palier de divulgation élevé. La transition d'archivage elle-même est enregistrée sous `GMC`, évitant toute opacité du type « après un certain moment, la visibilité d'une entrée change discrètement ».

**Cohérence du mécanisme** : accumulation / révision / retrait / archivage forment un cycle complet, et chaque action laisse une trace sous forme de nouvelle entrée. Cela garantit que la dimension du « temps » elle-même est intégrée au mécanisme MeriToken, plutôt que d'être contrôlée unilatéralement de l'extérieur par le porteur du projet. Tout changement d'état le long de la dimension temporelle doit être vérifiable de manière indépendante, sans dépendre de l'interprétation du porteur du projet.

**Questions ouvertes** :

- La question de savoir si le périmètre de co-signature multipartite d'une entrée de révision doit correspondre exactement à celui de l'entrée originale doit être affinée scénario par scénario ;
- La question de savoir si le palier de divulgation par défaut de la transition d'archivage peut être ajusté collectivement par le porteur du projet et les participants, ainsi que le flux de négociation que cela exige ;
- La question de savoir si le poids du référencement inter-étapes décroît avec le temps est un choix stratégique propre à chaque projet et doit être pris en charge par la chaîne d'outils plutôt qu'imposé par la couche protocolaire.

## Relation avec d'autres sujets

| Sujet | Relation avec ce document |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Fournit les définitions des deux rôles fondamentaux. Le sujet A et le sujet B s'appuient tous deux sur « composant contractuel / connecteur des relations sociales ». |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Fournit la sémantique technique concrète de la récupération, de la divulgation, du retrait et des propriété/droits d'usage, que les sujets ici réutilisent à haute densité et sur de longues échelles de temps. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Fournit la base de signification sociale de la « cartographie du poids du discours ». Le sujet A la réutilise dans la collaboration inter-sujets ; le sujet B la réutilise dans les scénarios à reconduction. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Fournit les modes de référencement et les scénarios d'application pour les deux classes d'entités effectuant des références — sujets personnels et sujets `Fay`. Le sujet A ici en est l'extension sous l'empilement à haute densité. |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Fournit la frontière et la correspondance avec `credential`. Le sujet B ici réutilise le principe des « chemins de révocation indépendants » dans le chemin de retrait. |
| [07-related-projects.md](./07-related-projects.md) | Fournit les liens externes officiels pour les sujets en amont tels que ifay, `GMC`, `Fay`, `agent`, `phase` et le cadre global. |

## Notes terminologiques

`Reserved_Term` apparaissant dans ce document :

- **GMC** : Global Merit Chain, le système de niveau supérieur auquel appartient MeriToken ; voir [glossary.md](./glossary.md).
- **Fay** : un sujet non personnel qui référence MeriToken ; voir [glossary.md](./glossary.md).
- **credential** : un credential, c'est-à-dire un justificatif d'identité et de propriété pour un sujet personnel ou `Fay` ; voir [glossary.md](./glossary.md).
- **ifay** : nom du système du projet ; voir [glossary.md](./glossary.md).

La forme principale chinoise de MeriToken n'est utilisée comme désignation conventionnelle de MeriToken que dans le corps de texte des blueprints `zh-CN` et `zh-TW`. Voir la section `Localized_Term` de [glossary.md](./glossary.md) pour les règles de localisation de MeriToken dans les différentes langues.
