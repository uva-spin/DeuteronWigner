"""C401 source-faithful longitudinal basis and fraction authority.

This module binds the C396 mass-direction implementation to the exact C45/C47
longitudinal partitions while preserving the C128 direct-sum basis dimensions
and partition-major block structure.  It also records, rather than silently
repairing, a historical defect in ``free2.core._partitions``: the C128 quark
fraction is larger than the source-qualified C47 value by ``1/K2`` at every
retained partition.  The gluon fraction is unaffected.

The mass-direction operators are constant within each longitudinal partition,
so their numerical action does not depend on the unresolved transverse
sub-ordering difference between C47 and the historical C128 helper.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from typing import Any, Mapping

from deuteron_wigner.bridge.basis1 import core as c47
from deuteron_wigner.bridge.free2 import core as c128

RESOLUTION_LABELS = ("K9", "K11", "K13")
C128_RESOLUTION_BY_LABEL = {
    "K9": "K9_2_N8_b0.40",
    "K11": "K11_2_N10_b0.45",
    "K13": "K13_2_N12_b0.50",
}
LABEL_BY_C128_RESOLUTION = {value: key for key, value in C128_RESOLUTION_BY_LABEL.items()}
_C47_RESOLUTION_BY_FULL_LABEL = {resolution.label: resolution for resolution in c47.RESOLUTIONS}


@dataclass(frozen=True)
class LongitudinalPartition:
    resolution: str
    partition_id: int
    kq: Fraction
    kg: Fraction
    xq: Fraction
    xg: Fraction
    qg_direct_start: int
    qg_direct_stop: int
    qg_state_count: int

    def to_record(self) -> dict[str, Any]:
        record = asdict(self)
        for key in ("kq", "kg", "xq", "xg"):
            value = record[key]
            record[key] = {
                "numerator": value.numerator,
                "denominator": value.denominator,
                "exact": str(value),
                "float": float(value),
            }
        record["fraction_sum_exact"] = str(self.xq + self.xg)
        record["fraction_sum_residual"] = float(self.xq + self.xg - 1)
        return record


def _canonical_json(value: Any) -> str:
    def plain(item: Any) -> Any:
        if isinstance(item, Fraction):
            return [item.numerator, item.denominator]
        if isinstance(item, Mapping):
            return {str(key): plain(val) for key, val in item.items()}
        if isinstance(item, (tuple, list)):
            return [plain(val) for val in item]
        return item

    return json.dumps(plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def content_root(value: Any) -> str:
    return sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def normalize_resolution(resolution: str) -> tuple[str, str]:
    if resolution in C128_RESOLUTION_BY_LABEL:
        return resolution, C128_RESOLUTION_BY_LABEL[resolution]
    if resolution in LABEL_BY_C128_RESOLUTION:
        return LABEL_BY_C128_RESOLUTION[resolution], resolution
    raise KeyError(resolution)


def resolution_record(resolution: str) -> dict[str, Any]:
    label, full = normalize_resolution(resolution)
    c47_resolution = _C47_RESOLUTION_BY_FULL_LABEL[full]
    if full not in c128.RESOLUTIONS:
        raise RuntimeError(f"C128 resolution missing: {full}")
    if c47_resolution.K != Fraction(c128.K[full]):
        raise RuntimeError(f"C47/C128 K mismatch at {full}")
    if c47_resolution.Nmax != c128.NMAX[full]:
        raise RuntimeError(f"C47/C128 Nmax mismatch at {full}")
    if Fraction(str(c47_resolution.b_GeV)) != Fraction(c128.BHO[full]):
        raise RuntimeError(f"C47/C128 b_HO mismatch at {full}")
    return {
        "resolution_label": label,
        "full_resolution_id": full,
        "K2": c47_resolution.K.numerator,
        "K_fraction": str(c47_resolution.K),
        "K_numerator": c47_resolution.K.numerator,
        "K_denominator": c47_resolution.K.denominator,
        "Nmax": c47_resolution.Nmax,
        "b_HO": float(c47_resolution.b_GeV),
        "b_HO_unit": "GeV",
        "C47_b_HO_field": "b_GeV",
        "C396_b_HO_metadata_field": "bHO_GeVinv",
        "C396_b_HO_unit_label_conflict_retained": True,
        "mass_direction_depends_on_b_HO": False,
        "q_dimension": c128.Q_DIM,
        "qg_dimension": c128.QG_DIMS[full],
        "direct_sum_dimension": c128.DIRECT_DIMS[full],
        "basis_order": "C128/C112 q sector followed by qg sector; qg partition-major",
        "C128_package_root": c128.PACKAGE_ROOT,
        "C47_status": c47.STATUS,
    }


@lru_cache(maxsize=None)
def canonical_partitions(resolution: str) -> tuple[LongitudinalPartition, ...]:
    label, full = normalize_resolution(resolution)
    c47_resolution = _C47_RESOLUTION_BY_FULL_LABEL[full]
    source_partitions = tuple(c47.partitions(c47_resolution))
    if not source_partitions:
        raise RuntimeError(f"no C47 qg partitions for {full}")
    qg_dimension = c128.QG_DIMS[full]
    if qg_dimension % len(source_partitions) != 0:
        raise RuntimeError(f"qg dimension does not factor by partition count at {full}")
    states_per_partition = qg_dimension // len(source_partitions)
    rows: list[LongitudinalPartition] = []
    for partition_id, (kq, kg, xq, xg) in enumerate(source_partitions):
        if kq + kg != c47_resolution.K:
            raise RuntimeError(f"longitudinal mode sum failure at {full}, partition {partition_id}")
        if xq <= 0 or xg <= 0 or xq + xg != 1:
            raise RuntimeError(f"invalid longitudinal fractions at {full}, partition {partition_id}")
        start = c128.Q_DIM + partition_id * states_per_partition
        stop = start + states_per_partition
        rows.append(
            LongitudinalPartition(
                resolution=label,
                partition_id=partition_id,
                kq=kq,
                kg=kg,
                xq=xq,
                xg=xg,
                qg_direct_start=start,
                qg_direct_stop=stop,
                qg_state_count=states_per_partition,
            )
        )
    if rows[-1].qg_direct_stop != c128.DIRECT_DIMS[full]:
        raise RuntimeError(f"partition blocks do not close the direct-sum basis at {full}")
    return tuple(rows)


def partition_for_direct_index(resolution: str, direct_index: int) -> LongitudinalPartition | None:
    _, full = normalize_resolution(resolution)
    if not 0 <= direct_index < c128.DIRECT_DIMS[full]:
        raise IndexError(direct_index)
    if direct_index < c128.Q_DIM:
        return None
    rows = canonical_partitions(resolution)
    states_per_partition = rows[0].qg_state_count
    partition_id = (direct_index - c128.Q_DIM) // states_per_partition
    return rows[partition_id]


def basis_fraction_provenance(resolution: str) -> dict[str, Any]:
    record = resolution_record(resolution)
    partitions = canonical_partitions(resolution)
    full = record["full_resolution_id"]
    # C128's private decoder is consulted only as a frozen ordering audit.  The
    # numerical fractions come exclusively from the public C47 partitions.  A
    # boundary audit is sufficient because ``_qg_decode`` uses a fixed stride;
    # it avoids decoding every transverse/helicity/color state at large K.
    decoder_boundary_rows: list[dict[str, Any]] = []
    partition_major_match = True
    qg_offset = 0
    for partition in partitions:
        local_start = qg_offset
        local_stop = qg_offset + partition.qg_state_count
        first_decoded = int(
            c128._qg_decode(full, local_start)[0]  # noqa: SLF001 - historical audit only
        )
        last_decoded = int(
            c128._qg_decode(full, local_stop - 1)[0]  # noqa: SLF001 - historical audit only
        )
        row_pass = first_decoded == partition.partition_id == last_decoded
        partition_major_match = partition_major_match and row_pass
        decoder_boundary_rows.append(
            {
                "partition_id": partition.partition_id,
                "local_start": local_start,
                "local_stop": local_stop,
                "first_decoded_partition": first_decoded,
                "last_decoded_partition": last_decoded,
                "pass": row_pass,
            }
        )
        qg_offset = local_stop
    partition_major_match = partition_major_match and qg_offset == c128.QG_DIMS[full]
    if not partition_major_match:
        raise RuntimeError(f"C128 qg partition-major ordering mismatch at {full}")
    payload = {
        "schema": "C401-C396-MASS-BASIS-FRACTION-PROVENANCE-V1",
        "resolution": record,
        "partitions": tuple(partition.to_record() for partition in partitions),
        "partition_count": len(partitions),
        "states_per_partition": partitions[0].qg_state_count,
        "partition_major_order_verified": partition_major_match,
        "decoder_boundary_rows": tuple(decoder_boundary_rows),
        "transverse_subordering_used_by_mass_directions": False,
        "fraction_authority": "C45/C47 exact positive APBC/PBC partitions x=k/K",
        "direct_sum_dimension_authority": "C128/C112",
        "all_fractions_positive": all(partition.xq > 0 and partition.xg > 0 for partition in partitions),
        "all_fraction_sums_exactly_one": all(partition.xq + partition.xg == 1 for partition in partitions),
    }
    return {**payload, "root": content_root(payload)}


def _fraction_from_historical_string(value: str) -> Fraction:
    return Fraction(value)


def historical_c128_partition_defect_audit() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    affected_resolutions: list[str] = []
    for label in RESOLUTION_LABELS:
        _, full = normalize_resolution(label)
        canonical = canonical_partitions(label)
        historical = tuple(c128._partitions(full))  # noqa: SLF001 - explicit historical audit
        if len(historical) != len(canonical):
            raise RuntimeError(f"historical/canonical partition count mismatch at {full}")
        resolution_defect = False
        for source, old in zip(canonical, historical):
            old_kq, old_kg, old_xq, old_xg = (
                _fraction_from_historical_string(str(value)) for value in old
            )
            row = {
                "resolution": label,
                "full_resolution_id": full,
                "partition_id": source.partition_id,
                "canonical": {
                    "kq": str(source.kq),
                    "kg": str(source.kg),
                    "xq": str(source.xq),
                    "xg": str(source.xg),
                    "sum": str(source.xq + source.xg),
                },
                "historical_C128": {
                    "kq": str(old_kq),
                    "kg": str(old_kg),
                    "xq": str(old_xq),
                    "xg": str(old_xg),
                    "sum": str(old_xq + old_xg),
                },
                "kq_residual": str(old_kq - source.kq),
                "kg_residual": str(old_kg - source.kg),
                "xq_residual": str(old_xq - source.xq),
                "xg_residual": str(old_xg - source.xg),
                "fraction_sum_residual": str(old_xq + old_xg - 1),
                "quark_fraction_match": old_xq == source.xq,
                "gluon_fraction_match": old_xg == source.xg,
            }
            if not row["quark_fraction_match"] or old_kq != source.kq:
                resolution_defect = True
            rows.append(row)
        if resolution_defect:
            affected_resolutions.append(label)
    payload = {
        "schema": "C401-HISTORICAL-C128-PARTITION-DEFECT-AUDIT-V1",
        "status": "HISTORICAL_C128_LONGITUDINAL_QUARK_FRACTION_IMPLEMENTATION_DEFECT_CONFIRMED",
        "C128_historical_package_root": c128.PACKAGE_ROOT,
        "C47_source_status": c47.STATUS,
        "affected_resolutions": tuple(affected_resolutions),
        "rows": tuple(rows),
        "defect_pattern": "historical kq and xq exceed C47 values by 1/2 and 1/K2 respectively",
        "gluon_fraction_affected": False,
        "quark_mass_derivative_affected": True,
        "qg_transverse_kinetic_denominator_affected": True,
        "C144_ID_derived_diagnostic_operator_directly_uses_C128_partition_values": False,
        "C144_diagnostic_status_changed": False,
        "historical_files_modified": False,
        "C401_policy": (
            "preserve C128 history; use C47 fractions in a versioned C401 mass-direction adapter"
        ),
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "RESOLUTION_LABELS",
    "C128_RESOLUTION_BY_LABEL",
    "LABEL_BY_C128_RESOLUTION",
    "LongitudinalPartition",
    "content_root",
    "normalize_resolution",
    "resolution_record",
    "canonical_partitions",
    "partition_for_direct_index",
    "basis_fraction_provenance",
    "historical_c128_partition_defect_audit",
]
