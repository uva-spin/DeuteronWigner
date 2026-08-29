#!/usr/bin/env python3
"""Build deterministic manifests for the isolated C27 native-CDF1 test."""
from __future__ import annotations
import ast,hashlib,json,subprocess,sys
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs/next_level'
REPO=ROOT/'data/raw/c25_sources/dataprocessor/artemide-DataProcessor-work'
DP=ROOT/'data/runtime/c27_cdf1/dataprocessor-art25'; RT=ROOT/'data/runtime/c27_cdf1'
CSV=REPO/'DataLib/unpolDY/CDF1.csv'; DATE='2026-08-04'
sys.path.insert(0,str(DP))
from DataProcessor.DataSet import LoadCSV  # type: ignore
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(n,o): (D/n).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def git(*args): return subprocess.check_output(['git','-C',str(REPO),*args],text=True).strip()
def cut_function():
    p=DP/'FittingPrograms/ART25/DY+SIDIS-fit.py'; t=ast.parse(p.read_text()); f=next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name=='cutFunc')
    ns={'numpy':np,'path_to_constants':'ART25_main.atmde'}; exec(compile(ast.Module(body=[f],type_ignores=[]),str(p),'exec'),ns); return ns['cutFunc']
def serializable_point(p):
    keys=('id','process','s','qT','<qT>','Q','<Q>','y','<y>','xSec','uncorrErr','corrErr','thFactor','includeCuts','cutParams')
    out={k:p[k] for k in keys}; out['weightProcess']=p.get('weightProcess'); return out
def main():
    ds=LoadCSV(str(CSV)); selected=ds.CutData(cut_function(),computeCovarianceMatrix=False)
    cur=git('rev-parse','HEAD'); art='761f3fcdd3701c5cf69e822f9ffbbd5db394fc58'
    history=[]
    raw=git('log','--follow','--format=%H%x09%ad%x09%s','--date=iso','--','DataLib/unpolDY/CDF1.csv')
    for line in raw.splitlines():
        c,date,subject=line.split('\t',2); history.append({'commit':c,'date':date,'subject':subject})
    points=[serializable_point(p) for p in ds.points]
    write('c27_cdf1_dataset_manifest.json',{'schema_version':'1.0.0','classification':'DIAGNOSTIC_ONLY',
      'repository':{'url':'https://github.com/VladimirovAlexey/artemide-DataProcessor.git','commit':cur,'branch':'master','checkout_date':DATE,
        'remote_synchronized':cur==git('rev-parse','origin/master')},'cdf1':{'path':'DataLib/unpolDY/CDF1.csv','sha256':sha(CSV),'supplied_copy_byte_identical':True,'history':history},
      'art25':{'explicit_commit_identified':True,'commit':art,'subject':'ART25 update','selection_path':'FittingPrograms/ART25/DY+SIDIS-fit.py',
        'selection_sha256':sha(DP/'FittingPrograms/ART25/DY+SIDIS-fit.py'),'selection_status':'EXACT_PUBLIC_ART25_SELECTION_FOUND',
        'loaded_count':ds.numberOfPoints,'retained_count':selected.numberOfPoints,'retained_ids':[p['id'] for p in selected.points]},
      'dataset':{'name':ds.name,'comment':ds.comment,'reference':ds.reference,'process_type':ds.processType,'number_of_points':ds.numberOfPoints,
        'normalization_errors':ds.normErr,'is_normalized':ds.isNormalized,'normalization_method':ds.normalizationMethod,
        'uncorrelated_errors_per_point':ds.numOfUncorrErr,'correlated_errors_per_point':ds.numOfCorrErr,'normalization_error_count':ds.numOfNormErr,
        'weight_process_present':any(p.get('weightProcess') is not None for p in points),'points':points}})
    runs={n:json.loads((RT/f'{n}.json').read_text()) for n in ('central_full','central_reinit','central_restart','member_1','member_599','member_321','member_1_restart')}
    c=runs['central_full']; reinit=abs(c['native_point_first']-runs['central_reinit']['native_point_first']); restart=abs(c['native_point_first']-runs['central_restart']['native_point_first'])
    members=[{'label':n,'identity':runs[n]['member'],'native_value':runs[n]['native_point_first']} for n in ('central_full','member_1','member_599','member_321')]
    p0=points[0]; data_abs=abs(c['native_point_first']-p0['xSec']); data_rel=data_abs/abs(p0['xSec'])
    write('c27_cdf1_native_prediction.json',{'schema_version':'1.0.0','classification':'DIAGNOSTIC_ONLY','selection':'EXACT_PUBLIC_ART25_SELECTION',
      'point_id':'CDF1.0','point':p0,'central_native_value':c['native_point_first'],'central_native_repeat':c['native_point_second'],
      'entire_selected_dataset_values':c['full_native_values'],'entire_selected_dataset_count':len(c['full_native_values']),
      'members':members,'serial_residual':c['serial_residual'],'clean_reinitialization_residual':reinit,'restart_route':'central record separate-process checkpoint route','restart_residual':restart,
      'all_finite':all(np.isfinite(c['full_native_values']))})
    write('c27_cdf1_code_path_manifest.json',{'schema_version':'1.0.0','native_path':['DataProcessor.DataSet.LoadCSV','public ART25 cutFunc','DataProcessor.harpyInterface.ComputeXSec(default)','harpy.DY.xSecList','TMDX_DY.xSec_DY_List','Xsec_PTint_Qint_Yint','TMDF_F'],
      'loader_commit':art,'engine':'ARTEMIDE v3.01','engine_commit':'d873dc9fdcebba707df3bf9ae73061511fbf803f','constants_modified':False,
      'observable':{'integration':'BIN_INTEGRATED_OVER_qT_Q2_AND_PHYSICAL_RAPIDITY_THEN_THEORY_FACTOR','reported_form':'absolute dSigma/dqT bin average','normalized':False,
        'theory_factor':'1/(qTmax-qTmin); CDF1.0 = 2 GeV^-1','fiducial_cuts':False,'rapidity_sentinel':'[-1000,1000] clipped internally to physical support',
        'factorization':'LOW_qT_LP_TMD_W_ONLY','fixed_order_Y':False,'matching':False,'hard_coefficient':'N4LO','pi2_resummation':False,
        'electroweak':'process [1,1,-1,3], gamma/Z DY combination through ARTEMIDE EW input and coefficient channel','units':'pb/GeV as traced from hc2*1e9 pb conversion and qT-bin theory factor'},
      'integration':{'compiled_mode':2,'description':'approximate/fast v3.01 bin integration','qT_rule':'Integrate_SN with automatic minimum 6 sections','Q_rule':'G7 away from Z and adaptive around MZ +/-3 GeV','y_rule':'G7','relative_tolerance_non_qT':1e-3,'general_tolerance':1e-6},
      'source_lines':{'native_adapter':'DataProcessor/harpyInterface.py::_ComputeXSec_Point','matching':'DataProcessor/DataSet.py::MatchWithData','engine':'src/TMDX_DY.f90'}})
    c27=json.loads((D/'c27_dy_central_reproduction.json').read_text())
    write('c27_cdf1_comparison_report.json',{'schema_version':'1.0.0','classification':'DIAGNOSTIC_ONLY','point_id':'CDF1.0',
      'A_native':c['native_point_first'],'experimental':p0['xSec'],'native_minus_experiment':c['native_point_first']-p0['xSec'],'absolute_data_difference':data_abs,'relative_data_difference':data_rel,
      'B_existing_c27':{'exact_match':False,'value':None,'reason':'all three C27 points differ in s and/or bin-integrated observable definition','immutable_points_inspected':c27['records']},
      'C_controlled_oracle':{'raw_native_engine_bin_integral':c['raw_artemide_bin_integral'],'theory_factor':c['theory_factor'],
        'raw_times_factor':c['raw_artemide_bin_integral']*c['theory_factor'],'native_residual':c['raw_times_factor_residual'],
        'bin_center_differential_raw':c['bin_center_differential_oracle_raw'],'compared_to_integrated':False},
      'determinism':{'serial_residual':c['serial_residual'],'clean_reinitialization_residual':reinit,'restart_residual':restart},
      'public_repository_sufficiency':'SUFFICIENT_FOR_UNAMBIGUOUS_AUTHOR_INDEPENDENT_NATIVE_DIAGNOSTIC',
      'remaining_ambiguity':['no author-frozen expected numerical output or tolerance','public ART25 commit postdates ART25 fit payload and exact historical engine/DataProcessor pairing is inferred from explicit ART25 directory and v3.01 interface compatibility'],
      'author_email_needed':False,'email_qualification':'Only needed if an author-frozen target/tolerance or explicit historical environment attestation is required.'})
if __name__=='__main__': main()
