"""Lossless C78/C82 pair-program algebra, without expanded-record output.

The program tracks C82's source-ordered leaf axes exactly.  It deliberately
does not claim the C89 attestation gate: two full dual-digest traversals have
not executed yet.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Iterator
from functools import lru_cache
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[4]
STATUS = "C89_IFBOUNDSTREAM_EXECUTION_INCOMPLETE"
NEXT = "C90/IFBOUNDRESTART — execute the complete pair-atomic dual-digest traversals under an explicitly measured runtime budget"
SCHEMA = "C89-FACTORIZED-SCIENTIFIC-PAIR-PROGRAM-V1"
ENVIRONMENT = "HISTORICAL_C82_SOURCE_WITH_C87_CANONICAL_COLOR_AUTHORITY"
RESOLUTION_ORDER = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def digest(value: Any) -> str:
    return sha256(_json(value).encode()).hexdigest()


@lru_cache(maxsize=None)
def _payload(resolution: str) -> dict[str, Any]:
    if resolution not in RESOLUTION_ORDER:
        raise KeyError(resolution)
    path = ROOT / "data/runtime/c78_ifsupport2" / f"{resolution}.json"
    if not path.is_file() or path.is_symlink():
        raise ValueError("unsafe C78 payload")
    return json.loads(path.read_text())


def _pair_rows(resolution: str) -> Iterator[dict[str, Any]]:
    payload = _payload(resolution)
    emission = {row["id"]: row for row in payload["emission_edges"]}
    absorption = {row["id"]: row for row in payload["absorption_edges"]}
    ep = payload["emission_path_domains"]
    ap = payload["absorption_path_domains"]
    for group in payload["witness_groups"]:
        for emission_id in group["emission_endpoint_ids"]:
            for absorption_id in group["absorption_endpoint_ids"]:
                out, inn = emission[emission_id], absorption[absorption_id]
                out_domain, in_domain = ep[emission_id], ap[absorption_id]
                count = int(out_domain["path_count"]) * int(in_domain["path_count"])
                yield {"resolution": resolution, "physical_bra_id": out["physical_qg_id"],
                       "physical_ket_id": inn["physical_qg_id"], "witness_id": f"C78:W:{digest([emission_id, group['intermediate_q_id'], absorption_id])}",
                       "intermediate_q_id": group["intermediate_q_id"], "emission_endpoint_id": emission_id,
                       "absorption_endpoint_id": absorption_id, "output_component_ids": tuple(out_domain["component_ids"]),
                       "output_color_record_ids": tuple(out_domain["color_record_ids"]),
                       "input_component_ids": tuple(in_domain["component_ids"]),
                       "input_color_record_ids": tuple(in_domain["color_record_ids"]), "logical_count": count}


@dataclass(frozen=True)
class FactorizedScientificPairProgram:
    resolution: str
    pair_sequence: int
    physical_bra_id: str
    physical_ket_id: str
    witness_id: str
    intermediate_q_id: str
    emission_endpoint_id: str
    absorption_endpoint_id: str
    output_component_ids: tuple[str, ...]
    output_color_record_ids: tuple[str, ...]
    input_component_ids: tuple[str, ...]
    input_color_record_ids: tuple[str, ...]

    @property
    def pair_id(self) -> str:
        return f"{self.physical_bra_id}|{self.physical_ket_id}"

    @property
    def logical_count(self) -> int:
        return (len(self.output_component_ids) * len(self.output_color_record_ids) *
                len(self.input_component_ids) * len(self.input_color_record_ids))

    @property
    def program_id(self) -> str:
        return "C89:PROGRAM:" + digest(self.to_dict())

    def to_dict(self) -> dict[str, Any]:
        return {"schema": SCHEMA, "environment": ENVIRONMENT, "resolution": self.resolution,
                "pair_sequence": self.pair_sequence, "pair_id": self.pair_id,
                "witness_id": self.witness_id, "intermediate_q_id": self.intermediate_q_id,
                "emission_endpoint_id": self.emission_endpoint_id, "absorption_endpoint_id": self.absorption_endpoint_id,
                "axes": {"output_component": self.output_component_ids, "output_color": self.output_color_record_ids,
                         "input_component": self.input_component_ids, "input_color": self.input_color_record_ids},
                "axis_order": ["output_component", "output_color", "input_component", "input_color"],
                "multiplicity": "one C78 ordered witness; Cartesian product retains each leaf exactly once",
                "logical_count": self.logical_count}


def iterate_pair_programs(resolution: str) -> Iterator[FactorizedScientificPairProgram]:
    seen: set[str] = set()
    for sequence, row in enumerate(_pair_rows(resolution)):
        expected_count = row.pop("logical_count")
        program = FactorizedScientificPairProgram(pair_sequence=sequence, **row)
        if program.pair_id in seen:
            raise ValueError("C78 pair order is not a disjoint supported-pair domain")
        seen.add(program.pair_id)
        if program.logical_count != expected_count or not program.logical_count:
            raise ValueError("invalid factorized C82 leaf cardinality")
        yield program


def pair_program(pair_id: str, resolution: str) -> FactorizedScientificPairProgram:
    for program in iterate_pair_programs(resolution):
        if program.pair_id == pair_id:
            return program
    raise KeyError(pair_id)


def _axes(program: FactorizedScientificPairProgram) -> tuple[tuple[str, ...], ...]:
    return (program.output_component_ids, program.output_color_record_ids,
            program.input_component_ids, program.input_color_record_ids)


def unrank_pair_leaf(program: FactorizedScientificPairProgram, ordinal: int) -> dict[str, Any]:
    if ordinal < 0 or ordinal >= program.logical_count:
        raise IndexError("pair-local ordinal outside C82 logical domain")
    sizes = tuple(len(axis) for axis in _axes(program)); values = [0, 0, 0, 0]; residual = ordinal
    for index in range(3, -1, -1):
        values[index] = residual % sizes[index]; residual //= sizes[index]
    selected = tuple(axis[index] for axis, index in zip(_axes(program), values))
    leaf = {"program_id": program.program_id, "pair_id": program.pair_id, "resolution": program.resolution,
            "local_ordinal": ordinal, "witness_id": program.witness_id,
            "output_component_id": selected[0], "output_color_record_id": selected[1],
            "input_component_id": selected[2], "input_color_record_id": selected[3],
            "source_order": ("b_dagger", "a_dagger", "a", "b")}
    return {**leaf, "leaf_id": "C89:LEAF:" + digest(leaf)}


def rank_pair_leaf(program: FactorizedScientificPairProgram, leaf: dict[str, Any]) -> int:
    if leaf.get("program_id") != program.program_id or leaf.get("pair_id") != program.pair_id:
        raise ValueError("leaf/program identity mismatch")
    values = (leaf["output_component_id"], leaf["output_color_record_id"], leaf["input_component_id"], leaf["input_color_record_id"])
    ordinal = 0
    for axis, value in zip(_axes(program), values):
        try: index = axis.index(value)
        except ValueError as exc: raise ValueError("leaf axis identity absent from program") from exc
        ordinal = ordinal * len(axis) + index
    return ordinal


def _physical_index(identifier: str) -> int:
    return int(identifier.split(":KIN=")[1].split(":")[0])


def _product_color(record_id: str) -> tuple[int, int]:
    row = record_id.split("|")[0].removeprefix("product:")
    parts = dict(token.split("=") for token in row.split(":"))
    return int(parts["cprime"]), int(parts["a"])


@lru_cache(maxsize=None)
def _raw_basis(resolution: str) -> dict[str, dict[str, Any]]:
    from ..qgembed9.core import QGEmbeddingPackage
    crosswalk = QGEmbeddingPackage().load_canonical_tm_crosswalk()
    return {row["id"]: dict(row) for row in crosswalk["raw_basis"] if row["resolution"] == resolution}


@lru_cache(maxsize=None)
def _color_records() -> dict[str, dict[str, Any]]:
    from ..qgcolor6.core import TripletAuthorityPackage
    return {f"{row['row_id']}|{row['column_id']}": dict(row) for row in TripletAuthorityPackage().exact_records()}


@lru_cache(maxsize=None)
def _u3() -> Any:
    from ..qgcolor6.core import TripletAuthorityPackage
    return TripletAuthorityPackage().load("U3")


@lru_cache(maxsize=8)
def _components(resolution: str, physical_id: str) -> tuple[dict[str, Any], ...]:
    from ..qgembed9.core import QGEmbeddingPackage
    return tuple(dict(row) for row in QGEmbeddingPackage().physical_qg_raw_components(resolution, _physical_index(physical_id)))


def _component(resolution: str, physical_id: str, raw_id: str) -> dict[str, Any]:
    return next(row for row in _components(resolution, physical_id) if row["raw"]["id"] == raw_id)


def _mode(raw: dict[str, Any], *, gluon: bool, helicity: int) -> tuple[int, int, int, int, int]:
    value = Fraction(raw["kg"] if gluon else raw["kq"])
    return (value.numerator, value.denominator, int(raw["n_g"] if gluon else raw["n_q"]),
            int(raw["m_g"] if gluon else raw["m_q"]), helicity)


def unrank_pair_record(program: FactorizedScientificPairProgram, ordinal: int) -> dict[str, Any]:
    """Reconstruct one full C88 scientific record without a kernel query."""
    from ..ifkernel2.core import ContactKernelCoordinate
    leaf = unrank_pair_leaf(program, ordinal)
    payload = _payload(program.resolution)
    state = {row["id"]: (index, row) for index, row in enumerate(payload["physical_qg_basis"])}
    bra_index, bra = state[program.physical_bra_id]; ket_index, ket = state[program.physical_ket_id]
    output = _component(program.resolution, program.physical_bra_id, leaf["output_component_id"])
    incoming = _component(program.resolution, program.physical_ket_id, leaf["input_component_id"])
    out_raw, in_raw = _raw_basis(program.resolution)[leaf["output_component_id"]], _raw_basis(program.resolution)[leaf["input_component_id"]]
    out_c, out_a = _product_color(leaf["output_color_record_id"]); in_c, in_a = _product_color(leaf["input_color_record_id"])
    coordinate = ContactKernelCoordinate(program.resolution, out_raw["id"], out_raw["id"], in_raw["id"], in_raw["id"],
        _mode(out_raw, gluon=False, helicity=bra["helicity_q"]), _mode(out_raw, gluon=True, helicity=bra["helicity_g"]),
        _mode(in_raw, gluon=False, helicity=ket["helicity_q"]), _mode(in_raw, gluon=True, helicity=ket["helicity_g"]),
        out_c, out_a, in_c, in_a)
    colors = _color_records(); u3 = _u3()
    out_record, in_record = colors[leaf["output_color_record_id"]], colors[leaf["input_color_record_id"]]
    out_u = complex(u3[tuple(out_record["index"])]); in_u = complex(u3[tuple(in_record["index"])])
    out_value, in_value = complex(*output["midpoint"]), complex(*incoming["midpoint"])
    out_bound, in_bound = float(output["bound"]), float(incoming["bound"])
    out_color_bound, in_color_bound = float(out_record["bound"]), float(in_record["bound"])
    value = (out_value * out_u).conjugate() * (in_value * in_u)
    bound = (abs(out_value*out_u)*(abs(in_value)*in_color_bound + abs(in_u)*in_bound + in_bound*in_color_bound) +
             abs(in_value*in_u)*(abs(out_value)*out_color_bound + abs(out_u)*out_bound + out_bound*out_color_bound) +
             (abs(out_value)*out_color_bound + abs(out_u)*out_bound + out_bound*out_color_bound) *
             (abs(in_value)*in_color_bound + abs(in_u)*in_bound + in_bound*in_color_bound))
    status = "NONZERO_CERTIFIED_PROJECTED_COEFFICIENT_INTERVAL_EXCLUDES_ZERO" if abs(value) > bound else "CERTIFIED_PROJECTED_COEFFICIENT_INTERVAL_INCLUDES_ZERO_NO_EXACT_ZERO"
    ancestry = digest({"witness": program.witness_id, "leaf": leaf["leaf_id"], "output": leaf["output_component_id"], "input": leaf["input_component_id"], "output_color": leaf["output_color_record_id"], "input_color": leaf["input_color_record_id"]})
    record = {"schema_version": "C88-C82-SCIENTIFIC-PAIR-COORDINATE-V1", "environment_qualification": ENVIRONMENT,
              "resolution_id": program.resolution, "supported_pair_id": program.pair_id, "physical_bra_id": program.physical_bra_id,
              "physical_ket_id": program.physical_ket_id, "physical_row_index": bra_index, "physical_column_index": ket_index,
              "canonical_C80_coordinate_id": coordinate.id, "C80_coordinate_equivalence_id": coordinate.id,
              "projected_coefficient_identity": "conj(C77COMP_bra*U3_bra)*(C77COMP_ket*U3_ket)",
              "projected_coefficient_midpoint": [value.real, value.imag], "certified_absolute_bound": bound,
              "precision": 53, "interval_convention": "float64 midpoint +/- propagated absolute bound",
              "terminal_projected_coefficient_status": status, "factor_ownership_identity": "C82:embedding/metric/conjugation only; C80 owns W3/g_s2",
              "witness_multiplicity": 1, "ordered_witness_endpoint_ancestry_digest": ancestry,
              "C77_root": "09dcbb14b01d1534e02c5312b962e37b0b163308910b0291f360bf2e330b1769",
              "C78_root": "117f908d05b3396448049bb4c73cc66cdf04c77e07835d1704a0793fc80261bf",
              "C80_root": "9124653be0c676a716dda2e36ce901f19b7876fb0a0c0a5ca8cdf3e97c73bbd7",
              "C82_root": "d1889d3676e28e29fa7094a045b009024ea199c8691feeff72de2377a3bde934",
              "contains_no_C80_kernel_value": True, "contains_no_g_s_squared": True,
              "contains_no_coefficient_times_kernel_product": True, "local_ordinal": ordinal}
    return {**record, "canonical_record_id": "C88:REC:" + digest(record)}


def factorized_census() -> dict[str, Any]:
    rows = []
    for resolution in RESOLUTION_ORDER:
        programs = 0; records = 0; maximum = 0; first = last = None
        for program in iterate_pair_programs(resolution):
            programs += 1; records += program.logical_count; maximum = max(maximum, program.logical_count)
            first = program.pair_id if first is None else first; last = program.pair_id
        rows.append({"resolution": resolution, "supported_pairs": programs, "logical_records": records,
                     "maximum_records_in_pair": maximum, "first_pair_id": first, "last_pair_id": last})
    return {"schema": SCHEMA, "resolution_rows": rows, "supported_pairs": sum(x["supported_pairs"] for x in rows),
            "logical_records": sum(x["logical_records"] for x in rows), "census_sha256": digest(rows)}
