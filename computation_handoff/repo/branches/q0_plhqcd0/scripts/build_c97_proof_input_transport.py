#!/usr/bin/env python3
from pathlib import Path
from deuteron_wigner.bridge.ifproofinput.proof_input_index import build
from deuteron_wigner.bridge.ifproofinput.zran_runtime import compile_adapter,build_persistent_zran_index
ROOT=Path(__file__).resolve().parents[1];CAP=ROOT/"data/runtime/c97_ifproofinput/capsule";OUT=ROOT/"data/runtime/c97_ifproofinput/proof_transport"
for resolution in ("K9_2_N8_b0.40","K11_2_N10_b0.45","K13_2_N12_b0.50"):
    OUT.mkdir(parents=True,exist_ok=True);adapter=OUT/"c97_zran";compile_adapter(adapter);source=CAP/f"route_b_indexed_{resolution}.jsonl.gz";z=build_persistent_zran_index(source,OUT/f"{resolution}.zran",adapter,span=1<<20);print(resolution,build(source,OUT/f"{resolution}.index",z)["root"])
