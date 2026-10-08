# strategy_lab progress (resume here)

**LIVE competition bot: `config_competition_s3v2e.yaml` (s3v2e on core10), tmux `competition_s3v2e`, since 2026-10-07
10:04 UTC. Never touch it.** (xsmom on R1 ran 2026-10-06 15:30 to 2026-10-07 10:00 UTC, ended -3.36%, replaced after the
stats-card review.) **Reference for all research: b3_s3v2e_core10.** All work here is offline or for the testing bot.

## Judging (team objective since 2026-10-07, block 5 on)
Primary: median 14d composite (0.4 Sortino + 0.3 Sharpe + 0.3 Calmar per window) and mean 14d return. Requirements (both
halves): mean 14d return > 0 in DOWN windows (BTC 14d < -5%), P(14d <= -10%) <= 5%, worst 14d >= -15%; OOS Sharpe >= 1.0.
Adopt: all requirements + beats b3_s3v2e_core10 on both primary numbers in both halves. Data to 2026-06-30 (IS 2020-02-15 to
2024-12-31, OOS 2025-01-01 to 2026-06-30); Jul-Oct informational, never a gate. Pre-register (variants file + commit) before
running; frequency sweep for the best 2; stats card (`python -m lab.stats_card`) for every finalist. Judging code: lab/b5.py.
Fitted models: expanding walk-forward, purge/embargo, min 6-month train, 1-month test steps, OOS predictions only.
Secondary: 3-day-horizon metrics overall and in the 30 analog windows.

## Done (newest last)
- Blocks 4a (events/exits), 4c (long/short xsmom), 4d (entry timing), 5 (down-market designs): none adopted.
- `8592182` competition switch prepared; deployed by the team 2026-10-07 10:04 UTC; `d154e7a` docs (README history, DEPLOY 13).
- Block 4b (sizing) 359-383 done (best sizing b4b_score; old objective: nothing beat live); sweep 384-393 running.
- Block 6 (s3v2e upgrades), all pre-registered (global declared 482):
  - A `variants_b6a_signal.yaml` 409-429: 409-419 run, NOT adopted (best cusum4_c50 meets all, never beats the reference's
    mean 14d return in both halves); sweep 420-429 running.
  - B `variants_b6b_regime.yaml` 430-444 (walk-forward HMM, data/regime/): 430-434 run, NOT adopted (hmm2 closest: comp
    better both halves, mean ties); sweep 435-444 running.
  - C `variants_b6c_alloc.yaml` 445-457 (ERC / HRP / shrunk Kelly): 445-447 running.
  - E `variants_b6e_universe.yaml` 458-470 (TREND screen): not run yet. reports/screen_track_e.md: screen does NOT persist OOS.
  - D `variants_b6d_meta.yaml` 471-482: `python -m lab.meta` running (dataset + walk-forward -> data/meta/preds.csv,
    reports/meta_track_d.md); then run 471-472.

- Block 6 MAIN RESULTS (all tracks run): NOTHING ADOPTED; s3v2e_core10 stays. reports/block6_summary.md,
  reports/stats_card_b6_finalists.md, leaderboard_b6{a,b,c,d,e}.md. Closest: B hmm2 (composite better both halves, mean ties),
  C erc (best OOS composite +0.71, worse IS), A cusum4_c50 (lowest drawdowns).

- Block 7 (combinations HMM2 / ERC / CUSUM, 483-486): NOT adopted; all margins |t| <= 1.5 vs luck threshold 2.9
  (leaderboard_b7.md, reports/stats_card_b7_finalists.md). Sweep 487-496 running. Block 4b final reports done (old objective:
  b4b_score / b4b_best_vol_target pass on noise-level margins but xsmom is retired; new objective: none).

- STEP 1 (2026-10-07): forward test HMM2 + CUSUM implemented in strategy_bot (regime_live.py, flags regime_hmm /
  changepoint_cut, config_testing_hmm_cusum.yaml, status.py lines, daily_check.py, shared-account guard,
  tests/test_hmm_cusum.py PASS), reports/forward_test_plan.md, DEPLOY.md section 14.

- STEP 2: block 8 (497-510) done, NOT adopted in either family (leaderboard_b8.md, reports/stats_card_b8_finalists.md);
  sweep 511-520 running (.cache/b8_sweep.log).
- STEP 3: all block 6 / 7 sweeps folded into the reports; trial ledger FROZEN at 520 declared trials.
- STEP 4: history secret scan CLEAN (reports/public_readiness.md: open decisions = author email in history, teammate
  consent, doc test vector); root README.md; reports/finals_outline.md ([FILL] items from daily_check.py).

- Block 9 STEP 0 (residual-momentum premise test, 0 trials): NO-GO (moves frequent, no continuation after costs in either
  half); STEP 1 not declared or run. reports/residual_premise.md. Ledger still 520.

- Block 10 (intraday jump premise test, 0 trials, 5-minute Binance bars in .cache/klines_5m): NO-GO (IS jumps reverse,
  t -5.4 at 1h; OOS ~0); recorded as a finding (reports/jump_premise.md). No capture bot. Ledger still 520.

- News risk layer (strategy_bot/news_layer.py, SHADOW on config_testing_hmm_cusum.yaml, tests/test_news_layer.py, DEPLOY.md
  section 15, news_shadow_report.py). Block 11 (1 trial, 521): calendar + Fear & Greed rules barely change OOS, cost return IS
  (reports/news_rules_dry_run.md). Veto rule: forward shadow log only.

## Running
- block 8 sweep 511-520 (tables only).

## Next
1. When the block 8 sweep finishes: `python -m lab.b8`, commit. Nothing else queued; research is closed.
