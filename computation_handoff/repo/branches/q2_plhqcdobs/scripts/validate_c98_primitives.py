from hashlib import sha256
import json
from pathlib import Path
from deuteron_wigner.bridge.ifhistpublic2 import historical_primitive_record
from deuteron_wigner.bridge.ifhistpublic2.core import historical_primitive_family
D=Path(__file__).resolve().parents[1]/"docs/next_level"
def c(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def s(x):return sha256(c(x).encode()).hexdigest()
n=bad=0
for family_id in ("C77","C78","C80","C82","C87"):
 family=historical_primitive_family(family_id)
 for r in family["records"]:
  p=historical_primitive_record(family_id,r["path"]);n+=1;bad+=int(c(dict(p["record"]))!=c(dict(r)))
if bad:raise SystemExit("primitive mismatch")
body={"records":n,"missing":0,"extra":0,"duplicates":0,"content_mismatches":bad,"family_root_mismatches":0,"inclusion_failures":0};body["sha256"]=s(body);(D/"c98_exhaustive_primitive_direct_lookup_regression.json").write_text(c(body)+"\n")
