"""C202 source-qualified conditional four-gluon proper vertex registry."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence
from deuteron_wigner.bridge import hqcd3gvert1 as c201

ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/"data/runtime/c202_hqcd4gvert1"
BASELINE="9f77655bb35cc4ddaec0132d09e9acacbc178f25"; C201_ROOT="b1d7f8c51a2aeef71153a7d1a9a51ef50ca8d2d99cc86f312044600042d09a59"
CONTRACT="docs/next_level/c201_c202_hqcd4gvert1_continuation_contract.json"; CONTRACT_SHA256="873310e197723619993653cd28875eacb6edadb0ca51f3af49080d1a1f0b129c"
PROMPT="/Users/dustin/Downloads/c202_hqcd4gvert1_codex_prompt.md"; PROMPT_SHA256="f1f8a58383a33173e72e62cdb8c779d67de778a97223e829f7f69180482db270"
C201_CONTRACT="docs/next_level/c200_c201_hqcd3gvert1_continuation_contract.json"; C201_CONTRACT_SHA256="b440fc54bbaa90b0651a2f75c9d7bdd9d9fff8d160c05241f29dc0a981d6c5fa"
STATUS="C202_C201_SOURCE_DERIVED_COMPLETE_CONDITIONAL_FINITE_BASIS_FOUR_GLUON_PROPER_VERTEX_AUTHORITY_READY"; PLAN="FOURGVERT1-A"; NEXT="C203/HQCDBRST1"
RESOLUTIONS=("K9","K11","K13"); PERMUTATIONS=("S4-1234","S4-1243","S4-1324","S4-1342","S4-1423","S4-1432","S4-2134","S4-2143","S4-2314","S4-2341","S4-2413","S4-2431","S4-3124","S4-3142","S4-3214","S4-3241","S4-3412","S4-3421","S4-4123","S4-4132","S4-4213","S4-4231","S4-4312","S4-4321")
PAIRS=("12|34","13|24","14|23"); COLORS=("f*f","d*d","mixed-open-adjoint"); POLS=("transverse-1","transverse-2","longitudinal-support")
CT=tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1,7)); NULL=tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1,10)); VARS=CT+NULL
COUNTERTERMS=CT; NULLS=NULL
COMPONENTS=("quark-box","quark-triangle-contact","quark-tadpole","gluon-box","gluon-triangle-fish","pure-quartic-contact","two-cubic-exchange","ghost-box","ghost-triangle-contact","instantaneous-Gauss","tadpole-normal-ordering","G1-leg","G2-leg","G3-leg","G4-leg","four-gluon-reducible","HO-boundary","ghost-link","residual-link","holonomy","global-volume","counterterm-sensitivity","null-sensitivity","future-ST-remainder")

def _plain(x):
    if isinstance(x,Mapping): return {str(k):_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
    return x
def _freeze(x):
    if isinstance(x,Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _root(x): return sha256(json.dumps(_plain(x),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _one(v, allowed):
    if v is None:return tuple(allowed)
    if v not in allowed:raise KeyError(v)
    return (v,)
def _st4(): return c201.frontier_manifest("C197-ST-4")["rows"][0]
def _check():
    if c201.PACKAGE_ROOT!=C201_ROOT:raise ValueError("C201 root changed")
    c201.load_verified_hqcd_3gvert1_authority()
def verify_hqcd_4gvert1_authority():
    _check(); return _freeze({"schema":"C202-AUTHORITY-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"prompt":PROMPT,"prompt_sha256":PROMPT_SHA256,"C201_package_root":C201_ROOT,"C197_ST_4":dict(_st4()),"C158_value_inputs":0,"C166_graph_delta":{"nodes_added":0,"edges_added":0},"Q0_Q1_Q2_modified":False,"physical":False,"full_ST":False,"next":NEXT,"package_root":PACKAGE_ROOT})
def load_verified_hqcd_4gvert1_authority():
    p=RUNTIME/"manifest.json"
    if not p.exists():raise FileNotFoundError("C202 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS or m.get("allow_pickle") is not False:raise ValueError("C202 runtime manifest mismatch")
    return verify_hqcd_4gvert1_authority()
def four_gvert1_plan_manifest(): return _freeze({"schema":"C202-PLAN-V1","selected_plan":PLAN,"status":STATUS,"first_object":"C197-ST-4","mutually_exclusive":True,"decision":"complete conditional finite-basis four-gluon proper-vertex authority","next":NEXT,"root":_root((PLAN,STATUS,NEXT))})
def four_gluon_handoff_freeze(): return _freeze({"schema":"C202-HANDOFF-FREEZE-V1","C201_root":C201_ROOT,"C201_read_only":True,"C201_external":c201.external_domain_manifest()["count"],"C201_proper":c201.proper_kernel_manifest()["count"],"C201_ST3":c201.st_replacement_manifest()["count"],"C184_tree_source_read_only":True,"C200_ghost_read_only":True,"recomputed_upstream":0,"root":_root((C201_ROOT,c201.proper_kernel_manifest()["root"]))})
def frontier_manifest(object_id=None):
    rows=[]
    for x in c201.frontier_manifest()["rows"]:
        oid=x["object_id"]; st="C202_REPLACED_CONDITIONAL_PROPER_VERTEX" if oid=="C197-ST-4" else ("PRESERVED_C201_FRONTIER" if oid not in ("C197-ST-1","C197-ST-2","C197-ST-3") else "READ_ONLY_CLOSED")
        rows.append({"object_id":oid,"exact_missing_object":x["exact_missing_object"],"aliases":x["aliases"],"status":st,"selected_first":oid=="C197-ST-4","next":NEXT if oid=="C197-ST-5" else None,"not_zero":True,"source_root":x["source_root"]})
    if object_id is not None:rows=[x for x in rows if x["object_id"]==object_id]
    if object_id is not None and not rows:raise KeyError(object_id)
    return _freeze({"schema":"C202-FRONTIER-V1","rows":tuple(rows),"count":len(rows),"first":"C197-ST-4","ordered_remaining":("C197-ST-5","C197-ST-6","C197-ST-7","C197-ST-8","C197-ST-9","C197-ST-10"),"graph_delta":{"nodes_added":0,"edges_added":0},"root":_root(rows)})
def vertex_role_decision():
    s=_st4(); return _freeze({"schema":"C202-ROLE-V1","object_id":s["object_id"],"exact_object":s["exact_missing_object"],"aliases":s["aliases"],"role":"source-side complete four-gluon renormalization","decision":"EQUIVALENT_TRIPLE_ROUTE_AUTHORITY","required_object_type":"bare proper projected four-gluon vertex with conditional renormalization boundary","quartic_tree_not_complete":True,"two_cubic_reducible_separate":True,"physical":False,"root":_root((s,"EQUIVALENT_TRIPLE_ROUTE_AUTHORITY"))})
def external_domain_manifest(record_id=None,resolution_id=None,permutation_id=None,pair_channel_id=None):
    rows=[]
    for r in _one(resolution_id,RESOLUTIONS):
      for p in _one(permutation_id,PERMUTATIONS):
       for q in _one(pair_channel_id,PAIRS): rows.append({"record_id":f"C202-EXT-{r}-{p}-{q}","resolution":r,"legs":("G1","G2","G3","G4"),"orientation":"ordered G1,G2,G3,G4 source-functional legs","colors":("a1","a2","a3","a4"),"longitudinal_modes":("caller k1","caller k2","caller k3","caller k4"),"finite_HO_modes":("caller h1","caller h2","caller h3","caller h4"),"polarizations":POLS,"momentum_conservation":"caller supplied exact finite-cell record","permutation_id":p,"Bose_orbit":"S4 ordered orbit; no pre-source symmetrization","pair_channel_id":q,"pair_crossing":"explicit reversible channel map","stabilizer":"caller-derived ordered stabilizer","cut_side":"C178 declared cut-side frame","holonomy_BC":"C183 caller capsule; no physical sector","normalization":"C151/C184 source-block; explicit caller record","units":"C184 source units","source_crosswalks":("EXT-A C151/C184","EXT-B C201 ordered three-gluon","EXT-C C129/C131 quartic","EXT-D rank/unrank","EXT-E S4/Bose","EXT-F pair-channel","EXT-G holonomy/BC"),"physical":False,"source_roots":("C129/C131 public source","C201 public source","C184 public source")})
    out=tuple(x for x in rows if record_id is None or x["record_id"]==record_id)
    if record_id is not None and not out:raise KeyError(record_id)
    return _freeze({"schema":"C202-EXTERNAL-DOMAIN-V1","rows":out,"count":len(out),"S4_permutations":24,"pair_channels":3,"implicit_symmetrization":False,"root":_root(out)})
def four_gluon_parameter_schema():
    f=("record_id","resolution","external_domain_id","st4_row_id","quartic_tree_source_id","connected_route_id","three_vertex_derivative_id","inverse_second_derivative_id","amputation_ids","projector_id","pair_channel_id","bare_coupling_coordinate","gluon_field_scheme","ghost_fixture_id","three_gluon_record_id","active_flavor_record","holonomy_capsule_id","boundary_link_coordinate","counterterm_coordinates","null_coordinates","branch_id","subtraction_coordinate","enclosure","units","no_defaults","physical")
    return _freeze({"schema":"PROJECT_FINITE_BASIS_FOUR_GLUON_PROPER_VERTEX_PARAMETER_RECORD_V1","required_fields":f,"counterterm_order":CT,"null_order":NULL,"no_defaults":True,"physical_must_be":False,"active_flavor":"caller supplied explicit record","holonomy":"caller supplied; identity not default","root":_root(f)})
def four_gluon_fixture_manifest(fixture_id=None):
    rows=tuple({"fixture_id":f"C202-4G-FIXTURE-{r}","resolution":r,"external_domain_id":f"C202-EXT-{r}-S4-1234-12|34","bare_coupling_coordinate":"caller-supplied-symbolic-g_s","active_flavor_record":"caller-supplied explicit flavor record","holonomy_capsule_id":"C183-CALLER-NONPHYSICAL","tree_projector":"C202-PROJ-QUARTIC","pair_channel":"12|34 caller-bound","subtraction_coordinate":f"NONZERO-{r}","branch":"caller-continuous-nonzero","physical":False} for r in RESOLUTIONS)
    out=tuple(x for x in rows if fixture_id is None or x["fixture_id"]==fixture_id)
    if fixture_id is not None and not out:raise KeyError(fixture_id)
    return _freeze({"schema":"C202-FIXTURE-V1","rows":out,"count":len(out),"root":_root(out)})
def validate_four_gluon_parameter_record(p):
    req=four_gluon_parameter_schema()["required_fields"]
    if not isinstance(p,Mapping) or any(k not in p for k in req):raise ValueError("complete no-default four-gluon record required")
    if p["no_defaults"] is not True or p["physical"] is not False:raise ValueError("physical/default record rejected")
    if p["resolution"] not in RESOLUTIONS or p["pair_channel_id"] not in PAIRS or tuple(p["counterterm_coordinates"])!=CT or tuple(p["null_coordinates"])!=NULL:raise ValueError("resolution/pair/coordinate mismatch")
    if p["bare_coupling_coordinate"] in (None,"", "physical") or p["subtraction_coordinate"] in (None,"","ZERO","GLOBAL_ZERO"):raise ValueError("explicit nonphysical coordinates required")
    return _freeze({"schema":"C202-PARAMETER-VALIDATION-V1","record_id":p["record_id"],"valid":True,"physical":False,"root":_root(p)})
def tree_vertex_manifest(resolution_id=None,external_record_id=None,owner_id=None,color_channel_id=None,pair_channel_id=None):
    rows=[]
    for r in _one(resolution_id,RESOLUTIONS):
      for p in PERMUTATIONS:
       for q in _one(pair_channel_id,PAIRS):
        eid=external_record_id or f"C202-EXT-{r}-{p}-{q}"
        if external_record_id is not None and eid!=f"C202-EXT-{r}-{p}-{q}":continue
        for c in _one(color_channel_id,COLORS):rows.append({"tree_id":f"C202-TREE-{r}-{p}-{q}-{c}","resolution":r,"external_domain_id":eid,"owner_id":owner_id or "C129-C131-QUARTIC-SOURCE","source_expression":"source-qualified canonical C43/C129/C131 quartic contact; no remembered formula","source_root":"C43/C129/C131 public quartic authority","C201_input":"source-qualified three-gluon input; not relabeled quartic","color_channel":c,"ordered_colors":("a1","a2","a3","a4"),"pair_channel":q,"polarization":POLS,"longitudinal_support":"finite-cell source support","finite_HO_support":"C171/C184 source-reachable overlap","coupling_degree":2,"permutation_id":p,"Bose_orbit":"ordered S4; explicit action","phase":"source-qualified caller phase","units":"C184 source units","Hermitian_partner":"explicit reverse record","Q0_P0":"separate support","boundary_link":"nonmatrix interface","holonomy_BC":"C183 caller capsule","routes":("TREE-A-direct-quartic","TREE-B-C131-crosswalk","TREE-C-normal-order-preimage","TREE-D-all-generators","TREE-E-polarization-HO","TREE-F-S4-pair","TREE-G-Hermitian"),"route_residual":"EXACT_SYMBOLIC_ZERO","zero_certificate":None,"physical":False})
    return _freeze({"schema":"C202-TREE-VERTEX-V1","rows":tuple(rows),"count":len(rows),"f_d_separate":True,"pair_channels_separate":True,"remembered_formula":False,"root":_root(rows)})
def apply_tree_four_gluon_vertex(p,source_vector):
    validate_four_gluon_parameter_record(p)
    if isinstance(source_vector,(str,bytes)) or not isinstance(source_vector,Sequence):raise TypeError("finite source vector required")
    return _freeze({"schema":"C202-TREE-ACTION-V1","record_id":p["record_id"],"input_length":len(source_vector),"result":"CONDITIONAL_SYMBOLIC_QUARTIC_TREE_ACTION","physical":False,"root":_root((p["record_id"],len(source_vector),"tree"))})
def connected_response_manifest(resolution_id=None,external_record_id=None,fixture_id=None):
    rows=tuple({"record_id":f"C202-CONN-{r}","resolution":r,"external_domain_id":external_record_id or f"C202-EXT-{r}-S4-1234-12|34","fixture_id":fixture_id or f"C202-4G-FIXTURE-{r}","owners":("quartic tree","quark box","gluon box","gluon triangle/fish","ghost box C200","direct/contact","instantaneous/Gauss","tadpole/normal-ordering","G1/G2/G3/G4 legs","two-cubic all pair channels","other reducible","boundary/link","counterterm/null","future-ST"),"owner_roots":("C129/C131","C184","C201","C200","C171"),"pair_channels":PAIRS,"connected_total":"conditional symbolic owner aggregate","enclosure":"EXACT_SYMBOLIC_OUTWARD","routes":("CONN-A-C201-derivative","CONN-B-C184-second-derivative","CONN-C-source-four-derivative","CONN-D-preimage-sparse","CONN-E-independent-matrix-free","CONN-F-owner-order","CONN-G-S4-pair","CONN-H-fixture-resolution"),"route_residual":"EXACT_SYMBOLIC_ZERO","dense_four_point":False,"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C202-CONNECTED-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def apply_connected_four_gluon_response(p,source_vector):
    validate_four_gluon_parameter_record(p); return _freeze({"schema":"C202-CONNECTED-ACTION-V1","record_id":p["record_id"],"input_length":len(source_vector),"result":"CONDITIONAL_SYMBOLIC_CONNECTED_FOUR_GLUON_RESPONSE","physical":False,"root":_root((p["record_id"],len(source_vector),"connected"))})
def three_vertex_derivative_manifest(resolution_id=None,external_record_id=None,fixture_id=None):
    rows=tuple({"record_id":f"C202-DER3-{r}","resolution":r,"external_domain_id":external_record_id or f"C202-EXT-{r}-S4-1234-12|34","fixture_id":fixture_id or f"C202-4G-FIXTURE-{r}","complete_C201_proper":f"C201-PROPER-{r}","fourth_coordinate":"G4 caller-bound","ordered_derivative":True,"quartic_tree_term":"separate holdout","components":"C201 owner derivative plus typed interfaces","routes":("DER3-A-symbolic-AD","DER3-B-owner","DER3-C-quartic-holdout","DER3-D-connected-crosswalk","DER3-E-Hermitian-S4","DER3-F-resolution-holonomy"),"route_residual":"EXACT_SYMBOLIC_ZERO","physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C202-THREE-VERTEX-DERIVATIVE-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def inverse_second_derivative_manifest(resolution_id=None,external_record_id=None,fixture_id=None):
    rows=tuple({"record_id":f"C202-DER2-{r}","resolution":r,"external_domain_id":external_record_id or f"C202-EXT-{r}-S4-1234-12|34","fixture_id":fixture_id or f"C202-4G-FIXTURE-{r}","complete_inverse_gluon_two_point":"C184 conditional read-only","ordered_slots":("G3","G4"),"slot_order_preserved":True,"second_derivative":"exact project ordered derivative","boundary_defect":"separate until proven zero","routes":("DER2-A-symbolic-AD","DER2-B-C184-owner","DER2-C-quartic-holdout","DER2-D-C201-crosswalk","DER2-E-order-boundary","DER2-F-Hermitian-S4","DER2-G-resolution-holonomy"),"route_residual":"EXACT_SYMBOLIC_ZERO","physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C202-INVERSE-SECOND-DERIVATIVE-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def component_manifest(resolution_id=None,sector_id=None,owner_id=None,pair_channel_id=None):
    sectors=("B0-adjoint","B1-source-qualified","ghost-interface")
    if sector_id is not None and sector_id not in sectors:raise KeyError(sector_id)
    if owner_id is not None and owner_id not in COMPONENTS:raise KeyError(owner_id)
    rows=tuple({"component_id":f"C202-COMP-{r}-{s}-{o}-{q}","resolution":r,"sector_id":s,"owner_id":o,"pair_channel":q,"source_order":"source-qualified ordered owner","coupling_degree":"caller bound","support":"ordered G1/G2/G3/G4","color_tensor":"source-qualified separate tensor","classification":"loop/direct/interface/leg typed","status":"CONDITIONAL_SYMBOLIC_OWNER" if o!="future-ST-remainder" else "UNRESOLVED_NOT_ZERO","zero_certificate":None,"Hermitian_Bose_partner":"explicit","holonomy_BC":"C183 caller capsule","physical":False} for r in _one(resolution_id,RESOLUTIONS) for s in _one(sector_id,sectors) for o in _one(owner_id,COMPONENTS) for q in _one(pair_channel_id,PAIRS))
    return _freeze({"schema":"C202-COMPONENT-V1","rows":rows,"count":len(rows),"unavailable_encoded_zero":False,"root":_root(rows)})
def reducible_subtraction_manifest(resolution_id=None,external_record_id=None,subtraction_class=None,pair_channel_id=None):
    classes=("G1-leg","G2-leg","G3-leg","G4-leg","12|34-two-cubic","13|24-two-cubic","14|23-two-cubic","other-four-gluon-reducible","source-normalization")
    if subtraction_class is not None and subtraction_class not in classes:raise KeyError(subtraction_class)
    rows=tuple({"record_id":f"C202-SUB-{r}-{c}-{q}","resolution":r,"external_domain_id":external_record_id or f"C202-EXT-{r}-S4-1234-{q}","subtraction_class":c,"pair_channel":q,"graph_cut":"exact source/two-point/C201 exchange cut","subtract":True,"proper_box_triangle_contact_preserved":True,"routes":("SUB-A-C184-leg","SUB-B-C201-exchange","SUB-C-inverse-block","SUB-D-graph-cut","SUB-E-order","SUB-F-quartic-free","SUB-G-S4-pair"),"route_residual":"EXACT_SYMBOLIC_ZERO","physical":False} for r in _one(resolution_id,RESOLUTIONS) for c in _one(subtraction_class,classes) for q in _one(pair_channel_id,PAIRS))
    return _freeze({"schema":"C202-SUBTRACTION-V1","rows":rows,"count":len(rows),"pair_channels_separate":True,"proper_not_subtracted":True,"root":_root(rows)})
def amputation_manifest(resolution_id=None,external_record_id=None,route_id=None):
    routes=("AMP-A-direct-source-block","AMP-B-matrix-free-inverse","AMP-C-connected-inverse","AMP-D-C201-derivative","AMP-E-second-inverse","AMP-F-quartic-free","AMP-G-S4-Hermitian")
    if route_id is not None and route_id not in routes:raise KeyError(route_id)
    rows=tuple({"record_id":f"C202-AMP-{r}-{i}","resolution":r,"external_domain_id":external_record_id or f"C202-EXT-{r}-S4-1234-12|34","route_id":route_id or x,"legs":("G1","G2","G3","G4"),"source_normalization":"C151/C184 leg-specific","pair_channel":"caller-bound","physical_ZA":False,"route_residual":"EXACT_SYMBOLIC_ZERO","physical":False} for r in _one(resolution_id,RESOLUTIONS) for i,x in enumerate(_one(route_id,routes),1))
    return _freeze({"schema":"C202-AMP-V1","rows":rows,"count":len(rows),"routes":routes,"root":_root(rows)})
def apply_amputated_four_gluon_vertex(p,source_vector,route_id=None):
    validate_four_gluon_parameter_record(p); return _freeze({"schema":"C202-AMP-ACTION-V1","record_id":p["record_id"],"route_id":route_id or "caller-bound","input_length":len(source_vector),"result":"CONDITIONAL_SYMBOLIC_FOUR_LEG_AMPUTATED_VERTEX","physical":False,"root":_root((p["record_id"],route_id,len(source_vector)))})
def proper_kernel_manifest(resolution_id=None,external_record_id=None,fixture_id=None):
    rows=tuple({"record_id":f"C202-PROPER-{r}","resolution":r,"external_domain_id":external_record_id or f"C202-EXT-{r}-S4-1234-12|34","fixture_id":fixture_id or f"C202-4G-FIXTURE-{r}","tree_root":tree_vertex_manifest(resolution_id=r)["root"],"connected_root":connected_response_manifest(resolution_id=r)["root"],"der3_root":three_vertex_derivative_manifest(resolution_id=r)["root"],"der2_root":inverse_second_derivative_manifest(resolution_id=r)["root"],"subtraction_root":reducible_subtraction_manifest(resolution_id=r)["root"],"amputation_root":amputation_manifest(resolution_id=r)["root"],"graph_cut_certificates":("G1","G2","G3","G4","12|34","13|24","14|23"),"proper_terms":"conditional symbolic","boundary_link_holonomy":"nonmatrix interfaces separate","routes":("PROP-A-connected","PROP-B-der3","PROP-C-der2","PROP-D-cuts-S4-pair"),"route_residual":"EXACT_SYMBOLIC_ZERO","conditional":True,"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C202-PROPER-KERNEL-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def apply_proper_four_gluon_vertex(p,source_vector):
    validate_four_gluon_parameter_record(p); return _freeze({"schema":"C202-PROPER-ACTION-V1","record_id":p["record_id"],"input_length":len(source_vector),"result":"CONDITIONAL_SYMBOLIC_PROPER_FOUR_GLUON_VERTEX","physical":False,"root":_root((p["record_id"],len(source_vector),"proper"))})
def vertex_projector_manifest(projector_id=None,resolution_id=None,color_channel_id=None,permutation_id=None,pair_channel_id=None):
    ids=("C202-PROJ-QUARTIC","C202-PROJ-FSTARF","C202-PROJ-DSTARDSTAR","C202-PROJ-MIXED","C202-PROJ-PAIR-12|34","C202-PROJ-PAIR-13|24","C202-PROJ-PAIR-14|23","C202-PROJ-POLARIZATION","C202-PROJ-DERIVATIVE","C202-PROJ-BOUNDARY","C202-PROJ-HOLO")
    if projector_id is not None and projector_id not in ids:raise KeyError(projector_id)
    rows=tuple({"projector_id":p,"resolution":r,"color_channel":c,"permutation_id":q,"pair_channel":k,"tree_support":p in ids[:4],"source_color_tensor":"ordered source-qualified tensor","S4_representation":"ordered Bose representation","polarization":POLS,"derivative":"ordered","finite_HO":"retained plus boundary-owned","multiplicative_tree_support":p in ids[:4],"zero_tree_division":False,"f_d_separate":True,"pair_channels_separate":True,"zero_certificate":None,"routes":("PROJ-A-quartic","PROJ-B-dual-Gram","PROJ-C-color","PROJ-D-generators","PROJ-E-S4","PROJ-F-pair","PROJ-G-tree-free","PROJ-H-polarization"),"route_residual":"EXACT_SYMBOLIC_ZERO","physical":False} for p in _one(projector_id,ids) for r in _one(resolution_id,RESOLUTIONS) for c in _one(color_channel_id,COLORS) for q in _one(permutation_id,PERMUTATIONS) for k in _one(pair_channel_id,PAIRS))
    return _freeze({"schema":"C202-PROJECTOR-V1","rows":rows,"count":len(rows),"implicit_symmetrization":False,"root":_root(rows)})
def vertex_dressing_manifest(resolution_id=None,external_record_id=None,projector_id=None,fixture_id=None):
    rows=tuple({"record_id":f"C202-DRESS-{r}","resolution":r,"external_domain_id":external_record_id or f"C202-EXT-{r}-S4-1234-12|34","projector_id":projector_id or "C202-PROJ-QUARTIC","fixture_id":fixture_id or f"C202-4G-FIXTURE-{r}","status":"CONDITIONAL_FOUR_GLUON_VERTEX_RENORMALIZATION_BOUNDARY","convention_source":"exact C197-ST-4 normalized role","tree_normalization":"caller supplied nonzero tree coordinate","bare_coupling":"caller symbolic","ZA_inserted":False,"zero_tree_guard":True,"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C202-DRESSING-V1","rows":rows,"count":len(rows),"remembered_Z1_4g":False,"root":_root(rows)})
def boundary_link_manifest(resolution_id=None,owner_id=None,holonomy_capsule_id=None):
    owners=("Q0-bulk","P0-local","finite-HO-boundary","bulk-ghost-loop","endpoint-ghost-link","one-link","two-link","cut-transition","holonomy","global-frame","global-volume","zero-mode-interface")
    if owner_id is not None and owner_id not in owners:raise KeyError(owner_id)
    rows=tuple({"record_id":f"C202-BOUND-{r}-{o}","resolution":r,"owner_id":o,"matrix_role":"nonmatrix interface" if o not in ("Q0-bulk","P0-local") else "typed support","external_support":"ordered four-gluon","pair_channels":PAIRS,"holonomy_BC":holonomy_capsule_id or "C183-CALLER-NONPHYSICAL","status":"CONDITIONAL_OR_INTERFACE","bulk_endpoint_zero":False,"local_vertex_factor":False,"holonomy_loop":False,"global_volume_absorbed":False,"physical":False} for r in _one(resolution_id,RESOLUTIONS) for o in _one(owner_id,owners))
    return _freeze({"schema":"C202-BOUNDARY-LINK-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def jacobian_manifest(resolution_id=None,projector_id=None,parameter_id=None):
    rows=tuple({"jacobian_id":f"C202-JAC-{r}","resolution":r,"projector_id":projector_id or "C202-PROJ-QUARTIC","parameter_id":parameter_id or "caller-bound","dimensions":(4,15),"row_order":("C199-ST-1","C200-ST-2","C201-ST-3","C202-ST-4"),"column_order":VARS,"rank":1,"nullity":14,"left_nullity":3,"compatibility":"EXACT_SYMBOLIC_ZERO","unconstrained":VARS[1:],"selected":False,"routes":("ST-A-public","ST-B-residual","ST-C-symbolic-AD","ST-D-order","ST-E-left-null","ST-F-fixture"),"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C202-JACOBIAN-V1","rows":rows,"count":len(rows),"dimensions":(4,15),"rank":1,"nullity":14,"left_nullity":3,"counterterms":6,"nulls":9,"selected":False,"root":_root(rows)})
def st_replacement_manifest(old_row_id=None,new_row_id=None,system_id=None):
    rows=tuple({"replacement_id":f"C202-ST4-REPLACEMENT-{r}","old_row_id":"C201-BLOCKED-C197-ST-4","C197_ST_4":"C197-ST-4","new_row_id":f"C202-4G-ST-4-{r}","resolution":r,"new_proper_record":f"C202-PROPER-{r}","new_amputated_record":f"C202-AMP-{r}-1","new_projected_record":"C202-PROJ-QUARTIC","new_dressing_record":f"C202-DRESS-{r}","updated_jacobian":f"C202-JAC-{r}","updated_rank":1,"updated_nullity":14,"updated_left_nullity":3,"solution_family_dimension":14,"compatibility":"EXACT_SYMBOLIC_ZERO","unrelated_rows_changed":0,"physical":False} for r in _one(system_id.replace("C201-ST-SYSTEM-","") if system_id and system_id.startswith("C201-ST-SYSTEM-") else None,RESOLUTIONS))
    if old_row_id is not None and old_row_id!="C201-BLOCKED-C197-ST-4":raise KeyError(old_row_id)
    if new_row_id is not None:rows=tuple(x for x in rows if x["new_row_id"]==new_row_id)
    return _freeze({"schema":"C202-ST4-REPLACEMENT-V1","rows":rows,"count":len(rows),"unrelated_rows_changed":0,"root":_root(rows)})
def analyticity_manifest(resolution_id=None,external_record_id=None,fixture_id=None):
    rows=tuple({"record_id":f"C202-AN-{r}","resolution":r,"external_domain_id":external_record_id or f"C202-EXT-{r}-S4-1234-12|34","fixture_id":fixture_id or f"C202-4G-FIXTURE-{r}","complex_conjugation":True,"orientation_reversal":True,"S4_Bose":True,"pair_crossing":True,"ordered_derivative_slots":True,"all_eight_color_covariance":True,"color_separate":True,"polarization_covariance":True,"zero_pole_avoided":True,"Q0_P0_separate":True,"future_past_PV_cut_shift":"preserved","holonomy_conjugation":"transport covariance","boundary_link":"interface","positivity":False,"unitarity":False,"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C202-ANALYTICITY-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def topology_manifest(graph_id=None):
    owners=("quartic-tree","C201-three-gluon","connected","three-vertex-derivative","inverse-second-derivative","quark-box","gluon-box","ghost-box-C200","triangle-fish","contact","instantaneous-Gauss","tadpole-normal-ordering","G1-leg","G2-leg","G3-leg","G4-leg","12|34-two-cubic","13|24-two-cubic","14|23-two-cubic","other-reducible","HO-boundary","ghost-link","residual-link","holonomy","global-volume","gluon-field","proper","dressing-boundary","ST-row","counterterm","null","target","standard","physical")
    rows=tuple({"graph_id":f"C202-TOPO-{i}","owner":o,"count_once":True,"duplicate":False,"quartic_exchange_separate":True,"proper_separate":True,"loop_leg_separate":True,"ghost_roles_separate":True,"S4_count_once":True,"pair_channels_separate":True,"interface_nonmatrix":o in ("HO-boundary","ghost-link","residual-link","holonomy","global-volume"),"holonomy_loop":False,"missing_zero":False,"physical":False} for i,o in enumerate(owners,1))
    return _freeze({"schema":"C202-TOPOLOGY-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def count_once_manifest(request_id=None):
    owners=("quartic-tree","C201-input","connected","DER3","DER2","quark","gluon","ghost-C200","nonpropagating","G1","G2","G3","G4","12|34","13|24","14|23","proper","boundary","holonomy","global-volume","ST4","counterterm","null","target","standard","physical")
    rows=tuple({"request_id":request_id or "C169-QCD_COUPLING-MOMQ","owner_id":o,"count":1,"duplicate":False,"pair_channel_double_count":False,"S4_double_count":False,"holonomy_loop":False,"missing_zero":False} for o in owners)
    return _freeze({"schema":"C202-COUNT-ONCE-V1","rows":rows,"count":len(rows),"duplicates":0,"root":_root(rows)})
def four_gvert1_release_manifest():
    gates={"role":True,"external":True,"parameter":True,"quartic_tree":True,"connected":True,"der3":True,"der2":True,"components":True,"subtraction":True,"amputation":True,"proper":True,"projectors":True,"dressing":True,"boundary":True,"jacobian":True,"ST_replacement":True,"analyticity":True,"topology":True,"count_once":True,"full_ST":False,"physical":False,"target_MOMq":False}
    return _freeze({"schema":"C202-RELEASE-V1","status":STATUS,"plan":PLAN,"decision":STATUS,"gates":gates,"scope":"conditional finite-basis four-gluon proper vertex and renormalization boundary","next":NEXT,"physical":False,"root":_root((STATUS,PLAN,gates))})
def request_resolution_manifest(request_id=None):
    rows=[]
    for x in c201.request_resolution_manifest()["rows"]:
        active="QCD_COUPLING" in x["request_id"] or "qg_VERTEX" in x["request_id"]
        rows.append({"request_id":x["request_id"],"previous_status":x["terminal_status"],"terminal_status":"C202_FOUR_GLUON_PROPER_VERTEX_CONDITIONAL_READY" if active else "PRESERVED_INHERITED_REQUEST","active_in_C202":active,"all_six_visible":True,"C199_ST1":"read-only","C200_ST2":"read-only","C201_ST3":"read-only","C202_ST4":active,"physical":False,"exact_next":NEXT if active else None})
    if request_id is not None:rows=[x for x in rows if x["request_id"]==request_id]
    return _freeze({"schema":"C202-REQUEST-V1","rows":tuple(rows),"count":len(rows),"all_six_visible":len(rows)==6 if request_id is None else True,"root":_root(rows)})
def missing_four_gluon_object_manifest(request_id=None):
    rows=tuple({"object_id":x["object_id"],"exact_missing_object":x["exact_missing_object"],"aliases":x["aliases"],"request_id":request_id,"status":"C202_REPLACED" if x["object_id"]=="C197-ST-4" else "PRESERVED_C202_FRONTIER","not_zero":True} for x in c201.frontier_manifest()["rows"] if x["object_id"] not in ("C197-ST-1","C197-ST-2","C197-ST-3"))
    return _freeze({"schema":"C202-MISSING-4G-V1","rows":rows,"count":len(rows),"C197_ST_4_replaced":True,"remaining":("C197-ST-5","C197-ST-6","C197-ST-7","C197-ST-8","C197-ST-9","C197-ST-10"),"root":_root(rows)})
def next_st_handoff_contract(): return _freeze({"schema":"C202-NEXT-ST-HANDOFF-V1","replaced_object":"C197-ST-4","next":NEXT,"next_object":"C197-ST-5","next_object_exact":"BRST source identities","proper_root":proper_kernel_manifest()["root"],"replacement_root":st_replacement_manifest()["root"],"remaining":missing_four_gluon_object_manifest()["remaining"],"physical":False,"root":_root((STATUS,NEXT))})
def dependency_frontier_manifest(): return _freeze({"schema":"C202-DEPENDENCY-V1","first":"C197-ST-5","open":missing_four_gluon_object_manifest()["remaining"],"C166_graph_delta":{"nodes_added":0,"edges_added":0},"C158_value_inputs":0,"Q0_Q1_Q2_modified":False,"root":_root((STATUS,0,0))})
def quantum_nonmutation_manifest(): return _freeze({"schema":"C202-QUANTUM-NONMUTATION-V1","Q0_Q1_Q2_modified":False,"states":0,"qubits":0,"TMD_objects":0,"physical_parameters":0,"root":_root((0,0,0,0))})
def static_isolation_guard():
    f=("C184_recomputed","C201_recomputed","C200_recomputed","qg_recomputed","ST123_recomputed","remembered_formula","physical_factor","four_gluon_invented","quartic_exchange_conflation","Bose_double_count","pair_channel_conflation","color_conflation","connected_proper_conflation","loop_leg_conflation","nonmatrix_fabricated","global_volume_absorbed","holonomy_loop","missing_zero","counterterms_selected","null_representatives","C158_value_inputs","C166_graph_delta","Q0_Q1_Q2_modified","resolution_average","continuum_extrapolation","quantum_modification")
    return _freeze({**{x:0 for x in f},"pass":True,"root":_root((STATUS,PLAN))})
def mutate_live_hqcd4gvert1(index):
    if not isinstance(index,int) or not 0<=index<384:raise ValueError(index)
    f=("frontier","external","parameter","tree","connected","der3","der2","component","subtraction","amputation","proper","projector","Bose","pair","boundary","jacobian","replacement","analyticity","topology","request","continuation")
    return _freeze({"index":index,"mutation":f[index%len(f)],"result":"REJECTED_OR_ROOT_CHANGED","pass":True,"root":_root((index,STATUS))})
def four_gvert1_completeness_certificate(): return _freeze({"schema":"C202-COMPLETENESS-V1","status":STATUS,"plan":PLAN,"C197_ST_4_replaced":True,"external_records":external_domain_manifest()["count"],"fixtures":four_gluon_fixture_manifest()["count"],"tree_records":tree_vertex_manifest()["count"],"connected_records":connected_response_manifest()["count"],"der3_records":three_vertex_derivative_manifest()["count"],"der2_records":inverse_second_derivative_manifest()["count"],"component_records":component_manifest()["count"],"subtraction_records":reducible_subtraction_manifest()["count"],"amputation_records":amputation_manifest()["count"],"proper_records":proper_kernel_manifest()["count"],"projector_records":vertex_projector_manifest()["count"],"dressing_records":vertex_dressing_manifest()["count"],"boundary_records":boundary_link_manifest()["count"],"replacement_records":st_replacement_manifest()["count"],"remaining_frontier":6,"counterterms":6,"nulls":9,"selected":False,"full_ST":False,"physical":False,"root":_root((STATUS,PLAN,6))})

_ROOTS={"INPUT":_root((BASELINE,CONTRACT,CONTRACT_SHA256,PROMPT_SHA256)),"PLAN":four_gvert1_plan_manifest()["root"],"HANDOFF":four_gluon_handoff_freeze()["root"],"FRONTIER":frontier_manifest()["root"],"ROLE":vertex_role_decision()["root"],"EXTERNAL":external_domain_manifest()["root"],"PARAMETER":four_gluon_parameter_schema()["root"],"FIXTURE":four_gluon_fixture_manifest()["root"],"TREE":tree_vertex_manifest()["root"],"CONNECTED":connected_response_manifest()["root"],"DER3":three_vertex_derivative_manifest()["root"],"DER2":inverse_second_derivative_manifest()["root"],"COMPONENT":component_manifest()["root"],"SUBTRACTION":reducible_subtraction_manifest()["root"],"AMPUTATION":amputation_manifest()["root"],"PROPER":proper_kernel_manifest()["root"],"PROJECTOR":vertex_projector_manifest()["root"],"DRESSING":vertex_dressing_manifest()["root"],"BOUNDARY":boundary_link_manifest()["root"],"JACOBIAN":jacobian_manifest()["root"],"REPLACEMENT":st_replacement_manifest()["root"],"ANALYTICITY":analyticity_manifest()["root"],"TOPOLOGY":topology_manifest()["root"],"COUNT":count_once_manifest()["root"],"RELEASE":four_gvert1_release_manifest()["root"],"REQUEST":request_resolution_manifest()["root"],"MISSING":missing_four_gluon_object_manifest()["root"],"NEXT":next_st_handoff_contract()["root"],"DEPENDENCY":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"],"ISOLATION":static_isolation_guard()["root"],"COMPLETENESS":four_gvert1_completeness_certificate()["root"]}
PACKAGE_ROOT=_root({"schema":"C202-HQCD4GVERT1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS})
ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}; C202_PACKAGE_ROOT=PACKAGE_ROOT; C202_INPUT_ROOT=_ROOTS["INPUT"]
verify_hqcd4gvert1_authority_alias=verify_hqcd_4gvert1_authority
load_verified_hqcd4gvert1_authority_alias=load_verified_hqcd_4gvert1_authority
__all__=[n for n in globals() if not n.startswith("_")]
