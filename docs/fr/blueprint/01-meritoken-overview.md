# 01 Présentation de MeriToken

> Introduction : ce document est le point de départ de la ligne principale du blueprint. Il situe MeriToken au sein du système ifay et donne les deux raisons pour lesquelles MeriToken est extrait de la discussion globale d'ifay en tant que sujet à part entière — comme composant contractuel et comme connecteur des relations sociales de la nouvelle société. Les documents 02 à 06 reposent tous sur la position établie ici.

## Contexte

Le « MeriToken » dont traite ce blueprint n'est pas encore un autre programme de fidélité généraliste ou un outil de comptabilisation des contributions. Il s'agit d'un élément d'infrastructure fondamental au sein de l'environnement opérationnel de la « nouvelle société » envisagée par ifay. MeriToken assume simultanément des rôles fondamentaux dans deux directions distinctes : à la couche institutionnelle, il participe aux promesses et à leur exécution entre individus et organisations sous la forme d'un « composant contractuel » ; à la couche relationnelle, il tisse ensemble des contributions personnelles dispersées, des traces de collaboration et des évaluations sociales sous la forme d'un « connecteur des relations sociales ».

Ces deux directions ne sont pas deux lignes d'activité parallèles. Ce sont des projections du même actif sur différentes couches d'abstraction. Ce blueprint élève MeriToken au rang de sujet de la ligne principale précisément parce qu'il existe une tension non négligeable entre les deux projections : lorsque la rigueur institutionnelle augmente, elle ne doit pas dévorer en retour l'élasticité de la couche relationnelle ; lorsque la richesse de la couche relationnelle s'accroît, elle ne doit pas déstabiliser la vérifiabilité de la couche contractuelle. Ce n'est qu'après avoir clairement énoncé la position de MeriToken et les raisons de le traiter comme un sujet autonome que les documents 02 à 06 peuvent partager un même point de départ.

## Contenu central

### Comment MeriToken s'inscrit sous GMC

MeriToken n'est pas un protocole d'actif autonome. C'est l'une des classes d'objets comptables concrets relevant de `GMC` (Global Merit Chain), un système de niveau supérieur. `GMC` fournit la comptabilité globale en chaîne, la vérifiabilité inter-sujets et la cohérence à terme. MeriToken s'inscrit au-dessus et porte la sémantique concrète de « contribution — évaluation — référencement ».

Cette subordination entraîne trois conséquences directes :

- **Cohérence du substrat de données** : les transferts de propriété, les enregistrements de référencement, les révocations et les mises à jour de MeriToken suivent tous la sémantique de chaîne de `GMC`. Il n'y a pas de registre séparé, ce qui évite le coût d'une réconciliation inter-registres.
- **Externalité du cycle de vie** : MeriToken ne couvre pas nécessairement l'intégralité du cycle de vie d'un sujet personnel. Sa visibilité, sa référençabilité et sa cumulabilité au sein de `GMC` peuvent être ouvertes ou retirées par étapes selon les règles de niveau supérieur, sans modifier la définition de MeriToken lui-même.
- **Externalisation de l'autorité interprétative** : la signification concrète de MeriToken dans la nouvelle société évolue à mesure que le système de niveau supérieur évolue. Ce blueprint choisit de laisser davantage de sujets en amont, tels que le « cadre global / l'évolution par `phase` », à la documentation officielle sur ifay.ai (voir [07-related-projects.md](./07-related-projects.md)) plutôt que de les reformuler dans ce dépôt.

La raison pour laquelle la relation de MeriToken avec `GMC` est énoncée si explicitement est d'éviter que les lectrices et lecteurs ne comprennent MeriToken comme une invention conceptuelle isolée. Il s'agit du point d'atterrissage du système de niveau supérieur au niveau de l'« objet comptable concret », et également du point de départ commun de toutes les discussions techniques et sociales ultérieures.

### Les deux raisons de traiter MeriToken comme un sujet autonome

Bien que MeriToken soit, au plan des données, subordonné à `GMC`, ce dépôt choisit de l'extraire de la discussion globale d'ifay sous la forme d'un blueprint autonome parce que MeriToken assume simultanément deux classes de rôles fondamentaux dans la nouvelle société, chacune suffisamment substantielle pour justifier sa propre ligne d'investigation. Replier les deux rôles dans la discussion globale de `GMC` brouillerait leurs frontières respectives ; les traiter séparément nous permet de caractériser plus précisément la double signification de MeriToken dans la nouvelle société.

#### Comme composant contractuel de la nouvelle société

La première raison provient de la couche institutionnelle. Dans la nouvelle société, MeriToken peut être référencé comme un enregistrement vérifiable de « ce que j'ai fait, envers qui je suis responsable et qui en a été témoin », et assume donc naturellement le rôle de « composant contractuel » :

- **Un bit vérifiable de la promesse et de l'exécution** : dans la collaboration inter-sujets, le processus même par lequel un MeriToken est généré — une contribution témoignée, évaluée et inscrite aux registres — constitue une unité minimale. Il sert de bit vérifiable de la promesse et de son exécution, sans nécessiter qu'un tiers prononce après coup une adjudication subjective.
- **Remplacer le crédit à gros grain par des enregistrements à grain fin** : « l'offre de confiance » que la société traditionnelle porte à travers des objets à gros grain tels que les scores de crédit, la réputation et les relations personnelles peut, dans la nouvelle société, être décomposée en une série d'entrées MeriToken à grain fin, traçables et vérifiables. La logique institutionnelle migre ainsi de la « réputation globale » vers les « enregistrements spécifiques ».
- **Frontière avec `credential`** : MeriToken est un enregistrement vérifiable de « ce que l'on a fait », non un credential — c'est-à-dire un justificatif d'identité et de propriété — de « qui je suis et ce que je détiens ». Cette dernière fonction relève de la responsabilité de `credential`. La frontière et la correspondance entre les deux sont déployées séparément dans [05-meritoken-credential.md](./05-meritoken-credential.md) et ne sont pas répétées ici.

L'implication clé du fait de considérer MeriToken comme un composant contractuel est la suivante : les règles institutionnelles ne dépendent plus d'une machine centralisée d'évaluation du crédit. Les trois éléments — « formation du contrat, exécution, défaut traçable » — sont chacun ancrés dans des enregistrements MeriToken concrets. Un contrat n'est plus une promesse textuelle ; il devient un objet structuré, référençable et auditable.

#### Comme connecteur des relations sociales de la nouvelle société

La seconde raison provient de la couche relationnelle. La même entrée MeriToken, en plus de porter le rôle de composant contractuel, est aussi un nœud de relations sociales qui relie les uns aux autres des sujets dispersés :

- **Arêtes minimales du graphe relationnel** : chaque enregistrement MeriToken contient la relation multipartite « contributeur — évaluateur — bénéficiaire du service ». Ces relations ternaires constituent naturellement le graphe relationnel de la nouvelle société. Le graphe dans son ensemble n'a pas besoin d'être maintenu par un nœud central ; il est assemblé à partir des relations locales encastrées dans chaque entrée MeriToken.
- **Connecter les types de sujets** : le connecteur est indifférent à la forme du sujet. Les sujets personnels entre eux, les sujets personnels avec les sujets `Fay`, et les sujets `Fay` entre eux peuvent tous former des chaînes de collaboration stables via les relations de référencement de MeriToken. Les détails de la manière dont les sujets `Fay` référencent MeriToken sont développés dans [04-meritoken-usage.md](./04-meritoken-usage.md).
- **Un parcours de migration de l'inconnu à la connaissance** : MeriToken n'est pas seulement un enregistrement de « relations déjà formées » ; c'est aussi un point d'entrée pour les « relations qui ne se sont pas encore formées ». Des inconnus peuvent établir un niveau initial de confiance en référençant mutuellement leurs entrées MeriToken existantes, puis déposer le résultat de la collaboration présente dans de nouvelles entrées MeriToken. Les relations sociales dans la nouvelle société acquièrent ainsi un parcours structuré allant de l'inconnu à la connaissance.

L'implication clé du fait de considérer MeriToken comme un connecteur des relations sociales est la suivante : les relations sociales ne dépendent plus de recommandations algorithmiques de plateforme ni de notations en boîte noire. Elles reviennent à un mécanisme de génération localisé, enraciné dans la « collaboration concrète, le témoignage concret et le référencement concret ».

> ⏳ **Illustration en attente** (créneau : `meritoken-overview-contract`)
> Description : un schéma conceptuel qui présente simultanément MeriToken portant les deux rôles fondamentaux de « composant contractuel » et de « connecteur des relations sociales » dans la nouvelle société, et qui indique sa subordination au système de niveau supérieur `GMC`.
> Fichier prévu : `illustration/meritoken-overview-contract.png`

## Relation avec d'autres sujets

Ce document est le point de départ de la ligne principale 01–06. Sa connexion avec les sujets ultérieurs est résumée ci-dessous :

| Sujet ultérieur | Connexion avec ce document |
|----------|-------------|
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Fait atterrir les deux rôles « composant contractuel » et « connecteur des relations sociales » sur les principes techniques du chiffrement, du stockage, de la récupération, de la confidentialité, de la propriété et des droits d'usage. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Continue à déployer les deux rôles selon quatre fils de signification sociale : relations sociales, logique politique, structure économique et cartographie du développement personnel. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Concrétise les deux rôles en modes de référencement et scénarios d'application des deux classes d'entités effectuant des références — « sujets personnels » et « sujets `Fay` ». |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Définit, sous la sémantique de « composant contractuel », la frontière et la correspondance entre MeriToken et `credential`. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Développe des études avancées des deux rôles dans des scénarios à haute densité tels que la collaboration inter-sujets et les scénarios à reconduction. |
| [07-related-projects.md](./07-related-projects.md) | Fournit les notes de positionnement minimales et les liens externes vers la documentation officielle pour les sujets en amont et périphériques tels que `GMC`, ifay, `Fay`, `agent`, `phase` et le cadre global. |

Si vous n'avez pas encore lu [00-readers-guide.md](./00-readers-guide.md), nous vous recommandons d'y revenir d'abord pour établir la vue d'ensemble, puis de revenir ici pour poursuivre la ligne principale.

## Notes terminologiques

`Reserved_Term` apparaissant dans ce document :

- **GMC** : Global Merit Chain, le système de niveau supérieur auquel appartient MeriToken ; voir [glossary.md](./glossary.md).
- **Fay** : un sujet non personnel qui référence MeriToken ; voir [glossary.md](./glossary.md).
- **credential** : un credential, c'est-à-dire un justificatif d'identité et de propriété pour un sujet personnel ou `Fay` ; voir [glossary.md](./glossary.md).
- **ifay** : nom du système du projet ; voir [glossary.md](./glossary.md).
- **agent** : une entité agent dans les frameworks LLM traditionnels ; voir [glossary.md](./glossary.md).
- **phase** : un numéro d'étape évolutive dans le blueprint ; voir [glossary.md](./glossary.md).

La forme principale chinoise de MeriToken n'est utilisée comme désignation conventionnelle de MeriToken que dans le corps de texte des blueprints `zh-CN` et `zh-TW`. Voir la section `Localized_Term` de [glossary.md](./glossary.md) pour les règles de localisation de MeriToken dans les différentes langues.
