# CV statistics: s3v2e_core10 (live) and HMM2 + CUSUM (forward test)

_Generated 2026-10-09 03:03 UTC by `python -m lab.cv_stats` from existing strategy_lab runs (`b3_s3v2e_core10`, `b7_hmm2_cusum`) and, for the live rows, `strategy_bot/cv_live_stats.py` output. No new trials, no estimates; "not computed" = the source does not exist here._

## Backtest (simulated, hourly, Roostoo costs)

| | s3v2e_core10 (live) | HMM2 + CUSUM (forward test) |
|---|---|---|
| **IS** period | 2020-02-15 to 2024-12-31 (1782 days) | 2020-02-15 to 2024-12-31 (1782 days) |
| IS Sharpe | 1.00 | 1.04 |
| IS Sortino | 1.48 | 1.56 |
| IS Calmar | 0.89 | 0.76 |
| IS max drawdown | -16.8% | -17.5% |
| IS total return | +97.8% | +84.5% |
| IS annualised return (CAGR) | +15.0% | +13.4% |
| IS trades per day | 2.0 | 2.3 |
| IS fees per year (share of mean equity) | 3.7% | 3.8% |
| IS stress (100% taker + 7 bps): return / Sharpe / max drawdown | +73.7% / 0.84 / -19.0% | +70.8% / 0.93 / -18.0% |
| **OOS** period | 2025-01-01 to 2026-06-30 (546 days) | 2025-01-01 to 2026-06-30 (546 days) |
| OOS Sharpe | 1.38 | 1.55 |
| OOS Sortino | 2.00 | 2.27 |
| OOS Calmar | 1.83 | 2.53 |
| OOS max drawdown | -12.0% | -8.1% |
| OOS total return | +34.5% | +32.1% |
| OOS annualised return (CAGR) | +21.9% | +20.5% |
| OOS trades per day | 2.1 | 2.4 |
| OOS fees per year (share of mean equity) | 4.3% | 4.2% |
| OOS stress (100% taker + 7 bps): return / Sharpe / max drawdown | +31.2% / 1.27 / -12.1% | +27.1% / 1.34 / -9.4% |
| cost assumptions (backtest) | taker 0.10% per fill (100% of spot fills assumed taker) + 2 bps slippage per fill; shorts 0.10% on open AND on close + slippage | taker 0.10% per fill (100% of spot fills assumed taker) + 2 bps slippage per fill; shorts 0.10% on open AND on close + slippage |

## LIVE (real exchange, Roostoo; label: live)

| | s3v2e_core10 (live) | HMM2 + CUSUM (forward test) |
|---|---|---|
| live on its own key | not computed | not computed |

**Whole competition account since 2026-10-06 15:30 UTC** (xsmom on R1 ran until 2026-10-07 10:00 UTC, then s3v2e_core10 from 10:04 UTC): not computed

_Live rows are "not computed" here: the live logs exist only on the EC2 machine (`logs_competition/`, `logs_competition_s3v2e/`, `logs_testing_hmm/`). To fill them from source: on EC2 run `.venv/bin/python cv_live_stats.py --json live_stats.json`, copy the file here and run `python -m lab.cv_stats --live live_stats.json`._

## CV-ready lines (built only from the numbers above)

- **s3v2e_core10 (live):** out-of-sample backtest 2025-01 to 2026-06 with taker fees and slippage: Sharpe 1.38, Sortino 2.00, CAGR +21.9%, max drawdown -12.0% (in-sample 2020-2024: Sharpe 1.00, max drawdown -16.8%).
- **HMM2 + CUSUM (forward test):** out-of-sample backtest 2025-01 to 2026-06 with taker fees and slippage: Sharpe 1.55, Sortino 2.27, CAGR +20.5%, max drawdown -8.1% (in-sample 2020-2024: Sharpe 1.04, max drawdown -17.5%).
