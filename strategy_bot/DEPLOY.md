# strategy_bot: S3v2 on Roostoo, deploy guide

`strategy_bot` runs a plug-in strategy, by default **S3v2**: low-turnover, volatility-targeted, multi-horizon time-series momentum on 10 crypto pairs, long and short. It runs on EC2 (Amazon Linux 2023, ap-southeast-2) and is reached through Session Manager only.

The instance setup (IAM role, deploy key, tmux basics) is the same as for pipeline_bot. See [../pipeline_bot/DEPLOY_AWS.md](../pipeline_bot/DEPLOY_AWS.md) sections 0–2 if this is a new instance.

> ⚠️ **One bot per Roostoo account.** `strategy_bot` and `pipeline_bot` both read the account's real balances. If both run on the same key, each sees the other's BTC as its own position and they trade against each other. **Stop `pipeline_bot` before starting `strategy_bot` live on the same key.**
>
> ⚠️ **tmux OR systemd, never both** (section 9 shows how to check).
>
> ⚠️ **Testing key only** until the team decides otherwise. `ROOSTOO_KEY_LABEL=competition` is refused unless `allow_competition: true` is set in `config.yaml`, and even then the bot shows a 10 s warning first.

---

## 1. What runs, and when

| When | What |
|---|---|
| Startup | Clock sync. exchangeInfo check. Universe check: each pair must be crypto, `CanTrade`, and have live ticker data; pairs that fail are dropped and logged. 800 h of Binance closes are seeded per pair, or loaded from `state/bars.csv` with any missing hours topped up. Stale pending orders are cancelled. Then the targets of the most recent 00:00 UTC slot are restored from `state/targets.json` (computed fresh only if none exist for that slot, or the strategy config changed), and the first rebalance runs. |
| Every 60 s | One `ticker` call for all pairs, which updates the hourly bars. The heartbeat is written. |
| Each completed hour | An account snapshot (SpotWallet plus short positions), the drawdown brake, then a rebalance of every pair whose weight is more than 6 pp off target, or whose target is 0 while we still hold it. Reductions go first, then increases. |
| 00:00 UTC daily | S3v2 target weights are recomputed, and the full vector is logged. |
| 20:00 UTC | If nothing has traded today, the bot rebalances with a 1 pp band (activity guard). |
| Any time | A `KILL` file makes the bot flatten within one poll, then idle while the file exists. |

Orders are placed as a LIMIT at our side of the touch (maker 0.05%). After 5 minutes the bot cancels and sends a MARKET order for the remainder. A limit that rests and fills later is logged as `LIMIT_LATE_FILL` (fill price and fee) in `orders.jsonl` and `bot.log`; a cancelled one as `LIMIT_TIMEOUT` with what had filled. Shorts go through `/v6` with collateral. A timed-out order request is never resent: the bot looks the order up and cancels it, and the next hour re-reads the account.

## 2. Key settings (`config.yaml`)

| Key | Default | Meaning |
|---|---|---|
| `dry_run` | `true` | Log intended orders only. Use `--live` or set `false` for real orders. |
| `capital_cap_usd` | `3000` | The bot sizes as if equity = min(actual, cap). Use `null` for full equity. |
| `allow_short` | `true` | If `false`, negative weights become 0, and any existing shorts are closed at the next rebalance. |
| `strategy.*` | S3v2 frozen params | horizons 24/72/168/336 h, vol 336 h, target_vol 0.40, short_scale_bull 0.5, max_w 0.30 |
| `band` / `guard_band` | 0.06 / 0.01 | rebalance thresholds |
| `dd_soft` / `dd_hard` | −4% / −7% | halve exposure / flat for 24 h (vs rolling 14-day peak) |
| `limit_wait_s` | 300 | seconds before a resting limit order falls back to market |

## 3. Install on the instance

```bash
sudo su - ec2-user
cd ~/Trading_Competition && git pull
bash strategy_bot/deploy/setup_ec2.sh          # idempotent: python3.11, venv, pinned deps (pandas, numpy)
cd ~/Trading_Competition/strategy_bot
nano .env                                       # TESTING key pair, ROOSTOO_KEY_LABEL=testing
chmod 600 .env && ls -l .env                    # -rw------- ec2-user
```

## 4. Offline tests (no keys, about 15 min on first run while history downloads)

```bash
cd ~/Trading_Competition/strategy_bot && source .venv/bin/activate
python -m tests.test_safety      # no-resend after timeout, key gate, plug-in contract
python -m tests.test_parity      # live S3v2 == research tsmom_lt (needs ../_reference, see below)
python -m tests.test_backtest    # reproduces the reference OOS backtest (needs ../_reference)
python -m tests.test_replay      # 30-day replay vs mock exchange: errors, cap, activity, KILL
```

`test_parity` and `test_backtest` import the reference research code from `Trading_Competition/_reference/roostoo-bot/research`. That folder is git-ignored, so on EC2 you would need to copy it over. Running these two locally is enough; `test_safety` and `test_replay` run anywhere.

## 5. Dry run (foreground)

```bash
cd ~/Trading_Competition/strategy_bot && source .venv/bin/activate
python bot.py --dry-run --max-cycles 2
python status.py
```

Check the output for:
- `universe (10): ...`, with no `dropping` warnings unless expected
- `bars loaded: ~800 rows x 10 pairs`
- `targets computed: first start (slot ...)` on a first start, or `targets restored from 00:00 (...)` on a restart the same day, and `[DRY RUN] ...` order lines
- `Errors in last 24h: 0`

## 6. Unattended run with tmux (one-line commands)

Session Manager drops after about 30 s idle, so every step below is a single command that returns immediately. You never need to stay attached. Run `sudo su - ec2-user` first.

**a) Stop pipeline_bot** (same key). This sends Ctrl+C, so it finishes its cycle and exits:
```bash
tmux send-keys -t bot C-c; sleep 15; tmux kill-session -t bot 2>/dev/null; pgrep -af "pipeline_bot|bot.py" || echo "no bot running"
```

**b) Start strategy_bot LIVE, detached** (the one-liner):
```bash
tmux new-session -d -s strategy -c /home/ec2-user/Trading_Competition/strategy_bot '.venv/bin/python bot.py --live'
```

**c) Check it** (about 90 s later, after the bootstrap and first rebalance):
```bash
tmux ls; cd /home/ec2-user/Trading_Competition/strategy_bot && .venv/bin/python status.py; tail -n 20 logs/bot.log
```

**Stop gracefully:**
```bash
tmux send-keys -t strategy C-c
```

Optional: `tmux attach -t strategy` to watch live (detach with Ctrl+B then D). If the session drops while attached, the bot keeps running.

If the bot process exits, the tmux session closes with it. `status.py` will then show a stale heartbeat, and `logs/bot.log` keeps the reason. The drawdown brake is ON (`dd_soft -4%`, `dd_hard -7%` in `config.yaml`).

## 7. systemd (auto-restart on crash and reboot)

```bash
cd ~/Trading_Competition/strategy_bot
nano config.yaml                # dry_run: false   (the unit runs plain `python bot.py`)
sudo cp deploy/strategy-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now strategy-bot
systemctl status strategy-bot
journalctl -u strategy-bot -f
```

Reboot test:

```bash
sudo reboot
# reconnect (Session Manager), then:
sudo su - ec2-user
systemctl status strategy-bot
cd ~/Trading_Competition/strategy_bot && .venv/bin/python status.py
```

`TimeoutStopSec=420` gives an in-flight limit order time to finish (5 min wait plus the market fallback) on a graceful stop.

## 8. Monitoring

```bash
cd ~/Trading_Competition/strategy_bot
.venv/bin/python status.py      # heartbeat age, equity, brake, target vs actual table, last decisions/orders, 24h errors
tail -f logs/bot.log            # human-readable, rotates at 5 MB x 5
tail -f logs/decisions.jsonl    # start / targets (full vector daily) / rebalance (current, target, plan)
tail -f logs/orders.jsonl       # every order request + full response
tail -f logs/equity.jsonl       # hourly equity, sizing equity, long/short value, exposure, brake
tail -f logs/errors.jsonl
```

With `sleeves:` in the config, `status.py` shows one block per sleeve (last and next decision, targets, book weights, universe; for R1 the month's list) and the table lists only the active universe plus anything still held. "Actual" is the latest account snapshot plus the fills logged after it, so it is correct right after a decision's orders fill (not only after the next hourly step). It is read-only: no API calls, no writes.

`status.py` exits with code 1 if the heartbeat is stale (older than 2 × (poll + limit wait)) or there were errors in the last 24 h. You can use that exit code in a cron alert.

## 9. Stop, kill switch, check what is running

```bash
systemctl is-active strategy-bot ; tmux ls ; pgrep -af "bot.py"   # expect ONE bot per account
sudo systemctl stop strategy-bot          # systemd (graceful)
tmux attach -t strategy  then Ctrl+C      # tmux (graceful; second Ctrl+C = immediate)

touch ~/Trading_Competition/strategy_bot/KILL   # flatten within ~1 min, then idle
rm    ~/Trading_Competition/strategy_bot/KILL   # resume at the next hour
```

KILL leaves only dust that can't legally be traded (below the $1 MiniOrder, or below one quantity step).

## 10. Update and restart

```bash
cd ~/Trading_Competition && git pull
cd strategy_bot && .venv/bin/pip install -r requirements.txt     # if requirements changed
sudo systemctl restart strategy-bot        # or in tmux: Ctrl+C, wait for "stopped cleanly", start again
.venv/bin/python status.py
```

Restarts are safe. State lives in `state/`: bars, the risk brake's peak and cool-off, the last trade day, and today's targets (`targets.json`; a mid-day restart reuses the 00:00 targets instead of recomputing, so a redeploy causes no extra trades). The first restart after this feature ships restores today's 00:00 targets from `logs/decisions.jsonl`. The account itself is always re-read from the exchange. Stale pending orders are cancelled on start.

## 11. Adding a strategy (teammates)

1. Create `strategies/<name>.py`, subclassing `strategies.base.Strategy`, and implement `target_weights(closes, cfg) -> {pair: signed weight}` with gross ≤ 1.
2. Register it in `strategies/__init__.py`.
3. Set `strategy.name: <name>` (plus its params) in `config.yaml`.
4. Run `python -m tests.test_replay`. Execution, risk, caps and logging are shared and need no changes.

## 11. Sleeves (optional: s3v2 + xsmom in one account)

`config.yaml` has the `sleeves:` block enabled (testing-key forward test from 2026-10-06: s3v2 0.5 + xsmom 0.5, cap $10,000). Remove the block to go back to single-strategy mode. Sleeves run several strategies on one account, one polling loop:

- **Books:** each sleeve gets `weight` x the capped capital as its own virtual book, persisted in `state/sleeves.json`, and then evolves with its own PnL.
- **s3v2 (`execution: band`):** keeps the hourly 6pp band checks.
- **xsmom (`execution: scheduled`):** trades fully to its target only at its 14:00 UTC-bar decision (wall clock about 15:00); there are no drift trades in between.
- **Netting:** each step's book changes are netted into one order per coin (no ping-pong on shared coins such as SOL). Every order in `orders.jsonl` has a `sleeves` field showing which sleeve caused it.
- **Account-wide rules:** brake, KILL and the capital cap apply to the whole account.
- **Restarts:** both sleeves' books and targets are restored. A config change gives that sleeve fresh targets once.
- **Liquidity guard:** `liquidity_guard` skips illiquid coins at each decision, for example LISTA or STO when their 24h volume on Roostoo is under $1M.

Tests: `python -m tests.test_sleeves` and `python -m tests.test_xsmom_parity`.

**First restart with the sleeves config** (switching from the single-strategy bot):

- **Books:** `state/sleeves.json` doesn't exist yet, so both books start at 0.5 x min(equity, $10,000). The positions the account already holds are assigned to the s3v2 book.
- **s3v2:** adopts today's 00:00 targets from `state/targets.json`, logged as `restored`, so there's no mid-day recompute. It may trade once at startup, but only to resize the inherited positions. They were sized for the old $3,000 cap; the s3v2 book now has about $5,000.
- **xsmom:** computes its targets from its last 14:00 UTC decision bar (`first start`). It trades to them at startup if that decision holds coins; otherwise it waits for the next 14:00 bar. After that it trades only at its daily decision.
- **Later restarts:** both books and targets are restored from `state/sleeves.json`, with 0 orders. Changing only `capital_cap_usd` doesn't reset targets.
  - Book capital is fixed when the books are created. A lower cap scales sizing down; a higher cap doesn't grow existing books.
  - To re-split the capital (for example after changing sleeve weights), stop the bot, delete `state/sleeves.json`, and restart.

## 12. Competition go-live (config_competition.yaml: xsmom on R1) - HISTORY, replaced 2026-10-07 (section 13)

**Required before any competition config:** a committed stats card next to it (`stats_card:` in the config, generated with `python -m lab.stats_card <run> [comparison runs]` in strategy_lab). `tests/test_safety.py` fails if a config with `allow_competition: true` has none.

`config_competition.yaml` runs **one sleeve: xsmom on the R1 universe**. That's the top 15 Roostoo crypto pairs by 30-day Binance dollar volume with ≥90 days of history, ≥$10M/day and a live Roostoo spread ≤5 bps, re-selected on the 1st of each month.

- **Sizing:** weight 1.0, full equity (`capital_cap_usd: null`).
- **Trading:** only at the decision on the 14:00 UTC bar (wall clock about 15:00 UTC).
- **Risk:** liquidity guard and drawdown brake on.
- **Isolation:** it has its own key file (`.env.competition`), `logs_competition/`, `state_competition/` and `KILL_competition`, so it runs next to the testing bot without sharing anything.
- **Fallback:** `config_competition_tm10.yaml` (xsmom on the teammate's 10 coins + liquidity guard) uses the same files.

**One-time setup (on EC2; the keys never go in chat or git):**
```bash
cd ~/Trading_Competition && git pull && bash strategy_bot/deploy/setup_ec2.sh
cd ~/Trading_Competition/strategy_bot && cp .env.competition.example .env.competition && chmod 600 .env.competition
nano .env.competition        # paste the COMPETITION key pair; keep ROOSTOO_KEY_LABEL=competition
git check-ignore -v .env.competition   # must print the .gitignore rule (= ignored)
.venv/bin/python -m tests.test_safety  # offline, no keys used
```

**Start (at launch, 04:00 UTC = 12:00 HKT), detached:**
```bash
tmux new-session -d -s competition -c /home/ec2-user/Trading_Competition/strategy_bot '.venv/bin/python bot.py --config config_competition.yaml --live'
```
- **10-second warning:** the bot prints a COMPETITION KEY warning and counts down from 10 before starting.
- **Bootstrap:** it then loads 2000 hourly bars for about 65 pairs and selects the R1 list, which takes about 5 minutes.
- **First trades:** it trades at startup only if the last 14:00 UTC decision holds coins; otherwise it waits for the next decision (about 15:00 UTC).

**Check:**
```bash
tmux ls; cd ~/Trading_Competition/strategy_bot && .venv/bin/python status.py --config config_competition.yaml
tail -n 30 logs_competition/bot.log; cat state_competition/universe_r1.json
```

**Stop / kill switch:**
- Graceful stop: `tmux send-keys -t competition C-c`.
- Flatten and idle: `touch KILL_competition`. Delete the file to resume.

**Fallback (tm10):** stop the bot, then `rm -rf state_competition` (its books belong to the R1 config), then start the same tmux command with `--config config_competition_tm10.yaml`.

Don't make any manual API call with the competition key. The bot is the only thing that uses it.

## 13. Competition switch: xsmom on R1 -> s3v2e on core10 (config_competition_s3v2e.yaml)

> **DONE 2026-10-07:** the xsmom bot was flattened via `KILL_competition` (09:55-10:00 UTC) and stopped (session removed).
> **The LIVE competition bot is `config_competition_s3v2e.yaml`, tmux session `competition_s3v2e`, since 10:04 UTC.**
> Section 12 (xsmom on R1) is history; do not start it again unless the team decides a rollback.

**Why (team decision 2026-10-07):** under the new objective (risk-adjusted composite, positive mean 14d return in down
windows, OOS Sharpe >= 1, P(14d <= -10%) <= 5%, worst 14d >= -15%), the live xsmom R1 fails: OOS Sharpe -0.79, mean 14d
return in down windows -3.2% OOS. s3v2e_core10 meets every requirement in both halves (`strategy_lab/leaderboard_b5.md`,
stats card `strategy_lab/reports/stats_card_s3v2e_core10_competition.md`).

`config_competition_s3v2e.yaml`: s3v2 with EWMA vol (halflife 168h) on the core10 universe, band 0.06, minimal activity
guard, drawdown brake on, shorts on (half size while BTC > its 14-day mean), full equity, competition key from
`.env.competition`. It has its **own fresh** `logs_competition_s3v2e/`, `state_competition_s3v2e/` and
`KILL_competition_s3v2e`; it never reads the xsmom bot's state. Tested offline by `tests/test_competition_s3v2e.py`
(lab parity, 30-day replay, restart, old-bot KILL flatten) and `tests/test_safety.py`.

**0. Update the code (the running bots keep the code they loaded at start; a pull does not change them):**
```bash
cd ~/Trading_Competition && git pull && cd strategy_bot && .venv/bin/python -m tests.test_safety
```

**(a) Let the old bot flatten itself (it must sell all its coins, incl. those outside core10 such as NEAR):**
```bash
cd ~/Trading_Competition/strategy_bot && touch KILL_competition
```
It reacts within one poll (about 1 minute). With limit orders, each sale can rest up to 5 minutes before the market
fallback, so allow up to about 30 minutes for 5 coins.

**(b) Confirm it is flat:**
```bash
.venv/bin/python status.py --config config_competition.yaml      # KILL=PRESENT, every actual weight ~0 (dust only)
tail -n 20 logs_competition/orders.jsonl                         # the SELL orders and their fills
grep -c '"error"' logs_competition/orders.jsonl; tail -n 5 logs_competition/errors.jsonl
```
Dust below the minimum order (a few cents to about $1 per coin) can stay; it cannot be traded. If any coin still shows a
real weight, wait for the next poll and check again. Do not stop the bot while orders are resting.

**(c) Stop the old bot (leave `KILL_competition` in place, so the old config can never trade again by accident):**
```bash
tmux send-keys -t competition C-c; sleep 5; tmux ls      # "competition" must be gone (else: tmux kill-session -t competition)
```

**(d) Start the new bot in its own tmux session:**
```bash
tmux new-session -d -s competition_s3v2e -c /home/ec2-user/Trading_Competition/strategy_bot '.venv/bin/python bot.py --config config_competition_s3v2e.yaml --live'
```
- 10-second COMPETITION KEY warning, then it loads 2000 hourly bars for the 10 coins (about 1 minute).
- **First start:** no saved targets exist in `state_competition_s3v2e/`, so it computes fresh targets immediately (decision
  log `targets` with reason `first start`) and trades only toward them: a pair trades if its weight is more than 6 pp off
  target, so small targets wait (same rule as the backtest). Afterwards targets are recomputed daily at 00:00 UTC, the
  band check runs hourly, and the minimal activity guard makes one small trade at 20:00 UTC if nothing traded that day.

**Check:**
```bash
tmux ls; .venv/bin/python status.py --config config_competition_s3v2e.yaml
tail -n 30 logs_competition_s3v2e/bot.log; grep '"first start"' logs_competition_s3v2e/decisions.jsonl | tail -n 1
```

**Stop / kill switch (new bot):** graceful stop `tmux send-keys -t competition_s3v2e C-c`; flatten and idle
`touch KILL_competition_s3v2e` (delete it to resume). **Rollback** to xsmom: stop the new bot, `rm KILL_competition`, and
start section 12's command (its books in `state_competition/` are flat after step a; at start it re-enters the targets of
its last 15:00 UTC decision).

## 14. Forward test on the TESTING key: s3v2e + HMM2 + CUSUM cut (config_testing_hmm_cusum.yaml)

Plan and switch criteria: `../strategy_lab/reports/forward_test_plan.md`. Tests: `tests/test_hmm_cusum.py`. **The live
competition bot (`competition_s3v2e`) is not touched by any step below.**

**One account, one bot:** the testing key is one Roostoo account, so the current testing bot (tmux `strategy`,
`config.yaml`, sleeves s3v2 + xsmom) must be flattened and stopped first. The new bot refuses to start while another bot's
fresh heartbeat shows the same key label running live (`allow_shared_account: false`).

**0. Update the code and install the extra packages (the running bots keep the code they loaded):**
```bash
cd ~/Trading_Competition && git pull && cd strategy_bot
.venv/bin/pip install -r requirements-forward-test.txt        # hmmlearn, scikit-learn, scipy (forward test only)
.venv/bin/python -m tests.test_safety
```

**1. Flatten and stop the old testing bot:**
```bash
touch KILL                                     # the old testing bot (config.yaml) sells everything itself
.venv/bin/python status.py                     # wait until KILL=PRESENT and every actual weight ~0 (allow up to ~30 min)
tmux send-keys -t strategy C-c; sleep 15; tmux ls     # "strategy" must be gone (else: tmux kill-session -t strategy)
```
Leave `KILL` in place so the old config cannot trade again by accident. A heartbeat stays "fresh" for 10 minutes after
the stop; if step 2 refuses with "another bot is running LIVE on the same key", wait 10 minutes and start again.

**2. Start the forward test in its own tmux session:**
```bash
tmux new-session -d -s testing_hmm -c /home/ec2-user/Trading_Competition/strategy_bot '.venv/bin/python bot.py --config config_testing_hmm_cusum.yaml --live'
```
- First start: loads 2000 hourly bars for the 10 coins, downloads BTC hourly closes since 2020 for the HMM (about 60 Binance
  requests, about 1 minute; cached in `state_testing_hmm/btc_1h_since_2020.csv`), fits the month's HMM (about 10 seconds,
  saved in `state_testing_hmm/hmm2_model.json`), computes fresh targets and trades toward them.
- Daily targets at 01:00 UTC (the bar opening 00:00, the lab convention); CUSUM cut checks every hour; the HMM refits on the
  1st of each month.

**3. Check:**
```bash
tmux ls; .venv/bin/python status.py --config config_testing_hmm_cusum.yaml     # incl. HMM p_crisis and active CUSUM cuts
tail -n 30 logs_testing_hmm/bot.log
.venv/bin/python daily_check.py      # once a day: forward test, old testing config and the live bot side by side
```

**Stop / kill switch:** graceful stop `tmux send-keys -t testing_hmm C-c`; flatten and idle `touch KILL_testing_hmm`.
**Back to the old testing bot:** stop this one, `rm KILL`, start section 6's `strategy` command.

## 15. News risk layer, SHADOW mode on the testing forward-test bot (`testing_hmm`)

The layer is in `config_testing_hmm_cusum.yaml` with `news_layer: {enabled: true, shadow: true}`: trading is unchanged,
would-be changes go to `logs_testing_hmm/news_shadow.jsonl`. **Never on the competition bot** until the shadow log has been
reviewed (`tests/test_safety.py` fails if a competition config enables it). Design: README "News risk layer".

**1. Keys (testing `.env` only; never in chat or git):**
```bash
cd ~/Trading_Competition/strategy_bot && nano .env
#   NEWS_LLM_API_KEY=<Anthropic API key for the news classifier>
#   CRYPTOPANIC_TOKEN=<CryptoPanic API token>        (optional; without it only RSS + Fear & Greed are used)
chmod 600 .env; git check-ignore -v .env           # must print the ignore rule
```

**2. Update and restart the forward-test bot (restart-safe: targets, CUSUM cuts and the HMM model are restored):**
```bash
cd ~/Trading_Competition && git pull && cd strategy_bot && .venv/bin/python -m tests.test_safety
tmux send-keys -t testing_hmm C-c; sleep 15; tmux ls        # "testing_hmm" gone (else: tmux kill-session -t testing_hmm)
tmux new-session -d -s testing_hmm -c /home/ec2-user/Trading_Competition/strategy_bot '.venv/bin/python bot.py --config config_testing_hmm_cusum.yaml --live'
```

**3. Check (first news refresh within ~1 minute of the first poll, then every 15 minutes):**
```bash
.venv/bin/python status.py --config config_testing_hmm_cusum.yaml     # "News layer (SHADOW)" line + last 5 shadow decisions
tail -n 5 logs_testing_hmm/news_shadow.jsonl; grep '"news:' logs_testing_hmm/errors.jsonl | tail -n 5
```
If `NEWS_LLM_API_KEY` is missing, the bot logs a warning and fetches headlines without classifying them (no vetoes);
calendar and Fear & Greed rules still run in shadow.

**4. After 3 days:**
```bash
.venv/bin/python news_shadow_report.py --config config_testing_hmm_cusum.yaml --days 3
```
Vetoes with what each coin did (false alarm or not), how often the calendar / Fear & Greed rules fired, LLM cost, and the
would-be P&L difference.

**Turn it off:** set `news_layer: {enabled: false}` and restart, or stop the bot. The layer never changes trades in shadow mode.
