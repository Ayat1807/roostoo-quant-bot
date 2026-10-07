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

## Findings for the finals presentation (negative results are results)
1. **Meta-labeling found no edge on this data.**
   - **Setup:** LightGBM learns which s3v2e positions will be profitable over the next 3 days net of costs. It is trained walk-forward: expanding window, monthly steps, a 3-day purge, at least 6 months of training, and only out-of-sample predictions.
   - **Result:** AUC 0.52 in both halves (0.50 = coin flip). Out of sample, the confidence bins are not monotone: the most confident bin (p > 0.6) had the worst hit rate (40%) and a −1.9% average 3-day result.
   - **Effect on the strategy:** sizing by the predicted probability mostly shrinks exposure and cuts OOS Sharpe from 1.38 to 0.34.
   - **Lesson:** with 10 coins and about 18,800 position-days, the trend signal's residual is not predictable from standard features. Most of the model's "importance" sits in the market-wide correlation state, a regime proxy rather than a position-level signal.
2. **Trend screening does not persist out of sample.**
   - **Setup:** coins that look trending over the past 180 days (7-day variance ratio > 1 and positive daily autocorrelation).
   - **In-sample:** they are more likely to stay trending over the next 90 days (38% vs 29%).
   - **Out of sample (2025–2026):** the edge reverses (17% vs 19%).
   - **Effect on the strategy:** s3v2e on the screened universes drops to an OOS Sharpe of about 0.3–0.4, vs 1.38 on the fixed core10.
   - **Lesson:** a stable, liquid universe beats a statistically "trending" one that changes every month.
3. **More flexible signals overfit.** The continuous t-stat signal had the best in-sample composite of the whole program and one of the worst OOS. The simple sign-of-returns signal of s3v2e generalises better.
4. **What did help, but not enough to clear the bar:**
   - **Changepoint (CUSUM) cuts** lower drawdowns.
   - **The walk-forward 2-state HMM** improves the composite in both halves.
   - **Equal-risk-contribution allocation** gives the best OOS composite.

   None beats the reference on both primary metrics in both halves on its own. Block 7 tests their combinations (`leaderboard_b7.md`).
5. **Process:**
   - 482 trials were declared in total by block 6 (luck threshold about 2.9 standard errors); every track was pre-registered before it ran.
   - Every fitted model was validated walk-forward with purging.
   - The Jul–Oct 2026 holdout was never used as a gate.

## Block 7: combinations (variants_b7_combo.yaml, leaderboard_b7.md, reports/stats_card_b7_finalists.md)
**Not adopted.**
- **Pass/fail:** all four combinations fail the both-halves rule against s3v2e_core10.
- **Significance:** every margin is far inside the noise. The largest t is +1.33 (HMM2 + ERC, OOS median composite), against a luck threshold of 2.9 at 496 declared trials.
- **HMM2 + ERC:**
  - Best OOS median 14d composite of the whole research program: +1.18, vs −0.28 for the reference.
  - Down windows: +2.5% OOS, +1.4% IS.
  - It misses in-sample by 0.03 composite (−1.64 vs −1.61), and its mean 14d return ties.
- **HMM2 + CUSUM:**
  - Best whole-period OOS composite (2.13 vs 1.77).
  - OOS Sharpe 1.55, the lowest drawdown (−8.1%) and worst 14 days −3.7%.
  - Its mean 14d return is slightly lower than the reference's in both halves.

**Recommendation for the finals:** keep s3v2e_core10. The upgrades mainly reshape risk (smaller drawdowns, better risk-adjusted windows) rather than add return, and none of them is statistically distinguishable from the reference.

## s3v2e_core10 vs HMM2 + CUSUM in a market like now (secondary check, team request 2026-10-07)
**Analogs:** the 30 historical states nearest to 2026-10-04 (lab/analogs.py, outcomes to 2026-06-30). They are at least 14 days apart, 2021-04 to 2026-05, mostly 2023–2024.

| | s3v2e_core10 | HMM2 + CUSUM |
|---|---|---|
| analogs, 14d: mean / median / P(>0) / worst | +0.39% / −0.31% / 43% / −3.85% | +0.44% / −0.09% / 47% / −3.78% |
| analogs, 3d: mean / median / P(>0) / worst | −0.22% / −0.13% / 33% / −1.76% | −0.17% / −0.15% / 30% / −1.63% |
| all 3d windows IS: mean / median / P(>0) / worst | +0.13% / −0.05% / 43% / −4.00% | +0.11% / −0.05% / 43% / −4.02% |
| all 3d windows OOS: mean / median / P(>0) / worst | +0.17% / −0.07% / 43% / −3.69% | +0.16% / −0.05% / 42% / −3.12% |

Paired comparison in the analog windows (HMM2 + CUSUM minus s3v2e):
- **14 days:** +0.05pp on average, better in 57% of the 30 analogs (t +0.47).
- **3 days:** +0.06pp, better in 60% (t +2.18).

Both are below the luck threshold of 2.9, and this is a secondary metric chosen after the fact.

**Reading:** in markets like now both are close to flat over 14 days, and slightly negative over 3 days. HMM2 + CUSUM loses a little less in the bad analogs (it was better in most of the negative cases) and gives up some of the best ones: +7.3% vs +8.2%, +3.6% vs +5.0%. That is the same risk-reshaping pattern as on the full sample, too small to justify a switch.
