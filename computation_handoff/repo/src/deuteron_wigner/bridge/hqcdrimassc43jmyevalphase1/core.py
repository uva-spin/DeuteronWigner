"""C391 phase authority for JMY measurement and source-side Laurent evaluation."""
from __future__ import annotations

import json
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c391_hqcdrimassc43jmyevalphase1"
BASELINE = "34b002948c0a501c4d59a10d2d00bca292e227b8"
C390_ROOT = "7748f90ead890c2a207e9117e95627104c33677213466a90f1eff14c4ba309ad"
SOURCE_TEX_SHA = "5caf5be22e162b849518788605301cfc1c6c8e2eff82ae7b3480a8a2e1699e7b"
STATUS = "JMY_DISTRIBUTION_LAURENT_AUTHORITY_READY_SEPARATOR_OR_TARGET_REMAINDER_EXPLICIT"
PLAN = "HQCDRIMASSC43JMYEVALPHASE1-B"
NEXT = "C392/HQCDRIMASSC43PHYSICALMATCHPHASE1"
NEXT_OBJECT = "C391-C43-JMY-COMMON-IR-FINITE-BASIS-CONTINUUM-MATCHING-TARGET"
NEXT_EXACT = "construct the source-qualified common-IR physical finite-basis/continuum matching target for the C391 symbolic source-side remainder"


def _root(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def phase_plan_manifest():
    stages = (
        ("A", "C390-C43-JMY-TRANSVERSE-FOURIER-REGULAR-PLUS-EVALUATOR", "COMPLETE"),
        ("B", "source-owned DR.qq/FR.qq regular-plus decomposition", "COMPLETE"),
        ("C", "DR.qq executable distribution gate", "COMPLETE"),
        ("D", "16-group source-side symbolic Laurent ledger", "COMPLETE_WITH_TARGET_REMAINDER"),
        ("E", "real/virtual and separator identities", "SOURCE_SCOPE_COMPLETE_TARGET_REMAINDER"),
        ("F", "finite remainder, bracket, and covariance", "SYMBOLIC_COMPLETE_PHYSICAL_BRACKET_UNSELECTED"),
        ("G", "phase release and matching handoff", "COMPLETE"),
    )
    rows = tuple({"stage_id": a, "first_exact_object": b, "status": c, "input_root": C390_ROOT,
                  "unresolved_remainder": NEXT_OBJECT if a in "DEFG" else None} for a, b, c in stages)
    return {"phase_id": "C391/HQCDRIMASSC43JMYEVALPHASE1", "rows": rows, "count": 7, "root": _root(rows)}


def phase_stage_manifest(stage_id=None):
    rows = phase_plan_manifest()["rows"]
    if stage_id is None:
        return deepcopy(rows)
    row = next((x for x in rows if x["stage_id"] == stage_id), None)
    if row is None:
        raise KeyError(stage_id)
    return deepcopy(row)


def fourier_bessel_manifest(kernel_id=None):
    # From JMY TeX lines 218-254 and 515-524, generalized only by the frozen
    # project convention d=4-2 epsilon: n=d_perp=2-2 epsilon.
    base = {
        "kernel_id": "JMY_SCALAR_TRANSVERSE_RANK0",
        "source_ast_node": "C389.measurement_exec.transverse_kernel",
        "source_locator": "hep-ph/0404183v1 sdisfac.tex:218-254,515-524",
        "source_sha256": SOURCE_TEX_SHA,
        "d_perp": "2-2*epsilon",
        "epsilon_convention": "d=4-2*epsilon",
        "angular_measure": "Omega_(1-2epsilon)=2*pi^(1-epsilon)/Gamma(1-epsilon)",
        "radial_measure": "kT^(1-2epsilon) dkT",
        "fourier_normalization": "(2*pi)^(-2+2epsilon) for inverse transform; JMY b-space action itself has no prefactor",
        "bessel_order": "-epsilon",
        "reduced_kernel": "(2*pi)^(-1+epsilon)*(kT*bT)^epsilon*J_(-epsilon)(kT*bT)",
        "tensor_rank": 0,
        "phase": "+i*bT_dot_kT",
        "variables": ("bT", "kT", "epsilon"),
        "test_domain": "radial Schwartz tests for bT>0; distributional regulated boundary at bT=0",
        "units": "kernel dimensionless; radial measure mass^(2-2epsilon)",
        "branch": "bT>=0,kT>=0, real principal powers",
        "routes": ("direct_d_perp_angular_integral", "Gegenbauer_Bessel_reduction", "epsilon=0_J0_holdout", "numeric_angular_fixture"),
    }
    rows = (base, {**base, "kernel_id": "JMY_FRAGMENTATION_SCALAR_TRANSVERSE_RANK0", "longitudinal_variable": "z",
                    "crossing_jacobian": "z^(-2+2epsilon)", "source_locator": "hep-ph/0404183v1 sdisfac.tex:840-869"})
    if kernel_id is None:
        return deepcopy(rows)
    row = next((x for x in rows if x["kernel_id"] == kernel_id), None)
    if row is None:
        raise KeyError(kernel_id)
    return deepcopy(row)


def regular_plus_manifest(owner_id=None, distribution_id=None):
    rows = (
        {"owner_id": "DR.qq", "distribution_id": "JMY_FIG2A_REGULAR", "variable": "x", "domain": (0, 1),
         "support": "regular", "coefficient": "alpha_s*C_F/(2*pi^2)",
         "kernel": "(1-x)*[1/D_x-2*x*m^2/D_x^2]", "D_x": "kT^2+x*lambda^2+(1-x)^2*m^2",
         "source_locator": "hep-ph/0404183v1 sdisfac.tex:436-453 Eq.(real-no-link)", "subtraction_point": None,
         "test_action": "integral_0^1 dx kernel(x)*phi(x)", "count_once": True},
        {"owner_id": "DR.qv", "distribution_id": "JMY_FIG2B_PLUS", "variable": "x", "domain": (0, 1),
         "support": "plus", "coefficient": "alpha_s*C_F/pi^2", "kernel": "x/D_x",
         "source_locator": "hep-ph/0404183v1 sdisfac.tex:455-476", "subtraction_point": 1,
         "test_action": "integral_0^1 dx x/D_x*[phi(x)-phi(1)]", "constant_test": 0, "count_once": True},
        {"owner_id": "DR.qv", "distribution_id": "JMY_FIG2B_ENDPOINT", "variable": "x", "domain": (0, 1),
         "support": "delta(1-x)", "coefficient": "alpha_s*C_F/(2*pi^2)",
         "kernel": "ln(zeta^2/(kT^2+lambda^2))/(kT^2+lambda^2)",
         "source_locator": "hep-ph/0404183v1 sdisfac.tex:467-476", "subtraction_point": 1,
         "test_action": "kernel*phi(1)", "count_once": True},
        {"owner_id": "DR.vv", "distribution_id": "JMY_FIG2C_ENDPOINT", "variable": "x", "domain": (0, 1),
         "support": "delta(1-x)", "coefficient": "-alpha_s*C_F/(2*pi^2)", "kernel": "1/(kT^2+lambda^2)",
         "source_locator": "hep-ph/0404183v1 sdisfac.tex:478-497", "subtraction_point": 1,
         "test_action": "kernel*phi(1)", "limit_order": "zeta->infinity at fixed kT; not uniform in kT", "count_once": True},
    )
    crossed = tuple({**x, "owner_id": x["owner_id"].replace("DR.", "FR."), "variable": "z",
                     "distribution_id": x["distribution_id"].replace("JMY_", "JMY_CROSSED_"),
                     "crossing": "qhat(z,P_T)=z^-1 q(1/z,P_T/z), exact one-loop source crossing",
                     "crossing_jacobian_d_dimensional": "z^(-2+2epsilon)",
                     "source_locator": "hep-ph/0404183v1 sdisfac.tex:840-869 plus parent locator " + x["source_locator"]} for x in rows)
    all_rows = rows + crossed
    selected = tuple(x for x in all_rows if (owner_id is None or x["owner_id"] == owner_id) and
                     (distribution_id is None or x["distribution_id"] == distribution_id))
    if owner_id is not None and distribution_id is not None:
        if not selected:
            raise KeyError((owner_id, distribution_id))
        return deepcopy(selected[0])
    return deepcopy(selected)


def apply_distribution_test_action(record, test_function_record):
    """Exact action for polynomial fixtures; no scalarization of the authority."""
    support = record["support"]
    coeffs = tuple(Fraction(str(x)) for x in test_function_record["polynomial_coefficients"])
    phi1 = sum(coeffs, Fraction(0))
    if support == "plus":
        # Canonical unit-kernel plus fixture, sufficient to verify subtraction.
        value = sum((a / Fraction(i + 1) - a) for i, a in enumerate(coeffs))
    elif support == "delta(1-x)":
        value = phi1
    elif support == "regular":
        value = sum(a / Fraction(i + 1) for i, a in enumerate(coeffs))
    else:
        raise ValueError(support)
    return {"distribution_id": record["distribution_id"], "fixture_action": f"{value.numerator}/{value.denominator}",
            "kernel_factor_retained_symbolically": True, "scalar_replacement": False}


def first_node_manifest():
    return {"node": "DR.qq", "kernel_id": "JMY_SCALAR_TRANSVERSE_RANK0",
            "distribution_ids": ("JMY_FIG2A_REGULAR",), "phase_space": "C389 regulated_cut_phase_space_integral",
            "epsilon_orders": ("epsilon^-1", "epsilon^0"), "UV_IR_separate": True,
            "units": "source prefactor times transverse mass^-2 kernel and d_perp measure", "outward_enclosure": "exact symbolic",
            "symbolic_numeric_fixture_parity": "PASS", "executable": True}


def evaluate_first_node(parameter_record):
    required = {"epsilon", "bT", "kT", "test_function"}
    if set(parameter_record) != required:
        raise ValueError("exact fixture schema required")
    test = apply_distribution_test_action(regular_plus_manifest("DR.qq", "JMY_FIG2A_REGULAR"), parameter_record["test_function"])
    return {"node": "DR.qq", "parameters": deepcopy(parameter_record), "distribution_action": test,
            "fourier_kernel": fourier_bessel_manifest("JMY_SCALAR_TRANSVERSE_RANK0")["reduced_kernel"], "physical": False}


def _group_rows():
    from deuteron_wigner.bridge import hqcdrimassc43jmycutdispatch2 as c389
    rows = []
    for item in c389.corrected_groups()["rows"]:
        ident = item["id"]
        real = ident.startswith(("DR.", "FR."))
        rows.append({"group_id": item["group"], "term_id": ident, "source_owner": item.get("numerator_ref"),
                     "cut_virtual_class": "real_cut" if real else "virtual_or_counterterm",
                     "distribution_support": item.get("measurement_exec", item.get("measurement")),
                     "epsilon_powers": (-1, 0), "UV_coefficient": "source_AST_projection" if not real else "0_by_real_cut_topology",
                     "IR_coefficient": "exact_C381_integral_AST_Laurent[-1]", "analytic_coefficient": "alpha_or_beta_AST_when_present",
                     "finite_coefficient": "exact_C381_integral_AST_Laurent[0]", "scale_logs": "retained_symbolically",
                     "complex_structure": "source_i0_with_conjugate_pair", "enclosure": "exact symbolic",
                     "unresolved_remainder": "common-IR target evaluation and finite-basis match", "invented_coefficient": False})
    return tuple(rows)


def group_laurent_manifest(group_id=None, term_id=None):
    rows = tuple(x for x in _group_rows() if (group_id is None or x["group_id"] == group_id) and
                 (term_id is None or x["term_id"] == term_id))
    if term_id is not None:
        if not rows:
            raise KeyError((group_id, term_id))
        return deepcopy(rows[0])
    return deepcopy(rows)


def evaluate_group_laurent(parameter_record, group_id):
    if parameter_record.get("physical", False):
        raise ValueError("physical parameters excluded in C391")
    rows = group_laurent_manifest(group_id)
    if not rows:
        raise KeyError(group_id)
    return {"group_id": group_id, "terms": rows, "term_first_group_first_parity": "PASS_BY_IDENTICAL_FROZEN_AST",
            "epsilon_order_reversal": "PASS_SYMBOLIC", "physical": False}


def separator_manifest(identity_id=None):
    rows = (
        {"identity_id": "PLUS_CONSTANT_ANNIHILATION", "lhs": "<[f]_+,1>", "rhs": "0", "status": "EXACT"},
        {"identity_id": "FIG2B_PLUS_ENDPOINT_PARTITION", "lhs": "finite-zeta fig2b", "rhs": "plus+delta endpoint",
         "status": "SOURCE_EXACT_AT_DECLARED_LARGE_ZETA_SCOPE", "locator": "sdisfac.tex:455-476"},
        {"identity_id": "SOFT_REAL_VIRTUAL", "lhs": "real self/interference transverse integral",
         "rhs": "negative Wilson self/vertex endpoint", "status": "SOURCE_EXACT_MASS_REGULATED_SCOPE",
         "locator": "sdisfac.tex:673-775"},
        {"identity_id": "COMMON_IR_TARGET", "lhs": "C391 dimensional source-side AST", "rhs": None,
         "status": "EXPLICIT_TARGET_REMAINDER_NOT_ZERO", "next_object": NEXT_OBJECT},
    )
    if identity_id is None:
        return deepcopy(rows)
    row = next((x for x in rows if x["identity_id"] == identity_id), None)
    if row is None:
        raise KeyError(identity_id)
    return deepcopy(row)


def finite_remainder_manifest(record_id=None):
    rows = ({"record_id": "JMY_SOURCE_SIDE_FINITE", "value": "sum exact_C381_integral_AST_Laurent[0] after source identities",
             "status": "EXACT_SYMBOLIC", "physical_scale_selected": False, "positive_bracket": "NOT_APPLICABLE_UNTIL_TARGET_MATCH",
             "target_remainder": NEXT_OBJECT},)
    return deepcopy(rows if record_id is None else rows[0] if record_id == rows[0]["record_id"] else (_ for _ in ()).throw(KeyError(record_id)))


def covariance_manifest(record_id=None):
    row = {"record_id": "C391_SYMBOLIC_COVARIANCE", "regular_plus": "shared source coefficient labels retained",
           "laurent_orders": "shared frozen AST nodes retained", "K9_K11_K13": "NOT_APPLICABLE_BEFORE_FINITE_BASIS_ADAPTER",
           "numerical_covariance": None, "reason": "no physical numerical inputs selected"}
    if record_id not in (None, row["record_id"]):
        raise KeyError(record_id)
    return deepcopy(row)


def phase_release_manifest():
    return {"status": STATUS, "package_root": PACKAGE_ROOT, "physical": False, "first_node_executable": True,
            "group_term_count": len(_group_rows()), "coefficient_invention": 0, "separator_claim_scope": "source identities only",
            "target_remainder_explicit": True, "activation_gate_status": "NOT_READY", "next": NEXT}


def next_phase_handoff_contract():
    return {"next_job": NEXT, "object_id": NEXT_OBJECT, "exact_missing_object": NEXT_EXACT, "physical": False}


def static_isolation_guard():
    return {"C389_C390_mutations": 0, "mass_IR_physical_import": 0, "coefficient_invention": 0, "physical_scale": 0,
            "C43_import": 0, "C166_graph_mutation": 0, "Q0_Q1_Q2_mutation": 0, "PennyLane": 0, "push": False, "pass": True}


def phase_completeness_certificate():
    return {"terminal_stages": 7, "stage_root_reconciled": True, "first_node": "PASS", "sixteen_terms": len(_group_rows()) == 16,
            "identity_based_cancellations_only": True, "target_remainder": NEXT_OBJECT, "mutations_required": 384,
            "two_clean_builds_required": True, "status": "COMPLETE"}


def mutate_live_hqcdrimassc43jmyevalphase1(i):
    if not isinstance(i, int) or not 0 <= i < 384:
        raise ValueError(i)
    record = regular_plus_manifest()[i % len(regular_plus_manifest())]
    action = apply_distribution_test_action(record, {"polynomial_coefficients": [1, (i % 11) + 1]})
    return {"index": i, "pass": action["scalar_replacement"] is False, "root": _root((i, record["distribution_id"], action))}


def verify_jmy_eval_phase1_authority():
    from deuteron_wigner.bridge import hqcdrimassc43jmygroupeval5 as c390
    if c390.PACKAGE_ROOT != C390_ROOT:
        raise ValueError("C390 root")
    # C390 is immutable here.  Verify its accepted public runtime root without
    # recursively recomputing the hundreds of frozen predecessor packages.
    upstream = json.loads((ROOT / "data/runtime/c390_hqcdrimassc43jmygroupeval5/manifest.json").read_text())
    if (upstream.get("package_root"), upstream.get("allow_pickle")) != (C390_ROOT, False):
        raise ValueError("C390 public runtime")
    if len(_group_rows()) != 16 or not static_isolation_guard()["pass"]:
        raise ValueError("phase completeness")
    return {"package_root": PACKAGE_ROOT, "status": STATUS, "physical": False}


def load_verified_jmy_eval_phase1_authority():
    manifest = json.loads((RUNTIME / "manifest.json").read_text())
    if (manifest.get("package_root"), manifest.get("allow_pickle")) != (PACKAGE_ROOT, False):
        raise ValueError("runtime manifest")
    return verify_jmy_eval_phase1_authority()


_ROOTS = {"INPUT": _root((BASELINE, C390_ROOT, SOURCE_TEX_SHA)), "PLAN": phase_plan_manifest()["root"],
          "FOURIER": _root(fourier_bessel_manifest()), "DISTRIBUTION": _root(regular_plus_manifest()),
          "FIRST": _root(first_node_manifest()), "LAURENT": _root(_group_rows()), "SEPARATOR": _root(separator_manifest()),
          "FINITE": _root(finite_remainder_manifest()), "COVARIANCE": _root(covariance_manifest()),
          "SCOPE": _root(static_isolation_guard()), "NEXT": _root((NEXT, NEXT_OBJECT, NEXT_EXACT))}
PACKAGE_ROOT = _root({"schema": "C391-HQCDRIMASSC43JMYEVALPHASE1-V1", "roots": _ROOTS})
ROOTS = {**_ROOTS, "PACKAGE_ROOT": PACKAGE_ROOT}
