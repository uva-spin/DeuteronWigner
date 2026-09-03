import json
from pathlib import Path
import pytest

from deuteron_wigner.process.p1a.core import ART25MemberParser
from deuteron_wigner.process.p1b.core import *

ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs/next_level'
REP=ROOT/'data/raw/c25_sources/git/artemide-public-work/Models/ART25/Replica-files/ART25_main.rep'
def load(n):return json.loads((D/n).read_text())
def ensemble(name,index):
    m={int(p.stem.rsplit('_',1)[1]):file_sha256(p) for p in (ROOT/'data/raw/c26_sources/lhapdf'/name).glob('*.dat')}
    s=CollinearSetSourceId(name,'official','hash')
    return CollinearMemberEnsemble(CollinearSetVersionLock(s,1,index,201,'replicas',True),m)

def test_all_art25_ff_indices_resolve_without_mapping():
    art,_=ART25MemberParser().parse(REP)
    bundles,report=ART25CollinearIndexMap(ensemble('MAPFF10NNLOPIp',2021000),ensemble('MAPFF10NNLOKAp',2023000)).validate(art)
    assert len(bundles)==642 and report.ff_indices_resolved==1284
    assert report.pion_range==report.kaon_range==(0,199)
    assert report.pdf_range==(0,999) and report.exact_joint_bundles_executable==0
    assert bundles[0].identity.pdf==599 and bundles[0].identity.pion_ff==75 and bundles[0].identity.kaon_ff==109

def test_out_of_range_fails_instead_of_wrapping():
    with pytest.raises(ValueError,match='INDEX_OUT_OF_RANGE'):
        ensemble('MAPFF10NNLOPIp',2021000).resolve(201)

def test_independent_np_oracles_and_limits():
    p=(.486,.041,.569,.147,5.26,21.12,7.71,.156,.240,.069,1.,1.)
    f=(.696,.626,.003,-.466,.884,.882,1.742,1.15,.610,-.101,0.,.1)
    assert max(abs(x-1) for x in tmdpdf_np(.1,0,p))==0
    assert max(abs(x-1) for x in tmdff_np(.3,0,'pi+',f))==0
    assert max(abs(x-1) for x in tmdff_np(.3,0,'K+',f))==0

def test_fail_closed_manifests_and_injections():
    assert load('c26_msht20_rep_source_lock.json')['standard_negative_control']['substituted'] is False
    assert load('c26_full_member_execution_manifest.json')['full_joint_source_members_executed']==0
    rows=injection_rows(); assert len(rows)==1040 and [x['ordinal'] for x in rows]==list(range(1,1041))
    assert load('c26_regression_report.json')['all_artifacts_unchanged']
