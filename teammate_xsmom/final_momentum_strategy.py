"""Final competition strategy: fixed-clock 24h cross-sectional momentum.

This is the finalized research/backtest implementation to share with the team.
It contains ONLY the selected strategy (no defensive 2h trading layer).

Strategy
--------
Data: hourly close prices.
Decision time: 14:00 UTC every day.
Execution assumption: signal at 14:00 executes at 15:00 (1h delay).
Universe: fixed 10-asset research universe.
Eligibility: EMA24 > EMA168 and 72h momentum > +2%.
Ranking: 72h momentum / 72h realized volatility.
Portfolio: top 5 eligible assets, 15% each, max risky exposure 75%, rest cash.
Rebalance: once per 24h at the fixed daily clock.
Fees: 0.1% taker fee in the backtest.
No leverage, no shorting, no forced end-of-window liquidation.

Important
---------
The 14:00 UTC clock and frozen historical sample are intentional. Do not make the
rebalance clock depend on when the script is launched; that changes the strategy.
"""

import numpy as np
import pandas as pd
import asset_selection_research as research


# -----------------------------------------------------------------------------
# Final fixed strategy parameters
# -----------------------------------------------------------------------------

UNIVERSE = ["ZEC", "PAXG", "POL", "ICP", "TRX", "LISTA", "STO", "CAKE", "TUT", "SOL"]

INITIAL_CAPITAL = 100_000.0
FEE_RATE = 0.001

FAST_EMA = 24
SLOW_EMA = 168
MOMENTUM_HOURS = 72
MOMENTUM_THRESHOLD = 0.02
VOLATILITY_HOURS = 72
TOP_N = 5

MAX_ASSET_WEIGHT = 0.15
MAX_RISKY_EXPOSURE = 0.75

DAILY_SIGNAL_HOUR_UTC = 14

# Reproducible research sample: 54 overlapping 14-day windows, stepped weekly.
WINDOW_DAYS = 14
WINDOW_STEP_DAYS = 7
FIRST_WINDOW_START_UTC = pd.Timestamp("2025-09-10 14:00:00+00:00")
LAST_WINDOW_START_UTC = pd.Timestamp("2026-09-16 14:00:00+00:00")
BACKTEST_DATA_START_UTC = FIRST_WINDOW_START_UTC - pd.Timedelta(
    hours=SLOW_EMA + MOMENTUM_HOURS
)
BACKTEST_DATA_END_UTC = LAST_WINDOW_START_UTC + pd.Timedelta(
    hours=WINDOW_DAYS * 24 - 1
)


# -----------------------------------------------------------------------------
# Signal construction
# -----------------------------------------------------------------------------

def is_daily_signal_time(timestamp: pd.Timestamp) -> bool:
    """True only at the fixed 14:00 UTC alpha decision time."""
    return timestamp.minute == 0 and timestamp.hour == DAILY_SIGNAL_HOUR_UTC


def validate_target(target) -> None:
    values = np.asarray(target, dtype=float)
    assert np.isfinite(values).all(), "NaN/infinite target"
    assert (values >= -1e-12).all(), "Negative risky target"
    assert (values <= MAX_ASSET_WEIGHT + 1e-12).all(), "Per-asset cap exceeded"
    assert values.sum() <= MAX_RISKY_EXPOSURE + 1e-12, "Risky exposure cap exceeded"


def momentum_components(prices: pd.DataFrame):
    """Compute all features used by the final strategy from hourly closes."""
    returns = prices.pct_change(fill_method=None)

    fast = prices.ewm(
        span=FAST_EMA,
        adjust=False,
        min_periods=FAST_EMA,
    ).mean()

    slow = prices.ewm(
        span=SLOW_EMA,
        adjust=False,
        min_periods=SLOW_EMA,
    ).mean()

    momentum = prices / prices.shift(MOMENTUM_HOURS) - 1.0
    volatility = returns.rolling(VOLATILITY_HOURS).std()
    ready = prices.rolling(SLOW_EMA).count().eq(SLOW_EMA)

    score = momentum / volatility.replace(0.0, np.nan)

    return {
        "fast_ema": fast,
        "slow_ema": slow,
        "momentum_72h": momentum,
        "volatility_72h": volatility,
        "ready": ready,
        "score": score,
    }


def build_momentum_targets(prices: pd.DataFrame):
    """Return hourly target rows; only 14:00 UTC rows are used for trading.

    Each selected asset receives exactly 15%. If fewer than five assets qualify,
    unused capital remains in cash.
    """
    c = momentum_components(prices)

    eligible = (
        (c["fast_ema"] > c["slow_ema"])
        & (c["momentum_72h"] > MOMENTUM_THRESHOLD)
        & c["ready"]
    )

    ranked = c["score"].where(eligible).rank(
        axis=1,
        ascending=False,
        method="first",
    )

    targets = (ranked <= TOP_N).astype(float) * MAX_ASSET_WEIGHT

    for row in targets.to_numpy():
        validate_target(row)

    return targets, c


def target_at_signal_time(prices: pd.DataFrame, timestamp: pd.Timestamp) -> pd.Series:
    """Convenience helper for live/integration work.

    `prices` must contain hourly history through `timestamp` and must not contain
    future information. This function computes the final portfolio target at that
    timestamp; call it only when `is_daily_signal_time(timestamp)` is True.
    """
    if not is_daily_signal_time(timestamp):
        raise ValueError(
            f"Final strategy only creates alpha targets at {DAILY_SIGNAL_HOUR_UTC:02d}:00 UTC"
        )

    prices = prices[UNIVERSE].sort_index().loc[:timestamp]
    if timestamp not in prices.index:
        raise ValueError("Signal timestamp is not present in hourly price history")

    targets, components = build_momentum_targets(prices)
    if not components["ready"].loc[timestamp].all():
        raise ValueError("Insufficient history for EMA168 / strategy warmup")

    target = targets.loc[timestamp].copy()
    validate_target(target)
    return target


# -----------------------------------------------------------------------------
# Realistic holdings ledger
# -----------------------------------------------------------------------------

def mark_to_market(cash, quantity, current_prices):
    asset_values = quantity * current_prices
    portfolio_value = float(cash + asset_values.sum())
    assert portfolio_value > 0.0
    return asset_values, portfolio_value


def execute_target(cash, quantity, current_prices, target_weights, fee_rate):
    """Rebalance to target weights at current execution prices."""
    validate_target(target_weights)

    current_asset_values, before = mark_to_market(cash, quantity, current_prices)
    desired_asset_values = np.asarray(target_weights, dtype=float) * before

    trades = desired_asset_values - current_asset_values
    traded_notional = float(np.abs(trades).sum())
    fee = float(fee_rate * traded_notional)

    new_quantity = desired_asset_values / current_prices
    new_cash = float(before - desired_asset_values.sum() - fee)
    assert new_cash >= -1e-8, "Insufficient cash for fees"

    new_asset_values, after = mark_to_market(new_cash, new_quantity, current_prices)
    assert np.isclose(after, before - fee, rtol=1e-12, atol=1e-8)

    return new_cash, new_quantity, traded_notional, fee, new_asset_values, before


def window_day_bucket(timestamp, start):
    hours = int((timestamp - start) / pd.Timedelta(hours=1))
    return hours // 24


def holdings_ledger(prices: pd.DataFrame, targets: pd.DataFrame, fee_rate: float):
    """Backtest the final strategy with natural holdings drift.

    A signal at 14:00 UTC executes at the next hourly bar (15:00 UTC).
    Quantities stay unchanged between daily rebalances.
    """
    assert prices.index.equals(targets.index)
    assert prices.notna().all().all()
    assert (prices > 0).all().all()

    cash = float(INITIAL_CAPITAL)
    quantity = np.zeros(len(prices.columns), dtype=float)
    previous_value = float(INITIAL_CAPITAL)
    start = prices.index[0]
    records = []

    for hour, timestamp in enumerate(prices.index):
        current_prices = prices.iloc[hour].to_numpy(dtype=float)
        old_quantity = quantity.copy()
        asset_values, before = mark_to_market(cash, quantity, current_prices)

        traded_notional = 0.0
        fee = 0.0
        decision_check = 0
        trade_check = 0

        signal_time = prices.index[hour - 1] if hour >= 1 else None

        if hour >= 1 and is_daily_signal_time(signal_time):
            decision_check = 1
            assert timestamp == signal_time + pd.Timedelta(hours=1), "LOOKAHEAD: execution delay"

            target = targets.iloc[hour - 1].to_numpy(dtype=float)
            cash, quantity, traded_notional, fee, asset_values, _ = execute_target(
                cash,
                quantity,
                current_prices,
                target,
                fee_rate,
            )
            trade_check = int(traded_notional > 1e-8)
        else:
            assert np.array_equal(quantity, old_quantity), "Holdings changed off-schedule"

        asset_values, after = mark_to_market(cash, quantity, current_prices)
        if fee == 0.0:
            assert np.isclose(after, before, rtol=1e-12, atol=1e-8)

        records.append(
            {
                "value": after,
                "return": after / previous_value - 1.0,
                "turnover": traded_notional / before if before > 0 else 0.0,
                "fee": fee,
                "traded_notional": traded_notional,
                "decision_check": decision_check,
                "trade_check": trade_check,
                "day_bucket": window_day_bucket(timestamp, start),
                "risky_exposure": float(asset_values.sum() / after),
                "cash_weight": float(cash / after),
                "assets": int(np.count_nonzero(asset_values / after > 1e-4)),
            }
        )
        previous_value = after

    return pd.DataFrame(records, index=prices.index)


# -----------------------------------------------------------------------------
# Metrics and frozen-window evaluation
# -----------------------------------------------------------------------------

def simulate(prices: pd.DataFrame, targets: pd.DataFrame):
    net = holdings_ledger(prices, targets, FEE_RATE)
    gross = holdings_ledger(prices, targets, 0.0)

    wealth = net["value"]
    peak = wealth.cummax().clip(lower=INITIAL_CAPITAL)
    max_drawdown = float((wealth / peak - 1.0).min())
    net_return = float(wealth.iloc[-1] / INITIAL_CAPITAL - 1.0)

    traded = net["traded_notional"] > 1e-8
    active_days = int(net.loc[traded, "day_bucket"].nunique())
    assert 0 <= active_days <= WINDOW_DAYS

    trade_checks = int(net["trade_check"].sum())
    decision_checks = int(net["decision_check"].sum())

    return {
        "net_return": net_return,
        "gross_return": float(gross["value"].iloc[-1] / INITIAL_CAPITAL - 1.0),
        "sharpe": research.sharpe_ratio(net["return"]),
        "sortino": research.sortino_ratio(net["return"]),
        "max_drawdown": max_drawdown,
        "window_calmar": net_return / abs(max_drawdown) if max_drawdown != 0 else np.nan,
        "turnover": float(net["turnover"].sum()),
        "fee_drag": float(net["fee"].sum() / INITIAL_CAPITAL),
        "active_days": active_days,
        "avg_risky_exposure": float(net["risky_exposure"].mean()),
        "avg_cash_weight": float(net["cash_weight"].mean()),
        "avg_assets": float(net["assets"].mean()),
        "decision_checks": decision_checks,
        "trade_checks": trade_checks,
        "skip_rate": 1.0 - trade_checks / decision_checks if decision_checks else np.nan,
    }


def evaluate_frozen_windows(prices: pd.DataFrame):
    prices = prices[UNIVERSE].sort_index()
    fixed_index = pd.date_range(BACKTEST_DATA_START_UTC, BACKTEST_DATA_END_UTC, freq="h")
    prices = prices.reindex(fixed_index)

    hourly_returns = prices.pct_change(fill_method=None)
    targets_all, components = build_momentum_targets(prices)

    starts = pd.date_range(
        FIRST_WINDOW_START_UTC,
        LAST_WINDOW_START_UTC,
        freq=f"{WINDOW_STEP_DAYS}D",
    )
    assert len(starts) == 54, f"Expected 54 frozen windows, got {len(starts)}"
    assert (starts.hour == DAILY_SIGNAL_HOUR_UTC).all(), "Backtest clock drifted"

    rows = []
    for start in starts:
        idx = pd.date_range(start, periods=WINDOW_DAYS * 24, freq="h")

        if not components["ready"].loc[start, UNIVERSE].all():
            continue
        if not hourly_returns.loc[idx, UNIVERSE].notna().all().all():
            continue

        result = simulate(
            prices.loc[idx, UNIVERSE],
            targets_all.loc[idx, UNIVERSE],
        )
        rows.append(
            {
                "start": start,
                "end": start + pd.Timedelta(days=WINDOW_DAYS),
                **result,
            }
        )

    if not rows:
        raise RuntimeError("No complete frozen-history windows")

    return pd.DataFrame(rows)


def print_summary(results: pd.DataFrame):
    net = results["net_return"]

    print("\nFINAL 24H MOMENTUM STRATEGY")
    print(f"Windows: {len(results)}")
    print(f"Positive windows: {(net > 0).mean():.1%}")
    print(f"Mean 14d net return: {net.mean():.2%}")
    print(f"Median 14d net return: {net.median():.2%}")
    print(f"Best 14d return: {net.max():.2%}")
    print(f"Worst 14d return: {net.min():.2%}")
    print(f"Mean Sharpe: {results['sharpe'].mean():.3f}")
    print(f"Median Sharpe: {results['sharpe'].median():.3f}")
    print(f"Mean Sortino: {results['sortino'].mean():.3f}")
    print(f"Median Sortino: {results['sortino'].median():.3f}")
    print(f"Mean window Calmar: {results['window_calmar'].mean():.3f}")
    print(f"Average max drawdown: {results['max_drawdown'].mean():.2%}")
    print(f"Worst max drawdown: {results['max_drawdown'].min():.2%}")
    print(f"Average turnover: {results['turnover'].mean():.3f}")
    print(f"Average fee drag: {results['fee_drag'].mean():.2%}")
    print(f"Average active days: {results['active_days'].mean():.2f}")
    print(f"Windows with >=8 active days: {(results['active_days'] >= 8).mean():.1%}")
    print(f"Average risky exposure: {results['avg_risky_exposure'].mean():.2%}")
    print(f"Average cash weight: {results['avg_cash_weight'].mean():.2%}")
    print(f"Average assets held: {results['avg_assets'].mean():.2f}")


# -----------------------------------------------------------------------------
# Research runner
# -----------------------------------------------------------------------------

def main():
    print("FINAL STRATEGY: fixed-clock 24h Momentum", flush=True)
    print("UNIVERSE:", UNIVERSE, flush=True)
    print(
        f"Signal={DAILY_SIGNAL_HOUR_UTC:02d}:00 UTC daily; execute one hour later; "
        f"EMA={FAST_EMA}/{SLOW_EMA}h; momentum72>{MOMENTUM_THRESHOLD:.0%}; "
        f"score=momentum72/vol72; top {TOP_N}; 15% each; max risky=75%; fee={FEE_RATE:.1%}",
        flush=True,
    )
    print(
        f"Frozen research windows: {FIRST_WINDOW_START_UTC} -> {LAST_WINDOW_START_UTC}",
        flush=True,
    )

    missing = set(UNIVERSE) - set(research.get_roostoo_crypto_universe())
    if missing:
        raise RuntimeError(f"Fixed assets unavailable on Roostoo: {sorted(missing)}")

    series = []
    for i, coin in enumerate(UNIVERSE, 1):
        print(f"[{i}/{len(UNIVERSE)}] {coin}USDT...", end="", flush=True)
        data = research.download_binance_close(coin, research.DOWNLOAD_DAYS + 1)
        if data is None:
            raise RuntimeError(f"Missing Binance data: {coin}")
        print(f" OK ({len(data)} hours)", flush=True)
        series.append(data)

    prices = pd.concat(series, axis=1).sort_index()

    if prices.index.min() > BACKTEST_DATA_START_UTC or prices.index.max() < BACKTEST_DATA_END_UTC:
        raise RuntimeError(
            "Downloaded history does not cover frozen sample: "
            f"need {BACKTEST_DATA_START_UTC} -> {BACKTEST_DATA_END_UTC}, "
            f"got {prices.index.min()} -> {prices.index.max()}"
        )

    prices = prices.loc[BACKTEST_DATA_START_UTC:BACKTEST_DATA_END_UTC]
    results = evaluate_frozen_windows(prices)
    results.to_csv("final_momentum_backtest.csv", index=False)
    print_summary(results)
    print("Saved final_momentum_backtest.csv", flush=True)


if __name__ == "__main__":
    main()
