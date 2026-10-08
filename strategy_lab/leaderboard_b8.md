# Block 8 (last block): universe breadth and exposure

_Generated 2026-10-08 03:32 UTC. Rules: `variants_b8_breadth.yaml` (declared before any run). Data to 2026-06-30, both halves; Jul-Oct 2026 informational. Each family vs its own core10 baseline._

**Trials:** 520 declared (ledger frozen after this block); luck threshold about 2.9 SE.

**Broad-down windows** (BTC 14d < -5% AND > 70% of pool coins down): 489 window starts in total.

**Adopted: none** (all requirements + beats its own baseline on both primary metrics in both halves).


## s3v2e (live) family (baseline `b3_s3v2e_core10`)

| run | median 14d comp IS / OOS | mean 14d IS / OOS | down mean IS / OOS | broad-down mean IS / OOS (n) | broad-down gross IS / OOS | worst 14d IS / OOS | P(<=-10%) IS / OOS | OOS Sharpe | meets all | beats baseline both halves | t mean / t comp (min of halves) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b3_s3v2e_core10 | -1.61 / -0.28 | +0.6% / +0.8% | +0.6% / +2.0% | +0.2% / +1.9% (346 / 141) | 15% / 21% | -5.3% / -5.2% | 0% / 0% | 1.38 | yes |  | baseline |
| b8_s_U1 | -1.76 / -2.09 | +0.5% / +0.4% | +0.4% / +1.7% | +0.3% / +1.7% (346 / 141) | 16% / 30% | -5.3% / -4.4% | 0% / 0% | 0.83 | **no** | no | -1.87 / -2.01 |
| b8_s_U2 | -1.76 / -1.23 | +0.7% / +0.3% | +0.6% / +1.2% | +0.6% / +1.2% (346 / 141) | 17% / 28% | -5.7% / -4.6% | 0% / 0% | 0.69 | **no** | no | -2.19 / -0.99 |
| b8_s_U3 | -1.69 / 0.07 | +0.7% / +0.4% | +0.4% / +0.9% | +0.4% / +0.9% (346 / 141) | 18% / 24% | -5.7% / -4.6% | 0% / 0% | 1.07 | yes | no | -1.45 / -0.11 |
| b8_s_U4 | -1.85 / -0.12 | +0.4% / +0.2% | +0.5% / +0.6% | +0.1% / +0.6% (346 / 141) | 8% / 13% | -7.0% / -1.8% | 0% / 0% | 1.13 | yes | no | -1.78 / -0.37 |
| b8_s_U5 | -1.51 / -1.11 | +0.6% / +0.3% | +0.4% / +0.8% | +0.4% / +0.8% (346 / 141) | 14% / 24% | -5.5% / -4.1% | 0% / 0% | 0.67 | **no** | no | -2.01 / -0.75 |
| b8_s_U6 | -1.26 / -1.17 | +0.7% / +0.5% | +0.9% / +1.9% | +0.7% / +1.9% (346 / 141) | 23% / 28% | -7.8% / -6.0% | 0% / 0% | 0.70 | **no** | no | -1.32 / -0.89 |
| b8_s_U7 | -1.30 / -1.74 | +0.8% / +0.4% | +1.4% / +2.2% | +1.1% / +2.1% (346 / 141) | 22% / 26% | -6.6% / -10.0% | 0% / 0% | 0.56 | **no** | no | -1.42 / -1.52 |

### s3v2e (live): exposure, positions, costs, analogs (OOS)

| run | avg gross | avg positions | net short share | fees/yr | trades/day | analogs 14d mean / P(>0) |
|---|---|---|---|---|---|---|
| b3_s3v2e_core10 | 20% | 3.6 | 47% | 4.3% | 2.1 | +0.4% / 43% |
| b8_s_U1 | 28% | 3.9 | 44% | 6.5% | 2.6 | +0.6% / 53% |
| b8_s_U2 | 28% | 4.0 | 44% | 6.4% | 2.6 | +0.8% / 53% |
| b8_s_U3 | 25% | 3.6 | 43% | 5.7% | 2.3 | +0.4% / 40% |
| b8_s_U4 | 13% | 2.9 | 43% | 2.7% | 1.9 | +0.3% / 47% |
| b8_s_U5 | 24% | 3.4 | 44% | 5.5% | 2.2 | +0.3% / 50% |
| b8_s_U6 | 26% | 4.3 | 50% | 6.0% | 2.8 | +0.4% / 43% |
| b8_s_U7 | 26% | 5.3 | 49% | 6.5% | 3.8 | +0.3% / 40% |

## HMM2 + CUSUM (forward test) family (baseline `b7_hmm2_cusum`)

| run | median 14d comp IS / OOS | mean 14d IS / OOS | down mean IS / OOS | broad-down mean IS / OOS (n) | broad-down gross IS / OOS | worst 14d IS / OOS | P(<=-10%) IS / OOS | OOS Sharpe | meets all | beats baseline both halves | t mean / t comp (min of halves) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b7_hmm2_cusum | -1.33 / 0.18 | +0.6% / +0.8% | +0.9% / +1.5% | +0.4% / +1.4% (346 / 141) | 14% / 18% | -6.5% / -3.7% | 0% / 0% | 1.55 | yes |  | baseline |
| b8_h_U1 | -1.24 / -1.70 | +0.5% / +0.3% | +0.7% / +1.0% | +0.7% / +1.0% (346 / 141) | 14% / 25% | -4.9% / -5.0% | 0% / 0% | 0.68 | **no** | no | -2.45 / -1.56 |
| b8_h_U2 | -1.34 / -0.31 | +0.6% / +0.3% | +0.7% / +0.8% | +0.7% / +0.8% (346 / 141) | 15% / 24% | -5.3% / -5.0% | 0% / 0% | 0.67 | **no** | no | -2.32 / -0.43 |
| b8_h_U3 | -1.62 / -0.00 | +0.4% / +0.3% | +0.5% / +0.5% | +0.4% / +0.6% (346 / 141) | 16% / 20% | -5.3% / -3.9% | 0% / 0% | 0.95 | **no** | no | -1.74 / -0.49 |
| b8_h_U4 | -1.81 / -0.12 | +0.3% / +0.2% | +0.6% / +0.4% | +0.2% / +0.4% (346 / 141) | 7% / 11% | -5.3% / -1.8% | 0% / 0% | 1.16 | yes | no | -2.27 / -0.86 |
| b8_h_U5 | -1.06 / 0.03 | +0.4% / +0.2% | +0.6% / +0.4% | +0.6% / +0.5% (346 / 141) | 13% / 20% | -4.7% / -3.9% | 0% / 0% | 0.52 | **no** | no | -2.00 / -0.11 |
| b8_h_U6 | -1.51 / 0.93 | +0.5% / +0.7% | +0.8% / +1.8% | +0.7% / +1.7% (346 / 141) | 20% / 24% | -7.9% / -4.9% | 0% / 0% | 1.08 | yes | no | -0.44 / -0.27 |
| b8_h_U7 | -1.10 / -0.45 | +0.5% / +0.5% | +1.3% / +1.9% | +1.0% / +1.8% (346 / 141) | 19% / 25% | -5.8% / -6.6% | 0% / 0% | 0.69 | **no** | no | -1.14 / -0.54 |

### HMM2 + CUSUM (forward test): exposure, positions, costs, analogs (OOS)

| run | avg gross | avg positions | net short share | fees/yr | trades/day | analogs 14d mean / P(>0) |
|---|---|---|---|---|---|---|
| b7_hmm2_cusum | 18% | 3.5 | 48% | 4.2% | 2.4 | +0.4% / 47% |
| b8_h_U1 | 25% | 3.8 | 46% | 6.3% | 2.9 | +0.7% / 50% |
| b8_h_U2 | 25% | 3.8 | 45% | 6.3% | 2.9 | +0.8% / 57% |
| b8_h_U3 | 22% | 3.4 | 43% | 5.6% | 2.6 | +0.4% / 47% |
| b8_h_U4 | 11% | 2.8 | 44% | 2.6% | 2.1 | +0.4% / 43% |
| b8_h_U5 | 21% | 3.3 | 45% | 5.4% | 2.5 | +0.3% / 43% |
| b8_h_U6 | 23% | 4.2 | 52% | 5.8% | 3.1 | +0.3% / 43% |
| b8_h_U7 | 25% | 5.3 | 50% | 6.9% | 4.4 | +0.4% / 40% |

## U6 exposure floor: when it fires

The floor fires on 964 daily decisions (42% of days; IS 710, OOS 224). Next-24h return on those days (mean / worst / P(>0)):

| run | IS | OOS | baseline on the same days IS | OOS |
|---|---|---|---|---|
| b8_s_U6 | +0.08% / -5.00% / 50% | +0.03% / -4.33% / 47% | +0.03% / -3.49% / 47% | +0.03% / -2.93% / 47% |
| b8_h_U6 | +0.03% / -4.03% / 49% | +0.04% / -2.76% / 47% | +0.03% / -1.82% / 47% | +0.02% / -1.90% / 46% |
