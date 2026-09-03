#!/usr/bin/env python3
"""Freeze C101's current descendant domain before any C98/C100 import.

This module has an intentionally narrow import graph.  Grepping its imports
is part of the independence audit: it cannot reach historical public data.
"""
from hashlib import sha256
import json
from pathlib import Path

from deuteron_wigner.bridge.ifequiv6.core import compile_descendant_programs, current_descendant_inputs, sha

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/runtime/c101_ifequiv9"
ORDER = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
DROP_INSTANCE = {"current_source_commit", "historical_C72_runtime_instance", "normal_form", "semantic_ir"}

def canonical(value): return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
def digest(value): return sha256(canonical(value).encode()).hexdigest()

def normalize(program):
    value = json.loads(json.dumps(program))
    value["primitive_roots"] = {key: item for key, item in value["primitive_roots"].items() if key not in DROP_INSTANCE}
    value["normal_form_root"] = sha({key: item for key, item in value.items() if key != "normal_form_root"})
    return value

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    counts = {}; logical = {}; roots = {}; global_sequence = 0
    for resolution in ORDER:
        rolling = ""; count = total = 0
        for local, program in enumerate(compile_descendant_programs(resolution)):
            normalized = normalize(program)
            if program["pair"]["sequence"] != local: raise ValueError("descendant local pair order")
            rolling = digest({"previous": rolling, "global_sequence": global_sequence, "pair": normalized["pair"], "normal_form_root": normalized["normal_form_root"], "cardinality": normalized["cardinality"]})
            count += 1; total += normalized["cardinality"]; global_sequence += 1
        counts[resolution] = count; logical[resolution] = total; roots[resolution] = rolling
    body = {"schema":"C101-DESCENDANT-HISTORICAL-BLIND-FREEZE-V1","source_commit":"046244b6092c7f85e140fc5ea11c1a15a43b2577","descendant_inputs":dict(current_descendant_inputs()),"dropped_instance_keys":sorted(DROP_INSTANCE),"resolution_order":list(ORDER),"counts":counts,"logical_records":logical,"resolution_roots":roots,"pairs":global_sequence,"logical_total":sum(logical.values()),"historical_imports":False,"historical_expected_values":False}
    if counts != {"K9_2_N8_b0.40":16224,"K11_2_N10_b0.45":43350,"K13_2_N12_b0.50":95256} or sum(logical.values()) != 891992018: raise ValueError("descendant census")
    body["root"] = digest(body)
    temporary = OUT / "descendant_freeze.json.tmp"; temporary.write_text(canonical(body)+"\n"); temporary.replace(OUT / "descendant_freeze.json")
    print(body["root"])

if __name__ == "__main__": main()
