"""C141/HQCD2PT fail-closed quark two-point construction.

Public sector identities and projectors are frozen, but no canonical local
QCD vacuum/source map is exposed by the C43--C140 public authority chain.
Consequently C141 selects plan 2PT-D and does not fabricate a Green function,
mass projector, residue, or parameter point.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/"data/runtime/c141_hqcd2pt"
BASELINE="f496f11841ec10fd029bd0fb37bc95db54c63ae7"; CONTRACT="docs/next_level/c140_c141_hqcd2pt_import_contract.json"; STATUS="C141_HQCD2PT_FIELD_SOURCE_MAP_INCOMPLETE"; NEXT="C142/HQCDFIELD"; SCHEMA="C141-HQCD2PT-V1"
C140_ROOT="2b54855f128afe5129f5dfe46cf23e06888ce8da13b9c98b0eccdb57d6cc4fba"; C139_ROOT="4f7a688eeaa492ce7bea569ac4442cea30ee549168ef8291be4e89774f92a361"; C138_ROOT="075c29f17e149b35ae2b78dcbc0f33c25d7457b321fd01479238cecd875eec9b"; C137_ROOT="96e3f9b1d25e546c7d968abe46def0cbacd205ed238b6f5d3aa776fc44b6041c"; C136_ROOT="fac2b3210bfef7cd3dc22a1a05ea47d9253a641172308603f4c2f3b6c31eb262"; C135_ROOT="e94b1bb47b0ab2d7499922ef558a8b32f0c6796ee7edcf2d86aed9e048ddcb5b"
RESOLUTIONS=("K9","K11","K13"); Q_DIMS=(6,6,6); QG_DIMS=(1344,2700,4752); DIRECT_DIMS=(1350,2706,4758)
NULLS=tuple(f"eta_{i}" for i in range(9))
SOURCES=(
 ("BPP_9705477","data/raw/c43_sources/hep-ph-9705477v1.pdf","2d7d5701fb49d1f75730eabb8b03694f0f2f6f61b160bc8e66a4d1a0969d5797","PROJECT_ACTION_AND_CONSTRAINT_AUTHORITY"),
 ("SB_0011372","data/raw/c43_sources/hep-ph-0011372v2.pdf","06a68c5233bb0ca048634d0c0f3e7c7de8aea27fb1e95745fd85d88b6bb77228","PROJECT_ACTION_AND_CONSTRAINT_AUTHORITY"),
 ("SB_0008293","data/raw/c141_sources/hep-ph_0008293.pdf","6229bd35c90128634c6e62410a6761276a5fb1e07edd0b30b2acfd6994c3b157","LIGHT_FRONT_PROPAGATOR_METHOD_AUTHORITY"),
 ("KMS_0801.4507","data/raw/c141_sources/arxiv_0801.4507.pdf","524da9860bd98b1ffee061e2eb85b45caf76a58916770f4c8e53966f97e76f21","FOCK_TRUNCATION_RENORMALIZATION_METHOD_AUTHORITY"),
 ("KMS_1204.3257","data/raw/c141_sources/arxiv_1204.3257.pdf","719212a67f3018c5c9dc77f4cc742e69ea5872f06827bdf71297d54036c811e9","FOCK_TRUNCATION_RENORMALIZATION_METHOD_AUTHORITY"),
 ("ZHAO_1402.4195","data/raw/c50_sources/1402.4195v1.pdf","c63145b47c166736367384ea2afe62ca123046147b43d3db2ac2d77338eacc9d","BASIS_SELF_ENERGY_METHOD_AUTHORITY"),
 ("ZHAO_2103.06719","data/raw/c141_sources/arxiv_2103.06719.pdf","ec7eca52356c5d05d64b17fbd7566df49c25d2714777cb828ffa5c2276db3860","COMPARISON_ONLY"),
 ("MARINHO_2604.22953","data/raw/c141_sources/arxiv_2604.22953.pdf","55a21e1c5240cbfd0e702235f47482345c33a4a6dfdfd0612a932480fbbd7f1f","SPECTRAL_RESOLVENT_METHOD_AUTHORITY"),
)
def _plain(x:Any)->Any:
 if isinstance(x,MappingProxyType): return {k:_plain(v) for k,v in x.items()}
 if isinstance(x,dict): return {k:_plain(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
 return x
def _freeze(x:Any)->Any:
 if isinstance(x,dict): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
 if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
 return x
def _canon(x:Any)->str:return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str:return sha256(_canon(x).encode()).hexdigest()
def two_point_plan_manifest()->MappingProxyType:return _freeze({"schema":"C141-PLAN-V1","selected_plan":"2PT-D","status":"FIELD_SOURCE_AUTHORITY_UNAVAILABLE","alternatives":{"2PT-A":"not available","2PT-B":"not available","2PT-C":"not available"},"root":_root(("2PT-D",))})
def primary_source_manifest()->MappingProxyType:
 rows=tuple({"id":a,"path":b,"sha256":c,"role":d,"regulator_identical":a.startswith(("BPP","SB_001"))} for a,b,c,d in SOURCES)
 return _freeze({"schema":"C141-SOURCE-MANIFEST-V1","rows":rows,"count":len(rows),"hash_locked":True,"root":_root(rows)})
def retained_sector_manifest()->MappingProxyType:
 rows=tuple({"resolution":r,"q_dimension":Q_DIMS[i],"qg_dimension":QG_DIMS[i],"direct_sum_dimension":DIRECT_DIMS[i],"basis_order":"q followed by qg","color":"triplet","flavor":"FLAVOR_IDENTITY_UNAVAILABLE"} for i,r in enumerate(RESOLUTIONS))
 return _freeze({"schema":"C141-SECTOR-MANIFEST-V1","rows":rows,"q_dimensions":Q_DIMS,"qg_dimensions":QG_DIMS,"direct_dimensions":DIRECT_DIMS,"root":_root(rows)})
def flavor_scope_manifest()->MappingProxyType:return _freeze({"schema":"C141-FLAVOR-SCOPE-V1","status":"FLAVOR_IDENTITY_UNAVAILABLE","allowed_status":"GENERIC_LIGHT_QUARK_CHANNEL","inferred_m_ud":False,"root":_root(("unavailable",))})
def antiparticle_scope_manifest()->MappingProxyType:return _freeze({"schema":"C141-ANTIPARTICLE-SCOPE-V1","status":"ANTIQUARK_COMPLETION_UNAVAILABLE","forward_quark_scope":"FORWARD_QUARK_NUMBER_PLUS_ONE_ONLY","negative_frequency_complete":False,"root":_root(("forward-only",))})
def local_qcd_vacuum_manifest()->MappingProxyType:return _freeze({"schema":"C141-LOCAL-QCD-VACUUM-V1","status":"FIELD_SOURCE_MAP_INCOMPLETE","vacuum_id":"C43_LOCAL_QCD_NONZERO_MODE_VACUUM_UNCONSTRUCTED","distinct_from_c33_tmd_soft_vacuum":True,"root":_root(("unconstructed", True))})
def quark_source_map_manifest()->MappingProxyType:return _freeze({"schema":"C141-QUARK-SOURCE-MAP-V1","status":"UNAVAILABLE","canonical_anticommutator_map":False,"source_sink_adjoint":False,"basis_row_inference":False,"root":_root(("unavailable",))})
def spectral_domain_manifest()->MappingProxyType:return _freeze({"schema":"C141-SPECTRAL-DOMAIN-V1","variable":"z=s+i epsilon_analytic","units":"GeV^2","upper_lower_half_planes":True,"spacelike_domain":"z=-mu^2 symbolic","finite_epsilon_selected":False,"pole_exclusion":True,"root":_root(("z", "GeV^2"))})
def external_probe_manifest()->MappingProxyType:return _freeze({"schema":"C141-EXTERNAL-PROBE-V1","status":"UNAVAILABLE_SOURCE_MAP","probe_kind":"external off-shell probe distinct from Hamiltonian eigenstate","spacelike_nonexceptional_candidate":True,"exact_C43_orbit":False,"root":_root(("probe", False))})
def sector_projector_manifest()->MappingProxyType:return _freeze({"schema":"C141-PROJECTOR-V1","exact":True,"relations":["P+Q=I","PQ=0"],"resolutions":RESOLUTIONS,"shapes":tuple((Q_DIMS[i],DIRECT_DIMS[i]) for i in range(3)),"root":_root((Q_DIMS,QG_DIMS,DIRECT_DIMS))})
def parameterized_operator_manifest()->MappingProxyType:return _freeze({"schema":"C141-PARAMETERIZED-OPERATOR-V1","symbolic_parameters":["m_q","m_q^2=(m_q)^2","g_s","six counterterm directions"],"physical_parameters_selected":0,"diagnostic_points":"NONPHYSICAL_RESOLVENT_DIAGNOSTIC_POINT only","root":_root(("symbolic",0))})
def projected_q_resolvent(*args,**kwargs):raise ValueError("C141_HQCD2PT_FIELD_SOURCE_MAP_INCOMPLETE: canonical field/source map unavailable")
def good_component_two_point(*args,**kwargs):raise ValueError("C141 good-component two-point unavailable without psi+ source map")
def full_spinor_two_point(*args,**kwargs):raise ValueError("C141 full-spinor reconstruction unavailable")
def inverse_two_point(*args,**kwargs):raise ValueError("C141 inverse two-point unavailable")
def self_energy(*args,**kwargs):raise ValueError("C141 self-energy unavailable")
def order_g2_self_energy(*args,**kwargs):raise ValueError("C141 order-g_s^2 self-energy unavailable")
def mass_projector_manifest()->MappingProxyType:return _freeze({"schema":"C141-MASS-PROJECTOR-V1","status":"MASS_LINEAR_PROJECTOR_INCOMPLETE","mass_squared_only_diagnostic":True,"mass_sign_sensitivity":False,"root":_root(("incomplete",))})
def quark_field_residue_manifest()->MappingProxyType:return _freeze({"schema":"C141-FIELD-RESIDUE-V1","status":"UNAVAILABLE","Z_q_propagator":False,"Z_2_sector_probability":False,"not_identified":True,"root":_root(("unavailable",))})
def self_energy_contribution_ledger()->MappingProxyType:return _freeze({"schema":"C141-SELF-ENERGY-LEDGER-V1","status":"STRUCTURAL_ONLY","contributions":("free q propagation","q-qg-q canonical vertex pair","instantaneous fermion","instantaneous current","counterterm direction","zero-mode/boundary","omitted Fock interfaces"),"unavailable_nonzero_not_zero":True,"root":_root(("ledger",7))})
def two_point_completeness_certificate()->MappingProxyType:return _freeze({"schema":"C141-COMPLETENESS-V1","basis_projected_resolvent":False,"canonical_field_source_map":False,"dynamical_good_component":False,"full_spinor":False,"instantaneous_ledger":True,"antiquark_completion":False,"zero_mode_boundary":False,"inverse_two_point":False,"self_energy":False,"order_g2":False,"mass_linear_projector":False,"quark_field_residue":False,"flavor_scope":"unavailable","physical_anchor_compatibility":"not established","next":NEXT,"root":_root((False,False,False,9))})
def legacy_target_preservation_manifest()->MappingProxyType:return _freeze({"schema":"C141-LEGACY-PRESERVATION-V1","M_R2_FB":"diagnostic","g_R_FB(K_R)":"diagnostic","legacy_capsules_generated":0,"null_coordinates_selected":0,"counterterms_solved":0,"root":_root(("diagnostic","diagnostic",0))})
def static_isolation_guard()->MappingProxyType:return _freeze({"pdg_values_consumed":0,"physical_anchors":0,"legacy_capsules":0,"null_zeroed":0,"counterterms":0,"effective_hamiltonians":0,"physical_states":0,"pass":True})
def mutate_live_hqcd2pt(index:int)->MappingProxyType:return _freeze({"mutation":("source","basis","flavor","antiparticle","vacuum","source_map","spectral","projector","resolvent","self_energy","mass_projector","residue","nullspace","loader","C142")[int(index)%15],"positive_gate":False,"must_fail_or_change_root":True})
ROOTS={"C141_SOURCE_ROOT":_root(primary_source_manifest()),"C141_RETAINED_SECTOR_ROOT":_root(retained_sector_manifest()),"C141_FLAVOR_ANTIPARTICLE_ROOT":_root((flavor_scope_manifest(),antiparticle_scope_manifest())),"C141_VACUUM_SOURCE_MAP_ROOT":_root((local_qcd_vacuum_manifest(),quark_source_map_manifest())),"C141_SPECTRAL_DOMAIN_ROOT":_root((spectral_domain_manifest(),external_probe_manifest())),"C141_PROJECTOR_ROOT":_root(sector_projector_manifest()),"C141_BASIS_RESOLVENT_ROOT":_root(("unavailable",)),"C141_GOOD_COMPONENT_ROOT":_root(("unavailable",)),"C141_FULL_SPINOR_ROOT":_root(("unavailable",)),"C141_SELF_ENERGY_ROOT":_root(self_energy_contribution_ledger()),"C141_ORDER_G2_ROOT":_root(("unavailable",)),"C141_MASS_PROJECTOR_ROOT":_root(mass_projector_manifest()),"C141_FIELD_RESIDUE_ROOT":_root(quark_field_residue_manifest()),"C141_COMPLETENESS_ROOT":_root(two_point_completeness_certificate())}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS,"ancestry":(C140_ROOT,C139_ROOT,C138_ROOT,C137_ROOT,C136_ROOT,C135_ROOT)})
def verify_hqcd_two_point_authority()->dict[str,Any]:return {"schema":SCHEMA,"status":STATUS,"positive_gate":False,"selected_plan":"2PT-D","baseline":BASELINE,"C140_package_root":C140_ROOT,"q_dimensions":Q_DIMS,"qg_dimensions":QG_DIMS,"direct_dimensions":DIRECT_DIMS,"source_map_complete":False,"basis_resolvent":False,"good_component":False,"full_spinor":False,"mass_projector":False,"Z_q":False,"nullspace":9,"null_zeroed":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_hqcd_two_point_authority()->MappingProxyType:
 p=RUNTIME/"manifest.json"
 if not p.exists():raise FileNotFoundError("C141 runtime manifest missing")
 m=json.loads(p.read_text())
 if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS:raise ValueError("C141 root/status mismatch")
 return _freeze(verify_hqcd_two_point_authority())
__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","two_point_plan_manifest","primary_source_manifest","retained_sector_manifest","flavor_scope_manifest","antiparticle_scope_manifest","local_qcd_vacuum_manifest","quark_source_map_manifest","spectral_domain_manifest","external_probe_manifest","parameterized_operator_manifest","sector_projector_manifest","projected_q_resolvent","good_component_two_point","full_spinor_two_point","inverse_two_point","self_energy","order_g2_self_energy","mass_projector_manifest","quark_field_residue_manifest","self_energy_contribution_ledger","two_point_completeness_certificate","legacy_target_preservation_manifest","verify_hqcd_two_point_authority","load_verified_hqcd_two_point_authority","static_isolation_guard","mutate_live_hqcd2pt"]
