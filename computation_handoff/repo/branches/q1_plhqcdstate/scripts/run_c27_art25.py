#!/usr/bin/env python3
"""Execute source-regenerated ART25 v3.01 benchmark records.

This runner intentionally uses only the exact released Lambda rows and their
stored collinear indices. It supports content-addressed range checkpoints so
serial, multi-process shard, and restart results can be compared without
changing physics.
"""
from __future__ import annotations

import argparse, hashlib, json, math, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ENGINE=ROOT/'data/raw/c25_sources/git/artemide-v301-engine/harpy'
sys.path.insert(0,str(ENGINE))
import harpy  # type: ignore  # noqa: E402

REP=ROOT/'data/raw/c25_sources/git/artemide-public-work/Models/ART25/Replica-files/ART25_main.rep'
CONST=ROOT/'data/runtime/c27_art25/ART25_main_path_adapter.atmde'

def rows():
    lines=REP.read_text().splitlines()
    data=[]
    for n,line in enumerate(lines,1):
        if line.count(',')<31:continue
        c=[x.strip() for x in line.split(',') if x.strip()]
        data.append({'source_line':n,'source_id':int(c[0]),'np':[float(x) for x in c[1:29]],
                     'pdf':int(c[29]),'pi':int(c[30]),'ka':int(c[31])})
    return data[1],data[2:] # central/mean, then 642 stochastic; initialization excluded

def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def execute(m):
    harpy.setNPparameters(m['np']); harpy.setPDFreplica(m['pdf']); harpy.setFFreplica(m['pi'],1); harpy.setFFreplica(m['ka'],2)
    dist={
      'cs_DNP_b1_mu5':float(harpy.get_DNP(1.,5.)),
      'tmdpdf_x01_b1_Q5':[float(x) for x in harpy.get_uTMDPDF(.1,1.,1,5.,25.)],
      'pion_tmdff_z03_b1_Q5':[float(x) for x in harpy.get_uTMDFF(.3,1.,1,5.,25.)],
      'kaon_tmdff_z03_b1_Q5':[float(x) for x in harpy.get_uTMDFF(.3,1.,2,5.,25.)],
    }
    dy=[float(x) for x in harpy.DY.xSecListBINLESS([[1,1,-1,3]]*3,[38.8**2,13000.**2,8000.**2],
          [.5,2.,3.],[6.,91.1876,91.1876],[0.,0.,2.],[False]*3,[[0.,0.,0.,0.]]*3)]
    sidis=[float(x) for x in harpy.SIDIS.xSecListBINLESS([[1,1,1,2001],[1,1,2,2001]],
          [52.657444,301.039844],[.25,.3],[.3,.3],[.1,.05],[2.5,3.],[[.938,.139],[.938,.494]])]
    result={'member_id':m['source_id'],'source_line':m['source_line'],'pdf_index':m['pdf'],'pion_ff_index':m['pi'],
            'kaon_ff_index':m['ka'],'np_sha256':digest(m['np']),'distribution':dist,'dy':dy,'sidis':sidis}
    if not all(math.isfinite(x) for x in [dist['cs_DNP_b1_mu5'],*dy,*sidis,*dist['tmdpdf_x01_b1_Q5'],*dist['pion_tmdff_z03_b1_Q5'],*dist['kaon_tmdff_z03_b1_Q5']]):
        raise ValueError(f"C27.NONFINITE:{m['source_id']}")
    result['content_sha256']=digest(result)
    return result

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--start',type=int,default=1); ap.add_argument('--stop',type=int,default=642)
    ap.add_argument('--output',type=Path,required=True); ap.add_argument('--include-central',action='store_true'); a=ap.parse_args()
    central,stochastic=rows(); selected=[m for m in stochastic if a.start<=m['source_id']<=a.stop]
    started=time.time(); harpy.initialize(str(CONST)); failures=[]; out=[]
    if a.include_central:
        c=dict(central); c['source_id']=0
        try:out.append(execute(c))
        except Exception as e:failures.append({'member_id':0,'error':type(e).__name__+':'+str(e)})
    for m in selected:
        try:out.append(execute(m))
        except Exception as e:failures.append({'member_id':m['source_id'],'error':type(e).__name__+':'+str(e)})
    payload={'schema_version':'1.0.0','engine':'v3.01','constants_adapter':str(CONST.relative_to(ROOT)),
      'range':[a.start,a.stop],'include_central':a.include_central,'attempted':len(selected)+int(a.include_central),
      'completed':len(out),'failures':failures,'elapsed_seconds':time.time()-started,'records':out}
    payload['records_sha256']=digest(out); a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'output':str(a.output),'attempted':payload['attempted'],'completed':len(out),'failures':len(failures),'elapsed_seconds':payload['elapsed_seconds']}))
    return 0 if not failures else 1
if __name__=='__main__':raise SystemExit(main())
