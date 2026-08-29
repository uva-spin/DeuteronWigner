from pathlib import Path


def test_c97_legacy_resolution_wide_route_b_is_hard_disabled():
    source = Path("scripts/build_c97_ifproofinput.py").read_text()
    start = source.index("def assemble_route_b")
    body = source[start:source.index("if __name__", start)]
    assert "legacy Route-B assembly is forbidden" in body
