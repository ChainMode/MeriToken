# Glossaire (fr)

Ce glossaire est le dictionnaire faisant autorité unique pour la documentation multilingue du blueprint iFay. Les entrées listées dans le tableau `Reserved_Term` conservent leur forme anglaise originale dans toutes les versions linguistiques et ne sont pas traduites. Les entrées du tableau `Localized_Term` adaptent leur forme principale en fonction de la langue cible. Les entrées qui ne sont ni des `Reserved_Term` ni des `Localized_Term` sont localisées par chaque langue selon les usages locaux.

## Reserved_Term (forme anglaise originale conservée dans toutes les langues)

| Original anglais | Définition | Politique de traduction | Lien de référence (Upstream_Project_Doc_Link) |
|----------|----------|----------|-----------------------------------|
| iFay / ifay | Nom de l'écosystème du projet iFay ; dans le contexte des avatars, `iFay` (Individual Fay) désigne un avatar numérique personnel ancré 1:N à un unique `Human Prime` | Réservé : conserver la forme anglaise originale dans toutes les langues | https://ifay.ai |
| agent | Entité agent (dans les frameworks LLM traditionnels, une entité programmatique qui exécute des tâches de manière autonome) | Réservé : conserver la forme anglaise originale dans toutes les langues | https://ifay.ai |
| phase | Étape (un numéro d'étape évolutive dans le blueprint) | Réservé : conserver la forme anglaise originale dans toutes les langues, le numéro étant placé directement à la suite (par exemple, `phase 1`) | — |
| credential | Credential (justificatif d'identité et de propriété pour un `Human Prime` ou un sujet `Fay`) | Réservé : conserver la forme anglaise originale dans toutes les langues | ./05-meritoken-credential.md |
| GMChain | Global Merit Chain, le système supérieur non monétaire de mesure de la contribution sociale et de gouvernance auquel appartient MeriToken | Réservé : conserver l'abréviation canonique `GMChain` dans toutes les langues | ./01-meritoken-overview.md |
| Fay | Terme général désignant les avatars numériques autonomes au sein du système iFay (`Fay = iFay + coFay`), où `iFay` est l'avatar personnel ancré à un unique `Human Prime` et `coFay` est l'avatar collaboratif non personnel de rôle public rattaché en une seule couche à une personne physique responsable ou à une organisation | Réservé : conserver la forme anglaise originale dans toutes les langues | ./04-meritoken-usage.md |
| Human Prime | Personne physique représentée et portant la responsabilité finale au sein du système iFay | Réservé : conserver `Human Prime` | https://ifay.ai |
| Host | Appareil matériel terminal, application cliente ou environnement d'exécution dans lequel un `Fay` s'exécute ou exerce un contrôle autorisé (ne désigne jamais une personne physique) | Réservé : conserver `Host` | https://ifay.ai |

## Localized_Term (la forme principale change selon la langue cible)

| Original anglais | 中文主用名 | Règle de traitement |
|----------|------------|----------|
| MeriToken | 美誉值 | Le corps de texte de `zh-CN` et `zh-TW` utilise « 美誉值 » (`zh-TW` : « 美譽值 ») comme forme principale et autorise l'annotation entre parenthèses de la forme anglaise originale `MeriToken` à la première occurrence dans cette version linguistique. Le corps de texte de `en`, `de`, `es`, `fr`, `ja`, `ko`, `ru` utilise la forme anglaise originale `MeriToken` et ne doit pas y substituer une traduction localisée. |

## Note sur MeriToken_Chinese_Name

« 美誉值 » est le nom chinois principal de MeriToken et n'est utilisé comme désignation conventionnelle de ce concept que dans le corps de texte des blueprints `zh-CN` et `zh-TW`. MeriToken est une mesure strictement non monétaire de contribution sociale — ni convertible en monnaie, ni spéculative, ni transférable. La chaîne « 美誉值 » n'apparaît dans aucune autre version linguistique (y compris `en`).

## Entrées non Reserved

| Terme source | Suggestion en français | Notes |
|------|----------|------|
| 蓝图 | blueprint | Traduit selon les usages locaux dans chaque langue. |
| 校对 | relecture | — |
| 凭证管理 | gestion des credential | Lorsque « credential » est conservé dans sa forme originale, l'expression entière est rendue par « gestion des credential ». |
