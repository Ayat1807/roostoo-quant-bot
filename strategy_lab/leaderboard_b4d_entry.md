# Block 4d: Entry timing (live strategy xsmom on R1 = control)

_Generated 2026-10-07 08:43 UTC. Rules: `variants_b4d_entry.yaml` (declared before any run). Data to 2026-06-30, both halves; Jul-Oct 2026 informational only._

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
