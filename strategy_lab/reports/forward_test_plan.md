# Forward test plan: s3v2e_core10 + HMM2 + CUSUM cut (testing key)

**Candidate:** strategy_lab run `b7_hmm2_cusum`. This is the live strategy (s3v2e on core10) plus two risk overlays:
- **HMM2:** a 2-state Gaussian HMM on BTC daily return and 7-day vol, refit monthly walk-forward, using the filtered probability. When the "crisis" probability rises, all targets shrink (×(1 − 0.5·p)) and shorts in bull markets grow (from 0.5 toward 1.0).
- **CUSUM cut:** if a held coin breaks against its position (CUSUM of standardised hourly returns > 4 since the daily target), it is cut to 50% until the next daily target.

**Where it runs:**
- Config `strategy_bot/config_testing_hmm_cusum.yaml`: testing key, $10,000 cap, own `logs_testing_hmm/`, `state_testing_hmm/`, `KILL_testing_hmm`.
- Parity and tests: `strategy_bot/tests/test_hmm_cusum.py`. It checks:
  - HMM probabilities identical to the lab (to 1e-12);
  - daily targets identical;
  - 15 of 15 cuts identical to the lab backtest over 30 days;
  - 0 errors;
  - a restart after a cut.

**The live competition bot (`competition_s3v2e`) is not touched.**

## Why a forward test and not a switch
The lab result is not distinguishable from the live strategy (block 7: every margin |t| ≤ 1.5 vs a luck threshold of 2.9). What the candidate should change is the shape of risk, not the return:

| backtest, OOS 2025-01 to 2026-06 | live s3v2e_core10 | candidate |
|---|---|---|
| Sharpe | 1.38 | 1.55 |
| max drawdown | −12.0% | −8.1% |
| worst 14 days | −5.2% | −3.7% |
| median 14d composite | −0.28 | +0.18 |
| mean 14d return | +0.8% | +0.8% |
| mean gross exposure | 20% | 18% |
| std of daily returns | 0.81% | 0.66% |
| CUSUM cuts | | 0.43 per day on average (15 in the last 30 days) |
| HMM crisis probability > 0.5 | | 10% of OOS days; currently about 0.2% |

The forward test checks that the bot really behaves like this on Roostoo: same coins, smaller swings, cuts at about the expected rate. Short-term P&L over a few days says almost nothing either way.

## One account, one bot
The testing key is one Roostoo account. Two live bots on it would trade the same coins, and each would cancel the other's resting orders at startup.
- **The guard:** the new bot refuses to start while another bot's fresh heartbeat shows a live bot on the same key label.
- **Plan:** stop the current testing bot (sleeves s3v2 + xsmom; xsmom is retired), let it flatten first, then start the forward test.

## Daily check (once a day, any time)
```bash
cd ~/Trading_Competition/strategy_bot && .venv/bin/python daily_check.py
```
It prints the forward-test bot, the old testing config and the live bot side by side: heartbeat, equity (24h and since start), gross / net exposure, brake, HMM p_crisis, active cuts and cuts fired in 24h, orders and errors in 24h, and positions. Exit code 1 means a stale heartbeat or errors.

## Switch criteria (all required; NOT short-term P&L)
1. **Clean operation:**
   - 0 unexplained errors;
   - the heartbeat is never stale;
   - restarts, if any, restore targets and cuts and place no orders;
   - the HMM refits on the 1st of the month without errors (the first refit is 2026-11-01);
   - every day is active.
2. **Behaviour consistent with the backtest:**
   - **Same coins and directions** as the live bot on the same day. The two may differ only in size: the HMM scaling, the cuts, and the one-hour later target time (01:00 vs 00:00 UTC).
   - **Smaller swings:** a lower or equal daily-return std than the live bot over the test period, and gross exposure at or below the live bot's.
   - **Cuts fire at a plausible rate,** around 0.2–1 per day. Each cut trades immediately, and there is no cut in the hour of a new daily target.
3. **The team accepts the risk profile:** about the same return, with smaller drawdowns, smaller worst-14-day losses, and more shorting when the HMM sees a crisis.

**Not a criterion:** P&L over a few days. The backtest difference in mean return is 0.0pp, so live P&L differences in days are noise.

## Calendar
- **Start:** as soon as possible (2026-10-08).
- **No deployment or switch between 2026-10-13 and 2026-10-15 (US CPI on 2026-10-14).** The live bot stays as is through CPI.
- **Earliest switch decision:** 2026-10-16. That leaves at least 7 days of forward test, including the CPI move. A switch would be a new competition config with its own stats card, and only on the team's decision.
- **If the forward test shows any criterion failing:** stop it (`touch KILL_testing_hmm`, then stop the tmux session) and keep the live strategy.
