# Run: hold_btc

Strategy `hold_btc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake False; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +725.29% | +37.42% | 0.83 | 1.16 | -77.20% | 0.48 | 0.86 |
| in_sample | 2020-02-15 → 2024-12-31 | +805.60% | +57.04% | 1.01 | 1.42 | -77.20% | 0.74 | 1.10 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -9.66% | -5.62% | 0.09 | 0.12 | -53.74% | -0.10 | 0.04 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -26.90% | -26.90% | -0.49 | -0.69 | -53.74% | -0.50 | -0.58 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | +0.88% | 55% | -47.44% | -54.86% | 1.74 | 0 | 0% |
| out_of_sample | 628 | +0.15% | 52% | -29.06% | -30.56% | 0.46 | 0 | 0% |
| in_sample | 1768 | +1.24% | 56% | -47.44% | -54.86% | 2.37 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +1.117% | 55% | 2.90 | +342.02% |
| bull | 687 | 28% | +0.503% | 56% | 4.06 | +2503.68% |
| bear | 400 | 17% | -0.597% | 42% | -4.30 | -92.09% |
| chop | 1160 | 48% | +0.030% | 50% | 0.22 | -5.46% |

## Turnover, fees, activity

- trades: 1 (0.00/day); active days 0%
- turnover 0.0x equity/year; fees 0.00% of equity/year ($50 total)
- average gross exposure 1.00; brake active 0.0% of hours
- correlation of daily returns with s3v2 baseline: -0.10
