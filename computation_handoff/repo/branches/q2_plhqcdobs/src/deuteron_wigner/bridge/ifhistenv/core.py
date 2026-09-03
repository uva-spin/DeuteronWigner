import json
from pathlib import Path
STATUS='C86_C82_HISTORICAL_RUNTIME_ENVIRONMENT_INCOMPLETE'
NEXT='C87/IFCAPSULE — bind historical C82 inputs to exact producer runtime roots before staging a capsule'
def audit_capsule():
 root=Path(__file__).resolve().parents[4]; freeze=json.loads((root/'docs/next_level/c82_input_freeze.json').read_text());c72=json.loads((root/'data/runtime/c72_qgcolor5/root.json').read_text())
 return {'status':STATUS,'next':NEXT,'blocker':'C86.HISTORICAL_C82.PRODUCER_RUNTIME_ROOT_UNBOUND','dependency_graph':['C82->C77','C82->C78','C82->C80','C82->C74->C72'],'C72_local_candidate_root':c72,'C82_frozen_C74':freeze.get('C74_color_records'),'historical_C72_root_hash_bound':False,'reason':'C82 freeze records C74 color-record count but no C72 root/index/payload hashes; current C72 cannot be promoted to an exact historical candidate.','capsule_created':False,'scientific_stream_generated':False}
