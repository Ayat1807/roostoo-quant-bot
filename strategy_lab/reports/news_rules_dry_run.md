# News risk layer: historical dry run of the deterministic rules (block 11)

_Generated 2026-10-08 07:50 UTC by `python -m lab.b11`. Rules declared in `variants_b11_news.yaml` before the run. **Not hindsight-contaminated**: the calendar and Fear & Greed rules use no LLM. **The headline veto rule is NOT evaluated here**: there is no free archive of timestamped headlines, and LLM recall of past events would be hindsight-contaminated; it is judged on the forward shadow log only._

Trials: 521 declared; luck threshold about 2.9 SE.

## How often the rules fire

| period | calendar rule active (share of hours) | Fear & Greed rule (share of days) |
|---|---|---|
| IS | 6.3% | 5.2% |
| OOS | 6.2% | 5.9% |
| Jan 2025 - Jun 2026 | 6.2% | 5.9% |

## Return and drawdown, with vs without the layer

| period | return without / with | max drawdown without / with | Sharpe without / with | worst 14d without / with |
|---|---|---|---|---|
| IS | +97.8% / +83.3% | -16.8% / -16.3% | 1.00 / 0.93 | -5.3% / -5.4% |
| OOS | +34.5% / +34.9% | -12.0% / -11.6% | 1.38 / 1.38 | -5.2% / -5.0% |
| Jan 2025 - Jun 2026 (team window) | +34.5% / +34.9% | -12.0% / -11.6% | 1.38 / 1.38 | -5.2% / -5.0% |

## Team objective (lab/b5.py)

| | median 14d composite IS / OOS | mean 14d IS / OOS | down-window mean IS / OOS | OOS Sharpe | meets all | beats s3v2e_core10 |
|---|---|---|---|---|---|---|
| b3_s3v2e_core10 | -1.61 / -0.28 | +0.6% / +0.8% | +0.6% / +2.0% | 1.38 | yes |  |
| b11_news_rules | -1.81 / -0.70 | +0.6% / +0.8% | +0.6% / +2.1% | 1.38 | yes | no |

Fear & Greed rule fired at 157 of 2424 daily target computations; calendar overlay active in 3650 hourly bars.
