"""Build the Q2/PLHQCDOBS acceptance and runtime manifests."""

from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.quantum import plhqcdobs as q2


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"
RUNTIME = ROOT / "data/runtime/q2_plhqcdobs"


def main() -> None:
    report = q2.build_q2_report()
    payload = q2._jsonable(report)
    (DOCS / "q2_plhqcdobs_acceptance.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    runtime = {
        "schema": "Q2-PLHQCDOBS-RUNTIME-MANIFEST-V1",
        "status": report["status"],
        "positive_gate": report["positive_gate"],
        "package": "deuteron_wigner.quantum.plhqcdobs",
        "source_structured": True,
        "ordinary_gate_only": True,
        "production_qubitunitary_count": 0,
        "device": q2.DEVICE,
        "shots": q2.SHOTS,
        "root": report["root"],
    }
    RUNTIME.mkdir(parents=True, exist_ok=True)
    (RUNTIME / "manifest.json").write_text(json.dumps(runtime, indent=2, sort_keys=True) + "\n")
    print(report["status"], report["positive_gate"], report["root"])


if __name__ == "__main__":
    main()
