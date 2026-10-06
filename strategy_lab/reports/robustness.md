# Real-market robustness

Same runs with **100% taker fills** (0.10%) and **+5 bps extra slippage per fill** (7 bps total). Judged on data to 2026-06-30; Jul-Oct 2026 informational only.

| run | costs | fees/yr | IS P>=10% / P<=-10% / worst | OOS P>=10% / P<=-10% / worst | OOS median 14d | meets both halves | INFO Jul-Oct P>=10% / median |
|---|---|---|---|---|---|---|---|
| b3_xsmom_tm10 | base (lab: taker + 2 bps) | 9.1% | 6% / 0% / -11.3% | 9% / 0% / -14.4% | -1.5% | yes | 24% / +2.1% |
| b3_xsmom_tm10 | taker + 7 bps | 8.7% | 5% / 0% / -11.4% | 9% / 1% / -14.5% | -1.5% | yes | 24% / +1.9% |
| b3_xsmom_tm10_liq | base (lab: taker + 2 bps) | 8.5% | 6% / 0% / -11.3% | 6% / 1% / -11.3% | -1.7% | yes | 20% / +4.7% |
| b3_xsmom_tm10_liq | taker + 7 bps | 8.3% | 6% / 0% / -11.4% | 5% / 1% / -11.7% | -1.9% | yes | 20% / +3.7% |
| b3_c50_s3v2e_xsmom_tm10 | base (lab: taker + 2 bps) | 6.1% | 2% / 0% / -6.6% | 2% / 0% / -6.0% | -0.3% | yes | 30% / +0.2% |
| b3_c50_s3v2e_xsmom_tm10 | taker + 7 bps | 5.8% | 2% / 0% / -6.6% | 2% / 0% / -5.8% | -0.3% | yes | 30% / -0.1% |
| b3_s3v2e_core10 | base (lab: taker + 2 bps) | 3.9% | 3% / 0% / -5.3% | 4% / 0% / -5.2% | -0.1% | yes | 16% / -0.9% |
| b3_s3v2e_core10 | taker + 7 bps | 3.8% | 3% / 0% / -5.4% | 3% / 0% / -4.2% | -0.1% | yes | 16% / -1.1% |
