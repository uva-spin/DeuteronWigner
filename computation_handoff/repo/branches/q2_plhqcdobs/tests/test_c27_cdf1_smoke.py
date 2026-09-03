import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs/next_level'
def load(n): return json.loads((D/n).read_text())

def test_native_loader_and_public_art25_selection():
    m=load('c27_cdf1_dataset_manifest.json')
    assert m['cdf1']['sha256']=='c0a178d9579017a7de91abf63df667d1bb3009253ce15b56fe428d32fc430c81'
    assert m['dataset']['number_of_points']==50
    assert m['art25']['selection_status']=='EXACT_PUBLIC_ART25_SELECTION_FOUND'
    assert m['art25']['retained_ids']==[f'CDF1.{i}' for i in range(33)]

def test_native_prediction_and_determinism():
    n=load('c27_cdf1_native_prediction.json'); c=load('c27_cdf1_comparison_report.json')
    assert n['point_id']=='CDF1.0' and n['entire_selected_dataset_count']==33
    assert n['central_native_value']==3.4394876804377352
    assert n['serial_residual']==n['clean_reinitialization_residual']==n['restart_residual']==0
    assert c['B_existing_c27']['exact_match'] is False
    assert c['C_controlled_oracle']['native_residual']==0

def test_code_path_is_w_only_and_diagnostic():
    p=load('c27_cdf1_code_path_manifest.json')['observable']
    assert p['factorization']=='LOW_qT_LP_TMD_W_ONLY'
    assert p['fixed_order_Y'] is False and p['matching'] is False
    assert load('c27_cdf1_comparison_report.json')['classification']=='DIAGNOSTIC_ONLY'
