# DepthSift

An extensible desktop crypto liquidity screener.

DepthSift is being developed to help traders discover spot trading pairs that match configurable conditions for order-book depth, bid–ask spread, 24-hour quote volume, recent trade activity, and Spot API availability.

The project targets Windows and macOS. Its initial integration focuses on MEXC Spot and MetaScalp, with separate interfaces for exchange adapters, market-data providers, and custom filters.

Screening profiles will define the selected markets, order size, thresholds, and enabled filters. Results will explain why each pair passes, fails, or cannot yet be evaluated because data is missing, incomplete, or stale.

**Status:** specification v1.3; source qualification and an internal prototype are the next milestones. Implementation and live integration validation are pending.

The [development specification](docs/specification.md) is the normative text. It separates source qualification, a small internal prototype, and the full first release, and includes acceptance scenarios, request-budget recovery rules, an active-set capacity model, default timeouts, a glossary, and a section-to-scenario traceability matrix. The [Word edition v1.3](docs/MetaScalp_Screener_Specification_v1_3.docx) contains the same requirements; earlier editions remain available in the git history.

The protocol schemas in [docs/contracts](docs/contracts) cover the [Companion envelope](docs/contracts/companion-envelope.schema.json), the hello and welcome handshake, order-book snapshot requests and responses, `instrument.open`, `request.cancel`, `limit.pause` and `limit.paused`, `requests.quiesce` and the [permit-resolution response](docs/contracts/permit-resolution.schema.json), and typed errors, with shared definitions in [common.schema.json](docs/contracts/common.schema.json). Payloads for health, heartbeat, connection and instrument listings, and terminal targets still require their own schemas before implementation enables the corresponding capability. Valid and invalid example messages live in [docs/contracts/examples](docs/contracts/examples); `python3 docs/contracts/check_examples.py` validates them (requires the `jsonschema` package). Schema validation complements the semantic checks described in the specification.
