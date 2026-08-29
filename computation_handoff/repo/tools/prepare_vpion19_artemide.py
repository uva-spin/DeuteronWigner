#!/usr/bin/env python3
"""Prepare high-order Vpion19/JAM21-transfer arTeMiDe constants.

The compiled vendored model already combines the Vpion19 pion profile with
BSV19 evolution.  The proton-only BPV20 setup intentionally removes hadron
2; this tool restores the original two-PDF QCD input and uTMDPDF grids while
disabling unrelated fragmentation modules. JAM18 is no longer distributed
by the official LHAPDF archive; the maintained JAM21 replacement is explicit
in the generated constants and remains an input-transfer scenario, not a
refit of the Vpion19 nonperturbative parameters.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def section(text: str, start: str, end: str) -> tuple[int, int, str]:
    first = text.index(start)
    last = text.index(end, first)
    return first, last, text[first:last]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root", type=Path, default=Path("data/vendor/artemide-v2.05")
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("build/artemide/const-Vpion19-native"),
    )
    arguments = parser.parse_args()
    source = (
        arguments.root / "Models/BPV20/Constants-files/const-BPV20_n3lo"
    )
    text = source.read_text()
    text = text.replace(" JAM18PionPDFnlo", " JAM21PionPDFnlo", 1)
    # Fragmentation inputs play no role in uTMDPDF evaluation.
    first, last, block = section(
        text, "*C   : ---- uFF sets----", "*D   : ----lpPDF sets----"
    )
    block = """*C   : ---- uFF sets----
*p1  : total number of FFs to initialize (0= initialization is skipped)
           0
*p2  : reference number for hadrons
    0
*p3  : LHAPDF set names for hadrons (line-by-line corresponding to reference number
*p4  : list of initialization replicas
    0

"""
    text = text[:first] + block + text[last:]
    first, last, block = section(
        text,
        "# ----                           PARAMETERS OF uTMDFF",
        "# ----                            PARAMETERS OF TMDs",
    )
    block = block.replace(
        "*p1  : initialize uTMDFF module\n T",
        "*p1  : initialize uTMDFF module\n F",
        1,
    )
    text = text[:first] + block + text[last:]
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(text)
    print(arguments.output)


if __name__ == "__main__":
    main()
