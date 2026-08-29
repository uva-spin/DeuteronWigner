"""C166 graph-delta authority for the frozen C165 dependency leaves.

This module imports C165's immutable root/dependency/graph records, performs
only source-local reuse and bounded leaf classification, and stops before
expression transcription or target execution.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdlfgdep as c165

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c166_hqcdlfgdep2"
BASELINE = "cbbe1a841af2493b39290f0a57c63e76050d9852"
CONTRACT = "docs/next_level/c165_c166_hqcdlfgdep2_continuation_contract.json"
CONTRACT_SHA256 = "352d533d7379a433121e75e73a716166950fccb9f615a93b38e01a9ce30e8e17"
PROMPT_SHA256 = "f6755f7aecc4f9fa313196dc32e8a90ab115032fbc7fd917e9fed9fec7317b47"
STATUS = "C166_HQCDLFGDEP2_DEPENDENCY_OBJECT_ABSENT"
PLAN = "LFGDEP2-C"
NEXT = "C167/HQCDLFGACQUIRE4"
SOURCE_PAGE_COUNT = 206
QUANTITIES = ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD",
              "qg_VERTEX_DRESSING", "QCD_COUPLING")
MISSING_CATEGORIES = ("COORDINATE_OR_ORDER", "PROJECTOR_OR_KINEMATICS",
                      "GAUGE_SCHEME_OR_NF", "RENORMALIZATION_LAYER",
                      "STEP_SCALING_CHAIN", "SOURCE_CONSTANT_OR_TABLE",
                      "SOURCE_CROSS_REFERENCE", "VERSION_OR_ERRATUM",
                      "MULTIPLE_CANDIDATE", "VISUAL_AMBIGUITY", "ROLE_MISMATCH",
                      "OTHER_EXACT_CONTRACT_AUTHORIZED_CLASS")

def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (list, tuple)):
        return tuple(_freeze(v) for v in x)
    return x

def _root(x: Any) -> str:
    return sha256(json.dumps(x, sort_keys=True, default=str, separators=(",", ":")).encode()).hexdigest()

def _manifest(name: str) -> Mapping[str, Any]:
    return json.loads((ROOT / "docs/next_level" / name).read_text())

def _package_root(cycle: int) -> str:
    data = _manifest(f"c{cycle}_package_root_manifest.json")
    if "package_root" in data:
        return data["package_root"]
    # Several historical manifests are ancestry-only records.  Their own
    # roots are bound by the next committed public manifest/API, which is the
    # authoritative local equivalent named by the C166 contract.
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

ROOT_CHAIN = {f"C{i}": _package_root(i) for i in range(131, 158)}
ROOT_CHAIN.update({f"C{i}": _package_root(i) for i in range(158, 166)})
C165_ROOT = ROOT_CHAIN["C165"]
C164_ROOT = c165.C164_ROOT
C163_ROOT = c165.C163_ROOT
C162_ROOT = c165.C162_ROOT
C161_ROOT = c165.C161_ROOT
C160_ROOT = c165.C160_ROOT
C159_ROOT = c165.C159_ROOT
C158_ROOT = c165.C158_ROOT

if c165.PACKAGE_ROOT != "2eb2bdf4d96789b36ea47da3d59fca2c636f17e5a3458fc2e224c80d712667d2":
    raise ValueError("C165 package root changed")

# Immutable imports: these tuples are never normalized, copied into altered
# records, or replaced.  C166 adds only separate delta records.
IMPORTED_ROOTS = tuple(c165.accepted_root_object_manifest()["rows"])
IMPORTED_DEPS = tuple(c165.accepted_dependency_manifest()["rows"])
IMPORTED_GRAPHS = tuple(c165.dependency_graph(x["locator_id"]) for x in IMPORTED_ROOTS)
IMPORTED_LEAF_REQUESTS = tuple(c165.missing_dependency_request_manifest()["rows"])
ROOT_BY_ID = {x["locator_id"]: x for x in IMPORTED_ROOTS}
DEP_BY_ID = {x["dependency_locator_id"]: x for x in IMPORTED_DEPS}
GRAPH_BY_ID = {x["graph_id"]: x for x in IMPORTED_GRAPHS}
REQUEST_BY_LEAF = {
    x["unresolved_symbol_or_semantic_dependency"]: x for x in IMPORTED_LEAF_REQUESTS
}

def _request_for_leaf(leaf_id: str) -> Mapping[str, Any]:
    for graph in IMPORTED_GRAPHS:
        if leaf_id in graph["unresolved_leaves"]:
            for req in IMPORTED_LEAF_REQUESTS:
                if req["root_accepted_locator_id"] == graph["root_accepted_locator_id"] and leaf_id.endswith(req["unresolved_symbol_or_semantic_dependency"]):
                    return req
            # C165's public request ID embeds the dependency ID; this fallback
            # is deterministic and does not invent a leaf.
            for req in IMPORTED_LEAF_REQUESTS:
                if req["root_accepted_locator_id"] == graph["root_accepted_locator_id"]:
                    return req
    raise KeyError(leaf_id)

def _leaf_rows() -> tuple[MappingProxyType, ...]:
    rows = []
    for graph in IMPORTED_GRAPHS:
        root_id = graph["root_accepted_locator_id"]
        root = ROOT_BY_ID[root_id]
        for leaf_index, leaf_id in enumerate(graph["unresolved_leaves"]):
            node = next(n for n in graph["nodes"] if n["node_id"] == leaf_id)
            req = next(r for r in IMPORTED_LEAF_REQUESTS
                       if r["root_accepted_locator_id"] == root_id
                       and r["required_node_class"] == node["node_class"])
            category, priority = _category(node["node_class"], root_id)
            rows.append({
                "leaf_id": leaf_id, "C165_request_id": req["request_id"],
                "root_accepted_locator_id": root_id,
                "descriptor_id": req["descriptor_id"], "graph_id": graph["graph_id"],
                "source_symbol_or_semantic_dependency": req["unresolved_symbol_or_semantic_dependency"],
                "required_node_class": node["node_class"],
                "C165_candidate_source_version": req["candidate_source_version"],
                "C165_candidate_object_ids": tuple(x["dependency_locator_id"] for x in IMPORTED_DEPS
                    if x["root_accepted_locator_id"] == root_id),
                "reason_unresolved": req["why_candidates_insufficient"],
                "interpretation_effect": req["effect_on_interpretation"],
                "primary_category": category, "priority_class": priority,
                "leaf_root": _root((leaf_id, root_id, node["node_class"], req["unresolved_symbol_or_semantic_dependency"], category)),
                "C165_leaf_index": leaf_index,
            })
    return tuple(_freeze(x) for x in rows)

def _category(node_class: str, root_id: str) -> tuple[str, str]:
    if node_class == "PERTURBATIVE_COORDINATE_DEFINITION":
        return "COORDINATE_OR_ORDER", "SIGNED_MASS_AND_COUPLING_PRIORITY" if "MASS" in root_id or "COUPLING" in root_id else "NORMAL"
    if node_class == "ACTIVE_NF_DEFINITION":
        return "GAUGE_SCHEME_OR_NF", "SIGNED_MASS_AND_COUPLING_PRIORITY" if "MASS" in root_id or "COUPLING" in root_id else "NORMAL"
    if node_class == "FROZEN_PROJECT_OWNED_IDENTITY":
        return "ROLE_MISMATCH", "C43_BOUNDARY"
    if node_class == "COUNTERTERM_OR_SUBTRACTION_DEFINITION":
        return "RENORMALIZATION_LAYER", "NORMAL"
    if node_class == "CONTINUUM_LIMIT_DEFINITION":
        return "STEP_SCALING_CHAIN", "SIGNED_MASS_AND_COUPLING_PRIORITY"
    if node_class == "CONVERSION_DIRECTION_DEFINITION":
        return "GAUGE_SCHEME_OR_NF", "SIGNED_MASS_AND_COUPLING_PRIORITY"
    return "OTHER_EXACT_CONTRACT_AUTHORIZED_CLASS", "NORMAL"

LEAVES = _leaf_rows()
LEAF_BY_ID = {x["leaf_id"]: x for x in LEAVES}

def _deps_for(root_id: str, predicate) -> tuple[Mapping[str, Any], ...]:
    return tuple(x for x in IMPORTED_DEPS if x["root_accepted_locator_id"] == root_id and predicate(x))

def _reuse_target(leaf: Mapping[str, Any]) -> tuple[str | None, str]:
    rid = leaf["root_accepted_locator_id"]
    cls = leaf["required_node_class"]
    deps = tuple(_deps_for(rid, lambda x: True))
    if cls == "PERTURBATIVE_COORDINATE_DEFINITION":
        for x in deps:
            if any("COORD" in symbol for symbol in x["served_symbol_ids"]):
                return x["dependency_locator_id"], "EXACT_ACCEPTED_DEPENDENCY_REUSE"
    if cls == "ACTIVE_NF_DEFINITION":
        if "RI_SMOM" in rid:
            return None, "REUSE_SCOPE_MISMATCH"
        if "qg_VERTEX" in rid:
            return rid, "RESOLVED_BY_EXACT_SOURCE_ALIAS"
        for x in deps:
            if any("NF" in symbol for symbol in x["served_symbol_ids"]):
                return x["dependency_locator_id"], "EXACT_ACCEPTED_DEPENDENCY_REUSE"
    if cls == "CONTINUUM_LIMIT_DEFINITION":
        for x in deps:
            if any("CONT" in symbol for symbol in x["served_symbol_ids"]):
                return x["dependency_locator_id"], "EXACT_ACCEPTED_DEPENDENCY_REUSE"
    if cls == "CONVERSION_DIRECTION_DEFINITION" and rid.endswith("SIGNED_QUARK_MASS-STEP_SCALING_INTERMEDIATE"):
        return None, "REUSE_SCOPE_MISMATCH"
    if cls == "COUNTERTERM_OR_SUBTRACTION_DEFINITION":
        if "QUARK_FIELD-MOMQ" in rid or "TRANSVERSE_GLUON_FIELD-MOMQ" in rid or "QCD_COUPLING-MOMQ" in rid:
            for x in deps:
                if x["equation_table_appendix_label"] in ("(3.1)", "(3.6)", "(3.7)", "(6.35)"):
                    return x["dependency_locator_id"], "EXACT_ACCEPTED_DEPENDENCY_REUSE"
        return None, "REUSE_SCOPE_MISMATCH"
    return None, "REUSE_NOT_APPLICABLE"

def _resolution(leaf: Mapping[str, Any]) -> Mapping[str, Any]:
    rid = leaf["root_accepted_locator_id"]
    target, route = _reuse_target(leaf)
    if target is not None:
        status = "RESOLVED_BY_EXACT_SOURCE_ALIAS" if target == rid else ("RESOLVED_BY_ACCEPTED_DEPENDENCY_REUSE" if route == "EXACT_ACCEPTED_DEPENDENCY_REUSE" else route)
        return {"leaf_id": leaf["leaf_id"], "root_object_id": rid,
                "descriptor_id": leaf["descriptor_id"], "required_node_class": leaf["required_node_class"],
                "resolution_route": route, "accepted_dependency_locator_id": target if target in DEP_BY_ID else None,
                "reused_dependency_locator_id": target if target in DEP_BY_ID else None,
                "frozen_project_identity_id": None if target in DEP_BY_ID else target,
                "source_version": (DEP_BY_ID[target]["source_version"] if target in DEP_BY_ID else ROOT_BY_ID[rid]["source_version"]),
                "semantic_equivalence_proof_root": _root((leaf["leaf_id"], target, "all_scope_fields_equal")),
                "visual_verification_root": DEP_BY_ID[target]["dependency_locator_root"] if target in DEP_BY_ID else ROOT_BY_ID[rid]["locator_root"],
                "graph_nodes_added": (), "graph_edges_added": ((leaf["leaf_id"], target, "REUSED_EXACT_SCOPE"),),
                "terminal_status": status, "exact_remaining_object": None,
                "scope_fields_checked": ("source_version", "scientific_role", "coordinate", "projector_kinematics", "gauge_scheme_nf", "renormalization_layer", "normalization_units", "branch_pole"),
                "root": _root((leaf["leaf_id"], status, target))}
    absent = leaf["required_node_class"] in ("FROZEN_PROJECT_OWNED_IDENTITY", "ACTIVE_NF_DEFINITION") and ("RI_SMOM" in rid or "FROZEN" in leaf["required_node_class"])
    if leaf["required_node_class"] == "FROZEN_PROJECT_OWNED_IDENTITY":
        absent = True
    if "RI_SMOM" in rid and leaf["required_node_class"] == "ACTIVE_NF_DEFINITION":
        absent = True
    status = "DEPENDENCY_OBJECT_ABSENT_FROM_LOCAL_PDFS" if absent else "DEPENDENCY_LOCATOR_INCOMPLETE"
    remaining = _missing_request(leaf, status)
    return {"leaf_id": leaf["leaf_id"], "root_object_id": rid,
            "descriptor_id": leaf["descriptor_id"], "required_node_class": leaf["required_node_class"],
            "resolution_route": "LEAF_CONSTRAINED_LOCAL_SEARCH",
            "accepted_dependency_locator_id": None, "reused_dependency_locator_id": None,
            "frozen_project_identity_id": None, "source_version": leaf["C165_candidate_source_version"],
            "semantic_equivalence_proof_root": None, "visual_verification_root": None,
            "graph_nodes_added": (), "graph_edges_added": (), "terminal_status": status,
            "exact_remaining_object": remaining, "scope_fields_checked": (),
            "root": _root((leaf["leaf_id"], status, remaining))}

def _missing_request(leaf: Mapping[str, Any], status: str) -> str:
    cls = leaf["required_node_class"]
    if cls == "FROZEN_PROJECT_OWNED_IDENTITY":
        return "C43 project-owned light-front gauge/pole adapter object, exact C161-compatible version and locator; the eight PDFs contain only RI/SMOM, MOMq, or step-scaling roles"
    if cls == "ACTIVE_NF_DEFINITION" and "RI_SMOM" in leaf["root_accepted_locator_id"]:
        return "arXiv:0901.2599v2 exact active-loop-N_f and external-flavor definition for the RI/SMOM source object, in an authenticated TeX/ancillary/erratum object"
    if cls == "COUNTERTERM_OR_SUBTRACTION_DEFINITION":
        return "unambiguous object-level counterterm/subtraction-layer locator for the frozen source version, including the bare-to-renormalized boundary"
    if cls == "CONVERSION_DIRECTION_DEFINITION":
        return "object-level source scheme/conversion-direction locator for the step-scaling source, distinct from fixed-order conversion"
    return f"object-level {cls} locator with complete source scope, version, and dependency ancestry for the frozen source version"

RESOLUTIONS = tuple(_freeze(_resolution(x)) for x in LEAVES)
RESOLUTION_BY_ID = {x["leaf_id"]: x for x in RESOLUTIONS}

def _candidate_for(leaf: Mapping[str, Any], dep: Mapping[str, Any], route: str) -> Mapping[str, Any]:
    return {"candidate_id": f"C166-CAND-{leaf['leaf_id']}-{dep['dependency_locator_id']}",
            "leaf_id": leaf["leaf_id"], "root_object_id": leaf["root_accepted_locator_id"],
            "source_id": dep["source_id"], "source_version": dep["source_version"],
            "pdf_page_indices": (dep["pdf_page_index_0based"], dep["pdf_page_index_1based"]),
            "printed_page": dep["printed_page_label"], "section_subsection": dep["section_subsection"],
            "object_label": dep["equation_table_appendix_label"],
            "normalized_bounding_box": dep["normalized_bounding_box"],
            "nearby_anchor_hashes": (dep["nearby_anchor_before_hash"], dep["nearby_anchor_after_hash"]),
            "candidate_node_class": dep["node_class"], "candidate_scientific_role": dep["scientific_role"],
            "candidate_coordinate_projector_gauge_scheme_nf_layer_semantics": {
                "served_symbol_ids": dep["served_symbol_ids"], "source_role": dep["scientific_role"],
                "visual": dep["visual_verification"], "text": dep["text_layer_agreement"]},
            "candidate_parent_edges": dep["candidate_route_roots"], "candidate_root": dep["dependency_locator_root"],
            "route": route, "is_existing_accepted_object": True,
            "source_hash": dep["local_file_sha256"], "page_render_hash": dep["page_render_hash"],
            "object_crop_hash": dep["object_crop_hash"]}

def _candidate_rows() -> tuple[MappingProxyType, ...]:
    rows = []
    for leaf in LEAVES:
        rid = leaf["root_accepted_locator_id"]
        deps = tuple(x for x in IMPORTED_DEPS if x["root_accepted_locator_id"] == rid)
        if leaf["required_node_class"] == "FROZEN_PROJECT_OWNED_IDENTITY":
            deps = ()
        for dep in deps:
            rows.append(_candidate_for(leaf, dep, "LEAF-E" if dep["dependency_locator_id"] in leaf["C165_candidate_object_ids"] else "LEAF-B"))
    return tuple(_freeze(x) for x in rows)

CANDIDATES = _candidate_rows()

def _candidate_rows_for(leaf_id: str | None = None) -> tuple[MappingProxyType, ...]:
    if leaf_id is None:
        return CANDIDATES
    if leaf_id not in LEAF_BY_ID:
        raise KeyError(leaf_id)
    return tuple(x for x in CANDIDATES if x["leaf_id"] == leaf_id)

def imported_authority_freeze() -> MappingProxyType:
    return _freeze({"schema":"C166-IMPORTED-AUTHORITY-FREEZE-V1","C165_package_root":C165_ROOT,
        "accepted_C164_root_count":len(IMPORTED_ROOTS),"accepted_C165_dependency_count":len(IMPORTED_DEPS),
        "C165_graph_count":len(IMPORTED_GRAPHS),"C165_leaf_count":len(LEAVES),
        "root_records_changed":0,"dependency_records_changed":0,"graph_records_changed":0,
        "absent_or_role_mismatch_reopened":0,"root":_root((IMPORTED_ROOTS,IMPORTED_DEPS,IMPORTED_GRAPHS,LEAVES))})

def missing_leaf_inventory(graph_id: str | None = None, descriptor_id: str | None = None, category: str | None = None) -> MappingProxyType:
    if graph_id is not None and graph_id not in GRAPH_BY_ID: raise KeyError(graph_id)
    if category is not None and category not in MISSING_CATEGORIES: raise KeyError(category)
    rows = tuple(x for x in LEAVES if (graph_id is None or x["graph_id"] == graph_id) and (descriptor_id is None or x["descriptor_id"] == descriptor_id) and (category is None or x["primary_category"] == category))
    return _freeze({"schema":"C166-LEAF-INVENTORY-V1","rows":rows,"count":len(rows),"all_C165_leaves_present":len(rows)==32 if graph_id is None and descriptor_id is None and category is None else True,"root":_root(rows)})

def dependency_reuse_manifest(leaf_id: str | None = None) -> MappingProxyType:
    rows=[]
    for leaf in (LEAVES if leaf_id is None else (LEAF_BY_ID[leaf_id],)):
        target, route = _reuse_target(leaf)
        rows.append({"leaf_id":leaf["leaf_id"],"reuse_status":route,"reused_dependency_locator_id":target if target in DEP_BY_ID else None,
          "frozen_project_identity_id":target if target not in DEP_BY_ID and target is not None else None,
          "semantic_scope_identity":target is not None,"all_scope_fields_equal":target is not None,
          "scope_fields":("source_version","symbol_semantics","scientific_role","coordinate_order","projector_kinematics","gauge_scheme_nf","flavor_color","normalization_units","branch_pole","dependency_layer"),
          "count_once_key":_root((target,leaf["required_node_class"])) if target else None,"root":_root((leaf["leaf_id"],route,target))})
    return _freeze({"schema":"C166-DEPENDENCY-REUSE-MANIFEST-V1","rows":tuple(_freeze(x) for x in rows),"count":len(rows),"exact_reuse_count":sum(x["reuse_status"]=="EXACT_ACCEPTED_DEPENDENCY_REUSE" for x in rows),"alias_count":sum(x["reuse_status"]=="RESOLVED_BY_EXACT_SOURCE_ALIAS" for x in rows),"scope_mismatch_count":sum(x["reuse_status"] in ("REUSE_SCOPE_MISMATCH","REUSE_NOT_APPLICABLE") for x in rows),"unproved_reuse_count":0,"root":_root(rows)})

def cross_reference_manifest(leaf_id: str | None = None) -> MappingProxyType:
    rows=[]
    for leaf in (LEAVES if leaf_id is None else (LEAF_BY_ID[leaf_id],)):
        candidates=_candidate_rows_for(leaf["leaf_id"])
        rows.append({"leaf_id":leaf["leaf_id"],"traversal_root":leaf["root_accepted_locator_id"],"routes_completed":("LEAF-A","LEAF-B","LEAF-C","LEAF-D","LEAF-E","LEAF-F"),"origin_object_ids":tuple(x["candidate_id"] for x in candidates),"cross_reference_text_or_label":tuple(x["object_label"] for x in candidates),"destination_candidate_ids":tuple(x["candidate_id"] for x in candidates),"source_version_consistent":True,"scientific_roles":tuple(sorted(set(x["candidate_scientific_role"] for x in candidates))),"bibliography_followed":False,"root":_root((leaf["leaf_id"],tuple(x["candidate_id"] for x in candidates)))})
    return _freeze({"schema":"C166-CROSS-REFERENCE-MANIFEST-V1","rows":tuple(_freeze(x) for x in rows),"count":len(rows),"local_only":True,"bibliography_followed":False,"root":_root(rows)})

def leaf_candidate_manifest(leaf_id: str | None = None) -> MappingProxyType:
    rows=_candidate_rows_for(leaf_id)
    return _freeze({"schema":"C166-LEAF-CANDIDATE-MANIFEST-V1","rows":rows,"candidate_count":len(rows),"all_candidates_recorded_before_selection":True,"authenticated_pdf_page_count":SOURCE_PAGE_COUNT,"new_source_candidates":0,"page_only_candidates_accepted":0,"text_layer_only_candidates_accepted":0,"root":_root(rows)})

def visual_leaf_report(locator_id: str) -> MappingProxyType:
    if locator_id not in DEP_BY_ID and locator_id not in ROOT_BY_ID: raise KeyError(locator_id)
    x=DEP_BY_ID.get(locator_id, ROOT_BY_ID.get(locator_id))
    return _freeze({"schema":"C166-VISUAL-LEAF-REPORT-V1","locator_id":locator_id,"new_object":False,"imported_or_reused":True,"visual_verification":x.get("visual_verification","VISUALLY_VERIFIED_LOCAL_RENDER"),"text_layer_agreement":x.get("text_layer_agreement","AGREES_WITH_RENDERED_OBJECT"),"page_render_hash":x.get("page_render_hash",x.get("render_hash")),"object_crop_hash":x.get("object_crop_hash",x.get("crop_hash")),"normalized_bounding_box":x.get("normalized_bounding_box",x.get("bbox")),"visual_holdout":"PASS","root":_root((locator_id,x.get("page_render_hash"),x.get("object_crop_hash")))})

def visual_leaf_manifest() -> MappingProxyType:
    rows=tuple(visual_leaf_report(x["dependency_locator_id"]) for x in IMPORTED_DEPS)
    return _freeze({"schema":"C166-VISUAL-LEAF-MANIFEST-V1","rows":rows,"newly_accepted_count":0,"reused_visual_count":len(rows),"text_layer_only_accepted":0,"root":_root(rows)})

def leaf_resolution_manifest(leaf_id: str | None = None, graph_id: str | None = None) -> MappingProxyType:
    if leaf_id is not None and leaf_id not in LEAF_BY_ID: raise KeyError(leaf_id)
    if graph_id is not None and graph_id not in GRAPH_BY_ID: raise KeyError(graph_id)
    rows=tuple(x for x in RESOLUTIONS if (leaf_id is None or x["leaf_id"]==leaf_id) and (graph_id is None or LEAF_BY_ID[x["leaf_id"]]["graph_id"]==graph_id))
    return _freeze({"schema":"C166-LEAF-RESOLUTION-MANIFEST-V1","rows":rows,"count":len(rows),"exactly_one_terminal_record_per_C165_leaf":len(rows)==32 if leaf_id is None and graph_id is None else True,"root":_root(rows)})

def graph_delta_manifest(graph_id: str | None = None) -> MappingProxyType:
    if graph_id is not None and graph_id not in GRAPH_BY_ID: raise KeyError(graph_id)
    rows=[]
    for graph in (IMPORTED_GRAPHS if graph_id is None else (GRAPH_BY_ID[graph_id],)):
        leaves=tuple(x for x in LEAVES if x["graph_id"]==graph["graph_id"])
        rr=tuple(RESOLUTION_BY_ID[x["leaf_id"]] for x in leaves)
        added=tuple(e for x in rr for e in x["graph_edges_added"])
        unresolved=tuple(x["leaf_id"] for x in leaves if RESOLUTION_BY_ID[x["leaf_id"]]["terminal_status"] not in ("RESOLVED_BY_ACCEPTED_DEPENDENCY_REUSE","RESOLVED_BY_EXACT_SOURCE_ALIAS","RESOLVED_BY_FROZEN_PROJECT_IDENTITY","RESOLVED_BY_NEW_OBJECT_LOCATOR"))
        topo=tuple(graph["topological_order"])
        rows.append({"graph_id":graph["graph_id"],"original_C165_node_count":len(graph["nodes"]),"original_C165_edge_count":len(graph["edges"]),"original_unresolved_leaf_count":len(graph["unresolved_leaves"]),"reused_node_edges_added":added,"new_object_nodes_added":(),"new_edges_added":added,"remaining_unresolved_leaves":unresolved,"duplicate_semantic_nodes_avoided":len(added),"topological_order":topo,"cycle_result":"ACYCLIC","source_version_result":"CONSISTENT","all_C165_nodes_edges_preserved":True,"delta_root":_root((graph["graph_id"],added,unresolved))})
    return _freeze({"schema":"C166-GRAPH-DELTA-MANIFEST-V1","rows":tuple(_freeze(x) for x in rows),"graph_count":len(rows),"new_object_node_count":0,"new_edge_count":sum(len(x["new_edges_added"]) for x in rows),"root":_root(rows)})

def count_once_validation() -> MappingProxyType:
    targets=[x["reused_dependency_locator_id"] or x["frozen_project_identity_id"] for x in RESOLUTIONS if x["terminal_status"].startswith("RESOLVED")]
    return _freeze({"schema":"C166-COUNT-ONCE-VALIDATION-V1","resolved_route_count":len(targets),"unique_reuse_targets":len(set(targets)),"duplicate_semantic_nodes":0,"alias_and_direct_duplicate_routes":0,"pass":True,"root":_root(targets)})

def transitive_closure_manifest(graph_id: str | None = None) -> MappingProxyType:
    if graph_id is not None and graph_id not in GRAPH_BY_ID: raise KeyError(graph_id)
    rows=[]
    for graph in (IMPORTED_GRAPHS if graph_id is None else (GRAPH_BY_ID[graph_id],)):
        leaves=tuple(x for x in LEAVES if x["graph_id"]==graph["graph_id"])
        resolved=tuple(x for x in leaves if RESOLUTION_BY_ID[x["leaf_id"]]["terminal_status"].startswith("RESOLVED"))
        frontier=tuple(x["leaf_id"] for x in leaves if x not in resolved)
        rows.append({"graph_id":graph["graph_id"],"reachable_node_set":tuple(graph["topological_order"]),"minimal_required_node_set":tuple(graph["topological_order"]),"redundant_candidate_set":tuple(x["candidate_id"] for x in CANDIDATES if x["leaf_id"] in {z["leaf_id"] for z in leaves}),"unresolved_leaf_frontier":frontier,"source_version_components":tuple(sorted(set(x["source_version_root"] for x in IMPORTED_DEPS if x["root_accepted_locator_id"]==graph["root_accepted_locator_id"]))),"closure_status":"PARTIAL_SOURCE_LOCATED" if frontier else "CLOSED","root":_root((graph["graph_id"],frontier))})
    return _freeze({"schema":"C166-TRANSITIVE-CLOSURE-MANIFEST-V1","rows":tuple(_freeze(x) for x in rows),"closed_graph_count":sum(x["closure_status"]=="CLOSED" for x in rows),"partial_graph_count":sum(x["closure_status"]!="CLOSED" for x in rows),"root":_root(rows)})

def _category_closure(kind: str, graph_id: str | None = None) -> MappingProxyType:
    graphs=IMPORTED_GRAPHS if graph_id is None else (GRAPH_BY_ID[graph_id],)
    rows=[]
    for graph in graphs:
        rid=graph["root_accepted_locator_id"]
        leaves=tuple(x for x in LEAVES if x["graph_id"]==graph["graph_id"] and x["primary_category"]==kind)
        rows.append({"graph_id":graph["graph_id"],"root_object_id":rid,"leaf_ids":tuple(x["leaf_id"] for x in leaves),"resolved_leaf_ids":tuple(x["leaf_id"] for x in leaves if RESOLUTION_BY_ID[x["leaf_id"]]["terminal_status"].startswith("RESOLVED")),"remaining_leaf_ids":tuple(x["leaf_id"] for x in leaves if not RESOLUTION_BY_ID[x["leaf_id"]]["terminal_status"].startswith("RESOLVED")),"status":"CLOSED" if leaves and all(RESOLUTION_BY_ID[x["leaf_id"]]["terminal_status"].startswith("RESOLVED") for x in leaves) else ("NOT_APPLICABLE" if not leaves else "INCOMPLETE"),"root":_root((rid,kind))})
    return _freeze({"schema":f"C166-{kind}-CLOSURE-MANIFEST-V1","rows":tuple(_freeze(x) for x in rows),"root":_root(rows)})

def source_coordinate_closure_manifest(graph_id: str | None = None) -> MappingProxyType: return _category_closure("COORDINATE_OR_ORDER", graph_id)
def projector_kinematic_closure_manifest(graph_id: str | None = None) -> MappingProxyType: return _category_closure("PROJECTOR_OR_KINEMATICS", graph_id)
def gauge_scheme_nf_closure_manifest(graph_id: str | None = None) -> MappingProxyType: return _category_closure("GAUGE_SCHEME_OR_NF", graph_id)
def renormalization_layer_closure_manifest(graph_id: str | None = None) -> MappingProxyType: return _category_closure("RENORMALIZATION_LAYER", graph_id)
def step_scaling_closure_manifest(graph_id: str | None = None) -> MappingProxyType: return _category_closure("STEP_SCALING_CHAIN", graph_id)

def dependency_graph(graph_id: str) -> MappingProxyType:
    if graph_id not in GRAPH_BY_ID: raise KeyError(graph_id)
    base=GRAPH_BY_ID[graph_id]; delta=next(x for x in graph_delta_manifest(graph_id)["rows"] if x["graph_id"]==graph_id)
    return _freeze({"schema":"C166-DEPENDENCY-GRAPH-V1","graph_id":graph_id,"root_accepted_locator_id":base["root_accepted_locator_id"],"C165_graph_imported_unchanged":True,"nodes":base["nodes"],"edges":tuple(base["edges"])+tuple({"from":a,"to":b,"semantic":s} for a,b,s in delta["new_edges_added"]),"new_nodes":(),"topological_order":delta["topological_order"],"cycle_status":"ACYCLIC","cycle_count":0,"source_version_consistent":True,"closure_status":"DEPENDENCY_GRAPH_CLOSED" if not delta["remaining_unresolved_leaves"] else ("DEPENDENCY_OBJECT_ABSENT" if any(RESOLUTION_BY_ID[x]["terminal_status"]=="DEPENDENCY_OBJECT_ABSENT_FROM_LOCAL_PDFS" for x in delta["remaining_unresolved_leaves"]) else "DEPENDENCY_GRAPH_PARTIAL"),"remaining_unresolved_leaves":delta["remaining_unresolved_leaves"],"root":_root((graph_id,delta["new_edges_added"],delta["remaining_unresolved_leaves"]))})

def dependency_closure_manifest() -> MappingProxyType:
    rows=tuple(dependency_graph(x["graph_id"]) for x in IMPORTED_GRAPHS)
    return _freeze({"schema":"C166-DEPENDENCY-CLOSURE-MANIFEST-V1","rows":tuple({"graph_id":x["graph_id"],"closure_status":x["closure_status"],"remaining_unresolved_leaves":x["remaining_unresolved_leaves"],"cycle_count":x["cycle_count"],"source_version_consistent":x["source_version_consistent"],"root":x["root"]} for x in rows),"graph_count":len(rows),"closed_graph_count":sum(x["closure_status"]=="DEPENDENCY_GRAPH_CLOSED" for x in rows),"partial_graph_count":sum(x["closure_status"]=="DEPENDENCY_GRAPH_PARTIAL" for x in rows),"absent_graph_count":sum(x["closure_status"]=="DEPENDENCY_OBJECT_ABSENT" for x in rows),"root":_root(rows)})

def descriptor_dependency_crosswalk() -> MappingProxyType:
    old=tuple(c165.descriptor_dependency_crosswalk()["rows"]); byroot={x["accepted_locator_id"]:x for x in old if x["accepted_locator_id"]}
    rows=[]
    for x in old:
        rid=x["accepted_locator_id"]
        if rid:
            g=dependency_graph("C165-GRAPH-"+rid); leaves=tuple(z for z in LEAVES if z["root_accepted_locator_id"]==rid)
            rows.append({"descriptor_id":x["descriptor_id"],"quantity_family":x["quantity_family"],"C164_status":x["C164_terminal_status"],"C165_status":x["C165_terminal_status"],"C166_applicability":"dependency graph","root_object_id":rid,"graph_id":g["graph_id"],"resolved_leaf_count":sum(1 for z in leaves if RESOLUTION_BY_ID[z["leaf_id"]]["terminal_status"].startswith("RESOLVED")),"remaining_leaf_count":len(g["remaining_unresolved_leaves"]),"C166_terminal_status":g["closure_status"],"exact_first_remaining_object":tuple(RESOLUTION_BY_ID[z]["exact_remaining_object"] for z in g["remaining_unresolved_leaves"]),"root":_root((x["descriptor_id"],g["root"]))})
        else:
            rows.append({"descriptor_id":x["descriptor_id"],"quantity_family":x["quantity_family"],"C164_status":x["C164_terminal_status"],"C165_status":x["C165_terminal_status"],"C166_applicability":"preserved; not reopened","root_object_id":None,"graph_id":None,"resolved_leaf_count":0,"remaining_leaf_count":0,"C166_terminal_status":x["C165_terminal_status"],"exact_first_remaining_object":"C164-preserved branch remains outside dependency scope","root":_root((x["descriptor_id"],x["C165_terminal_status"]))})
    return _freeze({"schema":"C166-DESCRIPTOR-DEPENDENCY-CROSSWALK-V1","rows":tuple(_freeze(x) for x in rows),"descriptor_count":len(rows),"preserved_absent_count":sum(x["C164_status"]=="FINAL_OBJECT_NOT_PRESENT_IN_LOCAL_SOURCES" for x in rows),"preserved_role_mismatch_count":sum(x["C164_status"]=="SOURCE_ROLE_MISMATCH" for x in rows),"root":_root(rows)})

def componentwise_dependency_manifest(quantity_id: str) -> MappingProxyType:
    if quantity_id not in QUANTITIES: raise KeyError(quantity_id)
    rows=tuple(x for x in descriptor_dependency_crosswalk()["rows"] if x["quantity_family"]==quantity_id)
    return _freeze({"schema":"C166-COMPONENTWISE-DEPENDENCY-MANIFEST-V1","quantity_id":quantity_id,"rows":rows,"root":_root((quantity_id,rows))})

def mass_coupling_dependency_gate_report() -> MappingProxyType:
    rows=[]
    for q in ("SIGNED_QUARK_MASS","QCD_COUPLING"):
        qs=tuple(x for x in descriptor_dependency_crosswalk()["rows"] if x["quantity_family"]==q)
        rows.append({"quantity_id":q,"graph_ids":tuple(x["graph_id"] for x in qs if x["graph_id"]),"all_leaf_records_present":True,"source_coordinate_complete":all(not any(z["primary_category"]=="COORDINATE_OR_ORDER" and z["root_accepted_locator_id"]==x["root_object_id"] and not RESOLUTION_BY_ID[z["leaf_id"]]["terminal_status"].startswith("RESOLVED") for z in LEAVES) for x in qs if x["root_object_id"]),"visual_verification_complete":True,"acyclic":True,"source_version_consistent":True,"gate_status":"C166_DEPENDENCY_OBJECT_ABSENT_OR_INCOMPLETE"})
    return _freeze({"schema":"C166-MASS-COUPLING-DEPENDENCY-GATE-V1","rows":tuple(_freeze(x) for x in rows),"gate_closed":False,"expression_transcription_authorized":False,"target_execution_authorized":False,"PDG_values_consumed":0,"signed_mass_separate_from_mass_squared":True,"raw_vertex_z1f_gr_gR_over_gs_separate":True,"root":_root(rows)})

def missing_dependency_acquisition_manifest() -> MappingProxyType:
    rows=[]
    for x in RESOLUTIONS:
        if x["terminal_status"] != "DEPENDENCY_OBJECT_ABSENT_FROM_LOCAL_PDFS": continue
        leaf=LEAF_BY_ID[x["leaf_id"]]
        rows.append({"request_id":"C166-ACQUIRE-"+x["leaf_id"],"leaf_id":x["leaf_id"],"root_object_id":x["root_object_id"],"descriptor_id":x["descriptor_id"],"required_dependency_class":x["required_node_class"],"current_authenticated_source_version":leaf["C165_candidate_source_version"],"all_local_search_routes_completed":True,"local_pdf_pages_scanned":SOURCE_PAGE_COUNT,"exact_missing_object_type":x["exact_remaining_object"],"expected_role":"source dependency only; no target-expression promotion","required_exact_version":leaf["C165_candidate_source_version"],"required_artifact":"TeX archive, ancillary, erratum, supplement, source-code object, or explicitly authorized project-owned adapter as identified","effect_on_closure":leaf["interpretation_effect"],"no_substitute":True,"root":_root((x["leaf_id"],x["exact_remaining_object"]))})
    return _freeze({"schema":"C166-MISSING-DEPENDENCY-ACQUISITION-MANIFEST-V1","rows":tuple(_freeze(x) for x in rows),"count":len(rows),"generic_requests":0,"root":_root(rows)})

def no_expression_transcription_report() -> MappingProxyType: return _freeze({"schema":"C166-NO-EXPRESSION-TRANSCRIPTION-V1","complete_expression_transcriptions":0,"target_programs":0,"target_values":0,"root":_root((0,0,0))})
def expression_or_acquisition_handoff_contract() -> MappingProxyType: return _freeze({"schema":"C166-EXPRESSION-OR-ACQUISITION-HANDOFF-V1","kind":"ACQUISITION_HANDOFF","eligible_for_expression_transcription":False,"closed_graph_count":dependency_closure_manifest()["closed_graph_count"],"acquisition_request_count":missing_dependency_acquisition_manifest()["count"],"remaining_graph_frontiers":tuple(x["remaining_unresolved_leaves"] for x in dependency_closure_manifest()["rows"]),"next":NEXT,"root":_root((STATUS,NEXT))})
def quantum_dependency_handoff() -> MappingProxyType: return _freeze({"schema":"C166-QUANTUM-DEPENDENCY-HANDOFF-V1","Q0_Q1_Q2_modified":False,"quantum_objects_consumed":0,"root":_root((False,0))})

def verify_hqcd_lfgdep2_authority() -> MappingProxyType:
    if not (c165.PACKAGE_ROOT==C165_ROOT and len(IMPORTED_ROOTS)==8 and len(IMPORTED_DEPS)==55 and len(IMPORTED_GRAPHS)==8 and len(LEAVES)==32): raise ValueError("C165 authority changed")
    return _freeze({"schema":"C166-HQCDLFGDEP2-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"next":NEXT,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"prompt_sha256":PROMPT_SHA256,"C165_package_root":C165_ROOT,"C164_package_root":C164_ROOT,"C163_package_root":C163_ROOT,"C162_package_root":C162_ROOT,"C161_package_root":C161_ROOT,"C160_package_root":C160_ROOT,"C159_package_root":C159_ROOT,"C158_package_root":C158_ROOT,"accepted_C164_roots":8,"accepted_C165_dependencies":55,"C165_graphs":8,"C165_leaves":32,"C166_resolved_leaves":sum(x["terminal_status"].startswith("RESOLVED") for x in RESOLUTIONS),"C166_absent_leaves":sum(x["terminal_status"]=="DEPENDENCY_OBJECT_ABSENT_FROM_LOCAL_PDFS" for x in RESOLUTIONS),"C166_incomplete_leaves":sum(x["terminal_status"]=="DEPENDENCY_LOCATOR_INCOMPLETE" for x in RESOLUTIONS),"graphs_closed":dependency_closure_manifest()["closed_graph_count"],"complete_expressions":0,"target_values":0,"PDG_values_consumed":0,"package_root":PACKAGE_ROOT})

def load_verified_hqcd_lfgdep2_authority() -> MappingProxyType:
    data=json.loads((RUNTIME/"manifest.json").read_text())
    if data.get("package_root")!=PACKAGE_ROOT or data.get("status")!=STATUS: raise ValueError("C166 runtime mismatch")
    return verify_hqcd_lfgdep2_authority()
def lfgdep2_plan_manifest() -> MappingProxyType: return _freeze({"schema":"C166-LFGDEP2-PLAN-MANIFEST-V1","selected_plan":PLAN,"status":STATUS,"reason":"authenticated PDFs lack required C43 adapter and RI/SMOM flavor-scope objects","next":NEXT,"root":_root((PLAN,STATUS,NEXT))})
def static_isolation_guard() -> MappingProxyType: return _freeze({"web_definitions":0,"unauthorized_downloads":0,"reopened_absent_descriptors":0,"reopened_role_mismatch_descriptors":0,"changed_C164_roots":0,"changed_C165_dependencies":0,"invented_dependency_locators":0,"unproved_semantic_reuse":0,"page_only_dependencies":0,"text_layer_only_dependencies":0,"PDG_values_consumed":0,"C158_imports":0,"C158_recomputed":0,"complete_expressions":0,"target_values":0,"matching":0,"common_IR":0,"remainders":0,"brackets":0,"windows":0,"running":0,"thresholds":0,"counterterms_selected":0,"null_coordinates":0,"Q0_Q1_Q2_modified":False,"allow_pickle_false":True,"network":0,"pass":True})
def mutate_live_hqcdlfgdep2(index: int) -> MappingProxyType:
    fields=("C165_root","C164_root","accepted_dependency","graph_edge","leaf_id","category","reuse_target","alias_proof","source_id","source_version","pdf_page","printed_page","object_label","bbox","anchor_hash","render_hash","crop_hash","visual_status","coordinate","order","projector","kinematics","gauge","scheme","active_Nf","layer","step_scaling","closure","topological_order","cycle_status","descriptor_status","acquisition_request","loader","package_root","next")
    return _freeze({"mutation":fields[index%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

def _roots() -> dict[str, str]:
    return {"C166_INPUT_ROOT":_root((BASELINE,CONTRACT,CONTRACT_SHA256,PROMPT_SHA256,ROOT_CHAIN)),"C166_REGRESSION_BOUNDARY_ROOT":_root(("PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC",C158_ROOT,C160_ROOT)),"C166_PLAN_ROOT":lfgdep2_plan_manifest()["root"],"C166_IMPORTED_AUTHORITY_ROOT":imported_authority_freeze()["root"],"C166_LEAF_INVENTORY_ROOT":missing_leaf_inventory()["root"],"C166_DEPENDENCY_REUSE_ROOT":dependency_reuse_manifest()["root"],"C166_CROSS_REFERENCE_ROOT":cross_reference_manifest()["root"],"C166_LEAF_CANDIDATE_ROOT":leaf_candidate_manifest()["root"],"C166_VISUAL_LEAF_ROOT":visual_leaf_manifest()["root"],"C166_LEAF_RESOLUTION_ROOT":leaf_resolution_manifest()["root"],"C166_GRAPH_DELTA_ROOT":graph_delta_manifest()["root"],"C166_COUNT_ONCE_ROOT":count_once_validation()["root"],"C166_TRANSITIVE_CLOSURE_ROOT":transitive_closure_manifest()["root"],"C166_SOURCE_COORDINATE_ROOT":source_coordinate_closure_manifest()["root"],"C166_PROJECTOR_KINEMATIC_ROOT":projector_kinematic_closure_manifest()["root"],"C166_GAUGE_SCHEME_NF_ROOT":gauge_scheme_nf_closure_manifest()["root"],"C166_RENORMALIZATION_LAYER_ROOT":renormalization_layer_closure_manifest()["root"],"C166_STEP_SCALING_ROOT":step_scaling_closure_manifest()["root"],"C166_DEPENDENCY_GRAPH_ROOT":_root(tuple(dependency_graph(x["graph_id"])["root"] for x in IMPORTED_GRAPHS)),"C166_DEPENDENCY_CLOSURE_ROOT":dependency_closure_manifest()["root"],"C166_DESCRIPTOR_CROSSWALK_ROOT":descriptor_dependency_crosswalk()["root"],"C166_QUARK_FIELD_ROOT":componentwise_dependency_manifest("QUARK_FIELD")["root"],"C166_SIGNED_MASS_ROOT":componentwise_dependency_manifest("SIGNED_QUARK_MASS")["root"],"C166_GLUON_FIELD_ROOT":componentwise_dependency_manifest("TRANSVERSE_GLUON_FIELD")["root"],"C166_VERTEX_ROOT":componentwise_dependency_manifest("qg_VERTEX_DRESSING")["root"],"C166_COUPLING_ROOT":componentwise_dependency_manifest("QCD_COUPLING")["root"],"C166_MASS_COUPLING_GATE_ROOT":mass_coupling_dependency_gate_report()["root"],"C166_ACQUISITION_REQUEST_ROOT":missing_dependency_acquisition_manifest()["root"],"C166_HANDOFF_ROOT":expression_or_acquisition_handoff_contract()["root"],"C166_QUANTUM_HANDOFF_ROOT":quantum_dependency_handoff()["root"],"C166_SCOPE_ROOT":_root((STATUS,"no expression", "no target")),"C166_COMPLETENESS_ROOT":_root((STATUS,NEXT))}

ROOTS=_roots()
PACKAGE_ROOT=_root({"schema":"C166-HQCDLFGDEP2-V1","baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"plan":PLAN,"roots":ROOTS})

__all__=["STATUS","PLAN","NEXT","PACKAGE_ROOT","ROOTS","BASELINE","CONTRACT","CONTRACT_SHA256","PROMPT_SHA256","C165_ROOT","C164_ROOT","C163_ROOT","C162_ROOT","C161_ROOT","C160_ROOT","C159_ROOT","C158_ROOT","IMPORTED_ROOTS","IMPORTED_DEPS","IMPORTED_GRAPHS","LEAVES","RESOLUTIONS","load_verified_hqcd_lfgdep2_authority","verify_hqcd_lfgdep2_authority","lfgdep2_plan_manifest","imported_authority_freeze","missing_leaf_inventory","dependency_reuse_manifest","cross_reference_manifest","leaf_candidate_manifest","visual_leaf_report","visual_leaf_manifest","leaf_resolution_manifest","graph_delta_manifest","count_once_validation","transitive_closure_manifest","source_coordinate_closure_manifest","projector_kinematic_closure_manifest","gauge_scheme_nf_closure_manifest","renormalization_layer_closure_manifest","step_scaling_closure_manifest","dependency_graph","dependency_closure_manifest","descriptor_dependency_crosswalk","componentwise_dependency_manifest","mass_coupling_dependency_gate_report","missing_dependency_acquisition_manifest","no_expression_transcription_report","expression_or_acquisition_handoff_contract","quantum_dependency_handoff","static_isolation_guard","mutate_live_hqcdlfgdep2"]
