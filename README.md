# DepthSift

An extensible desktop crypto liquidity screener.

DepthSift is being developed to help traders discover spot trading pairs that match configurable conditions for order-book depth, bid–ask spread, 24-hour quote volume, recent trade activity, and Spot API availability.

The project targets Windows and macOS. Its initial integration focuses on MEXC Spot and MetaScalp, with separate interfaces for exchange adapters, market-data providers, and custom filters.

Screening profiles will define the selected markets, order size, thresholds, and enabled filters. Results will explain why each pair passes, fails, or cannot yet be evaluated because data is missing, incomplete, or stale.

**Status:** specification v1.2; source qualification and an internal prototype are the next milestones. Implementation and live integration validation are pending.

The [development specification](docs/specification.md) is the normative text. It separates source qualification, a small internal prototype, and the full first release, and includes acceptance scenarios and request-budget recovery rules. The [Word edition v1.2](docs/MetaScalp_Screener_Specification_v1_2.docx) contains the same requirements. [Version 1.1](docs/MetaScalp_Screener_Specification_v1_1.docx) is retained for reference.

The initial protocol schemas cover the [Companion envelope](docs/contracts/companion-envelope.schema.json) and the [permit-resolution response](docs/contracts/permit-resolution.schema.json). Other operation payloads require their own schemas before implementation enables the corresponding capability. Schema validation complements the semantic checks described in the specification.
