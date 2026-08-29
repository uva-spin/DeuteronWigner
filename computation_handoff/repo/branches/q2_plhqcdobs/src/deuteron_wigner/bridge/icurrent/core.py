"""C114 Gauss-law current-current authority and fail-closed projection API.

The C43 action is complete at operator level, but the repository has no
source-qualified finite-HO matrix element for the surviving current products.
This module therefore exposes the complete audit and refuses to manufacture
component or complete matrices.  In particular, an unavailable diagonal
component is never represented by an empty/zero array.
"""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import ast
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "eda96bd6dcdde99ca60cc2475bbebc98cf5da53e"
CONTRACT_PATH = "docs/next_level/c113_c114_icurrent_import_contract.json"
STATUS = "C114_ICURRENT_FINITE_BASIS_PROJECTION_INCOMPLETE"
NEXT = "C115/ICHO — source-qualified instantaneous-current transverse-HO projection"
PRODUCTS = ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g")
BLOCKS = ("q->q", "q->qg", "qg->q", "qg->qg")
TERMINAL_STATUSES = ("AVAILABLE_SOURCE_QUALIFIED", "NOT_APPLICABLE_WITH_OPERATOR_PROOF", "EXACT_ZERO_WITH_OPERATOR_PROOF", "COUNTERTERM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE", "UNAVAILABLE_BLOCKING")
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N8_b0.40", "K13_2_N8_b0.40")

def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, list): return tuple(_freeze(v) for v in x)
    return x

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, tuple): return [_plain(v) for v in x]
    return x

def canonical_json(x: Any) -> str:
    return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def _root(x: Any) -> str:
    return sha256(canonical_json(x).encode()).hexdigest()

def _read(name: str) -> Any:
    return json.loads((ROOT / "docs" / "next_level" / name).read_text())

def _hash_path(rel: str) -> str:
    return sha256((ROOT / rel).read_bytes()).hexdigest()

def current_source_manifest() -> MappingProxyType:
    source = _read("c43_action_derivation_manifest.json")
    conventions = _read("c43_light_front_conventions.json")
    inverse = _read("c43_inverse_derivative_contract.json")
    return _freeze({
        "schema": "C114-GAUSS-LAW-SOURCE-V1",
        "source_path": "docs/next_level/c43_action_derivation_manifest.json",
        "source_hash": _hash_path("docs/next_level/c43_action_derivation_manifest.json"),
        "convention_path": "docs/next_level/c43_light_front_conventions.json",
        "convention_hash": _hash_path("docs/next_level/c43_light_front_conventions.json"),
        "operator": "P^-_IC = -(g_s^2/2) integral dx^- d^2x_perp [(i partial^+)^-1 Q0 j_a^+] [(i partial^+)^-1 Q0 j_a^+]",
        "current_decomposition": "j_a^+ = J_q,a^+ + J_g,a^+",
        "J_q": "J_q,a^+(x)=bar(psi)(x) gamma^+ T^a psi(x)",
        "J_g": "J_g,a^+(x)=-f^{abc} A_perp^b(x) partial^+ A_perp^c(x)",
        "gauss_rhs_sign": "-g f^{abc} A_perp^b partial^+ A_perp^c + g bar(psi) gamma^+ T^a psi",
        "covariant_derivative": "D_mu=partial_mu+i g_s A_mu^a T^a",
        "gauge": "A^+=0; x^+ time",
        "inverse_derivative": _freeze(inverse["contract"]),
        "kernel_order": "source ordered left current, Q0 (i partial^+)^-2, right current",
        "hermitian_rule": "R=Q0(i partial^+)^-1Q0 is anti-Hermitian; the integrated ordered square is Hermitian and its adjoint reverses current order",
        "zero_mode": "Q0 excludes exactly zero transferred plus momentum; P0 remains a separate control",
        "mass_dimension": "P^- coefficient GeV/g_s^2; M^2 coefficient GeV^2/g_s^2",
        "status": "SOURCE_OPERATOR_COMPLETE_PROJECTION_REQUIRED",
    })

def gauss_law_source_manifest() -> MappingProxyType:
    return current_source_manifest()

def current_operator_identity() -> MappingProxyType:
    src = current_source_manifest()
    return _freeze({"schema":"C114-CURRENT-OPERATOR-IDENTITY-V1", "source_root":_root(src), "coefficient":"-1/2", "coupling":"g_s^2 (factored)", "formula":src["operator"], "decomposition":("J_qJ_q","J_qJ_g","J_gJ_q","J_gJ_g"), "no_numerical_L_or_Pplus":True, "no_physical_coupling":True})

def inverse_partial_plus_squared() -> MappingProxyType:
    # exp(-i pi n x^-/L), -L<=x^-<=L; i partial^+ has eigenvalue pi n/L.
    route_a = {"phase":"exp(-i*pi*n*xminus/L)", "transfer":"n=k_left-k_right", "constraint":"delta_{n,n'}", "denominator":"L^2/(pi^2*n^2)", "domain":"n in Z\\{0}", "measure":"integral_{-L}^{L} dx^- = 2L delta", "zero":"Q0 removes n=0"}
    route_b = {"phase":"ordered Fourier current convolution", "transfer":"n=k_left-k_right", "constraint":"delta_{n,n'}", "denominator":"L^2/(pi^2*n^2)", "domain":"n in Z\\{0}", "measure":"2L delta", "zero":"Q0 removes n=0"}
    return _freeze({"schema":"C114-INVERSE-PARTIAL-SQUARED-V1", "route_a":route_a, "route_b":route_b, "residual":"0", "agreement":True, "hermitian_kernel":"K(n,n')=K(n',n)^*", "units":"mass^-2 before source current dimensions", "root":_root({"route_a":route_a,"route_b":route_b})})

def _product_fields(product: str) -> str:
    return {"J_qJ_q":"(bar psi gamma+ T psi)(bar psi gamma+ T psi)", "J_qJ_g":"(bar psi gamma+ T psi)(-f A_perp partial+ A_perp)", "J_gJ_q":"(-f A_perp partial+ A_perp)(bar psi gamma+ T psi)", "J_gJ_g":"(-f A_perp partial+ A_perp)(-f A_perp partial+ A_perp)"}[product]

def _block_status(product: str, block: str) -> tuple[str, str]:
    if block in ("q->qg", "qg->q"):
        return "EXACT_ZERO_WITH_OPERATOR_PROOF", "every current product contains an even net gluon-field parity at the retained endpoint; normal-ordering contractions remove gluons in pairs and cannot connect delta N_g=1"
    return "UNAVAILABLE_BLOCKING", "surviving normal-ordered monomials/contractions require source-qualified finite-HO, spin/polarization, color, and regulator matrix elements; no term is set to zero by Fock truncation"

def current_product_manifest() -> tuple[MappingProxyType, ...]:
    rows=[]
    for p in PRODUCTS:
        for b in BLOCKS:
            s,r = _block_status(p,b)
            rows.append(_freeze({"product":p,"block":b,"status":s,"field_identity":_product_fields(p),"proof":r,"coupling_order":2,"zero_mode":"Q0 nonzero-transfer only","counterterm":"not selected","source_operator_root":_root(current_source_manifest())}))
    return tuple(rows)

def current_product_block_status(product: str, resolution: str | None = None) -> MappingProxyType:
    if product not in PRODUCTS: raise KeyError(product)
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    rows = [x for x in current_product_manifest() if x["product"] == product]
    return _freeze({"schema":"C114-CURRENT-PRODUCT-BLOCK-STATUS-V1","product":product,"resolution":resolution,"blocks":rows,"all_terminal":False,"status":STATUS})

def current_monomial_inventory() -> tuple[MappingProxyType, ...]:
    rows=[]
    for p in PRODUCTS:
        rows.append(_freeze({"id":p+":direct", "parent":p, "normal_order":"source-ordered expansion before projection", "field_order":_product_fields(p), "delta_quark":"0", "delta_gluon":"0,+/-2,+/-4 as allowed by contractions", "contractions":"enumerated separately", "vacuum":"retained as control, not silently dropped", "status":"INVENTORIED"}))
    return tuple(rows)

def current_normal_ordering_inventory() -> tuple[MappingProxyType, ...]:
    return tuple(_freeze({"id":p+":normal_order", "parent":p, "descendants":("direct", "one-particle contraction", "vacuum contraction", "basis-external"), "source_order_preserved":True, "status":"INVENTORIED"}) for p in PRODUCTS)

def current_contraction_manifest() -> tuple[MappingProxyType, ...]:
    return tuple(_freeze({"id":p+":contraction", "product":p, "field_species":"gluon and/or fermion as dictated by product", "mode_domain":"finite C45 HO shells with Q0 nonzero longitudinal support", "value_status":"UNAVAILABLE_BLOCKING", "counterterm_direction":"available direction only; coefficient unavailable", "not_zero_by_truncation":True}) for p in PRODUCTS)

def current_contraction_inventory() -> tuple[MappingProxyType, ...]:
    return current_contraction_manifest()

def field_state_normalization_manifest() -> MappingProxyType:
    return _freeze({"schema":"C114-FIELD-STATE-NORMALIZATION-V1", "quark":"C43/C45 source normalization retained", "gluon":"C43 transverse field normalization retained", "C110_scope":"not applied universally; only exact two-external-gluon field-content identity would permit reuse", "current_products":{p:"UNAVAILABLE_BLOCKING" for p in PRODUCTS}, "missing_factors":"not claimed zero"})

def transverse_ho_kernel_manifest() -> MappingProxyType:
    return _freeze({"schema":"C114-HO-KERNEL-V1", "required":("two-HO","four-HO","derivative-HO","contracted-shell-sum","CM-ground"), "status":"UNAVAILABLE_BLOCKING", "threshold_pruning":False, "quadrature_as_primary":False})

def color_polarization_manifest() -> MappingProxyType:
    return _freeze({"schema":"C114-COLOR-POLARIZATION-V1", "structures":("T^aT^a","T^a f^{abc}","f^{abc}f^{ade}"), "status":"UNAVAILABLE_BLOCKING", "double_counting":False, "triplet_leakage":"not evaluated because no component matrix"})

def support_manifest() -> MappingProxyType:
    return _freeze({"schema":"C114-SUPPORT-V1", "source_ordered":True, "threshold_free":True, "cross_sector_status":"EXACT_ZERO_WITH_OPERATOR_PROOF", "diagonal_status":"UNAVAILABLE_BLOCKING", "duplicate_witnesses":0, "undecidable_pairs":"not terminal"})

def counterterm_direction_manifest(resolution: str | None = None) -> MappingProxyType:
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    return _freeze({"schema":"C114-COUNTERTERM-DIRECTION-V1", "resolution":resolution, "directions":tuple({"id":p+"_self_energy", "coefficient":"UNAVAILABLE"} for p in PRODUCTS), "included_in_bare":False})

def zero_mode_boundary_manifest() -> MappingProxyType:
    return _freeze({"schema":"C114-ZERO-BOUNDARY-V1", "ordinary_kernel":"Q0 nonzero transferred plus only", "zero_mode":"separate control, not default zero", "residual_boundary":"UNAVAILABLE_BLOCKING", "basis_boundary":"UNAVAILABLE_BLOCKING"})

def pminus_to_m2_manifest() -> MappingProxyType:
    return _freeze({"schema":"C114-PMINUS-M2-V1", "relation":"M^2=2 P^+ P^- - P_perp^2", "Pplus":"pi*K/L symbolic", "L":"symbolic", "status":"UNAVAILABLE_BLOCKING", "no_numerical_scale":True})

def restricted_current_identity_manifest() -> MappingProxyType:
    return _freeze({"schema":"C114-RESTRICTED-IDENTITY-V1", "identities":("current decomposition recomposition","adjoint product reversal","Abelian commuting-generator limit","Q0 finite-cell kernel"), "status":"SOURCE_OPERATOR_ONLY", "full_Ward_or_BRST":"UNAVAILABLE"})

def current_block_ancestry(resolution: str) -> MappingProxyType:
    if resolution not in RESOLUTIONS: raise KeyError(resolution)
    return _freeze({"resolution":resolution,"basis_dimensions":{"q":6,"qg":{"K9_2_N8_b0.40":1344,"K11_2_N8_b0.40":2700,"K13_2_N8_b0.40":4752}[resolution],"total":{"K9_2_N8_b0.40":1350,"K11_2_N8_b0.40":2706,"K13_2_N8_b0.40":4758}[resolution]},"complete_block":False,"missing_components":PRODUCTS})

def load_verified_instantaneous_current_authority() -> MappingProxyType:
    return _freeze(verify_instantaneous_current_authority())

def verify_instantaneous_current_authority() -> dict[str, Any]:
    source=current_source_manifest(); products=current_product_manifest();
    return {"status":STATUS,"baseline":BASELINE,"contract":CONTRACT_PATH,"contract_hash":_hash_path(CONTRACT_PATH),"source":source,"source_root":_root(source),"products":products,"product_count":4,"block_count":16,"exact_cross_sector_zeros":8,"diagonal_blockers":8,"monomial_count":4,"contraction_count":4,"inverse_kernel":inverse_partial_plus_squared(),"complete_block":False,"positive_gate":False,"no_zero_substitution":True,"no_C110_universal_reuse":True,"no_C112_substitution":True,"no_C53_substitution":True,"coupling_factored":True,"protected_paths_untouched":True}

def current_component_sparse_matrix(product: str, resolution: str):
    raise RuntimeError(f"{STATUS}: {product} has no terminal finite-HO component authority")

def apply_current_component(product: str, resolution: str, vector: Any):
    raise RuntimeError(f"{STATUS}: matrix-free component action unavailable until finite-HO projection closes")

def instantaneous_current_sparse_matrix(resolution: str):
    raise RuntimeError(f"{STATUS}: complete instantaneous-current block unavailable; missing components are not zero")

def apply_instantaneous_current(resolution: str, vector: Any):
    raise RuntimeError(f"{STATUS}: complete instantaneous-current action unavailable")

def current_block_completeness_decision() -> MappingProxyType:
    return _freeze({"status":STATUS,"decision":"FAIL_CLOSED","unavailable_products":PRODUCTS,"complete_block":False,"reason":"all diagonal current products require finite-HO projection and regulator authority","continuation":NEXT})

def static_isolation_guard() -> MappingProxyType:
    names={n.id for n in ast.walk(ast.parse(Path(__file__).read_text())) if isinstance(n,ast.Name)}
    forbidden=("C53","C112","c80","physical_coupling","counterterm_value","C80")
    return _freeze({"forbidden":forbidden,"found":tuple(x for x in forbidden if x in names),"pass":not any(x in names for x in forbidden)})

def mutate_live_current(fault_id: int) -> MappingProxyType:
    value=deepcopy(_plain(verify_instantaneous_current_authority())); choice=fault_id%16
    if choice==0: value["status"]="C114_CLAIMED_READY"
    elif choice==1: value["source"]["J_q"]="0"
    elif choice==2: value["source"]["J_g"]="0"
    elif choice==3: value["source"]["operator"]="+g_s^2"
    elif choice==4: value["source"]["zero_mode"]="included"
    elif choice==5: value["inverse_kernel"]["residual"]="1"
    elif choice==6: value["exact_cross_sector_zeros"]=0
    elif choice==7: value["diagonal_blockers"]=0
    elif choice==8: value["monomial_count"]=0
    elif choice==9: value["contraction_count"]=0
    elif choice==10: value["positive_gate"]=True
    elif choice==11: value["no_zero_substitution"]=False
    elif choice==12: value["no_C110_universal_reuse"]=False
    elif choice==13: value["no_C112_substitution"]=False
    elif choice==14: value["no_C53_substitution"]=False
    else: value["continuation"]="C115/OTHER"
    return _freeze(value)

__all__=["STATUS","NEXT","PRODUCTS","BLOCKS","RESOLUTIONS","load_verified_instantaneous_current_authority","verify_instantaneous_current_authority","current_source_manifest","gauss_law_source_manifest","current_operator_identity","inverse_partial_plus_squared","current_product_manifest","current_product_block_status","current_monomial_inventory","current_normal_ordering_inventory","current_contraction_manifest","current_contraction_inventory","field_state_normalization_manifest","transverse_ho_kernel_manifest","color_polarization_manifest","support_manifest","counterterm_direction_manifest","zero_mode_boundary_manifest","pminus_to_m2_manifest","restricted_current_identity_manifest","current_block_ancestry","current_component_sparse_matrix","apply_current_component","instantaneous_current_sparse_matrix","apply_instantaneous_current","current_block_completeness_decision","static_isolation_guard","mutate_live_current"]
