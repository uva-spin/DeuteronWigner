"""Exact finite longitudinal intermediate axes for same-species contractions.

The C114 Q0 projector excludes zero transferred plus momentum.  A same-species
one-body contraction therefore uses an intermediate mode ``r`` of the same
APBC/PBC species with ``q=r-k != 0``.  This axis is not the external BRA/KET
partition difference used by the mixed products in C406.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.basis1 import core as c47
from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    RESOLUTION_LABELS,
    content_root,
    normalize_resolution,
)
from deuteron_wigner.bridge.modes import core as c45

from .authority import STATUS

SPECIES = ("QUARK", "GLUON")
SECTORS = ("q->q", "qg->qg")
PRODUCT_BY_SPECIES = {"QUARK": "J_qJ_q", "GLUON": "J_gJ_g"}


@dataclass(frozen=True)
class IntermediateMode:
    resolution: str
    species: str
    sector: str
    external_id: str
    external_k: Fraction
    intermediate_rank: int
    intermediate_k: Fraction
    transfer_q: Fraction
    boundary: str

    def to_record(self) -> dict[str, Any]:
        record = asdict(self)
        for key in ("external_k", "intermediate_k", "transfer_q"):
            value = record[key]
            record[key] = {
                "numerator": value.numerator,
                "denominator": value.denominator,
                "exact": str(value),
                "float": float(value),
            }
        record.update(
            {
                "product": PRODUCT_BY_SPECIES[self.species],
                "Q0_admitted": self.transfer_q != 0,
                "zero_mode": False,
                "transfer_is_integer": self.transfer_q.denominator == 1,
                "source_ancestry": ("C45", "C47", "C114", "C115", "C119", "C406", "C407"),
            }
        )
        return record


def _source_resolution(resolution: str) -> c45.Resolution:
    _short, full = normalize_resolution(resolution)
    for source in c45.RESOLUTIONS:
        if source.label == full:
            return source
    raise KeyError(resolution)


def _species(species: str) -> str:
    value = str(species).upper()
    if value not in SPECIES:
        raise ValueError(f"species must be one of {SPECIES}")
    return value


def _fraction(record: Mapping[str, Any]) -> Fraction:
    numerator, denominator = record["k"]
    return Fraction(int(numerator), int(denominator))


@lru_cache(maxsize=None)
def species_mode_axis(resolution: str, species: str) -> tuple[Fraction, ...]:
    source = _source_resolution(resolution)
    species = _species(species)
    rows = c45.longitudinal_modes(source, species)
    modes = tuple(_fraction(row) for row in rows)
    if len(modes) != len(set(modes)):
        raise ValueError("C45 longitudinal mode axis contains duplicates")
    if any(mode <= 0 or mode > source.K for mode in modes):
        raise ValueError("C45 longitudinal mode outside positive finite resolution support")
    denominator = 2 if species == "QUARK" else 1
    if any(mode.denominator != denominator for mode in modes):
        raise ValueError("C45 boundary parity mismatch")
    return modes


@lru_cache(maxsize=None)
def external_mode_axis(resolution: str, species: str, sector: str) -> tuple[tuple[str, Fraction], ...]:
    source = _source_resolution(resolution)
    species = _species(species)
    if sector not in SECTORS:
        raise ValueError(f"sector must be one of {SECTORS}")
    if sector == "q->q":
        if species == "GLUON":
            return tuple()
        return ((f"{normalize_resolution(resolution)[0]}:q", source.K),)
    partitions = tuple(c47.partitions(source))
    rows = []
    for partition_id, (k_q, k_g, _x_q, _x_g) in enumerate(partitions):
        value = k_q if species == "QUARK" else k_g
        rows.append((f"{normalize_resolution(resolution)[0]}:qg:P{partition_id}", value))
    return tuple(rows)


@lru_cache(maxsize=None)
def intermediate_axis(
    resolution: str,
    species: str,
    sector: str,
    external_k: Fraction | int,
    external_id: str = "external",
) -> tuple[IntermediateMode, ...]:
    species = _species(species)
    external = external_k if isinstance(external_k, Fraction) else Fraction(int(external_k), 1)
    modes = species_mode_axis(resolution, species)
    if external not in modes:
        raise ValueError(f"external mode {external} is outside the C45 {species} axis")
    boundary = "ANTIPERIODIC" if species == "QUARK" else "PERIODIC_NONZERO"
    rows = []
    for rank, intermediate in enumerate(modes):
        transfer = intermediate - external
        if transfer == 0:
            continue
        if transfer.denominator != 1:
            raise ValueError("same-boundary mode difference must be an integer Q0 transfer")
        rows.append(
            IntermediateMode(
                resolution=normalize_resolution(resolution)[0],
                species=species,
                sector=sector,
                external_id=str(external_id),
                external_k=external,
                intermediate_rank=rank,
                intermediate_k=intermediate,
                transfer_q=transfer,
                boundary=boundary,
            )
        )
    if len(rows) != len(modes) - 1:
        raise RuntimeError("Q0 intermediate-axis cardinality failure")
    return tuple(rows)


@lru_cache(maxsize=1)
def intermediate_axis_inventory() -> Mapping[str, Any]:
    rows = []
    external_rows = []
    for resolution in RESOLUTION_LABELS:
        for species in SPECIES:
            for sector in SECTORS:
                external_axis = external_mode_axis(resolution, species, sector)
                if not external_axis:
                    external_rows.append(
                        {
                            "resolution": resolution,
                            "species": species,
                            "sector": sector,
                            "external_count": 0,
                            "status": (
                                "NUMBER_PRESERVING_ONE_BODY_BRANCH_NOT_APPLICABLE_EXTERNAL_GLUON_ABSENT_"
                                "OTHER_JGJG_BRANCHES_UNRESOLVED_NOT_ZERO"
                            ),
                        }
                    )
                    continue
                local_count = 0
                for external_id, external_k in external_axis:
                    axis = intermediate_axis(resolution, species, sector, external_k, external_id)
                    local_count += len(axis)
                    rows.extend(item.to_record() for item in axis)
                external_rows.append(
                    {
                        "resolution": resolution,
                        "species": species,
                        "sector": sector,
                        "external_count": len(external_axis),
                        "intermediate_rows": local_count,
                        "status": "FINITE_Q0_INTERMEDIATE_AXIS_CLOSED",
                    }
                )
    payload = {
        "schema": "C407-C117-I2-SAME-SPECIES-INTERMEDIATE-AXIS-INVENTORY-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "expected_row_count": 154,
        "external_axes": tuple(external_rows),
        "zero_transfer_rows": sum(not row["Q0_admitted"] for row in rows),
        "noninteger_transfer_rows": sum(not row["transfer_is_integer"] for row in rows),
        "duplicates": len(rows) - len(
            {
                (
                    row["resolution"],
                    row["species"],
                    row["sector"],
                    row["external_id"],
                    row["intermediate_k"]["exact"],
                )
                for row in rows
            }
        ),
        "complete_C117_action": False,
    }
    if payload["row_count"] != payload["expected_row_count"]:
        raise RuntimeError("C407 intermediate-axis expected count changed")
    if payload["zero_transfer_rows"] or payload["noninteger_transfer_rows"] or payload["duplicates"]:
        raise RuntimeError("C407 intermediate-axis validation failed")
    return {**payload, "root": content_root(payload)}


__all__ = [
    "SPECIES",
    "SECTORS",
    "PRODUCT_BY_SPECIES",
    "IntermediateMode",
    "species_mode_axis",
    "external_mode_axis",
    "intermediate_axis",
    "intermediate_axis_inventory",
]
