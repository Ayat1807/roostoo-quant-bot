import requests
import pandas as pd
import numpy as np
import time


# ============================================================
# SETTINGS
# ============================================================

INITIAL_CAPITAL = 100_000
TAKER_FEE = 0.001
TOP_N = 5
MAX_WEIGHT = 0.15

FAST_EMA = 24
SLOW_EMA = 168
MOMENTUM_HOURS = 72
MOMENTUM_THRESHOLD = 0.02

REBALANCE_HOURS = 24

DOWNLOAD_DAYS = 400


ROOSTOO_EXCHANGE_INFO = (
    "https://mock-api.roostoo.com/v3/exchangeInfo"
)

BINANCE_KLINES = (
    "https://data-api.binance.vision/api/v3/klines"
)


# ============================================================
# GET CURRENT ROOSTOO CRYPTO UNIVERSE
# ============================================================

def get_roostoo_crypto_universe():

    response = requests.get(
        ROOSTOO_EXCHANGE_INFO,
        timeout=20
    )

    response.raise_for_status()

    info = response.json()

    coins = []

    for pair, details in info["TradePairs"].items():

        if (
            details["CanTrade"]
            and details["AssetType"] == "crypto"
            and details["Unit"] == "USD"
        ):

            coins.append(
                details["Coin"]
            )

    return sorted(set(coins))


# ============================================================
# DOWNLOAD BINANCE HOURLY DATA
# ============================================================

def download_binance_close(
    coin,
    days=400
):

    symbol = f"{coin}USDT"

    end_time = int(
        time.time() * 1000
    )

    start_time = (
        end_time
        - days * 24 * 60 * 60 * 1000
    )

    rows = []

    current_start = start_time

    while current_start < end_time:

        params = {
            "symbol": symbol,
            "interval": "1h",
            "startTime": current_start,
            "endTime": end_time,
            "limit": 1000
        }

        try:

            response = requests.get(
                BINANCE_KLINES,
                params=params,
                timeout=20
            )

        except requests.RequestException:

            print(
                f"Network error for {symbol}"
            )

            return None


        if response.status_code != 200:

            # Usually means Binance does not have
            # this Roostoo asset.
            return None


        data = response.json()

        if not data:
            break


        rows.extend(data)

        current_start = (
            data[-1][0] + 1
        )


        if len(data) < 1000:
            break


        # Be polite to Binance API
        time.sleep(0.10)


    if len(rows) < 200:
        return None


    times = pd.to_datetime(
        [row[0] for row in rows],
        unit="ms",
        utc=True
    )

    closes = [
        float(row[4])
        for row in rows
    ]


    series = pd.Series(
        closes,
        index=times,
        name=coin
    )

    series = series[
        ~series.index.duplicated(
            keep="last"
        )
    ]

    return series



# Fixed research rules; do not tune against these results.
MIN_HISTORY_HOURS = 300 * 24
MIN_WINDOWS = 30
WINDOW_HOURS = 14 * 24
MIN_PAIR_HOURS = 90 * 24
CORRELATION_PENALTY = 0.25
SELECT_COUNT = 10
PERIODS_PER_YEAR = 24 * 365


def sharpe_ratio(r):
    std = r.std()
    return r.mean() / std * np.sqrt(PERIODS_PER_YEAR) if std > 0 else np.nan


def sortino_ratio(r):
    downside = r[r < 0]
    deviation = np.sqrt((downside ** 2).mean())
    return r.mean() / deviation * np.sqrt(PERIODS_PER_YEAR) if deviation > 0 else np.nan


def simulate_window(window_returns, window_targets):
    # Every competition starts in cash. Signals at t earn returns at t+1.
    targets = window_targets.copy()
    targets.iloc[np.arange(len(targets)) % REBALANCE_HOURS != 0] = np.nan
    executed = targets.ffill().fillna(0).shift(1).fillna(0)
    gross = (executed * window_returns).sum(axis=1)
    turnover = executed.diff().abs().sum(axis=1).fillna(0)
    fees = turnover * TAKER_FEE
    net = gross - fees
    wealth = (1 + net).cumprod()
    active_days = len(set(turnover.index[turnover > 1e-10].date))
    return {
        'start': window_returns.index[0],
        'end': window_returns.index[0] + pd.Timedelta(days=14),
        'net_return': wealth.iloc[-1] - 1,
        'gross_return': (1 + gross).prod() - 1,
        'sharpe': sharpe_ratio(net),
        'sortino': sortino_ratio(net),
        'max_drawdown': (wealth / wealth.cummax().clip(lower=1) - 1).min(),
        'turnover': turnover.sum(),
        'fee_drag': fees.sum(),
        'active_days': active_days,
        'avg_assets': (executed > 0).sum(axis=1).mean(),
    }


def summarize(windows):
    frame = pd.DataFrame(windows)
    return {
        'windows': len(frame),
        'positive_windows_pct': 100 * (frame.net_return > 0).mean(),
        'mean_return': frame.net_return.mean(),
        'median_return': frame.net_return.median(),
        'worst_return': frame.net_return.min(),
        'mean_sharpe': frame.sharpe.mean(),
        'median_sharpe': frame.sharpe.median(),
        'mean_sortino': frame.sortino.mean(),
        'median_sortino': frame.sortino.median(),
        'avg_max_drawdown': frame.max_drawdown.mean(),
    }


def main():
    coins = get_roostoo_crypto_universe()
    print(f'Roostoo crypto assets: {len(coins)}', flush=True)
    series_list = []
    for i, coin in enumerate(coins, 1):
        print(f'[{i}/{len(coins)}] Trying {coin}USDT...', end='', flush=True)
        data = download_binance_close(coin, DOWNLOAD_DAYS)
        print(' skipped' if data is None else f' OK ({len(data)} hours)', flush=True)
        if data is not None:
            series_list.append(data)
    if not series_list:
        raise RuntimeError('No Binance data downloaded.')
    last_hour = pd.Timestamp.now(tz='UTC').floor('h') - pd.Timedelta(hours=1)
    prices = pd.concat(series_list, axis=1).sort_index().loc[:last_hour]
    # Preserve missing history and missing candles; never backfill new listings.
    prices = prices.reindex(pd.date_range(prices.index.min(), prices.index.max(), freq='h'))
    returns = prices.pct_change(fill_method=None)
    ema_fast = prices.ewm(span=FAST_EMA, adjust=False, min_periods=FAST_EMA).mean()
    ema_slow = prices.ewm(span=SLOW_EMA, adjust=False, min_periods=SLOW_EMA).mean()
    momentum = prices / prices.shift(MOMENTUM_HOURS) - 1
    volatility = returns.rolling(72).std()
    # A complete trailing EMA-length price history is required at entry.
    ready = prices.rolling(SLOW_EMA).count().eq(SLOW_EMA)
    eligible = (ema_fast > ema_slow) & (momentum > MOMENTUM_THRESHOLD) & ready
    risk_adjusted_momentum = momentum / volatility.replace(0, np.nan)
    earliest = prices.index.min() + pd.Timedelta(hours=SLOW_EMA + MOMENTUM_HOURS)
    starts = pd.date_range(earliest, prices.index.max() - pd.Timedelta(hours=WINDOW_HOURS - 1), freq='7D')

    statistics = []
    valid_windows = {}
    for coin in prices.columns:
        asset_windows = []
        coin_returns = returns[[coin]]
        # Individual robustness evaluates the original binary trend/momentum signal
        # at 100% asset exposure, including the same fee and daily rebalance rules.
        coin_targets = eligible[[coin]].astype(float)
        for start in starts:
            idx = pd.date_range(start, periods=WINDOW_HOURS, freq='h')
            if not ready.at[start, coin] or not coin_returns.loc[idx, coin].notna().all():
                continue
            asset_windows.append(simulate_window(coin_returns.loc[idx], coin_targets.loc[idx]))
        history_hours = int(prices[coin].notna().sum())
        if asset_windows:
            row = {'asset': coin, **summarize(asset_windows)}
            row.update(history_hours=history_hours,
                       first_binance_candle=prices[coin].first_valid_index(),
                       last_binance_candle=prices[coin].last_valid_index(),
                       volatility=returns[coin].std(),
                       annualized_volatility=returns[coin].std() * np.sqrt(PERIODS_PER_YEAR),
                       substantial_coverage=history_hours >= MIN_HISTORY_HOURS and len(asset_windows) >= MIN_WINDOWS)
            statistics.append(row)
            valid_windows[coin] = {r['start'] for r in asset_windows}
    ranking = pd.DataFrame(statistics)
    if ranking.empty:
        raise RuntimeError('No assets have complete 14-day windows.')
    ranking['robust_score'] = np.nan
    covered = ranking.loc[ranking.substantial_coverage].copy()
    # Percentile ranks keep metrics on comparable scales; missing ratios score zero.
    score_weights = {'median_return': 0.25, 'positive_windows_pct': 0.20,
                     'median_sharpe': 0.15, 'median_sortino': 0.15,
                     'avg_max_drawdown': 0.15, 'history_hours': 0.10}
    score = pd.Series(0.0, index=covered.index)
    for metric, weight in score_weights.items():
        score += weight * covered[metric].rank(pct=True).fillna(0)
    # Explicit preference for a positive median; it cannot be offset by other metrics.
    score += (covered.median_return > 0).astype(float)
    ranking.loc[covered.index, 'robust_score'] = score
    ranking = ranking.sort_values(['robust_score', 'asset'], ascending=[False, True], na_position='last')
    ranking.to_csv('asset_ranking.csv', index=False)
    print('\nResearch coverage: at least 300 days and 30 complete windows.')
    print('Individual exposure: 100%; volatility is hourly return standard deviation.')
    print('Robust score: positive-median bonus + weighted percentile ranks.')
    print('\nTOP 25 ASSETS BY INDIVIDUAL ROBUSTNESS')
    print(ranking.loc[ranking.substantial_coverage].head(25).to_string(index=False))
    candidates = ranking.loc[ranking.substantial_coverage].set_index('asset')
    if len(candidates) < SELECT_COUNT:
        raise RuntimeError(f'Only {len(candidates)} assets meet fixed coverage rules; need 10.')
    correlations = returns.corr(min_periods=MIN_PAIR_HOURS)
    selected = [candidates.index[0]]
    selection_rows = [{'asset': selected[0], 'robust_score': candidates.at[selected[0], 'robust_score'],
                       'avg_correlation': 0.0, 'selection_score': candidates.at[selected[0], 'robust_score']}]
    while len(selected) < SELECT_COUNT:
        choices = []
        for coin in candidates.index:
            if coin in selected:
                continue
            pair_corr = correlations.loc[coin, selected]
            # Unknown correlations receive a conservative maximal penalty.
            avg_corr = pair_corr.fillna(1.0).mean()
            adjusted = candidates.at[coin, 'robust_score'] - CORRELATION_PENALTY * max(0.0, avg_corr)
            choices.append((adjusted, coin, avg_corr))
        adjusted, coin, avg_corr = sorted(choices, key=lambda x: (-x[0], x[1]))[0]
        selected.append(coin)
        selection_rows.append({'asset': coin, 'robust_score': candidates.at[coin, 'robust_score'],
                               'avg_correlation': avg_corr, 'selection_score': adjusted})
    selected_corr = correlations.loc[selected, selected]
    selected_corr.to_csv('selected10_correlation.csv')
    print('\nSELECTED DIVERSIFIED TOP 10')
    print(pd.DataFrame(selection_rows).to_string(index=False))
    print('\nSELECTED 10 HOURLY RETURN CORRELATIONS')
    print(selected_corr.round(3).to_string())

    scores = risk_adjusted_momentum[selected].where(eligible[selected])
    ranks = scores.rank(axis=1, ascending=False, method='first')
    targets = (ranks <= TOP_N).astype(float) * MAX_WEIGHT
    portfolio_windows = []
    for start in starts:
        # Compare a genuinely fixed universe only where all ten have complete data.
        if not all(start in valid_windows[coin] for coin in selected):
            continue
        idx = pd.date_range(start, periods=WINDOW_HOURS, freq='h')
        portfolio_windows.append(simulate_window(returns.loc[idx, selected], targets.loc[idx]))
    portfolio = pd.DataFrame(portfolio_windows)
    portfolio.to_csv('selected10_backtests.csv', index=False)
    print('\nSELECTED 10 PORTFOLIO SUMMARY')
    print('Research uses full-sample universe selection: results are in-sample, not an out-of-sample validation.')
    print('Windows overlap; their results are not independent. Signals use only current/past data.')
    if portfolio.empty:
        print('No complete common-history portfolio windows.')
        return
    summary = summarize(portfolio_windows)
    for name, value in summary.items():
        if name == 'windows':
            print(f'Number of windows: {value}')
        elif name == 'positive_windows_pct':
            print(f'Positive-window percentage: {value:.1f}%')
        elif 'return' in name or 'drawdown' in name:
            print(f'{name}: {value:.2%}')
        else:
            print(f'{name}: {value:.3f}')
    print(f'Best return: {portfolio.net_return.max():.2%}')
    print(f'Average turnover: {portfolio.turnover.mean():.3f}')
    print(f'Average fee drag: {portfolio.fee_drag.mean():.2%}')
    print(f'Average active trading days: {portfolio.active_days.mean():.2f}')
    print(f'Windows with at least 8 active trading days: {(portfolio.active_days >= 8).mean():.1%}')


if __name__ == '__main__':
    main()
