# Contributing to MeriToken

Thank you for contributing to **MeriToken**! Participation in this repository is governed by our [Code of Conduct](./CODE_OF_CONDUCT.md). For protocol-privacy or selective-disclosure security concerns, please use the private channels listed in [SECURITY.md](./SECURITY.md).

## Documentation Quality & Verification Guidelines

`MeriToken` hosts the architectural blueprints and protocol specifications for off-chain citation handles and tiered selective disclosure across 9 locales under `docs/` (`zh-CN` canonical source, synchronized with `zh-TW`, `ja`, `ko`, `en`, `de`, `es`, `fr`, `ru`):

```bash
# Clone your fork
git clone https://github.com/ChainMode/MeriToken.git
cd MeriToken
```

When proposing documentation or specification improvements:

1. **Canonical Source & Locale Parity**: Author substantive structural changes against `docs/zh-CN/` (and `docs/en/`) first, keeping section hierarchy, Markdown tables, and relative cross-references aligned across locales.
2. **Scope Boundary Discipline**: Keep on-chain accounting, decay formulas, quota refresh, and consensus rules referenced from `GMChain` rather than duplicating ledger formulas inside `MeriToken`; focus `MeriToken` specifications on off-chain citation handles (`mtk_`), three-tier selective disclosure (`existence_and_attribution`, `semantic_summary`, `raw_evidence`), revocation ripples, and the credential-vs-contribution boundary.
3. **Link & Formatting Hygiene**: Verify that all relative Markdown links resolve cleanly and Markdown tables render without broken columns.

## Contribution Workflow

1. **Fork & Branch**: Fork `https://github.com/ChainMode/MeriToken.git` and create a topic branch from `main`.
2. **Conventional Commits**: Use Conventional Commits (`docs:`, `feat:`, `fix:`, `chore:`).
3. **Sign Off Your Commits (DCO 1.1)**: Commit with `git commit -s` so every commit includes a valid `Signed-off-by` line.
4. **Pull Request**: Open a Pull Request against `main` explaining the specification or editorial improvement and listing updated locales.

## Developer Certificate of Origin v1.1 (DCO 1.1) & Licensing

We use the **Developer Certificate of Origin Version 1.1 (DCO 1.1)** (`https://developercertificate.org/`). **No separate CLA is required.**

Every commit must carry a `Signed-off-by` trailer (`git commit -s`):

```text
Signed-off-by: Jane Doe <jane.doe@example.com>
```

Contributions are accepted under **Inbound = Outbound** dual-track licensing (`Copyright (c) 2025-2026 ChainMode contributors`):

- **Source Code, Schemas & Test Vectors**: Licensed under the **MIT License** ([LICENSE](./LICENSE)).
- **Specifications & Architectural Blueprints** (`docs/`): Licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)** ([LICENSE-DOCS](./LICENSE-DOCS)).

## Ecosystem Terminology Alignment

Strict terminology precision is essential in `MeriToken`:

- **`MeriToken` (`美誉值`) & `Merit Unit` (`μ`)**: Always describe `MeriToken` (measured in `μ` / `Merit Unit`) strictly as a non-monetary, non-transferable measure of social contribution.
- **`GMChain` (`公誉链`)**: Always use `GMChain` (`公誉链` / Global Merit Chain) as the canonical name for the underlying contribution ledger.
- **`Human Prime` (`人类原型`) & `Host` (`宿主`)**: Use `Human Prime` (`人类原型`) for living human individuals, and `Host` (`宿主`) strictly for terminal hardware devices or runtime environments.
- **`Fay = iFay + coFay`**: Use `Fay` as the umbrella term encompassing both `iFay` (individual avatar) and `coFay` (public or organizational role avatar).
