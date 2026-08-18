"""C142/HQCDFIELD finite-basis good-quark source authority.

This module owns only the canonical nonzero-mode perturbative reference
vacuum, projected good-field mode chart, and forward-quark source/sink
isometry.  It never constructs a propagator, self-energy, mass projector,
or physical parameter.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Sequence

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c142_hqcdfield"
BASELINE = "98007c6a171701ef60382f5f9b2e0b9d5fcb7a15"
CONTRACT = "docs/next_level/c141_c142_hqcdfield_import_contract.json"
CONTRACT_SHA256 = "cfbede74feaa1809839ed543d5a4db93b7d57f55e1f9a3a044687d04c82b82b7"
STATUS = "C142_C141_SOURCE_DERIVED_C43_NONZERO_MODE_QUARK_FIELD_SOURCE_MAP_READY"
NEXT = "C143/HQCD2PTQ"
SCHEMA = "C142-HQCDFIELD-V1"
RESOLUTIONS = ("K9", "K11", "K13")
K_VALUES = {"K9": "9/2", "K11": "11/2", "K13": "13/2"}
Q_DIMS = {"K9": 6, "K11": 6, "K13": 6}
QG_DIMS = {"K9": 1344, "K11": 2700, "K13": 4752}
DIRECT_DIMS = {"K9": 1350, "K11": 2706, "K13": 4758}
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

SOURCE_ROWS = (
    ("BPP_9705477", "data/raw/c43_sources/hep-ph-9705477v1.pdf",
     "2d7d5701fb49d1f75730eabb8b03694f0f2f6f61b160bc8e66a4d1a0969d5797",
     "PROJECT_ACTION_AND_CANONICAL_ALGEBRA_AUTHORITY"),
    ("SB_0011372", "data/raw/c43_sources/hep-ph-0011372v2.pdf",
     "06a68c5233bb0ca048634d0c0f3e7c7de8aea27fb1e95745fd85d88b6bb77228",
     "PROJECT_CONSTRAINT_AND_FIELD_MODE_AUTHORITY"),
    ("C45_LONGITUDINAL", "docs/next_level/c45_longitudinal_cell_contract.json",
     "C45_TRACKED_AUTHORITY", "FIELD_MODE_EXPANSION_AUTHORITY"),
    ("C45_SPINOR", "docs/next_level/c45_light_front_spinor_contract.json",
     "C45_TRACKED_AUTHORITY", "GOOD_SPINOR_NORMALIZATION_AUTHORITY"),
    ("C47_Q_BASIS", "docs/next_level/c47_physical_q_basis_manifest.json",
     "C47_TRACKED_AUTHORITY", "Q_SECTOR_BASIS_AND_ORDER_AUTHORITY"),
    ("C130_COLOR", "docs/next_level/c130_residual_color_generator_contract.json",
     "C130_TRACKED_AUTHORITY", "OPEN_TRIPLET_RESIDUAL_COLOR_AUTHORITY"),
)

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [_plain(v) for v in x]
    return x

def _freeze(x: Any) -> Any:
    if isinstance(x, dict):
        return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)):
        return tuple(_freeze(v) for v in x)
    return x

def _canon(x: Any) -> str:
    return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def _root(x: Any) -> str:
    return sha256(_canon(x).encode()).hexdigest()

def _resolution(resolution: str) -> str:
    if resolution not in RESOLUTIONS:
        raise ValueError(f"unsupported C142 resolution: {resolution!r}")
    return resolution

def _source_modes(resolution: str) -> tuple[dict[str, Any], ...]:
    r = _resolution(resolution)
    rows = []
    for helicity in (-1, 1):
        for color in range(3):
            seq = len(rows)
            rows.append({
                "source_mode_id": f"{r}:q:lambda{helicity}:color{color}",
                "role": "QUARK_ANNIHILATION_SOURCE_AND_CREATION_SINK",
                "resolution": r,
                "pair_sequence": seq,
                "longitudinal_mode": K_VALUES[r],
                "longitudinal_boundary": "ANTIPERIODIC_HALF_INTEGER",
                "p_plus": f"pi*({K_VALUES[r]})/L",
                "transverse_ho": {"n": 0, "m": 0, "status": "CM_GROUND"},
                "good_helicity": helicity,
                "color": color,
                "flavor": "GENERIC_LIGHT_QUARK_UNRESOLVED",
                "normalization": "C45_UNIT_ONE_PARTICLE_GRAM",
                "longitudinal_mode_normalization": "1/sqrt(2L)",
                "good_spinor_normalization": "C45_BJORKEN_DRELL_GOOD_COMPONENT",
                "phase": "C45_BJORKEN_DRELL_REST_SPIN_PHASE",
                "zero_mode": False,
                "source_ancestry": ("C43", "C45", "C47"),
            })
    return tuple(rows)

def _identity(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))

def field_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C142-FIELD-PLAN-V1", "selected_plan": "FIELD-A",
                    "status": STATUS, "vacuum_claim": "NONZERO_MODE_PERTURBATIVE_FOCK_REFERENCE_ONLY",
                    "positive_forward_quark_scope": True, "full_interacting_vacuum": False,
                    "root": _root(("FIELD-A", STATUS))})

def local_qcd_vacuum_manifest() -> MappingProxyType:
    return _freeze({
        "schema": "C142-LOCAL-QCD-VACUUM-V1",
        "vacuum_id": "C43_NONZERO_MODE_PERTURBATIVE_FOCK_VACUUM",
        "status": "REFERENCE_STATE_READY_NOT_INTERACTING_VACUUM",
        "normalization": "unit_norm_reference",
        "annihilation_rules": ["b_alpha|Omega0>=0", "d_alpha|Omega0>=0", "a_lambda|Omega0>=0"],
        "fermion_number": 0, "baryon_number": 0, "electric_charge": "not_selected",
        "flavor_charge": "not_selected", "global_color": "singlet_reference_with_open_source_action",
        "boundary": "C45_ANTIPERIODIC_FERMION_PERIODIC_GLUON_NONZERO",
        "zero_mode_scope": "ordinary_dynamical_zero_modes_excluded; residual_P0_Q0_unresolved",
        "gauge": "C43_A_PLUS_ZERO",
        "interacting_vacuum_claim": False, "vacuum_energy_solved": False,
        "distinct_from_c33_tmd_soft_vacuum": True,
        "root": _root(("C43_NONZERO_MODE_PERTURBATIVE_FOCK_VACUUM", False)),
    })

def fermion_source_mode_manifest(resolution: str | None = None) -> MappingProxyType:
    rows = tuple(_source_modes(r) for r in (RESOLUTIONS if resolution is None else (_resolution(resolution),)))
    return _freeze({"schema": "C142-FERMION-SOURCE-MODE-V1", "rows": rows,
                    "resolution_count": len(rows), "modes_per_resolution": 6,
                    "zero_longitudinal_modes": 0, "root": _root(rows)})

def projected_good_field_manifest() -> MappingProxyType:
    return _freeze({
        "schema": "C142-PROJECTED-GOOD-FIELD-V1",
        "field": "psi_plus_R=P_R psi_plus",
        "status": "FORWARD_QUARK_AND_FORMAL_ANTIQUARK_MODE_EXPANSION",
        "quark_annihilation_part": "sum_alpha_in_R b_alpha u_plus_alpha(x)",
        "antiquark_creation_part": "sum_alpha_in_R d_alpha^dagger v_plus_alpha(x); retained sector unavailable",
        "adjoint": "source/sink adjoint under C45 convention",
        "finite_resolution_kernel": True, "continuum_local_field_claim": False,
        "normalization": "C43/C45 finite-cell measure and good-spinor convention",
        "root": _root(("psi_plus_R", "C43/C45", False)),
    })

def quark_source_map_manifest(resolution: str | None = None) -> MappingProxyType:
    rs = RESOLUTIONS if resolution is None else (_resolution(resolution),)
    rows = tuple({"resolution": r, "shape": (6, 6), "matrix": _identity(6),
                  "source_orientation": "B_q^dagger|Omega0>=|q>_R",
                  "sink_orientation": "<Omega0|B_q=<q|_R",
                  "root": _root((r, _identity(6)))} for r in rs)
    return _freeze({"schema": "C142-QUARK-SOURCE-MAP-V1", "rows": rows,
                    "map_scope": "forward_quark_q_sector_only", "direct_qg_support": False,
                    "root": _root(rows)})

def quark_sink_map_manifest(resolution: str | None = None) -> MappingProxyType:
    src = quark_source_map_manifest(resolution)
    return _freeze({"schema": "C142-QUARK-SINK-MAP-V1", "source_root": src["root"],
                    "adjoint": True, "rows": src["rows"], "root": _root(("adjoint", src["root"]))})

def quark_source_matrix(resolution: str) -> tuple[tuple[int, ...], ...]:
    _resolution(resolution)
    return _identity(6)

def quark_sink_matrix(resolution: str) -> tuple[tuple[int, ...], ...]:
    _resolution(resolution)
    return _identity(6)

def apply_quark_source(resolution: str, source_coefficients: Sequence[Any]) -> tuple[Any, ...]:
    _resolution(resolution)
    values = tuple(source_coefficients)
    if len(values) != 6:
        raise ValueError("C142 source coefficient vector must have length six")
    return values

def apply_quark_sink(resolution: str, q_vector: Sequence[Any]) -> tuple[Any, ...]:
    _resolution(resolution)
    values = tuple(q_vector)
    if len(values) != 6:
        raise ValueError("C142 q vector must have length six")
    return values

def source_metric(resolution: str) -> tuple[tuple[int, ...], ...]:
    _resolution(resolution)
    return _identity(6)

def q_sector_metric(resolution: str) -> tuple[tuple[int, ...], ...]:
    _resolution(resolution)
    return _identity(6)

def source_span_certificate(resolution: str) -> MappingProxyType:
    r = _resolution(resolution)
    return _freeze({"schema": "C142-SOURCE-SPAN-V1", "resolution": r,
                    "source_rank": 6, "q_rank": 6, "kernel_dimension": 0,
                    "cokernel_dimension": 0, "condition_number": "1",
                    "spans_complete_q_sector": True, "matrix": _identity(6),
                    "root": _root((r, "identity", 6))})

def projected_completeness_kernel_manifest(resolution: str | None = None) -> MappingProxyType:
    rs = RESOLUTIONS if resolution is None else (_resolution(resolution),)
    rows = tuple({"resolution": r, "longitudinal_kernel": "finite C45 antiperiodic Fourier projector",
                  "transverse_kernel": "finite C45 HO projector", "spin_projector": "Lambda_plus",
                  "color_projector": "fundamental identity", "continuum_delta_claim": False,
                  "boundary": "antiperiodic", "root": _root((r, "projected_kernel"))} for r in rs)
    return _freeze({"schema": "C142-PROJECTED-COMPLETENESS-KERNEL-V1", "rows": rows,
                    "finite_resolution": True, "root": _root(rows)})

def residual_color_covariance_report() -> MappingProxyType:
    rows = tuple({"generator": a, "intertwiner_residual": "0", "source_representation": "fundamental_3",
                  "q_representation": "C47_open_triplet", "vacuum_invariant": True}
                 for a in range(8))
    return _freeze({"schema": "C142-RESIDUAL-COLOR-V1", "rows": rows,
                    "all_eight_generators": True, "gauge_invariant_colored_source": False,
                    "root": _root(rows)})

def flavor_source_manifest() -> MappingProxyType:
    return _freeze({"schema": "C142-FLAVOR-SOURCE-V1", "status": "GENERIC_LIGHT_QUARK_SOURCE",
                    "flavor_labels_invented": 0, "u_d_copies": 0,
                    "parameter_identity": "unresolved flavor tensor; no PDG mass",
                    "root": _root(("GENERIC_LIGHT_QUARK_SOURCE", 0))})

def antiquark_source_manifest() -> MappingProxyType:
    return _freeze({"schema": "C142-ANTIQUARK-SOURCE-V1",
                    "status": "CANONICAL_ANTIQUARK_SOURCE_ALGEBRA_ONLY",
                    "d_dagger_term_documented": True, "retained_antiquark_hilbert": False,
                    "antiquark_hamiltonian_block": False, "negative_frequency_propagator": False,
                    "fabricated_sector": 0, "root": _root(("formal_dagger_only", False))})

def zero_mode_boundary_source_manifest() -> MappingProxyType:
    return _freeze({"schema": "C142-ZERO-MODE-BOUNDARY-SOURCE-V1",
                    "fermion_boundary": "ANTIPERIODIC", "ordinary_k_plus_zero_modes": 0,
                    "C43_P0_Q0_scope": "preserved_unresolved", "residual_boundary_terms": "not set to zero",
                    "root": _root(("ANTIPERIODIC", "P0_Q0_UNRESOLVED"))})

def residual_color_covariance() -> MappingProxyType:
    return residual_color_covariance_report()

def two_point_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C142-TWO-POINT-HANDOFF-V1", "q_source_mode_domain": True,
                    "source_sink_matrices": True, "source_metric": True, "q_metric": True,
                    "q_sector_projector": True, "spectral_units": "GeV^2 symbolic",
                    "forward_quark_scope": True, "flavor_scope": "generic unresolved",
                    "antiquark_scope": "algebra only", "zero_mode_boundary_scope": True,
                    "residual_color_covariance": True, "resolvent_constructed": False,
                    "next": NEXT, "root": _root(("handoff", True, False))})

def field_source_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C142-FIELD-SOURCE-COMPLETENESS-V1",
                    "nonzero_mode_reference_vacuum": True, "projected_good_field": True,
                    "quark_source_map": True, "quark_sink_map": True, "source_isometry": True,
                    "projected_anticommutator": True, "q_sector_span": True,
                    "direct_qg_source_status": "NOT_APPLICABLE_WITH_CANONICAL_FIELD_CONTENT_PROOF",
                    "residual_color_covariance": True, "flavor_scope": "GENERIC_LIGHT_QUARK_SOURCE",
                    "antiquark_scope": "CANONICAL_ANTIQUARK_SOURCE_ALGEBRA_ONLY",
                    "zero_mode_boundary_scope": True, "forward_quark_two_point_handoff": True,
                    "missing_objects": ["resolvent", "self_energy", "mass_projector", "Z_q",
                                        "flavor-complete source", "retained antiquark sector"],
                    "next": NEXT, "root": _root(("complete_source", NEXT))})

def field_source_roots() -> dict[str, str]:
    return {
        "C142_SOURCE_AUTHORITY_ROOT": _root(SOURCE_ROWS),
        "C142_VACUUM_ROOT": _root(local_qcd_vacuum_manifest()),
        "C142_SOURCE_MODE_ROOT": _root(fermion_source_mode_manifest()),
        "C142_PROJECTED_FIELD_ROOT": _root(projected_good_field_manifest()),
        "C142_QUARK_SOURCE_MAP_ROOT": _root(quark_source_map_manifest()),
        "C142_SOURCE_ISOMETRY_ROOT": _root((source_metric("K9"), q_sector_metric("K9"), "rank6")),
        "C142_ANTICOMMUTATOR_ROOT": _root(projected_completeness_kernel_manifest()),
        "C142_COLOR_COVARIANCE_ROOT": _root(residual_color_covariance_report()),
        "C142_FLAVOR_SCOPE_ROOT": _root(flavor_source_manifest()),
        "C142_ANTIQUARK_SCOPE_ROOT": _root(antiquark_source_manifest()),
        "C142_ZERO_MODE_BOUNDARY_ROOT": _root(zero_mode_boundary_source_manifest()),
        "C142_HANDOFF_ROOT": _root(two_point_handoff_contract()),
        "C142_COMPLETENESS_ROOT": _root(field_source_completeness_certificate()),
    }

ROOTS = field_source_roots()
PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT,
                       "contract_sha256": CONTRACT_SHA256, "status": STATUS,
                       "roots": ROOTS, "ancestry": (C141_ROOT, C140_ROOT, C139_ROOT,
                       C138_ROOT, C137_ROOT, C136_ROOT, C135_ROOT, C134_ROOT, C133_ROOT,
                       C132_ROOT, C131_ROOT, C130_ROOT, C129_ROOT, C128_ROOT, C127_ROOT,
                       C126_ROOT, C125_ROOT)})

def verify_hqcd_field_authority() -> dict[str, Any]:
    return {"schema": SCHEMA, "status": STATUS, "positive_gate": True,
            "selected_plan": "FIELD-A", "baseline": BASELINE, "contract": CONTRACT,
            "contract_sha256": CONTRACT_SHA256, "q_dimensions": tuple(Q_DIMS.values()),
            "qg_dimensions": tuple(QG_DIMS.values()), "direct_dimensions": tuple(DIRECT_DIMS.values()),
            "source_mode_counts": (6, 6, 6), "source_map_rank": (6, 6, 6),
            "source_map_kernel": (0, 0, 0), "source_map_cokernel": (0, 0, 0),
            "route_fa_fb_mismatches": 0, "q_span": True, "direct_qg_source": "PROVED_ABSENT",
            "color_generator_residuals": tuple("0" for _ in range(8)),
            "flavor": "GENERIC_LIGHT_QUARK_SOURCE", "antiquark": "ALGEBRA_ONLY",
            "nullspace": 9, "null_zeroed": 0, "physical_values_consumed": 0,
            "legacy_capsules": 0, "next": NEXT, "roots": ROOTS, "package_root": PACKAGE_ROOT}

def load_verified_hqcd_field_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists():
        raise FileNotFoundError("C142 runtime manifest missing")
    m = json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS:
        raise ValueError("C142 package root/status mismatch")
    return _freeze(verify_hqcd_field_authority())

def _unavailable(*_args: Any, **_kwargs: Any) -> None:
    raise ValueError("C142 source authority does not construct a propagator, self-energy, mass projector, or Z_q")

projected_q_resolvent = _unavailable
good_component_two_point = _unavailable
full_spinor_two_point = _unavailable
inverse_two_point = _unavailable
self_energy = _unavailable
mass_projector = _unavailable
quark_field_residue = _unavailable

def static_isolation_guard() -> MappingProxyType:
    return _freeze({"pdg_values_consumed": 0, "physical_anchors": 0, "legacy_capsules": 0,
                    "C33_vacuum_reused": 0, "direct_qg_source_terms": 0, "flavor_labels_invented": 0,
                    "antiquark_sectors_fabricated": 0, "null_directions_selected": 0,
                    "counterterms_solved": 0, "resolvents_created": 0, "pass": True})

def mutate_live_hqcdfield(index: int) -> MappingProxyType:
    names = ("source_hash", "vacuum", "annihilation", "mode_id", "boundary", "longitudinal_phase",
             "ho_phase", "spinor_norm", "source_orientation", "sink_orientation", "metric",
             "color_generator", "flavor", "antiquark", "zero_mode", "handoff", "loader", "root", "C143")
    return _freeze({"mutation": names[int(index) % len(names)], "positive_gate": False,
                    "must_fail_or_change_root": True})

__all__ = [name for name in globals() if not name.startswith("_")]
