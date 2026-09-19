# hsr v1

_Generated from `manifest.toml` and `metrics.json`. Do not edit._

Released 2026-09-19 · signature 1

**Why this version.** first release: binary XGBoost on Morgan, MACCS and RDKit descriptors over the Tox21 heat-shock-response screen

## Outputs

| column | dtype | range | meaning |
|---|---|---|---|
| `hsr_activation` | float32 | 0.0–1.0 | P(switches on the heat-shock-element reporter in the Tox21 qHTS screen). The assay reads the response, not the protein that misfolded |
| `hsr_cytotox` | float32 | 0.0–1.0 | P(reduces viability in the counter-screen over the same library). A compound scoring high on both readouts lit the reporter in a cell that was also dying |

Missing values: NaN when RDKit cannot parse the input SMILES

## Performance

Protocol `scaffold-balanced-5seed@1` — Bemis-Murcko scaffold split with scaffold groups permuted by seed and each group placed in the fold it overfills least, so a group larger than a fold's capacity settles in train instead of starving that fold. Same fold fractions, seeds and metrics as scaffold-shuffle-5seed@1; only the packing differs. Five seeds; report mean and standard deviation over the held-out test folds.

Evaluated 2026-09-19 on n_train=4569, n_val=501, n_test=753.

### `hsr_activation`

| metric | mean | std | per seed |
|---|---|---|---|
| auc_roc | 0.683 | 0.067 | 0.563, 0.711, 0.662, 0.761, 0.717 |
| auprc | 0.059 | 0.038 | 0.056, 0.132, 0.027, 0.047, 0.032 |
| mcc | 0.119 | 0.048 | 0.133, 0.189, 0.043, 0.131, 0.097 |
| brier | 0.120 | 0.074 | 0.033, 0.098, 0.230, 0.180, 0.059 |

### `hsr_cytotox`

Measured on n_train=4397, n_val=467, n_test=714.

| metric | mean | std | per seed |
|---|---|---|---|
| auc_roc | 0.731 | 0.080 | 0.760, 0.782, 0.673, 0.607, 0.831 |
| auprc | 0.102 | 0.085 | 0.093, 0.049, 0.079, 0.024, 0.266 |
| mcc | 0.109 | 0.180 | -0.005, -0.003, 0.099, -0.007, 0.459 |
| brier | 0.060 | 0.075 | 0.009, 0.026, 0.209, 0.015, 0.041 |

> Comparable only with metrics carrying the same protocol id.

## Data

Tox21 heat shock response qHTS — PubChem BioAssay AID 743210 (qHTS assay for small molecule activators of the heat shock response signaling pathway) and AID 743209 (qHTS assay for small molecule activators of the heat shock response signaling pathway - cell viability counter screen), rows called Active or Inactive, one row per compound labelled by majority call across its assay records. Retrieved 2026-09-06, licensed public-domain, redistributed here.

`5823` compounds, positive rate `0.007`, table SHA-256 `3c5a234a87b1a9ad…`

Regenerate and check for upstream drift with `python -m vp_hsr.data fetch --verify`.

## Model

xgboost-binary on `combo3` features. Shipped weights: one model per output, each on every compound its endpoint labels minus a 10% scaffold carve used for early stopping

`weights.joblib` SHA-256 `f31a6542db721e7d…`

## Provenance

Environment: python 3.11.11, rdkit 2026.03.5, xgboost 3.2.0.

Reproducibility is to this dataset hash and this environment, not bit-exact: the sources are live endpoints and RDKit descriptor values move between releases.
