import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_wp11_final_audit_is_reproducible_and_complete():
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/build_wp11_final_audit.py")],
        cwd=ROOT, check=True,
    )
    report = json.loads(
        (ROOT / "outputs/validation/wp11_final_acceptance.json").read_text()
    )
    assert report["status"] == "pass"
    assert [x["id"] for x in report["criteria"]] == [
        "C1", "C2", "C3", "C4", "C5", "C6", "C7"
    ]
    assert all(x["status"] == "pass" and not x["missing"]
               for x in report["criteria"])
