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
| Startup | Clock sync. exchangeInfo check. Universe check: each pair must be crypto, `CanTrade`, and have live ticker data; pairs that fail are dropped and logged. 800 h of Binance closes are seeded per pair, or loaded from `state/bars.csv` with any missing hours topped up. Stale pending orders are cancelled. Then targets are computed and the first rebalance runs. |
| Every 60 s | One `ticker` call for all pairs, which updates the hourly bars. The heartbeat is written. |
| Each completed hour | An account snapshot (SpotWallet plus short positions), the drawdown brake, then a rebalance of every pair whose weight is more than 6 pp off target, or whose target is 0 while we still hold it. Reductions go first, then increases. |
| 00:00 UTC daily | S3v2 target weights are recomputed, and the full vector is logged. |
| 20:00 UTC | If nothing has traded today, the bot rebalances with a 1 pp band (activity guard). |
| Any time | A `KILL` file makes the bot flatten within one poll, then idle while the file exists. |

Orders are placed as a LIMIT at our side of the touch (maker 0.05%). After 5 minutes the bot cancels and sends a MARKET order for the remainder. Shorts go through `/v6` with collateral. A timed-out order request is never resent: the bot looks the order up and cancels it, and the next hour re-reads the account.

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
- `targets (first start): {...}` and `[DRY RUN] ...` order lines
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

Restarts are safe. State lives in `state/`: bars, the risk brake's peak and cool-off, and the last trade day. The account itself is always re-read from the exchange. Stale pending orders are cancelled on start.

## 11. Adding a strategy (teammates)

1. Create `strategies/<name>.py`, subclassing `strategies.base.Strategy`, and implement `target_weights(closes, cfg) -> {pair: signed weight}` with gross ≤ 1.
2. Register it in `strategies/__init__.py`.
3. Set `strategy.name: <name>` (plus its params) in `config.yaml`.
4. Run `python -m tests.test_replay`. Execution, risk, caps and logging are shared and need no changes.
