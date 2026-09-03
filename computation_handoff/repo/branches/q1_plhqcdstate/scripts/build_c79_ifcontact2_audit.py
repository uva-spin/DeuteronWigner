"""Write C79's reproducible no-go audit; it never writes contact arrays."""
from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.bridge.ifcontact2.core import evaluate_readiness

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"


def serialise(value):
    if hasattr(value, "items"):
        return dict(value)
    if isinstance(value, tuple):
        return list(value)
    return str(value)


def write(name: str, value) -> None:
    (DOCS / name).write_text(json.dumps(value, sort_keys=True, indent=2, default=serialise) + "\n")


def main() -> None:
    audit = evaluate_readiness()
    write("c79_input_freeze.json", audit["C78_freeze"])
    write("c79_operator_coefficient_routes.json", audit["operator_routes"])
    write("c79_claim_vs_implementation_inventory.json", {"status": audit["status"], "rows": audit["inventory"]})
    write("c79_blocked_coordinate_domains.json", {"domains": audit["blocked_coordinate_domains"], "evaluation": "NOT_STARTED; no terminal values assigned"})
    write("c79_forbidden_substitution_audit.json", {"forbidden": audit["prohibited_substitutions"], "C53_values_used": False, "C58_values_used": False, "C50_as_contact": False})
    write("c79_readiness_report.json", audit)
    (DOCS / "c79_missing_calculation_specification.md").write_text(
        "# C80/IFKERNEL2 required calculation\n\n"
        "Before a C79 contact coordinate can be evaluated, derive from the C43/C55 W3 operator and C45 field expansions the normalized finite-cell plane-wave `b† a† a b` matrix element. The derivation must retain the ordered `T^a T^b`, the complete-right-product PV/Q0 inverse derivative, two transverse polarization labels, exact finite-cell factors, and the local four-HO overlap. Then map that kernel into C77 raw components and C78's immutable kernel coordinates, prove its P-minus-to-M-squared conversion, and only then stream the three C78 domains. C50's one-gluon b†a†b evaluator, C53 propagation, and C58 self-induced inertia remain invalid substitutes.\n"
    )
    (DOCS / "c79_implementation_report.md").write_text(
        "# C79/IFCONTACT2 — fail-closed direct-contact evaluation audit\n\n"
        "C79 authenticates the immutable C78 support package and re-closes the C43/C55 source-level W3 coefficient by both available symbolic routes. It does not assign a single direct-contact value: the repository has no source-derived finite-cell four-mode `b† a† a b` evaluator. The existing C50 finite-cell routine is a different three-mode canonical q-to-qg vertex and cannot supply the contact's measure, two-gluon spin/polarization contraction, ordered color product, or four-HO integral.\n\n"
        "Therefore `C79_IFCONTACT_KERNEL_EVALUATION_INCOMPLETE` supersedes any implication that C78 support alone permits a contact matrix. No sparse or matrix-free contact matrix, physical coupling, counterterm, renormalized operator, or C58/C53 substitution has been created.\n"
    )


if __name__ == "__main__":
    main()
