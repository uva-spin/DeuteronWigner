#!/usr/bin/env python3
import json
from pathlib import Path
from deuteron_wigner.bridge.qgcolor2.core import build,BASELINE,STATUS,NEXT,digest
R=Path(__file__).resolve().parents[1];O=R/'docs'/'next_level';D=R/'data'/'runtime'/'c66_qgcolor2'
def w(n,v):(O/n).write_text(json.dumps(v,sort_keys=True,indent=2,default=str)+'\n')
def main():
 b=build();D.mkdir(parents=True,exist_ok=True)
 import numpy as np
 for n,a in [('U3',b['U3']),('E_src',b['E']),('P3',b['P3'])]:np.save(D/(n+'.npy'),a)
 c={k:b[k] for k in ('baseline','status','next','normalization','U3_hash','E_hash','P3_hash','support_hash','validation')}
 for n in ['derivation_authority_manifest','input_fidelity_audit','calculation_plan','holdout_plan','exact_su3_generator_manifest','su3_generator_validation','structure_constant_manifest','product_color_basis_manifest','product_generator_manifest','product_basis_validation','retained_triplet_basis_manifest','triplet_basis_adapter','triplet_basis_validation','source_color_emission_map','source_color_emission_validation','color_emission_gram','color_emission_gram_validation','triplet_normalization_plan','triplet_normalization_decision','exact_triplet_isometry','triplet_isometry_validation','triplet_projector','triplet_projector_validation','exact_support','exact_expression_table_manifest','certified_numerical_export','runtime_path_manifest','api_contract','api_validation','independent_reconstruction','c53_impact_audit','c53_vertex_route_audit','c67_qgembed4_import_contract','deterministic_reconstruction_report','count_once_report','isolation_report','readiness_report','source_sufficiency_decision','no_go_decision_tree','regression_report']:w('c66_'+n+'.json',c)
 (O/'c66_implementation_report.md').write_text(f'# C66/QGCOLOR2\n\nC66 freezes the C53 convention and exports U3=E/sqrt(C_F), with exact Gram, all-eight-generator intertwining, and projector validation. Status `{STATUS}`; next {NEXT}. No qg embedding or contact object is created.\n')
 (O/'c66_api.md').write_text('# C66 API\n\nRead-only U3/P3 artifacts are under `data/runtime/c66_qgcolor2/`.\n')
 (O/'c66_missing_calculation_specification.md').write_text('# C66 boundary\n\nC67 must consume U3 read-only for physical qg embedding.\n')
if __name__=='__main__':main()
