# Security Policy

## Supported Versions

Security and protocol-privacy advisories apply to the current specification and blueprint baseline on `main`:

| Artifact / Scope | Version / Branch | Supported |
| --- | --- | --- |
| `MeriToken` Citation & Tiered Disclosure Blueprints (`docs/`) | `main` / `1.0` baseline | Yes |
| Legacy unaligned drafts | Pre-`main` snapshots | No |

## Security Scope

`MeriToken` (measured in `μ` / `Merit Unit`) is a strictly non-monetary measure of social contribution anchored on `GMChain` and presented off-chain through selective disclosure. In-scope security and privacy issues include:

1. **Off-Chain Citation Handle (`mtk_`) Integrity & Non-Transferability**:
   - Handle spoofing, binding ambiguity, replay, or protocol flaws that allow an actor to misattribute another Human Prime's, `iFay`'s, or `coFay`'s `GMChain` contribution record, or that violate `MeriToken` non-transferability and non-monetary invariants.
2. **Three-Tier Selective Disclosure Privacy**:
   - Downgrade, correlation, or unintended over-disclosure flaws across the three disclosure tiers (violating Tier 1 `existence_and_attribution` as the mandatory minimal default, or exposing Tier 2 `semantic_summary` / Tier 3 `raw_evidence` and social graphs without explicit scoped authorization).
3. **Revocation Ripple & Credential Boundary Integrity**:
   - Failure to propagate disclosure-grant revocations (Revocation Ripple) to downstream verifiers, or confusion/substitution attacks across the boundary between static identity credentials (`FayID`) and cumulative contribution records (`MeriToken`).

## Reporting a Vulnerability

**Please do NOT report undisclosed protocol vulnerabilities or privacy-de-anonymization vectors through public GitHub Issues or Pull Requests.**

- **Primary Channel (Recommended)**: Submit a report privately via **GitHub Private Vulnerability Reporting (Security Advisories)**:
  - https://github.com/ChainMode/MeriToken/security/advisories/new
- **Fallback Email Channels**: If GitHub Security Advisories is unavailable to you, email **[jah.g@ifay.ai](mailto:jah.g@ifay.ai)** or **[hello@meritora.org](mailto:hello@meritora.org)** with `[SECURITY][MeriToken]` in the subject line.

Please describe the protocol scenario, affected specification chapters, threat model assumptions, and potential privacy or attribution impact.

## Coordinated Disclosure Policy

- **Acknowledgment**: Within **72 hours** of receiving your report.
- **Triage & Assessment**: Initial protocol/security assessment within **7 calendar days**.
- **Coordinated Disclosure Window**: **90 days** from report receipt to coordinated specification/advisory publication.
- **Credit**: Reporters are acknowledged in the published advisory unless anonymity is requested.
