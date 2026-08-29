"""Build the Q1/PLHQCDSTATE acceptance report."""

from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge import plhqcdstate as q1
from deuteron_wigner.bridge.plhqcdstate import core as q1core


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"


def main() -> None:
    report = q1.build_q1_report()
    (DOCS / "q1_plhqcdstate_acceptance.json").write_text(
        json.dumps(q1core._jsonable(report), indent=2, sort_keys=True) + "\n"
    )
    print(report["status"], report["positive_gate"], report["root"])


if __name__ == "__main__":
    main()
