#!/usr/bin/env python3
"""Render and structurally audit every page of the authoritative TMD atlases."""

import json
from pathlib import Path

import fitz
import numpy as np

ATLASES = {
    "quark": (
        Path("outputs/parent_tmds/ensemble/quark_parent_tmd_atlas.pdf"), 72
    ),
    "gluon": (
        Path("outputs/parent_tmds/ensemble/gluon_parent_tmd_atlas.pdf"), 18
    ),
    "quark_sources": (
        Path(
            "outputs/parent_tmds/ensemble/"
            "quark_flavor_source_decomposition_atlas.pdf"
        ),
        72,
    ),
}
OUT = Path("outputs/validation/tmd_atlas_pdf_audit.json")


def main() -> None:
    reports = {}
    all_pass = True
    for name, (path, expected_pages) in ATLASES.items():
        document = fitz.open(path)
        titles = []
        ink = []
        for page in document:
            text = page.get_text("text")
            title = next(
                (
                    line.strip() for line in text.splitlines()
                    if line.startswith(("Parent-derived", "Retained flavor sources"))
                ),
                "",
            )
            titles.append(title)
            pixmap = page.get_pixmap(matrix=fitz.Matrix(0.7, 0.7), alpha=False)
            pixels = np.frombuffer(pixmap.samples, dtype=np.uint8).reshape(
                pixmap.height, pixmap.width, pixmap.n
            )[:, :, :3]
            ink.append(float(np.mean(np.any(pixels < 245, axis=2))))
        passed = (
            len(document) == expected_pages
            and len(set(titles)) == expected_pages
            and all(title for title in titles)
            and min(ink) > 0.01
            and max(ink) < 0.65
        )
        reports[name] = {
            "path": str(path), "pages": len(document),
            "expected_pages": expected_pages, "unique_titles": len(set(titles)),
            "minimum_ink_fraction": min(ink), "maximum_ink_fraction": max(ink),
            "all_pages_rendered": True, "passed": passed,
        }
        all_pass &= passed
    report = {
        "status": "pass" if all_pass else "fail",
        "renderer": "PyMuPDF fallback; Poppler unavailable",
        "scope": "every page of all authoritative quark/gluon TMD atlases",
        "atlases": reports,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    if not all_pass:
        raise SystemExit("TMD atlas PDF audit failed")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
