#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
cap=L("c23_process_capability_matrix.json");reg=L("c23_regression_report.json");wy=L("c23_wy_matching_manifest.json");basis=L("c23_spin1_structure_function_basis.json")
assert cap["input_eligibility"]=={"analytic":438,"not_eligible":102,"physical":0,"source":0}
assert not cap["matched_total_executable"] and cap["nuclear_plan"]=="NN_ONLY"
assert basis["count"]==23 and not basis["inclusive_b1_executable"] and not basis["tagged_dis_executable"]
assert wy["rank_0_3_oracles_implemented"] and wy["executed_ranks"]==[0,2]
assert reg["production_registry"]==216 and reg["all_artifacts_unchanged"] and not reg["source_process_executed"] and not reg["physical_process_executed"] and not reg["production_reachable"]
assert hashlib.sha256((D/"c23_p0_codex_prompt.md").read_bytes()).hexdigest()=="5346947dd612813386a07ed1827a8ffd9540f03614862e135191eb0a105d4347"
print("C23/P0 analytic architecture manifests validated")
