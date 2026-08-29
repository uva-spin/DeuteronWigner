#!/usr/bin/env python3
"""Execute the complete public ART25-selected dataset through native DataProcessor."""
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
from DataProcessor.DataMultiSet import DataMultiSet  # type: ignore
from DataProcessor import harpyInterface  # type: ignore

DY_NAMES=['CDF1','CDF2','D01','D02','D02m','A8-00y04','A8-04y08','A8-08y12','A8-12y16','A8-16y20','A8-20y24','A8-46Q66','A8-116Q150','A13-norm','CMS7','CMS8','CMS13-00y04','CMS13-04y08','CMS13-08y12','CMS13-12y16','CMS13-16y24','CMS13_dQ_106to170','CMS13_dQ_170to350','CMS13_dQ_350to1000','LHCb7','LHCb8','LHCb13_dy(2021)','PHE200','STAR510','E228-200','E228-300','E228-400','E772','E605','D0run1-W','CDFrun1-W']
SIDIS_NAMES=['hermes.p.vmsub.zxpt.pi+','hermes.p.vmsub.zxpt.pi-','hermes.d.vmsub.zxpt.pi+','hermes.d.vmsub.zxpt.pi-','hermes.p.vmsub.zxpt.k+','hermes.p.vmsub.zxpt.k-','hermes.d.vmsub.zxpt.k+','hermes.d.vmsub.zxpt.k-','compass.d.h+','compass.d.h-']
def digest(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def rows():
    out=[]
    for n,line in enumerate(REP.read_text().splitlines(),1):
        if line.count(',')<31:continue
        c=[x.strip() for x in line.split(',') if x.strip()]; out.append({'source_line':n,'source_id':int(c[0]),'np':[float(x) for x in c[1:29]],'pdf':int(c[29]),'pi':int(c[30]),'ka':int(c[31])})
    central=dict(out[1]); central['source_id']=0
    return central,out[2:]
def cut_function():
    path=DP/'FittingPrograms/ART25/DY+SIDIS-fit.py'; tree=ast.parse(path.read_text()); node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='cutFunc')
    ns={'numpy':np,'path_to_constants':str(DP/'FittingPrograms/ART25/ConstantsFiles/ART25_main.atmde')}; exec(compile(ast.Module(body=[node],type_ignores=[]),str(path),'exec'),ns); return ns['cutFunc']
def load_sets():
    cut=cut_function(); dy=[]; si=[]
    for n in DY_NAMES:
        folder='unpolW' if n.endswith('W') else 'unpolDY'; dy.append(LoadCSV(str(DP/'DataLib'/folder/(n+'.csv'))).CutData(cut))
    for n in SIDIS_NAMES:si.append(LoadCSV(str(DP/'DataLib/unpolSIDIS'/(n+'.csv'))).CutData(cut))
    return dy,si
def nuisance_lambda(ds,pred):
    sc=ds.numOfCorrErr+ds.numOfNormErr
    if sc==0:return []
    rho=np.zeros(sc)
    for i in range(ds.numberOfPoints):rho+=(ds.points[i]['xSec']-pred[i])*ds._listOfCorrErrors[i]/ds._listOfVariances[i]
    return np.matmul(ds.matrixAinverse,rho).tolist()
def execute(member,dy,si,dy_multi,si_multi):
    harpy.setNPparameters(member['np']); harpy.setPDFreplica(member['pdf']); harpy.setFFreplica(member['pi'],1); harpy.setFFreplica(member['ka'],2)
    pd=np.asarray(harpyInterface.ComputeXSec(dy_multi),float); ps=np.asarray(harpyInterface.ComputeXSec(si_multi),float); pred=np.concatenate([pd,ps])
    chi=[]; dec=[]; nuisance=[]; k=0
    for ds in [*dy,*si]:
        q=pred[k:k+ds.numberOfPoints]; chi.append(float(ds.chi2(q))); dec.append([float(x) for x in ds.DecomposeChi2(q)]); nuisance.append(nuisance_lambda(ds,q)); k+=ds.numberOfPoints
    if len(pred)!=1209 or not np.all(np.isfinite(pred)):raise ValueError('C28.EXECUTION.NONFINITE_OR_COUNT')
    ident={'lambda_index':member['source_id'],'source_line':member['source_line'],'pdf_index':member['pdf'],'pion_ff_index':member['pi'],'kaon_ff_index':member['ka'],'np_sha256':digest(member['np'])}
    return ident,pred,np.asarray(chi),np.asarray(dec),nuisance
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--start',type=int,default=1); ap.add_argument('--stop',type=int,default=642); ap.add_argument('--include-central',action='store_true'); ap.add_argument('--output-prefix',type=Path,required=True); a=ap.parse_args()
    central,stoch=rows(); selected=[x for x in stoch if a.start<=x['source_id']<=a.stop]; members=([central] if a.include_central else [])+selected
    dy,si=load_sets(); dm=DataMultiSet('ART25-DY',dy); sm=DataMultiSet('ART25-SIDIS',si); started=time.time(); harpy.initialize(str(CONST))
    ids=[]; predictions=[]; chis=[]; decomposed=[]; nuisances=[]; failures=[]
    for m in members:
        try:
            ident,p,c,d,n=execute(m,dy,si,dm,sm); ids.append(ident);predictions.append(p);chis.append(c);decomposed.append(d);nuisances.append(n)
        except Exception as e:failures.append({'lambda_index':m['source_id'],'error':type(e).__name__+':'+str(e)})
    a.output_prefix=(ROOT/a.output_prefix).resolve() if not a.output_prefix.is_absolute() else a.output_prefix
    a.output_prefix.parent.mkdir(parents=True,exist_ok=True); npz=a.output_prefix.with_suffix('.npz')
    np.savez_compressed(npz,predictions=np.asarray(predictions),chi2=np.asarray(chis),chi2_decomposed=np.asarray(decomposed))
    meta={'schema_version':'1.0.0','range':[a.start,a.stop],'include_central':a.include_central,'attempted':len(members),'completed':len(ids),'failures':failures,'member_identities':ids,
      'nuisance_profiles':nuisances,'dataset_order':DY_NAMES+SIDIS_NAMES,'dataset_point_counts':[x.numberOfPoints for x in [*dy,*si]],'point_ids':[p['id'] for p in dm.points+sm.points],
      'process_point_counts':{'DY':dm.numberOfPoints,'SIDIS':sm.numberOfPoints},'npz':str(npz.relative_to(ROOT)),'npz_sha256':hashlib.sha256(npz.read_bytes()).hexdigest(),'elapsed_seconds':time.time()-started}
    a.output_prefix.with_suffix('.json').write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n'); print(json.dumps({'attempted':len(members),'completed':len(ids),'failed':len(failures),'seconds':meta['elapsed_seconds'],'npz':str(npz)}))
if __name__=='__main__':main()
