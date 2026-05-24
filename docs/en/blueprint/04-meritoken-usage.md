# 04 MeriToken Referencing and Applications

> Introduction: This document continues from the position in [01-meritoken-overview.md](./01-meritoken-overview.md), the retrieval flow in [02-meritoken-technical.md](./02-meritoken-technical.md) and the social meaning in [03-meritoken-social.md](./03-meritoken-social.md). It lands the three questions "who references MeriToken", "how the referencing is done" and "in what scenarios MeriToken is referenced" separately for the two classes of referrers — personal subjects and `Fay` subjects.

## Background

The two foundational roles of MeriToken — "contract component" and "social-relationship connector" — only come into play when MeriToken is actually referenced. This blueprint explicitly divides MeriToken referrers into two classes:

- **Personal subjects**: natural persons acting as referrers, using MeriToken to participate in collaboration, express evaluations, and assert their rights.
- **`Fay` subjects**: non-personal subjects within the ifay system that bear the responsibility of "referencing MeriToken" — for example, organizations, projects, collaboration units and Fay-ified service instances. In the new society, `Fay` subjects take on the role of referrer in parallel with personal subjects, but their referencing methods and application scenarios differ structurally from those of personal subjects.

The reason for discussing the two classes of referrers in parallel is to avoid two common skews in the new society: treating MeriToken merely as an extension of a personal résumé, or treating MeriToken merely as an internal scoring tool inside an organization. Only by placing the two classes of referrers side by side can we present a complete picture of MeriToken as social infrastructure.

The differences between `Fay` and the traditional `agent` are carried by the official external links in [07-related-projects.md](./07-related-projects.md) and are not restated here.

## Core content

### The referencing methods and application scenarios of personal subjects

The personal subject is the most direct referrer of MeriToken in the new society. A personal subject is both a producer of MeriToken (contributor, witness, evaluator) and a user of MeriToken (citing existing entries in collaboration, appeals and deliberation).

#### Referencing methods

The concrete way in which a personal subject references MeriToken follows the "reference → verify → disclose" three-step flow described in [02-meritoken-technical.md](./02-meritoken-technical.md), and lands on four classes of concrete actions:

- **Holding-style referencing**: the personal subject holds the set of its own MeriToken in its growth portrait, collaboration archive and community-participation archive, and presents a subset to specific counterparts when needed. The act of presentation only generates a referencing record at the lowest disclosure tier and does not force disclosure of the details.
- **Citation-style referencing**: in argumentation, proposals and appeals, the subject cites existing MeriToken entries — its own or someone else's — as evidence. A citation must come with a verifiable reference handle, so that the audience can independently verify the existence and ownership of the entry, rather than rely on the citing party's unilateral statement.
- **Relational referencing**: when collaborating with another party, the subject uses the counterpart's existing MeriToken entries as the basis of trust, and deposits the output of the present collaboration as new MeriToken entries. This is the most common landing of the "social-relationship connector" semantics on the personal-subject side.
- **Withdrawal-style referencing**: the subject revokes a previously granted high-disclosure-tier authorization to a specific referrer. A withdrawal does not erase the trace of the original referencing action, but it removes the referrer's right to continue exposing the content.

These four methods share the same technical substrate (multi-party co-signing, on-chain commitments, tiered disclosure), and differ only in the trigger scenarios and the choice of disclosure tier.

#### Application scenarios

The following are several typical application scenarios that show how a personal subject uses MeriToken in everyday collaboration in the new society:

- **First handshake of a cross-organization collaboration**: when a personal subject joins a brand-new collaboration group, it can present a subset of MeriToken relevant to the group's topic at the lowest disclosure tier, allowing the group to perform an initial review without exposing the personal portrait.
- **Speech qualification on public issues**: when a personal subject speaks on a public issue, it cites its own MeriToken entries on adjacent issues as evidence of speech weight, and the audience can independently verify them as needed.
- **Education and transmission scenarios**: when a personal subject acts as a mentor, the mentoring relationship is deposited as the corresponding MeriToken entries. Long-term accumulation by the mentee yields an independently verifiable growth archive that is not imprisoned by any educational institution.
- **Appeal and correction scenarios**: when a personal subject considers an existing MeriToken entry to be unfair, it can initiate an appeal entry to record the questioning process itself in `GMC`. The final outcome (whether upheld or dismissed) is also deposited as a new entry.
- **Switching across identities**: when a personal subject moves between social roles (occupation, community, public participation), it can selectively present the subset of MeriToken relevant to the current role, avoiding over-exposure of unrelated portraits.

These scenarios all follow the shared principle of "minimal-disclosure default, scenario-driven escalation, ever-present revocation", consistent with the privacy guarantees in [02-meritoken-technical.md](./02-meritoken-technical.md).

### The referencing methods and application scenarios of Fay subjects

`Fay` subjects are the non-personal subjects within the ifay system that bear the responsibility of "referencing MeriToken". A `Fay` subject is not a substitute for a personal subject; it is an amplifier of personal-subject collaboration. It takes on the role of referencing, aggregating and coordinating in collaborations of larger scale, more participants and longer lifecycle.

#### Referencing methods

The referencing methods of `Fay` subjects share the same underlying flow as those of personal subjects, but differ structurally in usage scenarios and the boundary of authority:

- **Proxy-style referencing**: a `Fay` subject exercises referencing authority on behalf of a group of personal subjects or sub-`Fay` subjects within its authorization scope, in a unified manner. The proxy relationship itself is recorded as a MeriToken entry, with the authorization scope, validity period and revocation conditions all stated explicitly in the entry.
- **Aggregation-style referencing**: a `Fay` subject can aggregate the MeriToken entries of multiple personal subjects to form an outward-facing composite referencing surface. Aggregation is not possession: every aggregated entry is still held by its original owner; the `Fay` subject only holds the usage right of "referencing these entries in a particular scenario".
- **Protocol-style referencing**: when a `Fay` subject collaborates with another `Fay` subject, the referencing relationship is generally based on a pre-signed protocol. The protocol itself is also recorded as MeriToken entries, constituting a collaboration ledger between `Fay` subjects.
- **Lifecycle-management referencing**: a `Fay` subject can reference the MeriToken entries about its own lifecycle (formation, phase transitions, dissolution), allowing external subjects to see its history and changes.

The referencing authority of a `Fay` subject is technically homologous to that of a personal subject, but at the institutional layer it is more tightly constrained: the boundary of aggregation, the scope of proxy and the visibility of the protocol all require relatively clear verifiable records, in order to avoid the imbalance of "a `Fay` subject leveraging its scale to override personal subjects".

#### Application scenarios

Typical application scenarios of `Fay` subjects in the new society are as follows:

- **Collaboration subjects of public projects**: cross-regional, cross-organization public projects collaborate externally as `Fay` subjects, aggregating the contributions of many personal subjects into a unified outward referencing surface that displays the project's overall MeriToken profile.
- **Industry-level collaboration ledgers**: several `Fay` subjects in an industry establish a shared ledger via protocol-style referencing, mutually recognizing each other's MeriToken entries and avoiding repeated reconciliation across organizations.
- **Execution units in community governance**: `Fay` subjects acting as execution units within a community implement decisions made through deliberation, and deposit the decision actions as traceable MeriToken entries. Community members can cite these entries at any time to question or commend the execution unit.
- **Cross-generation continuity of projects**: long-running projects exist in the form of `Fay` subjects, so that the collaboration archive is preserved even after founding members depart. New members access the project's history via holding-style referencing, avoiding the knowledge breaks of a "project restart".
- **Bearing responsibility and witnessing fulfillment**: a `Fay` subject in the new society is both a collaboration amplifier and a bearer of responsibility. When a `Fay` subject makes an external promise, the promise itself is recorded as a MeriToken entry, and fulfillment or default is anchored by the corresponding entry.

The application scenarios of `Fay` subjects do not replace those of personal subjects. Rather, they are "two scales of the same infrastructure": personal subjects handle local, face-to-face, single-point collaboration, while `Fay` subjects handle cross-regional, cross-organization, long-term collaboration. The two classes of referrers reference each other and bear responsibility to each other through MeriToken entries, constituting the collaboration ecology of the new society.

> ⏳ **Pending illustration** (slot: `meritoken-usage-comparison`)
> Description: A comparison diagram presenting both classes of referrers — personal subjects and `Fay` subjects — together with their referencing methods (holding / citation / relational / withdrawal vs. proxy / aggregation / protocol / lifecycle) and typical application scenarios, with annotations showing that the two classes of referrers reference each other and bear responsibility to each other through MeriToken entries.
> Planned file: `illustration/meritoken-usage-comparison.png`

## Relationship with other topics

| Topic | Relationship to this document |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Provides the definitions of the two foundational roles that the referencing and applications in this document then land on. |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Provides the retrieval flow and the privacy / ownership semantics that underpin every referencing method here. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Provides the social-meaning background for the application scenarios here (social relationships, political logic, economic structure, personal-growth mapping). |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | At the layer of "identity and ownership" semantics, contrasts with the "contribution and evaluation" semantics here, preventing the two from being mixed. |
| [06-meritoken-deep-cases.md](./06-meritoken-deep-cases.md) | Extends the application scenarios here in cross-subject high-density collaboration and rolling scenarios. |
| [07-related-projects.md](./07-related-projects.md) | Provides the official external links for upstream topics such as `Fay`, `agent`, ifay, `GMC` and the overall framework. |

## Term footnotes

`Reserved_Term`s appearing in this document:

- **Fay**: A non-personal subject that references MeriToken; see [glossary.md](./glossary.md).
- **agent**: An agent entity in traditional LLM frameworks; see [glossary.md](./glossary.md).
- **ifay**: Name of the project system; see [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, the upper-level system to which MeriToken belongs; see [glossary.md](./glossary.md).
- **credential**: An identity and ownership credential for a personal or `Fay` subject; see [glossary.md](./glossary.md).

The Chinese primary form of MeriToken is used as the conventional designation of MeriToken only in the body text of the `zh-CN` and `zh-TW` blueprints. See the `Localized_Term` section of [glossary.md](./glossary.md) for the localization rules of MeriToken across languages.
