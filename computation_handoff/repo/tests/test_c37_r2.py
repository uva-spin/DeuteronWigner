import json
from pathlib import Path
from deuteron_wigner.bridge import r2
ROOT=Path(__file__).resolve().parents[1]
def test_c37_fails_closed_before_any_fictitious_matching():
 b=r2.blocker(); assert b.status==r2.C37_NO_GO and len(b.missing)==5
def test_c37_has_required_injections_and_no_export():
 docs=ROOT/'docs/next_level'; assert json.loads((docs/'c37_injection_manifest.json').read_text())['count']>=2840
 assert json.loads((docs/'c37_hadron_application_gate.json').read_text())['gate']['microscopic_export']==r2.EMPTY_NOT_ZERO
