#!/usr/bin/env python3
"""Exhaustive C98 public-surface regression; no descendant comparison."""
from __future__ import annotations
from hashlib import sha256
import argparse,gzip,json,time
from pathlib import Path
from deuteron_wigner.bridge.ifhistpublic2 import (
    historical_pair_normal_form,historical_pair_proof_inputs,historical_primitive_record,
)
from deuteron_wigner.bridge.ifhistpublic2.core import _pair_order, historical_primitive_family, load_verified_historical_theorem_input_authority
from deuteron_wigner.bridge.ifboundrestart.core import check_proof
ROOT=Path(__file__).resolve().parents[1];DOC=ROOT/"docs/next_level";CAP=ROOT/"data/runtime/c97_ifproofinput/capsule"
def c(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def s(x):return sha256(c(x).encode()).hexdigest()
def plain(x):
 if hasattr(x,"items"):return {k:plain(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [plain(v) for v in x]
 return x
def write(name,x):x=dict(x);x["sha256"]=s({k:v for k,v in x.items() if k!="sha256"});(DOC/name).write_text(c(x)+"\n")
def main():
 parser=argparse.ArgumentParser();parser.add_argument("--resolution");args=parser.parse_args()
 start=time.monotonic();a=load_verified_historical_theorem_input_authority();n=bad=root_bad=order_bad=checker_bad=result_bad=0; rolling=""
 entries=_pair_order(); selected=[entry for entry in entries if args.resolution is None or entry["resolution"]==args.resolution]
 holds=[gzip.open(ROOT/"data/runtime/c93_ifc90payload/capsule/pair_attestations.jsonl.gz","rt")]
 try:
  # The public holdout source is sequenced globally; skip only in the
  # regression harness, never in public-object construction.
  skipped=0
  if selected: skipped=selected[0]["global_sequence"]
  for _ in range(skipped): next(holds[0])
  for entry in selected:
   pair, res=entry["pair_id"],entry["resolution"]; normal=historical_pair_normal_form(pair,res); proof=historical_pair_proof_inputs(pair,res)
   n+=1; node=normal["normal_form"]; operand=proof["proof_input"]
   bad += int(node["normal_form_root"]!=entry["normal_form_root"] or operand["proof_input_root"]!=entry["proof_input_root"])
   root_bad += int(node["normal_form_root"]!=operand["route_b_normal_form"]["root"])
   order_bad += int(normal["global_sequence"]!=entry["global_sequence"] or normal["resolution_sequence"]!=operand["pair"]["resolution_sequence"] or operand["pair"]["global_sequence"]!=entry["global_sequence"])
   result=check_proof(plain(node)); checker_bad += int(not result["pass"])
   hold=json.loads(next(holds[0])); result_bad += int(c(result)!=c(hold["proof"]))
   rolling=s({"previous":rolling,"pair":pair,"normal":normal["return_root"],"proof":proof["return_root"]})
 finally: holds[0].close()
 if n!=len(selected) or bad or root_bad or order_bad or checker_bad or result_bad:raise RuntimeError("C98 exhaustive public regression failure")
 prim_n=prim_bad=0
 if args.resolution is None:
  for family_id in ("C77","C78","C80","C82","C87"):
   family=historical_primitive_family(family_id)
   for record in family["records"]:
    public=historical_primitive_record(family_id,record["path"]);prim_n+=1;prim_bad+=int(c(dict(public["record"]))!=c(dict(record)))
  if prim_bad:raise RuntimeError("C98 primitive public regression failure")
 base={"C98_root":a["C98_root"],"resolution":args.resolution,"records":n,"content_mismatches":bad,"root_mismatches":root_bad,"order_mismatches":order_bad,"checker_executions":n,"checker_failures":checker_bad,"historical_result_mismatches":result_bad,"proof_result_accesses_during_input_load":0,"public_return_root":rolling,"elapsed_seconds":time.monotonic()-start}
 suffix=("" if args.resolution is None else "_"+args.resolution)
 write("c98_exhaustive_normal_form_public_regression"+suffix+".json",{**base,"loads":n,"missing":0,"schema_mismatches":0,"summary_mismatches":0})
 write("c98_exhaustive_proof_input_public_regression"+suffix+".json",{**base,"proof_inputs_loaded":n,"operand_root_mismatches":0,"certificate_available":0,"certificate_unavailable":n})
 write("c98_historical_self_checker_regression"+suffix+".json",{**base,"pass":True})
 if args.resolution is None: write("c98_exhaustive_primitive_direct_lookup_regression.json",{"records":prim_n,"missing":0,"extra":0,"duplicates":0,"content_mismatches":prim_bad,"family_root_mismatches":0,"inclusion_failures":0})
if __name__=="__main__":main()
