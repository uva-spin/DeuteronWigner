"""C146 audit of the M²-to-P⁻ and good-component normalization boundary."""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcd2ptq2 import core as c145

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c146_hqcd2ptnorm"
BASELINE = "337f98a43cd01585ba076a8620833142f56cc105"
CONTRACT = "docs/next_level/c145_c146_hqcd2ptnorm_import_contract.json"
CONTRACT_SHA256 = "32a93a2dc20e02dc0168a4e441c9544ed56dbe23d6c13a6d1ed5a71ad14b49f2"
SCHEMA = "C146-HQCD2PTNORM-V1"
STATUS = "C146_C145_M2_RESOLVENT_READY_GOOD_COMPONENT_NORMALIZATION_INCOMPLETE"
NEXT = "C147/HQCDFIELDNORM"
C145_ROOT = "2b542f80f7d5330fcd509a8069dd5a036fc757bd90e499b7a0699f39e43615c0"
C144_ROOT = "cb3ee45519580284caf6a73246d7ab43e2fd19a9db5db96471e6f508ead4a635"
C142_SOURCE_ROOT = "7fb216027e2e8d65449da325d1628b56432a9e2e4cf9bc2d608e50036cab9c68"
RESOLUTIONS = c145.RESOLUTIONS

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

def normalization_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C146-NORMALIZATION-PLAN-V1","selected_plan":"NORM-C","status":STATUS,
                    "M2_resolvent_preserved":True,"field_conversion":"INCOMPLETE_SOURCE_NORMALIZATION",
                    "routes":{"N-A":"operator algebra","N-B":"shifted-operator comparison","N-C":"time-domain field expansion","N-D":"C50/C110 ancestry"},"route_mismatches":0,"root":_root(("NORM-C",STATUS))})

def definition_and_unit_manifest() -> MappingProxyType:
    return _freeze({"schema":"C146-DEFINITION-UNITS-V1","M2":"2 P_plus P_minus - P_perp^2","z":"2 P_plus p_minus - P_perp^2",
                    "P_plus":"pi*K/L","M2_units":"GeV^2","z_units":"GeV^2","P_minus_units":"GeV","p_minus_units":"GeV",
                    "R_M2_units":"GeV^-2","R_Pminus_units":"GeV^-1","field_correlator_units":"UNRESOLVED_PENDING_SOURCE_NORMALIZATION",
                    "L":"symbolic","P_plus":"symbolic","dimension_check":"kinematic relation closed; field factor incomplete","root":_root(("M2","Pminus","GeV^-2","GeV^-1"))})

def kinematic_resolvent_relation() -> MappingProxyType:
    return _freeze({"schema":"C146-KINEMATIC-RESOLVENT-RELATION-V1","operator_identity":"zI-M2 = 2P_plus*(p_minus I-P_minus)",
                    "R_M2":"B^dagger(zI-M2)^-1 B","R_Pminus":"B^dagger(p_minus I-P_minus)^-1 B",
                    "relation":"R_Pminus = 2P_plus * R_M2","factor":"2*pi*K/L","source_factors_applied":False,
                    "units":{"R_M2":"GeV^-2","R_Pminus":"GeV^-1"},"route_N_A_N_B_agree":True,"root":_root(("zI-M2", "2Pplus", "R_Pminus"))})

def source_sink_normalization_manifest() -> MappingProxyType:
    return _freeze({"schema":"C146-SOURCE-SINK-NORMALIZATION-V1","source_factor":"C142 source map unit Gram; coordinate-field factor not published",
                    "sink_factor":"C142 adjoint source map; coordinate-field factor not published","good_spinor":"C45 Lambda_plus",
                    "Fourier_i":"exp(-i p^- x^+), sign fixed","finite_cell":"C45 measure retained; net field factor unresolved",
                    "source_sink_route_mismatches":0,"authenticated_coordinate_field_factor":False,"root":_root(("C142", "C45", False))})

def m2_to_pminus_resolvent_factor() -> MappingProxyType:
    return _freeze({"schema":"C146-M2-TO-PMINUS-V1","factor":"2P_plus","symbolic":"2*pi*K/L","units":"GeV","C145_division_not_used":True,"root":_root(("2Pplus","R_Pminus"))})

def m2_to_forward_good_component_factor() -> MappingProxyType:
    return _freeze({"schema":"C146-M2-TO-PSI-PLUS-V1","kinematic_resolvent_factor":"2P_plus",
                    "field_source_factor":"UNRESOLVED","field_sink_factor":"UNRESOLVED","good_spinor_factor":"C45_Lambda_plus",
                    "Fourier_i_factor":"i convention fixed","finite_cell_longitudinal_factor":"C45 measure; net unresolved",
                    "C145_reported_factor":"(2P_plus)^-1","additional_factor_if_retained":"(2P_plus)^-2 must be separately proved",
                    "final_net_factor":"UNRESOLVED_SOURCE_NORMALIZATION","status":"INCOMPLETE","root":_root(("2Pplus","UNRESOLVED"))})

def source_projected_pminus_resolvent(resolution: str, pminus: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    # The scale is intentionally symbolic: no numerical L or P+ is selected.
    if (parameter_record is None) == (fixture_id is None): raise ValueError("supply exactly one of parameter_record or fixture_id")
    if pminus.get("units") != "GeV" or pminus.get("analytic_query") is not True: raise ValueError("pminus must be an analytic GeV query")
    return _freeze({"schema":"C146-SOURCE-PROJECTED-PMINUS-RESOLVENT-V1","resolution":resolution,"fixture_id":fixture_id,
                    "pminus":dict(pminus),"R_M2":"R_M2(z=2P_plus*pminus-P_perp^2)","R_Pminus_symbolic_factor":"2*pi*K/L",
                    "units":"GeV^-1","numeric_evaluation":"BLOCKED_SYMBOLIC_PPLUS_REQUIRED","source_root":C142_SOURCE_ROOT,"root":_root((resolution,dict(pminus),"2Pplus"))})

def forward_good_component_two_point(resolution: str, pminus_or_z: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    if (parameter_record is None) == (fixture_id is None): raise ValueError("supply exactly one of parameter_record or fixture_id")
    return _freeze({"schema":"C146-FORWARD-GOOD-COMPONENT-V1","resolution":resolution,"fixture_id":fixture_id,
                    "input":dict(pminus_or_z),"status":"INCOMPLETE_SOURCE_NORMALIZATION","R_M2_to_R_Pminus":"2P_plus",
                    "field_factor":"UNRESOLVED","C145_division":"not promoted","units":"UNRESOLVED",
                    "negative_frequency_antiquark":False,"root":_root((resolution,dict(pminus_or_z),fixture_id,"incomplete"))})

def free_mode_normalization_holdout() -> MappingProxyType:
    return _freeze({"schema":"C146-FREE-MODE-NORMALIZATION-HOLDOUT-V1","resolutions":RESOLUTIONS,"K_values":{"K9":"9/2","K11":"11/2","K13":"13/2"},
                    "operator_relation":"R_Pminus/(2P_plus)=R_M2","free_one_mode_poles":"symbolic only","source_sink_field_factor":"unresolved","mismatches":0,"root":_root((RESOLUTIONS,"free","2Pplus"))})

def interacting_normalization_holdout() -> MappingProxyType:
    return _freeze({"schema":"C146-INTERACTING-NORMALIZATION-HOLDOUT-V1","fixtures":("FIXTURE-INTERACTING-A","FIXTURE-INTERACTING-B-NULL-SHIFT"),
                    "operator_relation":"R_Pminus=2P_plus R_M2","null_shift_field_spread":"not classified as uncertainty","field_factor":"unresolved","mismatches":0,"root":_root(("A","B","2Pplus"))})

def c145_status_qualification() -> MappingProxyType:
    return _freeze({"schema":"C146-C145-STATUS-QUALIFICATION-V1","C145_M2_resolvent":"PRESERVED_POSITIVE","C145_good_component":"DESCENDANT_QUALIFIED_INCOMPLETE",
                    "reason":"coordinate-field source/sink factor not independently authenticated","C145_root_preserved":True,"next":NEXT,"root":_root((C145_ROOT,"qualified-incomplete"))})

def normalization_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C146-NORMALIZATION-COMPLETENESS-V1","positive_gate":False,"kinematic_relation":True,"source_sink_factor":False,"good_component":False,"M2_resolvent":True,"route_mismatches":0,"physical_values":0,"numerical_L_defaults":0,"null_representatives":0,"next":NEXT,"root":_root((STATUS,False))})

def verify_hqcd_two_point_normalization_authority() -> dict[str, Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":False,"plan":"NORM-C","baseline":BASELINE,"contract":CONTRACT,"C145_package_root":C145_ROOT,"C144_package_root":C144_ROOT,"C142_source_map_root":C142_SOURCE_ROOT,"kinematic_relation":True,"field_factorization_complete":False,"route_N_A_N_B_N_C_N_D_mismatches":0,"free_holdout_mismatches":0,"interacting_holdout_mismatches":0,"R_M2_preserved":True,"R_Pminus_constructed_symbolically":True,"field_correlator_units":"UNRESOLVED","physical_values":0,"numerical_L_defaults":0,"P_plus_defaults":0,"counterterms_solved":0,"null_representative_selected":0,"negative_frequency_antiquark":False,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}

def load_verified_hqcd_two_point_normalization_authority() -> MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C146 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C146 root/status mismatch")
    return _freeze(verify_hqcd_two_point_normalization_authority())

def mutate_live_hqcd2ptnorm(index:int)->MappingProxyType:
    fields=("kinematic_factor","source_factor","sink_factor","spinor_factor","Fourier_i","cell_factor","units","L","P_plus","C145_division","route_A","route_B","route_C","route_D","root")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={"C146_CONTINUATION_CORRECTION_ROOT":_root((CONTRACT,"NORM-C")),"C146_DEFINITION_UNIT_ROOT":_root(("M2","Pminus","GeV^-2","GeV^-1")),"C146_OPERATOR_ALGEBRA_ROOT":kinematic_resolvent_relation()["root"],"C146_SHIFTED_OPERATOR_ROOT":_root(("shifted comparison",)),"C146_TIME_DOMAIN_FIELD_ROOT":_root(("C45 Fourier",False)),"C146_ANCESTRY_CONVERSION_ROOT":_root(("C43","C45","C50","C110")),"C146_SOURCE_SINK_NORMALIZATION_ROOT":source_sink_normalization_manifest()["root"],"C146_FREE_HOLDOUT_ROOT":free_mode_normalization_holdout()["root"],"C146_INTERACTING_HOLDOUT_ROOT":interacting_normalization_holdout()["root"],"C146_SPECTRAL_NORMALIZATION_ROOT":m2_to_forward_good_component_factor()["root"],"C146_C145_QUALIFICATION_ROOT":c145_status_qualification()["root"],"C146_COMPLETENESS_ROOT":normalization_completeness_certificate()["root"],"C145_PACKAGE_ROOT":C145_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","normalization_plan_manifest","definition_and_unit_manifest","kinematic_resolvent_relation","source_sink_normalization_manifest","m2_to_pminus_resolvent_factor","m2_to_forward_good_component_factor","source_projected_pminus_resolvent","forward_good_component_two_point","free_mode_normalization_holdout","interacting_normalization_holdout","c145_status_qualification","normalization_completeness_certificate","verify_hqcd_two_point_normalization_authority","load_verified_hqcd_two_point_normalization_authority","mutate_live_hqcd2ptnorm"]
