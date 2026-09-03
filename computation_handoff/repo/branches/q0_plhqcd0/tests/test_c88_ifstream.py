from deuteron_wigner.bridge.ifstream.core import STATUS, bounded_export_preflight, canonical_scientific_schema, historical_c82_census


def test_c88_census_and_storage_preflight_fail_before_any_export(tmp_path):
    census = historical_c82_census()
    assert census["supported_pairs"] == 154830
    assert census["logical_pair_coordinate_records"] == 891992018
    output = tmp_path / "output"
    report = bounded_export_preflight(output)
    assert report["status"] == STATUS
    assert not report["bounded_export_possible"]
    assert not output.exists()


def test_c88_schema_prohibits_kernel_and_product_fields():
    schema = canonical_scientific_schema()
    assert schema["schema_sha256"]
    assert "C80 kernel value" in schema["prohibitions"]
