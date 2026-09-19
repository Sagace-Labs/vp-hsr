"""The endpoints this pathway predicts.

Frozen so the data sources are auditable.

Both assays were verified live against PubChem on 2026-09-06, and screen the
same library:

    AID 743210   qHTS assay for small molecule activators of the heat shock
                 response signaling pathway                9305 substances
    AID 743209   the same, cell viability counter screen   9305 substances
"""

from __future__ import annotations

from dataclasses import dataclass

__all__ = ["CYTOTOX", "TARGET", "TARGETS", "Endpoint", "all_names", "get"]


@dataclass(frozen=True)
class Endpoint:
    """One molecular initiating event, identified by the assay that reads it out."""

    name: str
    pathway: str
    mie: str
    pubchem_aid: int
    assay_name: str


TARGET = Endpoint(
    name="HSE",
    pathway="heat shock response / cytosolic proteostasis",
    mie=(
        "accumulation of misfolded cytosolic protein, which frees HSF1 to bind the "
        "heat shock element and switch on the chaperone programme"
    ),
    pubchem_aid=743210,
    assay_name=(
        "qHTS assay for small molecule activators of the heat shock response "
        "signaling pathway"
    ),
)

CYTOTOX = Endpoint(
    name="VIABILITY",
    pathway="heat shock response / cytosolic proteostasis",
    mie="loss of cell viability, which registers on the reporter readout as a consequence",
    pubchem_aid=743209,
    assay_name=(
        "qHTS assay for small molecule activators of the heat shock response "
        "signaling pathway - cell viability counter screen"
    ),
)

TARGETS: dict[str, Endpoint] = {"HSE": TARGET, "VIABILITY": CYTOTOX}


def get(name: str) -> Endpoint:
    try:
        return TARGETS[name.upper()]
    except KeyError:
        raise KeyError(f"unknown target {name!r}; known: {sorted(TARGETS)}") from None


def all_names() -> list[str]:
    return sorted(TARGETS)
