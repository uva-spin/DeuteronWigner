#!/usr/bin/env python3
"""Frozen CDF1.0 qT-section diagnostic without changing the source route."""
from __future__ import annotations
import json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from scripts.run_c28_art25_datasets import CONST,cut_function,rows,harpy,LoadCSV,DP

def main():
    central,_=rows();ds=LoadCSV(str(DP/'DataLib/unpolDY/CDF1.csv')).CutData(cut_function());p=ds.points[0]
    harpy.initialize(str(CONST));harpy.setNPparameters(central['np']);harpy.setPDFreplica(central['pdf']);harpy.setFFreplica(central['pi'],1);harpy.setFFreplica(central['ka'],2)
    # The exact C27 binary exposes the seven-argument ABI only.  Although the
    # public Python wrapper advertises ``Num``, passing it to this binary is a
    # type error.  Record that boundary instead of silently recompiling or
    # changing the validated source chain.
    raw=harpy.DY.xSec(p['process'],p['s'],p['qT'],p['Q'],p['y'],p['includeCuts'],p['cutParams'])
    values={'source_compiled_default':{'raw_integral':raw,'matched':raw*p['thFactor']}}
    auth=3.4394876804377352
    out={'accurate_mode_status':'UNAVAILABLE_IN_EXACT_C27_BINARY_ABI','point_id':'CDF1.0','authoritative_compiled_mode':2,'authoritative_native_value':auth,'diagnostic':'The public wrapper has a Num keyword, but the exact validated binary exports only the seven-argument dy_xsec_single ABI. No recompile or source-route change was permitted.','qT_sections':values,'source_default_residual':values['source_compiled_default']['matched']-auth,'requested_qT_sections':[6,12,24],'requested_qT_sections_executed':False,'full_compiled_mode1_executed':False,'source_route_replaced':False}
    path=ROOT/'data/runtime/c28_art25/numerical_accuracy.json';path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(path,values)
if __name__=='__main__':main()
