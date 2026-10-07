# Block 4d: Entry timing (live strategy xsmom on R1 = control)

_Generated 2026-10-07 10:10 UTC. Rules: `variants_b4d_entry.yaml` (declared before any run). Data to 2026-06-30, both halves; Jul-Oct 2026 informational only._

**Trials:** 408 declared across all blocks; luck threshold about 2.8 standard errors.

**Adopted: none**

Not yet run: none

| run | group | IS P>=10% / P>=8% / P<=-10% / worst / median | OOS P>=10% / P>=8% / P<=-10% / worst / median | meets | beats control | fees/yr OOS | trades/day OOS | INFO P>=10% / median |
|---|---|---|---|---|---|---|---|---|
| b3_xsmom_r1 (control) |  | 15% / 18% / 3% / -19.1% / -0.9% | 9% / 11% / 2% / -12.0% / -2.5% | yes |  | 14.1% | 5.0 | 15% / -1.3% |
| b4d_pullback | entry | 8% / 10% / 1% / -14.1% / -1.0% | 2% / 2% / 0% / -8.5% / -2.2% | yes | no | 8.5% | 2.8 | 2% / -0.6% |
| b4d_not_ext6 | entry | 9% / 11% / 0% / -8.3% / -0.6% | 2% / 4% / 0% / -7.5% / -1.6% | yes | no | 8.9% | 3.0 | 17% / -0.5% |
| b4d_not_ext10 | entry | 10% / 13% / 0% / -9.6% / -1.1% | 6% / 9% / 0% / -11.7% / -2.5% | yes | no | 12.5% | 4.3 | 15% / -0.3% |
| b4d_resistance | entry | 14% / 18% / 2% / -19.1% / -0.9% | 9% / 12% / 2% / -12.0% / -2.5% | yes | no | 13.9% | 4.9 | 15% / -1.5% |
| b4d_patient_limit | entry | 13% / 16% / 2% / -18.8% / -0.6% | 3% / 4% / 1% / -11.8% / -3.0% | yes | no | 10.4% | 4.4 | 0% / -0.7% |
| b4s_b4d_resistance_r1h | sweep | 10% / 12% / 3% / -21.1% / -1.8% | 3% / 5% / 3% / -13.0% / -3.5% | **no** | no | 49.9% | 55.2 | 15% / -2.5% |
| b4s_b4d_resistance_r2h | sweep | 12% / 15% / 3% / -18.7% / -1.3% | 6% / 8% / 4% / -12.9% / -3.1% | yes | no | 38.1% | 30.9 | 16% / -0.7% |
| b4s_b4d_resistance_r4h | sweep | 13% / 17% / 3% / -16.3% / -0.7% | 6% / 7% / 2% / -12.2% / -2.7% | yes | no | 29.2% | 17.8 | 15% / -0.2% |
| b4s_b4d_resistance_r6h | sweep | 13% / 17% / 3% / -15.3% / -0.7% | 9% / 12% / 3% / -12.3% / -2.4% | yes | no | 23.0% | 12.5 | 15% / -0.2% |
| b4s_b4d_resistance_r12h | sweep | 12% / 15% / 3% / -18.5% / -0.9% | 6% / 10% / 2% / -11.8% / -2.7% | yes | no | 18.6% | 8.0 | 20% / -0.3% |
| b4s_b4d_not_ext10_r1h | sweep | 8% / 11% / 1% / -11.5% / -1.7% | 4% / 7% / 2% / -11.7% / -2.8% | yes | no | 44.3% | 50.4 | 15% / -1.0% |
| b4s_b4d_not_ext10_r2h | sweep | 8% / 12% / 0% / -11.2% / -1.2% | 4% / 6% / 1% / -10.9% / -2.8% | yes | no | 33.4% | 28.0 | 15% / -1.0% |
| b4s_b4d_not_ext10_r4h | sweep | 11% / 14% / 0% / -10.5% / -0.8% | 5% / 6% / 0% / -9.9% / -2.4% | yes | no | 25.1% | 15.8 | 15% / +0.7% |
| b4s_b4d_not_ext10_r6h | sweep | 9% / 13% / 0% / -10.8% / -0.9% | 8% / 10% / 0% / -9.7% / -2.3% | yes | no | 21.0% | 11.3 | 15% / -0.6% |
| b4s_b4d_not_ext10_r12h | sweep | 8% / 11% / 1% / -17.0% / -1.2% | 7% / 10% / 0% / -10.0% / -2.0% | yes | no | 16.2% | 6.9 | 15% / +0.2% |

## Entries

Entry vs 3-day high = entry close / highest close of the previous 72h - 1 (mean over new entries). Missed = control entries that rose >= +20% within 14 days which the variant did not hold in the next 24h.

| run | period | new entries | entry vs 3d high | big winners missed (mean gain) | limit fill rate |
|---|---|---|---|---|---|
| b4d__control | IS | 2110 | -2.0% | 0 () |  |
| b4d__control | OOS | 637 | -1.7% | 0 () |  |
| b4d__control | INFO | 124 | -0.8% | 0 () |  |
| b4d_pullback | IS | 1363 | -5.0% | 405 (+47.0%) |  |
| b4d_pullback | OOS | 394 | -4.6% | 62 (+33.9%) |  |
| b4d_pullback | INFO | 71 | -4.2% | 26 (+40.9%) |  |
| b4d_not_ext6 | IS | 1166 | -2.9% | 456 (+47.8%) |  |
| b4d_not_ext6 | OOS | 441 | -2.5% | 69 (+37.0%) |  |
| b4d_not_ext6 | INFO | 89 | -2.4% | 17 (+45.9%) |  |
| b4d_not_ext10 | IS | 1776 | -2.7% | 296 (+49.0%) |  |
| b4d_not_ext10 | OOS | 572 | -2.2% | 41 (+34.5%) |  |
| b4d_not_ext10 | INFO | 106 | -1.6% | 8 (+38.1%) |  |
| b4d_resistance | IS | 2116 | -2.0% | 3 (+47.7%) |  |
| b4d_resistance | OOS | 640 | -1.8% | 0 () |  |
| b4d_resistance | INFO | 122 | -0.8% | 0 () |  |
| b4d_patient_limit | IS | 1991 | -3.3% | 137 (+44.7%) | 79% of 3377 (whole run) |
| b4d_patient_limit | OOS | 581 | -3.0% | 31 (+38.0%) |  |
| b4d_patient_limit | INFO | 109 | -2.0% | 10 (+40.3%) |  |
| b4s_b4d_resistance_r1h | IS | 9522 | -2.0% | 9 (+50.2%) |  |
| b4s_b4d_resistance_r1h | OOS | 3020 | -1.6% | 0 () |  |
| b4s_b4d_resistance_r1h | INFO | 628 | -1.7% | 0 () |  |
| b4s_b4d_resistance_r2h | IS | 6695 | -1.8% | 8 (+37.2%) |  |
| b4s_b4d_resistance_r2h | OOS | 2105 | -1.5% | 5 (+38.6%) |  |
| b4s_b4d_resistance_r2h | INFO | 448 | -1.6% | 0 () |  |
| b4s_b4d_resistance_r4h | IS | 4719 | -1.8% | 9 (+38.5%) |  |
| b4s_b4d_resistance_r4h | OOS | 1522 | -1.4% | 4 (+34.7%) |  |
| b4s_b4d_resistance_r4h | INFO | 303 | -1.4% | 0 () |  |
| b4s_b4d_resistance_r6h | IS | 3952 | -1.7% | 9 (+36.0%) |  |
| b4s_b4d_resistance_r6h | OOS | 1206 | -1.4% | 2 (+43.6%) |  |
| b4s_b4d_resistance_r6h | INFO | 249 | -1.4% | 0 () |  |
| b4s_b4d_resistance_r12h | IS | 2869 | -1.7% | 7 (+31.4%) |  |
| b4s_b4d_resistance_r12h | OOS | 887 | -1.5% | 1 (+58.0%) |  |
| b4s_b4d_resistance_r12h | INFO | 172 | -1.2% | 0 () |  |
| b4s_b4d_not_ext10_r1h | IS | 8309 | -2.7% | 192 (+50.1%) |  |
| b4s_b4d_not_ext10_r1h | OOS | 2630 | -2.1% | 27 (+38.0%) |  |
| b4s_b4d_not_ext10_r1h | INFO | 541 | -2.2% | 6 (+37.8%) |  |
| b4s_b4d_not_ext10_r2h | IS | 5847 | -2.7% | 196 (+50.0%) |  |
| b4s_b4d_not_ext10_r2h | OOS | 1888 | -2.1% | 27 (+37.4%) |  |
| b4s_b4d_not_ext10_r2h | INFO | 379 | -2.1% | 7 (+40.8%) |  |
| b4s_b4d_not_ext10_r4h | IS | 4210 | -2.7% | 218 (+49.6%) |  |
| b4s_b4d_not_ext10_r4h | OOS | 1374 | -2.0% | 30 (+36.4%) |  |
| b4s_b4d_not_ext10_r4h | INFO | 261 | -1.9% | 9 (+39.4%) |  |
| b4s_b4d_not_ext10_r6h | IS | 3559 | -2.6% | 234 (+48.4%) |  |
| b4s_b4d_not_ext10_r6h | OOS | 1143 | -2.1% | 34 (+35.7%) |  |
| b4s_b4d_not_ext10_r6h | INFO | 217 | -2.2% | 8 (+38.4%) |  |
| b4s_b4d_not_ext10_r12h | IS | 2505 | -2.6% | 274 (+49.2%) |  |
| b4s_b4d_not_ext10_r12h | OOS | 807 | -2.2% | 38 (+34.7%) |  |
| b4s_b4d_not_ext10_r12h | INFO | 165 | -2.1% | 7 (+39.8%) |  |
