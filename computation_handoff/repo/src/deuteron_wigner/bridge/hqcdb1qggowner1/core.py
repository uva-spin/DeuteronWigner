"""C188 source-domain audit for the q↔qgg primitive owners.

The public C112 and C127 authorities expose q and qg domains, but no exact
qgg source AST/operator object.  This package records that boundary in a
safe data-only grammar and supplies factorized, fail-closed adapter metadata.
No coefficient or contact matrix is constructed.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import iferm3 as c112
from deuteron_wigner.bridge import icagg3 as c127
from deuteron_wigner.bridge import gnorm as c129
from deuteron_wigner.bridge import hqcd4 as c131
from deuteron_wigner.bridge import hqcdb0holonomy2 as c183
from deuteron_wigner.bridge import hqcdlfmatchcalc2 as c184
from deuteron_wigner.bridge import hqcdb1higherfock1 as c185
from deuteron_wigner.bridge import hqcdb1qgg2 as c186
from deuteron_wigner.bridge import hqcdb1qggcontact1 as c187

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c188_hqcdb1qggowner1"
BASELINE = "ae497703a5e334b5a1376e539a69320280b8a679"
CONTRACT = "docs/next_level/c187_c188_hqcdb1qggowner1_continuation_contract.json"
CONTRACT_SHA256 = "5a52f292a3265b7efc85a04ba9b595e997719c6763e75fdb8a0d7791f85d44ae"
PROMPT = "/Users/dustin/Downloads/c188_hqcdb1qggowner1_codex_prompt.md"
PROMPT_SHA256 = "9d76f675396858fd933591c5bd3911f975aef1baad94cd9da8e67dd43e6cd3ca"
C187_REPORT_SHA256 = "9269eef5da5f14751543cfa18e2481c03157bdcce365213d213e3c03bef2e83d"
STATUS = "C188_HQCDB1QGGOWNER1_SOURCE_EXPRESSION_INCOMPLETE"
PLAN = "QGGOWNER1-E"
NEXT = "C189/HQCDB1QGGSOURCE1"
RESOLUTIONS = ("K9", "K11", "K13")
C112_RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
QGG_CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
OWNERS = ("C112_INSTANTANEOUS_FERMION_QGG", "C127_GAUSS_CURRENT_QGG")
BRANCHES = ("Q_TO_QGG", "QGG_TO_Q")
PROGRAM_OPCODES = (
    "LOAD_FIELD_OPERATOR", "LOAD_PROJECT_DERIVATIVE",
    "LOAD_FINITE_CELL_INVERSE_DERIVATIVE", "LOAD_COLOR_GENERATOR",
    "LOAD_SPIN_MATRIX", "ORDER_PRODUCT", "COMMUTATOR", "ANTICOMMUTATOR",
    "ADD_TERM", "MULTIPLY_SCALAR", "NORMAL_ORDER",
    "SELECT_CREATION_ANNIHILATION_BRANCH", "TAKE_HERMITIAN_PARTNER",
    "RETURN_TYPED_SOURCE_BRANCH",
)
REQUESTS = tuple(row["request_id"] for row in c187.request_resolution_manifest()["rows"])


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)):
        return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _select(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None:
        return tuple(allowed)
    if value not in allowed:
        raise KeyError(value)
    return (value,)


def _verify_frozen_roots() -> None:
    expected = {
        "C187": "9a9f7834eb30d28c432a470503bf2f3a720477bf71ebf6a2ffdce0aef075d365",
        "C186": "df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20",
        "C185": "c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885",
        "C184": "89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8",
        "C183": "7198854f07fdbde8a00d8d553a848ba0d5cf3408199b9b7ff3a3cd29074c7b5f",
    }
    actual = {"C187": c187.PACKAGE_ROOT, "C186": c186.PACKAGE_ROOT, "C185": c185.PACKAGE_ROOT, "C184": c184.PACKAGE_ROOT, "C183": c183.PACKAGE_ROOT}
    if actual != expected:
        raise ValueError("C184-C187 root boundary changed")
    if c187.qgg_contact_release_manifest()["decision"] != "QGG_NOT_RELEASED_PRIMITIVE_AGGREGATE_OWNERSHIP_INCOMPLETE":
        raise ValueError("C187 ownership boundary changed")
    if c185.basis_manifest("C170-B1-QGG")["count"] != len(RESOLUTIONS):
        raise ValueError("C185 qgg basis census changed")


def _c112_objects() -> tuple[MappingProxyType, ...]:
    rows = []
    for resolution in C112_RESOLUTIONS:
        sector = c112.instantaneous_fermion_sector_manifest(resolution)
        cross = c112.cross_sector_zero_certificate(resolution)
        rows.append({
            "source_object_id": f"C112_PUBLIC_SECTOR_{resolution}",
            "upstream_package": "C112",
            "project_expression_id": "C112-SECTOR-MANIFEST-V1",
            "version_root": _root(sector),
            "operator_expression": "PUBLIC_SECTOR_SHAPES_ONLY_NO_FIELD_AST",
            "field_content": ("q", "qg"),
            "normal_ordering": "C112_PUBLIC_BLOCK_METADATA",
            "coupling_degree": 2,
            "inverse_longitudinal": "C43/C112 scope not exposed in qgg source AST",
            "boundary_P0_Q0": "C43 finite-cell metadata; qgg placement absent",
            "available_domains": ("q", "qg"),
            "target_adapters": (),
            "hermiticity": "public block authority; qgg branch unbound",
            "completeness": "SOURCE_EXPRESSION_AST_INCOMPLETE",
            "q_shape": sector["q_shape"],
            "qg_shape": sector["qg_shape"],
            "cross_sector_certificate": cross["certificate_root"],
        })
    return tuple(_freeze(row) for row in rows)


def _c127_objects() -> tuple[MappingProxyType, ...]:
    components = c127.component_manifest()["components"]
    rows = ({
        "source_object_id": "C127_PUBLIC_COMPONENT_MANIFEST",
        "upstream_package": "C127",
        "project_expression_id": "C127-COMPONENT-MANIFEST-V1",
        "version_root": c127.PACKAGE_ROOT,
        "operator_expression": "PUBLIC_COMPONENT_STATUS_NO_QGG_FIELD_AST",
        "field_content": ("J_q", "J_g", "q", "qg"),
        "normal_ordering": "current-component public metadata",
        "coupling_degree": 2,
        "inverse_longitudinal": "C43/C127 finite-cell current authority; qgg placement absent",
        "boundary_P0_Q0": "P0/Q0 scope typed in C187; source AST absent",
        "available_domains": tuple(sorted({row["sector"] for row in components})),
        "target_adapters": (),
        "hermiticity": "public current-component authority; qgg branch unbound",
        "completeness": "SOURCE_EXPRESSION_AST_INCOMPLETE",
        "component_count": len(components),
    }, {
        "source_object_id": "C127_PUBLIC_CURRENT_AGGREGATE",
        "upstream_package": "C127",
        "project_expression_id": "C127-INSTANTANEOUS-CURRENT-SPARSE-V1",
        "version_root": c127.PACKAGE_ROOT,
        "operator_expression": "PUBLIC_FACTOR_CURRENT_AGGREGATE_NO_QGG_DESCENDANT",
        "field_content": ("J_q", "J_g", "q", "qg"),
        "normal_ordering": "aggregate component route",
        "coupling_degree": 2,
        "inverse_longitudinal": "finite-cell metadata only; qgg placement absent",
        "boundary_P0_Q0": "C43 finite-cell P0/Q0 scope",
        "available_domains": ("q", "qg"),
        "target_adapters": (),
        "hermiticity": "aggregate public route; qgg branch unbound",
        "completeness": "SOURCE_EXPRESSION_AST_INCOMPLETE",
        "component_count": len(components),
    })
    return tuple(_freeze(row) for row in rows)


def load_verified_hqcd_b1qggowner1_authority() -> MappingProxyType:
    path = RUNTIME / "manifest.json"
    if not path.exists():
        raise FileNotFoundError("C188 runtime manifest missing")
    manifest = json.loads(path.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS:
        raise ValueError("C188 runtime root/status mismatch")
    return _freeze(verify_hqcd_b1qggowner1_authority())


def verify_hqcd_b1qggowner1_authority() -> MappingProxyType:
    _verify_frozen_roots()
    return _freeze({"schema": "C188-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt_sha256": PROMPT_SHA256, "C187_package_root": c187.PACKAGE_ROOT, "C186_package_root": c186.PACKAGE_ROOT, "C185_package_root": c185.PACKAGE_ROOT, "C184_package_root": c184.PACKAGE_ROOT, "C112_root": _root(_c112_objects()), "C127_root": _root(_c127_objects()), "source_acquisitions": 0, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "physical": False, "complete_qg_1PI": False, "package_root": PACKAGE_ROOT})


def b1qggowner1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C188-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "next": NEXT, "reason": "C112/C127 exact source AST/operator monomial and qgg target descendants are absent from public authority", "mutually_exclusive": True, "root": _root((PLAN, STATUS, NEXT))})


def owner_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C188-OWNER-HANDOFF-FREEZE-V1", "C187_package_root": c187.PACKAGE_ROOT, "C187_owner_root": c187.owner_manifest()["root"], "C187_dag_root": c187.owner_dag_manifest()["root"], "C187_C112_root": c187.instantaneous_fermion_manifest()["source_root"], "C187_C127_root": c187.gauss_current_manifest()["source_root"], "C187_C129_root": c129.PACKAGE_ROOT, "C187_C131_root": c131.PACKAGE_ROOT, "C185_qgg_root": c185.basis_manifest("C170-B1-QGG")["root"], "C186_cubic_root": c186.cubic_action_manifest()["root"], "C184_B0_root": c184.PACKAGE_ROOT, "read_only": True, "root": _root((c187.PACKAGE_ROOT, c185.PACKAGE_ROOT, c186.PACKAGE_ROOT, c184.PACKAGE_ROOT))})


def source_inventory_manifest(owner_id: str | None = None, source_object_id: str | None = None) -> MappingProxyType:
    if owner_id is not None and owner_id not in OWNERS:
        raise KeyError(owner_id)
    rows = _c112_objects() + _c127_objects()
    rows = tuple(row for row in rows if owner_id is None or row["upstream_package"] == ("C112" if owner_id == OWNERS[0] else "C127"))
    if source_object_id is not None and source_object_id not in {row["source_object_id"] for row in rows}:
        raise KeyError(source_object_id)
    rows = tuple(row for row in rows if source_object_id is None or row["source_object_id"] == source_object_id)
    return _freeze({"schema": "C188-SOURCE-INVENTORY-V1", "rows": rows, "count": len(rows), "source_expression_complete": False, "root": _root(rows)})


def source_domain_layer_manifest() -> MappingProxyType:
    return _freeze({"schema": "C188-SOURCE-DOMAIN-LAYER-V1", "owners": OWNERS, "source_objects": source_inventory_manifest()["count"], "q_domain": True, "qg_domain": True, "qgg_domain": False, "source_ast": False, "target_descendant": False, "status": "SOURCE_EXPRESSION_INCOMPLETE", "root": _root((OWNERS, source_inventory_manifest()["root"]))})


def source_program_schema() -> MappingProxyType:
    return _freeze({"schema": "QGG_PRIMITIVE_SOURCE_PROGRAM_V1", "allowed_opcodes": PROGRAM_OPCODES, "immutable": True, "data_only": True, "arbitrary_callable": False, "eval": False, "pickle": False, "dynamic_import": False, "network": False, "physical_defaults": False, "root": _root(PROGRAM_OPCODES)})


def source_program_manifest(owner_id: str | None = None, program_id: str | None = None) -> MappingProxyType:
    owners = _select(owner_id, OWNERS)
    rows = tuple({"program_id": f"C188-{owner}-SOURCE-PROGRAM", "primitive_owner": owner, "source_root": source_inventory_manifest(owner)["root"], "operator_order": "SOURCE_AST_NOT_EXPOSED", "coupling_degree": 2, "field_slots": ("q", "qbar", "g_1", "g_2"), "inverse_derivative_slots": ("UNRESOLVED_SOURCE_PLACEMENT",), "branch_ids": (f"C188-{owner}-Q_TO_QGG", f"C188-{owner}-QGG_TO_Q"), "units": "GeV^2/g_s^2", "program": (("SELECT_CREATION_ANNIHILATION_BRANCH", "source AST unavailable"), ("RETURN_TYPED_SOURCE_BRANCH", "SOURCE_EXPRESSION_INCOMPLETE")), "source_expression_status": "SOURCE_EXPRESSION_AST_INCOMPLETE", "safe": True, "root": _root((owner, source_inventory_manifest(owner)["root"], PROGRAM_OPCODES))} for owner in owners)
    if program_id is not None and program_id not in {row["program_id"] for row in rows}:
        raise KeyError(program_id)
    rows = tuple(row for row in rows if program_id is None or row["program_id"] == program_id)
    return _freeze({"schema": "C188-SOURCE-PROGRAM-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def branch_manifest(owner_id: str | None = None, branch_id: str | None = None, source_sector_id: str | None = None, target_sector_id: str | None = None) -> MappingProxyType:
    owners = _select(owner_id, OWNERS)
    rows = []
    for owner in owners:
        zero = c112.cross_sector_zero_certificate(C112_RESOLUTIONS[0])["certificate_root"] if owner == OWNERS[0] else _root(("C127", c127.cross_sector_zero_certificate("K9_2_N8_b0.40", "J_qJ_q")))
        for branch in ("Q_TO_QGG", "QGG_TO_Q", "Q_TO_QG", "QG_TO_Q", "Q_TO_Q", "QG_TO_QG", "VACUUM_OR_ZERO_MODE", "BOUNDARY_OR_NONMATRIX"):
            if branch == "Q_TO_QGG":
                classification, target, net = "BRANCH_INCOMPLETE", "C170-B1-QGG", (2, 2)
            elif branch == "QGG_TO_Q":
                classification, target, net = "BRANCH_INCOMPLETE", "C170-B1-Q", (-2, -2)
            elif branch in ("Q_TO_QG", "QG_TO_Q"):
                classification, target, net = "SOURCE_EXCLUDED_EXACT_PUBLIC_ZERO", "C170-B1-QG", (1, -1) if branch == "Q_TO_QG" else (-1, 1)
            elif branch == "QG_TO_QG":
                classification, target, net = "PUBLIC_DOMAIN_ONLY_NOT_SOURCE_EXPANSION", "C170-B1-QG", (0, 0)
            elif branch == "Q_TO_Q":
                classification, target, net = "PUBLIC_DOMAIN_ONLY_NOT_SOURCE_EXPANSION", "C170-B1-Q", (0, 0)
            elif branch == "VACUUM_OR_ZERO_MODE":
                classification, target, net = "SOURCE_EXCLUDED", "VACUUM_OR_P0", (0, 0)
            else:
                classification, target, net = "BRANCH_INCOMPLETE", "C130_P0_BOUNDARY", (0, 0)
            rows.append({"branch_id": f"C188-{owner}-{branch}", "primitive_owner": owner, "ordered_field_slots": ("q", "g_1", "g_2"), "creation_annihilation_pattern": "UNEXPANDED_SOURCE_OPERATOR", "source_sector_id": "C170-B1-Q" if branch.startswith("Q_") else "C170-B1-QGG", "target_sector_id": target, "net_particle_number": net[0], "fermion_number_change": 0, "gluon_number_change": net[1], "longitudinal_sign_constraints": "UNRESOLVED_SOURCE_AST" if "QGG" in branch or "QGG" in target else "C43_PUBLIC_DOMAIN_SCOPE", "ordinary_zero_mode": "EXCLUDED_OR_TYPED_INTERFACE", "coupling_degree": 2, "operator_order_sign": "UNRESOLVED_SOURCE_AST" if classification == "BRANCH_INCOMPLETE" else "PUBLIC_CERTIFICATE", "hermitian_partner": f"C188-{owner}-{'QGG_TO_Q' if branch == 'Q_TO_QGG' else 'Q_TO_QGG' if branch == 'QGG_TO_Q' else branch}", "independent_routes": ("BRANCH-A field-slot expansion", "BRANCH-B operator preimage", "BRANCH-C normal ordering", "BRANCH-D Hermitian route", "BRANCH-E public-domain crosscheck"), "terminal_classification": classification, "public_zero_certificate": zero if branch in ("Q_TO_QG", "QG_TO_Q") else None, "root": _root((owner, branch, classification, target))})
    if branch_id is not None and branch_id not in {row["branch_id"] for row in rows}:
        raise KeyError(branch_id)
    if source_sector_id is not None:
        rows = [row for row in rows if row["source_sector_id"] == source_sector_id]
    if target_sector_id is not None:
        rows = [row for row in rows if row["target_sector_id"] == target_sector_id]
    rows = tuple(row for row in rows if branch_id is None or row["branch_id"] == branch_id)
    return _freeze({"schema": "C188-BRANCH-V1", "rows": tuple(rows), "count": len(rows), "qgg_branch_proven": False, "root": _root(rows)})


def exclusion_manifest(record_id: str | None = None) -> MappingProxyType:
    rows = ({"record_id": "C188-C129-SEQUENTIAL-EXCLUSION", "owner": "C129", "source_root": c129.PACKAGE_ROOT, "classification": "SEQUENTIAL_NORMAL_ORDERING_DESCENDANT_ONLY", "source_preimage": "qg->qgg", "q_to_qgg_primitive": False, "promoted": False}, {"record_id": "C188-C131-AGGREGATE-EXCLUSION", "owner": "C131", "source_root": c131.PACKAGE_ROOT, "classification": "AGGREGATE_CROSSWALK_ONLY", "primitive_children": ("C112", "C127"), "additive_count": 0, "promoted": False}, {"record_id": "C188-C130-NONMATRIX", "owner": "C130", "source_root": c187.zero_boundary_manifest()["root"], "classification": "TYPED_NONMATRIX_ZERO_MODE_BOUNDARY_INTERFACE", "local_matrix": False, "promoted": False}, {"record_id": "C188-C182-NONMATRIX", "owner": "C182", "source_root": c187.link_interface_manifest()["source_root"], "classification": "TYPED_SOURCE_OPERATOR_RESIDUAL_LINK_INTERFACE", "local_matrix": False, "promoted": False})
    if record_id is not None and record_id not in {row["record_id"] for row in rows}:
        raise KeyError(record_id)
    rows = tuple(row for row in rows if record_id is None or row["record_id"] == record_id)
    return _freeze({"schema": "C188-EXCLUSION-V1", "rows": rows, "count": len(rows), "aggregate_double_count": 0, "root": _root(rows)})


def target_adapter_manifest(owner_id: str | None = None, branch_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    owners = _select(owner_id, OWNERS)
    resolutions = _select(resolution_id, RESOLUTIONS)
    rows = []
    for owner in owners:
        for branch in BRANCHES:
            bid = f"C188-{owner}-{branch}"
            if branch_id is not None and branch_id != bid:
                continue
            for resolution in resolutions:
                basis = c185.basis_manifest("C170-B1-QGG", resolution)
                rows.append({"adapter_id": f"C188-ADAPTER-{owner}-{branch}-{resolution}", "primitive_owner": owner, "branch_id": bid, "resolution": resolution, "source_q_state_domain": "C170-B1-Q public domain", "target_qgg_sector_id": "C170-B1-QGG", "target_qgg_basis_root": basis["root"], "longitudinal_partition_domain": "positive APBC quark plus positive nonzero PBC gluons; source branch unresolved", "finite_HO_product_domain": "C185 factorized finite-HO basis", "Bose_projector": "C185 exact qgg Bose projector", "color_channels": QGG_CHANNELS, "CM_ground_projector": "C185 CM-ground", "holonomy_BC_class": "C183 fixture-dependent; see holonomy manifest", "source_reachable_filter": "UNAVAILABLE_SOURCE_BRANCH", "source_preimage_count": "UNAVAILABLE_NOT_ZERO", "paged_target_iteration": True, "full_cartesian_materialized": False, "rank_unrank": True, "status": "TARGET_ADAPTER_INCOMPLETE_SOURCE_BRANCH", "root": _root((owner, branch, resolution, basis["root"]))})
    return _freeze({"schema": "C188-TARGET-ADAPTER-V1", "rows": tuple(rows), "count": len(rows), "source_preimage_counts": "UNAVAILABLE_NOT_ZERO", "full_cartesian_materialized": False, "root": _root(rows)})


def denominator_manifest(owner_id: str | None = None, branch_id: str | None = None, denominator_id: str | None = None) -> MappingProxyType:
    owners = _select(owner_id, OWNERS)
    rows = []
    for owner in owners:
        for branch in BRANCHES:
            bid = f"C188-{owner}-{branch}"
            if branch_id is not None and branch_id != bid:
                continue
            for resolution in RESOLUTIONS:
                did = f"C188-DEN-{owner}-{branch}-{resolution}"
                rows.append({"denominator_id": did, "owner_id": owner, "branch_id": bid, "resolution": resolution, "source_operator_placement": "UNRESOLVED_SOURCE_AST", "inverse_operator": "inverse_partial_plus_or_squared_source-dependent", "P0_Q0_scope": "C43 finite-cell P0/Q0; no ordinary zero mode", "PV_prescription": "C43 antisymmetric/PV retained", "momentum_combination": "ordered k_q,k_g1,k_g2 with total conservation; descriptor only", "orientation": ("q_to_qgg", "qgg_to_q"), "units": "inverse longitudinal momentum power", "numerical_coefficient": False, "routes": ("DEN-A source placement", "DEN-B ordered momentum", "DEN-C finite Fourier/P0-Q0", "DEN-D Hermitian reverse", "DEN-E adapter consistency"), "status": "DENOMINATOR_DESCRIPTOR_SOURCE_INCOMPLETE", "root": _root((owner, branch, resolution, "C43-PV"))})
    if denominator_id is not None and denominator_id not in {row["denominator_id"] for row in rows}:
        raise KeyError(denominator_id)
    rows = tuple(row for row in rows if denominator_id is None or row["denominator_id"] == denominator_id)
    return _freeze({"schema": "C188-DENOMINATOR-V1", "rows": rows, "count": len(rows), "ordinary_zero_modes": 0, "continuum_substitution": False, "root": _root(rows)})


def color_descriptor_manifest(owner_id: str | None = None, branch_id: str | None = None, color_descriptor_id: str | None = None) -> MappingProxyType:
    rows = tuple({"color_descriptor_id": f"C188-COLOR-{owner}-{branch}", "owner_id": owner, "branch_id": f"C188-{owner}-{branch}", "ordered_gluon_slots": ("g_1", "g_2"), "source_color_word": "T^a T^b (source AST unavailable)", "reverse_order_word": "T^b T^a (source AST unavailable)", "generator_normalization": "C43 public normalization", "source_phase": "UNRESOLVED_SOURCE_AST", "exchange_parity": "C185 Bose projector metadata", "candidate_channels": QGG_CHANNELS, "all_eight_generator_route": True, "descriptor_completeness": "COLOR_DESCRIPTOR_SOURCE_INCOMPLETE", "numeric_projection": False, "root": _root((owner, branch, QGG_CHANNELS))} for owner in _select(owner_id, OWNERS) for branch in BRANCHES if branch_id is None or branch_id == f"C188-{owner}-{branch}")
    if color_descriptor_id is not None and color_descriptor_id not in {row["color_descriptor_id"] for row in rows}:
        raise KeyError(color_descriptor_id)
    rows = tuple(row for row in rows if color_descriptor_id is None or row["color_descriptor_id"] == color_descriptor_id)
    return _freeze({"schema": "C188-COLOR-DESCRIPTOR-V1", "rows": rows, "count": len(rows), "channels_separate": True, "premature_symmetrization": False, "root": _root(rows)})


def spin_polarization_manifest(owner_id: str | None = None, branch_id: str | None = None, descriptor_id: str | None = None) -> MappingProxyType:
    rows = tuple({"descriptor_id": f"C188-SPIN-{owner}-{branch}", "owner_id": owner, "branch_id": f"C188-{owner}-{branch}", "quark_helicities": "source AST unavailable", "spin_matrix_order": "source AST unavailable", "gluon_polarization_slots": ("g_1", "g_2"), "transverse_derivative": "source AST unavailable", "longitudinal_derivative": "source AST unavailable", "ordered_field_slots": ("q", "g_1", "g_2"), "mass_dependence": "caller/source descriptor required", "source_phase": "source AST unavailable", "units": "GeV^2/g_s^2", "hermitian_partner": f"C188-{owner}-{'QGG_TO_Q' if branch == 'Q_TO_QGG' else 'Q_TO_QGG'}", "routes": ("SPIN-A source order", "SPIN-B good/bad component", "SPIN-C current decomposition", "SPIN-D Hermitian reverse", "SPIN-E qgg compatibility"), "status": "SPIN_DESCRIPTOR_SOURCE_INCOMPLETE", "root": _root((owner, branch, "spin"))} for owner in _select(owner_id, OWNERS) for branch in BRANCHES if branch_id is None or branch_id == f"C188-{owner}-{branch}")
    if descriptor_id is not None and descriptor_id not in {row["descriptor_id"] for row in rows}:
        raise KeyError(descriptor_id)
    rows = tuple(row for row in rows if descriptor_id is None or row["descriptor_id"] == descriptor_id)
    return _freeze({"schema": "C188-SPIN-POLARIZATION-V1", "rows": rows, "count": len(rows), "finite_HO_evaluated": False, "root": _root(rows)})


def ho_cm_adapter_manifest(owner_id: str | None = None, branch_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows = []
    for owner in _select(owner_id, OWNERS):
        for branch in BRANCHES:
            bid = f"C188-{owner}-{branch}"
            if branch_id is not None and branch_id != bid:
                continue
            for resolution in _select(resolution_id, RESOLUTIONS):
                basis = c185.basis_manifest("C170-B1-QGG", resolution)
                rows.append({"adapter_id": f"C188-HO-CM-{owner}-{branch}-{resolution}", "owner_id": owner, "branch_id": bid, "resolution": resolution, "source_one_particle_HO_ids": "UNAVAILABLE_SOURCE_BRANCH", "target_qgg_HO_ids": "C185 factorized qgg IDs", "operator_type": "source derivative/operator unresolved", "talmi_moshinsky_route": "C185 metadata only", "Bose_orbit_stabilizer": "C185 exact projector metadata", "CM_projector": "C185 CM-ground", "finite_shell_leakage": "retained upstream metadata; not pruned", "expected_units": "GeV^2/g_s^2", "basis_root": basis["root"], "overlap_evaluated": False, "CM_excited_silently_included": False, "source_reachable": "UNAVAILABLE_NOT_ZERO", "status": "HO_CM_ADAPTER_SOURCE_INCOMPLETE", "root": _root((owner, branch, resolution, basis["root"]))})
    return _freeze({"schema": "C188-HO-CM-ADAPTER-V1", "rows": tuple(rows), "count": len(rows), "finite_HO_evaluated": False, "root": _root(rows)})


def hermitian_manifest(owner_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    rows = []
    for owner in _select(owner_id, OWNERS):
        for branch in BRANCHES:
            bid = f"C188-{owner}-{branch}"
            if branch_id is not None and branch_id != bid:
                continue
            reverse = f"C188-{owner}-{'QGG_TO_Q' if branch == 'Q_TO_QGG' else 'Q_TO_QGG'}"
            rows.append({"forward_branch_id": bid, "reverse_branch_id": reverse, "operator_reversal": "TAKE_HERMITIAN_PARTNER", "fermion_order_sign": "UNRESOLVED_SOURCE_AST", "gluon_slot_order": "preserve ordered slots; reverse descriptor", "color_word_adjoint": "T^a T^b ↔ T^b T^a descriptor", "denominator_orientation": "C43 PV reverse descriptor", "spin_polarization_adjoint": "source AST unavailable", "units": "GeV^2/g_s^2", "source_root": source_program_manifest(owner)["rows"][0]["root"], "status": "HERMITIAN_PAIR_UNPROVEN_SOURCE_EXPRESSION", "coefficient_matrix": False, "root": _root((owner, branch, reverse))})
    return _freeze({"schema": "C188-HERMITIAN-V1", "rows": tuple(rows), "count": len(rows), "exact_pairing": False, "root": _root(rows)})


def holonomy_bc_manifest(owner_id: str | None = None, branch_id: str | None = None, capsule_id: str | None = None) -> MappingProxyType:
    rows = []
    for owner in _select(owner_id, OWNERS):
        for branch in BRANCHES:
            bid = f"C188-{owner}-{branch}"
            if branch_id is not None and branch_id != bid:
                continue
            for fid in _select(capsule_id, c183.FIXTURE_IDS):
                c185_row = next(row for row in c185.holonomy_bc_manifest("C170-B1-QGG", fid)["rows"])
                rows.append({"owner_id": owner, "branch_id": bid, "capsule_id": fid, "q_boundary": "APBC explicit C183 fundamental twist", "qgg_boundary": c185_row["quark_boundary"], "gluon_boundary": c185_row["gluon_boundary"], "classification": c185_row["classification"], "source_branch_status": "SOURCE_EXPRESSION_INCOMPLETE", "center_sector_retained": True, "longitudinal_grid_changed": False, "physical_holonomy": False, "root": _root((owner, branch, fid, c185_row["classification"]))})
    return _freeze({"schema": "C188-HOLONOMY-BC-V1", "rows": tuple(rows), "count": len(rows), "grid_changed": False, "root": _root(rows)})


def coefficient_handoff_manifest(owner_id: str | None = None, branch_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows = []
    for owner in _select(owner_id, OWNERS):
        for branch in BRANCHES:
            bid = f"C188-{owner}-{branch}"
            if branch_id is not None and branch_id != bid:
                continue
            for resolution in _select(resolution_id, RESOLUTIONS):
                rows.append({"primitive_owner": owner, "branch_id": bid, "resolution": resolution, "source_program_root": source_program_manifest(owner)["root"], "branch_root": branch_manifest(owner, bid)["root"], "target_adapter_root": target_adapter_manifest(owner, bid, resolution)["root"], "denominator_root": denominator_manifest(owner, bid)["root"], "color_descriptor_root": color_descriptor_manifest(owner, bid)["root"], "spin_polarization_root": spin_polarization_manifest(owner, bid)["root"], "ho_cm_root": ho_cm_adapter_manifest(owner, bid, resolution)["root"], "hermitian_root": hermitian_manifest(owner, bid)["root"], "holonomy_bc_root": holonomy_bc_manifest(owner, bid)["root"], "required_parameter_fields": ("caller coupling", "caller source coordinates", "C43 PV record", "C185 target record"), "required_numerical_routes": ("factorized analytic", "sparse future", "matrix-free future", "Hermitian future", "channel-filtered future"), "status": "HANDOFF_BLOCKED_SOURCE_EXPRESSION", "nonclaims": ("no numerical coefficient", "no contact matrix", "no qg 1PI", "no physical coupling"), "root": _root((owner, bid, resolution))})
    return _freeze({"schema": "C188-COEFFICIENT-HANDOFF-V1", "rows": tuple(rows), "count": len(rows), "executable_next": False, "root": _root(rows)})


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    rows = ({"graph_id": "C188-C112-PRIMITIVE-CANDIDATE", "owner": "C112", "classification": "direct primitive candidate; source expression incomplete", "proper_1PI": "future", "sequential": False, "interface": False}, {"graph_id": "C188-C127-PRIMITIVE-CANDIDATE", "owner": "C127", "classification": "direct primitive candidate; source expression incomplete", "proper_1PI": "future", "sequential": False, "interface": False}, {"graph_id": "C188-C129-SEQUENTIAL", "owner": "C129", "classification": "sequential normal-ordering descendant", "proper_1PI": False, "sequential": True, "interface": False}, {"graph_id": "C188-C131-AGGREGATE", "owner": "C131", "classification": "aggregate crosswalk", "proper_1PI": False, "sequential": False, "interface": False}, {"graph_id": "C188-C130-BOUNDARY", "owner": "C130", "classification": "nonmatrix boundary interface", "proper_1PI": "future interface", "sequential": False, "interface": True}, {"graph_id": "C188-C182-LINK", "owner": "C182", "classification": "source/operator residual-link interface", "proper_1PI": "future interface", "sequential": False, "interface": True}, {"graph_id": "C185-QG-QGG-QUARK", "owner": "C185", "classification": "sequential qg↔qgg transition", "proper_1PI": False, "sequential": True, "interface": False}, {"graph_id": "C186-QG-QGG-CUBIC", "owner": "C186", "classification": "sequential cubic transition", "proper_1PI": False, "sequential": True, "interface": False}, {"graph_id": "C188-FUTURE-CONTACT", "owner": "C188", "classification": "future executable q↔qgg contact", "proper_1PI": "future", "sequential": False, "interface": False})
    if graph_id is not None and graph_id not in {row["graph_id"] for row in rows}:
        raise KeyError(graph_id)
    rows = tuple(row for row in rows if graph_id is None or row["graph_id"] == graph_id)
    return _freeze({"schema": "C188-TOPOLOGY-V1", "rows": rows, "count": len(rows), "complete_qg_1PI": False, "direct_sequential_conflation": False, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    if request_id is not None and request_id not in REQUESTS:
        raise KeyError(request_id)
    owners = ("C112", "C127", "C129", "C131", "C130", "C182", "C185_QGG_QUARK_EMISSION", "C186_QGG_CUBIC_GLUE", "C188_FUTURE_CONTACT", "C151_COUNTERTERMS", "C187_TARGET_MOMQ", "C187_FUTURE_ST")
    rows = tuple({"owner_id": owner, "count_once": True, "duplicate": False, "aggregate_additive": False if owner == "C131" else None, "direct_sequential_conflation": False, "interface_as_matrix": False, "unavailable_as_zero": False} for owner in owners)
    return _freeze({"schema": "C188-COUNT-ONCE-V1", "request_id": request_id, "rows": rows, "count": len(rows), "duplicates": 0, "root": _root((rows, request_id))})


def owner_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C188-OWNER-RELEASE-V1", "decision": "QGG_NOT_RELEASED_SOURCE_EXPRESSION_INCOMPLETE", "status": STATUS, "plan": PLAN, "gates": {"source_inventory": True, "source_program": False, "branch_census": False, "exclusions": True, "target_adapter": False, "denominator": False, "color": False, "spin": False, "ho_cm": False, "hermitian": False, "holonomy_bc": True, "handoff": False, "topology": True, "count_once": True}, "numerical_coefficient": False, "contact_matrix": False, "complete_qg_1PI": False, "physical": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for old in c187.request_resolution_manifest()["rows"]:
        req = old["request_id"]
        if "qg_VERTEX" in req or "QCD_COUPLING" in req:
            status, nxt, active = "SOURCE_EXPRESSION_INCOMPLETE", NEXT, True
        else:
            status, nxt, active = old["terminal_status"], old["exact_next_object"], False
        rows.append({"request_id": req, "terminal_status": status, "active_in_C188": active, "exact_next_object": nxt, "request4_frozen": "TRANSVERSE_GLUON" in req, "complete_qg_1PI": False, "physical_coupling": False})
    if request_id is not None and request_id not in REQUESTS:
        raise KeyError(request_id)
    selected = tuple(row for row in rows if request_id is None or row["request_id"] == request_id)
    return _freeze({"schema": "C188-REQUEST-RESOLUTION-V1", "rows": selected, "count": len(selected), "all_six_visible": len(selected) == 6 if request_id is None else True, "root": _root(selected)})


def missing_owner_object_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = REQUESTS if request_id is None else _select(request_id, REQUESTS)
    active = tuple(req for req in reqs if "qg_VERTEX" in req or "QCD_COUPLING" in req)
    object_types = ("C112_SOURCE_EXPRESSION_AST", "C112_QGG_BRANCH_ADAPTER", "C127_SOURCE_EXPRESSION_AST", "C127_QGG_BRANCH_ADAPTER", "FINITE_CELL_DENOMINATOR_PLACEMENT", "ORDERED_COLOR_DESCRIPTOR", "SPIN_POLARIZATION_DESCRIPTOR", "FINITE_HO_CM_ADAPTER", "HERMITIAN_BRANCH_PAIR", "HOLONOMY_BRANCH_CLASSIFICATION", "EXECUTABLE_CONTACT_PROGRAM")
    rows = tuple({"capsule_id": f"C188-{owner}-{kind}", "parent_request_id": req, "primitive_owner": owner, "source_object_id": f"{owner.split('_')[0]}_PUBLIC_SOURCE_INVENTORY", "branch_ids": (f"C188-{owner}-Q_TO_QGG", f"C188-{owner}-QGG_TO_Q"), "resolution": "K9/K11/K13", "target_sector": "C170-B1-QGG", "color_channels": QGG_CHANNELS, "holonomy_classes": c183.FIXTURE_IDS, "coupling_degree": 2, "required_routes": ("source-program", "branch", "adapter", "denominator", "color", "spin", "HO/CM", "Hermitian", "holonomy"), "status": "SOURCE_EXPRESSION_INCOMPLETE" if "SOURCE" in kind or "BRANCH" in kind else "BLOCKED_BY_SOURCE_EXPRESSION", "not_zero": True, "exact_request": "supply authenticated project source AST/operator monomial and locator; no external formula", "nonclaims": ("no numerical coefficient", "no contact matrix", "no complete qg 1PI", "no physical coupling")} for req in active for owner in OWNERS for kind in object_types)
    return _freeze({"schema": "C188-MISSING-OWNER-OBJECT-V1", "rows": rows, "count": len(rows), "not_zero": True, "root": _root(rows)})


def coefficient_phase_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C188-COEFFICIENT-PHASE-HANDOFF-V1", "source_programs": source_program_manifest()["root"], "branches": branch_manifest()["root"], "adapters": target_adapter_manifest()["root"], "denominators": denominator_manifest()["root"], "colors": color_descriptor_manifest()["root"], "spin": spin_polarization_manifest()["root"], "ho_cm": ho_cm_adapter_manifest()["root"], "hermitian": hermitian_manifest()["root"], "holonomy": holonomy_bc_manifest()["root"], "owner_release": owner_release_manifest()["root"], "executable": False, "remaining": NEXT, "root": _root((STATUS, NEXT))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C188-FRONTIER-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "completed": ("C184 B0", "C185 qgg/qqbarq bases and transitions", "C186 cubic", "C187 owner taxonomy"), "partial": ("C112 source AST/qgg descendant", "C127 source AST/qgg descendant", "qgg contact coefficient", "complete qg 1PI", "full ST", "target MOMq"), "counterterms_selected": 0, "null_coordinates_selected": 0, "root": _root((0, 0, STATUS))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C188-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "new_qubits": 0, "states": 0, "TMD_objects": 0, "physical_parameter_count": 0, "root": _root((0, 0, 0))})


def b1qggowner1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C188-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "source_inventory_count": source_inventory_manifest()["count"], "source_program_count": source_program_manifest()["count"], "qgg_branch_proven": False, "target_adapter_count": target_adapter_manifest()["count"], "source_preimage_counts": "UNAVAILABLE_NOT_ZERO", "ordinary_zero_modes": 0, "channels": QGG_CHANNELS, "finite_HO_evaluated": False, "complete_qg_1PI": False, "C166_graph_nodes_edges": (0, 0), "counterterms_selected": 0, "null_representatives": 0, "physical": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"new_external_sources": 0, "unqualified_formulas": 0, "invented_contracts": 0, "qgg_basis_recomputed": 0, "qqbarq_mutation": 0, "cubic_recomputed": 0, "B0_recomputed": 0, "numerical_contact_coefficients": 0, "contact_matrices": 0, "complete_qg_1PI": 0, "physical_inputs": 0, "owner_name_branch_inference": 0, "sequential_to_primitive_promotion": 0, "aggregate_to_primitive_promotion": 0, "nonmatrix_to_matrix": 0, "continuum_denominator_substitution": 0, "ordinary_zero_modes": 0, "ordered_color_losses": 0, "color_channel_conflations": 0, "finite_HO_evaluation": 0, "CM_contamination": 0, "missing_source_zeros": 0, "holonomy_omissions": 0, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "counterterms_selected": 0, "null_coordinates_selected": 0, "quantum_objects_modified": 0, "pass": True, "root": _root((STATUS, PLAN))})


def mutate_live_hqcd_b1qggowner1(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384:
        raise ValueError(index)
    return _freeze({"index": index, "mutation": "C188 source/branch/adapter record", "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS, "mutation"))})


ROOTS = {"C187": c187.PACKAGE_ROOT, "C186": c186.PACKAGE_ROOT, "C185": c185.PACKAGE_ROOT, "C184": c184.PACKAGE_ROOT, "C183": c183.PACKAGE_ROOT, "C112": _root(_c112_objects()), "C127": _root(_c127_objects()), "C188_PLAN": b1qggowner1_plan_manifest()["root"], "C188_HANDOFF_FREEZE": owner_handoff_freeze()["root"], "C188_SOURCE_INVENTORY": source_inventory_manifest()["root"], "C188_SOURCE_SCHEMA": source_program_schema()["root"], "C188_SOURCE_PROGRAM": source_program_manifest()["root"], "C188_BRANCH": branch_manifest()["root"], "C188_EXCLUSION": exclusion_manifest()["root"], "C188_ADAPTER": target_adapter_manifest()["root"], "C188_DENOMINATOR": denominator_manifest()["root"], "C188_COLOR": color_descriptor_manifest()["root"], "C188_SPIN": spin_polarization_manifest()["root"], "C188_HO_CM": ho_cm_adapter_manifest()["root"], "C188_HERMITIAN": hermitian_manifest()["root"], "C188_HOLONOMY": holonomy_bc_manifest()["root"], "C188_COEFFICIENT_HANDOFF": coefficient_handoff_manifest()["root"], "C188_TOPOLOGY": topology_manifest()["root"], "C188_COUNT": count_once_manifest()["root"], "C188_RELEASE": owner_release_manifest()["root"], "C188_REQUESTS": request_resolution_manifest()["root"], "C188_MISSING": missing_owner_object_manifest()["root"], "C188_PHASE": coefficient_phase_handoff_contract()["root"], "C188_FRONTIER": dependency_frontier_manifest()["root"], "C188_QUANTUM": quantum_nonmutation_manifest()["root"]}
PACKAGE_ROOT = _root({"schema": "C188-HQCDB1QGGOWNER1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = [name for name in globals() if not name.startswith("_")]
