# DepthSift

An extensible desktop crypto liquidity screener.

DepthSift is being developed to help traders discover spot trading pairs that match configurable conditions for order-book depth, bid–ask spread, 24-hour quote volume, recent trade activity, and Spot API availability.

The project targets Windows and macOS. Its initial integration focuses on MEXC Spot and MetaScalp, with separate interfaces for exchange adapters, market-data providers, and custom filters.

Screening profiles will define the selected markets, order size, thresholds, and enabled filters. Results will explain why each pair passes, fails, or cannot yet be evaluated because data is missing, incomplete, or stale.

**Status:** specification completed; implementation and live integration validation are the next milestones.
