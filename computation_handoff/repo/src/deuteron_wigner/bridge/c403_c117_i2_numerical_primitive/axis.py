"""C403 source-qualified finite internal-member axis for C117 ``I2``.

C124 materialized this axis through authenticated C64 exact-support artifacts.
C403 proves a narrower closed form for the C117 ``I2_density_projector``
domain that does not require the expensive complete C64 runtime bundle.

For any positive longitudinal partition and any one-particle transverse HO
mode ``(n,m)`` with shell ``2*n+abs(m) <= Nmax-2``, choose the companion
particle in its transverse ground state and the relative output equal to the
selected mode with CM output ``(0,0)``.  Separate circular-occupation
conservation then gives one nonzero Talmi--Moshinsky coefficient.  Modes in
the highest C45 one-particle shell ``2*n+abs(m)=Nmax-1`` cannot be admitted,
because even a ground-state companion would exceed the qg product-shell cap
``Nmax-2``.

This closes member identities and exact support only.  It does not supply the
C114 inverse/source factor, C119 current factor, color/spin contractions,
normalization, target-state aggregation, or a complete C396 coordinate action.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from typing import Any, Mapping

import sympy as sp

from deuteron_wigner.bridge.basis1 import core as c47
from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    RESOLUTION_LABELS,
    content_root,
    normalize_resolution,
    resolution_record,
)
from deuteron_wigner.bridge.modes import core as c45
from deuteron_wigner.bridge.qgtm import core as c62

GRAPH_ID = "I2_density_projector"
STATUS = "C403_C117_I2_FINITE_AXIS_AND_SPATIAL_KERNEL_NUMERICAL_PRIMITIVE_READY_FULL_C117_OPERATOR_UNAVAILABLE"
SPECIES = ("QUARK", "GLUON")
HELICITIES = (-1, 1)
COLOR_COUNT = {"QUARK": 3, "GLUON": 8}
SOURCE_SHELL_OFFSET = 2


@dataclass(frozen=True)
class InternalMember:
    """One finite C117 I2 internal member in C124-compatible order."""

    resolution: str
    species: str
    partition_id: int
    k: Fraction
    x: Fraction
    n: int
    m: int
    helicity: int
    color: int
    rank: int
    selection_status: str

    @property
    def shell(self) -> int:
        return 2 * self.n + abs(self.m)

    @property
    def member_id(self) -> str:
        return (
            f"C403:{GRAPH_ID}:{self.resolution}:{self.species}:"
            f"P={self.partition_id}:K={self.k}:N={self.n}:M={self.m}:"
            f"H={self.helicity}:C={self.color}:S={self.selection_status}"
        )

    def to_record(self) -> dict[str, Any]:
        record = asdict(self)
        for key in ("k", "x"):
            value = record[key]
            record[key] = {
                "numerator": value.numerator,
                "denominator": value.denominator,
                "exact": str(value),
                "float": float(value),
            }
        record.update(
            {
                "member_id": self.member_id,
                "graph_id": GRAPH_ID,
                "shell": self.shell,
                "derivative_weight": "1",
                "zero_mode": False,
                "orientation": "bra_conjugate_source_ordered",
                "source_ancestry": ("C45", "C47", "C62", "C114", "C115", "C116", "C117", "C124"),
                "numerical_factor_values_bound": False,
            }
        )
        return record


def _source_resolution(resolution: str) -> c45.Resolution:
    _label, full = normalize_resolution(resolution)
    for source in c45.RESOLUTIONS:
        if source.label == full:
            return source
    raise KeyError(resolution)


def _species(species: str) -> str:
    value = str(species).upper()
    if value not in SPECIES:
        raise ValueError(f"species must be one of {SPECIES}")
    return value


def transverse_shell(mode: tuple[int, int]) -> int:
    n, m = mode
    if n < 0:
        raise ValueError("radial quantum number must be nonnegative")
    return 2 * n + abs(m)


@lru_cache(maxsize=None)
def candidate_transverse_modes(resolution: str) -> tuple[tuple[int, int], ...]:
    """C45 one-particle candidate modes: shell <= Nmax-1."""
    source = _source_resolution(resolution)
    return tuple(c45.ho_labels(source.Nmax))


@lru_cache(maxsize=None)
def admitted_transverse_modes(resolution: str) -> tuple[tuple[int, int], ...]:
    """Exact C403 support theorem: shell <= Nmax-2."""
    source = _source_resolution(resolution)
    cap = source.Nmax - SOURCE_SHELL_OFFSET
    return tuple(mode for mode in candidate_transverse_modes(resolution) if transverse_shell(mode) <= cap)


@lru_cache(maxsize=None)
def rejected_transverse_modes(resolution: str) -> tuple[tuple[int, int], ...]:
    admitted = set(admitted_transverse_modes(resolution))
    return tuple(mode for mode in candidate_transverse_modes(resolution) if mode not in admitted)


def support_status(resolution: str, n: int, m: int) -> str:
    mode = (int(n), int(m))
    if mode not in candidate_transverse_modes(resolution):
        raise KeyError(f"mode {mode} is outside the C45 candidate shell")
    return "ADMITTED_MEMBER" if mode in admitted_transverse_modes(resolution) else "REJECTED_NOT_APPLICABLE"


def _partitions(resolution: str) -> tuple[tuple[Fraction, Fraction, Fraction, Fraction], ...]:
    source = _source_resolution(resolution)
    return tuple(c47.partitions(source))


def member_count(resolution: str, species: str, *, admitted_only: bool = False) -> int:
    species = _species(species)
    mode_count = len(admitted_transverse_modes(resolution) if admitted_only else candidate_transverse_modes(resolution))
    return len(_partitions(resolution)) * mode_count * len(HELICITIES) * COLOR_COUNT[species]


def member_by_rank(resolution: str, species: str, rank: int) -> InternalMember:
    """Decode C124-compatible order: partition, HO mode, helicity, color."""
    species = _species(species)
    total = member_count(resolution, species)
    rank = int(rank)
    if rank < 0 or rank >= total:
        raise IndexError(rank)
    modes = candidate_transverse_modes(resolution)
    colors = COLOR_COUNT[species]
    color = rank % colors
    quotient = rank // colors
    helicity = HELICITIES[quotient % len(HELICITIES)]
    quotient //= len(HELICITIES)
    mode = modes[quotient % len(modes)]
    partition_id = quotient // len(modes)
    kq, kg, xq, xg = _partitions(resolution)[partition_id]
    k, x = (kq, xq) if species == "QUARK" else (kg, xg)
    return InternalMember(
        resolution=normalize_resolution(resolution)[0],
        species=species,
        partition_id=partition_id,
        k=k,
        x=x,
        n=mode[0],
        m=mode[1],
        helicity=helicity,
        color=color,
        rank=rank,
        selection_status=support_status(resolution, *mode),
    )


def member_rank(member: InternalMember) -> int:
    candidate = member_by_rank(member.resolution, member.species, member.rank)
    if candidate != member:
        raise ValueError("member record does not match its canonical rank")
    return member.rank


def member_page(
    resolution: str,
    species: str,
    *,
    start: int = 0,
    limit: int = 128,
) -> dict[str, Any]:
    if start < 0 or limit <= 0:
        raise ValueError("start must be nonnegative and limit must be positive")
    total = member_count(resolution, species)
    stop = min(total, start + limit)
    rows = tuple(member_by_rank(resolution, species, rank).to_record() for rank in range(start, stop))
    payload = {
        "schema": "C403-C117-I2-MEMBER-PAGE-V1",
        "status": STATUS,
        "resolution": normalize_resolution(resolution)[0],
        "species": _species(species),
        "first_rank": start,
        "records": rows,
        "next_rank": None if stop >= total else stop,
        "terminal": stop >= total,
        "candidate_count": total,
    }
    return {**payload, "root": content_root(payload)}


def _expected_witness_expression(species: str, xq: Fraction, shell: int) -> sp.Expr:
    species = _species(species)
    base = sp.Rational((1 - xq).numerator, (1 - xq).denominator) if species == "QUARK" else sp.Rational(xq.numerator, xq.denominator)
    sign = 1 if species == "QUARK" else (-1) ** shell
    return sp.simplify(sign * base ** sp.Rational(shell, 2))


def _parse_c62_expression(expression: str) -> sp.Expr:
    return sp.sympify(
        expression,
        locals={
            "Integer": sp.Integer,
            "Rational": sp.Rational,
            "Pow": sp.Pow,
            "Mul": sp.Mul,
            "Add": sp.Add,
            "sqrt": sp.sqrt,
        },
    )


def witness_record(
    resolution: str,
    species: str,
    partition_id: int,
    n: int,
    m: int,
) -> dict[str, Any]:
    """Construct the exact CM-ground witness used in the support theorem."""
    species = _species(species)
    source = _source_resolution(resolution)
    partitions = _partitions(resolution)
    if partition_id < 0 or partition_id >= len(partitions):
        raise IndexError(partition_id)
    mode = (int(n), int(m))
    status = support_status(resolution, *mode)
    shell = transverse_shell(mode)
    cap = source.Nmax - SOURCE_SHELL_OFFSET
    kq, kg, xq, xg = partitions[partition_id]
    if status != "ADMITTED_MEMBER":
        payload = {
            "schema": "C403-C117-I2-SUPPORT-WITNESS-V1",
            "resolution": normalize_resolution(resolution)[0],
            "species": species,
            "partition_id": partition_id,
            "mode": {"n": n, "m": m, "shell": shell},
            "selection_status": status,
            "product_shell_cap": cap,
            "proof": "selected one-particle shell already exceeds product-shell cap even with a ground-state companion",
            "C62_evaluation_required": False,
            "exact_match": True,
        }
        return {**payload, "root": content_root(payload)}

    incoming = (n, m, 0, 0) if species == "QUARK" else (0, 0, n, m)
    outgoing = (0, 0, n, m)
    coefficient = c62.polar_tm_coefficient(outgoing, incoming, xq)
    actual = _parse_c62_expression(coefficient.expression)
    expected = _expected_witness_expression(species, xq, shell)
    exact_match = sp.simplify(actual - expected) == 0
    payload = {
        "schema": "C403-C117-I2-SUPPORT-WITNESS-V1",
        "resolution": normalize_resolution(resolution)[0],
        "species": species,
        "partition_id": partition_id,
        "longitudinal": {
            "kq": str(kq),
            "kg": str(kg),
            "xq": str(xq),
            "xg": str(xg),
        },
        "mode": {"n": n, "m": m, "shell": shell},
        "selection_status": status,
        "product_shell_cap": cap,
        "CM_output": {"n": 0, "m": 0},
        "relative_output": {"n": n, "m": m},
        "companion_mode": {"n": 0, "m": 0},
        "C62_status": coefficient.status,
        "C62_expression": coefficient.expression,
        "C62_value": [coefficient.value_re, coefficient.value_im],
        "expected_expression": sp.srepr(expected),
        "expected_value": [float(sp.N(expected, 50)), 0.0],
        "exact_match": exact_match,
        "absolute_numeric_residual": abs(complex(sp.N(actual - expected, 50))),
        "proof": (
            "separate circular occupations are conserved; with the companion and CM in their ground states, "
            "the unique bracket is xg^(shell/2) for a quark member or (-1)^shell*xq^(shell/2) for a gluon member"
        ),
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def support_theorem_rows() -> tuple[dict[str, Any], ...]:
    rows: list[dict[str, Any]] = []
    for resolution in RESOLUTION_LABELS:
        for partition_id, _partition in enumerate(_partitions(resolution)):
            for species in SPECIES:
                for n, m in candidate_transverse_modes(resolution):
                    rows.append(witness_record(resolution, species, partition_id, n, m))
    return tuple(rows)


def axis_summary() -> dict[str, Any]:
    rows = []
    for resolution in RESOLUTION_LABELS:
        record = resolution_record(resolution)
        transverse_candidate = len(candidate_transverse_modes(resolution))
        transverse_admitted = len(admitted_transverse_modes(resolution))
        transverse_rejected = len(rejected_transverse_modes(resolution))
        for species in SPECIES:
            rows.append(
                {
                    "resolution": resolution,
                    "species": species,
                    "K_fraction": record["K_fraction"],
                    "K2": record["K2"],
                    "Nmax": record["Nmax"],
                    "b_HO_GeV": record["b_HO"],
                    "partition_count": len(_partitions(resolution)),
                    "transverse_candidate_count": transverse_candidate,
                    "transverse_admitted_count": transverse_admitted,
                    "transverse_rejected_count": transverse_rejected,
                    "candidate_member_count": member_count(resolution, species),
                    "admitted_member_count": member_count(resolution, species, admitted_only=True),
                    "rejected_member_count": member_count(resolution, species) - member_count(resolution, species, admitted_only=True),
                    "helicity_count": len(HELICITIES),
                    "color_count": COLOR_COUNT[species],
                }
            )
    payload = {
        "schema": "C403-C117-I2-FINITE-MEMBER-AXIS-SUMMARY-V1",
        "status": STATUS,
        "graph_id": GRAPH_ID,
        "support_theorem": "ADMITTED iff 2*n+abs(m) <= Nmax-2; C45 highest shell Nmax-1 is rejected",
        "rows": tuple(rows),
        "finite_axis_paths": len(rows),
        "C64_runtime_required": False,
        "C62_exact_algebra_verification": True,
        "current_factor_values_bound": False,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


def support_theorem_certificate() -> dict[str, Any]:
    rows = support_theorem_rows()
    admitted = [row for row in rows if row["selection_status"] == "ADMITTED_MEMBER"]
    rejected = [row for row in rows if row["selection_status"] == "REJECTED_NOT_APPLICABLE"]
    payload = {
        "schema": "C403-C117-I2-SUPPORT-THEOREM-CERTIFICATE-V1",
        "status": STATUS,
        "row_count": len(rows),
        "admitted_witness_rows": len(admitted),
        "rejected_shell_rows": len(rejected),
        "all_exact_matches": all(bool(row["exact_match"]) for row in rows),
        "maximum_numeric_residual": max(float(row.get("absolute_numeric_residual", 0.0)) for row in rows),
        "row_root": content_root(rows),
        "theorem": (
            "For positive C47 longitudinal fractions, the C117 I2 one-particle mode is in the CM-ground preimage "
            "iff its transverse shell does not exceed Nmax-2."
        ),
        "proof_scope": "finite support identity only; no C114/C119/current/color/spin/normalization values",
        "C64_artifact_dependency_removed_at_this_scope": True,
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "GRAPH_ID",
    "STATUS",
    "SPECIES",
    "HELICITIES",
    "COLOR_COUNT",
    "InternalMember",
    "transverse_shell",
    "candidate_transverse_modes",
    "admitted_transverse_modes",
    "rejected_transverse_modes",
    "support_status",
    "member_count",
    "member_by_rank",
    "member_rank",
    "member_page",
    "witness_record",
    "support_theorem_rows",
    "axis_summary",
    "support_theorem_certificate",
]
