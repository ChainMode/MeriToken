# 02 MeriToken Technical Principles

> Introduction: Building on the position established in [01-meritoken-overview.md](./01-meritoken-overview.md), this document unfolds the technical invariants that MeriToken must satisfy under the two roles "contract component" and "social-relationship connector", along five threads — encryption, storage, retrieval, privacy guarantees, and ownership and usage-right guarantees. This document does not restate the overall design of `GMC`; when upper-level behavior is involved, it cites the external links in [07-related-projects.md](./07-related-projects.md) instead.

## Background

Once MeriToken takes on the role of a repeatedly referenceable contract component and social-relationship connector in the new society, its technical principles can no longer stop at "writing a single ledger entry". Every generation, transfer and referencing of a MeriToken is examined along two non-negotiable dimensions: first, verifiability — any referenced entry must be independently verifiable by any third party; second, privacy guarantees — the content of a referenced entry need not be fully disclosed to non-related parties during the act of referencing.

This document takes these two non-negotiable constraints as the starting point and develops the discussion along the five threads of encryption, storage, retrieval, privacy guarantees, and ownership and usage-right guarantees. Each thread corresponds to a set of concrete technical principles operating under the constraints of the `GMC` upper-level system, but this document does not unfold the protocol-layer details of `GMC` itself.

## Core content

### Encryption

Throughout the lifecycle of generation and transfer, MeriToken uses the same asymmetric-key system as `GMC` to issue and counter-sign entries:

- **Multi-party co-signing**: a MeriToken entry carries at least two classes of signatures — "contributor and witness". Additional signatures can be appended when third-party evaluation or arbitration is involved. Multi-party co-signing is the minimal technical carrier of the "contract component" semantics; missing one signature means missing one piece of evidence of fulfillment.
- **Content commitment**: the substantive content of an entry (contribution description, context, fingerprints of deliverables, etc.) is recorded on chain in commitment form; the original content itself need not go on chain. This both preserves verifiability and avoids exposing irrelevant content details to the entire `GMC` network.
- **Auditable but concealable**: in audit scenarios, the content behind a commitment can be selectively disclosed, and the disclosure act itself leaves a trace. Without disclosure, third parties can still verify the existence and ownership of the entry, but cannot read the content details.

The goal of the encryption design is not to turn MeriToken into a "leak-proof" content archive. It is to ensure that, under the "contract component" semantics, every promise and act of fulfillment carries an independent cryptographic backing, and that every act of referencing does not require the original content to be exposed again.

### Storage

The key question at the storage layer is not "where to store" but "at what granularity to organize, and by whom to persist":

- **Commitments on chain, content off chain**: the cryptographic commitments and signatures of MeriToken entries are persisted on the `GMC` chain; the original content (such as deliverables of a contribution, evaluation text) is held off chain by the subject according to its local policy. On-chain commitments guarantee network-wide consistency of the entries, and off-chain content preserves the subject's authority over its own data.
- **Aggregation by subject**: off-chain storage is aggregated at the granularity of personal subjects or `Fay` subjects. Each subject decides its own storage medium, backup policy and accessibility window, without depending on any centralized service provider.
- **Redundancy and recoverability**: a subject may choose to entrust an encrypted copy of its off-chain content to a trusted counterpart (also recorded as a MeriToken entry), so that recovery is possible if the local copy is lost. The act of entrustment itself is also entered into `GMC`, which prevents any covert "recovery from nothing" path.

Splitting storage into the two layers of "on-chain commitment / off-chain content" is meant to balance the goals of "network-wide verifiability" and "subject-controlled custody". Without one of them, MeriToken would either degenerate into a public archive readable by anyone, or shrink into a local point system that cannot be referenced across subjects.

### Retrieval

Retrieval refers to the concrete flow that any subject (personal or `Fay`) follows when referencing a MeriToken:

- **By reference rather than by copy**: the referenced party does not hand a copy of the MeriToken entry to the referrer. Instead, it provides an independently verifiable reference handle. With the handle, the referrer verifies the existence and ownership of the entry against `GMC`, and can then request further disclosure from the referenced party as needed.
- **Tiered disclosure**: the requester may request three tiers of disclosure — "existence + ownership" (lowest disclosure), "semantic summary of the entry" (mid disclosure), and "details of the original content" (highest disclosure). Each tier is an independent action; there is no default behavior of "having received the handle automatically grants access to the content".
- **Retrieval leaves a trace**: every retrieval action (including zero-disclosure retrievals that only verify existence) leaves a trace under the upper-level rules of `GMC`. The trace serves both as audit evidence and as edge data in the subsequent social-relationship graph that records "who has referenced whom".

Splitting retrieval into the three steps of "reference → verify → disclose" allows MeriToken to remain heavily usable under the "social-relationship connector" semantics: in most collaborations, only the first two steps are needed to supply trust; only when details genuinely need to be examined does the third step come into play.

### Privacy guarantees

Privacy guarantees are not a single feature but the privacy semantics extracted from each of the layers of encryption, storage and retrieval:

- **Minimal-disclosure default**: the default of any referencing relationship is the lowest disclosure tier; any retrieval above the minimum requires the referenced party's active consent, and that consent is itself recorded as a MeriToken entry.
- **Relations cannot be reconstructed by bystanders**: a third party cannot reconstruct the full social graph of "who referenced whom and what was referenced" from the on-chain commitments in `GMC` alone. The visibility of each act of referencing is restricted to the referrer and the referenced party, and may optionally be extended to specific third parties.
- **Revocation and invalidation**: under the original agreement, the referenced party may revoke disclosure permission, after which the high-disclosure-tier entry becomes invalid for the referrer from that moment on. The referencing actions that have already occurred remain independently verifiable, but the previously disclosed content is no longer permitted to be referenced again.

The point of the privacy guarantee is not "data never appears on chain" — that would contradict verifiability. It is "only commitments live on chain, and content is disclosed only when authorized". This is a necessary corollary of the "contract component" semantics on the privacy dimension.

### Ownership and usage-right guarantees

Ownership and usage rights are two matters that need to be discussed separately:

- **Ownership is defined by the signing relationship**: ownership of a MeriToken entry is defined jointly by the earliest "contributor and witness" signatures on that entry, and is anchored immutably in `GMC`. Ownership is not diluted by repeated referencing, and does not drift to non-signing subjects through transfer agreements.
- **Usage rights are granted by the referenced party**: distinct from ownership, "usage right" describes "who, in which scenarios, may reference this MeriToken and incorporate it into their argumentation chain". Usage rights are granted by the referenced party on a per-scenario basis, forming an authorization matrix of "scenario × user" that is independent of changes in ownership.
- **Priority in conflicts**: when ownership and usage rights conflict (for example, the usage-right holder wishes to disclose the original content while the owner refuses), the owner's revocation right takes priority. This priority is the direct consequence, under the "contract component" semantics, of "the promise precedes the citation".

Splitting ownership and usage rights into two layers prevents the ambiguity of "having referenced your MeriToken means I now own it". Ownership is an institutional bit; usage right is a relational bit. The distinction between them is invoked repeatedly in the collaborations of the new society.

> ⏳ **Pending illustration** (slot: `meritoken-technical-flow`)
> Description: A flow diagram showing the encryption / storage / retrieval closed loop of MeriToken: contributor and witness multi-party co-signing → on-chain commitment in `GMC` → off-chain content held locally by the subject → retrieval by the referrer using a handle → tiered disclosure → write-back of the retrieval trace into `GMC`.
> Planned file: `illustration/meritoken-technical-flow.png`

## Relationship with other topics

| Topic | Relationship to this document |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Provides the definitions of the two roles that this document then technicalizes. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Extends this document's "retrieval / privacy guarantee / usage right" into the meaning at the social-relationship, political-logic and economic-structure layers. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Concretizes this document's "retrieval" flow into application scenarios for the two classes of referrers — personal subjects and `Fay` subjects. |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Places this document's "ownership and usage rights" alongside the identity-and-ownership credential carried by `credential`, and gives the correspondence. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Reuses the retrieval and disclosure flows defined in this document under high-density usage and rolling scenarios. |
| [07-related-projects.md](./07-related-projects.md) | Provides the official external links for upstream topics such as the overall protocol layer of `GMC` and the operating environment of the ifay system. |

## Term footnotes

`Reserved_Term`s appearing in this document:

- **GMC**: Global Merit Chain, the upper-level system to which MeriToken belongs; see [glossary.md](./glossary.md).
- **Fay**: A non-personal subject that references MeriToken; see [glossary.md](./glossary.md).
- **credential**: An identity and ownership credential for a personal or `Fay` subject; see [glossary.md](./glossary.md).
- **ifay**: Name of the project system; see [glossary.md](./glossary.md).

The Chinese primary form of MeriToken is used as the conventional designation of MeriToken only in the body text of the `zh-CN` and `zh-TW` blueprints. See the `Localized_Term` section of [glossary.md](./glossary.md) for the localization rules of MeriToken across languages.
