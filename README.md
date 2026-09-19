# vp-hsr

Predicts activation of the cytosolic heat shock response from a SMILES string —
a molecular initiating event for drug-induced liver injury, where misfolded
protein accumulating in the hepatocyte frees HSF1 onto the heat shock element
and switches on the chaperone programme.

## Install

    pip install vp-hsr

## Use

    from vp_hsr import predict
    predict(["CC(=O)Oc1ccccc1C(=O)O"])   # -> DataFrame[hsr_activation, hsr_cytotox]

Returns one row per input and one column per declared output. `hsr_activation`
is the probability of switching on the heat-shock-element reporter;
`hsr_cytotox` is the probability of reducing viability in the counter-screen
over the same library. A compound scoring high on both lit the reporter in a
cell that was also dying. Unparseable SMILES come back as NaN. Pin a version
with `predict(smiles, version="v1")`; list what is available with `versions()`.

## Current version

**v1**, signature 1, measured under protocol `scaffold-balanced-5seed@1`.
The full record — metrics per output and per seed, dataset hash,
environment — is in
[`src/vp_hsr/versions/v1/CARD.md`](src/vp_hsr/versions/v1/CARD.md).

## Data

PubChem BioAssay AID 743210, the Tox21 qHTS screen for activators of the heat
shock response signaling pathway, and AID 743209, its cell-viability
counter-screen over the same library. Both are reduced to one row per compound
labelled by the majority call across its assay records, retrieved 2026-09-06 and
redistributed here as a United States government work in the public domain.
Rebuild and check for upstream drift with
`python -m vp_hsr.data fetch --verify`; see [`data/README.md`](data/README.md)
for the expected layout.

## Retrain

    python -m vp_hsr.train --version v2 --reason "why this version exists"
    python -m vp_hsr.evaluate --version v2

`train` fits one deployment model per output on the whole dataset and writes a
new version directory; `evaluate` refits per seed under the protocol and
records what those held-out models scored. Reproducibility is to the recorded
dataset hash and environment, which can change.

## Licence

Code is Apache-2.0 ([`LICENSE`](LICENSE)). The bundled dataset is in the public
domain ([`LICENSE-DATA`](LICENSE-DATA)).

## Cite

See [`CITATION.cff`](CITATION.cff).
