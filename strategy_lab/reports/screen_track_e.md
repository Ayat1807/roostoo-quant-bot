# Track E: per-coin point-in-time statistics and screening persistence

_Generated 2026-10-07 10:34 UTC by `python -m lab.screen`. Screened = VR(7d) > 1 and lag-1 autocorrelation > 0 over the previous 180 days (rule TREND). Persistence = VR(7d) > 1 over the next 90 days._

## Does the screen persist out of sample?

| period | coin-months screened / not | P(VR7 next 90d > 1): screened | not screened | difference |
|---|---|---|---|---|
| IS (to 2024-12) | 208 / 942 | 38% | 29% | +9% |
| OOS (2025-01 to 2026-04 selections) | 145 / 463 | 17% | 19% | -3% |

## Average point-in-time stats: screened vs not screened (all months)

| group | VR3 | VR7 | VR14 | Hurst | AC1 | BTC beta | vol stability | 30d volume |
|---|---|---|---|---|---|---|---|---|
| not screened | 0.92 | 0.87 | 0.81 | 0.45 | -0.056 | 1.24 | 0.27 | $54M |
| screened | 1.12 | 1.22 | 1.27 | 0.54 | +0.070 | 1.37 | 0.30 | $74M |

## Latest selection (2026-04), top 20 by volume

| coin | screened | VR7 | AC1 | Hurst | BTC beta | 30d volume |
|---|---|---|---|---|---|---|
| BTCUSDT |  | 0.71 | -0.074 | 0.45 | 1.00 | $1,591M |
| ETHUSDT |  | 0.76 | +0.051 | 0.46 | 1.31 | $849M |
| SOLUSDT |  | 0.74 | +0.036 | 0.46 | 1.34 | $280M |
| XRPUSDT |  | 0.66 | -0.091 | 0.39 | 1.31 | $171M |
| DOGEUSDT |  | 0.57 | -0.038 | 0.35 | 1.35 | $91M |
| PAXGUSDT |  | 0.84 | +0.014 | 0.45 | 0.20 | $84M |
| BNBUSDT |  | 0.72 | +0.081 | 0.45 | 0.95 | $81M |
| TAOUSDT | yes | 1.07 | +0.164 | 0.52 | 1.34 | $62M |
| ZECUSDT |  | 0.97 | +0.100 | 0.49 | 1.27 | $53M |
| TRXUSDT |  | 0.82 | -0.047 | 0.47 | 0.25 | $39M |
| ADAUSDT |  | 0.61 | -0.008 | 0.38 | 1.41 | $38M |
| PEPEUSDT |  | 0.86 | -0.029 | 0.46 | 1.61 | $36M |
| SUIUSDT |  | 0.80 | +0.013 | 0.48 | 1.62 | $35M |
| LINKUSDT |  | 0.59 | -0.014 | 0.41 | 1.39 | $28M |
| NEARUSDT |  | 0.87 | +0.113 | 0.47 | 1.43 | $25M |
| AVAXUSDT |  | 0.66 | -0.032 | 0.41 | 1.37 | $21M |
| TRUMPUSDT |  | 0.82 | -0.052 | 0.44 | 1.05 | $21M |
| LTCUSDT |  | 0.57 | -0.023 | 0.36 | 1.08 | $18M |
| FETUSDT | yes | 1.09 | +0.068 | 0.52 | 1.64 | $16M |
| WLDUSDT |  | 0.51 | -0.100 | 0.32 | 1.65 | $15M |
