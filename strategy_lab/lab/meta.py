"""Block 6 track D: meta-labeling of s3v2e_core10 (walk-forward LightGBM), predictions in data/meta/.

    python -m lab.meta          # dataset + walk-forward predictions + feature importance / calibration report

Samples: every daily decision (the 00:00 UTC bar, closes up to and including it, last 800 bars as the live strategy) and
every core10 coin with a non-zero s3v2e target (b3_s3v2e_core10 params). Label: sign(target) x (close 72h later / close - 1)
- 0.0024 (round trip: 2 x (0.10% taker + 2 bps)) > 0, i.e. the position was profitable over the next 3 days net of costs.
Features (all from data up to the decision bar): trend t-stats at 24 / 72 / 168 / 336h (log return / (std of 336 hourly
returns x sqrt(h))) signed by the position; EWMA vol (168h, annualised); vol-of-vol (std / mean of the daily EWMA vol over
30 days); breadth (share of core10 above their 30-day mean); 30-day BTC beta (hourly); 30-day correlation state (average
pairwise correlation of core10); changepoint score against the position (BOCPD P(change within 6h), lab/changepoint.py);
hours since the coin's target last changed sign; side (+1 / -1).
Walk-forward: for each calendar month M from the first month with >= 6 months of samples: train on samples with decision
time < M - 3 days (purge: the 3-day label window never reaches into M), expanding window; LightGBM (fixed params below)
fitted on the first 75% (time order) of the training samples, isotonic calibration on the last 25%; predictions for every
sample in M. Months before the first fit get no prediction (the strategy then keeps the s3v2e size).
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.changepoint import bocpd, standardized
from lab.data import load_close
from lab.runner import resolve_base

OUT = ROOT / "data" / "meta"
CORE = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "DOGEUSDT", "AVAXUSDT", "LINKUSDT", "DOTUSDT"]
FEATS = ["t24", "t72", "t168", "t336", "ewma_vol", "vol_of_vol", "breadth", "beta", "corr_state", "cp_score",
         "h_since_change", "side"]
LGB = dict(n_estimators=300, learning_rate=0.03, num_leaves=15, min_child_samples=50, subsample=0.8, subsample_freq=1,
           colsample_bytree=0.8, random_state=0, verbose=-1)
COST = 0.0024


def dataset() -> pd.DataFrame:
    from lab.strategies import get_strategy
    c = load_close(CORE)
    s3 = get_strategy("s3v2x")
    p = resolve_base("b3_s3v2e_core10")["params"]
    r = c.pct_change()
    lr = np.log(c).diff()
    ev = r.ewm(halflife=168).std() * np.sqrt(8760)
    ev_d = ev.resample("1D").last()
    vov = (ev_d.rolling(30).std() / ev_d.rolling(30).mean())
    sma30 = c.rolling(720).mean()
    z = standardized(c)
    dn, up = bocpd(z)
    dn, up = pd.DataFrame(dn, index=c.index, columns=c.columns), pd.DataFrame(up, index=c.index, columns=c.columns)
    rows, last_sign, since = [], {a: 0 for a in CORE}, {a: None for a in CORE}
    idx = c.index
    for i in np.where((idx.hour == 0) & (idx >= idx[0] + pd.Timedelta(hours=800)))[0]:
        t = idx[i]
        win = c.iloc[i - 799:i + 1]
        try:
            w = s3.target_weights(win, p)
        except ValueError:
            continue
        sd = lr.iloc[i - 335:i + 1].std()
        alive = [a for a in CORE if pd.notna(c.iat[i, c.columns.get_loc(a)])]
        br = float((c.loc[t, alive] > sma30.loc[t, alive]).mean()) if alive else np.nan
        rw = r.iloc[i - 719:i + 1]
        cm = rw[alive].corr().values if len(alive) > 2 else None
        corr_state = float(cm[np.triu_indices_from(cm, 1)].mean()) if cm is not None else np.nan
        btc = rw["BTCUSDT"]
        for a in CORE:
            sgn = int(np.sign(w.get(a, 0.0)))
            if sgn != last_sign[a]:
                last_sign[a], since[a] = sgn, t
            if sgn == 0 or i + 72 >= len(idx) or pd.isna(c.iat[i + 72, c.columns.get_loc(a)]):
                continue
            ret3 = c.iat[i + 72, c.columns.get_loc(a)] / c.iat[i, c.columns.get_loc(a)] - 1
            row = {"time": t, "asset": a, "side": sgn, "weight": w[a], "label": int(sgn * ret3 - COST > 0),
                   "fwd_net": sgn * ret3 - COST}
            for h in (24, 72, 168, 336):
                row[f"t{h}"] = float(sgn * np.log(c.iat[i, c.columns.get_loc(a)] / c.iat[i - h, c.columns.get_loc(a)])
                                     / (sd[a] * np.sqrt(h)))
            row["ewma_vol"] = float(ev.iat[i, c.columns.get_loc(a)])
            row["vol_of_vol"] = float(vov[a].asof(t.floor("D") - pd.Timedelta(days=1)))
            row["breadth"] = br
            row["beta"] = float(rw[a].cov(btc) / btc.var()) if btc.var() > 0 else np.nan
            row["corr_state"] = corr_state
            row["cp_score"] = float((dn if sgn > 0 else up).iat[i, c.columns.get_loc(a)])
            row["h_since_change"] = float((t - since[a]) / pd.Timedelta(hours=1))
            rows.append(row)
    return pd.DataFrame(rows)


def walk_forward(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    import lightgbm as lgb
    from sklearn.isotonic import IsotonicRegression
    preds, imps = [], []
    t0 = df["time"].min()
    for ms in pd.date_range((t0 + pd.DateOffset(months=6)).floor("D").replace(day=1) + pd.DateOffset(months=1),
                            df["time"].max(), freq="MS"):
        train = df[df["time"] < ms - pd.Timedelta(days=3)].sort_values("time")
        test = df[(df["time"] >= ms) & (df["time"] < ms + pd.DateOffset(months=1))]
        if len(test) == 0 or len(train) < 200:
            continue
        cut = int(len(train) * 0.75)
        fit, cal = train.iloc[:cut], train.iloc[cut:]
        m = lgb.LGBMClassifier(**LGB)
        m.fit(fit[FEATS], fit["label"])
        iso = IsotonicRegression(out_of_bounds="clip", y_min=0.0, y_max=1.0)
        iso.fit(m.predict_proba(cal[FEATS])[:, 1], cal["label"])
        p = iso.predict(m.predict_proba(test[FEATS])[:, 1])
        preds.append(test[["time", "asset", "side", "label", "fwd_net"]].assign(p=p, raw=m.predict_proba(test[FEATS])[:, 1],
                                                                             month=ms))
        imps.append(pd.Series(m.booster_.feature_importance("gain"), index=FEATS, name=ms))
        print(f"  {ms:%Y-%m}: train {len(train)} (fit {len(fit)} / cal {len(cal)}), test {len(test)}", flush=True)
    return pd.concat(preds), pd.DataFrame(imps)


def report(pr: pd.DataFrame, imp: pd.DataFrame, n_all: int) -> None:
    from lab.b3 import IS_END, OOS0, OOS_END
    L = ["# Track D: meta-labeling diagnostics (walk-forward, out-of-sample predictions only)\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by `python -m lab.meta`. {n_all} samples, {len(pr)} with an "
         f"out-of-sample prediction (first prediction month {pr['month'].min():%Y-%m})._\n",
         "## Feature importance (LightGBM gain, share, mean over folds)\n", "| feature | share |", "|---|---|"]
    share = (imp.div(imp.sum(axis=1), axis=0)).mean().sort_values(ascending=False)
    L += [f"| {f} | {v:.1%} |" for f, v in share.items()]
    L += ["\n## Calibration (predicted probability bins vs realised share of profitable positions)\n",
          "| period | bin | n | mean predicted | realised | mean net 3d return |", "|---|---|---|---|---|---|"]
    for k, (a, b) in {"IS": (None, IS_END), "OOS": (OOS0, OOS_END)}.items():
        x = pr[(pr["time"] >= (a or pr["time"].min())) & (pr["time"] <= b)]
        bins = pd.cut(x["p"], [0, 0.4, 0.45, 0.5, 0.55, 0.6, 1.0], include_lowest=True)
        for bn, g in x.groupby(bins, observed=True):
            L.append(f"| {k} | {bn} | {len(g)} | {g['p'].mean():.2f} | {g['label'].mean():.2f} | {g['fwd_net'].mean():+.2%} |")
        base = x["label"].mean()
        try:
            from sklearn.metrics import roc_auc_score
            auc = roc_auc_score(x["label"], x["p"])
        except ValueError:
            auc = float("nan")
        L.append(f"| {k} | all | {len(x)} | {x['p'].mean():.2f} | {base:.2f} | {x['fwd_net'].mean():+.2%} (AUC {auc:.3f}) |")
    (ROOT / "reports" / "meta_track_d.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[-14:]))


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    df = dataset()
    df.to_pickle(ROOT / ".cache" / "meta_dataset.pkl")
    print(f"dataset: {len(df)} samples, positive share {df['label'].mean():.2f}", flush=True)
    pr, imp = walk_forward(df)
    pr[["time", "asset", "p"]].to_csv(OUT / "preds.csv", index=False)
    report(pr, imp, len(df))
    return 0


if __name__ == "__main__":
    sys.exit(main())
