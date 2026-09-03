#!/usr/bin/env python3
"""Build C98's compact primitive lookup/package metadata only."""
from pathlib import Path
from hashlib import sha256
import json,gzip
from deuteron_wigner.bridge.ifequivapi2 import historical_primitive_family, load_verified_c93_public_authority
from deuteron_wigner.bridge.ifproofinput import verify_c90_proof_input_capsule
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"data/runtime/c98_ifhistpublic2"
def c(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def s(x):return sha256(c(x).encode()).hexdigest()
def write_atomic(path, payload):
 tmp=path.with_name(path.name+".tmp")
 tmp.write_text(payload)
 tmp.replace(path)
OUT.mkdir(parents=True,exist_ok=True); public=load_verified_c93_public_authority();c97=verify_c90_proof_input_capsule();records=[];families=[]
for family_id in ("C77","C78","C80","C82","C87"):
 f=historical_primitive_family(family_id); families.append({"family_id":family_id,"scientific_root":f["scientific_root"],"records":len(f["records"])})
 for seq,r in enumerate(f["records"]): records.append({"family_id":family_id,"record_id":r["path"],"sequence":seq,"record_digest":s(dict(r)),"inclusion":s({"family":family_id,"root":f["scientific_root"],"sequence":seq,"record":s(dict(r))})})
primitive={"schema":"C98-PRIMITIVE-DIRECT-INDEX-V1","records":records};primitive["root"]=s(primitive);write_atomic(OUT/"primitive_index.json",c(primitive)+"\n")
pairs=[]
for resolution in ("K9_2_N8_b0.40","K11_2_N10_b0.45","K13_2_N12_b0.50"):
 with gzip.open(ROOT/f"data/runtime/c97_ifproofinput/capsule/route_b_indexed_{resolution}.jsonl.gz","rt") as stream:
  for raw in stream:
   r=json.loads(raw);pairs.append({"pair_id":r["pair"]["id"],"resolution":resolution,"global_sequence":r["pair"]["global_sequence"],"normal_form_root":r["route_b_normal_form"]["root"],"proof_input_root":r["proof_input_root"]})
pair_body={"schema":"C98-PAIR-ORDER-INDEX-V1","records":pairs};pair_body["root"]=s(pair_body);write_atomic(OUT/"pair_order.json",c(pair_body)+"\n")
body={"schema":"C98-HISTORICAL-THEOREM-INPUT-PUBLIC-V1","C90_aggregate":dict(public["C90_aggregate"]),"C93_capsule_root":public["capsule_root"],"C94_package_root":public["package_root"],"C97_operand_root":c97["operand_root"],"C97_capsule_root":c97["capsule_root"],"primitive_index_root":primitive["root"],"pair_order_root":pair_body["root"],"families":families,"api":"ifhistpublic2-v1","no_recomputation":True};body["root"]=s(body);write_atomic(OUT/"manifest.json",c(body)+"\n");print(body["root"])
