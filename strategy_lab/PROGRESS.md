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
- Blocks 4a (events/exits), 4c (long/short xsmom), 5 (down-market designs): none adopted. leaderboard_b4_*.md, leaderboard_b5.md.
- `8592182` competition switch prepared; deployed by the team 2026-10-07 10:04 UTC; `d154e7a` docs (README history, DEPLOY 13).
- Block 4d (entry timing) 344-358 incl. sweep done, none adopted under the old objective.
- Block 4b (sizing) 359-383 done (best sizing b4b_score); sweep 384-393 to resolve and run.

## Running
- (see Next)

## Next (in order)
1. Block 4b: `python -m lab.b4gen 4b --resolve-sweep` -> commit -> `--group sweep`; reports `python -m lab.b4gen 4b` and
   `python -m lab.b5 b4d__control b5ref__b3_s3v2e_core10 <4b runs> --out leaderboard_b4b_newobj.md`; commit.
2. Block 4d: `python -m lab.b4gen 4d` + `python -m lab.b5 ... --out leaderboard_b4d_entry_newobj.md` incl. sweep runs; commit.
3. NEW PROGRAM (block 6, upgrades of s3v2e_core10), order A, B, C, E, D; pre-register each track before running:
   A signal / turning points (A1 continuous t-stat, A2 EMA speed ensemble, A3 changepoint exit CUSUM + BOCPD, A4 = A1 + A3);
   B regime (HMM 2/3 states, correlation-state filter); C allocation (ERC, HRP, shrunk Kelly); E universe screening;
   D meta-labeling (LightGBM, walk-forward). Implement a passing variant behind a config flag + tests; never deploy.
