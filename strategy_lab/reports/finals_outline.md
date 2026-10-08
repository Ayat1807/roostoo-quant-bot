# Finals deck: storyline outline

**Audience:** the finals judges. They score risk-adjusted performance and look for a credible process and real-market robustness.
**Length:** about 12 slides and 10 minutes.
**Source of every number:** `reports/block6_summary.md`, `leaderboard_*.md` and the stats cards. Items marked **[FILL]** come from the live bots (`strategy_bot/daily_check.py`) on presentation day.

## 1. The problem (1 slide)
- **The task:** trade crypto on Roostoo for the competition window, autonomously, with one trade a day at minimum.
- **How finalists are chosen:** the top 20 by return, then the top 5 per region on a risk-adjusted composite (0.4 Sortino + 0.3 Sharpe + 0.3 Calmar).
- **What that rewards:** reliable profit with small drawdowns, including when the market falls, not the biggest bet.

## 2. Our process (1 slide)
- **One lab, one bot:** the lab backtests the exact strategy code the bot runs. Parity tests show identical targets (`strategy_bot/tests/`).
- **Realistic costs:** taker fees on every fill (0.10%), 2 bps slippage, shorts charged 0.10% on open AND close. A stress run adds 5 bps more.
- **Pre-registration:** every idea was declared in a variants file and committed before running; 520 trials in 12 blocks; the ledger is frozen.
- **Out-of-sample discipline:** judged on two halves (2020-02 to 2024-12 and 2025-01 to 2026-06). The Jul–Oct 2026 holdout was never used as a gate.
- **Fitted models:** expanding walk-forward with purging (HMM, LightGBM).
- **Luck threshold:** with 520 trials, the best result is expected to look about 2.9 standard errors too good. Margins are reported as t-statistics against it.

## 3. The objective changed, and we followed the evidence (1 slide)
- **Start:** we first optimised P(14-day return ≥ +10%) and launched xsmom (cross-sectional momentum) on 2026-10-06.
- **The review:** when the team adopted the risk-adjusted objective, the stats-card review showed xsmom failed it:
  - OOS Sharpe −0.79;
  - −3.2% mean 14-day return when BTC fell;
  - max drawdown −40%.
- **The switch:** on 2026-10-07 at 10:04 UTC we moved to s3v2e on core10, which meets every requirement in both halves. xsmom ended at −3.36%.
- **Message:** a documented, tested switch procedure; the old bot flattened itself through its KILL switch.

## 4. The live strategy: s3v2e on core10 (1 slide)
- **Signal:** the average sign of 1 / 3 / 7 / 14-day returns per coin, on 10 liquid coins.
- **Sizing:** EWMA vol targeting (7-day half-life). Shorts at half size in bull markets.
- **Trading:** daily targets with a 6pp band; average gross exposure about 20%.
- **Risk:** drawdown brake, liquidity guard, KILL switch, limit-then-market execution, no resend after a timeout.
- **Backtest stats card (OOS):**
  - Sharpe 1.38, Sortino 2.00, Calmar 1.83, composite 1.77;
  - max drawdown −12%, worst 14 days −5.2%;
  - +2.0% mean 14-day return in BTC-down windows;
  - fees 4.3% a year.

## 5. Making money when the market falls (1 slide)
- **The chart:** mean 14-day return by BTC regime (down / flat / up). s3v2e: +2.0% in down windows OOS, +0.6% in-sample. xsmom: −3.2% / −2.8%.
- **Broad down markets** (BTC down more than 5% and over 70% of coins down): s3v2e +1.9% OOS.
- **Why it works:** the trend signal goes short when coins fall, and the book is net short about 47% of the time OOS.

## 6. What we tested and rejected (2 slides, one table each)
| idea | best variant | verdict (vs the live strategy, both halves) |
|---|---|---|
| Event-day trading (CPI / FOMC) | refresh every 12h on event days | won by 1 window in-sample: noise (4 events) |
| Intraday exits (trend break, stops, trailing) | none | lower P(+10%) in both halves |
| Long/short momentum with intraday swaps | 4h checks, w 0.5 | in-sample P(+10%) 12% vs 15%; 0 of 7 neighbours pass |
| Entry timing (pullback, not-extended, patient limits) | — | misses big winners (69 OOS winners of +37% skipped) |
| Short-only books, beta hedge, breakdown shorts | slow short book | profitable in down windows, loses overall |
| Continuous t-stat signal | — | best in-sample, among the worst OOS (Sharpe 0.56) |
| HMM regime, changepoint cuts, ERC / HRP / Kelly | HMM2, CUSUM, ERC | reshape risk, no return gain (all |t| ≤ 1.5) |
| Universe screening ("trending" coins) | — | does not persist OOS (17% vs 19%) |
| LightGBM meta-labeling | — | AUC 0.52, no edge |
| Wider universes (top 15 / 20 / 30), exposure floor | — | more fees and exposure, lower Sharpe |

## 7. The near miss we are forward-testing (1 slide)
- **Candidate:** s3v2e + walk-forward 2-state HMM + CUSUM changepoint cut.
- **Backtest OOS:** Sharpe 1.55 vs 1.38, max drawdown −8.1% vs −12.0%, worst 14 days −3.7% vs −5.2%, same mean return. Not statistically distinguishable (t ≤ 0.7).
- **Status:** running on the testing key since **[FILL: start date]**. The switch criteria are clean operation and the same behaviour as the backtest, not short-term P&L.
- **Forward-test results:** **[FILL: days, errors, cuts fired, daily-return std vs the live bot]**.

## 8. Real-market robustness (1 slide)
- **Cost stress:** the backtests already assume taker fills. With 100% taker plus 7 bps slippage, s3v2e OOS is +31.2% vs +34.5%, and the worst 14 days −4.2%.
- **Live execution:** a limit order rests first (maker), then a market order covers the rest, so live costs are at or below the backtest's.
- **Operations:** heartbeat and status checks, restart-safe target restore, one account = one bot guard, every order logged with its full response.

## 9. Live results (1 slide)
- **xsmom:** 2026-10-06 15:30 to 2026-10-07 10:00 UTC, −3.36%.
- **s3v2e on core10:** from 2026-10-07 10:04 UTC: **[FILL: return, Sharpe-like daily stats, max drawdown, number of trades, active days]**.
- **Comparison:** the backtest expectation for a window of this length, from the stats card's 14-day distribution: median about −0.1%, 48% of windows positive.

## 10. Lessons (1 slide)
1. Pick the objective first; the best strategy changed when the objective changed.
2. Simple, stable signals on a fixed, liquid universe generalise best. Flexible signals and ML overfit or find no edge.
3. Count your trials: with 520 tries, most "improvements" are luck.
4. Risk overlays (regimes, changepoint cuts) reshape drawdowns rather than add return. That is still valuable under a risk-adjusted score.
5. Negative results are results: meta-labeling and universe screening failed in a documented way.

## 11. Future work (1 slide)
These need more time, data or compute than the competition allowed:
- **Deep Momentum Networks** (LSTM sizing trained on Sharpe) and temporal fusion transformers, with a long walk-forward on many more assets.
- **Order-book, funding-rate, open-interest and options-implied-vol features.** They need historical feeds that Roostoo doesn't provide.
- **Reinforcement-learning execution.**
- **Online Bayesian model averaging** of the trend, regime and allocation modules, with conformal position sizing.

## 12. Close (1 slide)
- **One line:** "A simple trend strategy, chosen by a pre-registered, cost-realistic, out-of-sample process; switched when the evidence said so; robust to execution costs; profitable when the market falls."
- **Appendix:** stats cards, the trial ledger, repo link.
