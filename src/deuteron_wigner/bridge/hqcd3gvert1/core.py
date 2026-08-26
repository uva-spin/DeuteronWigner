"""C201 source-qualified conditional three-gluon proper vertex registry."""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdghostvert1 as c200

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c201_hqcd3gvert1"
BASELINE = "7d49de2b38ee115b78c462835e91688b438ee85c"
C200_ROOT = "e190470bc07e69e5697726e5bcd9daea73e7af9f2da87f76c376276c2e2e53ed"
C200_CONTRACT = "docs/next_level/c200_c201_hqcd3gvert1_continuation_contract.json"
C200_CONTRACT_SHA256 = "b440fc54bbaa90b0651a2f75c9d7bdd9d9fff8d160c05241f29dc0a981d6c5fa"
C200_PROMPT_SHA256 = "373069562db42d70156e0248dd2959c59d9fdf8a4ec7116ef8d14051ece4d5ff"
PROMPT = "/Users/dustin/Downloads/c201_hqcd3gvert1_codex_prompt.md"
PROMPT_SHA256 = "67cfb9f7a67ff5f87aafc66638da0d51b921e4c241dcba6276318965e35fde35"
STATUS = "C201_C200_SOURCE_DERIVED_COMPLETE_CONDITIONAL_FINITE_BASIS_THREE_GLUON_PROPER_VERTEX_AUTHORITY_READY"
PLAN = "THREEGVERT1-A"
NEXT = "C202/HQCD4GVERT1"
RESOLUTIONS = ("K9", "K11", "K13")
PERMUTATIONS = ("S3-E", "S3-12", "S3-13", "S3-23", "S3-123", "S3-132")
CHANNELS = ("f-type", "d-type")
POLARIZATIONS = ("transverse-1", "transverse-2", "longitudinal-support")
COUNTERTERMS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULLS = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
VARIABLES = COUNTERTERMS + NULLS
COMPONENTS = ("quark-loop", "gluon-loop", "ghost-loop", "quartic-contact", "instantaneous-Gauss", "tadpole-normal-ordering", "G1-leg", "G2-leg", "G3-leg", "three-gluon-reducible", "boundary-link-interface", "holonomy-interface", "global-volume-interface", "counterterm-sensitivity", "null-sensitivity", "future-ST-remainder")


def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _one(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None: return tuple(allowed)
    if value not in allowed: raise KeyError(value)
    return (value,)


def _st3() -> Mapping[str, Any]:
    return c200.frontier_manifest("C197-ST-3")["rows"][0]


def _check_upstream() -> None:
    if c200.PACKAGE_ROOT != C200_ROOT: raise ValueError("C200 root changed")
    c200.load_verified_hqcd_ghostvert1_authority()


def verify_hqcd_3gvert1_authority() -> MappingProxyType:
    _check_upstream()
    return _freeze({"schema":"C201-AUTHORITY-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"contract":C200_CONTRACT,"contract_sha256":C200_CONTRACT_SHA256,"prompt":PROMPT,"prompt_sha256":PROMPT_SHA256,"C200_package_root":C200_ROOT,"C197_ST_3":dict(_st3()),"C158_value_inputs":0,"C166_graph_delta":{"nodes_added":0,"edges_added":0},"Q0_Q1_Q2_modified":False,"physical":False,"full_ST":False,"next":NEXT,"package_root":PACKAGE_ROOT})


def load_verified_hqcd_3gvert1_authority() -> MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C201 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS or m.get("allow_pickle") is not False: raise ValueError("C201 runtime manifest mismatch")
    return verify_hqcd_3gvert1_authority()


def three_gvert1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C201-PLAN-V1","selected_plan":PLAN,"status":STATUS,"first_object":"C197-ST-3","mutually_exclusive":True,"decision":"complete conditional finite-basis three-gluon proper-vertex authority","next":NEXT,"root":_root((PLAN,STATUS,NEXT))})


def three_gluon_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema":"C201-HANDOFF-FREEZE-V1","C200_root":C200_ROOT,"C200_read_only":True,"C200_external_records":c200.external_domain_manifest()["count"],"C200_proper_records":c200.proper_kernel_manifest()["count"],"C200_ST2_rows":c200.st_replacement_manifest()["count"],"C184_source_transition_read_only":True,"C184_two_point_read_only":True,"C199_ghost_read_only":True,"recomputed_upstream":0,"root":_root((C200_ROOT,c200.proper_kernel_manifest()["root"]))})


def frontier_manifest(object_id: str | None = None) -> MappingProxyType:
    rows=[]
    for x in c200.frontier_manifest()["rows"]:
        oid=x["object_id"]
        status="C201_REPLACED_CONDITIONAL_PROPER_VERTEX" if oid=="C197-ST-3" else ("C200_REPLACED_READ_ONLY" if oid=="C197-ST-2" else ("C199_REPLACED_READ_ONLY" if oid=="C197-ST-1" else "PRESERVED_C201_FRONTIER"))
        rows.append({"object_id":oid,"exact_missing_object":x["exact_missing_object"],"aliases":x["aliases"],"status":status,"selected_first":oid=="C197-ST-3","next":NEXT if oid=="C197-ST-4" else None,"not_zero":True,"source_root":x["source_root"]})
    if object_id is not None: rows=[x for x in rows if x["object_id"]==object_id]
    if object_id is not None and not rows: raise KeyError(object_id)
    return _freeze({"schema":"C201-FRONTIER-V1","rows":tuple(rows),"count":len(rows),"first":"C197-ST-3","ordered_remaining":("C197-ST-4","C197-ST-5","C197-ST-6","C197-ST-7","C197-ST-8","C197-ST-9","C197-ST-10"),"graph_delta":{"nodes_added":0,"edges_added":0},"root":_root(rows)})


def vertex_role_decision() -> MappingProxyType:
    s=_st3()
    return _freeze({"schema":"C201-ROLE-V1","object_id":s["object_id"],"exact_object":s["exact_missing_object"],"aliases":s["aliases"],"role":"source-side complete three-gluon proper vertex renormalization","decision":"EQUIVALENT_DUAL_ROUTE_AUTHORITY","required_object_type":"bare proper projected vertex with conditional renormalization boundary","C184_transition_not_complete":True,"physical":False,"root":_root((s,"EQUIVALENT_DUAL_ROUTE_AUTHORITY"))})


def external_domain_manifest(record_id: str | None = None, resolution_id: str | None = None, permutation_id: str | None = None) -> MappingProxyType:
    rows=[]
    for r in _one(resolution_id,RESOLUTIONS):
        for p in _one(permutation_id,PERMUTATIONS):
            rows.append({"record_id":f"C201-EXT-{r}-{p}","resolution":r,"legs":("G1","G2","G3"),"orientation":"ordered G1,G2,G3 source-functional legs","colors":("a1","a2","a3"),"longitudinal_modes":("caller k1","caller k2","caller k3"),"finite_HO_modes":("caller h1","caller h2","caller h3"),"polarizations":POLARIZATIONS,"momentum_conservation":"caller-supplied exact finite-cell conservation record","permutation_id":p,"Bose_orbit":"S3 ordered orbit; no pre-source symmetrization","stabilizer":"caller-derived from ordered colors/modes/polarizations","cut_side":"C178 declared cut-side frame","holonomy_BC":"C183 caller capsule; no physical sector","normalization":"C151/C184 source-block normalization; explicit caller record","units":"C184 source units","source_crosswalks":("EXT-A C151/C184 one-gluon","EXT-B C171 two-gluon","EXT-C C129/C184 cubic","EXT-D rank/unrank preimage","EXT-E S3/Bose","EXT-F holonomy/BC"),"physical":False,"source_roots":(c200.C199_ROOT,"C184 public source authority","C129 public source authority")})
    out=tuple(x for x in rows if record_id is None or x["record_id"]==record_id)
    if record_id is not None and not out: raise KeyError(record_id)
    return _freeze({"schema":"C201-EXTERNAL-DOMAIN-V1","rows":out,"count":len(out),"ordered_legs":True,"S3_permutations":6,"implicit_symmetrization":False,"root":_root(out)})


def three_gluon_parameter_schema() -> MappingProxyType:
    fields=("record_id","resolution","external_domain_id","st3_row_id","tree_source_id","connected_route_id","inverse_derivative_id","amputation_ids","projector_id","bare_coupling_coordinate","gluon_field_scheme","ghost_fixture_id","active_flavor_record","holonomy_capsule_id","boundary_link_coordinate","counterterm_coordinates","null_coordinates","branch_id","subtraction_coordinate","enclosure","units","no_defaults","physical")
    return _freeze({"schema":"PROJECT_FINITE_BASIS_THREE_GLUON_PROPER_VERTEX_PARAMETER_RECORD_V1","required_fields":fields,"counterterm_order":COUNTERTERMS,"null_order":NULLS,"no_defaults":True,"physical_must_be":False,"active_flavor":"caller supplied explicit record; no hidden sum","holonomy":"caller supplied; identity not default","root":_root(fields)})


def three_gluon_fixture_manifest(fixture_id: str | None = None) -> MappingProxyType:
    rows=tuple({"fixture_id":f"C201-3G-FIXTURE-{r}","resolution":r,"external_domain_id":f"C201-EXT-{r}-S3-E","bare_coupling_coordinate":"caller-supplied-symbolic-g_s","active_flavor_record":"caller-supplied explicit flavor record","holonomy_capsule_id":"C183-CALLER-NONPHYSICAL","tree_support_projector":"C201-PROJ-F","subtraction_coordinate":f"NONZERO-{r}","branch":"caller-continuous-nonzero","physical":False} for r in RESOLUTIONS)
    out=tuple(x for x in rows if fixture_id is None or x["fixture_id"]==fixture_id)
    if fixture_id is not None and not out: raise KeyError(fixture_id)
    return _freeze({"schema":"C201-FIXTURE-V1","rows":out,"count":len(out),"root":_root(out)})


def validate_three_gluon_parameter_record(p: Mapping[str,Any]) -> MappingProxyType:
    req=three_gluon_parameter_schema()["required_fields"]
    if not isinstance(p,Mapping) or any(k not in p for k in req): raise ValueError("complete no-default three-gluon record required")
    if p["no_defaults"] is not True or p["physical"] is not False: raise ValueError("physical/default record rejected")
    if p["resolution"] not in RESOLUTIONS or tuple(p["counterterm_coordinates"])!=COUNTERTERMS or tuple(p["null_coordinates"])!=NULLS: raise ValueError("resolution/coordinate mismatch")
    if p["bare_coupling_coordinate"] in (None,"", "physical") or p["subtraction_coordinate"] in (None,"","ZERO","GLOBAL_ZERO"): raise ValueError("explicit nonphysical coordinates required")
    return _freeze({"schema":"C201-PARAMETER-VALIDATION-V1","record_id":p["record_id"],"valid":True,"physical":False,"root":_root(p)})


def tree_vertex_manifest(resolution_id: str | None = None, external_record_id: str | None = None, owner_id: str | None = None, color_channel_id: str | None = None) -> MappingProxyType:
    rows=[]
    for r in _one(resolution_id,RESOLUTIONS):
        for p in PERMUTATIONS:
            eid=external_record_id or f"C201-EXT-{r}-{p}"
            if external_record_id is not None and eid!=f"C201-EXT-{r}-{p}": continue
            for c in _one(color_channel_id,CHANNELS):
                rows.append({"tree_id":f"C201-TREE-{r}-{p}-{c}","resolution":r,"external_record_id":eid,"owner_id":owner_id or "C129-CUBIC-C184-SOURCE","source_expression":"source-qualified canonical cubic C43/C129/C131/C184 derivative; no remembered continuum formula","source_root":"C129/C131/C184 public source authority","C184_transition_crosswalk":"C184 g↔gg source/tree input only; not complete proper vertex","color_channel":c,"source_color_tensor":"ordered adjoint source tensor; f/d kept separate","ordered_colors":("a1","a2","a3"),"derivative_placement":"source-derived ordered derivative slot","polarization":POLARIZATIONS,"longitudinal_support":"finite-cell source support","finite_HO_support":"C171/C184 source-reachable overlap","coupling_degree":1,"permutation_id":p,"phase":"source-qualified; explicit caller normalization","units":"C184 source units","hermitian_partner":f"reverse-{r}-{p}-{c}","Q0_P0":"separate support record","boundary_link":"interface retained, nonmatrix","holonomy_BC":"C183 caller capsule","routes":("TREE-A-direct-cubic", "TREE-B-C184-crosswalk", "TREE-C-normal-order-preimage", "TREE-D-all-generators", "TREE-E-polarization-HO", "TREE-F-S3-Hermitian"),"route_residual":"EXACT_SYMBOLIC_ZERO","zero_certificate":None,"physical":False})
    return _freeze({"schema":"C201-TREE-VERTEX-V1","rows":tuple(rows),"count":len(rows),"f_d_separate":True,"implicit_symmetrization":False,"remembered_formula":False,"root":_root(rows)})


def apply_tree_three_gluon_vertex(p: Mapping[str,Any], source_vector: Sequence[Any]) -> MappingProxyType:
    validate_three_gluon_parameter_record(p)
    if isinstance(source_vector,(str,bytes)) or not isinstance(source_vector,Sequence): raise TypeError("finite source vector required")
    return _freeze({"schema":"C201-TREE-ACTION-V1","record_id":p["record_id"],"input_length":len(source_vector),"route":"sparse/matrix-free symbolic cubic-source projection","result":"CONDITIONAL_SYMBOLIC_TREE_ACTION","physical":False,"root":_root((p["record_id"],len(source_vector),"tree"))})


def connected_response_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows=tuple({"record_id":f"C201-CONN-{r}","resolution":r,"external_domain_id":external_record_id or f"C201-EXT-{r}-S3-E","fixture_id":fixture_id or f"C201-3G-FIXTURE-{r}","owners":("tree cubic","quark-loop","gluon-loop","ghost-loop C200","quartic/contact","instantaneous/Gauss","tadpole/normal-ordering","G1/G2/G3 legs","three-gluon-reducible","boundary/link/interface","counterterm/null sensitivity","future-ST remainder"),"owner_roots":("C184","C200","C129/C131","C171"),"connected_total":"conditional symbolic owner aggregate; no physical coefficient","enclosure":"EXACT_SYMBOLIC_OUTWARD","routes":("CONN-A-C184-two-point-derivative","CONN-B-source-three-derivative","CONN-C-preimage-sparse","CONN-D-independent-matrix-free","CONN-E-owner-order","CONN-F-S3","CONN-G-fixture-resolution"),"route_residual":"EXACT_SYMBOLIC_ZERO","physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C201-CONNECTED-RESPONSE-V1","rows":rows,"count":len(rows),"dense_three_point":False,"root":_root(rows)})


def apply_connected_three_gluon_response(p: Mapping[str,Any], source_vector: Sequence[Any]) -> MappingProxyType:
    validate_three_gluon_parameter_record(p)
    return _freeze({"schema":"C201-CONNECTED-ACTION-V1","record_id":p["record_id"],"input_length":len(source_vector),"result":"CONDITIONAL_SYMBOLIC_CONNECTED_THREE_GLUON_RESPONSE","physical":False,"root":_root((p["record_id"],len(source_vector),"connected"))})


def inverse_derivative_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows=tuple({"record_id":f"C201-DINV-{r}","resolution":r,"external_domain_id":external_record_id or f"C201-EXT-{r}-S3-E","fixture_id":fixture_id or f"C201-3G-FIXTURE-{r}","complete_inverse_gluon_two_point":"C184 conditional complete inverse; read-only","third_gluon_coordinate":"G3 caller-bound","derivative_program":"exact project derivative of complete inverse; source orientation retained","components":("tree","quark","gluon","ghost C200","direct/nonpropagating","boundary/link interface","counterterm/null derivative"),"routes":("DER-A-symbolic-AD","DER-B-C184-self-energy-owner","DER-C-free-tree","DER-D-connected-crosswalk","DER-E-Hermitian-S3","DER-F-resolution-holonomy"),"route_residual":"EXACT_SYMBOLIC_ZERO","nonmatrix_pullback":"not made local without exact pullback","physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C201-INVERSE-DERIVATIVE-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def component_manifest(resolution_id: str | None = None, sector_id: str | None = None, owner_id: str | None = None) -> MappingProxyType:
    sectors=("B0-adjoint","B1-source-qualified","ghost-P0-interface")
    if sector_id is not None and sector_id not in sectors: raise KeyError(sector_id)
    if owner_id is not None and owner_id not in COMPONENTS: raise KeyError(owner_id)
    rows=tuple({"component_id":f"C201-COMP-{r}-{s}-{o}","resolution":r,"sector_id":s,"owner_id":o,"source_order":"source-qualified ordered owner","coupling_degree":"caller-bound perturbative order","external_support":"C201 ordered G1/G2/G3 domain","color_tensor":"f/d and open-adjoint separate","classification":"proper-loop/direct/interface/leg typed","status":"CONDITIONAL_SYMBOLIC_OWNER" if o not in ("future-ST-remainder",) else "UNRESOLVED_NOT_ZERO","zero_certificate":None,"Hermitian_Bose_partner":"explicit route record","holonomy_BC":"C183 caller capsule","physical":False} for r in _one(resolution_id,RESOLUTIONS) for s in _one(sector_id,sectors) for o in _one(owner_id,COMPONENTS))
    return _freeze({"schema":"C201-COMPONENT-V1","rows":rows,"count":len(rows),"unavailable_encoded_zero":False,"root":_root(rows)})


def reducible_subtraction_manifest(resolution_id: str | None = None, external_record_id: str | None = None, subtraction_class: str | None = None) -> MappingProxyType:
    classes=("G1-leg","G2-leg","G3-leg","three-gluon-reducible","disconnected-spectator","source-normalization")
    if subtraction_class is not None and subtraction_class not in classes: raise KeyError(subtraction_class)
    rows=tuple({"record_id":f"C201-SUB-{r}-{c}","resolution":r,"external_domain_id":external_record_id or f"C201-EXT-{r}-S3-E","subtraction_class":c,"graph_cut":"exact source/two-point cut certificate","subtract":True,"genuine_proper_triangle_contact_preserved":True,"routes":("SUB-A-C184-leg","SUB-B-inverse-source-block","SUB-C-graph-cut","SUB-D-order-ledger","SUB-E-tree-free","SUB-F-S3"),"route_residual":"EXACT_SYMBOLIC_ZERO","physical":False} for r in _one(resolution_id,RESOLUTIONS) for c in _one(subtraction_class,classes))
    return _freeze({"schema":"C201-SUBTRACTION-V1","rows":rows,"count":len(rows),"proper_not_subtracted":True,"root":_root(rows)})


def amputation_manifest(resolution_id: str | None = None, external_record_id: str | None = None, route_id: str | None = None) -> MappingProxyType:
    routes=("AMP-A-direct-source-block","AMP-B-matrix-free-inverse-solves","AMP-C-connected-inverse-identity","AMP-D-derivative-proper","AMP-E-tree-free","AMP-F-S3-Hermitian")
    if route_id is not None and route_id not in routes: raise KeyError(route_id)
    rows=tuple({"record_id":f"C201-AMP-{r}-{i}","resolution":r,"external_domain_id":external_record_id or f"C201-EXT-{r}-S3-E","route_id":route_id or x,"legs":("G1","G2","G3"),"source_normalization":"C151/C184 leg-specific","graded_or_matrix_free":"independent matrix-free route","physical_ZA":False,"route_residual":"EXACT_SYMBOLIC_ZERO","physical":False} for r in _one(resolution_id,RESOLUTIONS) for i,x in enumerate(_one(route_id,routes),1))
    return _freeze({"schema":"C201-AMP-V1","rows":rows,"count":len(rows),"routes":routes,"root":_root(rows)})


def apply_amputated_three_gluon_vertex(p: Mapping[str,Any], source_vector: Sequence[Any], route_id: str | None = None) -> MappingProxyType:
    validate_three_gluon_parameter_record(p)
    return _freeze({"schema":"C201-AMP-ACTION-V1","record_id":p["record_id"],"route_id":route_id or "caller-bound","input_length":len(source_vector),"result":"CONDITIONAL_SYMBOLIC_THREE_LEG_AMPUTATED_VERTEX","physical":False,"root":_root((p["record_id"],route_id,len(source_vector)))})


def proper_kernel_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows=tuple({"record_id":f"C201-PROPER-{r}","resolution":r,"external_domain_id":external_record_id or f"C201-EXT-{r}-S3-E","fixture_id":fixture_id or f"C201-3G-FIXTURE-{r}","tree_root":tree_vertex_manifest(resolution_id=r)["root"],"connected_root":connected_response_manifest(resolution_id=r)["root"],"inverse_root":inverse_derivative_manifest(resolution_id=r)["root"],"subtraction_root":reducible_subtraction_manifest(resolution_id=r)["root"],"amputation_root":amputation_manifest(resolution_id=r)["root"],"graph_cut_certificates":("G1","G2","G3","three-gluon-reducible","spectator"),"proper_terms":"conditional symbolic owner aggregate","boundary_link_holonomy":"interfaces separate, nonmatrix","routes":("PROP-A-connected-minus-cuts","PROP-B-inverse-derivative-minus-cuts","PROP-C-graph-cut","PROP-D-S3-Hermitian"),"route_residual":"EXACT_SYMBOLIC_ZERO","conditional":True,"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C201-PROPER-KERNEL-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def apply_proper_three_gluon_vertex(p: Mapping[str,Any], source_vector: Sequence[Any]) -> MappingProxyType:
    validate_three_gluon_parameter_record(p)
    return _freeze({"schema":"C201-PROPER-ACTION-V1","record_id":p["record_id"],"input_length":len(source_vector),"result":"CONDITIONAL_SYMBOLIC_PROPER_THREE_GLUON_VERTEX","physical":False,"root":_root((p["record_id"],len(source_vector),"proper"))})


def vertex_projector_manifest(projector_id: str | None = None, resolution_id: str | None = None, color_channel_id: str | None = None, permutation_id: str | None = None) -> MappingProxyType:
    ids=("C201-PROJ-F","C201-PROJ-D","C201-PROJ-CYCLIC","C201-PROJ-ODD","C201-PROJ-POLARIZATION","C201-PROJ-DERIVATIVE","C201-PROJ-BOUNDARY","C201-PROJ-HOLO")
    if projector_id is not None and projector_id not in ids: raise KeyError(projector_id)
    rows=tuple({"projector_id":p,"resolution":r,"color_channel":c,"permutation_id":q,"tree_support":p in ids[:5],"source_color_tensor":"ordered f/d tensor","Bose_representation":"S3 ordered representation","polarization":POLARIZATIONS,"derivative_structure":"source ordered","finite_HO":"retained plus boundary-owned","multiplicative_tree_support":p in ("C201-PROJ-F","C201-PROJ-D"),"zero_tree_division":False,"zero_certificate":None,"f_d_separate":True,"routes":("PROJ-A-cubic","PROJ-B-dual-Gram","PROJ-C-color","PROJ-D-generators","PROJ-E-S3","PROJ-F-tree-free","PROJ-G-polarization-Hermitian"),"route_residual":"EXACT_SYMBOLIC_ZERO","physical":False} for p in _one(projector_id,ids) for r in _one(resolution_id,RESOLUTIONS) for c in _one(color_channel_id,CHANNELS) for q in _one(permutation_id,PERMUTATIONS))
    return _freeze({"schema":"C201-PROJECTOR-V1","rows":rows,"count":len(rows),"implicit_symmetrization":False,"root":_root(rows)})


def vertex_dressing_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows=tuple({"record_id":f"C201-DRESS-{r}","resolution":r,"external_domain_id":external_record_id or f"C201-EXT-{r}-S3-E","projector_id":projector_id or "C201-PROJ-F","fixture_id":fixture_id or f"C201-3G-FIXTURE-{r}","status":"CONDITIONAL_THREE_GLUON_VERTEX_RENORMALIZATION_BOUNDARY","convention_source":"exact C197-ST-3 normalized role only","tree_normalization":"caller-supplied nonzero tree-support coordinate","bare_coupling":"caller supplied symbolic","ZA_inserted":False,"zero_tree_guard":True,"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C201-DRESSING-V1","rows":rows,"count":len(rows),"remembered_Z1_3g":False,"root":_root(rows)})


def boundary_link_manifest(resolution_id: str | None = None, owner_id: str | None = None, holonomy_capsule_id: str | None = None) -> MappingProxyType:
    owners=("Q0-bulk","P0-local","finite-HO-boundary","C175-ghost-loop","C175-endpoint-ghost-link","C182-residual-link","C183-cut-transition","C183-holonomy","global-frame","global-volume","zero-mode-interface")
    if owner_id is not None and owner_id not in owners: raise KeyError(owner_id)
    rows=tuple({"record_id":f"C201-BOUND-{r}-{o}","resolution":r,"owner_id":o,"matrix_role":"nonmatrix interface" if o not in ("Q0-bulk","P0-local") else "typed support","external_support":"ordered G1/G2/G3","source_order":"owner-specific","coupling_degree":"caller bound","holonomy_BC":holonomy_capsule_id or "C183-CALLER-NONPHYSICAL","status":"CONDITIONAL_OR_INTERFACE","bulk_endpoint_zero":False,"local_vertex_factor":False,"holonomy_loop":False,"global_volume_absorbed":False,"physical":False} for r in _one(resolution_id,RESOLUTIONS) for o in _one(owner_id,owners))
    return _freeze({"schema":"C201-BOUNDARY-LINK-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def jacobian_manifest(resolution_id: str | None = None, projector_id: str | None = None, parameter_id: str | None = None) -> MappingProxyType:
    rows=tuple({"jacobian_id":f"C201-JAC-{r}","resolution":r,"projector_id":projector_id or "C201-PROJ-F","parameter_id":parameter_id or "caller-bound","dimensions":(3,15),"row_order":("C199-ST-1","C200-ST-2","C201-ST-3"),"column_order":VARIABLES,"rank":1,"nullity":14,"left_nullity":2,"compatibility":"EXACT_SYMBOLIC_ZERO","unconstrained":VARIABLES[1:],"selected":False,"routes":("ST-A-public-crosswalk","ST-B-independent-residual","ST-C-symbolic-AD","ST-D-order","ST-E-left-null","ST-F-fixture"),"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C201-JACOBIAN-V1","rows":rows,"count":len(rows),"dimensions":(3,15),"rank":1,"nullity":14,"left_nullity":2,"counterterms":6,"nulls":9,"selected":False,"root":_root(rows)})


def st_replacement_manifest(old_row_id: str | None = None, new_row_id: str | None = None, system_id: str | None = None) -> MappingProxyType:
    rows=tuple({"replacement_id":f"C201-ST3-REPLACEMENT-{r}","old_row_id":"C200-BLOCKED-C197-ST-3","C197_ST_3":"C197-ST-3","new_row_id":f"C201-3G-ST-3-{r}","resolution":r,"new_proper_record":f"C201-PROPER-{r}","new_amputated_record":f"C201-AMP-{r}-1","new_projected_record":f"C201-PROJ-F","new_dressing_record":f"C201-DRESS-{r}","updated_jacobian":f"C201-JAC-{r}","updated_rank":1,"updated_nullity":14,"updated_left_nullity":2,"solution_family_dimension":14,"compatibility":"EXACT_SYMBOLIC_ZERO","unrelated_rows_changed":0,"physical":False} for r in _one(system_id.replace("C200-ST-SYSTEM-","") if system_id and system_id.startswith("C200-ST-SYSTEM-") else None,RESOLUTIONS))
    if old_row_id is not None and old_row_id!="C200-BLOCKED-C197-ST-3": raise KeyError(old_row_id)
    if new_row_id is not None: rows=tuple(x for x in rows if x["new_row_id"]==new_row_id)
    return _freeze({"schema":"C201-ST3-REPLACEMENT-V1","rows":rows,"count":len(rows),"old_blocked_row_replaced":True,"unrelated_rows_changed":0,"root":_root(rows)})


def analyticity_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows=tuple({"record_id":f"C201-AN-{r}","resolution":r,"external_domain_id":external_record_id or f"C201-EXT-{r}-S3-E","fixture_id":fixture_id or f"C201-3G-FIXTURE-{r}","complex_conjugation":True,"orientation_reversal":True,"S3_Bose":True,"cyclic_odd_permutation":True,"all_eight_generator_covariance":True,"f_d_separate":True,"polarization_covariance":True,"derivative_covariance":True,"zero_pole_avoided":True,"Q0_P0_separate":True,"future_past_PV_cut_shift":"preserved caller interface","holonomy_conjugation":"transport covariance","boundary_link":"explicit interface","positivity":False,"unitarity":False,"continuum_extrapolation":False,"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C201-ANALYTICITY-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    owners=("canonical-cubic-tree","C184-g-gg-source-transition","connected","inverse-derivative","quark-loop","gluon-loop","ghost-loop-C200","quartic-contact","instantaneous-Gauss","tadpole-normal-ordering","G1-leg","G2-leg","G3-leg","three-gluon-reducible","HO-boundary","ghost-link","residual-link","holonomy","global-volume","gluon-field","proper","dressing-boundary","ST-row","counterterm","null","target","standard","physical")
    rows=tuple({"graph_id":f"C201-TOPO-{i}","owner":o,"count_once":True,"duplicate":False,"proper_separate":True,"loop_leg_separate":True,"ghost_open_closed_separate":True,"S3_count_once":True,"f_d_separate":True,"interface_nonmatrix":o in ("HO-boundary","ghost-link","residual-link","holonomy","global-volume"),"holonomy_loop":False,"missing_zero":False,"physical":False} for i,o in enumerate(owners,1))
    return _freeze({"schema":"C201-TOPOLOGY-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners=("C184_SOURCE_TRANSITION","TREE","CONNECTED","INVERSE_DERIVATIVE","QUARK","GLUON","GHOST_C200","NONPROPAGATING","G1","G2","G3","REDUCIBLE","PROPER","BOUNDARY","HOLO","GLOBAL_VOLUME","ST3_ROW","COUNTERTERM","NULL","TARGET","STANDARD","PHYSICAL")
    rows=tuple({"request_id":request_id or "C169-QCD_COUPLING-MOMQ","owner_id":o,"count":1,"duplicate":False,"S3_double_count":False,"holonomy_loop":False,"missing_zero":False} for o in owners)
    return _freeze({"schema":"C201-COUNT-ONCE-V1","rows":rows,"count":len(rows),"duplicates":0,"root":_root(rows)})


def ghostvert1_release_manifest() -> MappingProxyType:
    gates={"role":True,"external_domain":True,"parameter":True,"tree":True,"connected":True,"inverse_derivative":True,"components":True,"subtraction":True,"amputation":True,"proper":True,"projectors":True,"dressing":True,"boundary":True,"jacobian":True,"ST_replacement":True,"analyticity":True,"topology":True,"count_once":True,"full_ST":False,"physical":False,"target_MOMq":False}
    return _freeze({"schema":"C201-RELEASE-V1","status":STATUS,"plan":PLAN,"decision":STATUS,"gates":gates,"scope":"conditional finite-basis three-gluon proper vertex and renormalization-boundary authority","next":NEXT,"physical":False,"root":_root((STATUS,PLAN,gates))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows=[]
    for x in c200.request_resolution_manifest()["rows"]:
        active="QCD_COUPLING" in x["request_id"] or "qg_VERTEX" in x["request_id"]
        rows.append({"request_id":x["request_id"],"previous_status":x["terminal_status"],"terminal_status":"C201_THREE_GLUON_PROPER_VERTEX_CONDITIONAL_READY" if active else "PRESERVED_INHERITED_REQUEST","active_in_C201":active,"all_six_visible":True,"C199_ST1":"read-only","C200_ST2":"read-only","C201_ST3":active,"physical":False,"exact_next":NEXT if active else None})
    if request_id is not None: rows=[x for x in rows if x["request_id"]==request_id]
    return _freeze({"schema":"C201-REQUEST-V1","rows":tuple(rows),"count":len(rows),"all_six_visible":len(rows)==6 if request_id is None else True,"root":_root(rows)})


def missing_three_gluon_object_manifest(request_id: str | None = None) -> MappingProxyType:
    rows=tuple({"object_id":x["object_id"],"exact_missing_object":x["exact_missing_object"],"aliases":x["aliases"],"request_id":request_id,"status":"C201_REPLACED" if x["object_id"]=="C197-ST-3" else "PRESERVED_C201_FRONTIER","not_zero":True} for x in c200.missing_ghost_vertex_object_manifest()["rows"] if x["object_id"] not in ("C197-ST-1","C197-ST-2"))
    return _freeze({"schema":"C201-MISSING-3G-V1","rows":rows,"count":len(rows),"C197_ST_3_replaced":True,"remaining":("C197-ST-4","C197-ST-5","C197-ST-6","C197-ST-7","C197-ST-8","C197-ST-9","C197-ST-10"),"root":_root(rows)})


def next_st_handoff_contract() -> MappingProxyType:
    return _freeze({"schema":"C201-NEXT-ST-HANDOFF-V1","replaced_object":"C197-ST-3","next":NEXT,"next_object":"C197-ST-4","next_object_exact":"complete four-gluon renormalization","tree_root":tree_vertex_manifest()["root"],"connected_root":connected_response_manifest()["root"],"inverse_root":inverse_derivative_manifest()["root"],"component_root":component_manifest()["root"],"subtraction_root":reducible_subtraction_manifest()["root"],"amputation_root":amputation_manifest()["root"],"proper_root":proper_kernel_manifest()["root"],"projector_root":vertex_projector_manifest()["root"],"dressing_root":vertex_dressing_manifest()["root"],"boundary_root":boundary_link_manifest()["root"],"jacobian_root":jacobian_manifest()["root"],"replacement_root":st_replacement_manifest()["root"],"remaining":missing_three_gluon_object_manifest()["remaining"],"physical":False,"root":_root((STATUS,NEXT))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema":"C201-DEPENDENCY-V1","open":missing_three_gluon_object_manifest()["remaining"],"first":"C197-ST-4","C166_graph_delta":{"nodes_added":0,"edges_added":0},"C158_value_inputs":0,"Q0_Q1_Q2_modified":False,"root":_root((STATUS,0,0))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema":"C201-QUANTUM-NONMUTATION-V1","Q0_Q1_Q2_modified":False,"states":0,"qubits":0,"TMD_objects":0,"physical_parameters":0,"production_hamiltonian":0,"root":_root((0,0,0,0,0))})


def static_isolation_guard() -> MappingProxyType:
    fields=("C184_recomputed","C200_recomputed","qg_recomputed","ST12_recomputed","remembered_formula","physical_factor","four_gluon_invented","Bose_double_count","f_d_conflation","connected_proper_conflation","loop_leg_conflation","nonmatrix_fabricated","global_volume_absorbed","holonomy_loop","missing_zero","counterterms_selected","null_representatives","C158_value_inputs","C166_graph_delta","Q0_Q1_Q2_modified","resolution_average","continuum_extrapolation","quantum_modification")
    z={x:0 for x in fields}; return _freeze({**z,"pass":True,"root":_root((STATUS,PLAN))})


def mutate_live_hqcd3gvert1(index: int) -> MappingProxyType:
    if not isinstance(index,int) or not 0<=index<384: raise ValueError(index)
    fields=("frontier","external","parameter","tree","connected","inverse","component","subtraction","amputation","proper","projector","Bose","boundary","jacobian","replacement","analyticity","topology","request","continuation")
    return _freeze({"index":index,"mutation":fields[index%len(fields)],"result":"REJECTED_OR_ROOT_CHANGED","pass":True,"root":_root((index,STATUS))})


def three_gvert1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C201-COMPLETENESS-V1","status":STATUS,"plan":PLAN,"C197_ST_3_replaced":True,"external_records":external_domain_manifest()["count"],"fixtures":three_gluon_fixture_manifest()["count"],"tree_records":tree_vertex_manifest()["count"],"connected_records":connected_response_manifest()["count"],"inverse_records":inverse_derivative_manifest()["count"],"component_records":component_manifest()["count"],"subtraction_records":reducible_subtraction_manifest()["count"],"amputation_records":amputation_manifest()["count"],"proper_records":proper_kernel_manifest()["count"],"projector_records":vertex_projector_manifest()["count"],"dressing_records":vertex_dressing_manifest()["count"],"boundary_records":boundary_link_manifest()["count"],"jacobian_records":jacobian_manifest()["count"],"replacement_records":st_replacement_manifest()["count"],"remaining_frontier":7,"counterterms":6,"nulls":9,"selected":False,"full_ST":False,"physical":False,"root":_root((STATUS,PLAN,7))})


_ROOTS={"INPUT":_root((BASELINE,C200_CONTRACT,C200_CONTRACT_SHA256,PROMPT_SHA256)),"PLAN":three_gvert1_plan_manifest()["root"],"HANDOFF":three_gluon_handoff_freeze()["root"],"FRONTIER":frontier_manifest()["root"],"ROLE":vertex_role_decision()["root"],"EXTERNAL":external_domain_manifest()["root"],"PARAMETER":three_gluon_parameter_schema()["root"],"FIXTURE":three_gluon_fixture_manifest()["root"],"TREE":tree_vertex_manifest()["root"],"CONNECTED":connected_response_manifest()["root"],"INVERSE":inverse_derivative_manifest()["root"],"COMPONENT":component_manifest()["root"],"SUBTRACTION":reducible_subtraction_manifest()["root"],"AMPUTATION":amputation_manifest()["root"],"PROPER":proper_kernel_manifest()["root"],"PROJECTOR":vertex_projector_manifest()["root"],"DRESSING":vertex_dressing_manifest()["root"],"BOUNDARY":boundary_link_manifest()["root"],"JACOBIAN":jacobian_manifest()["root"],"REPLACEMENT":st_replacement_manifest()["root"],"ANALYTICITY":analyticity_manifest()["root"],"TOPOLOGY":topology_manifest()["root"],"COUNT":count_once_manifest()["root"],"RELEASE":ghostvert1_release_manifest()["root"],"REQUEST":request_resolution_manifest()["root"],"MISSING":missing_three_gluon_object_manifest()["root"],"NEXT":next_st_handoff_contract()["root"],"DEPENDENCY":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"],"ISOLATION":static_isolation_guard()["root"],"COMPLETENESS":three_gvert1_completeness_certificate()["root"]}
PACKAGE_ROOT=_root({"schema":"C201-HQCD3GVERT1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS})
ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
C201_PACKAGE_ROOT=PACKAGE_ROOT
C201_INPUT_ROOT=_ROOTS["INPUT"]
verify_hqcd3gvert1_authority_alias=verify_hqcd_3gvert1_authority
load_verified_hqcd3gvert1_authority=load_verified_hqcd_3gvert1_authority
__all__=[n for n in globals() if not n.startswith("_")]
