#!/usr/bin/env python3
"""Persist the independent uncertainty-axis catalog and refusal evidence."""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path

from deuteron_wigner.uncertainty_axes import (
    EnsembleKind,
    SeparatedUncertaintyLedger,
    UncertaintyAxis,
    UncertaintyEnsemble,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs/validation/uncertainty_axes.audit.json"

SPECS = (
    ("six_wave_functions", UncertaintyAxis.WAVE_FUNCTION,
     EnsembleKind.SENSITIVITY_ENVELOPE,
     ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib"), "av18",
     "project wave tables", ("x", "k", "flavor", "tmd")),
    ("lf_quadrature", UncertaintyAxis.INTERNAL_QUADRATURE,
     EnsembleKind.CONVERGENCE_SEQUENCE,
     ("medium", "fine", "ultrafine"), "ultrafine",
     "production convergence audits", ("wave", "x", "k", "tmd")),
    ("external_grid", UncertaintyAxis.EXTERNAL_GRID,
     EnsembleKind.CONVERGENCE_SEQUENCE,
     ("coarse", "refined"), "refined",
     "parent x-grid convergence", ("x", "flavor", "mechanism")),
    ("fourier_transform", UncertaintyAxis.TRANSFORM,
     EnsembleKind.CONVERGENCE_SEQUENCE,
     ("nominal", "extended"), "nominal",
     "rank-aware transform convergence", ("rank", "k", "tmd")),
    ("fit_inputs", UncertaintyAxis.PDF_TMD_FIT,
     EnsembleKind.MONTE_CARLO,
     ("central", "replicas"), "central",
     "BPV20/JAMDiFF/JAM21 native member releases", ("x", "k", "flavor", "wave")),
    ("evolution_profiles", UncertaintyAxis.EVOLUTION_PROFILE,
     EnsembleKind.SENSITIVITY_ENVELOPE,
     ("low", "central", "high"), "central",
     "declared in-house CSS profile family", ("x", "b", "parton_sector")),
    ("nuclear_mechanisms", UncertaintyAxis.NUCLEAR_MECHANISM,
     EnsembleKind.CORRELATED_SCENARIOS,
     ("central", "named_responses"), "central",
     "H1-DPDF/FGS and configurable mechanism ledgers",
     ("x", "flavor", "wave", "mechanism")),
)


def main() -> None:
    ensembles = {}
    for name, axis, kind, members, central, source, dimensions in SPECS:
        ensembles[name] = UncertaintyEnsemble(
            name=name,
            axis=axis,
            kind=kind,
            member_ids=members,
            source=source,
            central_member=central,
            correlated_dimensions=dimensions,
        )
    ledger = SeparatedUncertaintyLedger(ensembles)
    ledger.require_all_axes()
    refusal = None
    try:
        ledger.joint_covariance()
    except ValueError as exc:
        refusal = str(exc)
    if refusal is None:
        raise RuntimeError("unsourced joint covariance was not refused")
    report = {
        "axes": {
            name: {
                **asdict(item),
                "axis": item.axis.value,
                "kind": item.kind.value,
            }
            for name, item in ensembles.items()
        },
        "all_required_axes_present": True,
        "kept_separate": True,
        "unsourced_joint_covariance_refused": True,
        "refusal_reason": refusal,
        "joint_probability_status": (
            "unavailable across wave/PDF-TMD/evolution/nuclear sources"
        ),
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "axes": len(ledger.axes),
        "kept_separate": True,
    }, indent=2))


if __name__ == "__main__":
    main()
