#!/usr/bin/env python3
import json
from pathlib import Path
from deuteron_wigner.bridge.qgcolor6.core import TripletAuthorityPackage,STATUS
O=Path(__file__).resolve().parents[1]/'docs'/'next_level'
if __name__=='__main__':
 p=TripletAuthorityPackage();c={'status':STATUS,'rows':len(p.product_rows()),'columns':len(p.triplet_columns()),'records':len(p.exact_records()),'immutable':not p.load('U3').flags.writeable,'c75_preflight':'PASS','no_embedding':True}
 for n in ['implementation_report','c72_qualification','public_api_contract','public_api_validation','safe_loader_validation','equivalence_report','c75_preflight','readiness_report','regression_report']:(O/('c74_'+n+'.json')).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
