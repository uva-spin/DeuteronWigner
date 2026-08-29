"""C49 fail-closed audit of the canonical q-to-qg source chain.

No available locked source supplies a finite-box, C43-normalised QCD
``<qg|P^-_qqg|q>`` matrix element in the C45/C47 open-triplet module.  The
C47 arrays are therefore preserved and audited as raw composite tuples, not
reinterpreted as a vertex by inserting a convenient power of L, P+, or bHO.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

import numpy as np

from ..basis1.core import canonical_kernel, qg_basis, resolutions
from ..modes.core import array_hash

ROOT = Path(__file__).resolve().parents[4]
STATUS = "C49_CANONICAL_SOURCE_CHAIN_INCOMPLETE"
NEXT = "C50/VSRC — exact finite-volume light-front canonical-vertex source and convention closure"
BASELINE = "d237da980274a4d819b8881750fbbd189f0ef469"
RAW = ROOT / "data" / "raw" / "c49_sources"


def _read(name: str) -> dict[str, Any]:
    return json.loads((ROOT / "docs" / "next_level" / name).read_text())


def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _code_hash() -> str:
    return _sha(Path(__file__))


def additional_source_manifest() -> dict[str, Any]:
    """Hash-lock the official sources C49 acquired and audited."""
    rows = []
    for arxiv, title in [
        ("2503.21372v1", "Basis light-front quantization: Advancing a first principles approach for the nucleon"),
        ("2401.03480v1", "Quark and gluon distributions in rho-meson from basis light-front quantization"),
    ]:
        pdf, archive = RAW / f"{arxiv}.pdf", RAW / f"{arxiv}.tar"
        rows.append({
            "arxiv": arxiv, "title": title, "official_host": "arxiv.org",
            "pdf_path": str(pdf.relative_to(ROOT)), "archive_path": str(archive.relative_to(ROOT)),
            "pdf_sha256": _sha(pdf), "archive_sha256": _sha(archive),
            "pdf_bytes": pdf.stat().st_size, "archive_bytes": archive.stat().st_size,
            "audit_result": "INSUFFICIENT_FOR_C43_C45_C47_OPEN_TRIPLET_VERTEX",
        })
    return {"status": "HASH_LOCKED_AUDITED", "rows": rows}


def source_sufficiency_matrix() -> dict[str, Any]:
    """Source-level evidence, deliberately separated from numerical plausibility."""
    return {
        "status": STATUS,
        "required_rows": [
            {
                "id": "C49.SRC.C43_QCD_CANONICAL_ACTION",
                "authority": "hep-ph/0011372v2 Eq. (24)",
                "available": "continuum canonical QCD interaction and continuum field expansions",
                "missing": "finite-box C43/C45 state normalization and projected open-triplet q-to-qg matrix element",
                "classification": "SOURCE_CHAIN_INCOMPLETE",
            },
            {
                "id": "C49.SRC.C45_FINITE_CELL",
                "authority": "0905.1411v1 Eqs. (1)-(6),(14); C45 contract",
                "available": "cell-normalised one-particle longitudinal and HO modes",
                "missing": "C43 QCD field-expansion-to-C45 finite-box operator normalization and many-body q-to-qg matrix element",
                "classification": "SOURCE_CHAIN_INCOMPLETE",
            },
            {
                "id": "C49.SRC.C47_BL_FQ_NPI_ANALOGUE",
                "authority": "1911.10762v1 Appendix, Pion absorption Eq. following Eq. (P^-_int; abs)",
                "available": "finite-volume N-pion interaction and HO integral pattern",
                "missing": "QCD gamma^mu T^a quark-gluon vertex, C43 convention map, C45 polarization normalization, and open triplet color module",
                "classification": "ANALOGUE_NOT_SUBSTITUTABLE",
            },
            {
                "id": "C49.SRC.2503_QCD_BLFQ",
                "authority": "2503.21372v1 Eq. (QCD Hamiltonian) and basis paragraph",
                "available": "effective QCD BLFQ Hamiltonian description with qqq/qqqg sectors",
                "missing": "normalized q-to-qg matrix element; it uses fitted parameters, a color-singlet hadron module, and a distinct longitudinal convention",
                "classification": "MODEL_NOT_REGULATOR_IDENTICAL",
            },
            {
                "id": "C49.SRC.2401_QCD_BLFQ",
                "authority": "2401.03480v1 Eq. (QCD-Hamiltonian) and basis paragraph",
                "available": "effective q-qbar/q-qbar-g BLFQ Hamiltonian description",
                "missing": "normalized matrix elements; it includes confinement, counterterm/vertex-mass modelling, a color-singlet meson module, and a distinct longitudinal convention",
                "classification": "MODEL_NOT_REGULATOR_IDENTICAL",
            },
        ],
        "complete_required_rows": 0,
        "incomplete_required_rows": 5,
        "decision": "No source-qualified finite-volume C43/C45/C47 open-triplet canonical P-minus formula exists. It is prohibited to infer it from the N-pion analogue or phenomenological BLFQ Hamiltonians.",
    }


def _tuple_records() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for r in resolutions():
        values, tuples = canonical_kernel(r)
        qg_rows, _, _ = qg_basis(r)
        for raw_id, row in enumerate(values):
            outgoing = int(row[1])
            records.append({
                "resolution": r.label, "raw_tuple_id": raw_id,
                "incoming_q_basis_id": int(row[0]), "outgoing_qg_basis_id": outgoing,
                "mrel": int(qg_rows[outgoing][6]), "raw_real": float(row[2]), "raw_imag": float(row[3]),
                "raw_ancestry": tuples[raw_id][4:],
                "semantic_status": "AMBIGUOUS_BLOCKING",
                "reason": "The raw four-column value does not separately encode the QCD spinor/polarization numerator, transverse measure, finite-box state normalization, or C43 P-minus-to-M2 conversion.",
                "normalized_component_ids": [], "recomposed_pminus_tuple_id": None, "m2_tuple_id": None,
            })
    return records


@lru_cache(maxsize=1)
def _summary_json() -> str:
    by_resolution = []
    for r in resolutions():
        values, _ = canonical_kernel(r)
        qg_rows, _, _ = qg_basis(r)
        ms = [abs(int(qg_rows[int(row[1])][6])) for row in values]
        by_resolution.append({
            "resolution": r.label, "raw_tuple_count": int(values.shape[0]), "raw_tuple_sha256": array_hash(values),
            "mrel_abs_values": sorted(set(ms)), "raw_declared_unit": "L^(-1/2) GeV^(1+|mrel|)",
            "semantic_status_counts": {"AMBIGUOUS_BLOCKING": int(values.shape[0])},
        })
    return json.dumps({
        "status": STATUS, "baseline": BASELINE, "raw_tuples_preserved": True,
        "raw_tuple_records": by_resolution, "total_raw_tuples": sum(x["raw_tuple_count"] for x in by_resolution),
        "total_ambiguous_blocking": sum(x["raw_tuple_count"] for x in by_resolution),
        "source_sufficiency": source_sufficiency_matrix(), "generator_code_sha256": _code_hash(),
    }, sort_keys=True, separators=(",", ":"))


def raw_tuple_semantics_summary() -> dict[str, Any]:
    return json.loads(_summary_json())


def tuple_semantics_records() -> list[dict[str, Any]]:
    """Every raw tuple gets a deterministic, non-destructive semantic decision."""
    return _tuple_records()


def dimensional_type_system() -> dict[str, Any]:
    return {
        "natural_units": {"L": -1, "P_plus": 1, "b_HO": 1, "explicit_mass": 1, "g_s": 0, "x_K_TM": 0},
        "operator_targets": {"P_MINUS_MATRIX_ELEMENT": 1, "MASS_SQUARED_MATRIX_ELEMENT": 2},
        "raw_C47_signature": {"L": "-1/2", "P_plus": "UNSPECIFIED", "b_HO": "implicit and mrel-dependent", "total_mass_dimension": "1+|mrel|", "operator_type": "AMBIGUOUS_COMPOSITE"},
        "gate": "FAIL: source-level components are absent, so the raw signature cannot be converted to one P-minus or M2 operator signature without an unproved factor.",
    }


def validate_c49_summary(value: dict[str, Any]) -> bool:
    return value == raw_tuple_semantics_summary() and value["status"] == STATUS


def mutate_live_vertex_input(fault_id: int) -> dict[str, Any]:
    """Actual tuple/source/unit mutations rejected by exact gate validation."""
    value = deepcopy(raw_tuple_semantics_summary())
    record = value["raw_tuple_records"][fault_id % 3]
    choice = (fault_id // 3) % 8
    if choice == 0:
        record["raw_tuple_sha256"] = "0" * 64
    elif choice == 1:
        record["raw_tuple_count"] -= 1
    elif choice == 2:
        record["mrel_abs_values"] = [0]
    elif choice == 3:
        record["raw_declared_unit"] = "GeV^2"
    elif choice == 4:
        value["source_sufficiency"]["complete_required_rows"] = 1
    elif choice == 5:
        value["source_sufficiency"]["required_rows"][0]["classification"] = "SOURCE_COMPLETE"
    elif choice == 6:
        value["total_raw_tuples"] -= 1
    else:
        value["raw_tuples_preserved"] = False
    return value


def assert_canonical_source_chain_incomplete() -> dict[str, Any]:
    summary = raw_tuple_semantics_summary()
    assert summary["total_raw_tuples"] == 3618
    assert summary["total_ambiguous_blocking"] == 3618
    assert [x["raw_tuple_count"] for x in summary["raw_tuple_records"]] == [720, 1170, 1728]
    assert all(x["mrel_abs_values"] == [0, 1] for x in summary["raw_tuple_records"])
    assert summary["source_sufficiency"]["complete_required_rows"] == 0
    assert validate_c49_summary(summary)
    return summary
