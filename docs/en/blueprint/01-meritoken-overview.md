# 01 MeriToken Overview

> Introduction: This document is the starting point of the main line of the blueprint. It locates MeriToken within the ifay system, and gives the two reasons MeriToken is extracted from the overall ifay discussion as a standalone subject — as the contract component and as the social-relationship connector of the new society. Documents 02 through 06 all build on the position established here.

## Background

The "MeriToken" discussed in this blueprint is not yet another general-purpose loyalty point or contribution-accounting tool. It is a piece of foundational infrastructure within the operating environment of the "new society" envisioned by ifay. MeriToken takes on foundational roles in two distinct directions at the same time: at the institutional layer, it participates in promises and their fulfillment between individuals and organizations in the form of a "contract component"; at the relational layer, it weaves together scattered personal contributions, collaboration records and social evaluations in the form of a "social-relationship connector".

These two directions are not two parallel business lines. They are projections of the same asset onto different layers of abstraction. This blueprint elevates MeriToken to a main-line topic precisely because there is non-negligible tension between the two projections: when institutional rigor goes up, it must not in turn devour the elasticity of the relational layer; when the richness of the relational layer grows, it must not destabilize the verifiability of the contract layer. Only after we have clearly stated MeriToken's position and the reasons for treating it as a standalone subject can documents 02 through 06 share a common starting point.

## Core content

### How MeriToken belongs to GMC

MeriToken is not a standalone asset protocol. It is one class of concrete accounting object under `GMC` (Global Merit Chain), an upper-level system. `GMC` provides global chain-based bookkeeping, cross-subject verifiability and eventual consistency. MeriToken sits on top of that and carries the concrete semantics of "contribution — evaluation — referencing".

This subordination yields three direct consequences:

- **Consistency of the data substrate**: ownership transfers, referencing records, revocations and updates of MeriToken all follow the chain semantics of `GMC`. There is no separate ledger, which avoids the cost of cross-ledger reconciliation.
- **Externality of the lifecycle**: MeriToken does not necessarily span the entire lifecycle of a personal subject. Its visibility, referenceability and accumulability inside `GMC` may be opened or recovered in stages according to upper-level rules, without modifying the definition of MeriToken itself.
- **Externalization of interpretive authority**: the concrete meaning of MeriToken in the new society evolves as the upper-level system evolves. This blueprint chooses to leave more upstream topics such as the "overall framework / `phase` evolution" to the official documentation on ifay.ai (see [07-related-projects.md](./07-related-projects.md)) rather than restating them in this repository.

The reason for stating MeriToken's relationship with `GMC` so explicitly is to prevent readers from understanding MeriToken as an isolated conceptual invention. It is the landing point of the upper-level system at the level of "concrete accounting object", and it is also the shared starting point for every subsequent technical and social discussion.

### The two reasons for treating MeriToken as a standalone subject

Although MeriToken is data-wise subordinate to `GMC`, this repository chooses to extract it from the overall discussion of ifay as a standalone blueprint because MeriToken simultaneously bears two classes of foundational roles in the new society, each of which is substantial enough to warrant its own line of inquiry. Folding both roles into the overall `GMC` discussion would blur their respective boundaries; treating them separately allows us to characterize the dual meaning of MeriToken in the new society more accurately.

#### As the contract component of the new society

The first reason comes from the institutional layer. In the new society MeriToken can be referenced as a verifiable record of "what I have done, to whom I am accountable, and who has witnessed it", and therefore naturally bears the role of a "contract component":

- **A verifiable bit for promise and fulfillment**: in cross-subject collaboration, the very process by which a MeriToken is generated — a contribution being witnessed, evaluated and entered into the books — is a minimal unit. It serves as a verifiable bit for promise and fulfillment, rather than relying on an after-the-fact subjective adjudication by a third party.
- **Replacing coarse-grained credit with fine-grained records**: the "supply of trust" that traditional society carries through coarse-grained objects such as credit scores, reputation and personal connections can in the new society be decomposed into a series of fine-grained, traceable, verifiable MeriToken entries. Institutional logic thereby migrates from "overall reputation" to "specific records".
- **Boundary with `credential`**: MeriToken is a verifiable record of "what one has done", not an identity-and-ownership credential of "who I am, what I hold". The latter is the responsibility of `credential`. The boundary and correspondence between the two are unfolded separately in [05-meritoken-credential.md](./05-meritoken-credential.md) and are not repeated here.

The key implication of viewing MeriToken as a contract component is this: institutional rules no longer depend on a centralized credit-scoring machine. The three things — "contract formation, fulfillment, traceable default" — are each grounded in concrete MeriToken records. A contract is no longer a textual promise; it becomes a structured, referenceable, auditable object.

#### As the social-relationship connector of the new society

The second reason comes from the relational layer. The same MeriToken entry, in addition to bearing the role of a contract component, is also a node of social relationships that connects scattered subjects to one another:

- **Minimal edges of the relationship graph**: every MeriToken record contains the multi-party relationship of "contributor — evaluator — service recipient". These ternary relationships naturally constitute the relationship graph of the new society. The graph as a whole need not be maintained by any central node; it is assembled from the local relationships embedded in each MeriToken entry.
- **Connecting across subject types**: the connector is indifferent to subject form. Personal subjects between themselves, personal subjects with `Fay` subjects, and `Fay` subjects between themselves can all form stable collaboration chains via referencing relationships of MeriToken. The details of how `Fay` subjects reference MeriToken are elaborated in [04-meritoken-usage.md](./04-meritoken-usage.md).
- **A migration path from stranger to acquaintance**: MeriToken is not only a record of "relationships that have already formed"; it is also an entry point for "relationships that have not yet formed". Strangers can establish an initial level of trust by referencing each other's existing MeriToken entries, and then deposit the result of the present collaboration into newly generated MeriToken entries. Social relationships in the new society thereby gain a structured path from stranger to acquaintance.

The key implication of viewing MeriToken as a social-relationship connector is this: social relationships no longer depend on platform algorithmic recommendations and black-box ratings. They return to a localized generation mechanism rooted in "concrete collaboration, concrete witnessing, and concrete referencing".

> ⏳ **Pending illustration** (slot: `meritoken-overview-contract`)
> Description: A conceptual diagram that simultaneously presents MeriToken bearing the two foundational roles of "contract component" and "social-relationship connector" in the new society, and indicates that it is subordinate to the `GMC` upper-level system.
> Planned file: `illustration/meritoken-overview-contract.png`

## Relationship with other topics

This document is the starting point of the main line 01–06. Its connection to subsequent topics is summarized below:

| Subsequent topic | Connection to this document |
|----------|-------------|
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Lands the two roles "contract component" and "social-relationship connector" onto the technical principles of encryption, storage, retrieval, privacy, ownership and usage rights. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Continues to unfold the two roles into four threads of social meaning: social relationships, political logic, economic structure and personal-growth mapping. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Concretizes the two roles into the referencing methods and application scenarios of the two classes of referrers — "personal subjects" and "`Fay` subjects". |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Defines, under the "contract component" semantics, the boundary and correspondence between MeriToken and `credential`. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Develops advanced studies of the two roles in high-density scenarios such as cross-subject collaboration and rolling scenarios. |
| [07-related-projects.md](./07-related-projects.md) | Provides the minimal positional notes and the official-documentation external links for upstream and peripheral topics such as `GMC`, ifay, `Fay`, `agent`, `phase` and the overall framework. |

If you have not yet read [00-readers-guide.md](./00-readers-guide.md), we recommend going back there first to establish the overall view, and then returning here to continue the main line.

## Term footnotes

`Reserved_Term`s appearing in this document:

- **GMC**: Global Merit Chain, the upper-level system to which MeriToken belongs; see [glossary.md](./glossary.md).
- **Fay**: A non-personal subject that references MeriToken; see [glossary.md](./glossary.md).
- **credential**: An identity and ownership credential for a personal or `Fay` subject; see [glossary.md](./glossary.md).
- **ifay**: Name of the project system; see [glossary.md](./glossary.md).
- **agent**: An agent entity in traditional LLM frameworks; see [glossary.md](./glossary.md).
- **phase**: An evolutionary stage number in the blueprint; see [glossary.md](./glossary.md).

The Chinese primary form of MeriToken is used as the conventional designation of MeriToken only in the body text of the `zh-CN` and `zh-TW` blueprints. See the `Localized_Term` section of [glossary.md](./glossary.md) for the localization rules of MeriToken across languages.
