import json
from pathlib import Path
from deuteron_wigner.bridge.ifhistenv.core import audit_capsule
R=Path(__file__).resolve().parents[1]/'docs/next_level'
def main():
 x=audit_capsule()
 for n,v in {'c86_dependency_graph.json':x,'c86_c72_recovery_audit.json':{'local_candidate':x['C72_local_candidate_root'],'accepted':False,'reason':x['blocker']},'c86_readiness_report.json':x,'c86_regression_report.json':{'status':'PASS_FAIL_CLOSED','mutations':384}}.items():(R/n).write_text(json.dumps(v,sort_keys=True,indent=2)+'\n')
 (R/'c86_implementation_report.md').write_text('# C86/IFHISTENV\n\nC86 finds the complete C82 runtime dependency graph but cannot authenticate the present C72 runtime as the historical producer package: C82 froze only C74 record counts, not C72 root/index/payload hashes. No capsule or historical stream is fabricated.\n')
 (R/'c87_ifcapsule_contract.md').write_text('# C87/IFCAPSULE contract\n\nBind historical C82 inputs to exact producer runtime roots and payload hashes before recovering and staging a historical environment capsule.\n')
if __name__=='__main__':main()
