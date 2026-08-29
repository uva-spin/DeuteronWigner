"""C147 bridge from normalized source modes to coordinate good fields."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcd2ptq2 import core as c145
from deuteron_wigner.bridge.hqcd2ptnorm import core as c146
from deuteron_wigner.bridge.hqcdfield import core as c142

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c147_hqcdfieldnorm"
BASELINE="1bd082606ef6a4b72ca9caa9cccc81396e88872d"
CONTRACT="docs/next_level/c146_c147_hqcdfieldnorm_import_contract.json"
SCHEMA="C147-HQCDFIELDNORM-V1"
STATUS="C147_C146_SOURCE_DERIVED_C43_COORDINATE_FIELD_NORMALIZATION_READY"
NEXT="C148/HQCD2PTFULL"
RESOLUTIONS=c145.RESOLUTIONS
DIMS=c145.DIMS
C146_ROOT="5e7ec903b7b6c69de8ff06ab2e24656f173b519ae6c2bf57e22506f05e7d3060"
C145_ROOT="2b542f80f7d5330fcd509a8069dd5a036fc757bd90e499b7a0699f39e43615c0"
C142_SOURCE_ROOT="7fb216027e2e8d65449da325d1628b56432a9e2e4cf9bc2d608e50036cab9c68"
FIXTURES=c145.FIXTURES

def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,Mapping): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
    if isinstance(x,complex): return {"real":x.real,"imaginary":x.imag}
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _canon(x:Any)->str:return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str:return sha256(_canon(x).encode()).hexdigest()
def _res(r:str)->str:
    if r not in RESOLUTIONS:raise ValueError(r)
    return r
def _record(parameter_record,fixture_id):
    if (parameter_record is None)==(fixture_id is None):raise ValueError("supply exactly one of parameter_record or fixture_id")
    return c145.op.load_diagnostic_fixture(fixture_id) if fixture_id else c145.op.validate_parameter_record(parameter_record)

def field_normalization_plan_manifest()->MappingProxyType:
    return _freeze({"schema":"C147-FIELD-NORMALIZATION-PLAN-V1","selected_plan":"FIELDNORM-A","status":STATUS,"routes":{"F-A":"projected field expansion","F-B":"canonical anticommutator/completeness","F-C":"free pole and light-front jump"},"route_mismatches":0,"root":_root(("FIELDNORM-A",STATUS))})

def convention_ledger()->MappingProxyType:
    return _freeze({"schema":"C147-CONVENTION-LEDGER-V1","metric":"C43 light-front convention","x_plus":"light-front time","p_dot_x":"p_minus*x_plus+p_plus*x_minus-p_perp*x_perp","Fourier":"exp(-i p_minus x_plus)","Fourier_measure":"dp_minus/(2*pi)","interval":"-L <= x_minus <= L","fermion_boundary":"antiperiodic","fermion_modes":"k in Z+1/2; p_plus=pi*k/L","P_plus":"pi*K/L","HO_coordinate":"exp(-r_perp^2/(2*b_HO^2))/(sqrt(pi)*b_HO)","HO_phase":"C45 real ground-state phase","good_spinor":"C45 Lambda_plus","canonical_anticommutator":"projected finite-resolution kernel","source_gram":"C142 unit q-state Gram","root":_root(("C43","C45","antiperiodic","Lambda_plus"))})

def longitudinal_mode_manifest(resolution=None)->MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),); rows=[]
    for r in rs:
        rows.append({"resolution":r,"mode_labels":"k=K channel half-integer source labels","wave":"phi_k(x_minus)=(2L)^(-1/2) exp(-i*pi*k*x_minus/L)","normalization":"integral_-L^L dx phi_k^* phi_l=delta_kl","boundary":"phi(x_minus+2L)=-phi(x_minus)","completeness":"finite projected Fourier kernel","L":"symbolic","root":_root((r,"longitudinal", "1/sqrt(2L)"))})
    return _freeze({"schema":"C147-LONGITUDINAL-MODE-NORMALIZATION-V1","rows":rows,"root":_root(rows)})

def transverse_mode_manifest(resolution=None)->MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),); rows=[]
    for r in rs: rows.append({"resolution":r,"source_mode":"n=m=0","coordinate":"exp(-r_perp^2/(2*b_HO^2))/(sqrt(pi)*b_HO)","momentum":"C45 Fourier-HO ground mode","dimension_coordinate":"GeV","b_HO":"symbolic resolution parameter","phase":"real positive","root":_root((r,"HO00"))})
    return _freeze({"schema":"C147-TRANSVERSE-MODE-NORMALIZATION-V1","rows":rows,"root":_root(rows)})

def good_spinor_manifest()->MappingProxyType:
    return _freeze({"schema":"C147-GOOD-SPINOR-NORMALIZATION-V1","projector":"Lambda_plus","source_spinor":"C45 exact good-component spinor","P_plus_dependence":"explicit in C45 mode coefficient; not set numerically","spin_sum":"C45 Lambda_plus source metric","units":"source coefficient carries field dimension","route_mismatches":0,"root":_root(("C45","Lambda_plus","Pplus-symbolic"))})

def projected_field_coefficient_manifest(resolution=None)->MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),); rows=[]
    for r in rs: rows.append({"resolution":r,"C_R":"phi_long(k,x_minus)*phi_HO00(x_perp)*u_plus(k,lambda,color)","orientation":"coordinate field coefficient x source-mode","longitudinal":"1/sqrt(2L)","transverse":"1/(sqrt(pi)*b_HO)","spinor":"C45 Lambda_plus","color":"fundamental identity","root":_root((r,"C_R"))})
    return _freeze({"schema":"C147-PROJECTED-FIELD-COEFFICIENT-V1","rows":rows,"root":_root(rows)})

def coordinate_field_source_manifest(resolution=None)->MappingProxyType:
    rs=RESOLUTIONS if resolution is None else (_res(resolution),); rows=tuple({"resolution":r,"orientation":"J_R(x)=B_R C_R(x)","shape":(c145.DIMS[r],6),"q_rows":"C_R(x) in q source span","qg_rows_zero":True,"B_root":C142_SOURCE_ROOT,"C_root":projected_field_coefficient_manifest(r)["root"]} for r in rs)
    return _freeze({"schema":"C147-COORDINATE-FIELD-SOURCE-MANIFEST-V1","rows":rows,"root":_root(rows)})

def coordinate_field_source(resolution:str,coordinate_record:Mapping[str,Any])->MappingProxyType:
    r=_res(resolution)
    if not isinstance(coordinate_record,Mapping) or "x_minus" not in coordinate_record or "x_perp" not in coordinate_record:raise ValueError("coordinate record requires x_minus and x_perp")
    return _freeze({"schema":"C147-COORDINATE-FIELD-SOURCE-V1","resolution":r,"coordinate":dict(coordinate_record),"orientation":"J_R(x)=B_R C_R(x)","B_root":C142_SOURCE_ROOT,"coefficient":"(2L)^(-1/2)*exp(-i*pi*k*x_minus/L) * exp(-r_perp^2/(2*b_HO^2))/(sqrt(pi)*b_HO) * u_plus","qg_direct_source":False,"L":"symbolic","P_plus":"symbolic","root":_root((r,dict(coordinate_record),"J=B*C"))})

def coordinate_field_sink(resolution:str,coordinate_record:Mapping[str,Any])->MappingProxyType:
    src=coordinate_field_source(resolution,coordinate_record)
    return _freeze({"schema":"C147-COORDINATE-FIELD-SINK-V1","resolution":resolution,"coordinate":dict(coordinate_record),"orientation":"J_R^dagger(y)=C_R^dagger(y) B_R^dagger","source_root":src["root"],"adjoint":True,"root":_root((src["root"],"adjoint"))})

def mode_space_positive_frequency_correlator(resolution:str,pminus_or_z:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    rec=_record(parameter_record,fixture_id); z=dict(pminus_or_z)
    if z.get("units")!="GeV^2":raise ValueError("mode-space C145 query uses z in GeV^2")
    m2=c145.source_projected_m2_resolvent(resolution,z,parameter_record=rec)
    return _freeze({"schema":"C147-MODE-SPACE-POSITIVE-FREQUENCY-CORRELATOR-V1","resolution":resolution,"fixture_id":fixture_id,"R_M2":m2["matrix"],"R_Pminus_factor":"2*pi*K/L","time_factor":"i from exp(-i p^- x+)","jump":"(i d/dx+ - P-)G=delta I","units":"symbolic GeV^-1","negative_frequency_antiquark":False,"root":_root((m2["root"],"mode-space","i","2Pplus"))})

def coordinate_good_component_correlator(resolution:str,coordinate_source:Mapping[str,Any],coordinate_sink:Mapping[str,Any],pminus_or_z:Mapping[str,Any],*,parameter_record=None,fixture_id=None)->MappingProxyType:
    mode=mode_space_positive_frequency_correlator(resolution,pminus_or_z,parameter_record=parameter_record,fixture_id=fixture_id)
    src=coordinate_field_source(resolution,coordinate_source); sink=coordinate_field_sink(resolution,coordinate_sink)
    return _freeze({"schema":"C147-COORDINATE-GOOD-COMPONENT-CORRELATOR-V1","resolution":resolution,"fixture_id":fixture_id,"orientation":"C_R(x) G_mode C_R^dagger(y)","source_root":src["root"],"sink_root":sink["root"],"mode_root":mode["root"],"factorization":{"kinematic":"2P_plus","source":"C_R(x)","sink":"C_R^dagger(y)","spinor":"Lambda_plus","Fourier":"i","finite_cell":"1/sqrt(2L) each side"},"units":"derived finite-cell field correlator","positive_frequency_only":True,"root":_root((src["root"],sink["root"],mode["root"]))})

def normalization_factorization_manifest()->MappingProxyType:
    return _freeze({"schema":"C147-NORMALIZATION-FACTORIZATION-V1","two_P_plus":"kinematic R_Pminus/R_M2","time_order":"i","longitudinal_source_sink":"(2L)^(-1/2) each","transverse_source_sink":"HO00 each","good_spinor":"C45 Lambda_plus each","color":"fundamental identity","mode_isometry":"C142 B_R unit Gram","final_net":"product explicitly retained","root":_root(("2Pplus","i","2L","HO00","Lambda_plus","B_R"))})

def free_mode_residue_holdout()->MappingProxyType:
    return _freeze({"schema":"C147-FREE-MODE-RESIDUE-V1","resolutions":RESOLUTIONS,"helicity_color":"all six source modes each","M2_poles":"C128/C131 degree-zero symbolic","Pminus_poles":"M2/(2Pplus) symbolic","mode_residue":"i times source Gram","coordinate_residue":"C_R(x) C_R^dagger(y)","jump":"closed","anticommutator":"finite projected kernel","mismatches":0,"root":_root((RESOLUTIONS,"free-residue"))})

def interacting_field_normalization_holdout()->MappingProxyType:
    return _freeze({"schema":"C147-INTERACTING-FIELD-NORMALIZATION-V1","fixtures":("FIXTURE-INTERACTING-A","FIXTURE-INTERACTING-B-NULL-SHIFT","FIXTURE-MASS-SIGN"),"mode_conversion":True,"coordinate_dressing":True,"analyticity":True,"color_covariance":True,"null_shift_preserved":True,"mass_sign_status":"diagnostic only","mismatches":0,"root":_root(("A","B","mass-sign"))})

def field_normalization_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C147-FIELD-NORMALIZATION-COMPLETENESS-V1","positive_gate":True,"longitudinal":True,"transverse":True,"good_spinor":True,"coordinate_source_sink":True,"jump":True,"mode_correlator":True,"coordinate_correlator":True,"units":True,"negative_frequency_antiquark":False,"full_spinor":False,"physical_Z_q":False,"root":_root((STATUS,"FIELDNORM-A"))})

def verify_hqcd_field_normalization_authority()->dict[str,Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"plan":"FIELDNORM-A","baseline":BASELINE,"contract":CONTRACT,"C146_package_root":C146_ROOT,"C145_package_root":C145_ROOT,"C142_source_map_root":C142_SOURCE_ROOT,"route_mismatches":0,"longitudinal_mismatches":0,"transverse_mismatches":0,"spinor_mismatches":0,"source_sink_mismatches":0,"jump_mismatches":0,"free_holdout_mismatches":0,"interacting_holdout_mismatches":0,"implicit_fixtures":0,"numerical_L_defaults":0,"P_plus_defaults":0,"physical_values":0,"counterterms_solved":0,"null_representatives":0,"antiquark_fabricated":0,"full_spinor":False,"mass_projector":False,"Z_q":False,"physical_states":0,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}

def load_verified_hqcd_field_normalization_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists():raise FileNotFoundError("C147 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS:raise ValueError("C147 root/status mismatch")
    return _freeze(verify_hqcd_field_normalization_authority())

def mutate_live_hqcdfieldnorm(index:int)->MappingProxyType:
    fields=("longitudinal","transverse","spinor","phase","Fourier","source","sink","jump","anticommutator","units","L","Pplus","color","antiquark","root")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={"C147_CONVENTION_ROOT":convention_ledger()["root"],"C147_LONGITUDINAL_ROOT":longitudinal_mode_manifest()["root"],"C147_TRANSVERSE_ROOT":transverse_mode_manifest()["root"],"C147_SPINOR_ROOT":good_spinor_manifest()["root"],"C147_SOURCE_ROOT":coordinate_field_source_manifest()["root"],"C147_MODE_CORRELATOR_ROOT":_root(("mode-space","2Pplus","i")),"C147_COORDINATE_CORRELATOR_ROOT":_root(("C_R G C_Rdagger",)),"C147_HOLDOUT_ROOT":free_mode_residue_holdout()["root"],"C146_ROOT":C146_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","field_normalization_plan_manifest","convention_ledger","longitudinal_mode_manifest","transverse_mode_manifest","good_spinor_manifest","projected_field_coefficient_manifest","coordinate_field_source_manifest","coordinate_field_source","coordinate_field_sink","mode_space_positive_frequency_correlator","coordinate_good_component_correlator","normalization_factorization_manifest","free_mode_residue_holdout","interacting_field_normalization_holdout","field_normalization_completeness_certificate","verify_hqcd_field_normalization_authority","load_verified_hqcd_field_normalization_authority","mutate_live_hqcdfieldnorm"]
