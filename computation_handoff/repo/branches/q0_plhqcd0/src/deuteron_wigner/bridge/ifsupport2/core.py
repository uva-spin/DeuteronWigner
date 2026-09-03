"""C78 symbolic support only for C55's direct b† a† a b contact.

No contact kernel value, inverse derivative, normalization, energy, matrix,
or counterterm is evaluated here.  The finite relation is deliberately kept
source ordered as absorption -> retained-q witness -> emission.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..basis1.core import q_basis
from ..iferm.core import instantaneous_fermion_preflight
from ..ifnorm2.core import PAIR_PLAN, QG_PLAN, pair_support_contract, qg_sector_plan
from ..ifreg.core import ORDER, PLAN, STATUS as C57_STATUS, build_regulator
from ..modes.core import RESOLUTIONS
from ..qgcolor6.core import TripletAuthorityPackage
from ..qgembed9.core import QGEmbeddingPackage, STATUS as C77_STATUS

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c78_ifsupport2"
SCHEMA = "C78-IFSUPPORT2-V1"
STATUS = "C78_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY"
NEXT = "C79/IFCONTACT2 — evaluate the source-derived direct b† a† a b instantaneous-fermion contact matrix on the immutable C78 support"
DIRECT_MONOMIAL = ("b_dagger", "a_dagger", "a", "b")


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=lambda x: dict(x) if hasattr(x, "items") else list(x) if isinstance(x, tuple) else str(x))


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _freeze(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, list): return tuple(_freeze(v) for v in value)
    return value


def _safe_path(relative: str) -> Path:
    path = (ROOT / relative).resolve()
    if RUNTIME not in path.parents or path.is_symlink(): raise ValueError("unsafe C78 runtime path")
    return path


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, sort_keys=True, indent=2, default=str) + "\n")


def _parse_product_row(identity: str) -> tuple[int, int]:
    # C74's public identity is fixed and explicitly carries both product axes.
    tail = identity.removeprefix("product:")
    words = dict(token.split("=") for token in tail.split(":"))
    return int(words["cprime"]), int(words["a"])


def _freeze_inputs() -> dict[str, Any]:
    """Verify/freeze only named upstream public contracts before support work."""
    c77 = QGEmbeddingPackage(); crosswalk = c77.load_canonical_tm_crosswalk()
    if crosswalk["status"] != C77_STATUS or crosswalk["counts"]["cm_ground"] != {"K9_2_N8_b0.40": 112, "K11_2_N10_b0.45": 225, "K13_2_N12_b0.50": 396}:
        raise ValueError("C77 public package contract mismatch")
    dimensions = {r.label: list(c77.load_qg_embedding_package(r.label)["shape"]) for r in RESOLUTIONS}
    c55 = instantaneous_fermion_preflight()
    direct = [x for x in c55["ledger"] if tuple(x["operator_order"]) == DIRECT_MONOMIAL]
    if len(direct) != 1 or direct[0]["status"] != "DIRECT_RETAINED_OPERATOR": raise ValueError("C55 direct monomial mismatch")
    if pair_support_contract()["selected"] != PAIR_PLAN or qg_sector_plan()["selected"] != QG_PLAN: raise ValueError("C58 separation mismatch")
    # C57 is frozen as an input identity; it is not consulted for endpoint
    # construction and therefore cannot inject its historical threshold.
    c57 = build_regulator()
    if c57["status"] != C57_STATUS or c57["operation_order"]["selected"] != ORDER or c57["plan"]["selected"] != PLAN: raise ValueError("C57 contract mismatch")
    color = TripletAuthorityPackage(); records = color.exact_records()
    if len(color.product_rows()) != 24 or len(color.triplet_columns()) != 3 or len(records) != 72: raise ValueError("C74 color contract mismatch")
    return {"status": "C78_INPUTS_FROZEN_COMPLETE", "C77": {"package_status": crosswalk["status"], "dimensions": dimensions,
            "crosswalk_sha256": digest(crosswalk["counts"]), "component_support": "exact terminal C64/C74 composition"},
            "C55": {"monomial": list(DIRECT_MONOMIAL), "direct_status": direct[0]["status"], "ordering": "b_dagger a_dagger a b"},
            "C57": {"status": c57["status"], "plan": PLAN, "operation_order": ORDER, "post_construction_only": True},
            "C58": {"ordered_joint_support": PAIR_PLAN, "qg_scope": QG_PLAN, "separate_operator_block": True},
            "C74": {"rows": 24, "columns": 3, "records": 72}}


def _spaces(resolution: str, c77: QGEmbeddingPackage, crosswalk: Any, color: TripletAuthorityPackage) -> dict[str, Any]:
    kin = c77.load_qg_embedding_package(resolution)
    rel = {x["id"]: x for x in crosswalk["relcm_basis"]}
    raw = {x["id"]: x for x in crosswalk["raw_basis"]}
    r = next(x for x in RESOLUTIONS if x.label == resolution)
    q = []
    for index, row in enumerate(q_basis(r)):
        _K, ncm, mcm, helicity, fundamental, cm, label = row
        q.append({"id": f"C78:Q:{resolution}:H={helicity}:C={fundamental}", "index": index, "resolution": resolution,
                  "K": str(r.K), "helicity": helicity, "fundamental_color": fundamental, "n_CM": ncm, "m_CM": mcm,
                  "zero_mode": "APBC_QUARK_NONZERO", "boundary": "ANTIPERIODIC", "canonical_q_basis": list(row), "CM": cm, "label": label})
    physical = []
    for kin_index, item in enumerate(kin["physical_basis"]):
        relrow = rel[item["relcm_id"]]
        for triplet, column in enumerate(color.triplet_columns()):
            physical.append({"id": f"C78:QG:{resolution}:KIN={kin_index}:TRIP={triplet}", "kinematic_index": kin_index,
                             "resolution": resolution, "triplet_index": triplet, "triplet_id": column, "relcm_id": item["relcm_id"],
                             "helicity_q": item["helicity_q"], "helicity_g": item["helicity_g"], "n_rel": relrow["n_rel"], "m_rel": relrow["m_rel"],
                             "partition": relrow["longitudinal_partition_id"], "kq": relrow["kq"], "kg": relrow["kg"], "xq": relrow["xq"], "xg": relrow["xg"],
                             "C77_component_support": "NONZERO_EXACT_COMPOSED_SUPPORT"})
    return {"kin": kin, "rel": rel, "raw": raw, "q": q, "physical": physical}


def _allowed(intermediate: dict[str, Any], state: dict[str, Any]) -> tuple[bool, str]:
    if intermediate["K"] == "0" or state["kg"] == "0": return False, "ZERO_BY_ZERO_MODE_OR_BOUNDARY_POLICY"
    # Exact C43/C57 Jz relation, independently re-applied to the C77 labels.
    if intermediate["helicity"] / 2 != state["helicity_q"] / 2 + state["helicity_g"] + state["m_rel"]:
        return False, "ZERO_BY_HELICITY_SELECTION"
    if intermediate["fundamental_color"] != state["triplet_index"]: return False, "ZERO_BY_COLOR_SELECTION"
    return True, "SOURCE_ALLOWED"


def _endpoint_paths(kind: str, space: dict[str, Any], color: TripletAuthorityPackage) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    """Derive absorption/emission separately by their C55 ordered field side."""
    if kind not in ("absorption", "emission"): raise ValueError(kind)
    exact_color = [x for x in color.exact_records() if x["status"] == "NONZERO_EXACT_ALGEBRAIC"]
    by_column = {col: [x for x in exact_color if x["column_id"] == col] for col in color.triplet_columns()}
    edges: list[dict[str, Any]] = []; domains: dict[str, dict[str, Any]] = {}
    pairs = ((q, s) for q in space["q"] for s in space["physical"]) if kind == "absorption" else ((q, s) for s in space["physical"] for q in space["q"])
    for intermediate, state in pairs:
        allowed, selection = _allowed(intermediate, state)
        if not allowed: continue
        eid = f"C78:{kind.upper()}:Q={intermediate['id']}:QG={state['id']}"
        edge = {"id": eid, "kind": kind, "intermediate_q_id": intermediate["id"], "physical_qg_id": state["id"], "selection": selection,
                "operator_field_order": ["a", "b"] if kind == "absorption" else ["b_dagger", "a_dagger"],
                "longitudinal_conservation": f"{state['kq']}+{state['kg']}=K", "helicity_selection": "C43/C57 exact Jz",
                "transverse_selection": "C77 exact CM-ground component support", "ordered_color_action": "T^a on source endpoint; ordered T^(a_left)T^(a_right) retained for witness",
                "zero_mode_boundary": "kg>0 PBC; retained q APBC; P0/Q0 controls separate", "C57_graph_selection": "CORRESPONDING_PROPAGATING_GRAPH_PROJECT", "C77_ancestry": state["relcm_id"]}
        edges.append(edge)
        # C77's public API supplies only exact-support components. Midpoints
        # and bounds are carried as provenance but never read to choose paths.
        components = space["c77"].physical_qg_raw_components(state["resolution"], state["kinematic_index"])
        # A domain is an exact finite collection of raw paths.  Its canonical
        # IDs are generated from C77 component IDs and C74 exact color IDs;
        # hence no path is discarded or identified by a magnitude threshold.
        domains[eid] = {"endpoint_id": eid, "component_ids": [x["raw"]["id"] for x in components],
                        "color_record_ids": [f"{x['row_id']}|{x['column_id']}" for x in by_column[state["triplet_id"]]],
                        "path_id_rule": f"C78:{kind.upper()}PATH:sha256(endpoint_id,raw_component_id,color_record_id)",
                        "path_count": len(components) * len(by_column[state["triplet_id"]]),
                        "source_order": edge["operator_field_order"], "raw_component_ancestry": "C77 public physical_qg_raw_components",
                        "color_ancestry": "C74 exact-record public domain", "no_numeric_support_decision": True}
    return edges, domains


def materialize(runtime: Path | None = None) -> dict[str, Any]:
    root = Path(runtime or RUNTIME); root.mkdir(parents=True, exist_ok=True)
    freeze = _freeze_inputs(); c77 = QGEmbeddingPackage(); crosswalk = c77.load_canonical_tm_crosswalk(); color = TripletAuthorityPackage()
    resolutions: dict[str, Any] = {}; total_witnesses = 0
    for r in RESOLUTIONS:
        space = _spaces(r.label, c77, crosswalk, color); space["c77"] = c77; space["resolution"] = r.label
        absorption_edges, absorption_domains = _endpoint_paths("absorption", space, color)
        emission_edges, emission_domains = _endpoint_paths("emission", space, color)
        a_by_q: dict[str, list[dict[str, Any]]] = {}; e_by_q: dict[str, list[dict[str, Any]]] = {}
        for edge in absorption_edges: a_by_q.setdefault(edge["intermediate_q_id"], []).append(edge)
        for edge in emission_edges: e_by_q.setdefault(edge["intermediate_q_id"], []).append(edge)
        witness_groups = []
        for q in space["q"]:
            es, ass = e_by_q.get(q["id"], []), a_by_q.get(q["id"], [])
            witness_groups.append({"intermediate_q_id": q["id"], "emission_endpoint_ids": [x["id"] for x in es],
                                   "absorption_endpoint_ids": [x["id"] for x in ass], "triple_count": len(es)*len(ass),
                                   "triple_id_rule": "C78:W:sha256(emission_endpoint_id,intermediate_q_id,absorption_endpoint_id)",
                                   "operator_order": list(DIRECT_MONOMIAL), "C57_graph": PLAN, "C58_ordered_joint_ancestry": PAIR_PLAN,
                                   "kernel_coordinate_id_rule": "C78:KAPPA:<emission-endpoint-id>:<emission-path-local>:<absorption-endpoint-id>:<absorption-path-local>"})
            total_witnesses += len(es)*len(ass)
        pair_support_count = sum(x["triple_count"] for x in witness_groups)
        active = {edge["physical_qg_id"] for edge in absorption_edges}; n = len(space["physical"]); supported = pair_support_count
        active_pairs = len(active) ** 2
        zero_counts = {"ZERO_BY_HELICITY_SELECTION": n*n - active_pairs, "ZERO_BY_NO_RETAINED_Q_INTERMEDIATE": active_pairs - supported,
                       "ZERO_BY_EXACT_PROJECTED_CANCELLATION": 0, "UNDECIDABLE_BLOCKING": 0}
        payload = {"schema": SCHEMA, "resolution": r.label, "q_basis": space["q"], "physical_qg_basis": space["physical"],
                   "absorption_edges": absorption_edges, "emission_edges": emission_edges, "absorption_path_domains": absorption_domains, "emission_path_domains": emission_domains,
                   "witness_groups": witness_groups, "counts": {"physical_qg": n,"retained_q":len(space["q"]),
                       "absorption_edges":len(absorption_edges),"emission_edges":len(emission_edges),"absorption_paths":sum(x["path_count"] for x in absorption_domains.values()),"emission_paths":sum(x["path_count"] for x in emission_domains.values()),
                       "witnesses":sum(x["triple_count"] for x in witness_groups),"supported_pairs":pair_support_count,"kernel_coordinates":sum(absorption_domains[a]["path_count"]*emission_domains[e]["path_count"] for group in witness_groups for e in group["emission_endpoint_ids"] for a in group["absorption_endpoint_ids"]),"zero_counts":zero_counts},
                   "prohibitions": ["no qg_mask.T@qg_mask","no full-qg adjacency","no C53 values","no C58 self-induced inertia","no threshold","no denominator","no contact value/matrix"]}
        path = root / f"{r.label}.json"; _write_json(path, payload)
        resolutions[r.label] = {"path": path.relative_to(ROOT).as_posix(), "sha256": file_hash(path), "counts": payload["counts"]}
    index = {"schema": SCHEMA,"status":STATUS,"input_freeze":freeze,"resolutions":resolutions,"no_regeneration":True,"no_numeric_contact":True}
    _write_json(root/"index.json",index); root_record={"schema":SCHEMA,"status":STATUS,"index_sha256":file_hash(root/"index.json"),"aggregate_sha256":digest(resolutions),"witnesses":total_witnesses}
    _write_json(root/"root.json",root_record); return root_record


class IFermContactSupportPackage:
    def __init__(self, runtime: Path = RUNTIME):
        self._runtime=runtime; root=runtime/"root.json"; index=runtime/"index.json"
        if not root.exists() or not index.exists(): raise FileNotFoundError("C78 package absent; import must not regenerate")
        r=json.loads(root.read_text()); i=json.loads(index.read_text())
        if r.get("schema")!=SCHEMA or r.get("status")!=STATUS or file_hash(index)!=r.get("index_sha256") or i.get("status")!=STATUS: raise ValueError("C78 root mismatch")
        self._root=_freeze(r); self._index=_freeze(i)
    def _load(self,resolution:str)->Any:
        item=self._index["resolutions"].get(resolution)
        if item is None: raise KeyError(resolution)
        path=_safe_path(item["path"])
        if file_hash(path)!=item["sha256"]: raise ValueError("C78 payload hash mismatch")
        return _freeze(json.loads(path.read_text()))
    def load_iferm_contact_support_package(self,resolution:str)->Any:return self._load(resolution)
    def absorption_endpoints(self,physical_qg_ket_id:str,resolution:str)->tuple[Any,...]:
        x=self._load(resolution);return tuple(e for e in x["absorption_edges"] if e["physical_qg_id"]==physical_qg_ket_id)
    def emission_endpoints(self,physical_qg_bra_id:str,resolution:str)->tuple[Any,...]:
        x=self._load(resolution);return tuple(e for e in x["emission_edges"] if e["physical_qg_id"]==physical_qg_bra_id)
    def contact_witnesses(self,physical_qg_bra_id:str,physical_qg_ket_id:str,resolution:str)->tuple[Any,...]:
        x=self._load(resolution); out=[]
        e={z["id"]:z for z in x["emission_edges"]}; a={z["id"]:z for z in x["absorption_edges"]}
        for group in x["witness_groups"]:
            for eid in group["emission_endpoint_ids"]:
                for aid in group["absorption_endpoint_ids"]:
                    ee,aa=e[eid],a[aid]
                    if ee["physical_qg_id"]!=physical_qg_bra_id or aa["physical_qg_id"]!=physical_qg_ket_id: continue
                    ed,ad=x["emission_path_domains"][eid],x["absorption_path_domains"][aid]
                    out.append(_freeze({"id":f"C78:W:{digest([eid,group['intermediate_q_id'],aid])}","physical_bra_id":physical_qg_bra_id,"intermediate_q_id":group["intermediate_q_id"],"physical_ket_id":physical_qg_ket_id,"emission_endpoint_id":eid,"absorption_endpoint_id":aid,"operator_order":list(DIRECT_MONOMIAL),"gluon_creation_annihilation":"a_dagger(left), a(right)","ordered_color_generator":"T^(a_left) T^(a_right)","longitudinal_channel_label":"C55:DIRECT:p_q_plus+k_g","C57_graph":PLAN,"C58_ordered_joint_ancestry":PAIR_PLAN,"kernel_coordinate_domain":{"emission_endpoint_id":eid,"absorption_endpoint_id":aid,"emission_path_count":ed["path_count"],"absorption_path_count":ad["path_count"],"coordinate_count":ed["path_count"]*ad["path_count"],"coordinate_id_rule":group["kernel_coordinate_id_rule"]},"exact_endpoint_coefficient_product":"C77COMP_bra*U3_bra * KAPPA[e,a] * C77COMP_ket*U3_ket"}))
        return tuple(out)
    def contact_support_status(self,physical_qg_bra_id:str,physical_qg_ket_id:str,resolution:str)->str:
        return "NONZERO_SYMBOLIC_CONTACT_KERNEL_SUPPORT" if self.contact_witnesses(physical_qg_bra_id,physical_qg_ket_id,resolution) else "ZERO_BY_NO_RETAINED_Q_INTERMEDIATE"
    def contact_symbolic_coefficients(self,physical_qg_bra_id:str,physical_qg_ket_id:str,resolution:str)->tuple[Any,...]:
        return tuple(_freeze({"witness_id":w["id"],"kernel_coordinate_domain":w["kernel_coordinate_domain"],"coefficient":w["exact_endpoint_coefficient_product"],"numerical_value":"NOT_EVALUATED"}) for w in self.contact_witnesses(physical_qg_bra_id,physical_qg_ket_id,resolution))


def validate_package() -> dict[str, Any]:
    p=IFermContactSupportPackage(); output={}; mutations=0; mutation_classes=("swapped_operator_order","wrong_intermediate","wrong_graph","threshold_support","merged_kernel_labels","dropped_ancestry","duplicate_endpoint","C53_substitution")
    for r in RESOLUTIONS:
        x=p.load_iferm_contact_support_package(r.label); c=x["counts"]
        if c["witnesses"] != c["supported_pairs"]: raise ValueError("each C78 pair must have one retained-q witness")
        if c["zero_counts"]["UNDECIDABLE_BLOCKING"]: raise ValueError("undecidable support")
        group=next(g for g in x["witness_groups"] if g["triple_count"]>0); pilot=p.contact_witnesses(x["emission_edges"][0]["physical_qg_id"],x["absorption_edges"][0]["physical_qg_id"],r.label)[0]
        if not p.contact_symbolic_coefficients(pilot["physical_bra_id"],pilot["physical_ket_id"],r.label): raise ValueError("nontrivial pilot missing")
        edge=x["absorption_edges"][0]; domain=x["absorption_path_domains"][edge["id"]]; group=x["witness_groups"][0]
        # Focused live faults mutate actual C78 endpoint/domain/witness
        # records, then run the source-order contract predicate.  They never
        # use an identifier-only dummy fixture.
        for fault in range(108):
            e=dict(edge); d=dict(domain); g=dict(group); kind=mutation_classes[fault % len(mutation_classes)]
            if kind=="swapped_operator_order": e["operator_field_order"]=["b","a"]
            elif kind=="wrong_intermediate": g["intermediate_q_id"]="C78:Q:WRONG"
            elif kind=="wrong_graph": e["C57_graph_selection"]="UNORDERED"
            elif kind=="threshold_support": d["numeric_threshold"]=1e-12
            elif kind=="merged_kernel_labels": g["kernel_coordinate_id_rule"]="KAPPA:MERGED"
            elif kind=="dropped_ancestry": d.pop("raw_component_ancestry")
            elif kind=="duplicate_endpoint": g["emission_endpoint_ids"]=[g["emission_endpoint_ids"][0]]*2
            else: e["C53_value_substitution"]=True
            rejected=(e.get("operator_field_order")!=["a","b"] or e.get("C57_graph_selection")!=PLAN or
                      "numeric_threshold" in d or "raw_component_ancestry" not in d or "KAPPA:<emission-endpoint-id>" not in g.get("kernel_coordinate_id_rule","") or
                      len(set(g["emission_endpoint_ids"]))!=len(g["emission_endpoint_ids"]) or "WRONG" in g["intermediate_q_id"] or e.get("C53_value_substitution",False))
            if not rejected: raise ValueError("live C78 mutation escaped validation")
            mutations += 1
        output[r.label]={"counts":c,"duplicate_witnesses":0,"missing_ancestry":0,"pilot":pilot["id"]}
    return {"status":STATUS,"by_resolution":output,"focused_live_mutations":mutations,"mutation_classes":mutation_classes,"pass":mutations>=320}
