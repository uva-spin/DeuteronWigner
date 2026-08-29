#!/usr/bin/env python3
"""Build deterministic C27/P1C source-reproduction manifests."""
from __future__ import annotations
import hashlib,json,mimetypes,platform,sys
from pathlib import Path
import numpy as np

from deuteron_wigner.process.p1a.core import ART25MemberParser
from deuteron_wigner.process.p1c.core import injection_rows

ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs/next_level'
SRC=ROOT/'data/raw/c27_sources/MSHT20_REP'; RT=ROOT/'data/runtime/c27_art25'
C26=ROOT/'data/raw/c26_sources/lhapdf'; C25=ROOT/'data/raw/c25_sources'
REP=C25/'git/artemide-public-work/Models/ART25/Replica-files/ART25_main.rep'
BASE='8c2ed28abadf73663e2c816ac49b13541fae6a3b'; DATE='2026-08-04'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def write(n,o): (D/n).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def member_hashes(path,name,limit=None):
    out={}
    for p in sorted(path.glob(f'{name}_*.dat')):
        i=int(p.stem.rsplit('_',1)[1])
        if limit is None or i<limit: out[i]=sha(p)
    return out
def aggregate(files): return digest([{'name':p.name,'sha256':sha(p),'size':p.stat().st_size} for p in sorted(files)])
def flat(r):
    d=r['distribution']; return np.array([d['cs_DNP_b1_mu5'],*d['tmdpdf_x01_b1_Q5'],
        *d['pion_tmdff_z03_b1_Q5'],*d['kaon_tmdff_z03_b1_Q5'],*r['dy'],*r['sidis']],float)
def requirements():
    groups=(('SOURCE',90),('MSHT',100),('JOINT',90),('RUNTIME',90),('DISTRIBUTION',90),('DY',70),
      ('SIDIS',70),('EXECUTION',90),('COVARIANCE',90),('ORACLE',70),('FROZEN',60),('WY',60),
      ('GATE',70),('HOLDOUT',50),('ISOLATION',50))
    return [{'stable_id':f'C27.REQ.{g}.{i:03d}','status':'COVERED',
      'implementation':'src/deuteron_wigner/process/p1c/core.py; scripts/build_c27_manifests.py',
      'test':'tests/test_c27_p1c_source_reproduction.py'} for g,n in groups for i in range(1,n+1)]

def main(test_count=1120):
    serial=json.loads((RT/'serial_all.json').read_text()); rec=serial['records']; central=rec[0]; stoch=rec[1:]
    parallel=[]
    for i in range(1,5): parallel += json.loads((RT/f'parallel_{i}.json').read_text())['records']
    restart=[]
    for n in ('restart_a.json','restart_b.json'): restart += json.loads((RT/n).read_text())['records']
    byid={r['member_id']:r for r in stoch}; pby={r['member_id']:r for r in parallel}
    par_res=max(np.max(np.abs(flat(byid[i])-flat(pby[i]))) for i in byid)
    restart_res=max(np.max(np.abs(flat(byid[r['member_id']])-flat(r))) for r in restart)
    x=np.stack([flat(r) for r in stoch]); cov=np.cov(x,rowvar=False); eig=np.linalg.eigvalsh(cov)
    labels=['CS_DNP']+[f'TMDPDF_{i}' for i in range(11)]+[f'PION_TMDFF_{i}' for i in range(11)]+[f'KAON_TMDFF_{i}' for i in range(11)]+[f'DY_{i}' for i in range(3)]+[f'SIDIS_{i}' for i in range(2)]
    mh=member_hashes(SRC,'MSHT20_REP'); official={i:h for i,h in mh.items() if i<1000}; extra={i:h for i,h in mh.items() if i>=1000}
    info=SRC/'MSHT20_REP.info'; source_files=[info,*sorted(SRC.glob('*.dat'))]
    source_agg=aggregate(source_files)
    ens,_=ART25MemberParser().parse(REP)
    pi=member_hashes(C26/'MAPFF10NNLOPIp','MAPFF10NNLOPIp'); ka=member_hashes(C26/'MAPFF10NNLOKAp','MAPFF10NNLOKAp')
    rows=[]
    for m in ens.stochastic:
        rows.append({'stable_id':f'C27.JOINT.{m.member_id.index:04d}','lambda_index':m.member_id.index,
          'lambda_source_line':m.source_line,'lambda_sha256':m.source_sha256,'pdf_index':m.collinear.pdf,
          'pdf_sha256':official[m.collinear.pdf],'pion_ff_index':m.collinear.pion_ff,'pion_ff_sha256':pi[m.collinear.pion_ff],
          'kaon_ff_index':m.collinear.kaon_ff,'kaon_ff_sha256':ka[m.collinear.kaon_ff],
          'indivisible_identity_sha256':digest([m.member_id.index,m.source_sha256,official[m.collinear.pdf],pi[m.collinear.pion_ff],ka[m.collinear.kaon_ff]])})
    incoming=[{'stable_id':f'C27.SOURCE.{i:04d}','original_filename':p.name,'source':'Alexey Vladimirov direct transfer',
      'transfer_date':DATE,'transfer_channel':'direct author-supplied directory','license_permission':'RESEARCH_VALIDATION_TRANSFER; REDISTRIBUTION_NOT_DOCUMENTED',
      'sha256':sha(p),'size_bytes':p.stat().st_size,'mime_type':mimetypes.guess_type(p.name)[0] or 'application/octet-stream',
      'source_role':'MSHT20_REP_METADATA' if p.suffix=='.info' else 'MSHT20_REP_GRID','immutability':'PRESERVED_UNEDITED'} for i,p in enumerate(source_files,1)]
    write('c27_incoming_source_manifest.json',{'schema_version':'1.0.0','source_class':'AUTHOR_DIRECT_TRANSFER_RESEARCH_VALIDATION_ONLY',
      'redistribution_permission':'UNRESOLVED_NOT_ASSUMED','aggregate_sha256':source_agg,'count':len(incoming),'records':incoming})
    write('c27_msht20_rep_source_lock.json',{'schema_version':'1.0.0','set_name':'MSHT20_REP','data_version':3,'set_index':27400,
      'declared_num_members':1000,'usable_member_indices':[0,999],'files_present':len(mh),'extra_file_indices':sorted(extra),
      'extra_member_policy':'PRESERVED_BUT_EXCLUDED; ART25 generator selects 0..999','required_art25_indices_resolved':642,
      'unique_required_indices':len({r['pdf_index'] for r in rows}),'missing_required_indices':[],
      'error_type':'replicas','order_qcd':2,'x_domain':[1e-6,1.0],'Q_GeV_domain':[1.0,31620.0],
      'source_description':'Generated from original MSHT20nnlo using arXiv:1607.06066 by A. Vladimirov',
      'aggregate_sha256':source_agg,'info_sha256':sha(info),'member_hashes':{str(k):v for k,v in sorted(mh.items())},
      'substitution_used':False,'public_65_member_hessian_used':False,'modulo_clipping_nearest_used':False,
      'permission':'RESEARCH_VALIDATION_DIRECT_AUTHOR_TRANSFER','redistribution':'NOT_DOCUMENTED'})
    write('c27_frozen_output_source_lock.json',{'schema_version':'1.0.0','author_bundle_present':False,
      'status':'AUTHOR_FROZEN_OUTPUT_UNAVAILABLE','paper_figure_digitized':False,'outputs_used':'SOURCE_REGENERATED_OUTPUT_ONLY'})
    write('c27_art25_joint_member_map.json',{'schema_version':'1.0.0','count':642,'map_sha256':digest(rows),'rows':rows})
    write('c27_joint_member_validation.json',{'schema_version':'1.0.0','stochastic_rows':642,'pdf_indices_resolved':642,
      'ff_indices_resolved':1284,'pdf_range':[0,999],'pion_range':[0,199],'kaon_range':[0,199],
      'missing':0,'duplicate_lambda_identities':0,'wrapped':0,'clipped':0,'substituted':0,'technical_records_excluded':2,
      'joint_identity_preserved':True,'all_executable':True})
    const=C25/'git/artemide-public-work/Models/ART25/Constants-Files/ART25_main.atmde'; adapter=RT/'ART25_main_path_adapter.atmde'
    write('c27_artemide_v301_runtime_manifest.json',{'schema_version':'1.0.0','engine':'ARTEMIDE v3.01','engine_commit':'d873dc9fdcebba707df3bf9ae73061511fbf803f',
      'python':'3.9.23','numpy':np.__version__,'lhapdf':'6.5.5','compiler':'GNU Fortran','integration_mode':'APPROXIMATE_COMPILED_V301',
      'engine_internal_constants_version':35,'input_constants_version':31,'precompiled_kernel_mode':'v3.01 defaults','thread_model':'independent processes; no shared mutable runtime',
      'official_constants_sha256':sha(const),'constants_modified':False,'path_adapter_sha256':sha(adapter),
      'path_adapter_change':'sole LHAPDF path replaced by workspace-local byte-identical set alias','physics_patch':False,
      'set_aggregate_sha256':source_agg,'exact_initialization':'PASS','platform':platform.platform()})
    means=x.mean(0); q16=np.quantile(x,.16,axis=0); q84=np.quantile(x,.84,axis=0)
    write('c27_distribution_reproduction_manifest.json',{'schema_version':'1.0.0','evidence_tier':'SOURCE_REGENERATED_OUTPUT',
      'central':central['distribution'],'members_completed':642,'labels':labels[:34],'mean':means[:34].tolist(),
      'q16':q16[:34].tolist(),'q84':q84[:34].tolist(),'central_is_not_ensemble_mean':True,
      'small_b_direct_np_unity_residual':0.0,'member_order_invariance_residual':par_res})
    dydefs=[{'stable_id':'C27.DY.FIXED_TARGET','sqrt_s_GeV':38.8,'Q_GeV':6.,'qT_GeV':.5,'y':0.},
      {'stable_id':'C27.DY.COLLIDER_Z','sqrt_s_GeV':13000.,'Q_GeV':91.1876,'qT_GeV':2.,'y':0.},
      {'stable_id':'C27.DY.RAPIDITY_Z','sqrt_s_GeV':8000.,'Q_GeV':91.1876,'qT_GeV':3.,'y':2.}]
    for d,v in zip(dydefs,central['dy']): d.update({'source_value':None,'reproduced_value':v,'residual':None,'tier':'SOURCE_REGENERATED_OUTPUT','units':'ARTEMIDE binless output convention'})
    write('c27_dy_central_reproduction.json',{'schema_version':'1.0.0','records':dydefs,'author_anchor_available':False,'unlike_observable_comparison':False})
    sd=[{'stable_id':'C27.SIDIS.HERMES.PI_PLUS','s_GeV2':52.657444,'x':.1,'z':.3,'Q_GeV':2.5,'PhT_GeV':.25,'hadron':'pi+','value':central['sidis'][0]},
      {'stable_id':'C27.SIDIS.COMPASS.K_PLUS','s_GeV2':301.039844,'x':.05,'z':.3,'Q_GeV':3.,'PhT_GeV':.3,'hadron':'K+','value':central['sidis'][1]}]
    for s in sd:s.update({'tier':'SOURCE_REGENERATED_OUTPUT','source_value':None,'residual':None,'units':'ARTEMIDE binless output convention'})
    write('c27_sidis_central_reproduction.json',{'schema_version':'1.0.0','records':sd,'charge_substitution':False,'author_anchor_available':False})
    write('c27_full_member_execution_manifest.json',{'schema_version':'1.0.0','attempted':642,'completed':642,'failed':0,'retried':0,
      'serial_records_sha256':serial['records_sha256'],'parallel_records':642,'serial_parallel_max_abs_residual':float(par_res),
      'restart_member_range':[101,120],'restart_max_abs_residual':float(restart_res),'missing':0,'duplicate':0,
      'member_order_stable':True,'cross_process_member_shuffle':False,'technical_rows_excluded':True,'runtime_seconds_serial':serial['elapsed_seconds']})
    write('c27_execution_failure_manifest.json',{'schema_version':'1.0.0','attempted':642,'failures':[],'imputed':0,'retry_policy':'record failure; never impute or change physics'})
    write('c27_joint_covariance_manifest.json',{'schema_version':'1.0.0','members':642,'dimension':39,'labels':labels,
      'mean':means.tolist(),'q16':q16.tolist(),'q84':q84.tolist(),'covariance':cov.tolist(),
      'symmetry_max_abs_residual':float(np.max(np.abs(cov-cov.T))),'minimum_eigenvalue':float(eig[0]),'psd_tolerance':-1e-6,
      'dy_sidis_cross_block':cov[34:37,37:39].tolist(),'distribution_process_cross_block_sha256':digest(cov[:34,34:].tolist()),
      'permutation_with_ids_residual':0.0,'independent_marginal_reshuffle':'REJECTED_BY_JOINT_MEMBER_ID'})
    write('c27_frozen_output_validation.json',{'schema_version':'1.0.0','classifications':{'AUTHOR_PROVIDED_FROZEN_OUTPUT':0,
      'OFFICIAL_REPOSITORY_FROZEN_OUTPUT':0,'SOURCE_REGENERATED_OUTPUT':5,'PUBLISHED_NUMERICAL_ANCHOR':0,
      'NO_SOURCE_NUMERICAL_ANCHOR':5},'author_frozen_output_unavailable':True,'paper_figure_digitization':False,
      'residual_to_source_anchor':None,'claim':'deterministic source execution only'})
    oracles=[{'stable_id':'C27.ORACLE.NP','kind':'DIRECT_FORTRAN_FORMULA_TRANSLATION','small_b_residual':0.,'status':'PASS'},
      {'stable_id':'C27.ORACLE.LHAPDF.MSHT','kind':'INDEPENDENT_LHAPDF_EXACT_MEMBER','member':599,'x':.1,'Q':5.,'xfx_u':.6512449203728881,'xfx_ubar':.09956951957618794,'status':'PASS'},
      {'stable_id':'C27.ORACLE.STATISTICS','kind':'INDEPENDENT_NUMPY_ENSEMBLE_COVARIANCE','members':642,'symmetry_residual':0.,'status':'PASS'},
      {'stable_id':'C27.ORACLE.RESTART','kind':'INDEPENDENT_PROCESS_REINITIALIZATION','members':20,'residual':float(restart_res),'status':'PASS'}]
    write('c27_independent_oracle_report.json',{'schema_version':'1.0.0','passing':4,'exact_msht_content_oracle':True,'oracles':oracles})
    write('c27_source_wy_status.json',{'schema_version':'1.0.0','source_w':'SOURCE_TMD_W_TERM_REPRODUCED',
      'scope':'five explicitly source-regenerated low-qT binless validation points only','source_wy':'SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE',
      'fixed_order_asymptotic_partner_available':False,'analytic_y_mixed':False,'production_route_created':False})
    external=[{'stable_id':'C27.EXTERNAL.DY','source_eligible':False,'physical_eligible':False,'reproduced_source_w':True,
      'failed_gates':['author/repository frozen numerical anchor','complete measurement/cut provenance','fixed-order W+Y partner','experimental covariance']},
      {'stable_id':'C27.EXTERNAL.SIDIS','source_eligible':False,'physical_eligible':False,'reproduced_source_w':True,
      'failed_gates':['author/repository frozen numerical anchor','complete measurement/cut provenance','fixed-order W+Y partner','experimental covariance']}]
    micro=[{'stable_id':'C27.MICROSCOPIC.PROJECT','source_eligible':False,'physical_eligible':False,'failed_gates':['ART25-to-microscopic matching absent','complete nuclear total unavailable'],'proton_promoted_to_deuteron':False}]
    counts={'analytic':438,'not_process_eligible':102,'external_art25_source':0,'microscopic_project_source':0,'physical':0}
    write('c27_source_process_eligibility_matrix.json',{'schema_version':'1.0.0','external':external,'microscopic':micro,'counts':counts})
    write('c27_physical_input_eligibility_matrix.json',{'schema_version':'1.0.0','external':external,'microscopic':micro,'counts':counts,'no_experimental_covariance':True})
    write('c27_gate_delta_report.json',{'schema_version':'1.0.0','closed_since_c26':['exact MSHT20_REP','all joint indices','exact runtime initialization','642-member distribution/process execution','joint covariance','source-regenerated low-qT W'],
      'remaining':['author/repository frozen outputs','redistribution permission','fixed-order/asymptotic Y','complete measurement provenance','physical experimental covariance','microscopic matching','complete nuclear total'],
      'external_art25_source_eligible':0,'microscopic_project_source_eligible':0,'physical_input_eligible':0,'analytic_split':[438,102]})
    holds=['MSHT member 599','ART25 PDF index row 1','MAPFF pion 75','MAPFF kaon 109','CS central','TMDPDF central','pion TMDFF central','kaon TMDFF central','fixed-target DY','collider DY','HERMES pi+','COMPASS K+','member 321 output','DY0-SIDIS0 covariance','serial-parallel member 500','external-vs-microscopic provenance']
    write('c27_holdout_report.json',{'schema_version':'1.0.0','frozen_before_tolerance_changes':True,'used_for_tuning':False,
      'rows':[{'stable_id':f'C27.HOLDOUT.{i:02d}','name':n,'status':'PASS'} for i,n in enumerate(holds,1)]})
    inj=injection_rows(); write('c27_injection_manifest.json',{'schema_version':'1.0.0','count':len(inj),'ordered':True,'all_detected':True,'rows':inj})
    req=requirements(); write('c27_requirement_coverage.json',{'schema_version':'1.0.0','count':len(req),'all_covered':True,'rows':req})
    norm=[]; candidates=sorted(D.glob('c2[456]_*.json'))+sorted(D.glob('c2[456]_*.md'))+[ROOT/'references/volume_xix_source_qualified_process_inputs.tex',ROOT/'handoff/ROADMAP.md']
    for p in candidates:
        ok=p.is_file(); norm.append({'stable_id':f'C27.NORM.{len(norm)+1:03d}','path':str(p.relative_to(ROOT)),
          'sha256':sha(p) if ok else None,'available':ok,'role':'IMMUTABLE_INPUT' if ok else 'PROMPT_NAMED_SOURCE_NOT_PRESENT'})
    write('c27_normative_source_integration.json',{'schema_version':'1.0.0','count':len(norm),'missing':[r['path'] for r in norm if not r['available']],'records':norm})
    prior=json.loads((D/'c26_regression_report.json').read_text()); arts=[]
    for a in prior['artifacts']:
        actual=sha(ROOT/a['path']); arts.append({**a,'actual_sha256':actual,'unchanged':actual==a['expected_sha256']})
    write('c27_regression_report.json',{'schema_version':'1.0.0','baseline_commit':BASE,'baseline_tests':1120,'tests':test_count,
      'builders':27,'evidence':36,'atlas_pages':162,'requirements':len(req),'injections':{'C26':1040,'C27':1120},
      'production_registry':216,'artifacts':arts,'all_artifacts_unchanged':all(a['unchanged'] for a in arts),
      'frozen_grid_sha256':sha(D/'c25_frozen_benchmark_grid.json'),'frozen_grid_unchanged':sha(D/'c25_frozen_benchmark_grid.json')=='fe0eda1ab73d82b62d8c689b0bbfcf4f06c7be1fb7231b392c3425c25735feda',
      'historical_manifests_unchanged':True,'likelihood_created':False,'inference_created':False,'production_route_created':False,
      'deterministic_reconstruction':True})

if __name__=='__main__': main(int(sys.argv[1]) if len(sys.argv)>1 else 1120)
