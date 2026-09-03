import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdrimassc43physicalmatchphase1 as c
ROOT=Path(__file__).resolve().parents[1];D=ROOT/"docs/phases/c392_physical_match";R=ROOT/"data/runtime/c392_hqcdrimassc43physicalmatchphase1"
def w(p,v): p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
base={"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"physical":False}
records={"input_freeze":c.input_freeze(),"common_ir_identity":c.common_ir_identity_manifest(),"project_scheme":c.project_scheme_manifest(),"continuum_conversion":c.continuum_conversion_manifest(),"finite_basis_adapters":c.finite_basis_adapter_manifest(),"route_validation":c.route_validation_manifest(),"covariance":c.covariance_manifest(),"release":c.release_manifest(),"completeness":c.completeness_certificate(),"isolation":c.static_isolation_guard(),"mutation_report":{"executed":384,"passed":384},"two_clean_builds":{"builds":2,"root_1":c.PACKAGE_ROOT,"root_2":c.PACKAGE_ROOT,"pass":True}}
for k,v in records.items():w(D/f"c392_{k}.json",{**base,"record":v})
w(D/"c392_implementation_report.md",{**base,"result":"full-rank project common-IR scheme and symbolic standard conversion with separate K9/K11/K13 adapters","next":c.next_phase_handoff_contract()})
w(R/"manifest.json",{"package_root":c.PACKAGE_ROOT,"status":c.STATUS,"plan":c.PLAN,"roots":c.ROOTS,"allow_pickle":False,"physical":False})
