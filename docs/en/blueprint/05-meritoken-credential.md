# 05 The Relationship Between credential and MeriToken

> Introduction: This document continues from the position established in [01-meritoken-overview.md](./01-meritoken-overview.md). Under the "contract component" semantics, it specifically handles the boundary and correspondence between MeriToken and `credential`. The two are often confused, but in the collaboration practice of the new society, failure to distinguish them simultaneously weakens the stability of identity and ownership, and the accumulability of contribution and evaluation.

## Background

Several questions in the new society — "who am I", "may I do this", "what have I done", "how was I evaluated" — must be carried by objects that are structurally independent of one another and yet composable with one another. If we pile every question onto a single class of object, two typical skews appear:

- **Credential bloat**: writing "what I have done and how I have been evaluated" — that is, content that should belong to MeriToken — into `credential` forces identity-and-ownership credentials to be issued and updated continuously. The issuer is overburdened, and the holder loses authority over its own evaluation records.
- **Evaluation drift**: writing "who I am and what I hold" into MeriToken lets identity attributes squeeze the container of contribution evaluation. The MeriToken evaluation records that should be supported by multi-party co-signing in collaboration become diluted by the right to issue credentials.

This blueprint divides the two classes of objects between two different carriers, and makes the assignment explicit: `credential` solves the "identity and ownership" side; MeriToken solves the "contribution and evaluation" side. The two are independent of each other, yet correspond to each other. This document's task is to make the boundary between MeriToken and `credential` clear, so that documents 06–07 and the various language fan-outs do not mix the two when referencing.

The protocol-layer details of `credential` are carried by the official documentation of the ifay system. This document provides only the minimal explanation needed for "the boundary with MeriToken".

## Core content

![credential management](../../zh-CN/blueprint/illustration/credential-management.png)

The diagram above (provisionally reused) outlines the basic actions of `credential` along the issuance, verification and revocation chain. The discussion in this document builds on this set of actions and places it alongside the "contribution-evaluation" semantics of MeriToken.

### The role of credential

`credential` solves the question "who is the subject, and what ownership does it hold over what object", and is the credential carrier of identity and ownership in the new society:

- **A verifiable bit of identity and ownership**: `credential` is issued by a subject with issuance authority, and records the identity attributes of the issued subject (membership, role, qualification, etc.) or its ownership of a specific object (control over a resource, a protocol bit, a protocol role). It answers "what ownership state this subject is in with respect to a specific object at a specific point in time".
- **Issued, verified and revoked at the credential-and-token layer**: the lifecycle of `credential` is constrained by the protocol rules of the credential-and-token layer. The act of issuance defines its scope of validity. The act of verification allows any third party to independently confirm the existence and ownership of the credential. The act of revocation lets the issuer promptly recover a credential when ownership changes, preventing the credential from continuing to be cited after it has detached from the actual ownership.
- **Focused on the entry qualification of "what one may do"**: in cross-subject collaboration, `credential` is typically examined as an entry qualification. A subject holding the corresponding `credential` means that, at the institutional layer, it has the qualification to enter a particular collaboration surface, cite a particular protocol bit, or call a particular resource interface. `credential` does not directly evaluate how the subject has performed in the past.
- **Stability comes first**: the semantic stability of `credential` is its fundamental property. A long-lived membership or a long-lived control right over a resource does not fluctuate frequently with the holder's short-term collaboration performance. The fluctuating part should be borne by MeriToken, not reflected back into `credential`.

Locking the role of `credential` to "the credential of identity and ownership" keeps the issuance-and-revocation paths simple and auditable, undisturbed by frequent evaluation records.

### The role of MeriToken

MeriToken solves the question "what the subject has done and how it has been evaluated", and is the carrier of contribution-and-evaluation records in the new society:

- **An accumulable bit of contribution and evaluation**: MeriToken is generated by multi-party co-signing among collaborators (see the "Encryption" and "Retrieval" sections of [02-meritoken-technical.md](./02-meritoken-technical.md)) and records, in a specific collaboration, "who contributed what, who witnessed what, and how each evaluated whom". It answers "in which specific past collaborations this subject has performed, and how".
- **Subordinate to the `GMC` upper-level system**: unlike the issuance-and-revocation chain of `credential`, the generation-referencing-revocation chain of MeriToken is uniformly bookkept under the `GMC` upper-level system, with chain semantics guaranteeing network-wide consistency and immutability (see the "How MeriToken belongs to GMC" section of [01-meritoken-overview.md](./01-meritoken-overview.md)).
- **Focused on the process trace of "what was done and how it was done"**: MeriToken does not act as the verification of an entry qualification; it is generated continuously throughout collaboration. Externally it can be cited, aggregated and compared, but every entry corresponds to a concrete collaboration fact and cannot be created or removed at will.
- **Accumulable, revocable, with tiered disclosure**: MeriToken accumulates over long-term collaborations into a multidimensional growth portrait. When the original agreement changes, the referenced party may revoke the corresponding disclosure permission. Every reference leaves a trace under `GMC` (see the "Privacy guarantees" section of [02-meritoken-technical.md](./02-meritoken-technical.md)).

Locking the role of MeriToken to "the record of contribution and evaluation" lets the fine-grained evaluation of the collaboration process accumulate over time and remain independently controlled, without being annexed by the credential-issuance authority.

### The boundary and correspondence

`credential` and MeriToken each take on a non-substitutable role in collaboration in the new society. The table below places them side by side along five semantic axes:

| Semantic axis | `credential` | MeriToken |
|--------|--------------|---------------------|
| Semantic focus | Credential of identity and ownership; answers "who the subject is and what it holds over what object" | Record of contribution and evaluation; answers "in which collaborations the subject has done what and how it was evaluated" |
| Lifecycle | Issued, verified and revoked at the credential-and-token layer; emphasizes state transitions of the entry qualification | Bookkept under the `GMC` upper-level system; the generation-referencing-revocation chain leaves a trace under chain semantics |
| Holding form | A state object two-way-anchored between issuer and holder; emphasizes stability | A process object multi-party-co-signed by collaborators; emphasizes accumulability |
| Method of referencing | Examined at the entry of collaboration to verify "whether the qualification is held" | Cited, aggregated and compared during or after collaboration to present "how things have been done in the past" |
| Cross-subject semantics | The same subject holds different `credential`s on different collaboration surfaces, which are not necessarily comparable to each other | MeriToken accumulated by the same subject on different topics may be cross-cited, but evaluation weight does not migrate automatically |

The boundary holds at four levels that mutually reinforce each other, ensuring the two classes of objects are not mixed:

- **Non-substitutable**: `credential` cannot be used to record "what I have done and how I have been evaluated"; otherwise we get credential bloat and an unbalanced load on the issuer. MeriToken cannot be used to record "who I am and what I hold"; otherwise we get evaluation drift and dilution of ownership. The two each carry distinct institutional tasks.
- **Mutually presupposing and extending**: in many collaborations, `credential` provides the entry qualification, and MeriToken deposits the process trace once the subject is inside. For example, in a cross-organization deliberation, `credential` decides whether a participant has the qualification to speak, while MeriToken records the contribution and evaluation of every utterance, accumulating over time to influence speech weight on subsequent topics (see the "Political logic" section of [03-meritoken-social.md](./03-meritoken-social.md)).
- **Cited together, carried separately**: in the proxy-style and aggregation-style referencing of `Fay` subjects (see the "The referencing methods and application scenarios of Fay subjects" section of [04-meritoken-usage.md](./04-meritoken-usage.md)), a set of `credential`s and a set of MeriToken entries are typically presented externally at the same time. The former proves that the `Fay` subject has representational authority; the latter MeriToken set presents its history of collaboration. The two are cited side by side, not merged.
- **Independent revocation paths**: revocation of `credential` is triggered by the issuer when ownership changes; revocation of MeriToken is triggered by the referenced party as a withdrawal of disclosure permission. These two revocation paths must not compensate for each other: the issuer cannot use the recovery of `credential` to erase a MeriToken entry that has already been witnessed; the referenced party cannot work backward from a withdrawal of MeriToken disclosure to force the issuer to recover `credential`. The independence of the revocation paths follows the principle defined in the "Boundary and correspondence" section of this document.

> ⏳ **Pending illustration** (slot: `meritoken-credential-boundary`)
> Description: A comparison diagram presenting the boundary and correspondence between `credential` and MeriToken along the two semantic axes of "identity and ownership" and "contribution and evaluation". During the transitional period, `credential-management.png` may be provisionally reused.
> Planned file: `illustration/meritoken-credential-boundary.png`

## Relationship with other topics

| Topic | Relationship to this document |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Provides the definitions of the two foundational roles that this document then lands on, and the subordination of MeriToken to `GMC`. |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Provides the technical semantics of MeriToken at the ownership and usage-right layer, on which this document places the issuance-and-revocation chain of `credential` in correspondence. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Reuses, in "political logic" and "economic structure", the boundary drawn here, preventing identity-and-ownership topics from squeezing the space of contribution and evaluation. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | In the proxy-style and aggregation-style referencing of `Fay` subjects, reuses the principle of "cited together, carried separately" stated here. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Concretely exercises the boundary partition stated here in cross-subject high-density collaboration and rolling scenarios. |
| [07-related-projects.md](./07-related-projects.md) | Provides the official external links for `credential`, `GMC`, ifay, `Fay` and other upstream topics. |

## Term footnotes

`Reserved_Term`s appearing in this document:

- **credential**: An identity and ownership credential for a personal or `Fay` subject; see [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, the upper-level system to which MeriToken belongs; see [glossary.md](./glossary.md).
- **Fay**: A non-personal subject that references MeriToken; see [glossary.md](./glossary.md).
- **ifay**: Name of the project system; see [glossary.md](./glossary.md).

The Chinese primary form of MeriToken is used as the conventional designation of MeriToken only in the body text of the `zh-CN` and `zh-TW` blueprints. See the `Localized_Term` section of [glossary.md](./glossary.md) for the localization rules of MeriToken across languages.
