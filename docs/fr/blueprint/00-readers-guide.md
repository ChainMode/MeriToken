# 00 Guide de lecture

> Ce document est le point d'entrée du blueprint. Il explique l'axe rédactionnel du blueprint de ce dépôt, esquisse le profil des lectrices et lecteurs ainsi que les parcours de lecture recommandés et oriente vers les documents de la ligne principale (01–06).

![Bannière titre ifay](../../zh-CN/blueprint/illustration/ifay-title-banner.png)

## Contexte

Le blueprint de ce dépôt s'organise autour d'une analyse approfondie de **MeriToken**. Dans la nouvelle société, MeriToken assume deux rôles fondamentaux — « composant contractuel » et « connecteur des relations sociales » — et constitue donc l'axe de contenu de tous les documents de ce blueprint.

Des sujets tels que le système ifay, GMC, Fay, agent et phase sont positionnés comme un arrière-plan de soutien que l'analyse de MeriToken ne peut éviter. Ils ne sont introduits que lorsque le déploiement de MeriToken les rend strictement nécessaires, après quoi la lectrice ou le lecteur est dirigé via des liens externes vers les pages de documentation officielles correspondantes sur ifay.ai. Ce dépôt ne développe pas longuement ces sujets en amont ou périphériques.

Le lectorat visé par ce blueprint comprend :

- les chercheuses, chercheurs, autrices, auteurs et collaborateurs souhaitant comprendre de manière systématique les principes techniques, la signification sociale et les scénarios d'application de MeriToken ;
- les praticiennes et praticiens déjà familiarisés avec les concepts fondamentaux du système ifay et qui souhaitent maintenant examiner de plus près le rôle concret de MeriToken dans la nouvelle société, en particulier la manière dont MeriToken interagit avec les institutions environnantes ;
- les traductrices, traducteurs et personnes en charge de la maintenance qui doivent rédiger ou traduire ce blueprint MeriToken pour des versions linguistiques supplémentaires.

## Contenu central

### Axe du blueprint : MeriToken

Le corps principal du blueprint (01–06) déploie l'analyse approfondie de MeriToken dans l'ordre suivant :

- **Présentation (01)** : la manière dont MeriToken s'inscrit sous GMC ; les deux raisons pour lesquelles il est traité comme un sujet à part entière — comme composant contractuel de la nouvelle société et comme connecteur des relations sociales de la nouvelle société.
- **Principes techniques (02)** : chiffrement, stockage, récupération, garanties de confidentialité, garanties de propriété et de droit d'usage.
- **Signification sociale (03)** : relations sociales, logique politique, structure économique, cartographie du développement personnel, et la signification de MeriToken comme support de la cartographie entre « contribution personnelle et poids du discours social ».
- **Référencement et applications (04)** : les modes de référencement et les scénarios d'application typiques des deux classes d'entités effectuant des références — sujets personnels et sujets Fay.
- **Relation avec credential (05)** : définitions de rôles, frontière et correspondance entre credential et MeriToken.
- **Sujets avancés (06)** : cas d'extension tels que l'utilisation à haute densité entre plusieurs sujets et les scénarios à reconduction.

### Parcours de lecture recommandés

L'ordre de lecture recommandé est séquentiel selon la numérotation : `01 → 02 → 03 → 04 → 05 → 06`. Si le temps est limité ou si l'objectif est plus ciblé, les parcours dérivés suivants peuvent être utiles :

- **Pour les lectrices et lecteurs centrés sur la mise en œuvre technique** : `01 → 02 → 05 → 06` — établir d'abord la position de base de MeriToken, puis approfondir la boucle fermée chiffrement / stockage / récupération et la frontière avec credential.
- **Pour les lectrices et lecteurs centrés sur la signification sociale et institutionnelle** : `01 → 03 → 04 → 06` — comprendre d'abord la position globale de MeriToken, puis déployer la signification sociale, le référencement et les applications.
- **Pour les lectrices et lecteurs qui ont besoin d'expliquer MeriToken à d'autres** : `01 → 04 → 03` — clarifier d'abord « ce que c'est et qui l'utilise », puis combler le « pourquoi cela est conçu ainsi ».

`07-related-projects.md` est le document d'interface entre ce blueprint et les sujets en amont. C'est une référence complémentaire à consulter à la demande et il ne se trouve pas sur le parcours de lecture principal.

### Relation avec les sujets en amont et périphériques

Les sujets en amont et périphériques tels que ifay, GMC, Fay, agent et phase sont consolidés par [07-related-projects.md](./07-related-projects.md) sous la forme de « notes de positionnement minimales nécessaires + liste de liens externes », ce qui oriente la lectrice ou le lecteur vers les pages de documentation officielles correspondantes sur ifay.ai. Le blueprint lui-même ne développe pas longuement ces sujets, afin de préserver la densité rédactionnelle de l'axe MeriToken.

Si vous n'avez pas encore rencontré ces concepts en amont, nous vous recommandons de visiter d'abord les liens externes dans [07-related-projects.md](./07-related-projects.md) pour vous constituer un arrière-plan rapide, puis de revenir à la ligne principale en 01.

## Relation avec d'autres sujets

| N° | Sujet | Relation avec ce guide |
|------|------|---------------|
| 01 | Présentation de MeriToken | Point de départ de la ligne principale et document suivant ce guide |
| 02 | Principes techniques de MeriToken | Deuxième document de la ligne principale |
| 03 | Signification sociale de MeriToken | Troisième document de la ligne principale |
| 04 | Référencement et applications de MeriToken | Quatrième document de la ligne principale |
| 05 | Relation entre credential et MeriToken | Cinquième document de la ligne principale |
| 06 | Sujets avancés sur MeriToken | Sixième document de la ligne principale |
| 07 | Relation avec le système ifay | Interface et liste des liens externes pour les sujets en amont et périphériques |

## Notes terminologiques

`Reserved_Term` apparaissant dans ce document :

- **ifay** : nom du système du projet ; voir [glossary.md](./glossary.md).
- **GMC** : Global Merit Chain, le système de niveau supérieur auquel appartient MeriToken ; voir [glossary.md](./glossary.md).
- **Fay** : un sujet non personnel qui référence MeriToken ; voir [glossary.md](./glossary.md).
- **agent** : une entité agent dans les frameworks LLM traditionnels ; voir [glossary.md](./glossary.md).
- **phase** : un numéro d'étape évolutive dans le blueprint ; voir [glossary.md](./glossary.md).
- **credential** : un credential, c'est-à-dire un justificatif d'identité et de propriété pour un sujet personnel ou Fay ; voir [glossary.md](./glossary.md).

La forme principale chinoise de MeriToken n'est utilisée comme désignation conventionnelle de MeriToken que dans le corps de texte des blueprints `zh-CN` et `zh-TW`. Voir la section `Localized_Term` de [glossary.md](./glossary.md) pour les règles de localisation de MeriToken dans les différentes langues.
