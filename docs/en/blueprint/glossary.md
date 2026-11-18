# Glossary (en)

This glossary is the single authoritative dictionary for the multilingual documentation of the iFay blueprint. Entries listed in the `Reserved_Term` table retain their original English form across all language versions and are not translated. Entries in the `Localized_Term` table switch their primary form according to the target language. Entries that are neither `Reserved_Term` nor `Localized_Term` are localized by each language according to local convention.

## Reserved_Term (original English form retained in all languages)

| Original English | Definition | Translation policy | Reference link (Upstream_Project_Doc_Link) |
|----------|----------|----------|-----------------------------------|
| iFay / ifay | Name of the iFay project ecosystem; in avatar context, `iFay` (Individual Fay) denotes a personal digital avatar anchored 1:N to a single `Human Prime` | Reserved: keep the original English form across all languages | https://ifay.ai |
| agent | Agent entity (in traditional LLM frameworks, a program entity that autonomously executes tasks) | Reserved: keep the original English form across all languages | https://ifay.ai |
| phase | Stage (an evolutionary stage number in the blueprint) | Reserved: keep the original English form across all languages, with the number directly following (for example, `phase 1`) | — |
| credential | Credential (an identity and ownership credential for a `Human Prime` or `Fay` subject) | Reserved: keep the original English form across all languages | ./05-meritoken-credential.md |
| GMChain | Global Merit Chain, the non-monetary social contribution and governance system to which MeriToken belongs | Reserved: keep the canonical abbreviation `GMChain` across all languages | ./01-meritoken-overview.md |
| Fay | General term for autonomous digital avatars in the iFay system (`Fay = iFay + coFay`), where `iFay` is the personal avatar anchored to a single `Human Prime` and `coFay` is the non-personal public-role collaborative avatar anchored in a single layer to an accountable natural person or organization | Reserved: keep the original English form across all languages | ./04-meritoken-usage.md |
| Human Prime | The natural person mapped, represented, and holding ultimate accountability in the iFay system | Reserved: keep `Human Prime` in English (`人类原型` in Chinese) | https://ifay.ai |
| Host | Terminal hardware device, client application, or runtime execution environment where a `Fay` executes or exercises authorized control (never refers to a natural person) | Reserved: keep `Host` in English (`宿主` in Chinese) | https://ifay.ai |

## Localized_Term (primary form switches by target language)

| Original English | 中文主用名 | Handling rule |
|----------|------------|----------|
| MeriToken | 美誉值 | The body text of `zh-CN` and `zh-TW` uses "美誉值" (`zh-TW`: "美譽值") as the primary form, and is allowed to annotate the original English form `MeriToken` in parentheses at the first occurrence in that language version. The body text of `en`, `de`, `es`, `fr`, `ja`, `ko`, `ru` uses the original English form `MeriToken` and must not substitute a localized translation. |

## Note on MeriToken_Chinese_Name

"美誉值" is the primary Chinese name for MeriToken, and is used as the conventional designation for this concept only in the body text of the `zh-CN` and `zh-TW` blueprints. MeriToken is a strictly non-monetary measure of social contribution—never cashable, speculative, or transferable. The string "美誉值" does not appear in any other language version (including `en`).

## Non-Reserved entries

| Source term | Suggested English | Notes |
|------|----------|------|
| 蓝图 | blueprint | Translated according to local convention in each language. |
| 校对 | review | — |
| 凭证管理 | credential management | When "credential" is kept in its original form, the phrase as a whole is rendered as "credential management". |
