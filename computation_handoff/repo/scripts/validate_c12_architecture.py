#!/usr/bin/env python3
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/"docs"/"next_level";L=lambda n:json.loads((D/n).read_text())
assert L("c12_normative_source_integration.json")["all_present"]
assert L("c12_spectral_support_manifest.json")["below_threshold"]==0
assert L("c12_cut_ledger.json")["residual"]<1e-14
assert L("c12_quark_antiquark_link_odd_manifest.json")["projectors_distinct"]
g=L("c12_gluon_fd_manifest.json");assert len(g["ordered_pairs"])==4 and g["fd_inner"]==0 and g["process_mixture"] is None
assert L("c12_soft_overlap_report.json")["one_subtraction_residual"]==0
assert L("c12_injection_manifest.json")["count"]>=120
r=L("c12_regression_report.json");assert r["production_registry"]==216 and r["all_artifacts_unchanged"] and not r["production_reachable"]
print("C12/H5 architecture manifests validated")
