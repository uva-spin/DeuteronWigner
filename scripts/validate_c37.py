#!/usr/bin/env python3
from hashlib import sha256
import json
from pathlib import Path
from deuteron_wigner.bridge import r2
import build_c37_manifests as b
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs/next_level'
def main():
 for n in b.NAMES:
  v=json.loads((DOCS/n).read_text()); q=dict(v); got=q.pop('content_hash'); assert got==sha256(json.dumps(q,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
 assert json.loads((DOCS/'c37_finite_basis_partonic_collinear.json').read_text())['status']==r2.C37_NO_GO
 assert json.loads((DOCS/'c37_injection_manifest.json').read_text())['count']>=2840
 assert not json.loads((DOCS/'c37_hadron_application_gate.json').read_text())['bridge_rerun']
 print('C37_VALIDATION_PASS')
if __name__=='__main__':main()
