#!/usr/bin/env python3
import json
from pathlib import Path
from deuteron_wigner.bridge.qgtm4.core import preflight
O=Path(__file__).resolve().parents[1]/'docs'/'next_level'
if __name__=='__main__':
 v=preflight()
 for n in ['implementation_report','crosswalk_source_audit','public_api_contract','c77_preflight','readiness_report','no_go_decision_tree','missing_calculation_specification','regression_report']:(O/('c76_'+n+'.json')).write_text(json.dumps(v,sort_keys=True,indent=2)+'\n')
