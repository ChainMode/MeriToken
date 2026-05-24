# 02 Principes techniques de MeriToken

> Introduction : en s'appuyant sur la position établie dans [01-meritoken-overview.md](./01-meritoken-overview.md), ce document déploie les invariants techniques que MeriToken doit satisfaire sous les deux rôles « composant contractuel » et « connecteur des relations sociales », selon cinq fils — chiffrement, stockage, récupération, garanties de confidentialité, et garanties de propriété et de droit d'usage. Ce document ne reformule pas la conception globale de `GMC` ; lorsque le comportement de niveau supérieur entre en jeu, il renvoie aux liens externes de [07-related-projects.md](./07-related-projects.md).

## Contexte

Une fois que MeriToken assume le rôle de composant contractuel et de connecteur des relations sociales, référencé de manière répétée dans la nouvelle société, ses principes techniques ne peuvent plus se limiter à « écrire une seule entrée de registre ». Chaque génération, transfert et référencement d'un MeriToken est examiné selon deux dimensions non négociables : d'abord, la vérifiabilité — toute entrée référencée doit être vérifiable indépendamment par n'importe quel tiers ; ensuite, les garanties de confidentialité — le contenu d'une entrée référencée n'a pas besoin d'être entièrement divulgué aux parties non concernées lors de l'acte de référencement.

Ce document prend ces deux contraintes non négociables comme point de départ et développe la discussion selon les cinq fils du chiffrement, du stockage, de la récupération, des garanties de confidentialité, et des garanties de propriété et de droit d'usage. Chaque fil correspond à un ensemble de principes techniques concrets opérant sous les contraintes du système de niveau supérieur `GMC`, mais ce document ne déploie pas les détails de la couche protocolaire de `GMC` lui-même.

## Contenu central

### Chiffrement

Tout au long du cycle de vie de la génération et du transfert, MeriToken utilise le même système de clés asymétriques que `GMC` pour émettre et contre-signer les entrées :

- **Co-signature multipartite** : une entrée MeriToken porte au moins deux classes de signatures — « contributeur et témoin ». Des signatures supplémentaires peuvent être ajoutées lorsque l'évaluation ou l'arbitrage par un tiers entre en jeu. La co-signature multipartite est le support technique minimal de la sémantique de « composant contractuel » ; l'absence d'une signature signifie l'absence d'une preuve d'exécution.
- **Engagement de contenu** : le contenu substantiel d'une entrée (description de la contribution, contexte, empreintes des livrables, etc.) est consigné en chaîne sous forme d'engagement ; le contenu original lui-même n'a pas besoin de figurer en chaîne. Cela préserve à la fois la vérifiabilité et évite d'exposer au réseau `GMC` entier des détails de contenu non pertinents.
- **Auditable mais dissimulable** : dans les scénarios d'audit, le contenu derrière un engagement peut être divulgué de manière sélective, et l'acte de divulgation laisse lui-même une trace. Sans divulgation, les tiers peuvent encore vérifier l'existence et la propriété de l'entrée, mais ne peuvent pas lire les détails de son contenu.

L'objectif de la conception du chiffrement n'est pas de transformer MeriToken en une archive de contenu « anti-fuite ». Il s'agit de garantir que, sous la sémantique de « composant contractuel », chaque promesse et acte d'exécution porte un appui cryptographique indépendant et que chaque acte de référencement n'exige pas que le contenu original soit à nouveau exposé.

### Stockage

La question clé à la couche de stockage n'est pas « où stocker » mais « à quelle granularité organiser et qui doit persister » :

- **Engagements en chaîne, contenu hors chaîne** : les engagements cryptographiques et les signatures des entrées MeriToken sont persistés sur la chaîne `GMC` ; le contenu original (tel que les livrables d'une contribution, le texte d'une évaluation) est conservé hors chaîne par le sujet selon sa politique locale. Les engagements en chaîne garantissent la cohérence des entrées sur l'ensemble du réseau, et le contenu hors chaîne préserve l'autorité du sujet sur ses propres données.
- **Agrégation par sujet** : le stockage hors chaîne est agrégé à la granularité des sujets personnels ou des sujets `Fay`. Chaque sujet décide de son propre support de stockage, de sa politique de sauvegarde et de sa fenêtre d'accessibilité, sans dépendre d'un fournisseur de service centralisé.
- **Redondance et récupérabilité** : un sujet peut choisir de confier une copie chiffrée de son contenu hors chaîne à un homologue de confiance (également enregistré sous forme d'entrée MeriToken), de sorte qu'une récupération soit possible si la copie locale est perdue. L'acte de confiance lui-même est également inscrit dans `GMC`, ce qui empêche tout chemin clandestin de « récupération à partir de rien ».

Diviser le stockage en deux couches « engagement en chaîne / contenu hors chaîne » vise à équilibrer les objectifs de « vérifiabilité à l'échelle du réseau » et de « garde sous contrôle du sujet ». Sans l'un d'eux, MeriToken dégénérerait soit en une archive publique lisible par n'importe qui, soit en un système de points local ne pouvant pas être référencé entre sujets.

### Récupération

La récupération désigne le flux concret que tout sujet (personnel ou `Fay`) suit lorsqu'il référence un MeriToken :

- **Par référence plutôt que par copie** : la partie référencée ne remet pas une copie de l'entrée MeriToken au demandeur. Elle fournit plutôt une poignée de référence vérifiable de manière indépendante. Avec la poignée, le demandeur vérifie l'existence et la propriété de l'entrée auprès de `GMC`, et peut ensuite demander une divulgation supplémentaire à la partie référencée selon ses besoins.
- **Divulgation par paliers** : le demandeur peut requérir trois paliers de divulgation — « existence + propriété » (divulgation la plus faible), « résumé sémantique de l'entrée » (divulgation intermédiaire) et « détails du contenu original » (divulgation la plus élevée). Chaque palier est une action indépendante ; il n'existe pas de comportement par défaut « avoir reçu la poignée donne automatiquement accès au contenu ».
- **La récupération laisse une trace** : chaque action de récupération (y compris les récupérations à divulgation nulle qui ne vérifient que l'existence) laisse une trace sous les règles de niveau supérieur de `GMC`. La trace sert à la fois de preuve d'audit et de donnée d'arête dans le graphe ultérieur des relations sociales qui enregistre « qui a référencé qui ».

Diviser la récupération en trois étapes « référence → vérification → divulgation » permet à MeriToken de rester intensivement utilisable sous la sémantique de « connecteur des relations sociales » : dans la plupart des collaborations, seules les deux premières étapes sont nécessaires pour fournir la confiance ; ce n'est que lorsque les détails doivent réellement être examinés que la troisième étape entre en jeu.

### Garanties de confidentialité

Les garanties de confidentialité ne constituent pas une fonctionnalité unique mais la sémantique de confidentialité extraite de chacune des couches du chiffrement, du stockage et de la récupération :

- **Divulgation minimale par défaut** : la valeur par défaut de toute relation de référencement est le palier de divulgation le plus faible ; toute récupération au-dessus du minimum exige le consentement actif de la partie référencée, et ce consentement est lui-même enregistré sous forme d'entrée MeriToken.
- **Les relations ne peuvent pas être reconstruites par des spectateurs** : un tiers ne peut pas reconstruire à partir des seuls engagements en chaîne dans `GMC` le graphe social complet de « qui a référencé qui et ce qui a été référencé ». La visibilité de chaque acte de référencement est restreinte au demandeur et à la partie référencée, et peut éventuellement être étendue à des tiers spécifiques.
- **Révocation et invalidation** : selon l'accord initial, la partie référencée peut révoquer l'autorisation de divulgation, après quoi l'entrée à palier de divulgation élevé devient invalide pour le demandeur à partir de ce moment. Les actions de référencement déjà survenues restent vérifiables de manière indépendante, mais le contenu précédemment divulgué n'est plus autorisé à être référencé à nouveau.

L'objectif de la garantie de confidentialité n'est pas que « les données n'apparaissent jamais en chaîne » — cela contredirait la vérifiabilité. C'est que « seuls les engagements vivent en chaîne, et le contenu n'est divulgué que lorsqu'il est autorisé ». C'est un corollaire nécessaire de la sémantique de « composant contractuel » sur la dimension de la confidentialité.

### Garanties de propriété et de droit d'usage

La propriété et les droits d'usage sont deux questions qui doivent être discutées séparément :

- **La propriété est définie par la relation de signature** : la propriété d'une entrée MeriToken est définie conjointement par les premières signatures « contributeur et témoin » de cette entrée, et est ancrée de manière immuable dans `GMC`. La propriété n'est pas diluée par des référencements répétés, et ne dérive pas vers des sujets non signataires par le biais d'accords de transfert.
- **Les droits d'usage sont accordés par la partie référencée** : distinct de la propriété, le « droit d'usage » décrit « qui, dans quels scénarios, peut référencer ce MeriToken et l'incorporer dans sa chaîne d'argumentation ». Les droits d'usage sont accordés par la partie référencée scénario par scénario, formant une matrice d'autorisation « scénario × utilisateur » indépendante des changements de propriété.
- **Priorité en cas de conflit** : lorsque la propriété et les droits d'usage entrent en conflit (par exemple, le titulaire du droit d'usage souhaite divulguer le contenu original alors que le propriétaire refuse), le droit de révocation du propriétaire est prioritaire. Cette priorité est la conséquence directe, sous la sémantique de « composant contractuel », du principe « la promesse précède la citation ».

Diviser la propriété et les droits d'usage en deux couches évite l'ambiguïté du « avoir référencé votre MeriToken signifie que je le possède désormais ». La propriété est un bit institutionnel ; le droit d'usage est un bit relationnel. La distinction entre eux est invoquée à plusieurs reprises dans les collaborations de la nouvelle société.

> ⏳ **Illustration en attente** (créneau : `meritoken-technical-flow`)
> Description : un schéma de flux montrant la boucle fermée chiffrement / stockage / récupération de MeriToken : co-signature multipartite contributeur et témoin → engagement en chaîne dans `GMC` → contenu hors chaîne conservé localement par le sujet → récupération par le demandeur via une poignée → divulgation par paliers → réécriture de la trace de récupération dans `GMC`.
> Fichier prévu : `illustration/meritoken-technical-flow.png`

## Relation avec d'autres sujets

| Sujet | Relation avec ce document |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Fournit les définitions des deux rôles que ce document technicise ensuite. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Étend la « récupération / garantie de confidentialité / droit d'usage » de ce document à la signification sur les couches des relations sociales, de la logique politique et de la structure économique. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Concrétise le flux de « récupération » de ce document en scénarios d'application pour les deux classes d'entités effectuant des références — sujets personnels et sujets `Fay`. |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Place les « propriété et droits d'usage » de ce document aux côtés du credential — justificatif d'identité et de propriété — porté par `credential`, et donne la correspondance. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Réutilise les flux de récupération et de divulgation définis dans ce document dans des scénarios d'utilisation à haute densité et à reconduction. |
| [07-related-projects.md](./07-related-projects.md) | Fournit les liens externes officiels pour les sujets en amont tels que la couche protocolaire globale de `GMC` et l'environnement opérationnel du système ifay. |

## Notes terminologiques

`Reserved_Term` apparaissant dans ce document :

- **GMC** : Global Merit Chain, le système de niveau supérieur auquel appartient MeriToken ; voir [glossary.md](./glossary.md).
- **Fay** : un sujet non personnel qui référence MeriToken ; voir [glossary.md](./glossary.md).
- **credential** : un credential, c'est-à-dire un justificatif d'identité et de propriété pour un sujet personnel ou `Fay` ; voir [glossary.md](./glossary.md).
- **ifay** : nom du système du projet ; voir [glossary.md](./glossary.md).

La forme principale chinoise de MeriToken n'est utilisée comme désignation conventionnelle de MeriToken que dans le corps de texte des blueprints `zh-CN` et `zh-TW`. Voir la section `Localized_Term` de [glossary.md](./glossary.md) pour les règles de localisation de MeriToken dans les différentes langues.
