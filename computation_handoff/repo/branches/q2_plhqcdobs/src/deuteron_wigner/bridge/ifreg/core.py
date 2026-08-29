"""C57 fixed-K conditional HO regulator, prior to any self-inertia sum.

The regulator is deliberately not BPP/TBP DLCQ.  It applies TBP's
corresponding-propagating-graph rule to the source-qualified C45 field modes
and the C47 fixed-K Fock projection.  The result is a family of conditional
finite-rank field projectors indexed by the incoming quark state, plus a
separate universal C45 one-particle *envelope*.  No C53 numerical value, C47
historical tuple value, counterterm, or contraction coefficient is consumed.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import ast
import inspect
import json
from math import pi
from pathlib import Path
from typing import Any

import numpy as np

from ..basis1.core import partitions, q_basis, qg_basis, tm_cm_ground_map
from ..ifnorm.core import contraction_preflight
from ..modes.core import (
    RESOLUTIONS, array_hash, gell_mann, ho_coordinate, ho_labels,
    longitudinal_values, zero_mode_projectors,
)

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "1b49803a7a08d12feb5caca80f4c18b0aab795b6"
STATUS = "C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY"
NEXT = "C58/IFNORM2 — execute the self-induced-inertia contraction"
BLOCKER = "C57.IFREG.FIELD_REGULATOR_CONSTRUCTION"
PLAN = "IFREG-CORRESPONDING-PROPAGATING-SUPPORT"
ORDER = "CORRESPONDING_PROPAGATING_GRAPH_PROJECT"
THRESHOLD = 1.0e-12


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def _hash(value: Any) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def _mode_hash(mode: tuple) -> str:
    return _hash(mode)


def source_hierarchy() -> dict[str, Any]:
    return {
        "status": "SOURCE_COMPLETE_AT_DECLARED_SCOPE",
        "rows": [
            {"source": "SB hep-ph/0011372v2 Eq.(24)", "role": "ACTION_AND_COMMUTATOR_AUTHORITY", "scope": "C55 instantaneous constrained-fermion operator"},
            {"source": "BPP hep-ph/9705477v1 Eq.(2.97), Sec.2 and DLCQ contraction table", "role": "DLCQ_REGULATOR_AUTHORITY", "scope": "normal ordering/self-induced inertia in distinct DLCQ momentum regulator"},
            {"source": "Tang--Brodsky--Pauli, SLAC-PUB-5425 / Phys.Rev.D 44, 1842 (1991), Secs.3,5; p.27", "role": "CORRESPONDING_PROPAGATING_GRAPH_TRUNCATION_AUTHORITY", "scope": "instantaneous graph retained/cut in the same set as its corresponding real intermediate state"},
            {"source": "Li--Lappi--Zhao--Salgado arXiv:2504.07162v1 Appendix B, lines app:inst", "role": "CORRESPONDING_PROPAGATING_GRAPH_TRUNCATION_AUTHORITY", "scope": "q+qg example: instantaneous terms in q but not qg sector; transverse representation is a finite momentum lattice"},
            {"source": "0905.1411v1; 1311.2980v1", "role": "BLFQ_ONE_PARTICLE_BASIS_AUTHORITY", "scope": "C45 finite cell and normalized 2D-HO modes"},
            {"source": "1911.10762v1", "role": "BLFQ_MANY_BODY_TRUNCATION_AUTHORITY", "scope": "C47 x-weighted TM/CM and Nmax projection"},
            {"source": "C53", "role": "NOT_OPERATOR_REGULATOR_IDENTICAL", "scope": "read-only support/basis holdout; numerical matrix values forbidden"},
            {"source": "0801.4507; 1402.4195; 1404.6234", "role": "SECTOR_RENORMALIZATION_METHOD_COMPARISON", "scope": "not used to choose a C57 counterterm or regulator map"},
        ],
    }


def operation_order() -> dict[str, Any]:
    return {
        "selected": ORDER,
        "selected_definition": "At fixed K, first apply the TBP corresponding-propagating selection to the source canonical q->qg candidate space and C47 Fock/CM/triplet restrictions. The induced conditional field projector is then normal ordered.",
        "alternatives": [
            {"id": "FIELD_PROJECT_THEN_NORMAL_ORDER", "status": "REJECTED_AS_PRIMARY", "reason": "a universal C45 one-particle envelope exists but cannot by itself encode the fixed-K many-body/CM/triplet propagating support"},
            {"id": "NORMAL_ORDER_THEN_FOCK_PROJECT", "status": "REJECTED_AS_PRIMARY", "reason": "it leaves the full source commutator in place before the truncation-dependent graph-selection rule"},
            {"id": ORDER, "status": "SELECTED", "reason": "TBP requires instantaneous and corresponding real intermediate graphs to be retained/cut together; C57 implements this as a fixed-K conditional support"},
            {"id": "DLCQ_REGULATE_THEN_CONVERT_TO_HO", "status": "REJECTED", "reason": "no finite DLCQ-to-C45-HO conversion is source-qualified"},
            {"id": "OPERATION_ORDER_UNAVAILABLE", "status": "REJECTED", "reason": "the selected project-specific conditional construction is explicit"},
        ],
        "noncommutativity": "P_R N(A A) P_R - N(P_R A P_R P_R A P_R) contains P_R A (1-P_R) A P_R and its reversed-order commutator term; it vanishes only under an additional closure proof, which is not assumed.",
        "status": "SOURCE_DERIVED_PROJECT_SPECIFIC_ORDER",
    }


def regulator_plan() -> dict[str, Any]:
    return {
        "selected": PLAN,
        "definition": "A fixed-total-K conditional finite-HO/Fock regulator: source C45 field modes provide the one-particle envelope; source C47 CM-clean qg Fock projection plus TBP corresponding-propagating selection induce Pi_g,R|alpha. It is not a universal field projector and not BPP DLCQ.",
        "plans": [
            {"id": "IFREG-UNIVERSAL-PROJECTED-HO-FIELD", "status": "REJECTED_AS_PRIMARY", "reason": "the C45 envelope does not encode qg many-body, CM, triplet, or canonical reachability"},
            {"id": "IFREG-FIXED-K-FOCK-PROJECTED-FIELD", "status": "COMPONENT_OF_SELECTED_PLAN", "reason": "fixed-K C47 Fock/CM/triplet projection is applied, but TBP graph matching is additionally required"},
            {"id": PLAN, "status": "SELECTED", "reason": "TBP graph matching supplies the conditional support rule; C45/C47 supply the project-specific HO and Fock realization"},
            {"id": "IFREG-DLCQ-LONGITUDINAL-HO-TRANSVERSE-HYBRID", "status": "REJECTED", "reason": "would create a new hybrid without need; it cannot be named BPP DLCQ"},
            {"id": "IFREG-EXACT-DLCQ-TO-HO-CONVERSION", "status": "REJECTED", "reason": "source momentum cutoffs and C45 HO shell have no exact finite conversion"},
            {"id": "IFREG-UNAVAILABLE", "status": "REJECTED", "reason": "C57 provides an honestly conditional regulator rather than claiming a universal one"},
        ],
        "status": "SELECTED_CONDITIONAL_PROJECTOR",
    }


def _field_envelope(r: Any) -> list[tuple]:
    """C45 one-particle field envelope at fixed K, before Fock conditioning."""
    modes = []
    for _, kg, _, _ in partitions(r):
        for ng, mg in ho_labels(r.Nmax):
            for hg in (-1, 1):
                for adj in range(8):
                    modes.append((kg, ng, mg, hg, adj, "PBC_NONZERO", r.b_GeV, r.label))
    return modes


def _allowed_adjoint(in_color: int) -> tuple[int, ...]:
    t = gell_mann()
    return tuple(a for a in range(8) if np.linalg.norm(t[a][:, in_color]) > THRESHOLD)


def _physical_selection(parent_h: int, parent_c: int, row: tuple) -> bool:
    _, _, _, _, _, _nrel, mrel, _, _, hq, hg, out_c, _, _ = row
    # The canonical bilinear has no additional source-owned |m_rel| cap.
    # Its allowed transverse OAM follows from exact Jz conservation; the C47
    # many-body Nmax rule supplies the finite limit.  The old |m|<=1 C47
    # tuple helper is diagnostic-only and is intentionally not consulted.
    return out_c == parent_c and Fraction(parent_h, 2) == Fraction(hq, 2) + hg + mrel


def _conditional_support(r: Any, envelope: list[tuple]) -> tuple[np.ndarray, np.ndarray, list[dict[str, Any]]]:
    """Source-rule support, not a C53-value support mask.

    qg rows are only C47 kinematic/CM/triplet basis identities.  Canonical
    selection uses total K, exact Jz, the C47 Nmax limit, and the raw SU(3)
    T^a emission image computed from the C45 convention.
    """
    qrows = q_basis(r); qgrows, maps, _ = qg_basis(r)
    envelope_index = {mode: i for i, mode in enumerate(envelope)}
    qg_mask = np.zeros((len(qrows), len(qgrows)), dtype=np.uint8)
    field_mask = np.zeros((len(qrows), len(envelope)), dtype=np.uint8)
    maps_by_part = []
    for part_id, (_, _, xq, _) in enumerate(partitions(r)):
        intr, product, cm = tm_cm_ground_map(xq, r.Nmax - 2)
        maps_by_part.append(({label: idx for idx, label in enumerate(intr)}, product, cm))
    records: list[dict[str, Any]] = []
    for iq, (_, _, _, hp, cp, _, _) in enumerate(qrows):
        for jq, row in enumerate(qgrows):
            if not _physical_selection(hp, cp, row):
                continue
            qg_mask[iq, jq] = 1
            part, _, kg, _, _, nrel, mrel, _, _, hq, hg, _, _, _ = row
            rel_index, product, cm = maps_by_part[part]
            rel = rel_index[(nrel, mrel)]
            raw_indices = np.flatnonzero(np.abs(cm[rel]) > THRESHOLD)
            for raw in raw_indices:
                _, _, ng, mg = product[int(raw)]
                for adj in _allowed_adjoint(cp):
                    mode = (kg, ng, mg, hg, adj, "PBC_NONZERO", r.b_GeV, r.label)
                    field_mask[iq, envelope_index[mode]] = 1
        records.append({"incoming_q_id": iq, "helicity": hp, "fundamental_color": cp, "qg_support_rank": int(qg_mask[iq].sum()), "conditional_field_rank": int(field_mask[iq].sum())})
    return qg_mask, field_mask, records


def _kernel(r: Any, envelope: list[tuple], mask: np.ndarray) -> np.ndarray:
    """Finite-rank scalar trace of the conditional coordinate-space kernel."""
    y = np.array([0.0, 0.29, -0.41], dtype=float)  # x^-/L; L stays symbolic.
    xy = np.array([[0.0, 0.0], [0.7 / r.b_GeV, -0.2 / r.b_GeV], [-0.4 / r.b_GeV, 0.6 / r.b_GeV]])
    values = np.zeros((mask.shape[0], len(y), len(xy)), dtype=np.complex128)
    for j, (kg, n, m, _h, _a, _b, b, _label) in enumerate(envelope):
        if not mask[:, j].any():
            continue
        longitudinal = longitudinal_values([kg], y)[0]
        transverse = ho_coordinate(n, m, xy[:, 0], xy[:, 1], b)
        values += mask[:, j, None, None] * longitudinal[None, :, None] * transverse[None, None, :]
    flat = values.reshape(values.shape[0], -1)
    return np.einsum("ai,aj->aij", flat, np.conjugate(flat), optimize=True)


def _resolution_record(r: Any) -> dict[str, Any]:
    envelope = _field_envelope(r)
    qg_mask, field_mask, parent_records = _conditional_support(r, envelope)
    max_k = int(r.K)
    p0, q0 = zero_mode_projectors(max_k)
    long_diag = np.real(np.diag(q0)[1:]).astype(np.uint8)
    trans_labels = ho_labels(r.Nmax)
    trans_diag = np.ones(len(trans_labels), dtype=np.uint8)
    kernel = _kernel(r, envelope, field_mask)
    field_diag = field_mask.astype(np.uint8)
    shell = np.asarray([2*n + abs(m) + 1 for _, n, m, *_ in envelope], dtype=np.int16)
    shell_ranks = {str(s): [int(np.count_nonzero(field_mask[i] & (shell == s))) for i in range(field_mask.shape[0])] for s in sorted(set(shell.tolist()))}
    return {
        "resolution": r.label, "K": str(r.K), "Nmax": r.Nmax, "bHO_GeV": r.b_GeV,
        "envelope_modes": envelope, "field_mask": field_diag, "qg_mask": qg_mask, "kernel": kernel,
        "longitudinal_diag": long_diag, "transverse_diag": trans_diag, "p0": p0, "q0": q0,
        "shell": shell, "parents": parent_records, "shell_ranks": shell_ranks,
    }


def _metadata(record: dict[str, Any]) -> dict[str, Any]:
    envelope = record["envelope_modes"]
    return {
        "resolution": record["resolution"], "K": record["K"], "Nmax": record["Nmax"], "bHO_GeV": record["bHO_GeV"],
        "envelope_mode_count": len(envelope), "conditional_type": "INCOMING_QUARK_INDEXED_FIELD_PROJECTOR",
        "conditional_ranks": [x["conditional_field_rank"] for x in record["parents"]], "qg_ranks": [x["qg_support_rank"] for x in record["parents"]],
        "longitudinal_support": sorted({str(x[0]) for x in envelope}), "zero_mode": "k_g=0 excluded from primary Q0 field envelope; retained P0/residual controls separate",
        "shell_ranks": record["shell_ranks"], "mode_set_hash": _hash(envelope), "field_mask_hash": array_hash(record["field_mask"]),
        "qg_mask_hash": array_hash(record["qg_mask"]), "kernel_hash": array_hash(record["kernel"]),
    }


def _assert_record(record: dict[str, Any]) -> None:
    assert np.all(record["longitudinal_diag"] == 1)
    assert np.array_equal(record["field_mask"] ** 2, record["field_mask"])
    assert np.array_equal(record["qg_mask"] ** 2, record["qg_mask"])
    assert np.linalg.norm(record["p0"] @ record["q0"]) == 0
    assert all(x["conditional_field_rank"] > 0 and x["qg_support_rank"] > 0 for x in record["parents"])
    assert np.linalg.norm(record["kernel"] - np.swapaxes(record["kernel"].conj(), -1, -2)) < 1e-11


@lru_cache(maxsize=1)
def build_regulator() -> dict[str, Any]:
    c56 = contraction_preflight()
    assert c56["status"] == "C56_IFNORM_FINITE_HO_REGULATOR_INCOMPLETE"
    records = [_resolution_record(r) for r in RESOLUTIONS]
    for record in records:
        _assert_record(record)
    return {
        "baseline": BASELINE, "status": STATUS, "next": NEXT, "blocker": BLOCKER,
        "C56": {"status": c56["status"], "contraction_hash": c56["contraction_identity"]["hash"], "normal_ordering_vacuum": c56["normal_ordering_reference"]["vacuum_identity"], "IFNORM_plan": c56["regulator_plan"]["selected_plan"]},
        "source_hierarchy": source_hierarchy(), "operation_order": operation_order(), "plan": regulator_plan(),
        "records": records, "conversion": {"status": "CONVERSION_UNAVAILABLE", "TBP_regulator": "DLCQ longitudinal discretization plus invariant-mass/global or kinetic cutoff", "Li_2504": "finite periodic transverse momentum lattice Omega_perp, not HO", "C45": "finite 2D-HO shell basis", "overlap_shape": [0, 0], "rank": 0, "singular_values": [], "inverse": "ABSENT", "remainder": "VISIBLE_NOT_COMPUTABLE: source momentum cutoff parameters/cell quadrature are not an operator-identical finite C45-HO map"},
        "no_self_induced_inertia_sum": True, "no_contraction_matrices": True, "no_subtraction_or_counterterm": True, "no_direct_contact": True, "no_C53_values": True, "positive_gate": True,
    }


def runtime_arrays(record: dict[str, Any]) -> dict[str, np.ndarray]:
    return {
        "longitudinal_projector_diag": record["longitudinal_diag"], "transverse_envelope_projector_diag": record["transverse_diag"],
        "conditional_field_projector_diag": record["field_mask"], "corresponding_qg_projector_diag": record["qg_mask"],
        "commutator_kernel_samples": record["kernel"], "shell_labels": record["shell"], "P0": record["p0"], "Q0": record["q0"],
    }


def static_isolation_guard() -> dict[str, Any]:
    source = inspect.getsource(_conditional_support) + inspect.getsource(_physical_selection) + inspect.getsource(build_regulator)
    tree = ast.parse(source); names = {x.id for x in ast.walk(tree) if isinstance(x, ast.Name)} | {x.attr for x in ast.walk(tree) if isinstance(x, ast.Attribute)}
    forbidden = ("assemble_physical_vertex", "evaluate_canonical_vertex", "canonical_kernel", "C40", "ART25", "counterterm", "C53")
    found = tuple(x for x in forbidden if x in names)
    return {"guard": "C57_IFREG_SOURCE_SELECTION_ISOLATION", "forbidden": forbidden, "found": found, "pass": not found}


def serializable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return {"shape": list(value.shape), "dtype": value.dtype.str, "hash": array_hash(value)}
    if isinstance(value, tuple): return [serializable(v) for v in value]
    if isinstance(value, list): return [serializable(v) for v in value]
    if isinstance(value, dict): return {str(k): serializable(v) for k, v in value.items()}
    return value


def validate_c57(value: dict[str, Any]) -> bool:
    expected = serializable(build_regulator())
    return canonical_json(value) == canonical_json(expected) and value["status"] == STATUS


def snapshot() -> dict[str, Any]:
    return serializable(build_regulator())


def mutate_live_c57(fault_id: int) -> dict[str, Any]:
    value = deepcopy(snapshot()); choice = fault_id % 28
    if choice == 0: value["operation_order"]["selected"] = "NORMAL_ORDER_THEN_FOCK_PROJECT"
    elif choice == 1: value["plan"]["selected"] = "IFREG-UNIVERSAL-PROJECTED-HO-FIELD"
    elif choice == 2: value["records"][0]["longitudinal_diag"]["hash"] = "bad"
    elif choice == 3: value["records"][0]["transverse_diag"]["shape"][0] -= 1
    elif choice == 4: value["records"][0]["field_mask"]["hash"] = "nonidempotent"
    elif choice == 5: value["records"][0]["qg_mask"]["hash"] = "C53-values"
    elif choice == 6: value["records"][0]["parents"][0]["conditional_field_rank"] = 0
    elif choice == 7: value["records"][0]["zero_mode"] = "deleted"
    elif choice == 8: value["records"][0]["envelope_mode_count"] = 0
    elif choice == 9: value["records"][0]["shell_ranks"] = {}
    elif choice == 10: value["records"][0]["kernel"]["hash"] = "delta"
    elif choice == 11: value["conversion"]["status"] = "EXACT_FINITE_CONVERSION"
    elif choice == 12: value["conversion"]["rank"] = 1
    elif choice == 13: value["C56"]["IFNORM_plan"] = "IFNORM-BARE-RETAINED"
    elif choice == 14: value["C56"]["normal_ordering_vacuum"] = "hadron"
    elif choice == 15: value["source_hierarchy"]["rows"][2]["role"] = "BLFQ_ONE_PARTICLE_BASIS_AUTHORITY"
    elif choice == 16: value["source_hierarchy"]["rows"][3]["scope"] = "HO identical"
    elif choice == 17: value["records"][1]["mode_set_hash"] = "duplicate"
    elif choice == 18: value["records"][1]["field_mask_hash"] = "omitted"
    elif choice == 19: value["records"][1]["qg_mask_hash"] = "C53"
    elif choice == 20: value["records"][2]["conditional_type"] = "UNIVERSAL"
    elif choice == 21: value["no_self_induced_inertia_sum"] = False
    elif choice == 22: value["no_contraction_matrices"] = False
    elif choice == 23: value["no_subtraction_or_counterterm"] = False
    elif choice == 24: value["no_direct_contact"] = False
    elif choice == 25: value["no_C53_values"] = False
    elif choice == 26: value["positive_gate"] = False
    else: value["next"] = "C58/IFCONV"
    return value


def assert_ready_c57() -> dict[str, Any]:
    value = build_regulator()
    assert value["C56"]["IFNORM_plan"] == "IFNORM-UNAVAILABLE"
    assert value["plan"]["selected"] == PLAN and value["operation_order"]["selected"] == ORDER
    assert value["conversion"]["status"] == "CONVERSION_UNAVAILABLE"
    assert value["no_self_induced_inertia_sum"] and value["no_contraction_matrices"] and value["no_subtraction_or_counterterm"]
    assert all(np.all(r["field_mask"] ** 2 == r["field_mask"]) for r in value["records"])
    assert static_isolation_guard()["pass"]
    return value
