# Block 4b: Sizing, exposure, number of coins (live strategy xsmom on R1 = control)

_Generated 2026-10-07 11:02 UTC. Rules: `variants_b4b_sizing.yaml` (declared before any run). Data to 2026-06-30, both halves; Jul-Oct 2026 informational only._

**Trials:** 496 declared across all blocks; luck threshold about 2.9 standard errors.

**Adopted: `b4b_score`** (also passing: b4b_best_vol_target)

Not yet run: none

| run | group | IS P>=10% / P>=8% / P<=-10% / worst / median | OOS P>=10% / P>=8% / P<=-10% / worst / median | meets | beats control | fees/yr OOS | trades/day OOS | INFO P>=10% / median |
|---|---|---|---|---|---|---|---|---|
| b3_xsmom_r1 (control) |  | 15% / 18% / 3% / -19.1% / -0.9% | 9% / 11% / 2% / -12.0% / -2.5% | yes |  | 14.1% | 5.0 | 15% / -1.3% |
| b4b_score | sizing | 16% / 18% / 2% / -16.7% / -0.6% | 9% / 13% / 2% / -11.1% / -2.4% | yes | **yes** | 14.1% | 4.9 | 15% / -1.5% |
| b4b_inv_vol | sizing | 13% / 16% / 2% / -19.6% / -0.8% | 3% / 5% / 0% / -9.3% / -2.1% | yes | no | 16.2% | 5.3 | 15% / -1.0% |
| b4b_score_x_invvol | sizing | 15% / 18% / 2% / -18.2% / -0.6% | 2% / 4% / 1% / -11.4% / -1.9% | yes | no | 16.3% | 5.3 | 15% / -0.8% |
| b4b_score_cap25 | sizing | 16% / 18% / 2% / -17.1% / -0.7% | 9% / 12% / 2% / -11.1% / -2.3% | yes | no | 14.1% | 4.9 | 15% / -1.5% |
| b4b_inv_vol_cap25 | sizing | 13% / 16% / 1% / -15.9% / -0.6% | 2% / 4% / 1% / -11.4% / -2.4% | yes | no | 16.1% | 5.3 | 15% / -1.1% |
| b4b_score_x_invvol_cap25 | sizing | 15% / 18% / 2% / -17.6% / -0.8% | 3% / 7% / 0% / -11.1% / -2.1% | yes | no | 15.2% | 5.1 | 15% / -1.1% |
| b4b_score_cap20 | sizing | 16% / 19% / 2% / -18.6% / -0.8% | 9% / 10% / 2% / -12.7% / -2.4% | yes | no | 13.9% | 4.9 | 15% / -0.9% |
| b4b_inv_vol_cap20 | sizing | 13% / 16% / 1% / -19.8% / -0.6% | 4% / 7% / 1% / -11.4% / -2.3% | yes | no | 15.0% | 5.0 | 15% / -1.2% |
| b4b_score_x_invvol_cap20 | sizing | 15% / 18% / 2% / -17.5% / -0.8% | 4% / 7% / 1% / -11.1% / -2.8% | yes | no | 15.9% | 5.4 | 15% / -1.2% |
| b4b_live_breadth | exposure | 13% / 16% / 1% / -14.8% / -0.6% | 7% / 10% / 1% / -11.4% / -1.8% | yes | no | 10.9% | 4.6 | 15% / -1.3% |
| b4b_live_vol_target | exposure | 15% / 19% / 1% / -11.6% / -0.4% | 8% / 12% / 2% / -12.4% / -2.3% | yes | no | 16.4% | 4.7 | 15% / +0.5% |
| b4b_live_regime | exposure | 14% / 16% / 4% / -22.0% / -1.2% | 5% / 8% / 2% / -12.9% / -2.3% | **no** | no | 15.3% | 5.4 | 15% / -1.2% |
| b4b_live_conviction | exposure | 13% / 16% / 2% / -18.6% / -1.0% | 6% / 9% / 0% / -12.9% / -3.0% | yes | no | 15.8% | 5.5 | 16% / -0.5% |
| b4b_top3 | coins | 17% / 21% / 6% / -18.5% / -0.5% | 8% / 13% / 7% / -13.1% / -3.0% | yes | no | 17.8% | 3.7 | 15% / -2.7% |
| b4b_top7 | coins | 12% / 15% / 1% / -20.4% / -0.6% | 5% / 8% / 1% / -12.6% / -2.3% | **no** | no | 12.0% | 6.1 | 15% / -0.6% |
| b4b_top10 | coins | 9% / 12% / 0% / -11.3% / -0.5% | 2% / 6% / 1% / -11.7% / -2.0% | yes | no | 9.6% | 7.2 | 16% / -0.4% |
| b4b_top7_g90 | coins | 12% / 15% / 3% / -17.1% / -1.1% | 9% / 12% / 2% / -13.2% / -3.2% | yes | no | 15.6% | 6.4 | 16% / -1.1% |
| b4b_top10_g90 | coins | 9% / 14% / 1% / -17.3% / -0.7% | 7% / 10% / 1% / -12.0% / -2.5% | yes | no | 11.2% | 7.1 | 21% / -0.5% |
| b4b_all_elig_cap15 | coins | 13% / 16% / 2% / -18.8% / -0.8% | 5% / 7% / 1% / -11.7% / -2.9% | yes | no | 14.5% | 8.2 | 22% / -1.2% |
| b4b_all_elig_cap10 | coins | 10% / 13% / 1% / -15.9% / -0.5% | 4% / 7% / 2% / -12.7% / -2.5% | yes | no | 12.0% | 8.4 | 16% / -0.5% |
| b4b_breadth_k | coins | 14% / 17% / 3% / -18.5% / -0.8% | 6% / 10% / 2% / -12.2% / -2.7% | yes | no | 16.0% | 6.6 | 26% / -0.6% |
| b4b_best_breadth | exposure_best | 14% / 15% / 1% / -15.3% / -0.6% | 9% / 11% / 1% / -12.7% / -1.8% | yes | no | 11.2% | 4.7 | 15% / -1.6% |
| b4b_best_vol_target | exposure_best | 15% / 20% / 1% / -12.7% / +0.0% | 9% / 11% / 4% / -11.4% / -2.4% | yes | **yes** | 16.0% | 4.7 | 15% / +0.4% |
| b4b_best_regime | exposure_best | 15% / 17% / 3% / -22.2% / -1.0% | 9% / 10% / 1% / -14.7% / -2.0% | **no** | no | 15.8% | 5.4 | 16% / -1.4% |
| b4b_best_conviction | exposure_best | 13% / 15% / 3% / -19.1% / -1.1% | 8% / 10% / 1% / -13.5% / -2.9% | yes | no | 15.5% | 5.4 | 16% / -2.3% |
| b4s_b4b_score_r1h | sweep | 11% / 13% / 3% / -18.6% / -2.2% | 4% / 5% / 3% / -12.2% / -3.7% | yes | no | 54.9% | 58.1 | 15% / -3.5% |
| b4s_b4b_score_r2h | sweep | 13% / 16% / 3% / -15.1% / -1.3% | 7% / 10% / 4% / -12.5% / -3.2% | yes | no | 40.8% | 31.5 | 15% / -1.7% |
| b4s_b4b_score_r4h | sweep | 15% / 18% / 3% / -16.1% / -0.7% | 8% / 9% / 2% / -12.5% / -2.3% | yes | no | 30.0% | 17.7 | 15% / -1.6% |
| b4s_b4b_score_r6h | sweep | 14% / 17% / 2% / -16.8% / -0.7% | 11% / 13% / 2% / -12.1% / -2.3% | yes | no | 24.6% | 12.6 | 15% / -0.3% |
| b4s_b4b_score_r12h | sweep | 14% / 17% / 2% / -18.4% / -0.9% | 10% / 12% / 1% / -11.2% / -2.4% | yes | no | 19.4% | 8.0 | 16% / -1.2% |
| b4s_b4b_top7_g90_r1h | sweep | 9% / 12% / 3% / -19.6% / -1.8% | 4% / 5% / 5% / -13.4% / -3.8% | yes | no | 48.8% | 63.5 | 27% / -2.9% |
| b4s_b4b_top7_g90_r2h | sweep | 11% / 14% / 3% / -19.8% / -1.3% | 7% / 9% / 3% / -13.6% / -3.6% | yes | no | 36.9% | 37.5 | 15% / -1.1% |
| b4s_b4b_top7_g90_r4h | sweep | 12% / 16% / 2% / -16.3% / -0.7% | 8% / 10% / 4% / -13.6% / -3.2% | yes | no | 28.3% | 21.5 | 16% / -1.9% |
| b4s_b4b_top7_g90_r6h | sweep | 12% / 15% / 3% / -16.5% / -0.7% | 9% / 11% / 5% / -14.1% / -3.2% | yes | no | 24.3% | 15.6 | 16% / -0.4% |
| b4s_b4b_top7_g90_r12h | sweep | 12% / 15% / 3% / -19.2% / -1.1% | 11% / 11% / 3% / -12.4% / -3.0% | yes | no | 18.9% | 9.5 | 16% / -1.1% |

## Concentration

| run | period | avg coins held | max coin weight | worst single-coin contribution in the 5 worst 14d windows |
|---|---|---|---|---|
| b4b_score | IS | 2.5 | 54% | SOLUSDT -5.4% (window from 2021-05-06) |
| b4b_score | OOS | 2.3 | 40% | WIFUSDT -3.7% (window from 2025-05-14) |
| b4b_score | INFO | 2.6 | 31% | PUMPUSDT -1.6% (window from 2026-09-19) |
| b4b_inv_vol | IS | 2.6 | 48% | XRPUSDT -4.0% (window from 2021-05-09) |
| b4b_inv_vol | OOS | 2.3 | 44% | LINKUSDT -2.2% (window from 2026-03-13) |
| b4b_inv_vol | INFO | 2.6 | 50% | PUMPUSDT -1.4% (window from 2026-09-19) |
| b4b_score_x_invvol | IS | 2.5 | 52% | XRPUSDT -5.8% (window from 2024-12-03) |
| b4b_score_x_invvol | OOS | 2.3 | 55% | WIFUSDT -2.9% (window from 2025-02-15) |
| b4b_score_x_invvol | INFO | 2.6 | 63% | PUMPUSDT -2.4% (window from 2026-08-29) |
| b4b_score_cap25 | IS | 2.5 | 34% | SOLUSDT -5.2% (window from 2021-05-06) |
| b4b_score_cap25 | OOS | 2.2 | 31% | HBARUSDT -3.3% (window from 2025-03-03) |
| b4b_score_cap25 | INFO | 2.6 | 26% | PUMPUSDT -1.9% (window from 2026-09-19) |
| b4b_inv_vol_cap25 | IS | 2.6 | 28% | XRPUSDT -4.3% (window from 2021-05-16) |
| b4b_inv_vol_cap25 | OOS | 2.3 | 27% | WIFUSDT -2.4% (window from 2025-02-21) |
| b4b_inv_vol_cap25 | INFO | 2.6 | 26% | PUMPUSDT -1.3% (window from 2026-09-19) |
| b4b_score_x_invvol_cap25 | IS | 2.5 | 30% | SOLUSDT -4.9% (window from 2021-05-07) |
| b4b_score_x_invvol_cap25 | OOS | 2.2 | 26% | WIFUSDT -2.5% (window from 2025-02-13) |
| b4b_score_x_invvol_cap25 | INFO | 2.6 | 26% | PUMPUSDT -1.6% (window from 2026-09-19) |
| b4b_score_cap20 | IS | 2.5 | 32% | SOLUSDT -4.6% (window from 2021-05-10) |
| b4b_score_cap20 | OOS | 2.3 | 25% | WIFUSDT -3.9% (window from 2025-05-13) |
| b4b_score_cap20 | INFO | 2.6 | 21% | ZECUSDT -1.5% (window from 2026-08-05) |
| b4b_inv_vol_cap20 | IS | 2.5 | 24% | XRPUSDT -4.0% (window from 2021-05-09) |
| b4b_inv_vol_cap20 | OOS | 2.2 | 22% | WIFUSDT -2.7% (window from 2025-02-13) |
| b4b_inv_vol_cap20 | INFO | 2.6 | 22% | SUIUSDT -1.6% (window from 2026-09-01) |
| b4b_score_x_invvol_cap20 | IS | 2.5 | 27% | SOLUSDT -4.4% (window from 2021-05-06) |
| b4b_score_x_invvol_cap20 | OOS | 2.2 | 22% | SUIUSDT -2.5% (window from 2025-03-28) |
| b4b_score_x_invvol_cap20 | INFO | 2.6 | 22% | PUMPUSDT -2.2% (window from 2026-08-29) |
| b4b_live_breadth | IS | 2.6 | 25% | BNBUSDT -2.5% (window from 2021-06-04) |
| b4b_live_breadth | OOS | 2.3 | 19% | WIFUSDT -2.3% (window from 2025-02-21) |
| b4b_live_breadth | INFO | 2.7 | 17% | SUIUSDT -1.3% (window from 2026-08-31) |
| b4b_live_vol_target | IS | 2.6 | 90% | NEARUSDT -3.8% (window from 2022-04-08) |
| b4b_live_vol_target | OOS | 2.3 | 90% | SUIUSDT -4.3% (window from 2025-03-28) |
| b4b_live_vol_target | INFO | 2.6 | 68% | ADAUSDT -2.6% (window from 2026-07-17) |
| b4b_live_regime | IS | 2.5 | 28% | PEPEUSDT -7.7% (window from 2024-03-05) |
| b4b_live_regime | OOS | 2.2 | 23% | WIFUSDT -4.0% (window from 2025-05-13) |
| b4b_live_regime | INFO | 2.6 | 21% | DOGEUSDT -1.8% (window from 2026-09-19) |
| b4b_live_conviction | IS | 2.5 | 28% | PEPEUSDT -4.2% (window from 2024-11-13) |
| b4b_live_conviction | OOS | 2.2 | 22% | HBARUSDT -2.8% (window from 2025-03-03) |
| b4b_live_conviction | INFO | 2.6 | 21% | DOGEUSDT -2.0% (window from 2026-09-19) |
| b4b_top3 | IS | 1.7 | 37% | AVAXUSDT -5.7% (window from 2024-03-14) |
| b4b_top3 | OOS | 1.5 | 31% | WIFUSDT -5.4% (window from 2025-05-13) |
| b4b_top3 | INFO | 1.9 | 27% | SUIUSDT -2.8% (window from 2026-09-20) |
| b4b_top7 | IS | 3.2 | 18% | DOGEUSDT -3.6% (window from 2021-05-06) |
| b4b_top7 | OOS | 2.8 | 14% | HBARUSDT -3.0% (window from 2025-03-03) |
| b4b_top7 | INFO | 3.1 | 13% | ADAUSDT -0.9% (window from 2026-07-05) |
| b4b_top10 | IS | 3.8 | 18% | PEPEUSDT -4.2% (window from 2024-03-05) |
| b4b_top10 | OOS | 3.4 | 10% | HBARUSDT -2.1% (window from 2025-03-03) |
| b4b_top10 | INFO | 3.7 | 9% | NEARUSDT -0.8% (window from 2026-07-16) |
| b4b_top7_g90 | IS | 3.1 | 21% | PEPEUSDT -4.2% (window from 2024-03-05) |
| b4b_top7_g90 | OOS | 2.7 | 17% | HBARUSDT -3.5% (window from 2025-03-03) |
| b4b_top7_g90 | INFO | 3.1 | 15% | ADAUSDT -1.0% (window from 2026-07-05) |
| b4b_top10_g90 | IS | 3.7 | 15% | DOGEUSDT -3.6% (window from 2021-05-08) |
| b4b_top10_g90 | OOS | 3.3 | 12% | HBARUSDT -2.5% (window from 2025-03-03) |
| b4b_top10_g90 | INFO | 3.6 | 11% | NEARUSDT -0.9% (window from 2026-07-16) |
| b4b_all_elig_cap15 | IS | 4.2 | 19% | DOGEUSDT -3.5% (window from 2021-05-08) |
| b4b_all_elig_cap15 | OOS | 3.7 | 19% | ENAUSDT -3.2% (window from 2025-05-23) |
| b4b_all_elig_cap15 | INFO | 4.1 | 17% | ZECUSDT -1.2% (window from 2026-08-05) |
| b4b_all_elig_cap10 | IS | 4.2 | 14% | PEPEUSDT -4.3% (window from 2024-03-05) |
| b4b_all_elig_cap10 | OOS | 3.7 | 13% | HBARUSDT -2.4% (window from 2025-03-03) |
| b4b_all_elig_cap10 | INFO | 4.2 | 11% | NEARUSDT -0.9% (window from 2026-07-16) |
| b4b_breadth_k | IS | 3.3 | 31% | SOLUSDT -4.5% (window from 2021-06-04) |
| b4b_breadth_k | OOS | 2.9 | 31% | LTCUSDT -2.9% (window from 2025-02-15) |
| b4b_breadth_k | INFO | 3.3 | 27% | ENAUSDT -3.0% (window from 2026-09-01) |
| b4b_best_breadth | IS | 2.6 | 52% | BNBUSDT -5.1% (window from 2021-02-20) |
| b4b_best_breadth | OOS | 2.3 | 32% | WIFUSDT -2.5% (window from 2025-03-03) |
| b4b_best_breadth | INFO | 2.7 | 27% | XPLUSDT -1.2% (window from 2026-07-04) |
| b4b_best_vol_target | IS | 2.6 | 90% | DOGEUSDT -5.1% (window from 2024-01-10) |
| b4b_best_vol_target | OOS | 2.3 | 90% | TRXUSDT -4.1% (window from 2025-03-28) |
| b4b_best_vol_target | INFO | 2.6 | 63% | ADAUSDT -2.5% (window from 2026-07-18) |
| b4b_best_regime | IS | 2.5 | 65% | XRPUSDT -6.9% (window from 2024-12-02) |
| b4b_best_regime | OOS | 2.2 | 48% | WIFUSDT -5.4% (window from 2025-05-13) |
| b4b_best_regime | INFO | 2.6 | 37% | DOGEUSDT -1.8% (window from 2026-09-19) |
| b4b_best_conviction | IS | 2.5 | 65% | XRPUSDT -6.3% (window from 2024-12-02) |
| b4b_best_conviction | OOS | 2.2 | 36% | HBARUSDT -3.6% (window from 2025-03-03) |
| b4b_best_conviction | INFO | 2.6 | 33% | DOGEUSDT -1.9% (window from 2026-09-19) |
| b4s_b4b_score_r1h | IS | 2.5 | 58% | XRPUSDT -4.3% (window from 2024-12-03) |
| b4s_b4b_score_r1h | OOS | 2.2 | 40% | DOGEUSDT -2.4% (window from 2025-05-11) |
| b4s_b4b_score_r1h | INFO | 2.6 | 41% | ZECUSDT -1.3% (window from 2026-07-16) |
| b4s_b4b_score_r2h | IS | 2.5 | 55% | XRPUSDT -3.7% (window from 2024-12-03) |
| b4s_b4b_score_r2h | OOS | 2.2 | 42% | HBARUSDT -2.4% (window from 2025-03-03) |
| b4s_b4b_score_r2h | INFO | 2.7 | 40% | WLDUSDT -1.7% (window from 2026-07-13) |
| b4s_b4b_score_r4h | IS | 2.5 | 54% | WLDUSDT -3.9% (window from 2024-03-10) |
| b4s_b4b_score_r4h | OOS | 2.2 | 39% | WIFUSDT -2.4% (window from 2025-02-13) |
| b4s_b4b_score_r4h | INFO | 2.7 | 40% | WLDUSDT -1.8% (window from 2026-07-13) |
| b4s_b4b_score_r6h | IS | 2.5 | 54% | PEPEUSDT -6.1% (window from 2024-11-13) |
| b4s_b4b_score_r6h | OOS | 2.2 | 40% | HBARUSDT -2.7% (window from 2025-03-03) |
| b4s_b4b_score_r6h | INFO | 2.7 | 39% | WLDUSDT -1.2% (window from 2026-07-13) |
| b4s_b4b_score_r12h | IS | 2.5 | 54% | PEPEUSDT -6.0% (window from 2024-11-13) |
| b4s_b4b_score_r12h | OOS | 2.3 | 40% | HBARUSDT -2.5% (window from 2025-03-03) |
| b4s_b4b_score_r12h | INFO | 2.7 | 39% | XPLUSDT -1.5% (window from 2026-09-18) |
| b4s_b4b_top7_g90_r1h | IS | 3.1 | 13% | PEPEUSDT -4.7% (window from 2024-11-12) |
| b4s_b4b_top7_g90_r1h | OOS | 2.8 | 13% | XRPUSDT -2.4% (window from 2025-02-21) |
| b4s_b4b_top7_g90_r1h | INFO | 3.1 | 13% | XPLUSDT -1.6% (window from 2026-07-04) |
| b4s_b4b_top7_g90_r2h | IS | 3.1 | 16% | XLMUSDT -4.8% (window from 2021-05-06) |
| b4s_b4b_top7_g90_r2h | OOS | 2.8 | 14% | HBARUSDT -2.7% (window from 2025-03-03) |
| b4s_b4b_top7_g90_r2h | INFO | 3.1 | 14% | XPLUSDT -1.7% (window from 2026-07-04) |
| b4s_b4b_top7_g90_r4h | IS | 3.1 | 17% | XLMUSDT -3.4% (window from 2021-05-06) |
| b4s_b4b_top7_g90_r4h | OOS | 2.8 | 15% | HBARUSDT -2.7% (window from 2025-03-03) |
| b4s_b4b_top7_g90_r4h | INFO | 3.1 | 14% | XPLUSDT -1.8% (window from 2026-09-02) |
| b4s_b4b_top7_g90_r6h | IS | 3.1 | 16% | WLDUSDT -3.0% (window from 2024-03-10) |
| b4s_b4b_top7_g90_r6h | OOS | 2.7 | 15% | PEPEUSDT -3.0% (window from 2025-05-11) |
| b4s_b4b_top7_g90_r6h | INFO | 3.1 | 14% | AAVEUSDT -1.7% (window from 2026-08-22) |
| b4s_b4b_top7_g90_r12h | IS | 3.1 | 19% | AVAXUSDT -3.6% (window from 2021-05-07) |
| b4s_b4b_top7_g90_r12h | OOS | 2.8 | 15% | LINKUSDT -2.2% (window from 2026-02-21) |
| b4s_b4b_top7_g90_r12h | INFO | 3.1 | 15% | XPLUSDT -1.5% (window from 2026-07-04) |
