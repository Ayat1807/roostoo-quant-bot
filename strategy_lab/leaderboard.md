# strategy_lab leaderboard

_Generated 2026-10-05 06:55 UTC from runs/*/result.json. Declared trials: 33 (executed runs incl. re-runs: 43). Out-of-sample = 2025-01-01 -> 2026-10-05 (1.76 years)._

Ranked by **OOS rolling 14-day windows** (the competition horizon): median composite (0.4 Sortino + 0.3 Sharpe + 0.3 Calmar), then % of windows positive.

**How much is noise?** With 1.8 OOS years, one standard error of an annualised Sharpe is about **0.99**. The luck threshold for the best of 33 trials (DSR SR*) is about **2.26** annualised above zero. Differences smaller than these are not evidence.

| # | run | group | OOS ret | OOS Sharpe | OOS maxDD | IS Sharpe | full Sharpe | 14d med comp | 14d med ret | 14d % pos | 14d worst | 14/14 active | trades/day | fees/yr | corr s3v2 | DSR | flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | u_paxg_park | universe | +74.1% | 1.63 | -27.7% | 0.49 | 0.80 | 3.60 | +0.69% | 60% | -12.1% | 86% | 2.6 | 11.1% | 0.67 | 0.21 | DSR<0.95, noise vs guard_minimal, OOS>>IS, fails daily activity |
| 2 | hold_btc | bench | -9.7% | 0.09 | -53.7% | 1.01 | 0.83 | 0.46 | +0.15% | 52% | -29.1% | 0% | 0.0 | 0.0% | -0.10 | 0.00 | DSR<0.95, noise vs s3v2_base |
| 3 | u_roostoo65_div10 | universe | +10.1% | 1.12 | -4.7% | 0.71 | 0.73 | -0.70 | -0.04% | 47% | -4.2% | 100% | 2.2 | 5.4% | 0.59 | 0.07 | DSR<0.95, noise vs guard_minimal |
| 4 | hold_ew10 | bench | -37.9% | -0.22 | -65.6% | 1.35 | 1.02 | -0.76 | -0.95% | 47% | -31.2% | 0% | 0.0 | 0.1% | -0.06 | 0.00 | DSR<0.95, noise vs s3v2_base |
| 5 | p_brake_off | params | +37.8% | 1.09 | -18.2% | 1.12 | 1.11 | -1.03 | -0.17% | 46% | -9.6% | 100% | 2.2 | 4.8% | 0.88 | 0.06 | DSR<0.95, noise vs guard_minimal |
| 6 | p_tv08 | params | +16.5% | 0.43 | -28.2% | 0.55 | 0.52 | -1.13 | -0.59% | 44% | -15.4% | 80% | 4.2 | 11.5% | 0.83 | 0.01 | DSR<0.95, noise vs guard_minimal, fails daily activity |
| 7 | u_kadoo30_div10 | universe | +16.4% | 0.73 | -11.1% | 1.01 | 0.94 | -1.18 | -0.19% | 47% | -4.9% | 100% | 2.3 | 5.2% | 0.77 | 0.02 | DSR<0.95, noise vs guard_minimal |
| 8 | u_top30_div10 | universe | +11.8% | 0.66 | -9.8% | 0.93 | 0.86 | -1.28 | -0.24% | 43% | -3.7% | 100% | 2.3 | 5.2% | 0.72 | 0.02 | DSR<0.95, noise vs guard_minimal |
| 9 | guard_off | guard | +40.3% | 1.21 | -16.8% | 0.65 | 0.82 | -1.42 | -0.22% | 45% | -8.0% | 5% | 1.6 | 4.1% | 0.83 | 0.08 | DSR<0.95, fails daily activity |
| 10 | p_band08 | params | +27.6% | 1.26 | -10.1% | 1.27 | 1.27 | -1.42 | -0.16% | 45% | -5.6% | 100% | 1.6 | 3.0% | 0.80 | 0.10 | DSR<0.95, noise vs guard_minimal |
| 11 | guard_minimal | guard | +41.6% | 1.23 | -14.6% | 0.84 | 0.95 | -1.44 | -0.26% | 45% | -7.9% | 100% | 2.2 | 4.4% | 0.87 | 0.09 | DSR<0.95 |
| 12 | u_kadoo20_div10 | universe | +34.6% | 1.10 | -14.8% | 0.82 | 0.90 | -1.62 | -0.31% | 46% | -5.4% | 100% | 2.3 | 5.2% | 0.81 | 0.06 | DSR<0.95, noise vs guard_minimal |
| 13 | p_band04 | params | +21.2% | 0.62 | -21.4% | 0.90 | 0.82 | -1.67 | -0.44% | 42% | -9.7% | 98% | 3.6 | 6.5% | 0.90 | 0.02 | DSR<0.95, noise vs guard_minimal |
| 14 | u_top20_div10 | universe | +20.1% | 0.78 | -13.1% | 0.87 | 0.85 | -1.69 | -0.30% | 45% | -5.4% | 100% | 2.4 | 5.5% | 0.78 | 0.03 | DSR<0.95, noise vs guard_minimal |
| 15 | p_horizons_long | params | +34.6% | 1.03 | -12.0% | 1.36 | 1.28 | -1.71 | -0.30% | 43% | -5.8% | 98% | 1.7 | 3.1% | 0.82 | 0.05 | DSR<0.95, noise vs guard_minimal |
| 16 | u_roostoo65 | universe | +0.1% | 0.07 | -1.4% | 1.30 | 1.11 | -1.80 | -0.02% | 44% | -0.4% | 100% | 1.3 | 1.2% | 0.51 | 0.00 | DSR<0.95 |
| 17 | u_top10 | universe | +29.7% | 1.10 | -10.9% | 0.73 | 0.84 | -2.24 | -0.35% | 44% | -5.0% | 100% | 2.0 | 4.3% | 0.81 | 0.06 | DSR<0.95, noise vs guard_minimal |
| 18 | guard_band_edge | guard | +35.3% | 1.04 | -17.5% | 0.82 | 0.88 | -2.26 | -0.48% | 42% | -8.0% | 100% | 2.2 | 4.9% | 0.91 | 0.05 | DSR<0.95 |
| 19 | p_tv06 | params | +17.8% | 0.48 | -23.9% | 0.77 | 0.69 | -2.29 | -0.67% | 43% | -12.4% | 85% | 3.3 | 8.3% | 0.87 | 0.01 | DSR<0.95, noise vs guard_minimal, fails daily activity |
| 20 | u_top20_div10_band04 | universe | +1.1% | 0.14 | -24.1% | 0.75 | 0.59 | -2.77 | -0.92% | 40% | -10.4% | 98% | 4.5 | 8.2% | 0.81 | 0.00 | DSR<0.95 |
| 21 | u_kadoo20 | universe | +10.5% | 0.90 | -6.5% | 0.98 | 0.94 | -2.80 | -0.14% | 40% | -3.1% | 100% | 1.6 | 2.6% | 0.75 | 0.04 | DSR<0.95, noise vs guard_minimal |
| 22 | mft_breakout_top30_top3 | mft | -82.1% | -0.97 | -89.8% | -2.14 | -1.84 | -3.26 | -5.47% | 32% | -35.7% | 4% | 11.8 | 144.8% | 0.08 | 0.00 | DSR<0.95, OOS>>IS, fails daily activity |
| 23 | u_top20 | universe | +1.1% | 0.18 | -8.0% | 0.93 | 0.76 | -3.57 | -0.15% | 35% | -2.2% | 100% | 1.4 | 1.8% | 0.71 | 0.00 | DSR<0.95 |
| 24 | s3v2_base | guard | +2.4% | 0.17 | -20.5% | 1.04 | 0.81 | -3.83 | -0.99% | 36% | -8.7% | 91% | 4.0 | 6.1% |  | 0.00 | DSR<0.95 |
| 25 | u_kadoo30 | universe | +6.1% | 0.99 | -2.8% | 1.01 | 0.96 | -3.98 | -0.11% | 34% | -1.3% | 100% | 1.4 | 1.7% | 0.67 | 0.05 | DSR<0.95, noise vs guard_minimal |
| 26 | mft_breakout_top20_top3 | mft | -86.9% | -2.09 | -91.7% | -1.90 | -1.91 | -4.01 | -3.80% | 29% | -23.3% | 8% | 13.6 | 139.6% | 0.13 | 0.00 | DSR<0.95, fails daily activity |
| 27 | mft_s3v2_fast | mft | -20.9% | -0.80 | -35.2% | 0.46 | 0.12 | -4.69 | -1.03% | 33% | -5.3% | 100% | 7.8 | 19.6% | 0.57 | 0.00 | DSR<0.95 |
| 28 | p_shorts_off | params | +31.8% | 1.22 | -17.3% | 1.50 | 1.42 | -4.86 | -0.20% | 31% | -4.4% | 31% | 1.3 | 2.6% | 0.61 | 0.09 | DSR<0.95, noise vs guard_minimal, fails daily activity |
| 29 | mft_breakout_top20 | mft | -2.9% | -1.03 | -5.0% | -0.52 | -0.62 | -5.80 | -0.10% | 32% | -1.0% | 34% | 1.1 | 0.8% | 0.19 | 0.00 | DSR<0.95, fails daily activity |
| 30 | mft_breakout_10_top3 | mft | -84.7% | -2.34 | -88.0% | -0.70 | -1.04 | -5.92 | -4.92% | 20% | -17.0% | 11% | 11.6 | 100.4% | 0.23 | 0.00 | DSR<0.95, fails daily activity |
| 31 | mft_breakout_10 | mft | -1.3% | -0.54 | -2.1% | 0.89 | 0.62 | -6.02 | -0.08% | 31% | -0.6% | 4% | 1.0 | 0.7% | 0.27 | 0.00 | DSR<0.95, fails daily activity |
| 32 | mft_breakout_top30 | mft | -4.1% | -1.29 | -6.9% | -0.43 | -0.62 | -6.38 | -0.15% | 27% | -1.1% | 83% | 1.2 | 0.8% | 0.17 | 0.00 | DSR<0.95, fails daily activity |
| 33 | u_top30 | universe | -5.1% | -1.47 | -5.9% | 1.17 | 0.78 | -6.49 | -0.17% | 30% | -1.7% | 100% | 1.3 | 1.5% | 0.61 | 0.00 | DSR<0.95 |

## Recommended competition config (as of 2026-10-05; MFT trials added)

**Read this first: nothing here is statistically proven.** With 1.8 OOS years and 33 declared trials (26 + 7 MFT), no run passes the Deflated Sharpe test (DSR ≥ 0.95). One standard error of an annualised Sharpe is about 0.99 OOS and about 0.48 over the full 6.6 years. The recommendations below rest on **mechanism plus consistency across in-sample and OOS**, not on the top rank.

| setting | recommendation | evidence |
|---|---|---|
| strategy | **s3v2, parameters frozen** (horizons 24/72/168/336, target_vol 0.40, max_w 0.30, short_scale_bull 0.5) | Reproduces the reference (+20.5% on the reference OOS year). Higher target_vol (0.6 / 0.8) is worse in both halves, Sharpe 0.48 / 0.43 OOS. Long horizons (72–720) are better in-sample (1.36) but worse OOS (1.03), so no change. |
| activity guard | **`minimal`** (switch from `full`) | Same exposure path as no guard, every day active (100% of 14-day windows have 14/14 active days). Full-period Sharpe 0.95 vs 0.81, OOS 1.23 vs 0.17, max DD −20% vs −24%. The `full` guard re-sets all 10 pairs daily to a stale target, which adds about ±20pp/year of path variance (best in-sample, worst OOS). |
| shorts | **on** | Shorts off has a similar Sharpe but fails the daily-activity rule (only 31% of windows fully active) and has fewer positive 14-day windows (39% vs 45%). In the analogs to today, shorts on beat shorts off (+0.45% vs −0.04% mean over the next 14 days; 53% vs 33% positive). |
| drawdown brake | **keep on** (team decision; revisit with kadoo69's finding) | Brake off: full Sharpe 1.11 vs 0.95, OOS 1.09 vs 1.23. That is mixed and well within noise. |
| band | **0.06 (keep)**; 0.08 is the one promising tweak | Band 0.08: Sharpe 1.27 in-sample / 1.26 OOS / 1.27 full, max DD −12%. It is the only variant that improves both halves, but +0.32 Sharpe is under one standard error. Band 0.04 is worse in both halves. Adopt 0.08 only if the team accepts a within-noise change. |
| universe | **keep the 10 coins** | Top-N and Roostoo-65 universes are not better. With the divisor = N, wider universes dilute sizing (top30: OOS Sharpe −1.47, Roostoo-65: +0.1% OOS). Fixed divisor 10 recovers some (kadoo20_div10 OOS 1.10, full 0.90) but never beats the 10 coins in both halves. kadoo69's "rank all Binance, trade the Roostoo intersection" is the best wide variant, but it doesn't beat the 10 coins in both halves. |
| PAXG parking | **do not use** | Flagged OOS>>IS. The in-sample Sharpe (0.49) is worse than baseline (0.84); OOS +74% is gold's 2025–26 rally (gold beta, not skill). Its max DD (−30%) is worse. |
| coin picking by recent trendiness | **do not** | Per-coin trend Sharpe barely persists: rank correlation +0.23 (2022–24 → 2025–26) and +0.07 (→ Jun–Oct 2026). The mid-caps that trended in Jun–Oct 2026 (LTC, ARB, HBAR, SEI) were weak in 2022–24 (LTC −1.20). See reports/trend_capture.md. |

**What to expect over a 14-day competition window** (s3v2 + minimal guard, OOS): median −0.3%, 45% of windows positive, worst about −8%, worst in-window drawdown about −8.5%. S3v2 earns from occasional strong trends (bull Sharpe 2.45, shock days 3.11) and is flat in chop (48% of days). Conditional on today's market state (30 analogs), the mean next-14-day result is +0.45% (53% positive; worst −4.1%), while BTC was positive in only 37% of analogs (the team's 4h study: 32%).

**Known limitation of the minimal guard:** if the book is completely flat *and* every target is 0 (KILL, a hard brake stop, or shorts off with all-negative signals), there is no trade "toward target" to make, so that day stays inactive. The base config was 100% active, but shorts off / target_vol 0.6–0.8 had some such days. Team decision 2026-10-05: no artificial round trip; inactive days under KILL or a hard brake stop are acceptable. **Live since commit a4e5b43** (restart-safe targets since ecb3461): `activity_guard: minimal`, everything else frozen.

### MFT variants (30m bars): do not use

All run on 30m bars with targets recomputed every bar, the minimal guard and the brake on. Definitions were fixed in variants.yaml before running.

| run | full Sharpe | IS Sharpe | OOS return | OOS Sharpe | OOS max DD | 14d median / % positive | avg gross exposure | trades/day | fees/yr (% equity) |
|---|---|---|---|---|---|---|---|---|---|
| guard_minimal (live, 1h) | 0.95 | 0.84 | +41.6% | 1.23 | −14.6% | −0.26% / 45% | 0.19 | 2.2 | 4.4% |
| mft_s3v2_fast | 0.12 | 0.46 | −20.9% | −0.80 | −35.2% | −1.03% / 33% | 0.16 | 7.8 | 19.6% |
| mft_breakout_10_top3 | −1.04 | −0.70 | −84.7% | −2.34 | −88.0% | −4.92% / 20% | 0.40 | 11.6 | 100% |
| mft_breakout_top20_top3 | −1.91 | −1.90 | −86.9% | −2.09 | −91.7% | −3.80% / 29% | 0.46 | 13.6 | 140% |
| mft_breakout_top30_top3 | −1.84 | −2.14 | −82.1% | −0.97 | −89.8% | −5.47% / 32% | 0.55 | 11.8 | 145% |

- **s3v2_fast** (s3v2 with every window counted in 30m bars, so 12h–7d) churns: 4.5× the fees of the live config, and negative in both halves relative to it.
- **breakout_30m, team spec** (long-only Donchian: in above the 48h high, out below the 24h low; hold the top 3 in breakout state by 48h return, 1/3 each): it loses everything in every universe and both halves. This is not a bug. On average 3.6 coins are in breakout state and their 48h-return ranking flips constantly, so a new coin enters the top 3 about 5 times a day and each swap moves 33% of equity. That's about 840× equity turnover a year, and fees exceed equity annually.
  - A "sticky" variant (keep a holding until its own exit signal; fill empty slots by rank) would cut churn sharply. It is not tested: it would be a new declared trial.
- **Trial history:** trials 28–30 (3% vol sizing, band 0.06) barely traded. The first version of 31–33 (3% sizing, band 0.01) did not match the spec. It was replaced under the same trial numbers (runs/trials.json "corrections"; results in runs/_superseded/).
- **Engine check:** the 30m backtester matches the 1h one within 0.01pp with the brake off. With the brake on, checking it every 30m instead of hourly changed a 2.7-year s3v2 result from +38% to +82%. The drawdown brake is highly sensitive to when it is evaluated, which is worth knowing for the kadoo69 brake discussion.

