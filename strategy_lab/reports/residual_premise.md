# Block 9 STEP 0: residual-momentum premise test

_Generated 2026-10-08 06:51 UTC by `python -m lab.residual_premise`; definitions in `variants_b9_residual.yaml` (declared before computing). Events: |residual 3-day move| >= 10% while BTC's 3-day move is within +/-3%; continuation C = next-3-day residual return in the direction of the move; C_net after a hedged round trip (0.24% x (1 + |beta|))._

**Verdict (declared rule: mean C_net > 0 with t >= 2 in BOTH halves, overall or in the attention subset): NO-GO: continuation is not positive after costs; the block stops here**

## How often

| period | days | days with >= 1 event | calm-BTC days with >= 1 event | calm weeks | median event coins per calm week | mean universe size |
|---|---|---|---|---|---|---|
| IS (2020-2024) | 1824 | 27% | 53% | 108 | 3 | 22 |
| OOS (2025-01 to 2026-06) | 546 | 47% | 75% | 33 | 7 | 44 |
| Jul-Oct 2026 (info) | 96 | 50% | 62% | 7 | 7 | 35 |

## Do the moves continue? (next-3-day residual return in the move's direction)

| period | subset | events (dates) | mean C | median C | hit C > 0 | mean C_net (after costs) | t (C_net, clustered by date) |
|---|---|---|---|---|---|---|---|
| IS (2020-2024) | all | 1344 (492) | +0.24% | -0.78% | 46% | -0.29% | -0.71 |
| IS (2020-2024) | volume >= 2x | 446 (244) | +0.94% | -0.74% | 46% | +0.45% | +0.67 |
| IS (2020-2024) | volume < 2x | 898 (388) | -0.11% | -0.81% | 47% | -0.66% | -1.35 |
| IS (2020-2024) | single-day spike > 25% | 86 (68) | +4.17% | +1.25% | 52% | +3.66% | +1.85 |
| IS (2020-2024) | no spike | 1258 (476) | -0.03% | -0.84% | 46% | -0.56% | -1.35 |
| IS (2020-2024) | ATTENTION (vol >= 2x, no spike) | 374 (221) | +0.27% | -0.86% | 45% | -0.21% | -0.33 |
| IS (2020-2024) | up moves | 805 (368) | +0.47% | -1.19% | 44% | -0.04% | -0.07 |
| IS (2020-2024) | down moves | 539 (225) | -0.12% | +0.15% | 50% | -0.66% | -0.94 |
| OOS (2025-01 to 2026-06) | all | 856 (255) | +0.34% | +0.46% | 52% | -0.35% | -0.67 |
| OOS (2025-01 to 2026-06) | volume >= 2x | 261 (121) | +0.15% | +0.13% | 51% | -0.53% | -0.49 |
| OOS (2025-01 to 2026-06) | volume < 2x | 595 (215) | +0.42% | +0.50% | 53% | -0.28% | -0.48 |
| OOS (2025-01 to 2026-06) | single-day spike > 25% | 46 (36) | -1.91% | -0.40% | 43% | -2.68% | -1.07 |
| OOS (2025-01 to 2026-06) | no spike | 810 (246) | +0.47% | +0.60% | 53% | -0.22% | -0.42 |
| OOS (2025-01 to 2026-06) | ATTENTION (vol >= 2x, no spike) | 224 (107) | +0.61% | +0.67% | 52% | -0.06% | -0.06 |
| OOS (2025-01 to 2026-06) | up moves | 412 (162) | -0.39% | -1.74% | 42% | -1.09% | -1.37 |
| OOS (2025-01 to 2026-06) | down moves | 444 (151) | +1.02% | +1.81% | 63% | +0.33% | +0.46 |
| Jul-Oct 2026 (info) | all | 109 (48) | +1.74% | +1.06% | 54% | +1.19% | +1.23 |
| Jul-Oct 2026 (info) | volume >= 2x | 34 (20) | -0.98% | -2.94% | 35% | -1.52% | -0.68 |
| Jul-Oct 2026 (info) | volume < 2x | 75 (43) | +2.97% | +1.63% | 63% | +2.41% | +2.13 |
| Jul-Oct 2026 (info) | single-day spike > 25% | 4 | | | | | |
| Jul-Oct 2026 (info) | no spike | 105 (48) | +1.64% | +0.98% | 53% | +1.08% | +1.17 |
| Jul-Oct 2026 (info) | ATTENTION (vol >= 2x, no spike) | 30 (18) | -1.70% | -3.20% | 30% | -2.24% | -1.03 |
| Jul-Oct 2026 (info) | up moves | 63 (32) | +1.36% | -1.00% | 48% | +0.82% | +0.49 |
| Jul-Oct 2026 (info) | down moves | 46 (29) | +2.25% | +1.36% | 63% | +1.68% | +1.16 |
