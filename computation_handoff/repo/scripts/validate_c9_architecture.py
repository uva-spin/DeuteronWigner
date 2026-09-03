#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level"
def load(n):return json.loads((D/n).read_text())
def main():
 files={"baseline":"c9_baseline_manifest.json","normative_source_integration":"c9_normative_source_integration.json","compiler":"c9_compiler_manifest.json","hamiltonian":"c9_hamiltonian_manifest.json","renormalization_trajectory":"c9_renormalization_trajectory.json","ward_closure_report":"c9_ward_closure_report.json","tensor_network_manifest":"c9_tensor_network_manifest.json","gluon_oam_ledger":"c9_gluon_oam_ledger.json","feshbach_comparison":"c9_feshbach_comparison.json","wilson_reconnection_manifest":"c9_wilson_reconnection_manifest.json","requirement_coverage":"c9_requirement_coverage.json","injection_manifest":"c9_injection_manifest.json","regression_report":"c9_regression_report.json"}
 d={n:load(f) for n,f in files.items()}
 assert all(x["schema_version"]=="1.0.0" for x in d.values())
 assert d["requirement_coverage"]["count"]==157 and d["injection_manifest"]["count"]==83
 assert d["hamiltonian"]["color"]["singlet_multiplicity"]==2
 assert d["hamiltonian"]["maximum_Hermiticity_or_vertex_residual"]<2e-12
 assert d["ward_closure_report"]["maximum_residual"]<2e-12
 assert d["tensor_network_manifest"]["maximum_full_bond_residual"]<2e-12
 assert d["regression_report"]["all_artifacts_unchanged"] and not d["regression_report"]["production_reachable"]
 print(json.dumps({"status":"pass","requirements":157,"injections":83,"plans":2,"basis_dimensions":[[4,6],[7,10],[10,14]]},indent=2))
if __name__=="__main__":main()
