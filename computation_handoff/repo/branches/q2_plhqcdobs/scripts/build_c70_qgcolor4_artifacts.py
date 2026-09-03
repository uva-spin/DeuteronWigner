#!/usr/bin/env python3
import json
from pathlib import Path
from deuteron_wigner.bridge.qgcolor4.core import materialize,STATUS
O=Path(__file__).resolve().parents[1]/'docs'/'next_level'
def main():
 r=materialize();c={'status':STATUS,'package_root':r,'no_embedding':True,'no_regeneration':True}
 for n in ['implementation_report','runtime_inventory','package_root_manifest','api_contract','api_validation','source_fingerprint','api_fingerprint','equivalence_report','c71_import_preflight','readiness_report','regression_report']:(O/('c70_'+n+'.json')).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
if __name__=='__main__':main()
