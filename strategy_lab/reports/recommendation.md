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
