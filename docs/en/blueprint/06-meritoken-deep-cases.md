# 06 MeriToken Advanced Topics

> Introduction: This document is the extension slot of the MeriToken topic set. Building on every prior agreement in [01-meritoken-overview.md](./01-meritoken-overview.md) through [05-meritoken-credential.md](./05-meritoken-credential.md), it develops as standalone advanced topics two high-density usage settings of MeriToken in the new society — "high-density use across multiple subjects" and "rolling scenarios". Each topic does not restate concepts already covered on the main line; it places the main-line mechanisms back into a concrete pressure scenario for another look.

## Background

The main line, documents 01 through 05, has clarified the position of MeriToken, its technical principles, social meaning, referencing and applications, and its boundary with `credential`. Once the new society actually lands, however, two classes of "high-load" settings emerge that the main-line discussion cannot directly cover:

- **High-density use across multiple subjects**: when several `Fay` subjects and several personal subjects continuously reference MeriToken on the same topic, an individual reference looks simple, but the aggregate brings three problems — overhead, disclosure and aggregation.
- **Rolling scenarios**: when the lifecycle of a collaboration is long enough, MeriToken stops being the trace of a one-shot deliverable and instead has to go through cycles of accumulation, revision, withdrawal and archiving across multiple rounds. This requires the MeriToken mechanism to remain self-consistent on a long time scale, not merely look reasonable on a single act of referencing.

This document develops the two topics. Each topic first sketches the source of pressure, then revisits the main-line mechanisms (retrieval, disclosure, trace, ownership and usage rights, the boundary with `credential`, and so on) under that pressure, and points out open questions worth further argument or engineering work. This document does not introduce new concepts at the protocol layer; everything is a continued derivation of mechanisms already defined on the main line, applied in new settings.

## Core content

### Topic A: High-density use across multiple subjects

**Source of pressure**: in real collaboration in the new society, "one `Fay` subject references one MeriToken" is too idealized a minimal setting. What is more common is that on the same topic three classes of referrers appear simultaneously:

- **Multiple `Fay` subjects**: for example, collaborators from different industries and regions each reference the relevant MeriToken on behalf of their own members;
- **Multiple personal subjects**: for example, the key participants on the topic each cite the MeriToken entries from their own past relevant collaborations;
- **Nested referencing**: the `Fay` subjects above themselves reference some personal subjects' MeriToken entries as the basis of their representational authority.

This high-density referencing happens within the same topic, the same time window and the same disclosure surface, and pushes several properties of the MeriToken mechanism to their pressure limits at the same time.

**Mechanisms revisited**:

- **The boundary of reference aggregation**: aggregation-style referencing by a single `Fay` subject is already a composite referencing surface (see the "The referencing methods and application scenarios of Fay subjects" section of [04-meritoken-usage.md](./04-meritoken-usage.md)). When the composite referencing surfaces of multiple `Fay` subjects stack on the same topic, the external reviewer needs not "every MeriToken to be unfolded" but "to confirm that these aggregated surfaces do not contradict each other without unfolding the details". This means aggregation-style referencing must support "reconcilability at the aggregation level", not just verifiability at the level of individual entries.
- **Coordination of tiered disclosure**: in high-density use, each referenced party (a personal subject or a lower-level `Fay` subject) may have a different disclosure-tier permission. The aggregator cannot mix high-tier and low-tier disclosures into a single external presentation; otherwise that is equivalent to forcing a low-tier disclosure to escalate. Topic A requires the principle of "minimal-disclosure-tier as backstop": the disclosure tier of an aggregated surface is no higher than the lowest-permission tier among any of the referenced entries it contains, and is escalated as a whole only when every referenced party actively consents.
- **Echo of the revocation path**: when an underlying personal subject revokes its disclosure permission, the share corresponding to that entry must immediately become invalid in every `Fay`-subject aggregated surface that depended on it. There must be no situation in which "the upstream has revoked but the downstream aggregation continues to expose by means of caches". This extends the "revocation and invalidation" semantics of the "Privacy guarantees" section of [02-meritoken-technical.md](./02-meritoken-technical.md) into the nested setting.
- **Readability of the retrieval trace**: in the high-density setting, recording every reference under `GMC` causes the trace volume of a single topic to balloon quickly. The trace at the mechanism layer is still necessary, but for human presentation it needs to be folded along the three axes of "topic — subject — time", to avoid drowning the audit process in raw trace entries.

**Open questions**:

- Which set of commitment mechanisms exactly carries reconcilability at the aggregation level needs to be designed together with the upper-level rules of `GMC`;
- The negotiation flow between "minimal-disclosure-tier as backstop" and individual participants' wish to escalate the whole should itself be recorded as MeriToken entries;
- The presentation rules for trace folding are not a protocol-layer issue, but they need to be agreed upon in unison by the supporting toolchain of the blueprint.

> ⏳ **Pending illustration** (slot: `meritoken-deep-cases-density`)
> Description: A conceptual diagram presenting reference aggregation / tiered disclosure / revocation paths of MeriToken in cross-subject high-density collaboration scenarios.
> Planned file: `illustration/meritoken-deep-cases-density.png`

### Topic B: Rolling scenarios

**Source of pressure**: in long-lifecycle projects, MeriToken does not stay at the minimal unit of "one contribution — one evaluation — one trace". It will recur over a long time scale through cycles of accumulation, revision, withdrawal and archiving. Typical settings include cross-generation public projects, long-evolving open-source collaborations, and community governance facing multiple cohorts of participants. The pressure brought by such projects is no longer the complexity of a single referencing action, but the self-consistency of the mechanism over a long time scale.

**Mechanisms revisited**:

- **Accumulation**: every stage of the project deposits new MeriToken entries that are recorded under `GMC` and are not lost when stages change. But the project's outward "overall picture" must avoid stacking every entry indiscriminately; layering by stage, by role and by topic is necessary. This is consistent with "from single-point capability to multidimensional portrait" in the "Personal-growth mapping" section of [03-meritoken-social.md](./03-meritoken-social.md), but on the project side a `Fay` subject must take on the responsibility of layered aggregation.
- **Revision**: when an existing MeriToken entry receives, at the factual layer, new witnessing, new evaluation or new comparison, the appropriate response is to append a revision entry rather than overwrite the original. The revision entry is itself a MeriToken entry, containing the reason for revision and multi-party co-signing. Along the timeline a reader can see both the original entry and the subsequent revisions, avoiding the situation where "a single entry is repeatedly rewritten and history is flattened".
- **Withdrawal**: in a long lifecycle, withdrawal refers not only to the withdrawal of disclosure permissions but also to the withdrawal of the effect of the original entry (for example, the issuer leaves, or the precondition of the collaboration changes). Withdrawal of effect does not delete the trace; it marks the entry's state as "withdrawn" so that subsequent referrers can distinguish "references made before the withdrawal" from "references made after the withdrawal". The act of withdrawal follows the independent revocation path defined in the "The boundary and correspondence" section of [05-meritoken-credential.md](./05-meritoken-credential.md), without compensating for the recovery path of `credential`.
- **Archiving**: when a project stage ends or the project as a whole concludes, the relevant MeriToken entries should enter an archived state rather than be destroyed. In the archived state, the entries can still be independently verified and cited, but the default disclosure tier drops to the lowest, avoiding the situation where, years after a long-running project ends, the entries continue to expose participants at a high disclosure tier. The archiving transition itself is recorded under `GMC`, avoiding any "after a certain point in time the visibility of an entry quietly changes" opacity.

**Self-consistency of the mechanism**: accumulation / revision / withdrawal / archiving form a complete cycle, and every action leaves a trace as a new entry. This ensures that the dimension of "time" itself is drawn into the MeriToken mechanism, rather than being controlled unilaterally from outside by the project owner. Any state change along the time dimension must be independently verifiable, without depending on the project owner's interpretation.

**Open questions**:

- Whether the multi-party co-signing scope of a revision entry should match exactly that of the original entry needs to be refined per scenario;
- Whether the default disclosure tier of the archiving transition can be adjusted collectively by the project owner and the participants, and the negotiation flow that this requires;
- Whether the weight of cross-stage referencing decays over time is a per-project strategic choice and should be supported by the toolchain rather than mandated by the protocol layer.

## Relationship with other topics

| Topic | Relationship to this document |
|------|--------------|
| [01-meritoken-overview.md](./01-meritoken-overview.md) | Provides the definitions of the two foundational roles. Topic A and Topic B both build on "contract component / social-relationship connector". |
| [02-meritoken-technical.md](./02-meritoken-technical.md) | Provides the concrete technical semantics of retrieval, disclosure, withdrawal and ownership/usage rights, which the topics here reuse under high density and on long time scales. |
| [03-meritoken-social.md](./03-meritoken-social.md) | Provides the social-meaning basis of "discourse-weight mapping". Topic A reuses it in cross-subject collaboration; Topic B reuses it in rolling scenarios. |
| [04-meritoken-usage.md](./04-meritoken-usage.md) | Provides the referencing methods and application scenarios for both classes of referrers — personal subjects and `Fay` subjects. Topic A here is its extension under high-density stacking. |
| [05-meritoken-credential.md](./05-meritoken-credential.md) | Provides the boundary and correspondence with `credential`. Topic B here reuses the principle of "independent revocation paths" in the withdrawal path. |
| [07-related-projects.md](./07-related-projects.md) | Provides the official external links for upstream topics such as ifay, `GMC`, `Fay`, `agent`, `phase` and the overall framework. |

## Term footnotes

`Reserved_Term`s appearing in this document:

- **GMC**: Global Merit Chain, the upper-level system to which MeriToken belongs; see [glossary.md](./glossary.md).
- **Fay**: A non-personal subject that references MeriToken; see [glossary.md](./glossary.md).
- **credential**: An identity and ownership credential for a personal or `Fay` subject; see [glossary.md](./glossary.md).
- **ifay**: Name of the project system; see [glossary.md](./glossary.md).

The Chinese primary form of MeriToken is used as the conventional designation of MeriToken only in the body text of the `zh-CN` and `zh-TW` blueprints. See the `Localized_Term` section of [glossary.md](./glossary.md) for the localization rules of MeriToken across languages.
