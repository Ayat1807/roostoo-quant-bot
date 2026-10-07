# Track D: meta-labeling diagnostics (walk-forward, out-of-sample predictions only)

_Generated 2026-10-07 10:37 UTC by `python -m lab.meta`. 18759 samples, 17589 with an out-of-sample prediction (first prediction month 2020-09)._

## Feature importance (LightGBM gain, share, mean over folds)

| feature | share |
|---|---|
| corr_state | 25.5% |
| ewma_vol | 9.5% |
| breadth | 8.7% |
| vol_of_vol | 8.6% |
| t336 | 8.3% |
| t24 | 7.3% |
| beta | 7.2% |
| t72 | 7.1% |
| t168 | 6.7% |
| h_since_change | 4.6% |
| side | 3.3% |
| cp_score | 3.2% |

## Calibration (predicted probability bins vs realised share of profitable positions)

| period | bin | n | mean predicted | realised | mean net 3d return |
|---|---|---|---|---|---|
| IS | (-0.001, 0.4] | 956 | 0.32 | 0.42 | -1.58% |
| IS | (0.4, 0.45] | 1703 | 0.44 | 0.49 | +0.33% |
| IS | (0.45, 0.5] | 5977 | 0.47 | 0.47 | -0.04% |
| IS | (0.5, 0.55] | 2261 | 0.53 | 0.50 | +1.00% |
| IS | (0.55, 0.6] | 1240 | 0.57 | 0.52 | +1.76% |
| IS | (0.6, 1.0] | 347 | 0.69 | 0.46 | +1.30% |
| IS | all | 12484 | 0.48 | 0.48 | +0.30% (AUC 0.520) |
| OOS | (-0.001, 0.4] | 260 | 0.32 | 0.51 | +0.20% |
| OOS | (0.4, 0.45] | 1961 | 0.43 | 0.43 | -0.79% |
| OOS | (0.45, 0.5] | 1480 | 0.48 | 0.48 | -0.15% |
| OOS | (0.5, 0.55] | 390 | 0.52 | 0.45 | -0.94% |
| OOS | (0.55, 0.6] | 224 | 0.56 | 0.50 | -0.63% |
| OOS | (0.6, 1.0] | 48 | 0.71 | 0.40 | -1.91% |
| OOS | all | 4363 | 0.46 | 0.45 | -0.53% (AUC 0.522) |
