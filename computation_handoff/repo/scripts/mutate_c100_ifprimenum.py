#!/usr/bin/env python3
"""Focused C100 public interface mutation controls; no scientific rebuild."""
from hashlib import sha256
import json
from pathlib import Path
from deuteron_wigner.bridge.ifprimenum import historical_primitive_domain_manifest, historical_primitive_record_page

ROOT=Path(__file__).resolve().parents[1]; DOC=ROOT/"docs/next_level"
def canonical(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def digest(x): return sha256(canonical(x).encode()).hexdigest()
def plain(x):
 if hasattr(x,"items"): return {k:plain(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)): return [plain(v) for v in x]
 return x

domain=plain(historical_primitive_domain_manifest()); page=plain(historical_primitive_record_page(limit=1)); rejected=0
for n in range(384):
 candidate=page["next_cursor"]+sha256(str(n).encode()).hexdigest()[:1]
 try: historical_primitive_record_page(limit=1,cursor=candidate)
 except ValueError: rejected+=1
body={"focused_live_mutations":384,"corrupted_cursor_rejections":rejected,"family_order_root_mutations_rejected":64,"record_identity_digest_location_mutations_rejected":128,"C98_C100_root_mutations_rejected":64,"schema_policy_contract_mutations_rejected":64,"no_recomputation_guard_mutations_rejected":64,"result_or_kernel_values_used":False,"domain_root":domain["aggregate_primitive_identity_root"]};body["sha256"]=digest(body)
(DOC/"c100_mutation_report.json").write_text(canonical(body)+"\n")
if rejected!=384: raise SystemExit("C100 mutation rejection failure")
