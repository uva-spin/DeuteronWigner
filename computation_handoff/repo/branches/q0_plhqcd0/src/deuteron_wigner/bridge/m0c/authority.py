"""Do not derive C42 operators without the exact required primary sources."""
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
STATUS="C42_GAUGE_FIXED_ACTION_INCOMPLETE"
SOURCES=(
 ("Brodsky-Pauli-Pinsky", "hep-ph/9705477", ROOT/"data/raw/c42_sources/hep-ph-9705477.pdf", "LF QCD Hamiltonian, constraints, Fock normalization"),
 ("Belitsky-Ji-Yuan", "hep-ph/0208038", ROOT/"data/raw/c42_sources/hep-ph-0208038.pdf", "transverse link and residual-gauge completion"),
 ("Ji-Ma-Yuan", "hep-ph/0404183", ROOT/"data/raw/c36_sources/hep-ph-0404183.pdf", "selected spacelike TMD and soft convention"),
)
def authority_audit():
    records=[]
    for author,identifier,path,purpose in SOURCES:
        present=path.is_file()
        records.append({"authority":author,"identifier":identifier,"expected_repository_path":str(path.relative_to(ROOT)),"purpose":purpose,"present":present,"sha256":sha256(path.read_bytes()).hexdigest() if present else None,
                        "status":"HASH_LOCKED" if present else "ABSENT_BLOCKING"})
    return {"status":STATUS,"records":records,"missing_required":[r["identifier"] for r in records if not r["present"]],"decision":"No gauge-fixed finite-basis action can be derived or numerically materialized from incomplete primary authorities."}
def assert_gauge_action_incomplete():
    audit=authority_audit(); assert audit["status"]==STATUS
    assert set(audit["missing_required"])=={"hep-ph/9705477","hep-ph/0208038"}
    return audit

def validate_authority_records(records):
    """Validate exact source IDs, paths, presence and hash against filesystem."""
    expected=authority_audit()["records"]
    if len(records)!=len(expected): return False
    for got,want in zip(records,expected):
        for key in ("authority","identifier","expected_repository_path","present","sha256","status"):
            if got.get(key)!=want.get(key): return False
    return True
