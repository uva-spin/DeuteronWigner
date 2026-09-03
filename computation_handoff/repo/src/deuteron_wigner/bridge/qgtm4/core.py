from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[4];STATUS='C76_TM_CROSSWALK_CM_IDENTITY_INCOMPLETE';NEXT='C77/QGTM5 — materialize C64 row/column identities and authenticated CM labels'
def preflight():
 x=json.loads((ROOT/'docs/next_level/c64_c65_basis_crosswalk.json').read_text());sample=x['blocks'][0];missing=[k for k in ('global_row_basis_id','global_column_basis_id','n_CM','m_CM','orientation') if k not in sample]
 return {'status':STATUS,'next':NEXT,'crosswalk_entries':len(x['blocks']),'source':'docs/next_level/c64_c65_basis_crosswalk.json','missing_authenticated_fields':missing,'blocker':'C64 crosswalk documentation has offsets/counts/hashes but no row/column identities, CM labels, or orientation per entry. C76 may not infer these from array positions or numerical magnitude.','no_embedding':True}
