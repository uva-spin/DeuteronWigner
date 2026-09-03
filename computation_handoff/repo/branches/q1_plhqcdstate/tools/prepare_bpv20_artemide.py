#!/usr/bin/env python3
"""Prepare the vendored arTeMiDe v2.05 tree for the BPV20 proton sector.

BPV20's historical constants file initializes pion PDFs and fragmentation
functions used by its global-fit programs.  Evaluating the proton Sivers TMD
does not use those objects, and their old LHAPDF set names are no longer in
the current public registry.  This reproducible transformation retains the
fit's NNPDF31 proton input while disabling only the unused pion/FF inputs.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil


def replace_section(text: str, start: str, end: str, replacement: str) -> str:
    first = text.index(start)
    last = text.index(end, first)
    return text[:first] + replacement.rstrip() + "\n\n" + text[last:]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root", type=Path, default=Path("data/vendor/artemide-v2.05")
    )
    parser.add_argument(
        "--constants-output",
        type=Path,
        default=Path("build/artemide/const-BPV20_n3lo-proton-sivers"),
    )
    args = parser.parse_args()

    model_dir = args.root / "Models/BPV20/Model"
    target_dir = args.root / "src/Model"
    for source in model_dir.glob("*.f90"):
        shutil.copy2(source, target_dir / source.name)

    source_constants = (
        args.root / "Models/BPV20/Constants-files/const-BPV20_n3lo"
    )
    text = source_constants.read_text()
    text = replace_section(
        text,
        "*B   : ---- uPDF sets----",
        "*C   : ---- uFF sets----",
        """*B   : ---- uPDF sets----
*p1  : total number of PDFs to initialize (0= initialization is skipped)
           1
*p2  : reference number for hadrons
    1
*p3  : LHAPDF set names for hadrons (line-by-line corresponding to reference number
 NNPDF31_nnlo_as_0118_1000
*p4  : list of initialization replicas
    0""",
    )
    text = replace_section(
        text,
        "*C   : ---- uFF sets----",
        "*D   : ----lpPDF sets----",
        """*C   : ---- uFF sets----
*p1  : total number of FFs to initialize (0= initialization is skipped)
           0
*p2  : reference number for hadrons
    0
*p3  : LHAPDF set names for hadrons (line-by-line corresponding to reference number
*p4  : list of initialization replicas
    0""",
    )
    # The constants file also asks uTMDPDF to prebuild hadrons 1 and 2 even
    # though the proton-only QCD input above now has only hadron 1.
    utmd_start = text.index("# ----                           PARAMETERS OF uTMDPDF")
    utmd_end = text.index("# ----                           PARAMETERS OF uTMDFF", utmd_start)
    utmd = text[utmd_start:utmd_end]
    utmd = utmd.replace(
        """*p3  : total number of PDFs added to the grid (by default it coincides with number of initialized PDFs)
           2
*p4  : reference numbers for hadrons (by default it coincides with references for PDFs)
    1,     2""",
        """*p3  : total number of PDFs added to the grid (by default it coincides with number of initialized PDFs)
           1
*p4  : reference numbers for hadrons (by default it coincides with references for PDFs)
    1""",
    )
    text = text[:utmd_start] + utmd + text[utmd_end:]

    # Fragmentation functions are outside the proton Sivers evaluation and
    # their QCD inputs were intentionally disabled above.
    uff_start = text.index("# ----                           PARAMETERS OF uTMDFF")
    uff_end = text.index("# ----                            PARAMETERS OF TMDs", uff_start)
    uff = text[uff_start:uff_end].replace(
        "*p1  : initialize uTMDFF module\n T",
        "*p1  : initialize uTMDFF module\n F",
        1,
    )
    uff = uff.replace(
        """*p3  : total number of FFs added to the grid (by default it coincides with number of initialized FFs)
           2
*p4  : reference numbers for hadrons (by default it coincides with references for FFs)
    1,     2""",
        """*p3  : total number of FFs added to the grid (by default it coincides with number of initialized FFs)
           0
*p4  : reference numbers for hadrons (by default it coincides with references for FFs)
    0""",
    )
    text = text[:uff_start] + uff + text[uff_end:]
    args.constants_output.parent.mkdir(parents=True, exist_ok=True)
    args.constants_output.write_text(text)
    print(args.constants_output)


if __name__ == "__main__":
    main()
