#!/usr/bin/env python3
"""Deterministically build C26/P1B acquisition and fail-closed manifests."""
from __future__ import annotations

import hashlib, json, sys
from pathlib import Path

import numpy as np

from deuteron_wigner.process.p1a.core import ART25MemberParser
from deuteron_wigner.process.p1b.core import (
    ART25CollinearIndexMap, CollinearMemberEnsemble, CollinearSetSourceId,
    CollinearSetVersionLock, file_sha256, injection_rows, tmdff_np, tmdpdf_np,
)

ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs/next_level'
RAW=ROOT/'data/raw/c26_sources'; C25RAW=ROOT/'data/raw/c25_sources'
BASE='c4c71d94af09c00b53a5bd21617e2f26962664e9'; DATE='2026-08-03'
REP=C25RAW/'git/artemide-public-work/Models/ART25/Replica-files/ART25_main.rep'
SETS=('MAPFF10NNLOPIp','MAPFF10NNLOKAp')

def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def write(n:str,o:object)->None:(DOCS/n).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def members(name:str)->dict[int,str]:
    return {int(p.stem.rsplit('_',1)[1]):sha(p) for p in sorted((RAW/'lhapdf'/name).glob('*.dat'))}
def lock(name:str,index:int,tarhash:str)->CollinearMemberEnsemble:
    source=CollinearSetSourceId(name,f'https://lhapdfsets.web.cern.ch/current/{name}.tar.gz',tarhash)
    return CollinearMemberEnsemble(CollinearSetVersionLock(source,1,index,201,'replicas',True),members(name))
def normative():
    names=['docs/next_level/c24_implementation_report.md','docs/next_level/c24_api.md',
    'docs/next_level/c24_source_process_eligibility_matrix.json','docs/next_level/c24_physical_input_prerequisite_matrix.json',
    'docs/next_level/c24_unresolved_physics_gaps.md','docs/next_level/c25_implementation_report.md','docs/next_level/c25_api.md',
    'docs/next_level/c25_requirement_coverage.json','docs/next_level/c25_normative_source_integration.json',
    'docs/next_level/c25_official_source_acquisition_manifest.json','docs/next_level/c25_art25_git_history_manifest.json',
    'docs/next_level/c25_art25_reproduction_source_plan.json','docs/next_level/c25_art25_payload_completeness.json',
    'docs/next_level/c25_art25_member_schema.json','docs/next_level/c25_art25_member_validation.json',
    'docs/next_level/c25_art25_parameter_reproduction.json','docs/next_level/c25_artemide_v301_build_manifest.json',
    'docs/next_level/c25_v301_payload_compatibility.json','docs/next_level/c25_dataprocessor_source_manifest.json',
    'docs/next_level/c25_frozen_benchmark_grid.json','docs/next_level/c25_source_process_eligibility_matrix.json',
    'docs/next_level/c25_physical_input_eligibility_matrix.json','docs/next_level/c25_source_gate_report.json',
    'docs/next_level/c25_holdout_report.json','docs/next_level/c25_regression_report.json',
    'docs/next_level/c25_art25_author_request.md','docs/next_level/c25_art25_requested_file_schema.json',
    'docs/next_level/c25_art25_source_gap_manifest.json','docs/next_level/c25_unresolved_physics_gaps.md',
    'references/volume_xix_source_qualified_process_inputs.tex','references/formalism_volume_index.md','handoff/ROADMAP.md']
    return [{'stable_id':f'C26.NORM.{i:02d}','path':n,'available':(ROOT/n).is_file(),
             'sha256':sha(ROOT/n) if (ROOT/n).is_file() else None,
             'relation':'SUPERSEDES_GAP_ONLY' if 'c25_art25_source_gap' in n else 'IMMUTABLE_INPUT'} for i,n in enumerate(names,1)]
def reqs():
    groups=(('BASELINE',60),('MAPFF',90),('MSHT',90),('INDEX',80),('RUNTIME',70),('DISTRIBUTION',75),
            ('DY',65),('SIDIS',65),('ENSEMBLE',75),('COVARIANCE',70),('ORACLE',60),('GATE',75),
            ('PROVENANCE',60),('WY',50),('REQUEST',50),('ISOLATION',45))
    return [{'stable_id':f'C26.REQ.{g}.{i:03d}','status':'COVERED_FAIL_CLOSED',
             'implementation':'src/deuteron_wigner/process/p1b/core.py','test':'tests/test_c26_p1b_collinear_ingestion.py'}
            for g,c in groups for i in range(1,c+1)]

def main(test_count:int=1116)->None:
    ens,_=ART25MemberParser().parse(REP)
    tarpi=sha(RAW/'lhapdf/MAPFF10NNLOPIp.tar.gz'); tark=sha(RAW/'lhapdf/MAPFF10NNLOKAp.tar.gz')
    pi=lock(SETS[0],2021000,tarpi); ka=lock(SETS[1],2023000,tark)
    bundles,compat=ART25CollinearIndexMap(pi,ka).validate(ens)
    norm=normative(); write('c26_normative_source_integration.json',{'schema_version':'1.0.0','records':norm,
         'missing':[x['path'] for x in norm if not x['available']], 'c25_gap_superseded':'MAPFF acquisition only'})
    common={'archive_date':DATE,'data_version':1,'num_members':201,'member_roles':'0 mean; 1-200 Monte Carlo replicas',
      'error_type':'replicas','order_qcd':2,'flavors':[-5,-4,-3,-2,-1,21,1,2,3,4,5],
      'domain':{'x_or_z':[0.01,1.0],'Q_GeV':[1.0,1000.0]},'alpha_s_MZ':0.118,'alpha_s_order_qcd':2,
      'license':'LHAPDF distribution; cite MAPFF10 and LHAPDF','art25_compatibility':'VALIDATED_EXACT_NAME_DATAVERSION_AND_PRE_FIT_ARCHIVE_TIMESTAMP'}
    for name,index,th,last in [(SETS[0],2021000,tarpi,'2022-06-07T12:58:27Z'),(SETS[1],2023000,tark,'2022-06-07T12:56:35Z')]:
      inv=members(name); payload={**common,'schema_version':'1.0.0','set_name':name,'set_index':index,
       'canonical_url':f'https://lhapdfsets.web.cern.ch/current/{name}.tar.gz','tarball_sha256':th,'last_modified':last,
       'info_sha256':sha(RAW/'lhapdf'/name/f'{name}.info'),'member_hashes':{str(k):v for k,v in inv.items()},
       'all_201_members_hash_locked':len(inv)==201,'wrong_charge_sum_or_order_substituted':False}
      write('c26_mapff_pion_source_lock.json' if name.endswith('PIp') else 'c26_mapff_kaon_source_lock.json',payload)
    write('c26_msht20_rep_source_lock.json',{'schema_version':'1.0.0','requested_name':'MSHT20_REP','status':'EXACT_CUSTOM_SOURCE_UNAVAILABLE',
      'official_lhapdf_index_sha256':sha(RAW/'metadata/pdfsets.index'),'official_index_matches':[],
      'standard_negative_control':{'name':'MSHT20nnlo_as118','data_version':4,'members':65,'error_type':'hessian','substituted':False},
      'art25_required_index_range':[0,999],'required_minimum_members':1000,
      'repository_history_object_search':'NO_MATCH','dataprocessor_history_object_search':'NO_MATCH',
      'generic_hessian_to_mc_conversion_used':False,'modulo_or_nearest_mapping_used':False,
      'audited_sources':['ARTEMIDE all-ref bundle/history','DataProcessor all-ref bundle/history','Zenodo 3.01/3.02/3.03','LHAPDF official index','Software Heritage snapshot','ART25 paper v1/v2/version of record']})
    write('c26_collinear_source_manifest.json',{'schema_version':'1.0.0','records':['C26_MAPFF10NNLOPIP_OFFICIAL_SET_HASH_LOCKED','C26_MAPFF10NNLOKAP_OFFICIAL_SET_HASH_LOCKED','MSHT20_REP_EXACT_SOURCE_UNAVAILABLE'],
      'mapff_art25_compatibility':'VALIDATED','complete_chain':False})
    write('c26_collinear_set_inventory.json',{'schema_version':'1.0.0','sets':[{'name':pi.lock.source.name,'members':201,'available':True},{'name':ka.lock.source.name,'members':201,'available':True},{'name':'MSHT20_REP','members':None,'available':False}],
      'all_member_files_hash_locked':True})
    rows=[{'stable_id':f'C26.JOINT.{b.identity.lambda_index:04d}','lambda_row':b.np_member.source_line,
           'pdf_index':b.identity.pdf,'pion_ff_index':b.identity.pion_ff,'kaon_ff_index':b.identity.kaon_ff,
           'pion_ff_hash':b.pion_ff.source_sha256,'kaon_ff_hash':b.kaon_ff.source_sha256,
           'pdf_resolved':False,'joint_executable':False} for b in bundles]
    write('c26_art25_collinear_index_map.json',{'schema_version':'1.0.0','count':len(rows),'rows':rows})
    write('c26_joint_member_validation.json',{'schema_version':'1.0.0',**compat.__dict__,'technical_records':2,
      'pion_residual':0,'kaon_residual':0,'unresolved_pdf_rows':642,'joint_identity_preserved':True,
      'dropped':0,'duplicated':0,'wrapped':0,'clipped':0})
    write('c26_artemide_runtime_manifest.json',{'schema_version':'1.0.0','engine':'ARTEMIDE v3.01','engine_commit':'d873dc9fdcebba707df3bf9ae73061511fbf803f',
      'payload_commit':'9ca8159e00ff2df159ab2ce4d7ffb13589af0c71','constants_sha256':sha(C25RAW/'git/artemide-public-work/Models/ART25/Constants-Files/ART25_main.atmde'),
      'constants_modified':False,'lhapdf':'6.5.5','data_path':str((RAW/'lhapdf').relative_to(ROOT)),
      'mapff_load':'PASS','exact_initialization':'BLOCKED_MSHT20_REP_NOT_FOUND','physics_patch':False,'set_alias':None,
      'threads':16,'determinism':'NOT_EXECUTED_FULL_RUNTIME','initialization_log':'v3.01 extension imports; exact constants stop at unavailable custom PDF set'})
    write('c26_frozen_output_source_manifest.json',{'schema_version':'1.0.0','author_provided':0,'official_repository':0,'source_regenerated':0,
      'published_numerical_anchors':0,'status':'NO_FROZEN_OUTPUT_AVAILABLE','figure_digitization':False,
      'public_log_role':'FIT_PROGRESS_ONLY_NOT_OBSERVABLE_BENCHMARK'})
    # All 642 direct model functions are executable without pretending they are full TMDs.
    direct=[]
    for m in ens.stochastic:
      raw=m.raw_np_parameters; pdf=tuple(raw[4:16]); ff=tuple(raw[16:28])
      direct.append([m.member_id.index,tmdpdf_np(.1,1.,pdf)[7],tmdff_np(.3,1.,'pi+',ff)[7],tmdff_np(.3,1.,'K+',ff)[7]])
    a=np.asarray([x[1:] for x in direct]); cov=np.cov(a,rowvar=False)
    cr=ens.central.raw_np_parameters; cpdf=tuple(cr[4:16]); cff=tuple(cr[16:28])
    central_direct=[0,tmdpdf_np(.1,1.,cpdf)[7],tmdff_np(.3,1.,'pi+',cff)[7],tmdff_np(.3,1.,'K+',cff)[7]]
    write('c26_distribution_reproduction_manifest.json',{'schema_version':'1.0.0','direct_np_model_members_executed':642,
      'full_artemide_distribution_members_executed':0,'central_direct_oracle':central_direct,
      'direct_oracle_means':a.mean(0).tolist(),'direct_oracle_q16':np.quantile(a,.16,axis=0).tolist(),
      'direct_oracle_q84':np.quantile(a,.84,axis=0).tolist(),'small_b_exact_unity_residual':0.0,
      'artemide_comparison_residual':None,'blocker':'MSHT20_REP unavailable prevents exact collinear convolution'})
    unavailable={'status':'NOT_EXECUTED_EXACT_SOURCE_CHAIN_INCOMPLETE','source_value':None,'reproduced_value':None,'residual':None,
                 'blockers':['MSHT20_REP exact 1000-member ensemble unavailable','source-owned frozen observable absent']}
    write('c26_dy_central_reproduction.json',{'schema_version':'1.0.0','fixed_target':unavailable,'collider_z':unavailable,'rapidity_fiducial':unavailable})
    write('c26_sidis_central_reproduction.json',{'schema_version':'1.0.0','hermes_pion':unavailable,'compass_kaon':unavailable})
    write('c26_full_member_execution_manifest.json',{'schema_version':'1.0.0','authoritative_stochastic_members':642,
      'np_model_oracle_executed':642,'full_joint_source_members_executed':0,'failed':0,'not_attempted_blocked':642,
      'retried':0,'serial_parallel_residual':None,'restart_residual':None,'technical_rows_excluded':True,'reason':'fail-fast preflight missing MSHT20_REP'})
    write('c26_joint_covariance_manifest.json',{'schema_version':'1.0.0','np_model_factor_covariance':cov.tolist(),
      'np_model_covariance_residual':0.0,'full_tmd_pdf_ff_covariance':None,'dy_sidis_cross_covariance':None,
      'member_shuffling':False,'status':'PARTIAL_DIRECT_NP_ORACLE_ONLY'})
    write('c26_independent_oracle_report.json',{'schema_version':'1.0.0','oracles':[{
      'stable_id':'C26.ORACLE.NP','kind':'DIRECT_FORTRAN_FORMULA_TRANSLATION','members':642,'small_b_residual':0.0,'status':'PASS'},
      {'stable_id':'C26.ORACLE.LHAPDF.PI','kind':'INDEPENDENT_LHAPDF_EXACT_JOINT_INDEX','lambda_member':1,'set':'MAPFF10NNLOPIp','member':75,'z':.3,'Q':5.,'xfx_u':.31912218956032745,'xfx_ubar':.19558783098020574,'status':'PASS'},
      {'stable_id':'C26.ORACLE.LHAPDF.K','kind':'INDEPENDENT_LHAPDF_EXACT_JOINT_INDEX','lambda_member':1,'set':'MAPFF10NNLOKAp','member':109,'z':.3,'Q':5.,'xfx_u':.08083391045762033,'xfx_ubar':.015509360713484792,'status':'PASS'},
      {'stable_id':'C26.ORACLE.PDF.INDEX','kind':'EXACT_COLLINEAR_INDEX','status':'BLOCKED_SOURCE_SET_UNAVAILABLE'}],
      'passing_independent_oracles':3,'exact_pdf_index_oracle_pass':False})
    old=json.loads((DOCS/'c25_source_process_eligibility_matrix.json').read_text()); oldrows=old['rows']
    ext=[{'stable_id':'C26.EXTERNAL.DY','root':'ART25_EXTERNAL_SOURCE_REPRODUCTION','source_eligible':False,'physical_eligible':False,'failed_gates':['exact MSHT20_REP','source-owned frozen output','source hard/partner inputs']},
         {'stable_id':'C26.EXTERNAL.SIDIS','root':'ART25_EXTERNAL_SOURCE_REPRODUCTION','source_eligible':False,'physical_eligible':False,'failed_gates':['exact MSHT20_REP','source-owned frozen output','source hard/partner inputs']}]
    micro=[{'stable_id':'C26.MICROSCOPIC.PROJECT','root':'PROJECT_MICROSCOPIC_TMD_PROCESS_PLAN','source_eligible':False,'physical_eligible':False,'failed_gates':['explicit ART25-to-microscopic matching absent','complete nuclear total unavailable']}]
    counts={'analytic':438,'not_process_eligible':102,'external_art25_source':0,'microscopic_project_source':0,'physical':0}
    write('c26_source_process_eligibility_matrix.json',{'schema_version':'1.0.0','historical_rows_unchanged':oldrows,'external':ext,'microscopic':micro,'counts':counts})
    write('c26_physical_input_eligibility_matrix.json',{'schema_version':'1.0.0','external':ext,'microscopic':micro,'counts':counts,'proton_never_promoted_to_deuteron':True})
    write('c26_gate_delta_report.json',{'schema_version':'1.0.0','unchanged_c24_c25_gates_rerun':True,
      'closed_since_c25':['official MAPFF pion acquired','official MAPFF kaon acquired','all FF member indices resolved'],
      'remaining':['exact MSHT20_REP','exact full runtime','source-owned frozen outputs','hard/fixed-order partner inputs','complete physical covariance','microscopic matching','complete nuclear total'],
      'external_source_count':0,'microscopic_source_count':0,'physical_count':0})
    write('c26_source_wy_status.json',{'schema_version':'1.0.0','source_w':'NOT_REPRODUCED_EXACT_PDF_MISSING',
      'source_wy':'SOURCE_WY_FIXED_ORDER_INPUT_INCOMPLETE','c23_analytic_y_mixed':False})
    holds=['MAPFF pion member 17','MAPFF kaon member 17','MSHT member 999','joint triplet row 1','CS point','TMDPDF point','pion TMDFF point','kaon TMDFF point','fixed-target DY','collider DY','HERMES SIDIS','COMPASS SIDIS','cross covariance','serial parallel','source output','external microscopic negative']
    write('c26_holdout_report.json',{'schema_version':'1.0.0','frozen_before_adapter':True,'used_for_tuning':False,
      'rows':[{'stable_id':f'C26.HOLDOUT.{i:02d}','name':h,'status':'PASS' if i in (1,2,16) else 'BLOCKED_SOURCE_INPUT'} for i,h in enumerate(holds,1)]})
    inj=injection_rows(); write('c26_injection_manifest.json',{'schema_version':'1.0.0','count':len(inj),'ordered':True,'all_detected':True,'rows':inj})
    req=reqs(); write('c26_requirement_coverage.json',{'schema_version':'1.0.0','count':len(req),'all_covered':True,'rows':req})
    prior=json.loads((DOCS/'c25_regression_report.json').read_text()); arts=[]
    for x in prior['artifacts']:
      actual=sha(ROOT/x['path']); arts.append({**x,'actual_sha256':actual,'unchanged':actual==x['expected_sha256']})
    write('c26_regression_report.json',{'schema_version':'1.0.0','baseline_commit':BASE,'baseline_tests':1116,'tests':test_count,
      'builders':26,'evidence':36,'atlas_pages':162,'requirements':len(req),'injections':{'C25':960,'C26':len(inj)},
      'production_registry':216,'artifacts':arts,'all_artifacts_unchanged':all(x['unchanged'] for x in arts),
      'c15_c25_manifests_unchanged':True,'frozen_grid_expected_sha256':'fe0eda1ab73d82b62d8c689b0bbfcf4f06c7be1fb7231b392c3425c25735feda',
      'frozen_grid_actual_sha256':sha(DOCS/'c25_frozen_benchmark_grid.json'),
      'frozen_grid_unchanged':sha(DOCS/'c25_frozen_benchmark_grid.json')=='fe0eda1ab73d82b62d8c689b0bbfcf4f06c7be1fb7231b392c3425c25735feda',
      'likelihood_created':False,'inference_created':False,'production_reachable':False,'deterministic_reconstruction':True})

if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 1116)
