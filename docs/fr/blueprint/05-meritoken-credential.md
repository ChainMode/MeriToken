# 05 Relation entre credential et MeriToken

> Introduction : ce document poursuit la position établie dans [01-meritoken-overview.md](./01-meritoken-overview.md). Sous la sémantique de « composant contractuel », il traite spécifiquement la frontière et la correspondance entre MeriToken et `credential`. Les deux sont souvent confondus, mais dans la pratique de collaboration de la nouvelle société, l'absence de distinction affaiblit simultanément la stabilité de l'identité et de la propriété, et la cumulabilité de la contribution et de l'évaluation.

## Contexte

Plusieurs questions dans la nouvelle société — « qui suis-je », « ai-je le droit de faire cela », « qu'ai-je fait », « comment ai-je été évalué » — doivent être portées par des objets structurellement indépendants les uns des autres et néanmoins composables entre eux. Si l'on entasse chaque question sur une seule classe d'objet, deux dérives typiques apparaissent :

- **Surcharge de credential** : écrire « ce que j'ai fait et comment j'ai été évalué » — c'est-à-dire un contenu qui devrait relever de MeriToken — dans `credential` oblige à émettre et mettre à jour en continu les justificatifs d'identité et de propriété. L'émetteur est surchargé et le détenteur perd l'autorité sur ses propres enregistrements d'évaluation.
- **Dérive de l'évaluation** : écrire « qui je suis et ce que je détiens » dans MeriToken laisse les attributs identitaires écraser le conteneur des évaluations de contribution. Les enregistrements d'évaluation MeriToken qui devraient être appuyés par la co-signature multipartite dans la collaboration se trouvent dilués par le droit d'émettre des credential.

Ce blueprint répartit les deux classes d'objets entre deux supports distincts et rend l'attribution explicite : `credential` résout le côté « identité et propriété » ; MeriToken résout le côté « contribution et évaluation ». Les deux sont indépendants l'un de l'autre, et néanmoins se correspondent l'un à l'autre. La tâche de ce document est de rendre claire la frontière entre MeriToken et `credential`, afin que les documents 06–07 et les diverses déclinaisons linguistiques ne mélangent pas les deux lors du référencement.

Les détails de la couche protocolaire de `credential` sont portés par la documentation officielle du système ifay. Ce document ne fournit que l'explication minimale nécessaire à « la frontière avec MeriToken ».

## Contenu central

![gestion des credential](../../zh-CN/blueprint/illustration/credential-management.png)

Le schéma ci-dessus (réutilisé à titre transitoire) esquisse les actions de base de `credential` selon la chaîne émission, vérification et révocation. La discussion de ce document s'appuie sur cet ensemble d'actions et le place aux côtés de la sémantique « contribution-évaluation » de MeriToken.

### Le rôle de credential

`credential` résout la question « qui est le sujet, et quelle propriété détient-il sur quel objet », et constitue le support de credential — justificatif d'identité et de propriété — dans la nouvelle société :

- **Un bit vérifiable d'identité et de propriété** : `credential` est émis par un sujet doté d'autorité d'émission, et enregistre les attributs d'identité du sujet émis (appartenance, rôle, qualification, etc.) ou sa propriété sur un objet spécifique (contrôle d'une ressource, d'un bit protocolaire, d'un rôle protocolaire). Il répond à « dans quel état de propriété ce sujet se trouve par rapport à un objet spécifique à un moment spécifique ».
- **Émis, vérifié et révoqué à la couche credential-and-token** : le cycle de vie de `credential` est contraint par les règles protocolaires de la couche credential-and-token. L'acte d'émission définit son périmètre de validité. L'acte de vérification permet à tout tiers de confirmer indépendamment l'existence et la propriété du credential. L'acte de révocation permet à l'émetteur de récupérer rapidement un credential lorsque la propriété change, empêchant ainsi que le credential continue à être cité après s'être détaché de la propriété réelle.
- **Centré sur la qualification d'entrée de « ce que l'on peut faire »** : dans la collaboration inter-sujets, `credential` est typiquement examiné comme une qualification d'entrée. Un sujet détenant le `credential` correspondant signifie qu'à la couche institutionnelle, il dispose de la qualification pour entrer dans une surface de collaboration particulière, citer un bit protocolaire particulier ou appeler une interface de ressource particulière. `credential` n'évalue pas directement comment le sujet s'est comporté dans le passé.
- **La stabilité prime** : la stabilité sémantique de `credential` est sa propriété fondamentale. Une appartenance de longue durée ou un droit de contrôle de longue durée sur une ressource ne fluctue pas fréquemment avec la performance de collaboration à court terme du détenteur. La part fluctuante doit être portée par MeriToken, et non répercutée dans `credential`.

Verrouiller le rôle de `credential` à « le credential d'identité et de propriété » maintient les chemins d'émission et de révocation simples et auditables, sans être perturbés par des enregistrements d'évaluation fréquents.

### Le rôle de MeriToken

MeriToken résout la question « qu'a fait le sujet et comment a-t-il été évalué », et constitue le support des enregistrements de contribution et d'évaluation dans la nouvelle société :

- **Un bit cumulable de contribution et d'évaluation** : MeriToken est généré par co-signature multipartite entre collaborateurs (voir les sections « Chiffrement » et « Récupération » de [02-meritoken-technical.md](./02-meritoken-technical.md)) et enregistre, dans une collaboration spécifique, « qui a contribué quoi, qui a été témoin de quoi et comment chacun a évalué l'autre ». Il répond à « dans quelles collaborations passées spécifiques ce sujet s'est comporté, et comment ».
- **Subordonné au système de niveau supérieur `GMC`** : contrairement à la chaîne émission-révocation de `credential`, la chaîne génération-référencement-révocation de MeriToken est tenue de manière unifiée sous le système de niveau supérieur `GMC`, la sémantique de chaîne garantissant la cohérence à l'échelle du réseau et l'immuabilité (voir la section « Comment MeriToken s'inscrit sous GMC » de [01-meritoken-overview.md](./01-meritoken-overview.md)).
- **Centré sur la trace processuelle de « ce qui a été fait et comment cela a été fait »** : MeriToken n'agit pas comme la vérification d'une qualification d'entrée ; il est généré en continu tout au long de la collaboration. Vers l'extérieur, il peut être cité, agrégé et comparé, mais chaque entrée correspond à un fait de collaboration concret et ne peut pas être créée ou supprimée à volonté.
- **Cumulable, révocable, avec divulgation par paliers** : MeriToken s'accumule au fil des collaborations à long terme en un portrait de développement multidimensionnel. Lorsque l'accord initial change, la partie référencée peut révoquer l'autorisation de divulgation correspondante. Chaque référence laisse une trace sous `GMC` (voir la section « Garanties de confidentialité » de [02-meritoken-technical.md](./02-meritoken-technical.md)).

Verrouiller le rôle de MeriToken à « l'enregistrement de contribution et d'évaluation » permet à l'évaluation à grain fin du processus de collaboration de s'accumuler dans le temps et de rester contrôlée de manière indépendante, sans être annexée par l'autorité d'émission de credential.

### La frontière et la correspondance

`credential` et MeriToken assument chacun un rôle non substituable dans la collaboration de la nouvelle société. Le tableau ci-dessous les place côte à côte selon cinq axes sémantiques :

| Axe sémantique | `credential` | MeriToken |
|--------|--------------|---------------------|
| Focalisation sémantique | Justificatif d'identité et de propriété ; répond à « qui est le sujet et ce qu'il détient sur quel objet » | Enregistrement de contribution et d'évaluation ; répond à « dans quelles collaborations le sujet a fait quoi et comment il a été évalué » |
| Cycle de vie | Émis, vérifié et révoqué à la couche credential-and-token ; met l'accent sur les transitions d'état de la qualification d'entrée | Comptabilisé sous le système de niveau supérieur `GMC` ; la chaîne génération-référencement-révocation laisse une trace sous la sémantique de chaîne |
| Forme de détention | Un objet d'état ancré bidirectionnellement entre émetteur et détenteur ; met l'accent sur la stabilité | Un objet de processus co-signé multipartite par les collaborateurs ; met l'accent sur la cumulabilité |
| Mode de référencement | Examiné à l'entrée de la collaboration pour vérifier « si la qualification est détenue » | Cité, agrégé et comparé pendant ou après la collaboration pour présenter « comment les choses ont été faites dans le passé » |
| Sémantique inter-sujets | Le même sujet détient différents `credential` sur différentes surfaces de collaboration, qui ne sont pas nécessairement comparables entre eux | Les MeriToken accumulés par le même sujet sur différents sujets peuvent être cités de manière croisée, mais le poids d'évaluation ne migre pas automatiquement |

La frontière tient à quatre niveaux qui se renforcent mutuellement, garantissant que les deux classes d'objets ne sont pas mélangées :

- **Non substituable** : `credential` ne peut pas être utilisé pour enregistrer « ce que j'ai fait et comment j'ai été évalué » ; sinon, on obtient une surcharge de credential et une charge déséquilibrée sur l'émetteur. MeriToken ne peut pas être utilisé pour enregistrer « qui je suis et ce que je détiens » ; sinon, on obtient une dérive de l'évaluation et une dilution de la propriété. Les deux portent chacun des tâches institutionnelles distinctes.
- **Mutuellement présupposants et étendants** : dans de nombreuses collaborations, `credential` fournit la qualification d'entrée, et MeriToken dépose la trace processuelle une fois que le sujet est à l'intérieur. Par exemple, dans une délibération inter-organisations, `credential` décide si un participant a la qualification pour s'exprimer, tandis que MeriToken enregistre la contribution et l'évaluation de chaque prise de parole, accumulant au fil du temps une influence sur le poids du discours dans les sujets ultérieurs (voir la section « Logique politique » de [03-meritoken-social.md](./03-meritoken-social.md)).
- **Cités ensemble, portés séparément** : dans le référencement par procuration et par agrégation des sujets `Fay` (voir la section « Modes de référencement et scénarios d'application des sujets Fay » de [04-meritoken-usage.md](./04-meritoken-usage.md)), un ensemble de `credential` et un ensemble d'entrées MeriToken sont typiquement présentés vers l'extérieur en même temps. Le premier prouve que le sujet `Fay` a une autorité de représentation ; l'ensemble MeriToken présente son histoire de collaboration. Les deux sont cités côte à côte, non fusionnés.
- **Chemins de révocation indépendants** : la révocation de `credential` est déclenchée par l'émetteur lorsque la propriété change ; la révocation de MeriToken est déclenchée par la partie référencée comme retrait de l'autorisation de divulgation. Ces deux chemins de révocation ne doivent pas se compenser mutuellement : l'émetteur ne peut pas utiliser la récupération de `credential` pour effacer une entrée MeriToken déjà témoignée ; la partie référencée ne peut pas, à partir d'un retrait de divulgation MeriToken, contraindre l'émetteur à récupérer le `credential`. L'indépendance des chemins de révocation suit le principe défini dans la section « La frontière et la correspondance » de ce document.

> ⏳ **Illustration en attente** (créneau : `meritoken-credential-boundary`)
> Description : un schéma comparatif présentant la frontière et la correspondance entre `credential` et MeriToken selon les deux axes sémantiques de « identité et propriété » et de « contribution et évaluation ». Pendant la période transitoire, `credential-management.png` peut être réutilisé à titre provisoire.
> Fichier prévu : `illustration/meritoken-credential-boundary.png`

## Relation avec d'autres sujets

| Sujet | Relation avec ce document |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Fournit les définitions des deux rôles fondamentaux sur lesquels atterrit ensuite ce document, et la subordination de MeriToken à `GMC`. |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Fournit la sémantique technique de MeriToken à la couche de la propriété et du droit d'usage, sur laquelle ce document place en correspondance la chaîne émission-révocation de `credential`. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Réutilise, dans la « logique politique » et la « structure économique », la frontière tracée ici, empêchant les sujets d'identité et de propriété d'écraser l'espace de la contribution et de l'évaluation. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Dans le référencement par procuration et par agrégation des sujets `Fay`, réutilise le principe « cités ensemble, portés séparément » énoncé ici. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Met concrètement en pratique la partition de frontière énoncée ici dans la collaboration inter-sujets à haute densité et les scénarios à reconduction. |
| [07-related-projects.md](./07-related-projects.md) | Fournit les liens externes officiels pour `credential`, `GMC`, ifay, `Fay` et autres sujets en amont. |

## Notes terminologiques

`Reserved_Term` apparaissant dans ce document :

- **credential** : un credential, c'est-à-dire un justificatif d'identité et de propriété pour un sujet personnel ou `Fay` ; voir [glossary.md](./glossary.md).
- **GMC** : Global Merit Chain, le système de niveau supérieur auquel appartient MeriToken ; voir [glossary.md](./glossary.md).
- **Fay** : un sujet non personnel qui référence MeriToken ; voir [glossary.md](./glossary.md).
- **ifay** : nom du système du projet ; voir [glossary.md](./glossary.md).

La forme principale chinoise de MeriToken n'est utilisée comme désignation conventionnelle de MeriToken que dans le corps de texte des blueprints `zh-CN` et `zh-TW`. Voir la section `Localized_Term` de [glossary.md](./glossary.md) pour les règles de localisation de MeriToken dans les différentes langues.
