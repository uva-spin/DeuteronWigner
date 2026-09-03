#!/usr/bin/env python3
import json
from pathlib import Path
from deuteron_wigner.bridge.qgcolor5.core import materialize,STATUS
O=Path(__file__).resolve().parents[1]/'docs'/'next_level'
if __name__=='__main__':
 r=materialize();c={'status':STATUS,'root':r,'no_embedding':True,'no_regeneration':True}
 for n in ['implementation_report','authority_manifest','source_api_fingerprints','basis_manifest','exact_record_manifest','bound_manifest','inventory','api_contract','api_validation','equivalence_report','c73_preflight','readiness_report','regression_report']:(O/('c72_'+n+'.json')).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
