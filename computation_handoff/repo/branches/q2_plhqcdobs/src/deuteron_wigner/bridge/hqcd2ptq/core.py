"""C143 forward-quark finite-basis two-point boundary.

This package freezes the C142 source map and exposes only structural
resolvent metadata until a caller supplies a complete, authenticated,
nonphysical diagnostic parameter record.  It deliberately never chooses a
mass, coupling, counterterm, null-space representative, or physical width.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c143_hqcd2ptq"
BASELINE = "62c748dd641bf095eec30b7d51249f457cd7c24d"
CONTRACT = "docs/next_level/c142_c143_hqcd2ptq_import_contract.json"
CONTRACT_SHA256 = "cfbede74feaa1809839ed543d5a4db93b7d57f55e1f9a3a044687d04c82b82b7"
SCHEMA = "C143-HQCD2PTQ-V1"
STATUS = "C143_HQCD2PTQ_PARAMETERIZED_OPERATOR_INCOMPLETE"
NEXT = "C144/HQCDOPAPI"
RESOLUTIONS = ("K9", "K11", "K13")
Q_DIMS = {"K9": 6, "K11": 6, "K13": 6}
QG_DIMS = {"K9": 1344, "K11": 2700, "K13": 4752}
DIMS = {r: Q_DIMS[r] + QG_DIMS[r] for r in RESOLUTIONS}
Z_UNITS = "GeV^2"
PARAMETER_TIER = "NONPHYSICAL_RESOLVENT_DIAGNOSTIC_POINT"
C142_PACKAGE_ROOT = "3e862b300f594a0bb8f5eda20f9dd6ca635cead07ef510195d86e6b73549736d"
C142_SOURCE_MAP_ROOT = "7fb216027e2e8d65449da325d1628b56432a9e2e4cf9bc2d608e50036cab9c68"
C142_SOURCE_MODE_ROOT = "c6417695b7ea0dd9da547852655a824c22cdab52a835b33ba23392aeafd30568"
C142_VACUUM_ROOT = "dba4ffdeae17cc42e95d77bec642ccc6dcf6392c4ab67ed1c6d47422a28336c0"
C141_ROOT = "860aa94d86b79e2ad113149258c0241e85000d0c1afe40173f5accb62dcb532f"
C140_ROOT = "2b54855f128afe5129f5dfe46cf23e06888ce8da13b9c98b0eccdb57d6cc4fba"
C139_ROOT = "4f7a688eeaa492ce7bea569ac4442cea30ee549168ef8291be4e89774f92a361"
C138_ROOT = "075c29f17e149b35ae2b78dcbc0f33c25d7457b321fd01479238cecd875eec9b"
C137_ROOT = "96e3f9b1d25e546c7d968abe46def0cbacd205ed238b6f5d3aa776fc44b6041c"
C136_ROOT = "fac2b3210bfef7cd3dc22a1a05ea47d9253a641172308603f4c2f3b6c31eb262"
C135_ROOT = "e94b1bb47b0ab2d7499922ef558a8b32f0c6796ee7edcf2d86aed9e048ddcb5b"
C134_ROOT = "709a8955c466cee493da30fe23b9a31b85d63e8541e256ba92f6ce21568a9dd4"
C133_ROOT = "c47a70ad4a87cac048db0c00fd1e24e7f5bde110596aec9116bcfc34bde9add9"
C132_ROOT = "192de102695f89ed00aa1a1f1959395c28118177bb59b9ae9c4ec11ecaf84adc"
C131_ROOT = "67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"
C130_ROOT = "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe"
C129_ROOT = "4c85424eb7cfa6a6ee190e907c36245ca0325623e4de79e923007583a9804678"
C128_ROOT = "d23ce7d398204f1e88612448564d26d17019fa832c8c041d3382c7be1553a6f1"
C127_ROOT = "0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"
C126_ROOT = "84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"
C125_ROOT = "a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"

COUNTERTERMS = ("ct_mass", "ct_vacuum_energy", "ct_gluon_mass", "ct_sector", "ct_boundary", "ct_truncation")
NULL_COORDINATES = tuple(f"eta_{i}" for i in range(9))
REQUIRED_PARAMETERS = ("g_s", "m_q", "m_q^2", "b_HO", *COUNTERTERMS, *NULL_COORDINATES)

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x

def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x

def _canon(x: Any) -> str:
    return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def _root(x: Any) -> str:
    return sha256(_canon(x).encode("utf-8")).hexdigest()

def _resolution(resolution: str) -> str:
    if resolution not in RESOLUTIONS: raise ValueError(f"unsupported C143 resolution: {resolution!r}")
    return resolution

def load_verified_hqcd2ptq_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C143 runtime manifest missing")
    m = json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS:
        raise ValueError("C143 package root/status mismatch")
    return _freeze(verify_hqcd_two_pointq_authority())

def parameter_record_schema() -> MappingProxyType:
    fields = []
    for ident in REQUIRED_PARAMETERS:
        unit = "GeV" if ident == "m_q" else "GeV^2" if ident == "m_q^2" else "GeV" if ident == "b_HO" else "1"
        fields.append({"id": ident, "value_or_expression": True, "units": unit,
                       "resolution": "K9|K11|K13|all", "role": "caller_supplied",
                       "claim_tier": PARAMETER_TIER, "provenance": "explicit caller capsule",
                       "no_default": True})
    return _freeze({"schema": "C143-PARAMETER-RECORD-SCHEMA-V1", "fields": tuple(fields),
                    "required_count": len(REQUIRED_PARAMETERS), "no_defaults": True,
                    "physical_values": False, "root": _root(fields)})

def diagnostic_parameter_manifest() -> MappingProxyType:
    return _freeze({"schema": "C143-DIAGNOSTIC-PARAMETER-MANIFEST-V1", "records_supplied": 0,
                    "required_inputs": REQUIRED_PARAMETERS, "claim_tier": PARAMETER_TIER,
                    "no_numerical_defaults": True, "evaluations": 0,
                    "status": "NO_CALLER_SUPPLIED_PARAMETER_RECORD", "root": _root((REQUIRED_PARAMETERS, 0))})

def validate_parameter_record(record: Mapping[str, Any]) -> MappingProxyType:
    if not isinstance(record, Mapping): raise ValueError("parameter record must be a mapping")
    missing = tuple(x for x in REQUIRED_PARAMETERS if x not in record)
    if missing: raise ValueError(f"parameter record missing required IDs: {missing}")
    if record.get("claim_tier") != PARAMETER_TIER or record.get("no_default") is not True:
        raise ValueError("parameter record must be explicit NONPHYSICAL_RESOLVENT_DIAGNOSTIC_POINT with no_default=true")
    if record.get("m_q^2") != record.get("m_q") ** 2:
        raise ValueError("m_q^2=(m_q)^2 identity mismatch")
    if record.get("resolution") not in RESOLUTIONS and record.get("resolution") != "all":
        raise ValueError("parameter record has invalid resolution scope")
    return _freeze({"schema": "C143-VALIDATED-PARAMETER-RECORD-V1", "record": dict(record),
                    "root": _root(dict(record)), "physical": False})

def spectral_variable(z: Mapping[str, Any]) -> MappingProxyType:
    if not isinstance(z, Mapping) or z.get("units") != Z_UNITS or z.get("analytic_query") is not True:
        raise ValueError("z must be an analytic GeV^2 query coordinate")
    if z.get("physical_width") is True: raise ValueError("imaginary z is not a physical width")
    if "real" not in z or "imaginary" not in z: raise ValueError("z requires real and imaginary coordinates")
    return _freeze({"schema": "C143-COMPLEX-MASS-SQUARED-V1", **dict(z), "physical_width": False})

def source_embedding(resolution: str) -> MappingProxyType:
    r = _resolution(resolution); d = DIMS[r]
    rows = tuple(tuple(1 if i == j else 0 for j in range(6)) if i < 6 else (0,) * 6 for i in range(d))
    return _freeze({"schema": "C143-FULL-Q-QG-SOURCE-EMBEDDING-V1", "resolution": r,
                    "shape": (d, 6), "basis_order": "q followed by qg", "q_rows_identity": True,
                    "qg_rows_zero": True, "direct_qg_source": "NOT_APPLICABLE_WITH_OPERATOR_PROOF",
                    "matrix": rows, "source_root": C142_SOURCE_MAP_ROOT, "root": _root((r, rows, C142_SOURCE_MAP_ROOT))})

def source_embedding_manifest() -> MappingProxyType:
    rows = tuple(source_embedding(r) for r in RESOLUTIONS)
    return _freeze({"schema": "C143-SOURCE-EMBEDDING-MANIFEST-V1", "rows": rows,
                    "route_A": "C142 source-map insertion", "route_B": "exact q/qg block embedding",
                    "route_C": "C142 public matrix-free source application", "route_mismatches": 0,
                    "root": _root(rows)})

def operator_block_manifest(resolution: str) -> MappingProxyType:
    r = _resolution(resolution)
    return _freeze({"schema": "C143-OPERATOR-BLOCK-MANIFEST-V1", "resolution": r,
                    "shape": (DIMS[r], DIMS[r]), "blocks": {"A_qq": (6, 6), "B_q_qg": (6, QG_DIMS[r]),
                    "C_qg_q": (QG_DIMS[r], 6), "D_qg_qg": (QG_DIMS[r], QG_DIMS[r])},
                    "orientation": "M=[[A,B],[C,D]]", "units": "GeV^2", "coupling_degrees": (0, 1, 2),
                    "source": "C131 public sparse coefficient authority", "effective_hamiltonian": False,
                    "parameter_record_required": True, "root": _root((r, DIMS[r], QG_DIMS[r]))})

def _require_record(parameter_record: Mapping[str, Any] | None) -> MappingProxyType:
    if parameter_record is None: raise ValueError("C143 numerical routes require an explicit caller-supplied parameter record")
    return validate_parameter_record(parameter_record)

def route_validation() -> MappingProxyType:
    return _freeze({"schema": "C143-ROUTE-VALIDATION-V1", "route_A": {"executed": False, "calls": 0},
                    "route_B": {"executed": False, "calls": 0}, "route_C": {"executed": False, "calls": 0},
                    "route_mismatches": 0, "blocked_on_parameter_record": True, "root": _root((0, 0, 0))})

def source_projected_resolvent(resolution: str, z: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None) -> MappingProxyType:
    _resolution(resolution); spectral_variable(z); _require_record(parameter_record)
    raise NotImplementedError("C143 numerical solve is outside the selected no-input plan")

def matrix_free_resolvent(resolution: str, z: Mapping[str, Any], vector: Sequence[Any], *, parameter_record: Mapping[str, Any] | None = None) -> MappingProxyType:
    _resolution(resolution); spectral_variable(z); _require_record(parameter_record)
    raise NotImplementedError("C143 matrix-free numerical solve is outside the selected no-input plan")

def inverse_two_point(*args: Any, **kwargs: Any) -> MappingProxyType:
    raise ValueError("C143 inverse source two-point is unavailable before parameterized resolvent evaluation")

def retained_qg_self_energy(*args: Any, **kwargs: Any) -> MappingProxyType:
    raise ValueError("C143 retained qg self-energy is unavailable before parameterized resolvent evaluation")

def order_g2_comparison(*args: Any, **kwargs: Any) -> MappingProxyType:
    raise ValueError("C143 order-g^2 comparison is unavailable before parameterized evaluation")

def static_isolation_guard() -> MappingProxyType:
    return _freeze({"schema": "C143-ISOLATION-GUARD-V1", "C80_calls": 0, "C53_replay": 0,
                    "C131_private_reads": 0, "PDG_reads": 0, "physical_parameters": 0,
                    "counterterms_selected": 0, "null_coordinates_selected": 0,
                    "dense_inverse": 0, "feshbach_hamiltonian": 0, "full_propagator": 0,
                    "pass": True, "root": _root((0,) * 10)})

def mutate_live_hqcd2ptq(index: int) -> MappingProxyType:
    fields = ("z", "parameter_record", "m_q", "m_q^2", "counterterm", "null_coordinate", "source_map",
              "qg_source", "basis_order", "imaginary_width", "mass_projector", "Z_q", "antiquark", "root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False,
                    "must_fail_or_change_root": True})

def verify_hqcd_two_pointq_authority() -> dict[str, Any]:
    return {"schema": SCHEMA, "status": STATUS, "positive_gate": False, "plan": "2PTQ-D",
            "baseline": BASELINE, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256,
            "C142_package_root": C142_PACKAGE_ROOT, "C142_source_map_root": C142_SOURCE_MAP_ROOT,
            "C142_source_mode_root": C142_SOURCE_MODE_ROOT, "C142_vacuum_root": C142_VACUUM_ROOT,
            "dimensions": DIMS, "q_dimensions": Q_DIMS, "qg_dimensions": QG_DIMS,
            "basis_order": "q followed by qg", "source_embedding_shapes": {r: (DIMS[r], 6) for r in RESOLUTIONS},
            "source_rank": 6, "source_kernel": 0, "source_cokernel": 0, "direct_qg_source": False,
            "parameter_records": 0, "route_A_calls": 0, "route_B_calls": 0, "route_C_calls": 0,
            "route_mismatches": 0, "resolvent_constructed": False, "self_energy_constructed": False,
            "mass_projector_constructed": False, "Z_q_constructed": False, "negative_frequency": False,
            "physical_parameters": 0, "counterterms_selected": 0, "null_coordinates_set_to_zero": 0,
            "expanded_domain": False, "block_resolvent_effective_hamiltonian": False,
            "blocker": "NO_CALLER_SUPPLIED_NONPHYSICAL_RESOLVENT_DIAGNOSTIC_PARAMETER_RECORD",
            "next": NEXT, "roots": ROOTS, "package_root": PACKAGE_ROOT}

# Descriptive aliases used by handoff clients.  They are the same immutable
# authority and do not open a private reconstruction route.
verify_hqcd2ptq_authority = verify_hqcd_two_pointq_authority
load_verified_hqcd2ptq = load_verified_hqcd2ptq_authority

ROOTS = {"C143_PARAMETER_SCHEMA_ROOT": _root(parameter_record_schema()),
         "C143_INPUT_MANIFEST_ROOT": _root(diagnostic_parameter_manifest()),
         "C143_SOURCE_EMBEDDING_ROOT": _root(source_embedding_manifest()),
         "C143_BLOCK_MANIFEST_ROOT": _root(tuple(operator_block_manifest(r) for r in RESOLUTIONS)),
         "C143_ROUTE_VALIDATION_ROOT": _root(route_validation()),
         "C143_SCOPE_ROOT": _root(("forward_good_component", "no_full_spinor", "no_mass_projector", "no_Zq")),
         "C142_PACKAGE_ROOT": C142_PACKAGE_ROOT}
PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT,
                      "status": STATUS, "roots": ROOTS, "next": NEXT})

__all__ = ["STATUS", "NEXT", "PACKAGE_ROOT", "ROOTS", "RESOLUTIONS", "DIMS", "Q_DIMS", "QG_DIMS",
           "parameter_record_schema", "diagnostic_parameter_manifest", "validate_parameter_record",
           "spectral_variable", "source_embedding", "source_embedding_manifest", "operator_block_manifest",
           "route_validation", "source_projected_resolvent", "matrix_free_resolvent", "inverse_two_point",
           "retained_qg_self_energy", "order_g2_comparison", "static_isolation_guard", "mutate_live_hqcd2ptq",
           "verify_hqcd_two_pointq_authority", "verify_hqcd2ptq_authority",
           "load_verified_hqcd2ptq_authority", "load_verified_hqcd2ptq"]
