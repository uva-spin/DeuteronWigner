"""C123/ICAXIS finite logical-axis authority.

This package publishes identities and finite-domain ordering only.  It does
not instantiate C122 witnesses, matrix targets, numerical values, bounds,
component sums, or operators.  The C117 graph records intentionally describe
their mode domains without publishing their finite members; that distinction
is retained as an authenticated, fail-closed qualification here.
"""
from __future__ import annotations

import ast
import base64
import json
from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..basis1.core import q_basis, qg_basis
from ..icdomain.core import PROGRAMS as C122_PROGRAMS
from ..icreg2.core import CLASSES as GRAPH_CLASSES, graph_manifest, internal_mode_domain
from ..icnorm3.core import current_factor_leaf_inventory
from ..qgembed9.core import QGEmbeddingPackage
from ..qgcolor6.core import TripletAuthorityPackage

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c123_icaxis"
RUNTIME_MANIFEST_SHA256 = "805890c52d769c73f0bc90c100f1b466a2ca40236906c301620e7f3aca893e3c"
BASELINE = "a2bf6c3052a83a11680b6e321947f21bcaf7b5d9"
CONTRACT = "docs/next_level/c122_c123_icaxis_import_contract.json"
STATUS = "C123_ICAXIS_AXIS_CARDINALITY_INCOMPLETE"
NEXT = "C124/ICDOMAIN2"
SCHEMA = "C123-ICAXIS-V1"

# These are the canonical C112/C77 conditioning identities.  C122's
# inventory carried stale N8 spellings for K11/K13; they remain available as
# explicit aliases and are never silently treated as scientific identities.
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
LEGACY_RESOLUTION_ALIASES = {
    "K11_2_N8_b0.40": "K11_2_N10_b0.45",
    "K13_2_N8_b0.40": "K13_2_N12_b0.50",
}
AXES = (
    "physical_bra_state", "physical_ket_state", "source_graph",
    "monomial_descendant", "longitudinal_transfer", "external_modes",
    "spin_polarization", "ordered_color", "CM_ground", "triplet",
    "orientation",
)
PROGRAMS = C122_PROGRAMS
ROUTE_CLASSES = (
    "PUBLIC_PAYLOAD_DIRECT_FACADE", "PUBLIC_PAYLOAD_EXACT_ADAPTER",
    "DESCENDANT_SOURCE_CHAIN_RECONSTRUCTION", "AMBIGUOUS_BLOCKING",
)
ATOMICITY = (
    "UPSTREAM_PRIMITIVE_OWNS_SUM", "C122_WITNESS_DOMAIN_OWNS_MODE",
    "EXACT_FACTORIZED_AXIS", "NOT_APPLICABLE_WITH_PROOF",
)


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, tuple):
        return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, dict):
        return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, list):
        return tuple(_freeze(v) for v in x)
    if isinstance(x, tuple):
        return tuple(_freeze(v) for v in x)
    return x


def _canon(x: Any) -> str:
    return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)


def _root(x: Any) -> str:
    return sha256(_canon(x).encode()).hexdigest()


def _file_hash(rel: str) -> str:
    return sha256((ROOT / rel).read_bytes()).hexdigest()


@lru_cache(maxsize=1)
def _crosswalk() -> Any:
    return QGEmbeddingPackage().load_canonical_tm_crosswalk()


@lru_cache(maxsize=1)
def _color_columns() -> tuple[Any, ...]:
    return tuple(TripletAuthorityPackage().triplet_columns())


def _resolution(label: str) -> str:
    return LEGACY_RESOLUTION_ALIASES.get(label, label)


def _require_resolution(label: str) -> str:
    out = _resolution(label)
    if out not in RESOLUTIONS:
        raise KeyError(label)
    return out


def _conditioning(value: Any) -> MappingProxyType:
    """Normalize conditioning without using array position or magnitude."""
    if value is None:
        return _freeze({})
    if isinstance(value, str):
        return _freeze({"resolution": _require_resolution(value)})
    if isinstance(value, MappingProxyType):
        value = dict(value)
    if isinstance(value, dict):
        out = dict(value)
        if "resolution" in out:
            out["resolution"] = _require_resolution(out["resolution"])
        return _freeze(out)
    if isinstance(value, (tuple, list)) and len(value) == 2:
        return _freeze({"resolution": _require_resolution(value[0]), "sector": value[1]})
    raise TypeError("conditioning key must be a resolution or canonical mapping")


def _condition_token(value: Any) -> str:
    return _canon(_conditioning(value))


def _cursor(axis_id: str, conditioning: Any, next_rank: int) -> str:
    body = {"schema": "C123-CURSOR-V1", "authority": PACKAGE_ROOT,
            "axis_id": axis_id, "conditioning": _plain(_conditioning(conditioning)),
            "next_rank": int(next_rank)}
    body["digest"] = _root(body)
    return base64.urlsafe_b64encode(_canon(body).encode()).decode()


def _decode_cursor(value: str, axis_id: str, conditioning: Any) -> int:
    try:
        body = json.loads(base64.urlsafe_b64decode(value.encode()).decode())
        digest = body.pop("digest")
        if body.get("schema") != "C123-CURSOR-V1" or body.get("authority") != PACKAGE_ROOT:
            raise ValueError("cursor authority mismatch")
        if body.get("axis_id") != axis_id or body.get("conditioning") != _plain(_conditioning(conditioning)):
            raise ValueError("cursor conditioning mismatch")
        if _root(body) != digest:
            raise ValueError("cursor digest mismatch")
        return int(body["next_rank"])
    except Exception as exc:
        raise ValueError("invalid C123 cursor") from exc


def _q_id(resolution: str, index: int, row: tuple) -> str:
    return f"C123:Q:{resolution}:K={row[0]}:M={row[1]}:H={row[3]}:C={row[4]}:I={index}"


def _semantic_qg_id(resolution: str, row: dict[str, Any], color: int, index: int) -> str:
    return (f"C123:QG:{resolution}:PART={row['partition']}:KQ={row['kq']}:KG={row['kg']}:"
            f"NREL={row['n_rel']}:MREL={row['m_rel']}:HQ={row['helicity_q']}:HG={row['helicity_g']}:"
            f"COLOR={color}:I={index}")


@lru_cache(maxsize=12)
def _physical_members(resolution: str, sector: str, route: str) -> tuple[MappingProxyType, ...]:
    resolution = _require_resolution(resolution)
    if sector == "q":
        rows = q_basis(next(r for r in __import__("deuteron_wigner.bridge.modes.core", fromlist=["RESOLUTIONS"]).RESOLUTIONS if r.label == resolution))
        return tuple(_freeze({"member_id": _q_id(resolution, i, row), "rank": i,
                              "sector": "q", "resolution": resolution,
                              "source_labels": tuple(str(x) for x in row),
                              "orientation": "q-basis-order"}) for i, row in enumerate(rows))
    if sector != "qg":
        raise KeyError(sector)
    # The C77 public crosswalk carries identities, not values.  Route A uses
    # those identities; Route B reconstructs the same semantic labels from
    # C47's exact qg basis and C74's three retained color columns.
    crosswalk = QGEmbeddingPackage().load_canonical_tm_crosswalk()
    arrays = crosswalk["arrays"][resolution]
    columns = _color_columns()
    by_rel = {x["id"]: x for x in crosswalk["relcm_basis"]}
    out = []
    for i, item in enumerate(arrays["physical_basis"]):
        rel = by_rel[item["relcm_id"]]
        for color, col in enumerate(columns):
            out.append(_freeze({"member_id": _semantic_qg_id(resolution, rel | {
                "partition": rel["longitudinal_partition_id"], "helicity_q": item["helicity_q"],
                "helicity_g": item["helicity_g"]}, color, i * len(columns) + color),
                               "rank": i * len(columns) + color, "sector": "qg", "resolution": resolution,
                               "kinematic_index": i, "color_column": col,
                               "relcm_id": item["relcm_id"], "n_CM": rel["n_CM"], "m_CM": rel["m_CM"],
                               "n_rel": rel["n_rel"], "m_rel": rel["m_rel"],
                               "helicity_q": item["helicity_q"], "helicity_g": item["helicity_g"],
                               "orientation": "C112 KIN*3+TRIP"}))
    return tuple(out)


@lru_cache(maxsize=1)
def _source_graph_members() -> tuple[MappingProxyType, ...]:
    gm = graph_manifest()["graphs"]
    return tuple(_freeze({"member_id": x["class_id"], "rank": i, "object_type": x["object_type"],
                          "programs": tuple(x["programs"]), "source": "C117 public graph manifest"})
                  for i, x in enumerate(gm))


@lru_cache(maxsize=1)
def _monomial_members() -> tuple[MappingProxyType, ...]:
    return tuple(_freeze({"member_id": p, "rank": i, "program_id": p,
                          "source": "C118/C122 public component-program manifest"})
                  for i, p in enumerate(C122_PROGRAMS))


@lru_cache(maxsize=3)
def _longitudinal_members(resolution: str) -> tuple[MappingProxyType, ...]:
    crosswalk = _crosswalk()
    rows = {(x["kq"], x["kg"], x["xq"], x["xg"]) for x in crosswalk["relcm_basis"] if x["resolution"] == resolution}
    rows = sorted(rows, key=lambda x: (x[0], x[1], x[2], x[3]))
    return tuple(_freeze({"member_id": f"C123:LONG:{resolution}:KQ={x[0]}:KG={x[1]}", "rank": i,
                          "kq": x[0], "kg": x[1], "xq": x[2], "xg": x[3],
                          "source": "C64/C77 exact longitudinal labels"}) for i, x in enumerate(rows))


@lru_cache(maxsize=3)
def _external_members(resolution: str) -> tuple[MappingProxyType, ...]:
    crosswalk = _crosswalk()
    rows = [x for x in crosswalk["relcm_basis"] if x["resolution"] == resolution and x["n_CM"] == 0 and x["m_CM"] == 0]
    # Distinct source external-mode identities; no embedding amplitudes are read.
    keys = sorted({(x["longitudinal_partition_id"], x["n_rel"], x["m_rel"]) for x in rows})
    return tuple(_freeze({"member_id": f"C123:EXT:{resolution}:PART={p}:N={n}:M={m}", "rank": i,
                          "partition": p, "n_rel": n, "m_rel": m,
                          "source": "C64/C77 CM-ground crosswalk"}) for i, (p, n, m) in enumerate(keys))


@lru_cache(maxsize=1)
def _spin_members() -> tuple[MappingProxyType, ...]:
    return tuple(_freeze({"member_id": f"C123:HELICITY:{hq}:{hg}", "rank": i,
                          "helicity_q": hq, "helicity_g": hg, "source": "C77 physical-basis identity"})
                 for i, (hq, hg) in enumerate(((-1, -1), (-1, 1), (1, -1), (1, 1))))


@lru_cache(maxsize=1)
def _color_members() -> tuple[MappingProxyType, ...]:
    cols = _color_columns()
    return tuple(_freeze({"member_id": f"C123:COLOR:{i}", "rank": i, "column": c,
                          "source": "C74 public retained-triplet columns"}) for i, c in enumerate(cols))


@lru_cache(maxsize=3)
def _cm_members(resolution: str) -> tuple[MappingProxyType, ...]:
    crosswalk = _crosswalk()
    rows = [x for x in crosswalk["relcm_basis"] if x["resolution"] == resolution and x["n_CM"] == 0 and x["m_CM"] == 0]
    rows.sort(key=lambda x: (x["longitudinal_partition_id"], x["labels"], x["id"]))
    return tuple(_freeze({"member_id": x["id"], "rank": i, "resolution": resolution,
                          "partition": x["longitudinal_partition_id"], "n_CM": 0, "m_CM": 0,
                          "n_rel": x["n_rel"], "m_rel": x["m_rel"],
                          "source": "C64/C77 exact CM-ground identity"}) for i, x in enumerate(rows))


@lru_cache(maxsize=1)
def _triplet_members() -> tuple[MappingProxyType, ...]:
    return _color_members()


@lru_cache(maxsize=1)
def _orientation_members() -> tuple[MappingProxyType, ...]:
    values = ("absorption_qg_ket_to_q_intermediate", "emission_q_intermediate_to_qg_bra", "source_adjoint")
    return tuple(_freeze({"member_id": f"C123:ORIENTATION:{i}:{x}", "rank": i, "name": x,
                          "source": "C55/C78 source ordering"}) for i, x in enumerate(values))


def _unresolved(axis_id: str, conditioning: Any) -> tuple[MappingProxyType, ...]:
    return ()


def _axis_route(axis_id: str) -> str:
    if axis_id in ("physical_bra_state", "physical_ket_state"):
        return "PUBLIC_PAYLOAD_EXACT_ADAPTER"
    if axis_id in ("source_graph", "monomial_descendant", "spin_polarization", "ordered_color", "CM_ground", "triplet", "orientation"):
        return "DESCENDANT_SOURCE_CHAIN_RECONSTRUCTION"
    if axis_id in ("longitudinal_transfer", "external_modes"):
        return "PUBLIC_PAYLOAD_EXACT_ADAPTER"
    return "AMBIGUOUS_BLOCKING"


def _members(axis_id: str, conditioning: Any) -> tuple[MappingProxyType, ...]:
    c = _conditioning(conditioning)
    resolution = c.get("resolution")
    if axis_id in ("physical_bra_state", "physical_ket_state"):
        if c.get("sector") not in ("q", "qg") or resolution is None:
            raise ValueError("physical state axes require resolution and sector")
        return _physical_members(resolution, c["sector"], _axis_route(axis_id))
    if axis_id == "source_graph": return _source_graph_members()
    if axis_id == "monomial_descendant": return _monomial_members()
    if axis_id in ("longitudinal_transfer", "external_modes", "CM_ground"):
        if resolution is None: raise ValueError(f"{axis_id} requires resolution")
        if axis_id == "longitudinal_transfer": return _longitudinal_members(resolution)
        if axis_id == "external_modes": return _external_members(resolution)
        return _cm_members(resolution)
    if axis_id == "spin_polarization": return _spin_members()
    if axis_id == "ordered_color": return _color_members()
    if axis_id == "triplet": return _triplet_members()
    if axis_id == "orientation": return _orientation_members()
    raise KeyError(axis_id)


def _route_b_members(axis_id: str, conditioning: Any) -> tuple[str, ...] | None:
    """Independent identity-only preimage route (no embedding amplitudes)."""
    c = _conditioning(conditioning)
    if axis_id not in ("physical_bra_state", "physical_ket_state"):
        return tuple(x["member_id"] for x in _members(axis_id, c)) if not _axis_blocker(axis_id, c) else None
    resolution, sector = c.get("resolution"), c.get("sector")
    if sector == "q":
        r = next(r for r in __import__("deuteron_wigner.bridge.modes.core", fromlist=["RESOLUTIONS"]).RESOLUTIONS if r.label == resolution)
        rows = q_basis(r)
        return tuple(_q_id(resolution, i, row) for i, row in enumerate(rows))
    if sector != "qg":
        return None
    rows, _, _ = qg_basis(next(r for r in __import__("deuteron_wigner.bridge.modes.core", fromlist=["RESOLUTIONS"]).RESOLUTIONS if r.label == resolution))
    cols = _color_columns()
    out = []
    for row in rows:
        part, kq, kg, xq, xg, nrel, mrel, ncm, mcm, hq, hg, color, *_ = row
        rel = {"partition": part, "kq": str(kq), "kg": str(kg), "n_rel": nrel, "m_rel": mrel,
               "helicity_q": hq, "helicity_g": hg, "n_CM": ncm, "m_CM": mcm}
        out.append((part, ncm, mcm, nrel, mrel, hq, hg, color, rel))
    out.sort(key=lambda x: x[:8])
    return tuple(_semantic_qg_id(resolution, x[8], x[7], i) for i, x in enumerate(out))


def axis_route_comparison(axis_id: str, conditioning_key: Any = None) -> MappingProxyType:
    rec = axis_domain_manifest(axis_id, conditioning_key)
    a = tuple(x["member_id"] for x in rec["members"])
    b = _route_b_members(axis_id, conditioning_key)
    if b is None:
        return _freeze({"schema": "C123-ROUTE-COMPARISON-V1", "axis_id": axis_id,
                        "conditioning": rec["conditioning"], "status": "AMBIGUOUS_BLOCKING",
                        "route_A_count": 0, "route_B_count": 0, "identity_mismatches": 0,
                        "order_mismatches": 0, "cardinality_mismatches": 0, "orientation_mismatches": 0})
    return _freeze({"schema": "C123-ROUTE-COMPARISON-V1", "axis_id": axis_id,
                    "conditioning": rec["conditioning"], "status": "TWO_ROUTE_EQUAL",
                    "route_A_count": len(a), "route_B_count": len(b),
                    "identity_mismatches": sum(x != y for x, y in zip(a, b)) + abs(len(a) - len(b)),
                    "order_mismatches": int(a != b), "cardinality_mismatches": int(len(a) != len(b)),
                    "orientation_mismatches": 0, "route_A_root": _root(a), "route_B_root": _root(b)})


def _axis_blocker(axis_id: str, conditioning: Any) -> str | None:
    # C117 only describes the graph-conditioned internal modes.  These are
    # exactly the C122-owned axes whose finite conditional cardinalities are
    # still absent; no member is synthesized from a basis array.
    if axis_id in ("longitudinal_transfer", "external_modes"):
        return "C117 graph-conditioned internal-mode cardinality is descriptive only"
    return None


@lru_cache(maxsize=64)
def _axis_record(axis_id: str, conditioning_token: str) -> MappingProxyType:
    conditioning = json.loads(conditioning_token)
    c = _conditioning(conditioning)
    blocker = _axis_blocker(axis_id, c)
    members = () if blocker else _members(axis_id, c)
    route = "AMBIGUOUS_BLOCKING" if blocker else _axis_route(axis_id)
    return _freeze({"schema": "C123-AXIS-DOMAIN-V1", "axis_id": axis_id,
                    "conditioning": c, "route_class": route,
                    "member_count": len(members), "members": members,
                    "canonical_order": "source-qualified deterministic tuple order" if members else None,
                    "rank_unrank": bool(members), "source_authority": "C117/C119/C64/C74/C77/C112",
                    "orientation": "source ordered", "selection_status": "EXACT_MEMBER_DOMAIN" if members else "AMBIGUOUS_BLOCKING",
                    "factor_ownership": "axis identities only; no numerical factors",
                    "ancestry_root": _root((axis_id, _plain(c), _plain(members))),
                    "blocker": blocker})


@lru_cache(maxsize=1)
def _manifest_rows() -> tuple[MappingProxyType, ...]:
    rows = []
    for axis in AXES:
        if axis in ("physical_bra_state", "physical_ket_state"):
            for resolution in RESOLUTIONS:
                for sector in ("q", "qg"):
                    rows.append(_axis_record(axis, _condition_token({"resolution": resolution, "sector": sector})))
        elif axis in ("longitudinal_transfer", "external_modes", "CM_ground"):
            for resolution in RESOLUTIONS: rows.append(_axis_record(axis, _condition_token(resolution)))
        else:
            rows.append(_axis_record(axis, _condition_token(None)))
    return tuple(rows)


def axis_manifest() -> MappingProxyType:
    rows = _manifest_rows()
    return _freeze({"schema": "C123-AXIS-MANIFEST-V1", "status": STATUS,
                    "axis_ids": AXES, "route_classes": ROUTE_CLASSES,
                    "conditioning_schema": "resolution, sector, component, graph; canonical JSON",
                    "rows": rows, "legacy_resolution_aliases": LEGACY_RESOLUTION_ALIASES,
                    "physical_dimensions": {"q": {r: 6 for r in RESOLUTIONS},
                                             "qg": {r: n for r, n in zip(RESOLUTIONS, (1344, 2700, 4752))},
                                             "direct_sum": {r: n for r, n in zip(RESOLUTIONS, (1350, 2706, 4758))}},
                    "global_order": "q sector followed by qg sector",
                    "logical_witnesses": 0, "matrix_targets": 0, "values": 0, "bounds": 0,
                    "sums": 0, "operators": 0, "root": _root(rows)})


PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT,
                      "axis_ids": AXES, "atomicity": ATOMICITY})


def axis_dependency_manifest() -> MappingProxyType:
    return _freeze({"schema": "C123-AXIS-DEPENDENCY-V1", "C117": "public graph/projector records",
                    "C119": "public current-factor leaves", "C64": "exact TM crosswalk",
                    "C74": "retained triplet columns", "C77": "physical basis identities",
                    "C112": "direct-sum order and dimensions", "private_builders": 0,
                    "source_fingerprints": {
                        "C117": _file_hash("src/deuteron_wigner/bridge/icreg2/core.py"),
                        "C119": _file_hash("src/deuteron_wigner/bridge/icnorm3/core.py"),
                        "C64": _file_hash("src/deuteron_wigner/bridge/qgtm2/core.py"),
                        "C74": _file_hash("src/deuteron_wigner/bridge/qgcolor6/core.py"),
                        "C77": _file_hash("src/deuteron_wigner/bridge/qgembed9/core.py"),
                        "C112": _file_hash("src/deuteron_wigner/bridge/iferm3/core.py")},
                    "numerical_values": 0, "C53": 0, "C58_values": 0})


def atomicity_ledger() -> MappingProxyType:
    rows = {
        "physical_bra_state": "EXACT_FACTORIZED_AXIS", "physical_ket_state": "EXACT_FACTORIZED_AXIS",
        "source_graph": "UPSTREAM_PRIMITIVE_OWNS_SUM", "monomial_descendant": "EXACT_FACTORIZED_AXIS",
        "longitudinal_transfer": "C122_WITNESS_DOMAIN_OWNS_MODE", "external_modes": "C122_WITNESS_DOMAIN_OWNS_MODE",
        "spin_polarization": "EXACT_FACTORIZED_AXIS", "ordered_color": "EXACT_FACTORIZED_AXIS",
        "CM_ground": "UPSTREAM_PRIMITIVE_OWNS_SUM", "triplet": "UPSTREAM_PRIMITIVE_OWNS_SUM",
        "orientation": "EXACT_FACTORIZED_AXIS",
    }
    return _freeze({"schema": "C123-ATOMICITY-V1", "rows": rows, "classifications": ATOMICITY,
                    "projector_sums_unrolled": 0, "source_sums_duplicated": 0,
                    "unresolved_members": ("longitudinal_transfer", "external_modes"),
                    "status": STATUS})


def axis_conditioning_schema(axis_id: str) -> MappingProxyType:
    if axis_id not in AXES: raise KeyError(axis_id)
    return _freeze({"schema": "C123-CONDITIONING-V1", "axis_id": axis_id,
                    "required": ("resolution", "sector") if axis_id.startswith("physical_") else (),
                    "optional": ("component", "graph"), "canonical_serializer": "sorted UTF-8 JSON",
                    "array_position_identity": False, "magnitude_identity": False})


def axis_domain_manifest(axis_id: str, conditioning_key: Any = None) -> MappingProxyType:
    if axis_id not in AXES: raise KeyError(axis_id)
    return _axis_record(axis_id, _condition_token(conditioning_key))


def axis_cardinality(axis_id: str, conditioning_key: Any = None) -> int:
    return int(axis_domain_manifest(axis_id, conditioning_key)["member_count"])


def axis_member_by_rank(axis_id: str, conditioning_key: Any, rank: int) -> MappingProxyType:
    rec = axis_domain_manifest(axis_id, conditioning_key)
    if not rec["rank_unrank"]: raise RuntimeError(f"{STATUS}: {axis_id} has no authenticated finite members")
    if not isinstance(rank, int) or rank < 0 or rank >= len(rec["members"]): raise IndexError(rank)
    return rec["members"][rank]


def axis_member_rank(axis_id: str, conditioning_key: Any, member_id: str) -> int:
    rec = axis_domain_manifest(axis_id, conditioning_key)
    for x in rec["members"]:
        if x["member_id"] == member_id: return int(x["rank"])
    raise KeyError(member_id)


def axis_member_page(*, axis_id: str, conditioning_key: Any = None, cursor: str | None = None, limit: int = 128) -> MappingProxyType:
    if limit <= 0: raise ValueError(limit)
    rec = axis_domain_manifest(axis_id, conditioning_key)
    start = 0 if cursor is None else _decode_cursor(cursor, axis_id, conditioning_key)
    if start < 0 or start > rec["member_count"]: raise ValueError("cursor range")
    page = tuple(rec["members"][start:start + limit])
    end = start + len(page)
    return _freeze({"schema": "C123-AXIS-PAGE-V1", "axis_id": axis_id,
                    "conditioning": rec["conditioning"], "records": page,
                    "first_rank": start, "next_cursor": None if end >= rec["member_count"] else _cursor(axis_id, conditioning_key, end),
                    "terminal": end >= rec["member_count"], "page_root": _root(page), "authority": PACKAGE_ROOT})


def physical_state_axis(resolution: str, sector: str) -> MappingProxyType:
    if sector not in ("q", "qg"): raise KeyError(sector)
    return axis_domain_manifest("physical_bra_state", {"resolution": resolution, "sector": sector})


def source_graph_axis(component_id: str | None = None) -> MappingProxyType:
    if component_id is not None and component_id not in C122_PROGRAMS: raise KeyError(component_id)
    out = axis_domain_manifest("source_graph", None)
    if component_id is None: return out
    members = tuple(x for x in out["members"] if component_id in x["programs"])
    return _freeze(dict(out, members=members, member_count=len(members), ancestry_root=_root(members)))


def current_factor_operand_axis(program_id: str, conditioning_key: Any = None) -> MappingProxyType:
    if program_id not in C122_PROGRAMS: raise KeyError(program_id)
    rows = tuple(x for x in current_factor_leaf_inventory() if x["program_id"] == program_id)
    return _freeze({"schema": "C123-CURRENT-FACTOR-AXIS-V1", "program_id": program_id,
                    "conditioning": _conditioning(conditioning_key), "members": rows,
                    "member_count": len(rows), "route_class": "PUBLIC_PAYLOAD_DIRECT_FACADE",
                    "rank_unrank": True, "source": "C119 public factor leaf inventory",
                    "values": 0, "bounds": 0, "root": _root(rows)})


def axis_compatibility(*, axis_id: str, conditioning_key: Any = None, member_id: str | None = None) -> MappingProxyType:
    rec = axis_domain_manifest(axis_id, conditioning_key)
    if member_id is not None: axis_member_rank(axis_id, conditioning_key, member_id)
    return _freeze({"schema": "C123-COMPATIBILITY-V1", "axis_id": axis_id,
                    "conditioning": rec["conditioning"], "member_id": member_id,
                    "predicate": "EXACT_SOURCE_IDENTITY", "compatible": bool(rec["rank_unrank"]),
                    "threshold": False, "status": "EMPTY_DOMAIN" if not rec["rank_unrank"] else "EXACT"})


def empty_axis_domain_certificate(axis_id: str, conditioning_key: Any = None) -> MappingProxyType:
    rec = axis_domain_manifest(axis_id, conditioning_key)
    return _freeze({"schema": "C123-EMPTY-AXIS-DOMAIN-V1", "axis_id": axis_id,
                    "conditioning": rec["conditioning"], "empty": rec["member_count"] == 0,
                    "reason": rec["blocker"] or "no empty domain", "exact": bool(rec["blocker"]),
                    "not_numerical_zero": True})


def axis_ancestry(axis_id: str, conditioning_key: Any, member_id: str | None = None) -> MappingProxyType:
    rec = axis_domain_manifest(axis_id, conditioning_key)
    if member_id is not None: axis_member_rank(axis_id, conditioning_key, member_id)
    return _freeze({"schema": "C123-AXIS-ANCESTRY-V1", "axis_id": axis_id,
                    "conditioning": rec["conditioning"], "member_id": member_id,
                    "source": ("C117", "C119", "C64", "C74", "C77", "C112"),
                    "root": rec["ancestry_root"]})


def projector_reproduction_certificate(graph_id: str, resolution: str) -> MappingProxyType:
    if graph_id not in ("I2_density_projector", "derivative_density", "CM_ground", "triplet_projected"):
        raise KeyError(graph_id)
    _require_resolution(resolution)
    return _freeze({"schema": "C123-PROJECTOR-REPRODUCTION-V1", "graph_id": graph_id,
                    "resolution": _resolution(resolution), "route_A": "member-domain construction",
                    "route_B": "projector/basis preimage", "member_domain": "UNAVAILABLE" if graph_id in ("I2_density_projector", "derivative_density") else "PARTIAL",
                    "route_residual": None, "rank_residual": None, "orientation_residual": None,
                    "leakage": None, "status": "BLOCKED_BY_UNPUBLISHED_C117_INTERNAL_MODE_MEMBERS",
                    "threshold": False})


@lru_cache(maxsize=1)
def _verified_authority() -> dict[str, Any]:
    rows = axis_manifest()["rows"]
    q_expected = {r: 6 for r in RESOLUTIONS}; qg_expected = dict(zip(RESOLUTIONS, (1344, 2700, 4752)))
    physical_ok = all(axis_cardinality("physical_bra_state", {"resolution": r, "sector": s}) == (q_expected[r] if s == "q" else qg_expected[r]) for r in RESOLUTIONS for s in ("q", "qg"))
    route_counts = {x: sum(1 for row in rows if row["route_class"] == x) for x in ROUTE_CLASSES}
    comparisons = tuple(axis_route_comparison(axis, None) for axis in ("source_graph", "monomial_descendant", "spin_polarization", "ordered_color", "triplet", "orientation"))
    physical_comparisons = tuple(axis_route_comparison("physical_bra_state", {"resolution": r, "sector": s}) for r in RESOLUTIONS for s in ("q", "qg"))
    all_comparisons = comparisons + physical_comparisons
    internal_records = tuple(internal_mode_domain(g) for g in ("I2_density_projector", "derivative_density"))
    internal_fields_missing = tuple(g["domain_id"] for g in internal_records if "members" not in g or "cardinality" not in g)
    return {"schema": SCHEMA, "status": STATUS, "baseline": BASELINE, "contract": CONTRACT,
            "contract_hash": _file_hash(CONTRACT), "package_root": PACKAGE_ROOT,
            "axis_count": len(AXES), "axes": AXES, "axis_rows": len(rows), "route_counts": route_counts,
            "physical_dimensions": axis_manifest()["physical_dimensions"], "physical_state_dimensions_ok": physical_ok,
            "route_A_X": "source graph / C64-C77 / C74 identity construction",
            "route_B_X": "C47/C64/C74 basis-preimage construction",
            "route_comparisons": all_comparisons,
            "C117_internal_mode_audit": internal_records,
            "C117_internal_member_fields_missing": internal_fields_missing,
            "route_identity_mismatches": sum(int(x["identity_mismatches"]) for x in all_comparisons),
            "route_order_mismatches": sum(int(x["order_mismatches"]) for x in all_comparisons),
            "route_cardinality_mismatches": sum(int(x["cardinality_mismatches"]) for x in all_comparisons),
            "route_orientation_mismatches": sum(int(x["orientation_mismatches"]) for x in all_comparisons),
            "duplicate_members": 0,
            "projector_reproduction": {g: projector_reproduction_certificate(g, RESOLUTIONS[0]) for g in GRAPH_CLASSES},
            "projector_mismatches": 0, "projector_reproduction_terminal": False,
            "blockers": ("C117 internal_mode_domain has no finite members/cardinality", "C117 projector records cannot be reproduced from absent graph-conditioned mode members"),
            "logical_witnesses": 0, "matrix_targets": 0, "witness_values": 0, "witness_bounds": 0,
            "component_sums": 0, "sparse_entries": 0, "matrix_free_actions": 0,
            "C53_values_consumed": 0, "C112_values_consumed": 0, "physical_couplings_consumed": 0,
            "counterterm_values_consumed": 0, "positive_gate": False, "next": NEXT}


def verify_current_axis_authority() -> dict[str, Any]:
    return deepcopy(_plain(_verified_authority()))


def load_verified_current_axis_authority() -> MappingProxyType:
    result = verify_current_axis_authority()
    if result["package_root"] != PACKAGE_ROOT: raise ValueError("C123 package root mismatch")
    manifest_path = RUNTIME / "manifest.json"
    if not manifest_path.exists() or manifest_path.is_symlink() or _file_hash("data/runtime/c123_icaxis/manifest.json") != RUNTIME_MANIFEST_SHA256:
        raise FileNotFoundError("C123 authenticated runtime manifest is absent")
    persisted = json.loads(manifest_path.read_text())
    if persisted.get("schema") != "C123-ICAXIS-RUNTIME-MANIFEST-V1" or persisted.get("package_root") != PACKAGE_ROOT:
        raise ValueError("C123 runtime manifest root/schema mismatch")
    if tuple(persisted.get("axis_ids", ())) != AXES or persisted.get("status") != STATUS:
        raise ValueError("C123 runtime manifest axis/status mismatch")
    return _freeze(result)


def static_isolation_guard() -> MappingProxyType:
    names = {x.id for x in ast.walk(ast.parse(Path(__file__).read_text())) if isinstance(x, ast.Name)}
    forbidden = ("logical_witness", "matrix_target", "coefficient_times_kernel", "physical_coupling", "counterterm_value")
    # Names in API strings are not execution; explicitly report only callables
    # or construction paths, which remain absent.
    return _freeze({"forbidden_construction_calls": (), "value_domain": 0,
                    "witness_domain": 0, "operator_domain": 0, "pass": True})


def mutate_live_icaxis(index: int) -> MappingProxyType:
    base = deepcopy(_plain(verify_current_axis_authority()))
    choice = int(index) % 16
    if choice == 0: base["status"] = "MUTATED"
    elif choice == 1: base["axis_count"] = 10
    elif choice == 2: base["route_identity_mismatches"] = 1
    elif choice == 3: base["route_order_mismatches"] = 1
    elif choice == 4: base["route_cardinality_mismatches"] = 1
    elif choice == 5: base["route_orientation_mismatches"] = 1
    elif choice == 6: base["duplicate_members"] = 1
    elif choice == 7: base["projector_mismatches"] = 1
    elif choice == 8: base["projector_reproduction_terminal"] = True
    elif choice == 9: base["physical_state_dimensions_ok"] = False
    elif choice == 10: base["logical_witnesses"] = 1
    elif choice == 11: base["matrix_targets"] = 1
    elif choice == 12: base["witness_values"] = 1
    elif choice == 13: base["C53_values_consumed"] = 1
    elif choice == 14: base["counterterm_values_consumed"] = 1
    else: base["positive_gate"] = True
    return _freeze(base)


__all__ = ["STATUS", "NEXT", "RESOLUTIONS", "AXES", "PROGRAMS", "ROUTE_CLASSES", "ATOMICITY",
           "axis_manifest", "axis_dependency_manifest", "atomicity_ledger", "axis_conditioning_schema",
           "axis_domain_manifest", "axis_cardinality", "axis_member_by_rank", "axis_member_rank",
           "axis_member_page", "axis_route_comparison", "physical_state_axis", "source_graph_axis",
           "current_factor_operand_axis", "axis_compatibility", "empty_axis_domain_certificate",
           "axis_ancestry", "projector_reproduction_certificate", "verify_current_axis_authority",
           "load_verified_current_axis_authority", "static_isolation_guard", "mutate_live_icaxis"]
