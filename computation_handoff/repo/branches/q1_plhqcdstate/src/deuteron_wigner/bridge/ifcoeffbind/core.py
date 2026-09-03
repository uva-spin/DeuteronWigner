"""C107 binding/evaluation over immutable C77 and C74 authorities.

The C104 AST is unchanged.  This module supplies only the missing endpoint
values and directed radii, then evaluates its closed CONJUGATE/MULTIPLY AST.
No C80 or downstream contact interface is imported.
"""
from __future__ import annotations
import gzip, json, math, re
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..ifpersist4.core import programs, canonical_record, manifest, COUNTS, LOGICAL

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c107_ifcoeffbind"
SCHEMA = "C107-IFCOEFFBIND-V1"
STATUS = "C107_C104_SOURCE_DERIVED_CERTIFIED_COEFFICIENT_SYMBOL_BINDING_READY"
C104_PACKAGE_ROOT = "42d3dc72def67806245875cf8c9fdfd1d801b212716e6735ade0763b4b2028de"
EXPECTED_AST_ROOT = "72c86d7a7b7191731f613b13a0be6dd060b5054669119935ee4de41652449136"
RESOLUTIONS = tuple(COUNTS)

def _plain(v: Any) -> Any:
    if hasattr(v, "items"): return {str(k): _plain(x) for k, x in v.items()}
    if isinstance(v, (tuple, list)): return [_plain(x) for x in v]
    return v

def _canon(v: Any) -> str:
    return json.dumps(_plain(v), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)

def _digest(v: Any) -> str:
    return sha256(_canon(v).encode()).hexdigest()

def _freeze(v: Any) -> Any:
    if isinstance(v, dict): return MappingProxyType({k: _freeze(x) for k, x in v.items()})
    if isinstance(v, list): return tuple(_freeze(x) for x in v)
    return v

def _safe(path: Path) -> Path:
    p = path.resolve()
    if RUNTIME not in p.parents or p.is_symlink() or not p.is_file(): raise ValueError("unsafe C107 runtime path")
    return p

def _load_runtime(name: str) -> Any:
    p = _safe(RUNTIME / name)
    return json.loads(p.read_text())

def _pair_kin(pair_id: str) -> int:
    m = re.search(r":KIN=(\d+):TRIP=(\d+)$", pair_id)
    if not m: raise ValueError("C104 pair identity lacks frozen C78 KIN/TRIP fields")
    return int(m.group(1))

def _color_key(identity: str) -> tuple[str, str]:
    if "|" not in identity: raise ValueError("C104 color identity is not the frozen product|triplet form")
    row, col = identity.split("|", 1)
    return row, col

def _component_key(resolution: str, kin: int, raw_id: str) -> str:
    return f"{resolution}|KIN={kin}|{raw_id}"

def _authority() -> dict[str, Any]:
    # Public project-owned authorities only; their loaders verify source
    # inventories and return immutable arrays/records.
    from ..qgembed9.core import QGEmbeddingPackage
    from ..qgcolor6.core import TripletAuthorityPackage
    c77 = QGEmbeddingPackage(); color = TripletAuthorityPackage()
    components: dict[str, dict[str, Any]] = {}
    for resolution in RESOLUTIONS:
        package = c77.load_qg_embedding_package(resolution)
        for kin in range(int(package["shape"][1])):
            for item in c77.physical_qg_raw_components(resolution, kin):
                key = _component_key(resolution, kin, item["raw"]["id"])
                row = {"key": key, "resolution": resolution, "kin": kin,
                       "raw_id": item["raw"]["id"], "midpoint": list(item["midpoint"]),
                       "bound": float(item["bound"]), "support": item["support"],
                       "source": "C77 public physical_qg_raw_components"}
                if key in components and components[key] != row: raise ValueError("ambiguous C77 component binding")
                components[key] = row
    u3: dict[str, dict[str, Any]] = {}
    for item in color.exact_records():
        row, col = item["row_id"], item["column_id"]
        key = f"{row}|{col}"
        arr = color.load("U3"); i, j = item["index"]
        z = complex(arr[i, j]); value = {"real": z.real, "imag": z.imag}
        rec = {"key": key, "row_id": row, "column_id": col, "midpoint": [z.real, z.imag],
               "bound": float(item["bound"]), "status": item["status"],
               "expression": item["expression"], "source": "C74 public exact-record/U3 authority"}
        if key in u3 and u3[key] != rec: raise ValueError("ambiguous U3 binding")
        u3[key] = rec
    if len(u3) != 72 or not components: raise ValueError("incomplete endpoint authority")
    return {"components": components, "u3": u3}

def _product_bound(z: complex, ez: float, w: complex, ew: float) -> float:
    return abs(z) * ew + abs(w) * ez + ez * ew

def _evaluate_from_record(rec: Any, component_table: dict[str, Any], u3_table: dict[str, Any]) -> dict[str, Any]:
    p = rec["pair"]; resolution = p["resolution"]; bra_kin = _pair_kin(p["bra"]); ket_kin = _pair_kin(p["ket"])
    vals = rec["coordinate"]["axis_values"]
    out_raw, out_color, in_raw, in_color = vals
    bout = component_table[_component_key(resolution, bra_kin, out_raw)]
    bket = component_table[_component_key(resolution, ket_kin, in_raw)]
    row_o, col_o = _color_key(out_color); row_i, col_i = _color_key(in_color)
    uo, ui = u3_table[f"{row_o}|{col_o}"], u3_table[f"{row_i}|{col_i}"]
    a = complex(*bout["midpoint"]); ea = bout["bound"]; b = complex(*bket["midpoint"]); eb = bket["bound"]
    u = complex(*uo["midpoint"]); eu = uo["bound"]; v = complex(*ui["midpoint"]); ev = ui["bound"]
    left, right = a * u, b * v
    # Radius of each two-factor enclosure, then the conjugate/multiply AST.
    el = _product_bound(a, ea, u, eu); er = _product_bound(b, eb, v, ev)
    value = left.conjugate() * right
    radius = _product_bound(left, el, right, er)
    ast_root = _digest(rec["projected_coefficient"]["expression"])
    if ast_root != EXPECTED_AST_ROOT: raise ValueError("C104 coefficient AST root mismatch")
    return {"value": [value.real, value.imag], "bound": radius,
            "status": "EXACT_ZERO" if value == 0 and radius == 0 else "CERTIFIED_INTERVAL",
            "unit": "dimensionless projected coefficient", "ast_root": ast_root,
            "record_id": rec["record_id"], "pair_local_ordinal": rec["pair_local_ordinal"],
            "components": {"bra": bout["key"], "ket": bket["key"]},
            "u3": {"bra": uo["key"], "ket": ui["key"]},
            "bound_rule": "C82_PROPAGATED_PRODUCT_BOUND", "C104_PACKAGE_ROOT": C104_PACKAGE_ROOT,
            "C103_equivalence_certificate_root": rec["ancestry"]["pair_equivalence_root"]}

def load_verified_coefficient_binding_authority() -> Any:
    m = _load_runtime("manifest.json")
    if m.get("schema") != SCHEMA or m.get("C104_PACKAGE_ROOT") != C104_PACKAGE_ROOT: raise ValueError("C107 root/schema mismatch")
    for obj in m["objects"]:
        p = _safe(ROOT / obj["path"])
        if sha256(p.read_bytes()).hexdigest() != obj["sha256"]: raise ValueError("C107 payload hash mismatch")
    return _freeze(m)

def verify_coefficient_binding_authority() -> dict[str, Any]:
    m = load_verified_coefficient_binding_authority(); a = _load_runtime("audit.json")
    return {"status": m["status"], "pass": bool(a["pass"]), "audit": _freeze(a),
            "C80_calls": 0, "kernel_values": 0, "products": 0, "contact_entries": 0}

def _tables() -> tuple[dict[str, Any], dict[str, Any]]:
    return _load_runtime("components.json"), _load_runtime("u3.json")

def evaluate_projected_coefficient(pair_id: str, resolution: str, ordinal: int) -> Any:
    p = programs().get((pair_id, resolution))
    if p is None: raise KeyError((pair_id, resolution))
    rec = canonical_record(pair_id, resolution, ordinal); components, u3 = _tables()
    return _freeze(_evaluate_from_record(rec, components, u3))

def evaluate_coefficient_bound(pair_id: str, resolution: str, ordinal: int) -> Any:
    return _freeze({k: evaluate_projected_coefficient(pair_id, resolution, ordinal)[k] for k in ("bound", "status", "record_id", "pair_local_ordinal")})

def evaluated_canonical_record(pair_id: str, resolution: str, ordinal: int) -> Any:
    rec = dict(canonical_record(pair_id, resolution, ordinal)); val = dict(evaluate_projected_coefficient(pair_id, resolution, ordinal))
    rec["projected_coefficient"] = {"expression": rec["projected_coefficient"]["expression"], "value": val["value"]}
    rec["coefficient_bound"] = {"kind": "C82_PROPAGATED_PRODUCT_BOUND", "value": val["bound"], "status": val["status"]}
    rec["evaluation"] = val
    return _freeze(rec)

def coefficient_binding_crosswalk(pair_id: str, resolution: str, ordinal: int) -> Any:
    val = evaluate_projected_coefficient(pair_id, resolution, ordinal)
    return _freeze({"pair_id": pair_id, "resolution": resolution, "ordinal": ordinal, "binding": val["components"], "u3": val["u3"], "record_id": val["record_id"]})

def evaluated_coefficient_page(pair_id: str, resolution: str, *, cursor: str | None = None, limit: int = 16) -> Any:
    """Bounded immutable page over one factorized pair; never expands globally."""
    if not 1 <= limit <= 256: raise ValueError("limit")
    p = programs().get((pair_id, resolution))
    if p is None: raise KeyError((pair_id, resolution))
    start = 0
    if cursor is not None:
        c = json.loads(cursor)
        if c.get("schema") != SCHEMA or c.get("pair_id") != pair_id or c.get("resolution") != resolution or c.get("limit") != limit: raise ValueError("cursor identity mismatch")
        start = int(c["next"])
    stop = min(start + limit, int(p["program"]["cardinality"]))
    rows = [evaluate_projected_coefficient(pair_id, resolution, i) for i in range(start, stop)]
    nxt = None if stop == int(p["program"]["cardinality"]) else _canon({"schema": SCHEMA, "pair_id": pair_id, "resolution": resolution, "next": stop, "limit": limit})
    return _freeze({"records": rows, "start": start, "stop": stop, "next_cursor": nxt})
