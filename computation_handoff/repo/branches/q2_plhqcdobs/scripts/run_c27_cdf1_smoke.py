#!/usr/bin/env python3
"""Native DataProcessor CDF1 diagnostic on the immutable C27 source chain."""
from __future__ import annotations
import argparse,ast,hashlib,json,sys,time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
ENGINE=ROOT/'data/raw/c25_sources/git/artemide-v301-engine/harpy'
DP=ROOT/'data/runtime/c27_cdf1/dataprocessor-art25'
CONST=ROOT/'data/runtime/c27_art25/ART25_main_path_adapter.atmde'
REP=ROOT/'data/raw/c25_sources/git/artemide-public-work/Models/ART25/Replica-files/ART25_main.rep'
sys.path[:0]=[str(ENGINE),str(DP)]
import harpy  # type: ignore
from DataProcessor.DataSet import LoadCSV  # type: ignore
from DataProcessor import harpyInterface  # type: ignore

def digest(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def replica_rows():
    data=[]
    for n,line in enumerate(REP.read_text().splitlines(),1):
        if line.count(',')<31: continue
        c=[x.strip() for x in line.split(',') if x.strip()]
        data.append({'source_line':n,'source_id':int(c[0]),'np':[float(x) for x in c[1:29]],
                     'pdf':int(c[29]),'pi':int(c[30]),'ka':int(c[31])})
    central=dict(data[1]); central['source_id']=0
    return central,{x['source_id']:x for x in data[2:]}
def art25_cut():
    path=DP/'FittingPrograms/ART25/DY+SIDIS-fit.py'
    tree=ast.parse(path.read_text()); node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='cutFunc')
    ns={'numpy':np,'path_to_constants':'ART25_main.atmde'}
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(path),'exec'),ns)
    return ns['cutFunc']
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--member',default='central'); ap.add_argument('--full',action='store_true'); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    central,stochastic=replica_rows(); member=central if a.member=='central' else stochastic[int(a.member)]
    dataset=LoadCSV(str(DP/'DataLib/unpolDY/CDF1.csv')); selected=dataset.CutData(art25_cut(),computeCovarianceMatrix=False)
    point=selected.points[0]; started=time.time(); harpy.initialize(str(CONST))
    harpy.setNPparameters(member['np']); harpy.setPDFreplica(member['pdf']); harpy.setFFreplica(member['pi'],1); harpy.setFFreplica(member['ka'],2)
    native1=float(harpyInterface.ComputeXSec(point,method='default')); native2=float(harpyInterface.ComputeXSec(point,method='default'))
    raw=float(harpy.DY.xSecList([point['process']],[point['s']],[point['qT']],[point['Q']],[point['y']],[point['includeCuts']],[point['cutParams']])[0])
    center_raw=float(harpy.DY.xSecListBINLESS([point['process']],[point['s']],[point['<qT>']],[point['<Q>']],[point['<y>']],[point['includeCuts']],[point['cutParams']])[0])
    full=[]
    if a.full: full=[float(x) for x in harpyInterface.ComputeXSec(selected,method='default')]
    out={'schema_version':'1.0.0','classification':'DIAGNOSTIC_ONLY','member':{'lambda_index':member['source_id'],'source_line':member['source_line'],
      'pdf_index':member['pdf'],'pion_ff_index':member['pi'],'kaon_ff_index':member['ka'],'np_sha256':digest(member['np'])},
      'selected_point_id':point['id'],'native_point_first':native1,'native_point_second':native2,'serial_residual':abs(native2-native1),
      'raw_artemide_bin_integral':raw,'theory_factor':point['thFactor'],'raw_times_factor_residual':abs(native1-raw*point['thFactor']),
      'bin_center_differential_oracle_raw':center_raw,'bin_center_not_compared_to_bin_integral':True,
      'selected_count':selected.numberOfPoints,'selected_ids':[p['id'] for p in selected.points],
      'full_native_values':full,'full_completed':len(full),'elapsed_seconds':time.time()-started}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'member':a.member,'native':native1,'serial_residual':out['serial_residual'],'full':len(full),'seconds':out['elapsed_seconds']}))
if __name__=='__main__': main()
