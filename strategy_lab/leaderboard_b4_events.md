# Research block 4a: event-day variants of the live strategy (xsmom on R1)

_Generated 2026-10-07 03:14 UTC. Rules in `variants_b4_events.yaml` (declared before any run). Judged on data to 2026-06-30: IS = 2020-02-15 to 2024-12-31, OOS = 2025-01-01 to 2026-06-30. **Jul-Oct 2026 is informational only.**_

**Trials:** 276 declared across all blocks (this block: 9). Luck threshold: with that many tries the best result is expected to look about 2.7 standard errors better than its true value.

**Event windows** = rolling 14-day windows (daily step) containing a CPI release or an FOMC decision. **Adopt rule:** event-window P(14d >= +10%) strictly above the control in BOTH halves, and all-window P(14d <= -10%) not above the control in both halves.

**Adopted: `b4e_fast_12h`**


## IS: 98 independent CPI/FOMC events, 1139 event windows of 1768 (64%)

| run | event windows: P>=10% / P<=-10% / worst / median | all windows: P>=10% / P<=-10% / worst / median | event day +/-2d: mean / median (n) | fees/yr | trades/day | beats on events / P<=-10% ok | windows won-lost vs control (events) |
|---|---|---|---|---|---|---|---|
| b3_xsmom_r1 (control) | 15% / 4% / -19.1% / -0.9% | 15% / 3% / -19.1% / -0.9% | +0.6% / -0.3% (98) | 17.5% | 6.02 | control | |
| b4e_fast_2h | 13% / 3% / -17.3% / -0.8% | 14% / 2% / -17.3% / -0.7% | +0.4% / -0.4% (98) | 22.4% | 12.06 | no / yes | +16 / -36 (7 events) |
| b4e_fast_4h | 14% / 3% / -17.4% / -0.7% | 15% / 3% / -18.0% / -0.7% | +0.6% / -0.1% (98) | 20.5% | 8.94 | no / yes | +17 / -26 (7 events) |
| b4e_fast_6h | 14% / 3% / -18.6% / -0.9% | 14% / 3% / -18.6% / -0.9% | +0.6% / -0.0% (98) | 20.1% | 8.02 | no / yes | +15 / -29 (7 events) |
| b4e_fast_12h | 15% / 4% / -18.3% / -0.8% | 15% / 3% / -18.3% / -0.8% | +0.7% / -0.0% (98) | 18.8% | 6.82 | yes / yes | +17 / -16 (6 events) |
| b4e_derisk_50 | 15% / 4% / -19.4% / -0.9% | 15% / 3% / -19.4% / -0.9% | +0.5% / -0.2% (98) | 17.6% | 6.21 | no / yes | +8 / -9 (3 events) |
| b4e_derisk_25 | 15% / 3% / -20.6% / -0.8% | 15% / 2% / -20.6% / -0.9% | +0.6% / -0.2% (98) | 17.6% | 6.22 | yes / yes | +20 / -17 (7 events) |
| b4e_breakout | 15% / 4% / -19.1% / -0.9% | 15% / 3% / -19.1% / -0.9% | +0.4% / -0.2% (98) | 17.6% | 6.09 | no / yes | +1 / -4 (1 events) |
| b4e_combined_50 | 15% / 4% / -19.4% / -0.9% | 15% / 3% / -19.4% / -0.9% | +0.3% / -0.2% (98) | 17.8% | 6.30 | no / yes | +9 / -12 (4 events) |
| b4e_combined_25 | 14% / 3% / -20.6% / -0.8% | 15% / 2% / -20.6% / -0.9% | +0.4% / -0.3% (98) | 17.7% | 6.29 | no / yes | +16 / -24 (6 events) |

## OOS: 29 independent CPI/FOMC events, 344 event windows of 532 (65%)

| run | event windows: P>=10% / P<=-10% / worst / median | all windows: P>=10% / P<=-10% / worst / median | event day +/-2d: mean / median (n) | fees/yr | trades/day | beats on events / P<=-10% ok | windows won-lost vs control (events) |
|---|---|---|---|---|---|---|---|
| b3_xsmom_r1 (control) | 8% / 2% / -12.0% / -2.4% | 9% / 2% / -12.0% / -2.5% | -0.4% / -2.1% (29) | 14.1% | 4.96 | control | |
| b4e_fast_2h | 8% / 1% / -11.8% / -2.0% | 8% / 2% / -11.8% / -2.2% | -0.5% / -1.0% (29) | 20.3% | 11.58 | no / yes | +3 / -4 (2 events) |
| b4e_fast_4h | 8% / 1% / -12.2% / -1.9% | 9% / 2% / -12.2% / -2.3% | -0.3% / -1.0% (29) | 17.9% | 8.20 | yes / yes | +3 / -2 (2 events) **FEW EVENTS** |
| b4e_fast_6h | 8% / 1% / -11.9% / -2.7% | 9% / 1% / -12.0% / -2.7% | -0.2% / -2.0% (29) | 17.3% | 7.23 | yes / yes | +3 / -2 (2 events) **FEW EVENTS** |
| b4e_fast_12h | 9% / 1% / -11.8% / -2.3% | 9% / 1% / -11.8% / -2.4% | -0.5% / -1.9% (29) | 15.2% | 5.74 | yes / yes | +5 / -3 (4 events) **FEW EVENTS** |
| b4e_derisk_50 | 10% / 1% / -12.0% / -1.9% | 10% / 2% / -12.0% / -2.3% | +0.1% / -1.4% (29) | 13.4% | 4.97 | yes / yes | +8 / -0 (3 events) **FEW EVENTS** |
| b4e_derisk_25 | 10% / 1% / -12.0% / -1.8% | 10% / 3% / -12.0% / -2.1% | +0.2% / -1.0% (29) | 13.8% | 5.19 | yes / no | +8 / -0 (3 events) **FEW EVENTS** |
| b4e_breakout | 8% / 2% / -12.0% / -2.4% | 8% / 2% / -12.0% / -2.5% | -0.5% / -2.1% (29) | 14.1% | 4.97 | no / yes | +0 / -2 (0 events) |
| b4e_combined_50 | 10% / 1% / -12.0% / -2.0% | 10% / 2% / -12.0% / -2.3% | -0.0% / -1.4% (29) | 13.4% | 4.96 | yes / yes | +8 / -0 (3 events) **FEW EVENTS** |
| b4e_combined_25 | 10% / 1% / -12.0% / -1.8% | 10% / 3% / -12.0% / -2.3% | +0.1% / -1.0% (29) | 13.7% | 5.18 | yes / no | +8 / -0 (3 events) **FEW EVENTS** |

## INFO (informational only): 5 independent CPI/FOMC events, 61 event windows of 82 (74%)

| run | event windows: P>=10% / P<=-10% / worst / median | all windows: P>=10% / P<=-10% / worst / median | event day +/-2d: mean / median (n) | fees/yr | trades/day | 
|---|---|---|---|---|---|
| b3_xsmom_r1 (control) | 8% / 0% / -4.5% / -1.5% | 15% / 0% / -6.4% / -1.3% | -1.0% / -1.0% (5) | 17.3% | 5.85 |
| b4e_fast_2h | 8% / 0% / -5.9% / -2.6% | 15% / 0% / -5.9% / -2.1% | -1.1% / -1.9% (5) | 21.4% | 10.77 |
| b4e_fast_4h | 8% / 0% / -5.9% / -2.7% | 15% / 0% / -6.9% / -2.3% | -1.4% / -1.9% (5) | 20.0% | 8.57 |
| b4e_fast_6h | 8% / 0% / -6.0% / -2.5% | 15% / 0% / -6.0% / -1.9% | -0.5% / -1.7% (5) | 17.5% | 6.72 |
| b4e_fast_12h | 8% / 0% / -5.4% / -2.7% | 15% / 0% / -6.6% / -2.3% | -1.2% / -1.5% (5) | 18.9% | 7.00 |
| b4e_derisk_50 | 8% / 0% / -4.5% / -1.5% | 15% / 0% / -6.4% / -1.3% | -1.0% / -1.1% (5) | 17.3% | 5.94 |
| b4e_derisk_25 | 8% / 0% / -4.3% / -1.3% | 15% / 0% / -6.4% / -1.0% | -0.7% / -0.9% (5) | 17.2% | 5.88 |
| b4e_breakout | 8% / 0% / -4.5% / -1.6% | 15% / 0% / -6.6% / -1.3% | -1.0% / -1.0% (5) | 17.3% | 5.89 |
| b4e_combined_50 | 8% / 0% / -4.5% / -1.6% | 15% / 0% / -6.6% / -1.3% | -1.0% / -1.1% (5) | 17.4% | 5.97 |
| b4e_combined_25 | 8% / 0% / -4.3% / -1.3% | 15% / 0% / -6.6% / -1.1% | -0.7% / -0.9% (5) | 17.0% | 5.80 |

## How often the breakout rule fires (BTC beyond +/-2% within 4h of a CPI/FOMC event)

| period | up (extra decision) | down (cash to next daily) | neither |
|---|---|---|---|
| IS | 29 | 21 | 51 |
| OOS | 4 | 2 | 23 |
| INFO | 2 | 0 | 3 |

_Windows won-lost: event windows where the variant reaches +10% and the control does not (won) and the reverse (lost); (events) = distinct events inside the won windows. FEW EVENTS = net gain resting on fewer than 5 distinct events in that half._
