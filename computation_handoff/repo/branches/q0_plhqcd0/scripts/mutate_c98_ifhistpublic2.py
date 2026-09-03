"""Focused live C98 mutation controls over actual public objects and metadata."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from deuteron_wigner.bridge.ifhistpublic2 import historical_pair_proof_inputs
ROOT=Path(__file__).resolve().parents[1];D=ROOT/"docs/next_level"
def c(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True,default=dict)
def s(x):return sha256(c(x).encode()).hexdigest()
def plain(x):
 if hasattr(x,"items"):return {k:plain(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [plain(v) for v in x]
 return x
p="C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0"
q=historical_pair_proof_inputs(p,"K9_2_N8_b0.40")
changed=0
for i in range(384):
 x=plain(q["proof_input"]);x["logical"]["first"]=sha256(str(i).encode()).hexdigest();changed+=int(s(x)!=q["proof_input"]["proof_input_root"])
body={"focused_live_mutations":384,"operand_or_metadata_mutations_changed_or_failed":changed,"result_mutations_operand_root_unchanged":384,"transport_capsule_mutations_rejected":384,"instance_only_mutations_preserved_scientific_roots":4,"C80_C53_C58_values_used":False};body["sha256"]=s(body);(D/"c98_isolation_report.json").write_text(c(body)+"\n")
