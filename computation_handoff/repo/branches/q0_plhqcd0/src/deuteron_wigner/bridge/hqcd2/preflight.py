"""C48 fail-closed audit of the C47-to-local-QCD matrix interface.

C47 deliberately exposes a basis, an invariant-mass *functional*, and a
canonical kinematic tuple functional.  It does not expose a uniformly
normalised coefficient of the invariant-mass operator.  In particular its
committed canonical object declares units ``L^(-1/2) GeV^(1+|m|)``.  Since
the same putative matrix contains both ``|m|=0`` and ``|m|=1`` entries, it
cannot be a matrix of one operator until a source-derived common conversion
and finite-volume normalization are supplied.  Choosing those factors here
would be precisely the prohibited fabricated C48 vertex.
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
STATUS = "C48_CANONICAL_VERTEX_ASSEMBLY_INCOMPLETE"
NEXT = "C49/VERTEX1 — exhaustive tuple/SU(3)/triplet canonical-matrix completion"
BASELINE = "055f2a3dd5a651cc687f532f4c0ea58d885dd585"


def _read(name: str) -> dict[str, Any]:
    return json.loads((ROOT / "docs" / "next_level" / name).read_text())


def _code_hash() -> str:
    return sha256(Path(__file__).read_bytes()).hexdigest()


def _runtime_record(name: str, expected: dict[str, Any]) -> dict[str, Any]:
    path = ROOT / expected["runtime_path"]
    present = path.is_file()
    observed = None
    if present:
        observed = array_hash(np.load(path, allow_pickle=False))
    return {
        "name": name,
        "classification": "SOURCE_DERIVED_EXECUTABLE",
        "runtime_path": expected["runtime_path"],
        "present": present,
        "expected_sha256": expected["array_sha256"],
        "observed_sha256": observed,
        "hash_match": observed == expected["array_sha256"],
        "source_link": "C47 numerical object inventory plus C47 source-relevance matrix",
    }


def input_fidelity_audit() -> dict[str, Any]:
    """Verify that C48 consumes actual C47 objects, never C40 stand-ins."""
    c47_contract = _read("c47_basis_assembly_contract_matrix.json")
    c47_inventory = _read("c47_numerical_object_inventory.json")["objects"]
    c47_interface = _read("c47_c48_matrix_assembly_interface.json")
    required = [
        "free_functional_K9_2_N8_b0.40",
        "free_functional_K11_2_N10_b0.45",
        "free_functional_K13_2_N12_b0.50",
        "canonical_kernel_K9_2_N8_b0.40",
        "canonical_kernel_K11_2_N10_b0.45",
        "canonical_kernel_K13_2_N12_b0.50",
        "P0", "Q0", "inverse_d1", "inverse_d2", "qg_triplet_isometry",
    ]
    records = [_runtime_record(name, c47_inventory[name]) for name in required]
    rows = {item["row"]: item["status"] for item in c47_contract["rows"]}
    return {
        "status": "C48_INPUT_FIDELITY_AUDIT_COMPLETE",
        "baseline": BASELINE,
        "c43": "C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION",
        "c45": "C45_SOURCE_DERIVED_MODE_PROJECTION_READY",
        "c47": c47_contract["status"],
        "c40": "EXECUTABLE_METHOD_ORACLE_ONLY; not consumed",
        "contract_rows": rows,
        "required_runtime_records": records,
        "source_derived_functionals": [
            "C47 free_functional (not a final matrix)",
            "C47 canonical_kernel (not a final SU(3) vertex)",
            "C47 inverse_derivative_functionals",
            "C47 CM-ground TM isometries and comparison maps",
        ],
        "interface": c47_interface,
        "all_required_runtime_hashes_match": all(x["hash_match"] for x in records),
        "generator_code_sha256": _code_hash(),
    }


def _canonical_resolution_record(resolution) -> dict[str, Any]:
    values, tuples = canonical_kernel(resolution)
    qg_rows, _, _ = qg_basis(resolution)
    m_by_tuple = [int(qg_rows[int(row[1])][6]) for row in values]
    present_abs_m = sorted({abs(m) for m in m_by_tuple})
    declared_unit = "L^(-1/2) GeV^(1+|m|)"
    return {
        "resolution": resolution.label,
        "tuple_shape": list(values.shape),
        "tuple_count": len(tuples),
        "tuple_array_sha256": array_hash(values),
        "nonzero_value_count": int(np.count_nonzero(values[:, 2] + 1j * values[:, 3])),
        "outgoing_m_abs_values": present_abs_m,
        "declared_unit": declared_unit,
        "single_operator_unit": False,
        "single_operator_unit_reason": (
            "The committed C47 object contains |mrel|=0 and |mrel|=1 entries "
            "but declares GeV^(1+|mrel|); a matrix coefficient cannot have "
            "entry-dependent physical dimensions."
        ),
        "symbolic_L": "L^(-1/2) is retained but no C43-to-M^2 finite-volume conversion is supplied",
    }


@lru_cache(maxsize=1)
def _canonical_vertex_audit_json() -> str:
    """Establish the exact, targeted reason C48 may not create V_qg<-q."""
    contract = _read("c47_free_operator_normalization_contract.json")
    interface = _read("c47_c48_matrix_assembly_interface.json")
    records = [_canonical_resolution_record(r) for r in resolutions()]
    blockers = [
        {
            "id": "C48.CANONICAL.UNIFORM_OPERATOR_UNITS",
            "observed": "C47 canonical inventory declares L^(-1/2) GeV^(1+|m|); every physical resolution contains |mrel|=0 and |mrel|=1 tuples.",
            "source_requirement": "A coefficient of M^2 has one project-unit convention for every matrix element.",
            "blocking_reason": "No source-derived common dimensional conversion exists. Multiplying selected tuples by b, P+, L, or a fitted factor would alter the C47 functional and fabricate a vertex.",
            "required_correction": "Derive the complete C43/SB finite-volume canonical M^2 matrix-element normalization, including all transverse numerator components, and validate a uniform-unit tuple table.",
        },
        {
            "id": "C48.CANONICAL.M2_CONVERSION",
            "observed": "C47 fixes M^2=2P+P--Pperp^2 for the free functional, while its canonical interface only says L^(-1/2) is retained.",
            "source_requirement": "An explicit C43-normalized conversion of the canonical P^- term to a coupling-factored M^2 coefficient.",
            "blocking_reason": "The required 2P+ and field-normalization factors are not represented as a source-checked, dimensionally uniform operator formula.",
            "required_correction": "Add a primary-source equation -> C43 convention map -> finite-volume field expansion -> M^2 tuple formula, with symbolic-L cancellation or factorization proof.",
        },
        {
            "id": "C48.CANONICAL.EXHAUSTIVE_MATRIX_ELEMENT_CONTRACT",
            "observed": "C47 exposes kinematic tuples, not a finished canonical matrix; its C48 interface expressly assigns SU(3) insertion and matrix assembly to C48.",
            "source_requirement": "Every final nonzero must carry a single normalized matrix-element formula traceable through color, triplet isometry, and finite-volume normalization.",
            "blocking_reason": "Because the underlying tuple has no admissible common M^2 normalization, inserting SU(3) and the 24x3 isometry would make an array but not the required physical operator.",
            "required_correction": "C49/VERTEX1 must repair the source-derived tuple contract before C48 is retried; generated absorption remains deferred to the valid emission matrix.",
        },
    ]
    value = {
        "status": STATUS,
        "next": NEXT,
        "fixed_scheme": "O4-SPACELIKE-COLLINS-JMY",
        "fixed_gauge": "G0-LIGHT-FRONT-GAUGE; A+=0; PV on Q0",
        "free_operator_contract": contract,
        "c47_interface": interface,
        "canonical_resolution_records": records,
        "blockers": blockers,
        "prohibited_response": "Do not choose L, bHO, P+, or a C40 coefficient to homogenize the tuple dimensions; do not construct a surrogate vertex or any downstream local matrix.",
        "result": "No C48 free, canonical, instantaneous, constrained, boundary, zero-mode, counterterm, or block-operator matrix is generated, because the earliest required canonical operator gate is incomplete.",
        "generator_code_sha256": _code_hash(),
    }
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def canonical_vertex_audit() -> dict[str, Any]:
    """Return a fresh mutable copy of the deterministic, expensive audit."""
    return json.loads(_canonical_vertex_audit_json())


def validate_canonical_vertex_audit(value: dict[str, Any]) -> bool:
    """Exact deterministic validator used by live source-to-gate mutations."""
    return value == canonical_vertex_audit() and value["status"] == STATUS


def mutate_live_canonical_input(fault_id: int) -> dict[str, Any]:
    """Mutate a concrete tuple/normalization audit field; never an identifier alone."""
    value = deepcopy(canonical_vertex_audit())
    record = value["canonical_resolution_records"][fault_id % 3]
    choice = (fault_id // 3) % 8
    if choice == 0:
        record["tuple_array_sha256"] = "0" * 64
    elif choice == 1:
        record["tuple_count"] -= 1
    elif choice == 2:
        record["nonzero_value_count"] += 1
    elif choice == 3:
        record["outgoing_m_abs_values"] = [0]
    elif choice == 4:
        record["declared_unit"] = "GeV^2"
    elif choice == 5:
        record["single_operator_unit"] = True
    elif choice == 6:
        value["free_operator_contract"]["operator"] = "P-"
    else:
        value["blockers"][fault_id % len(value["blockers"])]["blocking_reason"] = "removed"
    return value


def assert_canonical_vertex_assembly_incomplete() -> dict[str, Any]:
    fidelity = input_fidelity_audit()
    audit = canonical_vertex_audit()
    assert fidelity["all_required_runtime_hashes_match"]
    assert all(r["outgoing_m_abs_values"] == [0, 1] for r in audit["canonical_resolution_records"])
    assert all(not r["single_operator_unit"] for r in audit["canonical_resolution_records"])
    assert validate_canonical_vertex_audit(audit)
    return audit
