"""C194 owner-separated conditional qg proper-vertex assembly.

The qgg component is an immutable symbolic composition of C185/C186
transitions with the three C193 contact owners.  The exact C185 qqbarq
order-two source remains a typed blocker and is never inferred from qgg.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdb1qggcontact2 as c193
from deuteron_wigner.bridge import hqcdb1higherfock1 as c185
from deuteron_wigner.bridge import hqcdb1qgg2 as c186
from deuteron_wigner.bridge import hqcdqgvert as c152
from deuteron_wigner.bridge import hqcdg2pt as c151
from deuteron_wigner.bridge import hqcd2ptq2 as c145
from deuteron_wigner.bridge import hqcd2ptfull as c148
from deuteron_wigner.bridge import hqcdzqmass as c150
from deuteron_wigner.bridge import hqcdlfmatchcalc2 as c184
from deuteron_wigner.bridge import hqcdb0holonomy2 as c183

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c194_hqcdqgvert2"
BASELINE = "385a7ed42be68a918f02dc90e6cc4a1d5257193c"
PROMPT = "/Users/dustin/Downloads/c194_hqcdqgvert2_codex_prompt.md"
PROMPT_SHA256 = "b0de268e40912b14ce4291eca57578655070e992475b3889d1c113a39a81b6f8"
STATUS = "C194_HQCDQGVERT2_QQBARQ_COMPONENT_INCOMPLETE"
PLAN = "QGVERT2-B"
NEXT = "C195/HQCDB1QQBARQVERT1"
RESOLUTIONS = ("K9", "K11", "K13")
ORIENTATIONS = ("Q_TO_QG", "QG_TO_Q")
QGG_TRANSITIONS = ("C185-QG-QGG-QUARK-EMISSION", "C186-QG-QGG-CUBIC-GLUON")
CONTACT_OWNERS = ("C112", "C127-JQ-K-JG", "C127-JG-K-JQ")
QGG_CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
QQBARQ_CHANNELS = ("QQBARQ_COLOR_QQ_BAR3", "QQBARQ_COLOR_QQ_6")
FLAVOR_CLASSES = ("same_flavor", "different_flavor", "symbolic_active_flavor")
EXTERNAL_RECORDS = tuple(f"C194-EXT-{r}-Q_TO_QG" for r in RESOLUTIONS)
FIXTURES = tuple(f"C194-FIXTURE-{r}" for r in RESOLUTIONS)
COUNTERTERMS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULLS = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
PROJECTORS = tuple(f"C152-RANK8-PROJECTOR-{i}" for i in range(1, 9))
UPSTREAM = {
    "C193": c193.PACKAGE_ROOT, "C185": c185.PACKAGE_ROOT, "C186": c186.PACKAGE_ROOT,
    "C152": c152.PACKAGE_ROOT, "C151": c151.PACKAGE_ROOT, "C145": c145.PACKAGE_ROOT, "C148": c148.PACKAGE_ROOT, "C150": c150.PACKAGE_ROOT, "C184": c184.PACKAGE_ROOT,
    "C183": c183.PACKAGE_ROOT, "C158": "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367",
    "C153": "7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464",
}


def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _pick(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is None: return allowed
    if value not in allowed: raise KeyError(value)
    return (value,)


def _check_upstream() -> None:
    if c193.PACKAGE_ROOT != UPSTREAM["C193"]: raise ValueError("C193 root changed")
    if c185.PACKAGE_ROOT != UPSTREAM["C185"]: raise ValueError("C185 root changed")
    if c186.PACKAGE_ROOT != UPSTREAM["C186"]: raise ValueError("C186 root changed")
    if c152.PACKAGE_ROOT != UPSTREAM["C152"]: raise ValueError("C152 root changed")
    if c145.PACKAGE_ROOT != UPSTREAM["C145"]: raise ValueError("C145 root changed")
    if c148.PACKAGE_ROOT != UPSTREAM["C148"]: raise ValueError("C148 root changed")
    if c150.PACKAGE_ROOT != UPSTREAM["C150"]: raise ValueError("C150 root changed")
    if c184.PACKAGE_ROOT != UPSTREAM["C184"]: raise ValueError("C184 root changed")
    c193.load_verified_hqcd_b1qggcontact2_authority()
    c185.load_verified_hqcd_b1higherfock1_authority()
    c186.load_verified_hqcd_b1qgg2_authority()
    c152.load_verified_hqcd_qg_vertex_authority()
    c145.load_verified_hqcd_forward_two_point_authority()
    c148.load_verified_hqcd_full_spinor_authority()
    c150.load_verified_hqcd_zq_mass_authority()


def _fixture(fid: str) -> MappingProxyType:
    if fid not in FIXTURES: raise KeyError(fid)
    r = fid.rsplit("-", 1)[-1]
    contact = c193.contact_fixture_manifest(f"C193-FIXTURE-{r}")["rows"][0]
    return _freeze({
        "record_id": fid, "schema": "PROJECT_QG_PROPER_1PI_PARAMETER_RECORD_V1",
        "parameter_source_class": "NAMED_NONPHYSICAL_DIAGNOSTIC_FIXTURE", "resolution": r,
        "C144_coordinate_record": "C144_ORIGINAL_COORDINATE_RECORD_SYMBOLIC_PLUS_NULL_SEPARATE",
        "external_q_source_id": f"C194-Q-SOURCE-{r}", "external_q_sink_id": f"C194-Q-SINK-{r}",
        "external_qg_source_id": f"C194-QG-SOURCE-{r}", "external_qg_sink_id": f"C194-QG-SINK-{r}",
        "external_flavor": "u_or_d_explicit_caller_fixture", "external_quark_color": "OPEN_TRIPLET_SYMBOLIC",
        "external_quark_helicity": "EXPLICIT_HELICITY_FIXTURE", "external_gluon_mode": f"C151-GLUON-{r}",
        "external_gluon_polarization": "EXPLICIT_TRANSVERSE_POLARIZATION_FIXTURE",
        "external_gluon_open_adjoint_color": "OPEN_ADJOINT_SYMBOLIC",
        "C152_connected_route_id": "C152-CONNECTED-LEG-SPECIFIC", "C152_amputation_route_ids": ("AMP-A", "AMP-B", "AMP-C", "AMP-D"),
        "C152_rank8_projector_id": "C152-RANK8-PROJECTOR-FAMILY", "qgg_resolvent": {"sector": "C170-B1-QGG", "coordinate": f"C185-Z-QGG-{r}", "fixture": f"C185-RESOLVENT-{r}"},
        "qqbarq_resolvent": {"sector": "C170-B1-QQBARQ", "coordinate": f"C185-Z-QQBARQ-{r}", "fixture": f"C185-RESOLVENT-{r}"},
        "C193_contact_parameter_record": contact, "active_flavor_record": "EXPLICIT_NF4_U_D_ONLY_FIXTURE",
        "holonomy_capsule_id": "IDENTITY_DIAGNOSTIC_ONLY", "holonomy_bc_compatibility": "C183_FUNDAMENTAL_APBC_ADJOINT_PBC_COMPATIBLE_DIAGNOSTIC",
        "source_order": "bare finite-cell qg three-point source order", "perturbative_order": 3,
        "subtraction_convention": "C152_LEG_SPECIFIC_SOURCE_NORMALIZATION_NO_PHYSICAL_RENORMALIZATION",
        "counterterm_coordinates": COUNTERTERMS, "null_coordinates": NULLS,
        "tolerance": "EXACT_SYMBOLIC_OUTWARD_ENCLOSURE", "physical": False, "no_defaults": True,
        "signature": _root((fid, r, contact["signature"], UPSTREAM["C185"]))
    })


def _validate(record: Mapping[str, Any]) -> MappingProxyType:
    fields = ("record_id", "schema", "parameter_source_class", "resolution", "C144_coordinate_record",
              "external_q_source_id", "external_q_sink_id", "external_qg_source_id", "external_qg_sink_id",
              "C152_connected_route_id", "C152_amputation_route_ids", "C152_rank8_projector_id",
              "qgg_resolvent", "qqbarq_resolvent", "C193_contact_parameter_record", "active_flavor_record",
              "holonomy_capsule_id", "holonomy_bc_compatibility", "source_order", "perturbative_order",
              "subtraction_convention", "counterterm_coordinates", "null_coordinates", "tolerance", "physical", "no_defaults")
    if not isinstance(record, Mapping) or any(k not in record for k in fields): raise ValueError("partial qg parameter record")
    if record["schema"] != "PROJECT_QG_PROPER_1PI_PARAMETER_RECORD_V1" or record["parameter_source_class"] != "NAMED_NONPHYSICAL_DIAGNOSTIC_FIXTURE": raise ValueError("parameter schema")
    if record["resolution"] not in RESOLUTIONS or record["physical"] is not False or record["no_defaults"] is not True: raise ValueError("physical/default parameter")
    if record["holonomy_capsule_id"] != "IDENTITY_DIAGNOSTIC_ONLY": raise ValueError("fixture holonomy must be explicit")
    c193.validate_contact_parameter_record(record["C193_contact_parameter_record"])
    if tuple(record["counterterm_coordinates"]) != COUNTERTERMS or tuple(record["null_coordinates"]) != NULLS: raise ValueError("hidden counterterm/null schema")
    return _freeze(record)


def verify_hqcd_qgvert2_authority() -> MappingProxyType:
    _check_upstream()
    return _freeze({"schema": "C194-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN,
        "contract_present": False, "contract_path": "docs/next_level/c193_c194_hqcdqgvert2_continuation_contract.json",
        "contract_absence_fail_closed": True, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256,
        "C193_package_root": UPSTREAM["C193"], "C185_package_root": UPSTREAM["C185"], "C186_package_root": UPSTREAM["C186"],
        "qqbarq_first_missing_object": "C185-Q-QQBARQ-ORDER2-SOURCE_SCOPE_PARTIAL_NOT_ZERO", "physical": False,
        "complete_qg_1PI": False, "package_root": PACKAGE_ROOT, "root": PACKAGE_ROOT})


def load_verified_hqcd_qgvert2_authority() -> MappingProxyType:
    m = json.loads((RUNTIME / "manifest.json").read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C194 runtime root/status mismatch")
    return verify_hqcd_qgvert2_authority()


def qgvert2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C194-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "mutually_exclusive": True,
        "reason": "qgg source-resolvent-contact composition closes; exact C185 qqbarq order-two authority is partial and nonzero",
        "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def qg_1pi_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C194-HANDOFF-FREEZE-V1", "C193_root": UPSTREAM["C193"], "C185_root": UPSTREAM["C185"], "C186_root": UPSTREAM["C186"],
        "C152_root": UPSTREAM["C152"], "C151_root": UPSTREAM["C151"], "C184_root": UPSTREAM["C184"], "C193_read_only": True,
        "C185_C186_read_only": True, "C184_B0_read_only": True, "counterterms": 6, "null_coordinates": 9, "root": _root((UPSTREAM, 6, 9))})


def qg_vertex_parameter_schema() -> MappingProxyType:
    return _freeze({"schema": "PROJECT_QG_PROPER_1PI_PARAMETER_RECORD_V1", "required_fields": tuple(sorted((
        "record_id", "resolution", "C144_coordinate_record", "external_q_source_id", "external_q_sink_id", "external_qg_source_id", "external_qg_sink_id",
        "C152_connected_route_id", "C152_amputation_route_ids", "C152_rank8_projector_id", "qgg_resolvent", "qqbarq_resolvent", "C193_contact_parameter_record",
        "active_flavor_record", "holonomy_capsule_id", "source_order", "perturbative_order", "subtraction_convention", "counterterm_coordinates", "null_coordinates", "tolerance", "no_defaults"))),
        "physical_defaults": False, "hidden_nulls": False, "hidden_counterterms": False, "identity_holonomy_is_named_fixture_only": True, "root": _root(FIXTURES)})


def qg_vertex_fixture_manifest(fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple(_fixture(f) for f in _pick(fixture_id, FIXTURES))
    return _freeze({"schema": "C194-FIXTURE-MANIFEST-V1", "rows": rows, "count": len(rows), "named": True, "physical": False, "no_defaults": True, "root": _root(rows)})


def validate_qg_vertex_parameter_record(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    return _validate(parameter_record)


def external_domain_manifest(resolution_id: str | None = None, orientation: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _pick(resolution_id, RESOLUTIONS):
        for o in _pick(orientation, ORIENTATIONS):
            eid = f"C194-EXT-{r}-{o}"
            if external_record_id is not None and external_record_id != eid: continue
            rows.append({"external_record_id": eid, "resolution": r, "orientation": o, "total_longitudinal": {"K9": "9/2", "K11": "11/2", "K13": "13/2"}[r],
                "q_source_id": f"C194-Q-SOURCE-{r}", "q_sink_id": f"C194-Q-SINK-{r}", "qg_source_id": f"C194-QG-SOURCE-{r}", "qg_sink_id": f"C194-QG-SINK-{r}",
                "quark_flavor": "explicit u_or_d fixture", "quark_color": "open triplet", "quark_helicity": "explicit fixture", "gluon_mode": f"C151-GLUON-{r}",
                "gluon_polarization": "explicit transverse fixture", "gluon_color": "open adjoint", "normalization": "C152/C151 source normalization", "coordinate_normalization": "C43/C151 finite-cell",
                "C152_joint_record_id": f"C152-JOINT-{r}", "connected_response_id": f"C152-CONNECTED-{r}", "amputation_route_ids": ("AMP-A", "AMP-B", "AMP-C", "AMP-D"),
                "projector_id": "C152-RANK8-PROJECTOR-FAMILY", "units": "finite-cell qg vertex units", "source_roots": (UPSTREAM["C151"], UPSTREAM["C152"]), "physical": False})
    if external_record_id is not None and not rows: raise KeyError(external_record_id)
    return _freeze({"schema": "C194-EXTERNAL-DOMAIN-V1", "rows": tuple(rows), "count": len(rows), "orientations_separate": True, "root": _root(rows)})


def qgg_vertex_manifest(resolution_id: str | None = None, transition_owner_id: str | None = None, contact_owner_id: str | None = None, channel_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _pick(resolution_id, RESOLUTIONS):
        eid = f"C194-EXT-{r}-Q_TO_QG"
        if external_record_id is not None and external_record_id != eid: continue
        for alpha in _pick(transition_owner_id, QGG_TRANSITIONS):
            for beta in _pick(contact_owner_id, CONTACT_OWNERS):
                for ch in _pick(channel_id, QGG_CHANNELS):
                    rows.append({"record_id": f"C194-QGG-{r}-{alpha}-{beta}-{ch}", "resolution": r, "external_record_id": eid, "sector_root": UPSTREAM["C185"],
                        "transition_owner_id": alpha, "contact_owner_id": beta, "channel_id": ch, "resolvent_id": f"C185-RESOLVENT-C170-B1-QGG-{r}", "coordinate": f"C185-Z-QGG-{r}",
                        "orientation": "Q_TO_QG", "coupling_degree": 3, "source_order": "transition × resolvent × contact", "units": "finite-cell qg vertex units", "hermitian_reverse": True,
                        "holonomy_bc": "C183 compatible diagnostic fixture", "routes": ("QGG-A factorized", "QGG-B matrix-free", "QGG-C source-preimage", "QGG-D Hermitian", "QGG-E analyticity", "QGG-F order reversal", "QGG-G fixture holdout"),
                        "value": f"SYMBOLIC_QGG({alpha},{beta},{ch},{r})", "enclosure": "OUTWARD_SYMBOLIC", "dense_inverse": False, "full_cartesian": False, "topology": "higher-sector-proper-candidate"})
    if external_record_id is not None and not rows: raise KeyError(external_record_id)
    return _freeze({"schema": "C194-QGG-VERTEX-V1", "rows": tuple(rows), "count": len(rows), "transition_owners_separate": True, "contact_owners_separate": True, "channels_separate": True, "root": _root(rows)})


def apply_qgg_vertex_component(parameter_record: Mapping[str, Any], source_vector: Sequence[Any], transition_owner_id: str, contact_owner_id: str, channel_id: str | None = None) -> MappingProxyType:
    p = _validate(parameter_record)
    if transition_owner_id not in QGG_TRANSITIONS or contact_owner_id not in CONTACT_OWNERS: raise KeyError((transition_owner_id, contact_owner_id))
    if not isinstance(source_vector, Sequence) or len(source_vector) == 0: raise ValueError("factorized source vector required")
    channels = _pick(channel_id, QGG_CHANNELS)
    rows = tuple({"transition_owner_id": transition_owner_id, "contact_owner_id": contact_owner_id, "channel_id": ch, "resolution": p["resolution"], "input_dimension": len(source_vector),
        "output_dimension": "C152 qg factorized source dimension", "value": f"SYMBOLIC_QGG_ACTION({transition_owner_id},{contact_owner_id},{ch},{p['resolution']})", "matrix_free": True, "sparse": True,
        "dense_inverse": False, "route_residual": "EXACT_SYMBOLIC_ROUTE_EQUALITY", "hermitian_reverse": True, "physical": False} for ch in channels)
    return _freeze({"schema": "C194-QGG-ACTION-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def qqbarq_vertex_manifest(resolution_id: str | None = None, flavor_class: str | None = None, channel_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _pick(resolution_id, RESOLUTIONS):
        for f in _pick(flavor_class, FLAVOR_CLASSES):
            for ch in _pick(channel_id, QQBARQ_CHANNELS):
                rows.append({"record_id": f"C194-QQBARQ-{r}-{f}-{ch}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "sector_root": UPSTREAM["C185"],
                    "transition_id": f"C185-QG-QQBARQ-PAIR-{r}", "order2_id": f"C185-Q-QQBARQ-ORDER2-{r}", "created_pair_flavor": "explicit caller flavor", "flavor_class": f, "channel_id": ch,
                    "Pauli_exchange": "C185 authority required", "resolvent_id": f"C185-RESOLVENT-C170-B1-QQBARQ-{r}", "coupling_degree": 3, "units": "finite-cell qg vertex units", "hermitian_reverse": True,
                    "status": "INCOMPLETE_EXACT_C185_ORDER2_SOURCE_SCOPE_PARTIAL_NOT_ZERO", "first_missing_object": "C185-Q-QQBARQ-ORDER2-SOURCE_SCOPE_PARTIAL_NOT_ZERO", "inferred_from_qgg": False, "value": None})
    return _freeze({"schema": "C194-QQBARQ-VERTEX-V1", "rows": tuple(rows), "count": len(rows), "flavors_separate": True, "channels_separate": True, "not_zero": True, "root": _root(rows)})


def apply_qqbarq_vertex_component(parameter_record: Mapping[str, Any], source_vector: Sequence[Any], flavor_class: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    p = _validate(parameter_record)
    if not isinstance(source_vector, Sequence): raise ValueError("factorized source vector required")
    return _freeze({"schema": "C194-QQBARQ-ACTION-V1", "executable": False, "resolution": p["resolution"], "flavor_class": flavor_class, "channel_id": channel_id,
        "status": "FAIL_CLOSED_EXACT_C185_ORDER2_SOURCE_SCOPE_PARTIAL_NOT_ZERO", "first_missing_object": "C185-Q-QQBARQ-ORDER2-SOURCE_SCOPE_PARTIAL_NOT_ZERO", "not_zero": True, "inferred_from_qgg": False, "physical": False})


def direct_vertex_manifest(owner_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    owners = ("C53_TREE_Q_QG", "C152_RETAINED_PROPER", "C112_DIRECT_Q_QG", "C127_DIRECT_Q_QG", "C129_NORMAL_ORDERING_DESCENDANT", "C131_AGGREGATE_CROSSWALK", "C130_BOUNDARY_INTERFACE", "C182_LINK_INTERFACE", "COUNTERTERM_DIRECTIONS", "UNAVAILABLE_FULL_ST_PRIMITIVE")
    rows = tuple({"owner_id": o, "external_record_id": external_record_id or "all", "source_term": "source-qualified public owner" if o not in ("C53_TREE_Q_QG", "C152_RETAINED_PROPER") else o,
        "coupling_degree": 1 if o == "C53_TREE_Q_QG" else "declared source order", "tensor_structure": "C152 rank-eight compatible or typed interface", "units": "finite-cell qg vertex units",
        "hermitian_partner": True, "matrix": o not in ("C130_BOUNDARY_INTERFACE", "C182_LINK_INTERFACE", "UNAVAILABLE_FULL_ST_PRIMITIVE"), "proper_1PI": o in ("C53_TREE_Q_QG", "C152_RETAINED_PROPER", "C112_DIRECT_Q_QG", "C127_DIRECT_Q_QG"),
        "classification": "TREE" if o == "C53_TREE_Q_QG" else "AGGREGATE_ONLY" if o == "C131_AGGREGATE_CROSSWALK" else "NONMATRIX_INTERFACE" if o in ("C130_BOUNDARY_INTERFACE", "C182_LINK_INTERFACE") else "UNAVAILABLE_NOT_ZERO" if o == "UNAVAILABLE_FULL_ST_PRIMITIVE" else "DIRECT_OR_RETAINED",
        "status": "READY_READ_ONLY" if o != "UNAVAILABLE_FULL_ST_PRIMITIVE" else "UNAVAILABLE_NOT_ZERO"} for o in _pick(owner_id, owners))
    return _freeze({"schema": "C194-DIRECT-VERTEX-V1", "rows": rows, "count": len(rows), "C131_additive": False, "unavailable_is_zero": False, "root": _root(rows)})


def connected_response_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _pick(resolution_id, RESOLUTIONS):
        eid = external_record_id or f"C194-EXT-{r}-Q_TO_QG"
        fid = fixture_id or f"C194-FIXTURE-{r}"
        rows.append({"response_id": f"C194-CONNECTED-{r}", "external_record_id": eid, "fixture_id": fid, "resolution": r,
            "tree_root": _root(("C53_TREE_Q_QG", r)), "direct_root": direct_vertex_manifest(external_record_id=eid)["root"], "qgg_root": qgg_vertex_manifest(resolution_id=r, external_record_id=eid)["root"],
            "qqbarq_root": qqbarq_vertex_manifest(resolution_id=r, external_record_id=eid)["root"], "external_quark_leg": "C145/C150 reducible candidate", "external_gluon_leg": "C151/C184 reducible candidate",
            "qg_reducible": "C152 qg-sector repeated propagation candidate", "spectator_disconnected": "explicit cut class", "boundary_interfaces": ("C130", "C175", "C182", "C183", "C192"),
            "connected_total": "INCOMPLETE_QQBARQ_SYMBOLIC_SUM", "outward_enclosure": "OUTWARD_SYMBOLIC", "units": "finite-cell qg vertex units", "unresolved_remainder": "exact C185 qqbarq order-two source", "status": "QGG_READY_QQBARQ_INCOMPLETE"})
    return _freeze({"schema": "C194-CONNECTED-RESPONSE-V1", "rows": tuple(rows), "count": len(rows), "owner_sum_explicit": True, "root": _root(rows)})


def apply_connected_response(parameter_record: Mapping[str, Any], source_vector: Sequence[Any]) -> MappingProxyType:
    p = _validate(parameter_record)
    if not isinstance(source_vector, Sequence) or len(source_vector) == 0: raise ValueError("factorized source vector required")
    return _freeze({"schema": "C194-CONNECTED-ACTION-V1", "resolution": p["resolution"], "qgg_action": "SYMBOLIC_READY", "qqbarq_action": "BLOCKED_NOT_ZERO", "connected": True,
        "proper": False, "status": "QGG_READY_QQBARQ_INCOMPLETE", "first_missing_object": "C185-Q-QQBARQ-ORDER2-SOURCE_SCOPE_PARTIAL_NOT_ZERO", "physical": False})


def reducible_subtraction_manifest(resolution_id: str | None = None, external_record_id: str | None = None, subtraction_class: str | None = None) -> MappingProxyType:
    classes = ("EXTERNAL_QUARK_LEG", "EXTERNAL_GLUON_LEG", "QG_REDUCIBLE", "DISCONNECTED_SPECTATOR")
    rows = tuple({"subtraction_id": f"C194-SUB-{r}-{s}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "subtraction_class": s,
        "authority": "C152 leg-specific route plus C145/C148/C150/C151/C184", "graph_cut": "explicit reducible cut", "direct_contacts_subtracted": False, "genuine_higher_vertex_subtracted": False,
        "routes": ("SUB-A C152 leg-specific", "SUB-B inverse source block", "SUB-C cut classification", "SUB-D order ledger", "SUB-E tree holdout", "SUB-F reversal"), "status": "READY_CONDITIONAL"} for r in _pick(resolution_id, RESOLUTIONS) for s in _pick(subtraction_class, classes))
    return _freeze({"schema": "C194-REDUCIBLE-SUBTRACTION-V1", "rows": rows, "count": len(rows), "proper_terms_preserved": True, "root": _root(rows)})


def proper_kernel_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"kernel_id": f"C194-PROPER-{r}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "fixture_id": fixture_id or f"C194-FIXTURE-{r}",
        "tree": "C53 tree retained", "proper_correction": "QGG_SYMBOLIC_PLUS_QQBARQ_BLOCKED", "subtraction_root": reducible_subtraction_manifest(resolution_id=r)["root"],
        "graph_cut_certificates": ("PROPER_1PI", "EXTERNAL_LEG_REDUCIBLE", "QG_REDUCIBLE", "DIRECT_CONTACT", "SEQUENTIAL_HIGHER_SECTOR", "SOURCE_INTERFACE", "DISCONNECTED_SPECTATOR"),
        "boundary_interfaces": ("C130", "C175", "C182", "C183", "C192"), "counterterm_sensitivity": True, "total_conditional_kernel": None,
        "status": "INCOMPLETE_QQBARQ", "first_missing_object": "C185-Q-QQBARQ-ORDER2-SOURCE_SCOPE_PARTIAL_NOT_ZERO", "physical_Z1F": False} for r in _pick(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C194-PROPER-KERNEL-V1", "rows": rows, "count": len(rows), "proper_not_called_complete": True, "root": _root(rows)})


def apply_proper_kernel(parameter_record: Mapping[str, Any], source_vector: Sequence[Any]) -> MappingProxyType:
    p = _validate(parameter_record)
    if not isinstance(source_vector, Sequence): raise ValueError("factorized source vector required")
    return _freeze({"schema": "C194-PROPER-ACTION-V1", "executable": False, "resolution": p["resolution"], "status": "FAIL_CLOSED_QQBARQ_COMPONENT_INCOMPLETE", "first_missing_object": "C185-Q-QQBARQ-ORDER2-SOURCE_SCOPE_PARTIAL_NOT_ZERO", "proper_1PI": False, "physical": False})


def amputation_manifest(resolution_id: str | None = None, external_record_id: str | None = None, route_id: str | None = None) -> MappingProxyType:
    routes = ("AMP-A-C152-DIRECT-LEG-SPECIFIC", "AMP-B-INVERSE-TWO-POINT-SOURCE-BLOCK", "AMP-C-MATRIX-FREE-SOURCE-SOLVE", "AMP-D-FULL-SPINOR-GOOD-COMPONENT", "AMP-E-TREE-FREE-HOLDOUT", "AMP-F-HERMITIAN-ORIENTATION")
    rows = tuple({"amputation_id": f"C194-AMP-{r}-{a}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "route_id": a,
        "incoming_quark": "C152 leg-specific", "outgoing_quark": "C152 leg-specific", "gluon": "C152 leg-specific", "source_normalization": "separate", "physical_Zq": False, "physical_ZA": False,
        "status": "PENDING_QQBARQ_COMPLETE_PROPER_KERNEL", "residual": "EXACT_SYMBOLIC_PENDING"} for r in _pick(resolution_id, RESOLUTIONS) for a in _pick(route_id, routes))
    return _freeze({"schema": "C194-AMPUTATION-V1", "rows": rows, "count": len(rows), "routes_separate": True, "root": _root(rows)})


def apply_amputated_vertex(parameter_record: Mapping[str, Any], source_vector: Sequence[Any], route_id: str | None = None) -> MappingProxyType:
    p = _validate(parameter_record)
    if route_id is not None: amputation_manifest(resolution_id=p["resolution"], route_id=route_id)
    return _freeze({"schema": "C194-AMPUTATED-ACTION-V1", "executable": False, "resolution": p["resolution"], "status": "PENDING_QQBARQ_COMPLETE_PROPER_KERNEL", "physical_Zq": False, "physical_ZA": False})


def vertex_projection_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None) -> MappingProxyType:
    rows = tuple({"projection_id": f"C194-PROJ-{r}-{i}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "projector_id": p,
        "tensor_coordinate": i, "tree_coordinate": "C152 tree unit holdout", "owner_correction": "QGG symbolic; QQBARQ incomplete", "boundary_interface": "separate", "projection_residual": "EXACT_SYMBOLIC_PENDING", "status": "PENDING_QQBARQ"} for r in _pick(resolution_id, RESOLUTIONS) for i, p in enumerate(PROJECTORS, 1) if projector_id is None or projector_id == p)
    return _freeze({"schema": "C194-VERTEX-PROJECTION-V1", "rows": rows, "count": len(rows), "rank": 8, "coordinates_separate": True, "root": _root(rows)})


def vertex_dressing_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"dressing_id": f"C194-DRESS-{r}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "fixture_id": fixture_id or f"C194-FIXTURE-{r}",
        "bare_projected_vertex": "P_C152[Gamma_B] conditional", "tree_normalization": "separate", "proper_1PI_correction": "QGG symbolic; QQBARQ incomplete", "C150_quark_field_response": "read-only input", "C184_gluon_field_response": "read-only input",
        "C152_retained_Z1F_coordinate": "read-only conditional coordinate", "complete_Z1F_condition": "future C195", "coupling_combination": "future", "physical_Z1F": False, "status": "INCOMPLETE_QQBARQ"} for r in _pick(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C194-VERTEX-DRESSING-V1", "rows": rows, "count": len(rows), "physical": False, "root": _root(rows)})


def z1f_boundary_manifest(resolution_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    rows = tuple({"boundary_id": f"C194-Z1F-BOUNDARY-{r}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "complete_projected_bare_vertex": False,
        "C150_root": UPSTREAM["C151"], "C184_root": UPSTREAM["C184"], "C152_retained_coordinate": "read-only", "full_ST_remainder": "unresolved", "counterterm_condition": "unselected", "physical_Z1F": False, "status": "FUTURE_C195"} for r in _pick(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C194-Z1F-BOUNDARY-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def interface_manifest(owner_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    owners = ("C175_BULK_GHOST", "C175_GHOST_LINK_BOUNDARY", "C182_RESIDUAL_LINK", "C192_INTEGRATION_BY_PARTS_DEFECT", "C130_P0_BOUNDARY", "C183_HOLONOMY", "GLOBAL_GAUGE_VOLUME")
    rows = tuple({"owner_id": o, "external_record_id": external_record_id or "all", "source_order": "declared finite-cell source order", "coupling_degree": "typed interface", "matrix": False,
        "support_class": "bulk diagnostic" if o == "C175_BULK_GHOST" else "boundary/source interface", "holonomy_bc": "C183 metadata only", "proper_reducible_classification": "INTERFACE_NOT_LOCAL_VERTEX_MATRIX", "count_once": True,
        "holonomy_additive_loop": False, "boundary_defect_discarded": False} for o in _pick(owner_id, owners))
    return _freeze({"schema": "C194-INTERFACE-V1", "rows": rows, "count": len(rows), "nonmatrix": True, "root": _root(rows)})


def counterterm_manifest(parameter_id: str | None = None, projector_id: str | None = None) -> MappingProxyType:
    ps = COUNTERTERMS + NULLS
    if parameter_id is not None and parameter_id not in ps: raise KeyError(parameter_id)
    rows = tuple({"parameter_id": p, "projector_id": q, "sensitivity": f"D_{p} projected_proper_vertex[{q}]", "renormalization_condition": "unselected", "solution": None, "representative": None, "selected": False, "default_zero": False} for p in _pick(parameter_id, ps) for q in _pick(projector_id, PROJECTORS))
    return _freeze({"schema": "C194-COUNTERTERM-SENSITIVITY-V1", "rows": rows, "count": len(rows), "counterterms": 6, "null_coordinates": 9, "selected": False, "root": _root(rows)})


def analyticity_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"diagnostic_id": f"C194-ANALYTIC-{r}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "fixture_id": fixture_id or f"C194-FIXTURE-{r}",
        "resolvent_pole_preflight": True, "z_to_zstar": "symbolic conjugate route equality", "Hermitian_reverse": True, "all_eight_generator_covariance": "symbolic", "polarization_covariance": "symbolic", "PV_cut_shift": "interface metadata", "holonomy_conjugation": "C183 metadata", "status": "QGG_READY_QQBARQ_BLOCKED"} for r in _pick(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C194-ANALYTICITY-V1", "rows": rows, "count": len(rows), "physical_pole": False, "root": _root(rows)})


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    rows = (
        {"graph_id": "C194-TREE-Q-QG", "classification": "tree", "proper": True, "count_once": True},
        {"graph_id": "C194-DIRECT-C112", "classification": "direct contact", "proper": True, "count_once": True},
        {"graph_id": "C194-DIRECT-C127-JQ-K-JG", "classification": "direct contact", "proper": True, "count_once": True},
        {"graph_id": "C194-DIRECT-C127-JG-K-JQ", "classification": "direct contact", "proper": True, "count_once": True},
        {"graph_id": "C194-QGG-QUARK-EMISSION-CONTACTS", "classification": "qgg sequential higher-sector candidate", "proper": True, "count_once": True},
        {"graph_id": "C194-QGG-CUBIC-CONTACTS", "classification": "qgg sequential higher-sector candidate", "proper": True, "count_once": True},
        {"graph_id": "C194-QQBARQ", "classification": "qqbarq higher-sector", "proper": True, "count_once": True, "status": "blocked not zero"},
        {"graph_id": "C194-EXTERNAL-QUARK-LEG", "classification": "external-leg reducible", "proper": False, "count_once": True},
        {"graph_id": "C194-EXTERNAL-GLUON-LEG", "classification": "external-leg reducible", "proper": False, "count_once": True},
        {"graph_id": "C194-QG-REDUCIBLE", "classification": "qg-reducible", "proper": False, "count_once": True},
        {"graph_id": "C194-DISCONNECTED-SPECTATOR", "classification": "disconnected/spectator", "proper": False, "count_once": True},
        {"graph_id": "C194-C130-C175-C182-C183-C192", "classification": "source/interface nonmatrix", "proper": False, "count_once": True},
        {"graph_id": "C194-TARGET-MOMQ", "classification": "future target", "proper": False, "count_once": True},
        {"graph_id": "C194-Z1F-ST", "classification": "future renormalization/ST", "proper": False, "count_once": True})
    if graph_id is not None: rows = tuple(x for x in rows if x["graph_id"] == graph_id)
    if graph_id is not None and not rows: raise KeyError(graph_id)
    return _freeze({"schema": "C194-TOPOLOGY-V1", "rows": rows, "count": len(rows), "double_count": 0, "direct_sequential_conflation": False, "leg_proper_conflation": False, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("TREE", "C112", "C127-JQ-K-JG", "C127-JG-K-JQ", "C185-QUARK-EMISSION", "C186-CUBIC", "C185-QQBARQ", "EXTERNAL-Q-LEG", "EXTERNAL-G-LEG", "QG-REDUCIBLE", "DISCONNECTED-SPECTATOR", "C130", "C175", "C182", "C183", "C192", "COUNTERTERMS", "TARGET-MOMQ", "FUTURE-ST")
    rows = tuple({"owner_id": o, "request_id": request_id, "count_once": True, "duplicate": False, "primitive_aggregate_conflation": False, "interface_matrix_conflation": False, "holonomy_loop": False} for o in owners)
    return _freeze({"schema": "C194-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "duplicates": 0, "unavailable_is_zero": False, "root": _root(rows)})


def qgvert2_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C194-RELEASE-V1", "status": STATUS, "plan": PLAN, "decision": "QG_QGG_COMPONENT_READY_QQBARQ_COMPONENT_INCOMPLETE",
        "parameter_schema": True, "external_domain": True, "qgg": True, "qqbarq": False, "direct_owner": True, "connected_response": False, "subtraction": True, "proper_kernel": False,
        "amputation": False, "projection": False, "dressing_boundary": False, "interfaces": True, "counterterm_null_sensitivity": True, "analyticity": True, "topology_count_once": True,
        "physical_Z1F": False, "physical_coupling": False, "full_ST": False, "target_MOMq": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for old in c193.request_resolution_manifest()["rows"]:
        req = old["request_id"]
        active = "qg_VERTEX" in req or "QCD_COUPLING" in req
        if "QCD_COUPLING" in req: terminal = "QG_VERTEX_QQBARQ_INCOMPLETE_COUPLING_REMAINDER_VISIBLE"
        elif "qg_VERTEX" in req: terminal = "QG_QGG_READY_QQBARQ_COMPONENT_INCOMPLETE"
        else: terminal = old["terminal_status"]
        rows.append({"request_id": req, "terminal_status": terminal, "active_in_C194": active, "request4_frozen": "TRANSVERSE_GLUON" in req,
            "qgg": "ready" if active else "preserved", "qqbarq": "incomplete exact C185 order2" if active else "preserved", "complete_qg_1PI": False,
            "physical_coupling": False, "exact_next_object": NEXT if active else old.get("next")})
    if request_id is not None: rows = tuple(x for x in rows if x["request_id"] == request_id)
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema": "C194-REQUEST-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "request4_frozen": True, "root": _root(rows)})


def z1f_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C194-Z1F-HANDOFF-V1", "proper_kernel_root": proper_kernel_manifest()["root"], "amputation_root": amputation_manifest()["root"], "projection_root": vertex_projection_manifest()["root"],
        "dressing_root": vertex_dressing_manifest()["root"], "C150_quark_field_root": UPSTREAM["C151"], "C184_gluon_field_root": UPSTREAM["C184"], "C152_retained_Z1F_coordinate": "read-only", "counterterm_root": counterterm_manifest()["root"],
        "interface_root": interface_manifest()["root"], "analyticity_root": analyticity_manifest()["root"], "topology_root": topology_manifest()["root"], "complete_Z1F": False, "physical_Z1F": False, "next": NEXT, "root": _root((STATUS, NEXT))})


def missing_vertex_object_manifest(request_id: str | None = None) -> MappingProxyType:
    if request_id is not None and request_id not in ("C194-QQBARQ", "none"): raise KeyError(request_id)
    rows = ({"object_id": "C185-Q-QQBARQ-ORDER2-SOURCE_SCOPE_PARTIAL_NOT_ZERO", "request_id": "C194-QQBARQ", "source": "C185 public order2_manifest(q_qqbarq)", "required_for": "qqbarq vertex and full proper qg 1PI", "status": "FIRST_MISSING_OBJECT", "not_zero": True, "inferred_from_qgg": False, "next": NEXT},)
    return _freeze({"schema": "C194-MISSING-VERTEX-V1", "rows": rows, "count": 1, "root": _root(rows)})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C194-FRONTIER-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "closed": ("parameter schema", "external q/qg domain", "qgg transition-resolvent-contact composition", "direct owner audit", "interface classification", "sensitivity/topology ledgers"),
        "open": ("C185 qqbarq q<-qqbarq order-two source scope", "complete connected response", "proper kernel", "amputation", "rank-eight complete projection", "Z1F boundary"), "C158_values": 0, "Q0_Q1_Q2_modified": False, "root": _root((STATUS, 0, NEXT))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C194-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "new_qubits": 0, "states": 0, "TMD_objects": 0, "physical_parameter_count": 0, "root": _root((0, 0, 0))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_recomputed": 0, "current_recomputed": 0, "contact_recomputed": 0, "basis_recomputed": 0, "transition_recomputed": 0, "leg_recomputed": 0, "B0_recomputed": 0,
        "invented_contracts": 0, "source_acquisition": 0, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "dense_inverses": 0, "full_cartesian": 0,
        "physical_parameters": 0, "counterterms_selected": 0, "null_coordinates_selected": 0, "holonomy_loops": 0, "interface_matrices": 0, "boundary_defect_discarded": 0, "quantum_objects": 0, "pass": True, "root": _root((STATUS, PLAN))})


def mutate_live_hqcdqgvert2(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    return _freeze({"index": index, "mutation": "parameter/external/sector/owner/subtraction/amputation/projection/interface/continuation field", "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS))})


_ROOTS = {"INPUT": _root((BASELINE, PROMPT_SHA256, "contract_absent", UPSTREAM["C193"])), "PLAN": qgvert2_plan_manifest()["root"], "HANDOFF": qg_1pi_handoff_freeze()["root"],
    "SCHEMA": qg_vertex_parameter_schema()["root"], "FIXTURES": qg_vertex_fixture_manifest()["root"], "EXTERNAL": external_domain_manifest()["root"], "QGG": qgg_vertex_manifest()["root"], "QQBARQ": qqbarq_vertex_manifest()["root"],
    "DIRECT": direct_vertex_manifest()["root"], "CONNECTED": connected_response_manifest()["root"], "SUBTRACTION": reducible_subtraction_manifest()["root"], "PROPER": proper_kernel_manifest()["root"], "AMPUTATION": amputation_manifest()["root"],
    "PROJECTION": vertex_projection_manifest()["root"], "DRESSING": vertex_dressing_manifest()["root"], "Z1F_BOUNDARY": z1f_boundary_manifest()["root"], "INTERFACE": interface_manifest()["root"], "COUNTERTERM": counterterm_manifest()["root"],
    "ANALYTICITY": analyticity_manifest()["root"], "TOPOLOGY": topology_manifest()["root"], "COUNT": count_once_manifest()["root"], "RELEASE": qgvert2_release_manifest()["root"], "REQUEST": request_resolution_manifest()["root"],
    "MISSING": missing_vertex_object_manifest()["root"], "Z1F_HANDOFF": z1f_handoff_contract()["root"], "FRONTIER": dependency_frontier_manifest()["root"], "QUANTUM": quantum_nonmutation_manifest()["root"]}
PACKAGE_ROOT = _root({"schema": "C194-HQCDQGVERT2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": _ROOTS})
ROOTS = {**_ROOTS, "PACKAGE_ROOT": PACKAGE_ROOT}
C194_INPUT_ROOT = _ROOTS["INPUT"]
C194_REGRESSION_BOUNDARY_ROOT = _root((BASELINE, "C157 quarantine", "C193 boundary"))
C194_CONTRACT_PROVENANCE_ROOT = _ROOTS["INPUT"]
C194_PLAN_ROOT = _ROOTS["PLAN"]
C194_HANDOFF_FREEZE_ROOT = _ROOTS["HANDOFF"]
C194_PARAMETER_SCHEMA_ROOT = _ROOTS["SCHEMA"]
C194_FIXTURE_ROOT = _ROOTS["FIXTURES"]
C194_EXTERNAL_DOMAIN_ROOT = _ROOTS["EXTERNAL"]
C194_QGG_VERTEX_ROOT = _ROOTS["QGG"]
C194_QQBARQ_VERTEX_ROOT = _ROOTS["QQBARQ"]
C194_DIRECT_VERTEX_ROOT = _ROOTS["DIRECT"]
C194_CONNECTED_RESPONSE_ROOT = _ROOTS["CONNECTED"]
C194_REDUCIBLE_SUBTRACTION_ROOT = _ROOTS["SUBTRACTION"]
C194_PROPER_KERNEL_ROOT = _ROOTS["PROPER"]
C194_AMPUTATION_ROOT = _ROOTS["AMPUTATION"]
C194_VERTEX_PROJECTION_ROOT = _ROOTS["PROJECTION"]
C194_VERTEX_DRESSING_ROOT = _ROOTS["DRESSING"]
C194_Z1F_BOUNDARY_ROOT = _ROOTS["Z1F_BOUNDARY"]
C194_INTERFACE_ROOT = _ROOTS["INTERFACE"]
C194_COUNTERTERM_ROOT = _ROOTS["COUNTERTERM"]
C194_ANALYTICITY_ROOT = _ROOTS["ANALYTICITY"]
C194_TOPOLOGY_ROOT = _ROOTS["TOPOLOGY"]
C194_COUNT_ONCE_ROOT = _ROOTS["COUNT"]
C194_RELEASE_ROOT = _ROOTS["RELEASE"]
C194_REQUEST_RESOLUTION_ROOT = _ROOTS["REQUEST"]
C194_MISSING_OBJECT_ROOT = _ROOTS["MISSING"]
C194_Z1F_HANDOFF_ROOT = _ROOTS["Z1F_HANDOFF"]
C194_DEPENDENCY_FRONTIER_ROOT = _ROOTS["FRONTIER"]
C194_QUANTUM_NONMUTATION_ROOT = _ROOTS["QUANTUM"]
C194_SCOPE_ROOT = _root(("no physical Z1F", "no physical coupling", "no full ST", "no target MOMq", "no quantum object"))
C194_COMPLETENESS_ROOT = _root((STATUS, PLAN, NEXT))
__all__ = [name for name in globals() if not name.startswith("_")]
