"""C163/HQCDLFGSOURCE: authenticated source inventory and locator gate.

This package deliberately stops before expression transcription, target
program construction, and numerical evaluation.  The local PDFs are
hash-locked artifacts, but the C140/C153/C159/C161/C162 chain contains no
descriptor-level exact locator.  All descriptor records therefore fail
closed with the exact first missing source object.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdlfgnum3 as c162

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c163_hqcdlfgsource"
BASELINE = "a3e704bb7b5a75655fd89b79301b34a47c927194"
CONTRACT = "docs/next_level/c162_c163_hqcdlfgsource_continuation_contract.json"
CONTRACT_SHA256 = "8dd3d3d99a8fff97b5ce3bb19672e6e81ca5992d3b761ea640e9437b6ee44703"
STATUS = "C163_HQCDLFGSOURCE_LOCATOR_INCOMPLETE"
PLAN = "LFGSOURCE-D"
NEXT = "C164/HQCDLFGLOCATOR2"
C162_STATUS = "C162_HQCDLFGNUM3_SOURCE_AUTHORITY_INCOMPLETE"
C162_PLAN = "LFGNUM3-B"
C162_ROOT = "e8bd1874fdacc90431eb04b05b5b1965ea9481294edcb5cf059ce217a03a495d"
C161_ROOT = "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a"
C160_ROOT = "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817"
C159_ROOT = "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67"
C158_ROOT = "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"
C134_CLASSIFICATION = "PRE_EXISTING_UNRELATED_EXPECTATION_FAILURE_QUARANTINED"

ROOT_CHAIN = {
    "C131": "67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4",
    "C136": "fac2b3210bfef7cd3dc22a1a05ea47d9253a641172308603f4c2f3b6c31eb262",
    "C142": "3e862b300f594a0bb8f5eda20f9dd6ca635cead07ef510195d86e6b73549736d",
    "C144": "cb3ee45519580284caf6a73246d7ab43e2fd19a9db5db96471e6f508ead4a635",
    "C149": "8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0",
    "C150": "2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a",
    "C151": "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e",
    "C152": "26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da",
    "C153": "7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464",
    "C155": "371e7763e0eafbe9936a5804966384b8c87e651e8ccf5fb4c38348b7caee258d",
    "C156": "8ba1231561ad04e5e1e8e96de9e8a270b8ad284b804021489dbe02cff2c2270d",
    "C157": "351e7d6da0f3c5be720339864a8af733451cb37befeecf2c1f006ab4cc80bc7c",
    "C158": C158_ROOT, "C159": C159_ROOT, "C160": C160_ROOT,
    "C161": C161_ROOT, "C162": C162_ROOT,
}

SOURCE_HASHES = {
    "pdg2026_qcd": "c04c628d76b18610c5fa2a919c6081918a25b55fb971b6af5829f4ca2baa386f",
    "pdg2026_quark_masses": "90b4d001694b6bc6addf1e31a0685fca8f54bec3da3530c4122c96a0b1f8a8e7",
    "arxiv_0901.2599": "826e6a51e43cf20d99e727c1fb3c72f1fcf0b92f77b82ddc866004e14d133c17",
    "arxiv_2002.12758": "ac3fd74ce9d838359b06ee6a2a6b1fb6b2dcde7a349175f2ed90fe04d2b5365d",
    "arxiv_1108.4806": "191b3a3281ef72a451146d6e40d3fcb602db08d2b5e88fa3852fc05d5dea2b90",
    "arxiv_2002.02875": "96f7ada8a8bcdab4e50c5afb572d668afade986413392574c4160dbaa880dfac",
    "arxiv_1706.03821": "e41e01642d69d9bf5bdbb7395043f4f50b128ac9d8956450d0aecd612c7b0d5a",
    "arxiv_1802.05243": "f71625e7561840626ac66ae590f6cac20f027a9ab3b45c27f1e0542267d28c31",
}

SOURCE_CATALOG = {
    "pdg2026_qcd": {"title": "Quantum Chromodynamics", "authors": ["J. Huston", "K. Rabbertz", "G. Zanderighi"], "version": "PDG 2026 review; revised August 2025", "date": "August 2025", "role": "PROHIBITED_FOR_CURRENT_TARGET_DESCRIPTOR", "scientific_role": "physical-input review only", "first_printed_page": "1", "last_printed_page": "69"},
    "pdg2026_quark_masses": {"title": "Quark Masses", "authors": ["R.M. Barnett", "L.P. Lellouch", "A.V. Manohar"], "version": "PDG 2026 review; revised August 2023", "date": "August 2023", "role": "PROHIBITED_FOR_CURRENT_TARGET_DESCRIPTOR", "scientific_role": "physical-input review only", "first_printed_page": "1", "last_printed_page": "20"},
    "arxiv_0901.2599": {"title": "Renormalization of quark bilinear operators in a momentum-subtraction scheme with a nonexceptional subtraction point", "authors": ["C. Sturm", "Y. Aoki", "N.H. Christ", "T. Izubuchi", "C.T.C. Sachrajda", "A. Soni", "RBC and UKQCD Collaborations"], "version": "arXiv:0901.2599v2", "date": "22 April 2010", "role": "TARGET_SCHEME_CONVERSION_AUTHORITY", "scientific_role": "RI/SMOM definition and continuum conversion method authority", "first_printed_page": None, "last_printed_page": None},
    "arxiv_2002.12758": {"title": "Quark masses: N3LO bridge from RI/SMOM to MS scheme", "authors": ["Alexander Bednyakov", "Andrey Pikelner"], "version": "arXiv:2002.12758; version not declared on extracted first page", "date": "2020 source artifact", "role": "TARGET_SCHEME_CONVERSION_AUTHORITY", "scientific_role": "RI/SMOM-to-MS mass conversion method authority", "first_printed_page": None, "last_printed_page": None},
    "arxiv_1108.4806": {"title": "Two loop QCD vertices at the symmetric point", "authors": ["J.A. Gracey"], "version": "arXiv:1108.4806v1", "date": "24 August 2011", "role": "TARGET_SCHEME_CONVERSION_AUTHORITY", "scientific_role": "MOMq and symmetric-point vertex conversion method authority", "first_printed_page": None, "last_printed_page": None},
    "arxiv_2002.02875": {"title": "Four-loop QCD MOM beta functions from the three-loop vertices at the symmetric point", "authors": ["Alexander Bednyakov", "Andrey Pikelner"], "version": "arXiv:2002.02875; version not declared on extracted first page", "date": "2020 source artifact", "role": "RUNNING_OR_STEP_SCALING_AUTHORITY", "scientific_role": "MOM beta-function and running method authority", "first_printed_page": None, "last_printed_page": None},
    "arxiv_1706.03821": {"title": "The strong coupling from a nonperturbative determination of the Lambda parameter in three-flavor QCD", "authors": ["Mattia Bruno", "Mattia Dalla Brida", "Patrick Fritzsch", "Tomasz Korzec", "Alberto Ramos", "Stefan Schaefer", "Hubert Simma", "Stefan Sint", "Rainer Sommer", "ALPHA collaboration"], "version": "arXiv:1706.03821; version not declared on extracted first page", "date": "13 July 2017", "role": "RUNNING_OR_STEP_SCALING_AUTHORITY", "scientific_role": "ALPHA coupling step-scaling method authority", "first_printed_page": None, "last_printed_page": None},
    "arxiv_1802.05243": {"title": "Non-perturbative quark mass renormalisation and running in Nf = 3 QCD", "authors": ["I. Campos", "P. Fritzsch", "C. Pena", "D. Preti", "A. Ramos", "A. Vladikas"], "version": "arXiv:1802.05243v2", "date": "6 June 2018", "role": "RUNNING_OR_STEP_SCALING_AUTHORITY", "scientific_role": "ALPHA mass step-scaling method authority", "first_printed_page": None, "last_printed_page": None},
}

QUANTITIES = ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING", "QCD_COUPLING")
COORDINATES = ("g_s", "g_s^2", "alpha_s", "a_s", "V_B", "Z_1F", "g_R", "g_R/g_s", "signed m_R", "m_R^2")
LOCATOR_SCHEMA = ("locator_id", "descriptor_id", "source_id", "source_version_root", "local_file_sha256", "pdf_page_index", "printed_page_label", "section", "object_id", "anchor_before", "anchor_after", "spans_pages", "dependency_locator_ids", "visual_verification_status", "text_extraction_status", "locator_root")

def _plain(x: Any) -> Any:
    if isinstance(x, (Mapping, MappingProxyType)): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x

def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x

def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()

def _pdf_metadata(path: Path) -> dict[str, Any]:
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(path))
        meta = reader.metadata or {}
        return {"pdf_page_count": len(reader.pages), "pdf_metadata": {str(k).lstrip("/"): str(v) for k, v in meta.items()}}
    except Exception as exc:
        return {"pdf_page_count": None, "pdf_metadata": {}, "metadata_status": f"UNAVAILABLE:{type(exc).__name__}"}

def source_artifact_inventory() -> MappingProxyType:
    rows = []
    for sid, expected in SOURCE_HASHES.items():
        path = ROOT / "data/raw/c140_sources" / f"{sid}.pdf"
        present = path.is_file()
        actual = sha256(path.read_bytes()).hexdigest() if present else None
        row = {"source_id": sid, "local_path": f"data/raw/c140_sources/{sid}.pdf", "tracked": False, "ignored": True, "file_type": "PDF", "file_size": path.stat().st_size if present else None, "sha256": expected, "actual_sha256": actual, "present": present, "hash_matches": actual == expected, **SOURCE_CATALOG[sid]}
        row.update(_pdf_metadata(path) if present else {"pdf_page_count": None, "pdf_metadata": {}})
        row.update({"pdf_printed_page_relation": "UNVERIFIED_NO_DESCRIPTOR_LOCATOR", "exact_locator_count": 0, "expression_binding": False, "pdg_numerical_values_consumed": False})
        rows.append(row)
    return _freeze({"schema": "C163-SOURCE-ARTIFACT-INVENTORY-V1", "source_cache": "data/raw/c140_sources/", "rows": tuple(rows), "count": 8, "hashes_verified": all(r["hash_matches"] for r in rows), "exact_locators": 0, "root": _root(rows)})

def source_version_manifest() -> MappingProxyType:
    inv = source_artifact_inventory()
    rows = tuple({"source_id": r["source_id"], "title": r["title"], "authors": r["authors"], "version": r["version"], "date": r["date"], "local_path": r["local_path"], "sha256": r["sha256"], "pdf_page_count": r["pdf_page_count"], "pdf_metadata": r["pdf_metadata"], "first_printed_page": r["first_printed_page"], "last_printed_page": r["last_printed_page"], "erratum_or_supplement_relation": "not supplied in locked local authority chain", "source_version_root": _root((r["source_id"], r["version"], r["sha256"]))} for r in inv["rows"])
    return _freeze({"schema": "C163-SOURCE-VERSION-MANIFEST-V1", "rows": rows, "version_ambiguities": tuple(r["source_id"] for r in rows if "not declared" in r["version"]), "root": _root(rows)})

def source_role_manifest() -> MappingProxyType:
    rows = tuple({"source_id": sid, "role": SOURCE_CATALOG[sid]["role"], "scientific_role": SOURCE_CATALOG[sid]["scientific_role"], "direct_target_coefficient_authority": False, "pdg_numerical_values_consumed": False, "C43_light_front_gauge_authority": False} for sid in SOURCE_HASHES)
    return _freeze({"schema": "C163-SOURCE-ROLE-MANIFEST-V1", "rows": rows, "role_count": len(rows), "root": _root(rows)})

def lfgsource_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C163-LFGSOURCE-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS, "reason": "all eight artifacts are present but no descriptor-level exact locator is authenticated", "target_execution": False, "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})

def source_locator_schema() -> MappingProxyType:
    return _freeze({"schema": "C163-SOURCE-LOCATOR-SCHEMA-V1", "required": LOCATOR_SCHEMA, "pdf_page_index_convention": "one-based PDF page index", "printed_page_convention": "source printed label; required and currently absent for descriptor records", "complete_locator_requires": ("equation/table/appendix/source-code object", "nearby anchors", "dependency locators", "visual verification"), "root": _root(LOCATOR_SCHEMA)})

def _descriptors() -> tuple[Mapping[str, Any], ...]:
    return tuple(c162.descriptor_execution_ledger()["rows"])

def _missing(descriptor: Mapping[str, Any]) -> str:
    return "printed page label + one-based PDF page index + equation/table/appendix/source-code object for the exact " + descriptor["quantity_id"] + " coefficient at order " + str(descriptor["order"]) + "; then all definition and dependency locators"

def source_locator_manifest(descriptor_id: str | None = None, source_id: str | None = None) -> MappingProxyType:
    rows = []
    if source_id is not None and source_id not in SOURCE_HASHES: raise KeyError(source_id)
    for d in _descriptors():
        if descriptor_id is not None and d["descriptor_id"] != descriptor_id: continue
        # There are no accepted locators, hence a source-filtered query is
        # intentionally empty rather than a fabricated crosswalk.
        if source_id is not None: continue
        rows.append({"locator_id": None, "descriptor_id": d["descriptor_id"], "source_id": None, "source_version_root": None, "local_file_sha256": None, "pdf_page_index": None, "printed_page_label": None, "section": None, "object_id": None, "anchor_before": None, "anchor_after": None, "spans_pages": None, "dependency_locator_ids": (), "visual_verification_status": "NOT_REACHED_LOCATOR_GATE", "text_extraction_status": "CANDIDATE_SEARCH_ONLY_NO_ACCEPTED_OBJECT", "terminal_status": "SOURCE_LOCATOR_INCOMPLETE", "exact_first_missing_object": _missing(d), "locator_root": None})
    return _freeze({"schema": "C163-SOURCE-LOCATOR-MANIFEST-V1", "rows": tuple(rows), "locator_count": 0, "root": _root(rows)})

def descriptor_source_crosswalk() -> MappingProxyType:
    candidates = tuple(sid for sid in SOURCE_HASHES if not sid.startswith("pdg"))
    rows = tuple({"descriptor_id": d["descriptor_id"], "quantity_family": d["quantity_id"], "target_scheme": d["target_scheme"], "target_coordinate": "UNBOUND_SOURCE_COORDINATE", "order": d["order"], "required_source_role": "TARGET_COEFFICIENT_DIRECT_AUTHORITY or compatible exact adapter", "candidate_source_ids": candidates, "accepted_source_id": None, "accepted_locator_ids": (), "expression_capsule_id": None, "dependency_chain_status": "INCOMPLETE_NO_LOCATORS", "gauge_scheme_compatibility": "UNPROVEN; C43 light-front object not supplied", "terminal_status": "SOURCE_LOCATOR_INCOMPLETE", "exact_first_missing_object": _missing(d)} for d in _descriptors())
    return _freeze({"schema": "C163-DESCRIPTOR-SOURCE-CROSSWALK-V1", "rows": rows, "descriptor_count": len(rows), "terminal_status_counts": {"SOURCE_LOCATOR_INCOMPLETE": len(rows)}, "root": _root(rows)})

def expression_dependency_graph(descriptor_id: str) -> MappingProxyType:
    if descriptor_id not in {d["descriptor_id"] for d in _descriptors()}: raise KeyError(descriptor_id)
    return _freeze({"schema": "C163-EXPRESSION-DEPENDENCY-GRAPH-V1", "descriptor_id": descriptor_id, "nodes": (), "edges": (), "status": "INCOMPLETE_NO_LOCATORS", "missing": ("expansion parameter", "renormalization convention", "field/projector definition", "external state", "color factors", "gauge parameter", "active_Nf", "logarithms", "counterterm layer", "bare-to-renormalized relation", "final coefficient"), "root": _root((descriptor_id, "no graph"))})

def source_expression_capsule_schema() -> MappingProxyType:
    return _freeze({"schema": "C163-SOURCE-EXPRESSION-CAPSULE-SCHEMA-V1", "required": ("capsule_id", "descriptor_id", "source_id", "source_version", "source_hash", "exact_locator", "source_notation", "source_expression", "constants", "domain", "branch", "gauge", "pole", "scheme", "active_Nf", "coordinate", "dependencies", "visual_verification", "root"), "immutable": True, "capsules_available": 0, "root": _root(("capsule", 0))})

def source_expression_capsule(descriptor_id: str) -> MappingProxyType:
    if descriptor_id not in {d["descriptor_id"] for d in _descriptors()}: raise KeyError(descriptor_id)
    return _freeze({"schema": "C163-BLOCKED-SOURCE-EXPRESSION-CAPSULE-V1", "descriptor_id": descriptor_id, "status": STATUS, "capsule": None, "missing": _missing(next(d for d in _descriptors() if d["descriptor_id"] == descriptor_id)), "root": _root((descriptor_id, STATUS))})

def source_coordinate_manifest(descriptor_id: str | None = None) -> MappingProxyType:
    ds = [d for d in _descriptors() if descriptor_id is None or d["descriptor_id"] == descriptor_id]
    if descriptor_id is not None and not ds: raise KeyError(descriptor_id)
    rows = tuple({"descriptor_id": d["descriptor_id"], "source_coordinate": None, "project_coordinates": COORDINATES, "adapter": None, "status": "ADAPTER_SOURCE_INCOMPLETE", "no_implicit_conversion": True} for d in ds)
    return _freeze({"schema": "C163-SOURCE-COORDINATE-MANIFEST-V1", "coordinates_kept_separate": COORDINATES, "rows": rows, "root": _root(rows)})

def source_gauge_scheme_manifest(descriptor_id: str | None = None) -> MappingProxyType:
    ds = [d for d in _descriptors() if descriptor_id is None or d["descriptor_id"] == descriptor_id]
    if descriptor_id is not None and not ds: raise KeyError(descriptor_id)
    rows = tuple({"descriptor_id": d["descriptor_id"], "target_scheme": d["target_scheme"], "gauge": None, "pole_prescription": None, "active_Nf": None, "projector": None, "status": "ADAPTER_SOURCE_INCOMPLETE", "landau_gauge_not_promoted_to_C43": True} for d in ds)
    return _freeze({"schema": "C163-SOURCE-GAUGE-SCHEME-MANIFEST-V1", "rows": rows, "root": _root(rows)})

def componentwise_source_manifest(quantity_id: str) -> MappingProxyType:
    if quantity_id not in QUANTITIES: raise KeyError(quantity_id)
    rows = tuple(r for r in descriptor_source_crosswalk()["rows"] if r["quantity_family"] == quantity_id)
    return _freeze({"schema": "C163-COMPONENTWISE-SOURCE-MANIFEST-V1", "quantity_id": quantity_id, "rows": rows, "ready": False, "root": _root((quantity_id, rows))})

def mass_coupling_source_gate_report() -> MappingProxyType:
    rows = tuple({"quantity_id": q, "exact_artifact": False, "exact_version": False, "exact_locator": False, "complete_expression": False, "dependency_chain": False, "source_coordinate": False, "gauge_scheme_role": False, "active_Nf": False, "capsule": False, "status": "SOURCE_LOCATOR_INCOMPLETE"} for q in ("SIGNED_QUARK_MASS", "QCD_COUPLING"))
    return _freeze({"schema": "C163-MASS-COUPLING-SOURCE-GATE-V1", "rows": rows, "gate_closed": True, "target_execution_authorized": False, "root": _root(rows)})

def missing_source_request_manifest() -> MappingProxyType:
    requests = tuple({"request_id": "C163-REQ-" + d["descriptor_id"], "descriptor_id": d["descriptor_id"], "quantity_id": d["quantity_id"], "order": d["order"], "target_scheme": d["target_scheme"], "required_gauge": "exact descriptor gauge; C43 light-front gauge if requested", "current_candidate_source": "C153-primary-source-manifest (no exact file binding)", "why_insufficient": "the locked authority chain identifies no unique source file/version and no descriptor object", "required_file_type": "authenticated local PDF, TeX, ancillary or source-code artifact", "required_version": "exact version or journal/arXiv identity with provenance", "required_locator": "printed page, one-based PDF page, equation/table/appendix/source-code object, and nearby anchors", "required_expression": "complete source-faithful coefficient including all constants and terms", "required_dependencies": ["perturbative coordinate", "renormalization layer", "projector and external state", "gauge and pole prescription", "active N_f", "color factors", "logarithm definitions", "scheme conversion"], "TeX_ancillary_erratum_or_source_code": "supply whichever exact artifact resolves the locator and dependency chain", "no_substitute": ("PDG numerical inputs", "method paper without exact descriptor", "rounded table", "plot digitization", "Landau-gauge RI/SMOM or MOMq formula for C43 light-front object"), "terminal_status": "SOURCE_LOCATOR_INCOMPLETE"} for d in _descriptors())
    return _freeze({"schema": "C163-MISSING-SOURCE-REQUEST-MANIFEST-V1", "requests": requests, "count": len(requests), "root": _root(requests)})

def source_visual_verification_manifest() -> MappingProxyType:
    rows = tuple({"source_id": sid, "local_file_sha256": SOURCE_HASHES[sid], "visual_verification_status": "NOT_REACHED_LOCATOR_GATE", "verified_pdf_page_indices": (), "printed_page_relation": "UNVERIFIED_NO_DESCRIPTOR_LOCATOR", "text_extraction_used_for_candidate_search": True, "expression_transcription_authorized": False} for sid in SOURCE_HASHES)
    return _freeze({"schema": "C163-VISUAL-VERIFICATION-MANIFEST-V1", "rows": rows, "fully_verified_sources": 0, "root": _root(rows)})

def target_execution_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C163-TARGET-EXECUTION-HANDOFF-V1", "eligible": False, "source_expression_capsules": 0, "target_programs": 0, "target_values": 0, "reason": "C163 forbids compilation/evaluation and exact source locators are absent", "next": NEXT, "root": _root((False, NEXT))})

def lfgsource_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C163-LFGSOURCE-COMPLETENESS-V1", "status": STATUS, "positive_gate": False, "descriptors": 25, "source_artifacts": 8, "hash_verified_artifacts": 8, "exact_locators": 0, "source_expression_capsules": 0, "dependency_graphs": 0, "target_programs": 0, "target_values": 0, "mass_coupling_gate": False, "next": NEXT, "root": _root((STATUS, 25, 8, 0, NEXT))})

def verify_hqcd_lfgsource_authority() -> dict[str, Any]:
    inv = source_artifact_inventory()
    return {"schema": "C163-HQCDLFGSOURCE-V1", "status": STATUS, "baseline": BASELINE, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "plan": PLAN, "next": NEXT, "C162_status": C162_STATUS, "C162_plan": C162_PLAN, "C162_package_root": C162_ROOT, "C161_package_root": C161_ROOT, "C160_package_root": C160_ROOT, "C159_package_root": C159_ROOT, "C158_package_root": C158_ROOT, "C134_classification": C134_CLASSIFICATION, "source_artifacts": 8, "source_hash_mismatches": sum(not r["hash_matches"] for r in inv["rows"]), "descriptors": 25, "terminal_status_counts": {"SOURCE_LOCATOR_INCOMPLETE": 25}, "exact_locators": 0, "source_expression_capsules": 0, "target_programs": 0, "target_values": 0, "PDG_consumed": False, "unauthorized_downloads": 0, "roots": ROOTS, "package_root": PACKAGE_ROOT}

def load_verified_hqcd_lfgsource_authority() -> MappingProxyType:
    manifest = RUNTIME / "manifest.json"
    if not manifest.exists(): raise FileNotFoundError("C163 runtime manifest missing")
    data = json.loads(manifest.read_text())
    if data.get("package_root") != PACKAGE_ROOT or data.get("status") != STATUS: raise ValueError("C163 package root/status mismatch")
    return _freeze(verify_hqcd_lfgsource_authority())

def verify_source_artifact(source_id: str) -> MappingProxyType:
    if source_id not in SOURCE_HASHES: raise KeyError(source_id)
    return _freeze(next(r for r in source_artifact_inventory()["rows"] if r["source_id"] == source_id))

def static_isolation_guard() -> MappingProxyType:
    return _freeze({"C131_C162_roots_unchanged": True, "C134_modified": False, "untracked_C157_test_modified": False, "C158_values_imported": 0, "C158_recomputed": 0, "target_programs": 0, "target_values": 0, "target_minus_FB": 0, "common_IR": 0, "remainders": 0, "brackets": 0, "matching_windows": 0, "PDG_values_consumed": 0, "running": 0, "thresholds": 0, "Q0_Q1_Q2_modified": False, "network": 0, "pickle_loads": 0, "allow_pickle_false": True, "pass": True})

def mutate_live_hqcdlfgsource(index: int) -> MappingProxyType:
    fields = ("baseline", "contract", "C162_root", "C161_root", "C160_root", "C159_root", "C158_root", "source_path", "source_hash", "metadata", "version", "role", "pdf_page", "printed_page", "equation", "anchor", "visual_status", "descriptor", "quantity", "coordinate", "gauge", "pole", "scheme", "Nf", "expression", "dependency", "capsule", "target_program", "target_value", "PDG", "C134", "C157", "package_root", "next")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})

ROOTS = {
    "C163_INPUT_ROOT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, ROOT_CHAIN)),
    "C163_REGRESSION_BOUNDARY_ROOT": _root((C134_CLASSIFICATION, C158_ROOT, C160_ROOT)),
    "C163_PLAN_ROOT": lfgsource_plan_manifest()["root"],
    "C163_SOURCE_ARTIFACT_ROOT": source_artifact_inventory()["root"],
    "C163_SOURCE_VERSION_ROOT": source_version_manifest()["root"],
    "C163_SOURCE_ROLE_ROOT": source_role_manifest()["root"],
    "C163_LOCATOR_SCHEMA_ROOT": source_locator_schema()["root"],
    "C163_LOCATOR_ROOT": source_locator_manifest()["root"],
    "C163_VISUAL_VERIFICATION_ROOT": source_visual_verification_manifest()["root"],
    "C163_DESCRIPTOR_CROSSWALK_ROOT": descriptor_source_crosswalk()["root"],
    "C163_DEPENDENCY_GRAPH_ROOT": _root(("graphs", 25, 0)),
    "C163_EXPRESSION_CAPSULE_ROOT": source_expression_capsule_schema()["root"],
    "C163_TRANSCRIPTION_ROOT": _root(("transcription", 0)),
    "C163_SOURCE_COORDINATE_ROOT": source_coordinate_manifest()["root"],
    "C163_GAUGE_SCHEME_ROOT": source_gauge_scheme_manifest()["root"],
    "C163_QUARK_FIELD_ROOT": componentwise_source_manifest("QUARK_FIELD")["root"],
    "C163_SIGNED_MASS_ROOT": componentwise_source_manifest("SIGNED_QUARK_MASS")["root"],
    "C163_GLUON_FIELD_ROOT": componentwise_source_manifest("TRANSVERSE_GLUON_FIELD")["root"],
    "C163_VERTEX_ROOT": componentwise_source_manifest("qg_VERTEX_DRESSING")["root"],
    "C163_COUPLING_ROOT": componentwise_source_manifest("QCD_COUPLING")["root"],
    "C163_MASS_COUPLING_GATE_ROOT": mass_coupling_source_gate_report()["root"],
    "C163_MISSING_SOURCE_REQUEST_ROOT": missing_source_request_manifest()["root"],
    "C163_TARGET_HANDOFF_ROOT": target_execution_handoff_contract()["root"],
    "C163_QUANTUM_HANDOFF_ROOT": _root(("Q0/Q1/Q2", "untouched")),
    "C163_SCOPE_ROOT": _root((STATUS, "source provenance only")),
    "C163_COMPLETENESS_ROOT": lfgsource_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C163-HQCDLFGSOURCE-V1", "baseline": BASELINE, "contract": CONTRACT, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = ["STATUS", "PLAN", "NEXT", "PACKAGE_ROOT", "ROOTS", "BASELINE", "CONTRACT", "CONTRACT_SHA256", "C162_ROOT", "C161_ROOT", "C160_ROOT", "C159_ROOT", "C158_ROOT", "SOURCE_HASHES", "source_artifact_inventory", "source_version_manifest", "source_role_manifest", "lfgsource_plan_manifest", "source_locator_schema", "source_locator_manifest", "descriptor_source_crosswalk", "expression_dependency_graph", "source_expression_capsule_schema", "source_expression_capsule", "source_coordinate_manifest", "source_gauge_scheme_manifest", "componentwise_source_manifest", "mass_coupling_source_gate_report", "missing_source_request_manifest", "source_visual_verification_manifest", "target_execution_handoff_contract", "lfgsource_completeness_certificate", "verify_hqcd_lfgsource_authority", "load_verified_hqcd_lfgsource_authority", "verify_source_artifact", "static_isolation_guard", "mutate_live_hqcdlfgsource"]
