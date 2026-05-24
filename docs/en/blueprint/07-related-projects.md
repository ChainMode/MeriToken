# 07 Relationship with the ifay System

> This document, in the form of "minimal necessary positional notes + a list of external links pointing to the official documentation pages", consolidates the relationship between several upstream topics in the ifay system and the MeriToken blueprint, avoiding lengthy treatment of upstream topics inside this repository.

## Background

The blueprint of this repository takes the in-depth analysis of MeriToken as its main axis. Topics such as ifay, GMC, Fay, agent, phase and the overall framework are positioned as supporting background necessary for the analysis of MeriToken, not as the writing goal of this repository.

To avoid maintenance cost and version drift, this blueprint does not unfold lengthy narratives of those upstream topics inside the repository. For each topic only the minimal necessary positional notes related to MeriToken are provided, after which the reader is routed via external links to the corresponding official documentation page on ifay.ai, where the upstream project's authoritative narrative lives.

For readers encountering the ifay system for the first time, we recommend using this document as the "external-link entry page": first build the upstream background by following the links in the official-documentation external-link list, and then return to [01-meritoken-overview.md](./01-meritoken-overview.md) to enter the main line.

## Relationship with this blueprint

Each upstream term below appears in this blueprint in the form of a "minimal note", with its minimal connection to MeriToken stated as follows:

- **ifay**: the name of the project system, the overall technical and social operating environment that MeriToken depends on. This blueprint does not unfold the ifay system itself, and only cites it as needed when describing the operating environment of MeriToken.
- **GMC**: Global Merit Chain, the upper-level system to which MeriToken belongs. This blueprint explains the subordination of MeriToken to GMC in [01-meritoken-overview.md](./01-meritoken-overview.md), and does not unfold the overall design of GMC.
- **Fay**: a non-personal subject within the ifay system that bears the responsibility of "referencing MeriToken", and that stands alongside personal subjects as one of the two classes of MeriToken referrers. This blueprint discusses the referencing methods and application scenarios of Fay subjects independently in [04-meritoken-usage.md](./04-meritoken-usage.md).
- **agent**: a program entity in traditional LLM frameworks that autonomously executes tasks; in the ifay paradigm, the agent provides a contrast with the personal subject and the Fay subject. This blueprint does not unfold the discussion of the differences between the agent and the ifay paradigm; it provides only the entry to authoritative definitions via external links.
- **phase**: an evolutionary stage number for the project to which the blueprint belongs. The concrete stage semantics, timeline and milestones are maintained by ifay.ai documentation; this repository does not restate them.
- **Overall framework**: the overall architecture of the ifay project and the interactions among its components. The blueprint of this repository focuses on MeriToken as one component; for the overall framework, please visit the corresponding official documentation page on ifay.ai directly.

## Official-documentation external-link list

The table below gives the minimal external-link set required by this blueprint. The form of the links is fixed as "pointing to the corresponding official documentation page on ifay.ai". The concrete URLs are pinned at the design layer; substituting a domain other than `ifay.ai` is not permitted.

| Upstream term | Minimal note in this blueprint | Upstream_Project_Doc_Link |
|----------|-----------------------|---------------------------|
| ifay     | The overall project system on which MeriToken depends | https://ifay.ai/docs/ifay |
| GMC      | The upper-level system to which MeriToken belongs (Global Merit Chain) | https://ifay.ai/docs/gmc |
| Fay      | A non-personal subject that references MeriToken, in parallel with personal subjects | https://ifay.ai/docs/fay |
| agent    | The traditional agent-program paradigm contrasted with the ifay paradigm | https://ifay.ai/docs/agent |

Other upstream topics such as phase and the overall framework have dedicated pages on the ifay.ai site; readers are expected to navigate the site to access them as needed. This blueprint does not pin those links here, in order to avoid link drift.

## Term footnotes

`Reserved_Term`s appearing in this document:

- **ifay**: Name of the project system; see [glossary.md](./glossary.md).
- **GMC**: Global Merit Chain, the upper-level system to which MeriToken belongs; see [glossary.md](./glossary.md).
- **Fay**: A non-personal subject that references MeriToken; see [glossary.md](./glossary.md).
- **agent**: An agent entity in traditional LLM frameworks; see [glossary.md](./glossary.md).
- **phase**: An evolutionary stage number in the blueprint; see [glossary.md](./glossary.md).

The Chinese primary form of MeriToken is used as the conventional designation of MeriToken only in the body text of the `zh-CN` and `zh-TW` blueprints. See the `Localized_Term` section of [glossary.md](./glossary.md) for the localization rules of MeriToken across languages.
