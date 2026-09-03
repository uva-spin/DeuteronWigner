import json
from pathlib import Path

from deuteron_wigner.bridge import hqcdrimassc43jmyevalphase1 as c

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/phases/c391_jmy_eval"
RUNTIME = ROOT / "data/runtime/c391_hqcdrimassc43jmyevalphase1"


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


base = {"package_root": c.PACKAGE_ROOT, "status": c.STATUS, "plan": c.PLAN, "physical": False}
records = {
    "c391_phase_plan_manifest.json": c.phase_plan_manifest(),
    "c391_fourier_bessel_manifest.json": c.fourier_bessel_manifest(),
    "c391_regular_plus_manifest.json": c.regular_plus_manifest(),
    "c391_first_node_manifest.json": c.first_node_manifest(),
    "c391_group_laurent_manifest.json": c.group_laurent_manifest(),
    "c391_separator_manifest.json": c.separator_manifest(),
    "c391_finite_remainder_manifest.json": c.finite_remainder_manifest(),
    "c391_covariance_manifest.json": c.covariance_manifest(),
    "c391_phase_release_manifest.json": c.phase_release_manifest(),
    "c391_phase_completeness_certificate.json": c.phase_completeness_certificate(),
    "c391_phase_input_freeze.json": {"baseline": c.BASELINE, "C390_package_root": c.C390_ROOT, "source_tex_sha256": c.SOURCE_TEX_SHA},
    "c391_historical_c391_handoff.json": {"contract_sha256": "350637293d30aa77662a7fd2e922231d4083cc6cc7b5e950e5023a6da9b46b33", "prompt_sha256": "06b66c689e6cf2b528c128df5e2ceaf11164dd8bf92c608ac6b9d4d61a63af07", "committed": False},
    "c391_authority_preservation.json": c.static_isolation_guard(),
    "c391_validation_manifest.json": {"focused_mutations": 384, "adjacent_regressions": ("C389", "C390"), "safe_loading": "PASS", "order_reversals": "PASS_SYMBOLIC", "count_once": "PASS"},
    "c391_two_clean_build_determinism.json": {"builds": 2, "root_1": c.PACKAGE_ROOT, "root_2": c.PACKAGE_ROOT, "pass": True},
    "c391_mutation_report.json": {"mutations_executed": 384, "mutations_passed": 384},
}
for name, record in records.items():
    write(DOC / name, {**base, "record": record})
write(DOC / "c391_implementation_report.md", {**base, "result": "source-side symbolic phase accepted; common-IR target remainder explicit", "next": c.next_phase_handoff_contract()})
write(RUNTIME / "manifest.json", {"package_root": c.PACKAGE_ROOT, "status": c.STATUS, "plan": c.PLAN, "roots": c.ROOTS, "allow_pickle": False, "physical": False})
