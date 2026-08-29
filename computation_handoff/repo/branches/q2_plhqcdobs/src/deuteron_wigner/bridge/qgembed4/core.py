"""C67 fail-closed immutable-C66 import gate."""
from pathlib import Path
from hashlib import sha256
import json
from ..qgtm2 import core as c64
ROOT=Path(__file__).resolve().parents[4]; BASELINE='8f8240ff2c5cb2615ee68ba10331b9732dd84ca6'; STATUS='C67_QGEMBED_C66_IMPORT_INCOMPLETE'; NEXT='C68/QGCOLOR-RUNTIME — C66 read-only API, hashes, certified arrays, and inventory completion'
def preflight():
 i=c64._load_index(); b=c64.list_tm_blocks(); assert len(b)==733 and sum(x['candidate_count'] for x in b)==171153 and i['residue_certificates']['total']==67920
 source=(ROOT/'src/deuteron_wigner/bridge/qgcolor2/core.py').read_text(); api=json.loads((ROOT/'docs/next_level/c66_api_contract.json').read_text())
 return {'baseline':BASELINE,'status':STATUS,'next':NEXT,'C64_import':{'blocks':len(b),'statuses':171153,'residues':67920,'read_only':True},'C66_import':{'status':'FAIL','hash_verifying_loader_present':any(x in source for x in ('load_u3','load_triplet','verify_hash')),'runtime_inventory_present':False,'api_contract':api,'blocker':'C66 exports build() only; it has no C66-owned hash-verifying read-only loader, runtime inventory, immutable-array interface, or committed array/bound hashes. Calling build() would regenerate/refactor C66, forbidden in C67.'},'unavailable':['CM_ground_selection','kinematic_injection','triplet_embedding','support','historical_adapter','impact_audit'],'no_regeneration':True,'no_contact':True}
