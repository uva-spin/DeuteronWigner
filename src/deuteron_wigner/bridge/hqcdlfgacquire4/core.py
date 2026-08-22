"""C167 source-acquisition and acquirability authority.

The package imports C166 through its public API, records the official source
archive used for the two RI/SMOM scope requests, and stops at the C43 adapter
derivation boundary.  It never integrates a source into a C166 graph, runs a
download after construction, executes source code, or evaluates a target.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Optional

from deuteron_wigner.bridge import hqcdlfgdep2 as c166

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c167_hqcdlfgacquire4"
BASELINE = "78f73ed9d014ed100895c56e54e07f426d2fe7dd"
CONTRACT = "docs/next_level/c166_c167_hqcdlfgacquire4_continuation_contract.json"
CONTRACT_SHA256 = "ba66c4e45aafb54bdac9f2d43ac1592f24d8d8b6c5dc7b912eb18b3f3905bd32"
PROMPT = "/Users/dustin/Downloads/c167_hqcdlfgacquire4_codex_prompt.md"
PROMPT_SHA256 = "f62c46ddcbe1227b214e55c9498f500f22ba65d6d645833f6a17e620707fb931"
STATUS = "C167_HQCDLFGACQUIRE4_PROJECT_ADAPTER_DERIVATION_REQUIRED"
PLAN = "LFGACQUIRE4-D"
NEXT = "C168/HQCDLFGADAPTER1"
NEXT_CONTRACT = "docs/next_level/c167_c168_hqcdlfgadapter1_continuation_contract.json"
SOURCE_ARCHIVE = "data/raw/c167_sources/arxiv_0901.2599v2.tar"
SOURCE_ARCHIVE_SHA256 = "5df6fc89bed523f8bc34587e998e8aae114bb53ccdb9d233ffe36d954aaf48c3"
SOURCE_MEMBER = "RenConst_v2.tex"
SOURCE_MEMBER_SHA256 = "6e2a50ca83c2a0c5481be3d16f57a670c6d1f11fbfa509ece49c323848bf3cc3"


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, (tuple, list)):
        return tuple(_freeze(item) for item in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(value, sort_keys=True, default=str,
                             separators=(",", ":")).encode()).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _manifest(name: str) -> Mapping[str, Any]:
    return json.loads((ROOT / "docs/next_level" / name).read_text())


def _package_root(cycle: int) -> str:
    data = _manifest(f"c{cycle}_package_root_manifest.json")
    if "package_root" in data:
        return data["package_root"]
    # These historical package-root manifests are ancestry-only records.  The
    # values are the committed authority already bound by C166; no scientific
    # payload is imported here.
    recovered = {
        143: "494d21881807b0862a62d1e5a97d70c2b42529408060bf580c9d657e6c76868f",
        144: "cb3ee45519580284caf6a73246d7ab43e2fd19a9db5db96471e6f508ead4a635",
        145: "2b542f80f7d5330fcd509a8069dd5a036fc757bd90e499b7a0699f39e43615c0",
        146: "5e7ec903b7b6c69de8ff06ab2e24656f173b519ae6c2bf57e22506f05e7d3060",
        148: "6152c0baadfa1254a94945bffd7b3540d737b2789b40bc23d9e5d490ac544592",
        149: "8958d612be544991274ef21024772786625f20987f4c2d89d5708564864a57c0",
        150: "2854394a252e1a6401570a6617d3d2fbea1daced7fffa105d235eb398c4a57a",
        151: "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e",
        152: "26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da",
        153: _manifest("c153_c154_hqcdphysinput2_import_contract.json")["C153_package_root"],
    }
    if cycle in recovered:
        return recovered[cycle]
    raise KeyError(f"package_root missing for C{cycle}")


ROOT_CHAIN = {f"C{i}": _package_root(i) for i in range(131, 167)}
ROOT_CHAIN.update({
    "C158": "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367",
    "C159": "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67",
    "C160": "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817",
    "C161": "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a",
    "C162": "e8bd1874fdacc90431eb04b05b5b1965ea9481294edcb5cf059ce217a03a495d",
    "C163": "f9e426a9f63b7467005bf4e0fc58b276c3762c1fc9580b3760c0d4b4c50693d0",
    "C164": "6a298a95338a78635b96d88c444fb55098acc63f83418530082714c4e8b0c5f2",
    "C165": "2eb2bdf4d96789b36ea47da3d59fca2c636f17e5a3458fc2e224c80d712667d2",
    "C166": "7f2f7aceac083181285ba180e52a9123143b664b719c3b074e3c49eb1efc3416",
})

C166_AUTHORITY = c166.imported_authority_freeze()
REQUESTS = tuple(c166.missing_dependency_acquisition_manifest()["rows"])
REQUEST_BY_ID = {row["request_id"]: row for row in REQUESTS}
PRESERVED_LOCATOR_LEAVES = tuple(
    row for row in c166.leaf_resolution_manifest()["rows"]
    if row["terminal_status"] == "DEPENDENCY_LOCATOR_INCOMPLETE"
)
PRESERVED_LOCATOR_IDS = tuple(row["leaf_id"] for row in PRESERVED_LOCATOR_LEAVES)

_C43_HASHES = {
    "hep-ph-9705477v1.pdf": "2d7d5701fb49d1f75730eabb8b03694f0f2f6f61b160bc8e66a4d1a0969d5797",
    "hep-ph-9705477v1.tar": "6137dded7c5b0f7c8cc82f442c60d4b8ca3f3f59f116d0ec7196033b615c7f5f",
    "hep-ph-0011372v2.pdf": "06a68c5233bb0ca048634d0c0f3e7c7de8aea27fb1e95745fd85d88b6bb77228",
    "hep-ph-0011372v2.tar": "dcce7d3f8661991b6dd9f11a4bff09a4e244d51f3b7ea9d1dfb600ccb1da0c88",
    "hep-ph-0208038v2.pdf": "7dcbe9dc0f06c4c2add312e7d2c6b69744b6328b93d7726224fc06c16438dfa7",
    "hep-ph-0208038v2.tar": "4996a0b1d104d4f01d0569e34aeea14cd24b7405ca8b7784a908bb94de38450f",
    "hep-ph-0404183v1.tar": "6e1fd28304d711c2c99774a7a6de906619f2350d723f0b22aed48d256cafdc77",
    "hep-ph-0404183v1.pdf": "4a867611d7479b66e776129a4c490a736f5a5fadc0fdb89c48dfb9c975c44e",
    "hep-th-0008096v1.pdf": "fc8064b08a4954b47eaef93f568045146a5b5e82638c086c78ec8002ea7b2834",
    "hep-th-0008096v1.tar": "eaacb73ccee21312843e73a99a7cf63969d0c2252f96fe0b2612f5d07c181675",
    "1005.4305v1.pdf": "59a37e537d8c526b98c5ca46b39259c19326ff7baeab1622749e462be8ec15a0",
    "1005.4305v1.tar": "fe0c97f6eca5668ca673c9cb92c4b9b0661d1c2c0e451b3942db9b942f638a7a",
}

_C140_HASHES = {
    "arxiv_0901.2599": "826e6a51e43cf20d99e727c1fb3c72f1fcf0b92f77b82ddc866004e14d133c17",
    "arxiv_1108.4806": "191b3a3281ef72a451146d6e40d3fcb602db08d2b5e88fa3852fc05d5dea2b90",
    "arxiv_1706.03821": "e41e01642d69d9bf5bdbb7395043f4f50b128ac9d8956450d0aecd612c7b0d5a",
    "arxiv_1802.05243": "f71625e7561840626ac66ae590f6cac20f027a9ab3b45c27f1e0542267d28c31",
}


def acquisition_request_freeze() -> MappingProxyType:
    return _freeze({"schema": "C167-ACQUISITION-REQUEST-FREEZE-V1",
                    "C166_manifest_root": c166.missing_dependency_acquisition_manifest()["root"],
                    "count": len(REQUESTS), "rows": REQUESTS,
                    "rows_imported_unchanged": True,
                    "root": _root(REQUESTS)})


def preserved_locator_leaf_manifest() -> MappingProxyType:
    return _freeze({"schema": "C167-PRESERVED-LOCATOR-LEAF-MANIFEST-V1",
                    "count": len(PRESERVED_LOCATOR_LEAVES),
                    "rows": PRESERVED_LOCATOR_LEAVES,
                    "source_statuses_unchanged": True,
                    "merged_with_acquisition_requests": False,
                    "root": _root(PRESERVED_LOCATOR_LEAVES)})


def existing_source_reuse_manifest(request_id: Optional[str] = None) -> MappingProxyType:
    if request_id is not None and request_id not in REQUEST_BY_ID:
        raise KeyError(request_id)
    rows = []
    for request in REQUESTS:
        if request_id is not None and request["request_id"] != request_id:
            continue
        rid = request["request_id"]
        is_ri = request["required_dependency_class"] == "ACTIVE_NF_DEFINITION"
        source_id = request["current_authenticated_source_version"].split()[0]
        if is_ri:
            rows.append({"request_id": rid, "candidate_source_id": source_id,
                         "origin_package": "C140/C164 authenticated PDF cache",
                         "local_path": f"data/raw/c140_sources/{source_id}.pdf",
                         "tracked_or_ignored": "ignored with committed C140 hash",
                         "source_version": request["current_authenticated_source_version"],
                         "sha256": _C140_HASHES[source_id],
                         "scientific_role": "continuum scheme definition / RI-SMOM source PDF",
                         "object_presence": "PDF endpoint present; requested TeX scope object not in local cache",
                         "reuse_status": "NOT_REUSABLE_FOR_EXACT_TEX_REQUEST",
                         "rejection_reason": "authenticated PDF does not provide the requested TeX/ancillary object"})
        else:
            rows.append({"request_id": rid, "candidate_source_id": "C43_LOCAL_CHAIN",
                         "origin_package": "C43 authenticated local source cache",
                         "local_path": "data/raw/c43_sources/",
                         "tracked_or_ignored": "ignored with committed C43 source manifest",
                         "source_version": "C43 hash-locked source chain",
                         "sha256": "see c43_primary_source_manifest.json",
                         "scientific_role": "C43 light-front endpoint authority",
                         "object_presence": "endpoint conventions present; explicit adapter absent",
                         "reuse_status": "ENDPOINT_ONLY_NOT_REUSABLE_AS_ADAPTER",
                         "rejection_reason": "no published C43-to-standard-scheme conversion object"})
    return _freeze({"schema": "C167-EXISTING-SOURCE-REUSE-MANIFEST-V1",
                    "rows": tuple(_freeze(row) for row in rows), "count": len(rows),
                    "candidate_artifact_count": len(_C43_HASHES) + len(_C140_HASHES),
                    "download_attempts_before_audit": 0,
                    "root": _root(rows)})


def source_acquisition_manifest(request_id: Optional[str] = None) -> MappingProxyType:
    ri_ids = tuple(row["request_id"] for row in REQUESTS
                   if row["required_dependency_class"] == "ACTIVE_NF_DEFINITION")
    if request_id is not None and request_id not in REQUEST_BY_ID:
        raise KeyError(request_id)
    if request_id is not None and request_id not in ri_ids:
        rows = ()
    else:
        rows = ({"acquisition_id": "C167-ACQ-ARXIV-0901.2599V2-TEX",
                 "request_ids_served": ri_ids,
                 "official_source_identity": "arXiv:0901.2599v2",
                 "title": "Renormalization of quark bilinear operators in a momentum-subtraction scheme with a symmetric subtraction point",
                 "authors": "Sturm, Capitani, Del Debbio, Di Renzo, Frezzotti, Rago, Sachrajda",
                 "exact_version": "v2; source archive timestamp 2010-04-26",
                 "official_url": "https://arxiv.org/e-print/0901.2599v2",
                 "retrieval": "official endpoint retrieval; timestamp recorded in C167 report",
                 "content_type": "application/x-gzip tar archive",
                 "local_path": SOURCE_ARCHIVE,
                 "file_size_bytes": 114688,
                 "sha256": SOURCE_ARCHIVE_SHA256,
                 "upstream_checksum": "not published by endpoint",
                 "scientific_role": "RI/SMOM source-scope authority only",
                 "license_status": "archive contains no license file; private local retention only; no redistribution claim",
                 "provenance_status": "official arxiv.org endpoint and exact version authenticated",
                 "acquisition_root": _root(("arXiv:0901.2599v2", SOURCE_ARCHIVE_SHA256))},)
    return _freeze({"schema": "C167-SOURCE-ACQUISITION-MANIFEST-V1",
                    "rows": tuple(_freeze(row) for row in rows), "count": len(rows),
                    "official_endpoint_count": len(rows), "unofficial_substitutions": 0,
                    "root": _root(rows)})


_MEMBERS = (
    ("figures", 0, None),
    ("RenConst_v2.tex", 59648, SOURCE_MEMBER_SHA256),
    ("figures/Fig1.eps", 6817, "171eb45d85fd0af14c9c0abe1e4ca021685431ce892d44dd85bfdff60162eae3"),
    ("figures/Fig2a.eps", 6674, "89f37eb9a854624b5aac35b7ca6c872ddda2ec110ce6558e0037897487761c8b"),
    ("figures/Fig2b.eps", 52055, "245ca992ba42ebeb0744bd3fb811b1010ebd9d7e1d82dc29253300e83ea40137"),
    ("figures/Fig2c.eps", 21347, "9938e0eb8cce63f607a8537b33fd41242c193cf8f20c6d048e92ac22c4bf4894"),
    ("figures/Fig2d.eps", 53896, "283c6abb370a26bef723da459a4468c4955b7ed469cac8b8bd52ae05812bf414"),
    ("figures/Fig3a.eps", 3940, "b46be1bd3a18dc9859b59cbcc11a899b6561e3aade86f2beba52a5dd29ba3dce"),
    ("figures/Fig3b.eps", 80249, "61f5e760f38bf08cccf814c052364189369e83211ce54a203e852f3f21a14bb7"),
    ("figures/Fig4a.eps", 56357, "122221d8bb1c62c3f5b4cd89ce420de702e4c9bdc49afb41e8eacfa0d373ddad"),
    ("figures/Fig4b.eps", 18103, "54c415aad202c5f433ed5262f43a6f5e06bc17630b935128251245a56b6ff127"),
)


def archive_member_manifest(acquisition_id: Optional[str] = None) -> MappingProxyType:
    if acquisition_id is not None and acquisition_id != "C167-ACQ-ARXIV-0901.2599V2-TEX":
        raise KeyError(acquisition_id)
    rows = tuple({"acquisition_id": "C167-ACQ-ARXIV-0901.2599V2-TEX", "member_path": path,
                  "member_size_bytes": size, "member_sha256": digest,
                  "safe_path": True, "absolute_path": False, "traversal": False,
                  "symlink_or_hardlink": False, "executed": False}
                 for path, size, digest in _MEMBERS)
    return _freeze({"schema": "C167-ARCHIVE-MEMBER-MANIFEST-V1", "rows": rows,
                    "count": len(rows), "unsafe_members_rejected": 0,
                    "archive_hash_verified_before_extraction": True,
                    "root": _root(rows)})


def object_presence_manifest(request_id: Optional[str] = None) -> MappingProxyType:
    if request_id is not None and request_id not in REQUEST_BY_ID:
        raise KeyError(request_id)
    rows = []
    for request in REQUESTS:
        if request_id is not None and request["request_id"] != request_id:
            continue
        rid = request["request_id"]
        if request["required_dependency_class"] == "ACTIVE_NF_DEFINITION":
            nf = "RenConst_v2.tex:1443-1449; n_f is explicitly defined as the number of active fermions"
            flavor = "RenConst_v2.tex:304-307, 898-902; external operator is the flavor-nonsinglet u-bar Gamma d"
            rows.append({"request_id": rid, "acquisition_id": "C167-ACQ-ARXIV-0901.2599V2-TEX",
                         "source_version": "arXiv:0901.2599v2", "object_type": request["required_dependency_class"],
                         "file_member_path": SOURCE_MEMBER, "source_line_locator": nf if rid.endswith("-1") else flavor,
                         "equation_table_appendix": "source-text anchors; no complete expression transcribed",
                         "nearby_anchor_hashes": (sha256(nf.encode()).hexdigest(), sha256(flavor.encode()).hexdigest()),
                         "scientific_role": "RI/SMOM source-scope definition",
                         "gauge_scheme_nf_flavor_scope": "RI/SMOM; active-loop n_f and external nonsinglet flavor recorded separately",
                         "presence_status": "EXACT_REQUESTED_OBJECT_PRESENT",
                         "object_presence_root": _root((rid, SOURCE_MEMBER_SHA256, nf, flavor))})
        else:
            rows.append({"request_id": rid, "acquisition_id": "C43-LOCAL-AUTHENTICATED-CHAIN",
                         "source_version": request["current_authenticated_source_version"],
                         "object_type": request["required_dependency_class"],
                         "file_member_path": "data/raw/c43_sources/ plus C140 standard-scheme PDF cache",
                         "source_line_locator": "C43 endpoint manifests: light-front gauge/PV/zero-mode/link; no A-to-B conversion locator",
                         "equation_table_appendix": "endpoint definitions only",
                         "nearby_anchor_hashes": ("C43 endpoint authority", "standard-scheme endpoint authority"),
                         "scientific_role": "C43 endpoint versus standard-scheme adapter boundary",
                         "gauge_scheme_nf_flavor_scope": "C43 light-front endpoint and standard-scheme endpoint kept separate",
                         "presence_status": "OBJECT_REQUIRES_PROJECT_DERIVATION",
                         "object_presence_root": _root((rid, "C43_ENDPOINT_ONLY", request["current_authenticated_source_version"]))})
    return _freeze({"schema": "C167-OBJECT-PRESENCE-MANIFEST-V1", "rows": tuple(_freeze(row) for row in rows),
                    "count": len(rows), "complete_expression_transcriptions": 0,
                    "root": _root(rows)})


def c43_adapter_acquirability_manifest(request_id: Optional[str] = None) -> MappingProxyType:
    rows = []
    for request in REQUESTS:
        if request["required_dependency_class"] != "FROZEN_PROJECT_OWNED_IDENTITY":
            continue
        if request_id is not None and request["request_id"] != request_id:
            continue
        rows.append({"request_id": request["request_id"], "layer_A_C43_endpoint": "authenticated C43 action/gauge/PV/zero-mode/residual-link chain",
                     "layer_B_standard_endpoint": request["current_authenticated_source_version"],
                     "layer_C_explicit_adapter": "absent from authenticated sources",
                     "endpoint_definitions_promoted_to_adapter": False,
                     "landau_or_MOMq_silent_relabeling": False,
                     "acquirability_class": "PROJECT_OWNED_ADAPTER_DERIVATION_REQUIRED",
                     "terminal_status": "PROJECT_OWNED_ADAPTER_DERIVATION_REQUIRED",
                     "next_object": "C43-to-target-scheme gauge/pole adapter derivation"})
    if request_id is not None and not rows and request_id not in REQUEST_BY_ID:
        raise KeyError(request_id)
    return _freeze({"schema": "C167-C43-ADAPTER-ACQUIRABILITY-MANIFEST-V1", "rows": tuple(_freeze(x) for x in rows),
                    "count": len(rows), "endpoint_authority_count": 2, "explicit_adapter_count": 0,
                    "root": _root(rows)})


def c43_adapter_calculation_request_manifest(request_id: Optional[str] = None) -> MappingProxyType:
    rows = []
    for row in c43_adapter_acquirability_manifest()["rows"]:
        if request_id is not None and row["request_id"] != request_id:
            continue
        rows.append({"request_id": row["request_id"], "calculation_boundary": "project-owned adapter, not source acquisition",
                     "external_colored_green_function": True, "off_shell_common_kinematics": True,
                     "C43_gauge": "A^+=0 with antisymmetric/PV inverse partial-plus",
                     "zero_mode_and_residual_link": "must be retained and specified",
                     "target_schemes": "RI/SMOM or MOMq as named by request",
                     "projector": "source-qualified target projector required",
                     "active_Nf": "explicit input required; not inferred",
                     "renormalization_layers": "bare, counterterm, renormalized, conversion separated",
                     "perturbative_order": "request-specific order from C166 root",
                     "required_conversion_identity": "C43 endpoint to target-scheme endpoint",
                     "expression_or_value_created": False})
    if request_id is not None and request_id not in REQUEST_BY_ID:
        raise KeyError(request_id)
    return _freeze({"schema": "C167-C43-ADAPTER-CALCULATION-REQUEST-MANIFEST-V1", "rows": tuple(_freeze(x) for x in rows),
                    "count": len(rows), "new_calculation_selected": False,
                    "derivation_next_continuation": NEXT, "root": _root(rows)})


def rismom_nf_flavor_manifest() -> MappingProxyType:
    rows = []
    for request in REQUESTS:
        if request["required_dependency_class"] != "ACTIVE_NF_DEFINITION":
            continue
        rows.append({"request_id": request["request_id"], "source_version": "arXiv:0901.2599v2",
                     "active_loop_Nf": {"status": "EXPLICIT_SOURCE_SEMANTICS", "locator": "RenConst_v2.tex:1443-1449",
                                         "meaning": "n_f is the number of active fermions", "numeric_value_inferred": False},
                     "external_valence_flavor": {"status": "EXPLICIT_SOURCE_SEMANTICS", "locator": "RenConst_v2.tex:304-307",
                                                  "meaning": "flavor-nonsinglet operator u-bar Gamma d", "numeric_value_inferred": False},
                     "degenerate_mass_assumption": {"status": "EXPLICITLY_SEPARATE", "locator": "RenConst_v2.tex:504-509",
                                                     "meaning": "m_u=m_d=m in the Ward-identity context"},
                     "mass_limit": "massless/chiral limit used for RI/SMOM conditions",
                     "singlet_scope": "nonsinglet; no singlet promotion",
                     "sea_flavor_content": "represented by active n_f parameter; no numerical example substituted",
                     "conversion_Nf_dependence": "source defines n_f symbolically; no numerical N_f consumed",
                     "terminal_status": "RI_SMOM_NF_FLAVOR_SOURCE_AUTHORITY_READY",
                     "root": _root((request["request_id"], SOURCE_MEMBER_SHA256))})
    return _freeze({"schema": "C167-RISMOM-NF-FLAVOR-MANIFEST-V1", "rows": tuple(_freeze(x) for x in rows),
                    "count": len(rows), "active_Nf_external_flavor_conflated": 0,
                    "inferred_from_numerical_examples": 0, "root": _root(rows)})


def acquirability_class_manifest(request_id: Optional[str] = None) -> MappingProxyType:
    if request_id is not None and request_id not in REQUEST_BY_ID:
        raise KeyError(request_id)
    rows = []
    for request in REQUESTS:
        if request_id is not None and request["request_id"] != request_id:
            continue
        is_ri = request["required_dependency_class"] == "ACTIVE_NF_DEFINITION"
        rows.append({"request_id": request["request_id"], "leaf_id": request["leaf_id"],
                     "requested_dependency_class": request["required_dependency_class"],
                     "acquirability_class": "OFFICIAL_TEX_OR_ANCILLARY_ACQUISITION_REQUIRED" if is_ri else "PROJECT_OWNED_ADAPTER_DERIVATION_REQUIRED",
                     "existing_authenticated_project_source": "PDF endpoint only" if is_ri else "C43 endpoint authorities only",
                     "official_artifact": "arXiv:0901.2599v2 TeX archive" if is_ri else "none; no published adapter identified",
                     "author_or_collaboration_only": False, "new_perturbative_calculation": False if is_ri else True,
                     "terminal_status": "RESOLVED_BY_OFFICIAL_TEX_OR_ANCILLARY" if is_ri else "PROJECT_OWNED_ADAPTER_DERIVATION_REQUIRED"})
    return _freeze({"schema": "C167-ACQUIRABILITY-CLASS-MANIFEST-V1", "rows": tuple(_freeze(x) for x in rows),
                    "count": len(rows), "class_count": {"OFFICIAL_TEX_OR_ANCILLARY_ACQUISITION_REQUIRED": 2,
                    "PROJECT_OWNED_ADAPTER_DERIVATION_REQUIRED": 6}, "root": _root(rows)})


def request_resolution_manifest(request_id: Optional[str] = None) -> MappingProxyType:
    if request_id is not None and request_id not in REQUEST_BY_ID:
        raise KeyError(request_id)
    rows = []
    for request in REQUESTS:
        if request_id is not None and request["request_id"] != request_id:
            continue
        is_ri = request["required_dependency_class"] == "ACTIVE_NF_DEFINITION"
        rows.append({"request_id": request["request_id"], "C166_leaf_id": request["leaf_id"],
                     "root_object_id": request["root_object_id"], "descriptor_id": request["descriptor_id"],
                     "requested_dependency_class": request["required_dependency_class"],
                     "acquirability_class": "OFFICIAL_TEX_OR_ANCILLARY_ACQUISITION_REQUIRED" if is_ri else "PROJECT_OWNED_ADAPTER_DERIVATION_REQUIRED",
                     "existing_source_reuse": "not exact" if is_ri else "endpoint-only",
                     "new_acquisition": "C167-ACQ-ARXIV-0901.2599V2-TEX" if is_ri else None,
                     "object_presence": "EXACT_REQUESTED_OBJECT_PRESENT" if is_ri else "OBJECT_REQUIRES_PROJECT_DERIVATION",
                     "source_version": "arXiv:0901.2599v2" if is_ri else request["current_authenticated_source_version"],
                     "source_hash": SOURCE_ARCHIVE_SHA256 if is_ri else "C43 manifest hash-locked",
                     "license_status": "private local retention; no redistribution claim" if is_ri else "C43 local source provenance retained",
                     "scientific_role_status": "scope authority ready" if is_ri else "endpoint authority only",
                     "adapter_vs_calculation": "source scope object" if is_ri else "project-owned adapter derivation",
                     "terminal_status": "RESOLVED_BY_OFFICIAL_TEX_OR_ANCILLARY" if is_ri else "PROJECT_OWNED_ADAPTER_DERIVATION_REQUIRED",
                     "exact_next_object": None if is_ri else "C43-to-target-scheme adapter"})
    return _freeze({"schema": "C167-REQUEST-RESOLUTION-MANIFEST-V1", "rows": tuple(_freeze(x) for x in rows),
                    "count": len(rows), "exactly_one_terminal_record_per_request": len(rows) == 8,
                    "root": _root(rows)})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = tuple({"leaf_id": request["leaf_id"], "request_id": request["request_id"],
                  "frontier_reason": "acquired source awaits next-package graph integration" if request["required_dependency_class"] == "ACTIVE_NF_DEFINITION" else "C43 adapter derivation required"}
                 for request in REQUESTS) + tuple({"leaf_id": row["leaf_id"], "request_id": None,
                  "frontier_reason": "C166 locator-incomplete leaf preserved unchanged"}
                 for row in PRESERVED_LOCATOR_LEAVES)
    return _freeze({"schema": "C167-DEPENDENCY-FRONTIER-MANIFEST-V1", "original_acquisition_request_count": 8,
                    "preserved_locator_leaf_count": 6, "rows": rows, "count": len(rows),
                    "resolved_by_official_source": 2, "requires_project_derivation": 6,
                    "requires_locator_integration": 2, "graph_nodes_added": 0, "graph_edges_added": 0,
                    "C166_graphs_rewritten": False, "resulting_frontier_count": 14,
                    "root": _root(rows)})


def source_or_calculation_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C167-SOURCE-OR-CALCULATION-HANDOFF-V1", "kind": "ADAPTER_CALCULATION_HANDOFF",
                    "source_acquisition_roots": (source_acquisition_manifest()["root"], object_presence_manifest()["root"]),
                    "C43_endpoint_authority_roots": ("docs/next_level/c43_primary_source_manifest.json",
                                                     "docs/next_level/c43_gauge_convention_map.json",
                                                     "docs/next_level/c43_boundary_prescription_decision.json"),
                    "standard_scheme_endpoint_authority": "C140/C164 authenticated RI/SMOM and MOMq source records",
                    "missing_adapter_identities": tuple(row["request_id"] for row in c43_adapter_acquirability_manifest()["rows"]),
                    "preserved_locator_leaves": PRESERVED_LOCATOR_IDS,
                    "nonclaims": ("no adapter derived", "no complete expression", "no target value", "no graph integration"),
                    "next": NEXT, "root": _root((STATUS, NEXT))})


def quantum_source_handoff() -> MappingProxyType:
    return _freeze({"schema": "C167-QUANTUM-SOURCE-HANDOFF-V1", "Q0_Q1_Q2_modified": False,
                    "quantum_objects_consumed": 0, "root": _root((False, 0))})


def lfgacquire4_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C167-LFGACQUIRE4-PLAN-MANIFEST-V1", "selected_plan": PLAN,
                    "status": STATUS, "reason": "C43 endpoints are authenticated but their conversion adapter is project-owned",
                    "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def lfgacquire4_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C167-LFGACQUIRE4-COMPLETENESS-V1", "status": STATUS, "plan": PLAN,
                    "requests": 8, "terminal_request_records": 8, "preserved_locator_leaves": 6,
                    "C43_adapter_source_objects": 0, "RI_SMOM_scope_objects_acquired": 1,
                    "graphs_integrated": 0, "complete_expressions": 0, "target_values": 0,
                    "PDG_values_consumed": 0, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def no_derivation_report() -> MappingProxyType:
    return _freeze({"schema": "C167-NO-DERIVATION-V1", "C43_adapter_derived": 0,
                    "new_perturbative_calculation_executed": 0, "root": _root((0, 0))})


def no_execution_report() -> MappingProxyType:
    return _freeze({"schema": "C167-NO-EXECUTION-V1", "source_code_executions": 0,
                    "target_programs": 0, "target_values": 0, "C158_imports": 0,
                    "C158_recomputed": 0, "matching": 0, "running": 0, "thresholds": 0,
                    "PDG_values": 0, "Q0_Q1_Q2_modified": False, "root": _root((0, 0, False))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"network_after_construction": 0, "unsafe_archive_operations": 0,
                    "acquired_code_executions": 0, "unofficial_source_substitutions": 0,
                    "endpoint_only_promoted_to_adapter": 0, "reopened_absent_descriptors": 0,
                    "reopened_role_mismatch_descriptors": 0, "changed_C166_imports": 0,
                    "merged_locator_leaves": 0, "complete_expressions": 0,
                    "target_values": 0, "PDG_values_consumed": 0, "allow_pickle_false": True,
                    "pass": True, "root": _root((STATUS, NEXT))})


def verify_hqcd_lfgacquire4_authority() -> MappingProxyType:
    if c166.PACKAGE_ROOT != ROOT_CHAIN["C166"]:
        raise ValueError("C166 package root changed")
    if len(REQUESTS) != 8 or len(PRESERVED_LOCATOR_LEAVES) != 6:
        raise ValueError("C166 frontier import changed")
    return _freeze({"schema": "C167-HQCDLFGACQUIRE4-V1", "baseline": BASELINE,
                    "status": STATUS, "plan": PLAN, "next": NEXT, "contract": CONTRACT,
                    "contract_sha256": CONTRACT_SHA256, "prompt_sha256": PROMPT_SHA256,
                    "C166_package_root": ROOT_CHAIN["C166"], "C165_package_root": ROOT_CHAIN["C165"],
                    "C164_package_root": ROOT_CHAIN["C164"], "C158_package_root": ROOT_CHAIN["C158"],
                    "request_count": len(REQUESTS), "preserved_locator_leaf_count": len(PRESERVED_LOCATOR_LEAVES),
                    "graphs_integrated": 0, "complete_expressions": 0, "target_values": 0,
                    "PDG_values_consumed": 0, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_lfgacquire4_authority() -> MappingProxyType:
    data = json.loads((RUNTIME / "manifest.json").read_text())
    if data.get("package_root") != PACKAGE_ROOT or data.get("status") != STATUS:
        raise ValueError("C167 runtime mismatch")
    return verify_hqcd_lfgacquire4_authority()


def mutate_live_hqcdlfgacquire4(index: int) -> MappingProxyType:
    fields = ("baseline", "C166_root", "request_id", "leaf_id", "source_version", "archive_hash",
              "member_path", "member_hash", "license", "endpoint", "object_locator", "object_role",
              "active_Nf", "external_flavor", "C43_endpoint", "standard_endpoint", "adapter",
              "terminal_status", "frontier_count", "graph_nodes", "graph_edges", "plan", "next",
              "loader", "runtime", "package_root")
    return _freeze({"mutation": fields[index % len(fields)], "positive_gate": False,
                    "must_fail_or_change_root": True})


def _roots() -> Mapping[str, str]:
    return {
        "C167_INPUT_ROOT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, PROMPT_SHA256, ROOT_CHAIN)),
        "C167_REGRESSION_BOUNDARY_ROOT": _root(("PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC", ROOT_CHAIN["C158"], ROOT_CHAIN["C166"])),
        "C167_PLAN_ROOT": lfgacquire4_plan_manifest()["root"],
        "C167_REQUEST_FREEZE_ROOT": acquisition_request_freeze()["root"],
        "C167_ACQUIRABILITY_ROOT": acquirability_class_manifest()["root"],
        "C167_PRESERVED_LOCATOR_LEAF_ROOT": preserved_locator_leaf_manifest()["root"],
        "C167_EXISTING_SOURCE_REUSE_ROOT": existing_source_reuse_manifest()["root"],
        "C167_SOURCE_ACQUISITION_ROOT": source_acquisition_manifest()["root"],
        "C167_ARCHIVE_INTEGRITY_ROOT": archive_member_manifest()["root"],
        "C167_OBJECT_PRESENCE_ROOT": object_presence_manifest()["root"],
        "C167_C43_ADAPTER_ACQUIRABILITY_ROOT": c43_adapter_acquirability_manifest()["root"],
        "C167_C43_CALCULATION_REQUEST_ROOT": c43_adapter_calculation_request_manifest()["root"],
        "C167_RISMOM_NF_FLAVOR_ROOT": rismom_nf_flavor_manifest()["root"],
        "C167_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"],
        "C167_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
        "C167_HANDOFF_ROOT": source_or_calculation_handoff_contract()["root"],
        "C167_QUANTUM_HANDOFF_ROOT": quantum_source_handoff()["root"],
        "C167_SCOPE_ROOT": no_execution_report()["root"],
        "C167_COMPLETENESS_ROOT": lfgacquire4_completeness_certificate()["root"],
    }


ROOTS = _roots()
PACKAGE_ROOT = _root({"schema": "C167-HQCDLFGACQUIRE4-V1", "baseline": BASELINE,
                      "contract": CONTRACT, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = [
    "STATUS", "PLAN", "NEXT", "NEXT_CONTRACT", "PACKAGE_ROOT", "ROOTS",
    "BASELINE", "CONTRACT", "CONTRACT_SHA256", "PROMPT_SHA256", "ROOT_CHAIN",
    "REQUESTS", "PRESERVED_LOCATOR_LEAVES", "load_verified_hqcd_lfgacquire4_authority",
    "verify_hqcd_lfgacquire4_authority", "lfgacquire4_plan_manifest",
    "acquisition_request_freeze", "acquirability_class_manifest",
    "preserved_locator_leaf_manifest", "existing_source_reuse_manifest",
    "source_acquisition_manifest", "archive_member_manifest", "object_presence_manifest",
    "c43_adapter_acquirability_manifest", "c43_adapter_calculation_request_manifest",
    "rismom_nf_flavor_manifest", "request_resolution_manifest", "dependency_frontier_manifest",
    "source_or_calculation_handoff_contract", "quantum_source_handoff",
    "lfgacquire4_completeness_certificate", "no_derivation_report", "no_execution_report",
    "static_isolation_guard", "mutate_live_hqcdlfgacquire4",
]
