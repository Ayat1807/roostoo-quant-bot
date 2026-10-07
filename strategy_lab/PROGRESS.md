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

## Running
- logs: .cache/b4b_sweep.log, b6a_sweep.log, b6b_sweep.log, b6c_run.log, meta.log

## Next (in order)
1. When each finishes: resolve its sweep (`python -m lab.b6 <track> --resolve-sweep`), commit, run `--group sweep`;
   report `python -m lab.b6 <track>` -> leaderboard_b6<track>.md; stats cards for finalists (`python -m lab.stats_card`).
2. Track E runs 458-460, then D runs 471-472 (after lab.meta). 4b: `python -m lab.b4gen 4b` + b5 report (newobj).
3. Final block-6 summary: per track verdict, down-window results, stats cards, ideas needing more time (Deep Momentum
   Networks etc.) for the finals presentation. Implement a passing variant behind a config flag + tests; never deploy.
