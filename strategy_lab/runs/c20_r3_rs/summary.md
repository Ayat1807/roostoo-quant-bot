# Run: c20_r3_rs

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +127.58% | +13.76% | 0.88 | 1.22 | -25.50% | 0.54 | 0.91 |
| in_sample | 2020-02-15 → 2024-12-31 | +89.61% | +14.00% | 0.88 | 1.22 | -25.50% | 0.55 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +20.12% | +13.04% | 0.85 | 1.21 | -11.39% | 1.14 | 1.08 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.91% | +14.85% | 0.94 | 1.34 | -11.39% | 1.30 | 1.21 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.36% | 43% | -7.34% | -7.69% | -1.78 | 14 | 100% |
| out_of_sample | 532 | -0.37% | 42% | -6.63% | -7.41% | -2.06 | 14 | 100% |
| in_sample | 1768 | -0.34% | 44% | -7.34% | -7.69% | -1.63 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.171% | 56% | 2.70 | +32.04% |
| bull | 659 | 28% | +0.138% | 56% | 3.18 | +142.27% |
| bear | 399 | 17% | -0.043% | 44% | -1.28 | -16.59% |
| chop | 1099 | 47% | -0.009% | 45% | -0.22 | -12.70% |

## Turnover, fees, activity

- trades: 6518 (2.80/day); active days 100%
- turnover 40.6x equity/year; fees 4.06% of equity/year ($21,872 total)
- average gross exposure 0.21; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.90
