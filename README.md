# Roostoo quant trading hackathon: bot and research lab

A trend-following crypto trading bot for the Roostoo mock exchange, and the research lab used to choose, test and stress its strategy. Every strategy idea was pre-registered before it ran, judged on two halves of history (in-sample 2020-02 to 2024-12, out-of-sample 2025-01 to 2026-06), and checked against a luck threshold for the number of trials.

| folder | what it is |
|---|---|
| [`strategy_bot/`](strategy_bot) | the live bot: plug-in strategies, Roostoo client, risk controls, tests. Operation: [DEPLOY.md](strategy_bot/DEPLOY.md) |
| [`strategy_lab/`](strategy_lab) | offline research: hourly backtester with Roostoo costs, variants files (pre-registrations), reports, stats cards |
| `initial_testing/`, `pipeline_bot/` | early API tests and the first reference bot |
| `teammate_xsmom/` | a teammate's cross-sectional momentum strategy (live 2026-10-06 to 10-07, then retired) |

## Live strategy: s3v2e on core10
- **Signal:** multi-horizon trend. The average sign of 1, 3, 7 and 14-day returns per coin.
- **Sizing:** EWMA volatility targeting (7-day half-life), on 10 liquid coins: BTC, ETH, SOL, BNB, XRP, ADA, DOGE, AVAX, LINK, DOT.
- **Shorts:** allowed; half size while BTC is above its 14-day mean.
- **Trading:** targets daily at 00:00 UTC, with hourly band checks (6pp).
- **Risk:**
  - drawdown brake (−4% halves exposure, −7% goes flat for 24h);
  - liquidity guard;
  - minimal daily activity guard;
  - KILL switch;
  - limit orders first with a market fallback;
  - no resend after a timeout.
- **Config and evidence:** config `strategy_bot/config_competition_s3v2e.yaml`; stats card `strategy_lab/reports/stats_card_s3v2e_core10_competition.md`.

**Backtest** (OOS 2025-01 to 2026-06, costs: 0.10% taker and 2 bps slippage; shorts 0.10% on open and close):
- return +34.5%, Sharpe 1.38, Sortino 2.00, Calmar 1.83, composite 1.77, max drawdown −12.0%;
- worst 14 days −5.2%, and no 14-day window at −10% or worse;
- mean 14-day return in BTC-down windows +2.0%.

## Strategy history (competition key)
| period (UTC) | strategy | result | why it ended |
|---|---|---|---|
| 2026-10-06 15:30 to 2026-10-07 10:00 | xsmom on the R1 universe (long only, top 5 × 15%) | −3.36% | the stats-card review showed it failed the down-market and risk requirements (OOS Sharpe −0.79, −3.2% mean 14-day return in down windows) |
| 2026-10-07 10:04 to now | s3v2e on core10 | live | meets every requirement of the risk-adjusted objective in both halves |

A forward test of s3v2e + HMM2 regime + CUSUM changepoint cut runs on the testing key (plan: [forward_test_plan.md](strategy_lab/reports/forward_test_plan.md)).

## Research summary
- **Scale:** 520 pre-registered trials in 12 blocks; the ledger is frozen (`strategy_lab/runs/trials.json`). With that many trials, the best result is expected to look about 2.9 standard errors better than its true value. No variant beat the live strategy by more than |t| = 1.5.
- **Objective:** first P(14-day return ≥ +10%), then the team's risk-adjusted objective: median 14-day composite (0.4 Sortino + 0.3 Sharpe + 0.3 Calmar) and mean 14-day return, with positive returns in down markets.
- **Tested and rejected, with numbers:**
  - event-day trading (CPI, FOMC);
  - intraday exits;
  - a long/short xsmom;
  - entry timing;
  - position sizing;
  - short-only books;
  - continuous signals;
  - HMM regimes;
  - ERC, HRP and Kelly allocation;
  - universe screening;
  - LightGBM meta-labeling;
  - wider universes;
  - exposure floors.

  Details: [`strategy_lab/reports/block6_summary.md`](strategy_lab/reports/block6_summary.md), leaderboards `strategy_lab/leaderboard_*.md`.
- **Main lessons:**
  - simple, stable signals on a fixed liquid universe generalise best;
  - flexible signals and ML models overfit or find no edge (meta-labeling AUC 0.52);
  - risk overlays reshape drawdowns but do not add return.

## Real-market robustness
- **Execution cost stress:** each stats card re-runs the strategy with 100% taker fills and 7 bps slippage per fill. s3v2e_core10 OOS: +31.2% vs +34.5%, worst 14 days −4.2%. See also [strategy_bot/README.md](strategy_bot/README.md#real-market-robustness).
- **Parity tests:** the bot reproduces the lab's targets exactly (`strategy_bot/tests/`).

## How to run
- **Lab:** `cd strategy_lab && python -m lab.runner variants_<block>.yaml` (data cache: `python -m lab.data`), reports `python -m lab.b5` / `lab.b6` / `lab.b8`, stats card `python -m lab.stats_card <run>`.
- **Bot:** [strategy_bot/DEPLOY.md](strategy_bot/DEPLOY.md). Offline tests: `cd strategy_bot && python -m tests.test_safety` (and the other `tests/test_*.py`).
- **Keys:** keys live only in git-ignored `.env` files (templates: `.env.example`, `.env.competition.example`). Logs, state and caches are git-ignored too.
