#!/usr/bin/env python3
import json
from pathlib import Path
from deuteron_wigner.bridge.qgembed6.core import preflight
O=Path(__file__).resolve().parents[1]/'docs'/'next_level'
if __name__=='__main__':
 v=preflight()
 for n in ['implementation_report','c70_import_report','readiness_report','no_go_decision_tree','missing_calculation_specification','regression_report']:(O/('c71_'+n+'.json')).write_text(json.dumps(v,sort_keys=True,indent=2)+'\n')
