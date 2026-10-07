# Block 6: statistical and ML upgrades of s3v2e_core10 (the live competition strategy)

Judged under the team objective (lab/b5.py). The primary metrics are the median 14-day composite and the mean 14-day return. The requirements apply in both halves:
- the mean 14-day return is above 0 in DOWN windows (BTC −5% or worse over the window);
- P(14d ≤ −10%) is at most 5%;
- the worst 14-day window is no worse than −15%;
- OOS Sharpe is at least 1.

**Adoption** needs all of the requirements, plus a higher median composite AND a higher mean 14-day return than b3_s3v2e_core10, in both halves.

- **Data:** to 2026-06-30. IS is 2020-02-15 to 2024-12-31, OOS is 2025-01-01 to 2026-06-30, and Jul–Oct 2026 is informational only.
- **Trials:** 482 declared in total, so the luck threshold is about 2.9 standard errors.
- **Detailed tables:** `leaderboard_b6{a,b,c,d,e}.md`.
- **Stats card:** `reports/stats_card_b6_finalists.md` (the reference, ERC, HMM2 and the CUSUM cut).

## Verdict: nothing is adopted; s3v2e_core10 stays the reference (and the live strategy)

| track | best variant | OOS median 14d composite (reference −0.28) | IS median composite (reference −1.61) | OOS mean 14d (reference +0.8%) | meets all requirements | why it fails the adopt rule |
|---|---|---|---|---|---|---|
| A signal / turning points | CUSUM changepoint cut, threshold 4, cut to 50% | **+0.18** | −1.61 | +0.7% | yes | ties the reference in-sample; OOS mean 0.1pp lower |
| B regime | 2-state HMM (walk-forward) | −0.26 | **−1.29** | +0.8% | yes | composite better in both halves, but the mean 14-day return only ties |
| C allocation | equal risk contribution (ERC) | **+0.71** (best of all tracks) | −1.96 | +0.8% | yes | worse in-sample composite |
| E universe screening | trending top-10 | −1.05 | −1.73 | +0.2% | no (OOS Sharpe 0.29) | the screen does not persist OOS (17% vs 19%, reports/screen_track_e.md) |
| D meta-labeling | LightGBM, size = p | −3.84 | −1.56 | +0.1% | no (OOS Sharpe 0.34) | no predictive edge: walk-forward AUC 0.52 in both halves, OOS calibration fails |

**Down markets** (mean 14-day return when BTC is down more than 5%):

| | IS | OOS |
|---|---|---|
| reference | +0.6% | +2.0% |
| ERC | +1.4% | +2.4% |
| HMM2 | +0.6% | +2.1% |
| CUSUM cut | +0.6% | +1.9% |

All three finalists are profitable in down markets in both halves, and so is the reference.

## Notes per track
- **A:**
  - The continuous t-stat signal (A1) is the best in-sample result of the program (median composite +0.17) and one of the worst OOS (−2.00, Sharpe 0.56). That pattern is a regime change or an overfit, not an upgrade.
  - The EMA speed ensemble (A2) is weaker OOS.
  - Changepoint cuts help the risk profile: the CUSUM cut has the lowest OOS max drawdown (−8.4% vs −12.0%) and worst 14 days (−3.7% vs −5.2%). Its whole-period composite of 1.98 beats the reference's 1.77.
- **B:** the HMM probabilities are point-in-time: monthly expanding refit, 1-day embargo, filtered only.
  - HMM2 is the closest miss of the program: it beats the reference's composite in both halves, with OOS Sharpe 1.46 vs 1.38.
  - HMM3 and the correlation filter cut exposure at the wrong times.
- **C:**
  - ERC wins OOS but loses in-sample.
  - HRP is weaker in both halves.
  - Shrunk Kelly, the only fitted allocation (90-day regression, purged), is the worst. The fitted edge adds noise.
- **E:** screened coins are no more trending in the next 90 days than unscreened ones OOS. The rule picks small, changing universes, often only BTC plus 2–4 coins.
- **D:**
  - Feature importance is dominated by the correlation state (26% of gain). The trend t-stats and the changepoint score add little.
  - The probabilities are not monotone OOS: the top bin (p > 0.6) had the worst realised hit rate.
  - Bet sizing by p mostly shrinks exposure.

## Candidates for a follow-up (would need new pre-registered trials)
- **HMM2 combined with the CUSUM cut.** They improve different things (HMM2 the regime and in-sample composite, CUSUM the drawdowns and OOS composite). Their combination was not in the declared grid, so testing it is a new trial.
- **ERC with an in-sample check of why it lags in 2020–2024.** It may concentrate in low-vol coins during the 2021 alt rally.

## Ideas that need more time than the competition allows (finals presentation / post-competition)
- **Deep Momentum Networks** (Lim, Zohren, Roberts 2019): LSTM position sizing trained on Sharpe directly. It needs a GPU, hyper-parameter search inside a long walk-forward, and much more data than 10 coins × 6 years to avoid overfitting.
- **Temporal Fusion Transformer / attention models** for multi-horizon forecasts. Same constraints, plus interpretability work.
- **Reinforcement-learning execution** (limit placement, order splitting). It needs order-book history, and Roostoo provides none.
- **Market-structure features:** order book, funding rates, open interest, liquidations, options-implied vol (Deribit DVOL). These need historical data feeds that aren't in the lab.
- **Online / Bayesian model averaging** across the trend, regime and allocation modules, with conformal-prediction position sizing.
- **Hierarchical or multi-asset HMMs and BOCPD with a learned hazard rate**, validated on many more assets (top 50, 2017+).
