#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level"
def l(n):return json.loads((D/n).read_text())
def main():
 assert l("c10_requirement_coverage.json")["count"]==210
 assert l("c10_injection_manifest.json")["count"]==90
 assert l("c10_tolerance_manifest.json")["all_pass"]
 assert l("c10_pcac_closure_report.json")["maximum_residual"]<2e-12
 assert l("c10_tensor_network_manifest.json")["maximum_full_residual"]<2e-12
 assert l("c10_regression_report.json")["all_artifacts_unchanged"]
 assert all(not x["WILSON_READY"] and x["absorption"]==0 for x in l("c10_antiquark_wilson_handoff.json")["rows"])
 print(json.dumps({"status":"pass","requirements":210,"injections":90,"dimensions":[[4,6,9,9],[7,10,15,15],[10,14,21,21]]},indent=2))
if __name__=="__main__":main()
