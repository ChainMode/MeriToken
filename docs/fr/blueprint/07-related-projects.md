# 07 Relation avec le système ifay

> Ce document, sous la forme de « notes de positionnement minimales nécessaires + liste de liens externes vers les pages de documentation officielles », consolide la relation entre plusieurs sujets en amont du système ifay et le blueprint MeriToken, évitant un traitement étendu des sujets en amont à l'intérieur de ce dépôt.

## Contexte

Le blueprint de ce dépôt prend pour axe principal l'analyse approfondie de MeriToken. Des sujets tels que ifay, GMC, Fay, agent, phase et le cadre global sont positionnés comme un arrière-plan de soutien nécessaire à l'analyse de MeriToken, et non comme l'objectif rédactionnel de ce dépôt.

Pour éviter le coût de maintenance et la dérive de version, ce blueprint ne déploie pas de récits étendus de ces sujets en amont à l'intérieur du dépôt. Pour chaque sujet, seules les notes de positionnement minimales nécessaires liées à MeriToken sont fournies, après quoi la lectrice ou le lecteur est dirigé via des liens externes vers la page de documentation officielle correspondante sur ifay.ai, où vit le récit faisant autorité du projet en amont.

Pour les lectrices et lecteurs qui rencontrent le système ifay pour la première fois, nous recommandons d'utiliser ce document comme « page d'entrée des liens externes » : se constituer d'abord l'arrière-plan en amont en suivant les liens de la liste des liens externes de la documentation officielle, puis revenir à [01-meritoken-overview.md](./01-meritoken-overview.md) pour entrer dans la ligne principale.

## Relation avec ce blueprint

Chaque terme en amont ci-dessous apparaît dans ce blueprint sous la forme d'une « note minimale », sa connexion minimale avec MeriToken étant énoncée comme suit :

- **ifay** : nom du système du projet, l'environnement opérationnel technique et social global dont dépend MeriToken. Ce blueprint ne déploie pas le système ifay lui-même et ne le cite que selon les besoins lors de la description de l'environnement opérationnel de MeriToken.
- **GMC** : Global Merit Chain, le système de niveau supérieur auquel appartient MeriToken. Ce blueprint explique la subordination de MeriToken à GMC dans [01-meritoken-overview.md](./01-meritoken-overview.md), et ne déploie pas la conception globale de GMC.
- **Fay** : un sujet non personnel au sein du système ifay qui assume la responsabilité de « référencer MeriToken » et qui se tient aux côtés des sujets personnels comme l'une des deux classes d'entités effectuant des références à MeriToken. Ce blueprint discute les modes de référencement et les scénarios d'application des sujets Fay de manière indépendante dans [04-meritoken-usage.md](./04-meritoken-usage.md).
- **agent** : une entité programmatique dans les frameworks LLM traditionnels qui exécute des tâches de manière autonome ; dans le paradigme ifay, l'agent fournit un contraste avec le sujet personnel et le sujet Fay. Ce blueprint ne déploie pas la discussion des différences entre l'agent et le paradigme ifay ; il fournit uniquement l'entrée vers les définitions faisant autorité via des liens externes.
- **phase** : un numéro d'étape évolutive pour le projet auquel appartient le blueprint. La sémantique d'étape concrète, la chronologie et les jalons sont maintenus par la documentation ifay.ai ; ce dépôt ne les reformule pas.
- **Cadre global** : l'architecture globale du projet ifay et les interactions entre ses composants. Le blueprint de ce dépôt se concentre sur MeriToken comme un composant ; pour le cadre global, veuillez consulter directement la page de documentation officielle correspondante sur ifay.ai.

## Liste des liens externes vers la documentation officielle

Le tableau ci-dessous donne l'ensemble minimal de liens externes requis par ce blueprint. La forme des liens est figée à « pointer vers la page de documentation officielle correspondante sur ifay.ai ». Les URL concrètes sont épinglées à la couche de conception ; la substitution d'un domaine autre que `ifay.ai` n'est pas autorisée.

| Terme en amont | Note minimale dans ce blueprint | Upstream_Project_Doc_Link |
|----------|-----------------------|---------------------------|
| ifay     | Le système global du projet dont dépend MeriToken | https://ifay.ai/docs/ifay |
| GMC      | Le système de niveau supérieur auquel appartient MeriToken (Global Merit Chain) | https://ifay.ai/docs/gmc |
| Fay      | Un sujet non personnel qui référence MeriToken, en parallèle avec les sujets personnels | https://ifay.ai/docs/fay |
| agent    | Le paradigme traditionnel d'agent programmatique mis en contraste avec le paradigme ifay | https://ifay.ai/docs/agent |

D'autres sujets en amont tels que phase et le cadre global disposent de pages dédiées sur le site ifay.ai ; les lectrices et lecteurs sont attendus pour naviguer sur le site afin d'y accéder selon leurs besoins. Ce blueprint n'épingle pas ces liens ici, afin d'éviter la dérive des liens.

## Notes terminologiques

`Reserved_Term` apparaissant dans ce document :

- **ifay** : nom du système du projet ; voir [glossary.md](./glossary.md).
- **GMC** : Global Merit Chain, le système de niveau supérieur auquel appartient MeriToken ; voir [glossary.md](./glossary.md).
- **Fay** : un sujet non personnel qui référence MeriToken ; voir [glossary.md](./glossary.md).
- **agent** : une entité agent dans les frameworks LLM traditionnels ; voir [glossary.md](./glossary.md).
- **phase** : un numéro d'étape évolutive dans le blueprint ; voir [glossary.md](./glossary.md).

La forme principale chinoise de MeriToken n'est utilisée comme désignation conventionnelle de MeriToken que dans le corps de texte des blueprints `zh-CN` et `zh-TW`. Voir la section `Localized_Term` de [glossary.md](./glossary.md) pour les règles de localisation de MeriToken dans les différentes langues.
