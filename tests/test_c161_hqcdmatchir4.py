"""C161 target-binding and fail-closed public boundary tests."""
from deuteron_wigner.bridge import hqcdmatchir4 as c
from deuteron_wigner.bridge import hqcdfbnum as c158


def record():
    return c.common_ir_numeric_record(
        common_ir_id="C161-IR-FROZEN-K9",
        ir_family="REAL_SPACELIKE_COMMON_OFFSHELLNESS",
        resolution="K9",
        mu=1.13,
        rho=0.21,
        finite_basis_scheme="PROJECT_FINITE_BASIS_OPEN_TRIPLET_SUBTRACTION_V1",
        target_scheme_id="C43_ADAPTED_MSBAR",
        projector_id="C43_PROJECTOR_EXPLICIT",
        active_Nf=4,
        external_flavor="u",
        external_state={"units": "GeV", "state_id": "C161-COMMON-STATE-1"},
    )


def test_contract_roots_and_quarantine():
    authority = c.load_verified_hqcd_matchir4_authority()
    assert authority["status"] == c.STATUS
    assert authority["C160_package_root"] == "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817"
    assert authority["C159_package_root"] == "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67"
    assert authority["C158_package_root"] == "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"
    assert c.c134_quarantine_report()["classification"] == "PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC"


def test_target_descriptors_fail_closed_and_coordinate_adapters_are_explicit():
    binding = c.target_binding_manifest()
    assert binding["descriptor_count"] == 25
    assert all(row["binding_status"] == "SOURCE_EXPRESSION_INCOMPLETE" for row in binding["descriptors"])
    assert len(c.perturbative_coordinate_adapter_manifest()["rows"]) == 7
    assert c.matchir4_plan_manifest()["selected_plan"] == "MATCHIR4-B"


def test_public_c158_import_and_target_boundary():
    common = record()
    coupling = c158.coupling_expansion_record(fixture_id="FIXTURE-MASS-SIGN")
    imported = c.finite_basis_coefficient_import(
        "delta_signed_quark_mass^FB(order=0)", common, coupling, fixture_id="FIXTURE-MASS-SIGN"
    )
    assert imported["imported"] and not imported["recomputed"]
    assert imported["C158_package_root"] == c.C158_ROOT
    blocked = c.target_numeric_coefficient(
        "delta_signed_quark_mass^FB(order=0)", common, target_scheme_id="C43_ADAPTED_MSBAR"
    )
    assert blocked["value"] is None
    assert blocked["positive_gate"] is False


def test_explicit_remainder_control_and_isolation_mutations():
    common = record()
    control = {"computed_order": 0, "first_omitted_order": 1, "coupling_coordinate": "g_s", "coupling_envelope": {"min": 0.01, "max": 0.2}, "log_envelope": {"min": -3.0, "max": 3.0}, "no_default": True}
    remainder = c.first_omitted_order_report("delta_signed_quark_mass^FB(order=0)", common, control, target_scheme_id="C43_ADAPTED_MSBAR", fixture_id="FIXTURE-FREE")
    assert remainder["classification"] == "UNAVAILABLE_BLOCKING"
    assert c.static_isolation_guard()["pass"] is True
    for i in range(384):
        mutation = c.mutate_live_hqcdmatchir4(i)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
