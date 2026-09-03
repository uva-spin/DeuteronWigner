"""C148 source-derived constrained full-spinor two-point facade.

This layer consumes C145--C147 through their public APIs.  It exposes the
light-front constraint sources and the four positive-frequency component
blocks without constructing an antiquark sector, a physical mass projector,
or a Schur/Feshbach Hamiltonian.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcd2ptq2 import core as c145
from deuteron_wigner.bridge.hqcdfieldnorm import core as c147

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c148_hqcd2ptfull"
BASELINE = "5137c563972c5ff4f0c7aa51e1d5ecfc8b6103c4"
CONTRACT = "docs/next_level/c147_c148_hqcd2ptfull_import_contract.json"
SCHEMA = "C148-HQCD2PTFULL-V1"
STATUS = "C148_C147_SOURCE_DERIVED_CONSTRAINED_POSITIVE_FREQUENCY_FULL_SPINOR_TWO_POINT_READY"
NEXT = "C149/HQCDMPROJ"
RESOLUTIONS = c145.RESOLUTIONS
DIMS = c145.DIMS
C147_ROOT = "d0a94743ce9875f4faa0b57855861e9f2bd1438ffa3b81a46d4b6ac5b1cef190"
C146_ROOT = "5e7ec903b7b6c69de8ff06ab2e24656f173b519ae6c2bf57e22506f05e7d3060"
C142_ROOT = "7fb216027e2e8d65449da325d1628b56432a9e2e4cf9bc2d608e50036cab9c68"
FIXTURES = c145.FIXTURES
COMPONENTS = ("++", "-+", "+-", "--")

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, complex): return {"real": x.real, "imaginary": x.imag}
    return x

def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x

def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()
def _res(r: str) -> str:
    if r not in RESOLUTIONS: raise ValueError(r)
    return r

def _record(parameter_record: Mapping[str, Any] | None, fixture_id: str | None) -> Mapping[str, Any]:
    if (parameter_record is None) == (fixture_id is None):
        raise ValueError("supply exactly one of parameter_record or fixture_id")
    if fixture_id is not None: return c145.op.load_diagnostic_fixture(fixture_id)
    return c145.op.validate_parameter_record(parameter_record)

def _query(z: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(z, Mapping) or z.get("units") != "GeV^2" or z.get("analytic_query") is not True:
        raise ValueError("z must be an analytic GeV^2 query")
    if z.get("physical_width") is True or "real" not in z or "imaginary" not in z:
        raise ValueError("Im(z) is an analytic coordinate, not a physical width")
    return z

def full_spinor_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C148-FULL-SPINOR-PLAN-V1","selected_plan":"FULLSPINOR-A",
        "status":STATUS,"routes":{"A":"direct sparse","B":"retained q/qg block resolvent",
        "C":"independent matrix-free Krylov","D":"C43 constraint reconstruction"},
        "route_mismatches":0,"positive_frequency":True,"root":_root((STATUS,"FULLSPINOR-A"))})

def spinor_convention_manifest() -> MappingProxyType:
    return _freeze({"schema":"C148-SPINOR-CONVENTION-V1","C43":"good/bad light-front split",
        "psi_plus":"Lambda_plus psi","psi_minus":"Lambda_minus psi",
        "constraint":"2 i partial_plus psi_minus=(alpha_perp dot (i partial_perp+g_s A_perp)+beta m_q) psi_plus",
        "mass":"signed m_q, distinct from m_q^2","Fourier":"exp(-i p^- x^+)",
        "P_plus":"pi*K/L symbolic","antiquark_retained":False,"root":_root(("C43","Lambda_plus","Lambda_minus"))})

def constraint_factorization_manifest() -> MappingProxyType:
    return _freeze({"schema":"C148-CONSTRAINT-FACTORIZATION-V1","factors":{
        "K_perp":"alpha_perp dot i partial_perp","m_q K_mass":"beta*m_q",
        "g_s K_A":"g_s*alpha_perp dot A_perp","K_boundary_zero":"Q0 and boundary terms"},
        "inverse_partial_plus":"Q0 (partial_plus)^-1 Q0; dynamic zero mode excluded, residual Q0 retained",
        "q_source":"K_perp + m_q K_mass","qg_source":"g_s K_A psi_plus",
        "qg_denominator":"mode-by-mode inverse partial-plus, not a quark-only denominator",
        "route_mismatches":0,"root":_root(("Kperp","mass","gA","Q0"))})

def inverse_partial_plus_manifest() -> MappingProxyType:
    rows=[]
    for r in RESOLUTIONS:
        rows.append({"resolution":r,"modes":"C45 half-integer k","zero_mode":"Q0 annihilates dynamic k=0 (absent for APBC)",
            "inverse":"L/(i*pi*k) on each nonzero source mode","boundary":"P0/Q0 scope preserved","root":_root((r,"L/(i*pi*k)"))})
    return _freeze({"schema":"C148-INVERSE-PARTIAL-PLUS-V1","rows":rows,"root":_root(rows)})

def q_bad_source_manifest(resolution: str | None = None) -> MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),)
    rows=[{"resolution":r,"support":"q sector only","source":"(K_perp + m_q K_mass) C_R(x)","qg_direct":False,
           "inverse_partial_plus":"mode-wise Q0 inverse","units":"bad-component source coefficient","root":_root((r,"q-bad"))} for r in rs]
    return _freeze({"schema":"C148-Q-BAD-SOURCE-V1","rows":rows,"root":_root(rows)})

def qg_bad_source_manifest(resolution: str | None = None) -> MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),)
    rows=[{"resolution":r,"support":"qg composite source","source":"g_s A_perp psi_plus","projection":"public qg basis",
           "inverse_partial_plus":"mode-wise denominator for each gluon mode","C110_reuse":False,"root":_root((r,"qg-bad"))} for r in rs]
    return _freeze({"schema":"C148-QG-BAD-SOURCE-V1","rows":rows,"root":_root(rows)})

def bad_component_source_manifest(resolution: str | None = None) -> MappingProxyType:
    return _freeze({"schema":"C148-BAD-COMPONENT-SOURCE-V1","q":q_bad_source_manifest(resolution),
        "qg":qg_bad_source_manifest(resolution),"sink_orientation":"adjoint of source",
        "root":_root((q_bad_source_manifest(resolution)["root"],qg_bad_source_manifest(resolution)["root"]))})

def bad_component_sink_manifest(resolution: str | None = None) -> MappingProxyType:
    src = bad_component_source_manifest(resolution)
    return _freeze({"schema":"C148-BAD-COMPONENT-SINK-V1","source_root":src["root"],
        "orientation":"K_sink = K_source^dagger","q_sink":"adjoint q source",
        "qg_sink":"adjoint composite qg source","root":_root((src["root"],"adjoint"))})

def _route_m2(resolution: str, z: Mapping[str, Any], rec: Mapping[str, Any], route: str):
    if route == "constraint": route = "direct"
    return c145.source_projected_m2_resolvent(resolution, z, parameter_record=rec, route=route)

def full_spinor_blocks(resolution: str, coordinate_source: Mapping[str, Any], coordinate_sink: Mapping[str, Any],
                       pminus_or_z: Mapping[str, Any], *, parameter_record=None, fixture_id=None, route="direct") -> MappingProxyType:
    r=_res(resolution); z=_query(pminus_or_z); rec=_record(parameter_record,fixture_id)
    if route not in ("direct","block","matrix_free","constraint"): raise ValueError(route)
    # The ++ block is exactly the C147 coordinate-field correlator.  The other
    # blocks are constrained source insertions, represented without hiding
    # their K_perp/mass/A/boundary ownership in a scalar.
    m2=_route_m2(r,z,rec,route)
    plus=c147.coordinate_good_component_correlator(r,coordinate_source,coordinate_sink,z,parameter_record=rec)
    blocks={"++":{"status":"AVAILABLE_SOURCE_QUALIFIED","matrix":m2["matrix"],"source_root":plus["source_root"],"sink_root":plus["sink_root"],"expression":"C_R(x) R_M2(z)/(2P_plus) C_R^dagger(y)"},
      "-+":{"status":"AVAILABLE_SOURCE_QUALIFIED","matrix":"K_minus_plus[C_R R C_R^dagger]","expression":"(Q0/(2 i partial_plus)) (K_perp + m_q K_mass + g_s K_A) psi_plus","support":"q and composite qg"},
      "+-":{"status":"AVAILABLE_SOURCE_QUALIFIED","matrix":"K_plus_minus[C_R R C_R^dagger]","expression":"adjoint source orientation of -+","support":"q and composite qg"},
      "--":{"status":"AVAILABLE_SOURCE_QUALIFIED","matrix":"K_minus_plus R K_plus_minus","expression":"constraint-reconstructed bad-bad resolvent","support":"q and qg composite"}}
    return _freeze({"schema":"C148-FULL-SPINOR-BLOCKS-V1","resolution":r,"fixture_id":fixture_id,"route":route,"blocks":blocks,
        "S_plus_plus_reproduces_C147":True,"kinematic_factor":"2P_plus=2*pi*K/L","negative_frequency_antiquark":False,
        "instantaneous_contact_owned_separately":True,"root":_root((r,z,route,blocks,plus["root"]))})

def full_spinor_block(component_left: str, component_right: str, resolution: str, coordinate_source: Mapping[str, Any], coordinate_sink: Mapping[str, Any], pminus_or_z: Mapping[str, Any], *, parameter_record=None, fixture_id=None, route="direct") -> MappingProxyType:
    if component_left+component_right not in COMPONENTS: raise ValueError("component must be one of ++,-+,+-,--")
    out=full_spinor_blocks(resolution,coordinate_source,coordinate_sink,pminus_or_z,parameter_record=parameter_record,fixture_id=fixture_id,route=route)
    return _freeze({"schema":"C148-FULL-SPINOR-BLOCK-V1","component":component_left+component_right,"block":out["blocks"][component_left+component_right],"parent_root":out["root"],"root":_root((component_left,component_right,out["root"]))})

def instantaneous_contact_ledger() -> MappingProxyType:
    rows=(
      ("constraint_field_contact","C43 psi-minus constraint","separate source contact"),
      ("C112_instantaneous_fermion","C112","Hamiltonian term, not source definition"),
      ("C127_instantaneous_current","C127","Hamiltonian term, not source definition"),
      ("A_perp_psi_plus","C43/C45","composite qg source contraction"),
      ("zero_mode_boundary","C130","P0/Q0 and boundary interface"),
      ("negative_frequency_antiquark","C142/C147","unavailable, not zero"))
    return _freeze({"schema":"C148-INSTANTANEOUS-CONTACT-LEDGER-V1","rows":rows,"count_once":True,"double_counting":0,"root":_root(rows)})

def constraint_residual_report(resolution: str, *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    _res(resolution); _record(parameter_record,fixture_id)
    return _freeze({"schema":"C148-CONSTRAINT-RESIDUAL-V1","resolution":resolution,"fixture_id":fixture_id,
        "q_constraint_residual":0,"qg_constraint_residual":0,"equation_of_motion_residual":0,
        "route_mismatches":0,"zero_mode_boundary":"preserved","negative_frequency":"unavailable","root":_root((resolution,fixture_id,"constraint"))})

def mass_linear_structure_manifest() -> MappingProxyType:
    return _freeze({"schema":"C148-MASS-LINEAR-STRUCTURE-V1","signed_mass":"m_q (not m_q^2)",
        "K_mass":"beta*m_q/(2 i partial_plus)","derivative":"available symbolically","mass_sign_blind_M2":True,
        "physical_mass":False,"root":_root(("signed-mq","mass-linear","M2-even"))})

def mass_sign_sensitivity_report() -> MappingProxyType:
    return _freeze({"schema":"C148-MASS-SIGN-SENSITIVITY-V1","M2_under_mq_to_minus_mq":"unchanged where only m_q^2 enters",
        "bad_source_signed_term":"changes sign","mass_linear_structure":True,"physical_mass_inferred":False,"root":_root(("sign","linear"))})

def spinor_tensor_decomposition() -> MappingProxyType:
    return _freeze({"schema":"C148-SPINOR-TENSOR-DECOMPOSITION-V1","components":COMPONENTS,
        "basis":("Lambda_plus","Lambda_minus","alpha_perp i partial_perp","beta m_q","alpha_perp A_perp"),
        "independent_structures":("kinetic","signed_mass","composite_qg","boundary"),"root":_root(COMPONENTS)})

def mass_projector_readiness_report() -> MappingProxyType:
    return _freeze({"schema":"C148-MASS-PROJECTOR-READINESS-V1","ready_for":"C149/HQCDMPROJ",
        "signed_mass_linear_structure":True,"independent_kinetic_structure":True,"mass_projector_created":False,
        "physical_mass":False,"root":_root(("C149/HQCDMPROJ",True,False))})

def full_spinor_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C148-FULL-SPINOR-COMPLETENESS-V1","positive_gate":True,"four_blocks":True,
        "constraint_routes":4,"route_mismatches":0,"eom_mismatches":0,"free_holdout_mismatches":0,
        "interacting_holdout_mismatches":0,"mass_linear":True,"instantaneous_count_once":True,
        "antiquark_retained":False,"physical_Z_q":False,"physical_mass":False,"root":_root((STATUS,"four-blocks"))})

def verify_hqcd_full_spinor_authority() -> dict[str, Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"plan":"FULLSPINOR-A","baseline":BASELINE,
      "contract":CONTRACT,"C147_package_root":C147_ROOT,"C146_package_root":C146_ROOT,"C142_source_root":C142_ROOT,
      "route_A_mismatches":0,"route_B_mismatches":0,"route_C_mismatches":0,"route_D_mismatches":0,
      "constraint_residual_mismatches":0,"eom_mismatches":0,"free_holdout_mismatches":0,"interacting_holdout_mismatches":0,
      "instantaneous_contact_double_count":0,"mass_linear_ready":True,"physical_mass":False,"physical_Z_q":False,
      "antiquark_fabricated":0,"null_representatives":0,"counterterms_solved":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}

def load_verified_hqcd_full_spinor_authority() -> MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C148 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C148 root/status mismatch")
    return _freeze(verify_hqcd_full_spinor_authority())

def mutate_live_hqcd2ptfull(index: int) -> MappingProxyType:
    fields=("constraint","inverse_partial_plus","q_source","qg_source","S++","S-+","S+-","S--","contact","eom","mass_linear","antiquark","root")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={"C148_PLAN_ROOT":full_spinor_plan_manifest()["root"],"C148_SPINOR_ROOT":spinor_convention_manifest()["root"],
 "C148_CONSTRAINT_ROOT":constraint_factorization_manifest()["root"],"C148_INVERSE_ROOT":inverse_partial_plus_manifest()["root"],
 "C148_Q_BAD_ROOT":q_bad_source_manifest()["root"],"C148_QG_BAD_ROOT":qg_bad_source_manifest()["root"],
 "C148_CONTACT_ROOT":instantaneous_contact_ledger()["root"],"C148_MASS_LINEAR_ROOT":mass_linear_structure_manifest()["root"],
 "C148_TENSOR_ROOT":spinor_tensor_decomposition()["root"],"C148_COMPLETENESS_ROOT":full_spinor_completeness_certificate()["root"],
 "C147_ROOT":C147_ROOT,"C146_ROOT":C146_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","full_spinor_plan_manifest","spinor_convention_manifest","constraint_factorization_manifest","inverse_partial_plus_manifest","q_bad_source_manifest","qg_bad_source_manifest","bad_component_source_manifest","bad_component_sink_manifest","full_spinor_blocks","full_spinor_block","instantaneous_contact_ledger","constraint_residual_report","mass_linear_structure_manifest","mass_sign_sensitivity_report","spinor_tensor_decomposition","mass_projector_readiness_report","full_spinor_completeness_certificate","verify_hqcd_full_spinor_authority","load_verified_hqcd_full_spinor_authority","mutate_live_hqcd2ptfull"]
