# 00 Reader's Guide

> This document is the entry point of the blueprint. It explains the writing axis of this repository's blueprint, sketches the reader profile and recommended reading paths, and routes the reader toward the main-line documents (01–06).

![ifay title banner](../../zh-CN/blueprint/illustration/ifay-title-banner.png)

## Background

The blueprint of this repository is organized around an in-depth analysis of **MeriToken**. In the new society, MeriToken bears two foundational roles — "contract component" and "social-relationship connector" — and is therefore the content axis of every document in this blueprint.

Topics such as the ifay system, GMC, Fay, agent, and phase are positioned as supporting background that an analysis of MeriToken cannot avoid. They are introduced only when the unfolding of MeriToken makes them strictly necessary, and the reader is then routed via external links to the corresponding official documentation pages on ifay.ai. This repository does not elaborate on those upstream or peripheral topics at length.

The intended readers of this blueprint are:

- Researchers, writers and collaborators who wish to understand the technical principles, social meaning and application scenarios of MeriToken in a systematic way;
- Practitioners who already have some exposure to the foundational concepts of the ifay system and now wish to look more closely at the concrete role of MeriToken in the new society, especially how MeriToken interacts with surrounding institutions;
- Translators and maintainers who need to write or translate this MeriToken blueprint for additional language versions.

## Core content

### Blueprint axis: MeriToken

The main body of the blueprint (01–06) unfolds the in-depth analysis of MeriToken in the following order:

- **Overview (01)**: how MeriToken belongs to GMC; the two reasons it is treated as a standalone topic — as the contract component of the new society and as the social-relationship connector of the new society.
- **Technical principles (02)**: encryption, storage, retrieval, privacy guarantees, ownership and usage-right guarantees.
- **Social meaning (03)**: social relationships, political logic, economic structure, personal-growth mapping, and the meaning of MeriToken as a vehicle for the mapping between "personal contribution and social discourse weight".
- **Referencing and applications (04)**: the referencing methods and typical application scenarios of the two classes of referrers — personal subjects and Fay subjects.
- **Relationship with credential (05)**: the role definitions, boundary, and correspondence between credential and MeriToken.
- **Advanced topics (06)**: extension cases such as high-density use across multiple subjects and rolling scenarios.

### Recommended reading paths

The recommended reading order is sequential by number: `01 → 02 → 03 → 04 → 05 → 06`. If time is limited or the goal is more specific, the following branch paths may be helpful:

- **For readers focused on technical implementation**: `01 → 02 → 05 → 06` — first establish the basic position of MeriToken, then dig into the encryption/storage/retrieval closed loop and the credential boundary.
- **For readers focused on social and institutional meaning**: `01 → 03 → 04 → 06` — first understand the overall position of MeriToken, then unfold the social meaning, referencing and applications.
- **For readers who need to explain MeriToken to others**: `01 → 04 → 03` — first make clear "what it is and who uses it", then fill in "why it is designed this way".

`07-related-projects.md` is the interface document between this blueprint and upstream topics. It is a supplementary reference to be consulted on demand and is not on the main-line reading path.

### Relationship with upstream and peripheral topics

Upstream and peripheral topics such as ifay, GMC, Fay, agent, and phase are consolidated by [07-related-projects.md](./07-related-projects.md) into the form of "minimal necessary positional notes + a list of external links", which routes the reader to the corresponding official documentation pages on ifay.ai. The blueprint itself does not elaborate at length on those topics, in order to preserve the writing density of the MeriToken axis.

If you have not encountered these upstream concepts before, we recommend visiting the external links in [07-related-projects.md](./07-related-projects.md) first to build a quick background, and then returning to the main line at 01.

## Relationship with other topics

| No. | Topic | Relationship to this guide |
|------|------|---------------|
| 01 | MeriToken overview | The main-line starting point and the next document after this guide |
| 02 | MeriToken technical principles | Second document on the main line |
| 03 | MeriToken social meaning | Third document on the main line |
| 04 | MeriToken referencing and applications | Fourth document on the main line |
| 05 | The relationship between credential and MeriToken | Fifth document on the main line |
| 06 | MeriToken advanced topics | Sixth document on the main line |
| 07 | Relationship with the ifay system | Interface and external-link list for upstream and peripheral topics |

## Term footnotes

`Reserved_Term`s appearing in this document:

- **ifay**: Name of the project system; see [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, the upper-level system to which MeriToken belongs; see [glossary.md](./glossary.md).
- **Fay**: A non-personal subject that references MeriToken; see [glossary.md](./glossary.md).
- **agent**: An agent entity in traditional LLM frameworks; see [glossary.md](./glossary.md).
- **phase**: An evolutionary stage number in the blueprint; see [glossary.md](./glossary.md).
- **credential**: An identity and ownership credential for a personal or Fay subject; see [glossary.md](./glossary.md).

The Chinese primary form of MeriToken is used as the conventional designation of MeriToken only in the body text of the `zh-CN` and `zh-TW` blueprints. See the `Localized_Term` section of [glossary.md](./glossary.md) for the localization rules of MeriToken across languages.
