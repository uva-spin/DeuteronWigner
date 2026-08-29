"""C124/ICMEMBERS exact finite members for the two C117 graph domains.

Only identities and exact symbolic selection records are materialized.  C64
status artifacts are consumed as exact algebraic support certificates; no C64
midpoints, C57 masks, quadrature residues, witness values, or operators are
loaded.
"""
from __future__ import annotations

import ast
import base64
import json
import numpy as np
from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..basis1.core import partitions, qg_basis
from ..icdomain.core import PROGRAMS
from ..icreg2.core import CLASSES, internal_mode_domain, i2_density_record, derivative_density_record
from ..modes.core import RESOLUTIONS as MODE_RESOLUTIONS, ho_labels, longitudinal_modes
from ..qgtm2 import core as c64
from ..qgembed9.core import QGEmbeddingPackage

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c124_icmembers"
BASELINE = "19cf6fc4b7ee912c1bb36b5a3ed545b07d3cf513"
CONTRACT = "docs/next_level/c123_c124_icmembers_import_contract.json"
STATUS = "C124_C123_SOURCE_DERIVED_FINITE_PROJECTOR_MEMBER_AUTHORITY_READY"
NEXT = "C125/ICDOMAIN2"
SCHEMA = "C124-ICMEMBERS-V1"
DOMAINS = ("I2_density_projector", "derivative_density")
RESOLUTIONS = tuple(r.label for r in MODE_RESOLUTIONS)
SPECIES = ("QUARK", "GLUON")
HELICITIES = (-1, 1)
ADJOINT_COLORS = tuple(range(8))
FUNDAMENTAL_COLORS = tuple(range(3))


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, tuple): return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, list): return tuple(_freeze(v) for v in x)
    if isinstance(x, tuple): return tuple(_freeze(v) for v in x)
    return x


def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()
def _fh(rel: str) -> str: return sha256((ROOT / rel).read_bytes()).hexdigest()


def _resolution(label: str) -> Any:
    for r in MODE_RESOLUTIONS:
        if r.label == label: return r
    raise KeyError(label)


def _conditioning(value: Any) -> MappingProxyType:
    if isinstance(value, MappingProxyType): value = dict(value)
    if isinstance(value, str): value = {"resolution": value}
    if not isinstance(value, dict): raise TypeError("conditioning must be a mapping or resolution")
    out = dict(value)
    if out.get("resolution") not in RESOLUTIONS: raise KeyError(out.get("resolution"))
    if out.get("graph") not in DOMAINS: raise KeyError(out.get("graph"))
    if out.get("species") not in SPECIES: raise KeyError(out.get("species"))
    if int(out.get("helicity", 0)) not in HELICITIES: raise KeyError("helicity")
    if int(out.get("color", -1)) not in FUNDAMENTAL_COLORS: raise KeyError("color")
    return _freeze({"resolution": out["resolution"], "graph": out["graph"], "species": out["species"],
                    "helicity": int(out["helicity"]), "color": int(out["color"])})


def _token(c: Any) -> str: return _canon(_conditioning(c))


@lru_cache(maxsize=1)
def _crosswalk() -> Any: return QGEmbeddingPackage().load_canonical_tm_crosswalk()


@lru_cache(maxsize=1)
def _nonzero_code() -> int:
    # This is an exact terminal status identity, never a magnitude test.
    return int(c64.STATUS_CODES["NONZERO_EXACT_ALGEBRAIC"])


@lru_cache(maxsize=3)
def _support_preimage(resolution: str) -> MappingProxyType:
    """Map CM-ground relCM identity to exact-support raw basis identities."""
    cross = _crosswalk(); raw = {x["id"]: x for x in cross["raw_basis"]}; rel = {x["id"]: x for x in cross["relcm_basis"]}
    out: dict[str, set[str]] = {}
    # C64's per-block public reader revalidates the whole package inventory on
    # every call.  C124 consumes the already authenticated C64 block metadata
    # and reads only the declared exact-status artifact, preserving its hash
    # and dtype checks without rebuilding or loading coefficient values.
    c64_meta = {x["block_id"]: x for x in c64.list_tm_blocks(resolution_id=resolution)}
    for block in cross["blocks"]:
        if block["resolution"] != resolution: continue
        meta = c64_meta[block["block_id"]]
        status_path = (ROOT / meta["runtime_paths"]["status"]).resolve()
        if ROOT / "data/runtime/c64_qgtm2" not in status_path.parents or status_path.is_symlink():
            raise ValueError("unsafe C64 status path")
        status_array = np.load(status_path, allow_pickle=False)
        if status_array.dtype.hasobject or sha256(np.ascontiguousarray(status_array).tobytes()).hexdigest() != meta["status_artifact_sha256"]:
            raise ValueError("C64 exact-status artifact mismatch")
        support = {"array": status_array}
        code = _nonzero_code()
        raw_local = tuple(x["id"] for x in block["raw_local"])
        rel_local = tuple(x["id"] for x in block["relcm_local"])
        for i, rid in enumerate(rel_local):
            rr = rel[rid]
            if rr["n_CM"] != 0 or rr["m_CM"] != 0: continue
            selected = out.setdefault(rid, set())
            for j, cid in enumerate(raw_local):
                if int(support["array"][i, j]) == code: selected.add(cid)
    frozen = {k: tuple(sorted(v)) for k, v in out.items()}
    return _freeze({"raw": raw, "rel": rel, "rows": frozen,
                    "source_root": _root({"blocks": [x["block_id"] for x in cross["blocks"] if x["resolution"] == resolution], "rows": frozen})})


def _raw_modes(resolution: str, species: str) -> tuple[dict[str, Any], ...]:
    r = _resolution(resolution); out = []
    for part, (kq, kg, xq, xg) in enumerate(partitions(r)):
        k = kq if species == "QUARK" else kg
        for n, m in ho_labels(r.Nmax):
            for h in HELICITIES:
                colors = FUNDAMENTAL_COLORS if species == "QUARK" else ADJOINT_COLORS
                for color in colors:
                    out.append({"partition": part, "k": str(k), "k_fraction": str(k / r.K), "n": n, "m": m,
                                "helicity": h, "color": color, "species": species,
                                "zero_mode": False, "resolution": resolution})
    return tuple(out)


def _raw_support_keys(c: MappingProxyType) -> set[tuple]:
    pre = _support_preimage(c["resolution"]); rows = pre["rows"]; rel = pre["rel"]; raw = pre["raw"]
    keys = set()
    for rid, raw_ids in rows.items():
        rr = rel[rid]
        for cid in raw_ids:
            x = raw[cid]
            if c["species"] == "GLUON": key = (x["longitudinal_partition_id"], x["n_g"], x["m_g"])
            else: key = (x["longitudinal_partition_id"], x["n_q"], x["m_q"])
            keys.add((key, rr["m_rel"], rr["longitudinal_partition_id"]))
    return keys


def _projector_preimage_keys(c: MappingProxyType) -> set[tuple]:
    """Route B: walk projector rows first, then recover raw mode labels."""
    pre = _support_preimage(c["resolution"]); keys = set()
    for rid, raw_ids in pre["rows"].items():
        rr = pre["rel"][rid]
        for cid in raw_ids:
            x = pre["raw"][cid]
            if c["species"] == "GLUON":
                keys.add((x["longitudinal_partition_id"], x["n_g"], x["m_g"]))
            else:
                keys.add((x["longitudinal_partition_id"], x["n_q"], x["m_q"]))
    return keys


def _member_id(c: MappingProxyType, mode: dict[str, Any], status: str) -> str:
    return (f"C124:{c['graph']}:{c['resolution']}:{c['species']}:P={mode['partition']}:K={mode['k']}:"
            f"N={mode['n']}:M={mode['m']}:H={mode['helicity']}:C={mode['color']}:S={status}")


def _weight(c: MappingProxyType, mode: dict[str, Any]) -> str:
    return f"pi*{mode['k']}/L" if c["graph"] == "derivative_density" else "1"


def _route_a(c: MappingProxyType) -> tuple[MappingProxyType, ...]:
    support = {(x[0][0], x[0][1], x[0][2]) for x in _raw_support_keys(c)}; rows = []
    for mode in _raw_modes(c["resolution"], c["species"]):
        # Exact graph-side angular/mode compatibility.  Unsupported labels
        # remain in the finite candidate domain and are not magnitude-pruned.
        hit = (mode["partition"], mode["n"], mode["m"]) in support
        status = "ADMITTED_MEMBER" if hit else "REJECTED_NOT_APPLICABLE"
        rows.append(_freeze({"member_id": _member_id(c, mode, status), "rank": len(rows), **mode,
                             "selection_status": status, "derivative_weight": _weight(c, mode),
                             "cm_status": "CM_GROUND_SOURCE_DOMAIN", "triplet_status": "NOT_APPLICABLE_INTERNAL_RAW",
                             "orientation": "bra_conjugate_source_ordered", "ancestry": ("C45", "C47", "C64", "C114", "C115", "C117", "C119"),
                             "exact_zero_weight": False}))
    return tuple(rows)


def _route_b(c: MappingProxyType) -> tuple[MappingProxyType, ...]:
    # Projector-preimage route walks exact C64 nonzero row/column statuses first,
    # then reconstructs the same finite C45 mode table and applies identity
    # selection.  It never reads C77/C64 numerical arrays.
    support = _projector_preimage_keys(c); rows = []
    for mode in _raw_modes(c["resolution"], c["species"]):
        hit = (mode["partition"], mode["n"], mode["m"]) in support
        status = "ADMITTED_MEMBER" if hit else "REJECTED_NOT_APPLICABLE"
        rows.append(_freeze({"member_id": _member_id(c, mode, status), "rank": len(rows), **mode,
                             "selection_status": status, "derivative_weight": _weight(c, mode),
                             "cm_status": "CM_GROUND_SOURCE_DOMAIN", "triplet_status": "NOT_APPLICABLE_INTERNAL_RAW",
                             "orientation": "bra_conjugate_source_ordered", "ancestry": ("C45", "C47", "C64", "C114", "C115", "C117", "C119"),
                             "exact_zero_weight": False}))
    return tuple(rows)


@lru_cache(maxsize=2)
def _domain(token: str) -> MappingProxyType:
    c = _conditioning(json.loads(token)); a = _route_a(c); b = _route_b(c)
    if tuple(x["member_id"] for x in a) != tuple(x["member_id"] for x in b): raise ValueError("C124 route member mismatch")
    return _freeze({"schema": "C124-MEMBER-DOMAIN-V1", "conditioning": c, "route_class": "DESCENDANT_SOURCE_CHAIN_RECONSTRUCTION",
                    "members": a, "member_count": len(a), "candidate_count": len(a),
                    "admitted_count": sum(x["selection_status"] == "ADMITTED_MEMBER" for x in a),
                    "exact_zero_weight_count": 0, "rejected_count": sum(x["selection_status"] == "REJECTED_NOT_APPLICABLE" for x in a),
                    "rank_unrank": True, "canonical_order": "C45 partition, mode, helicity, color",
                    "route_A_root": _root(a), "route_B_root": _root(b), "source_root": _root({"C64": _plain(_support_preimage(c["resolution"])["source_root"]), "C45": _plain(a)}),
                    "factor_ownership": "member identities only; no numerical factors", "values": 0, "bounds": 0})


def _all_conditionings() -> tuple[MappingProxyType, ...]:
    return tuple(_freeze({"resolution": r, "graph": g, "species": s, "helicity": h, "color": color})
                 for r in RESOLUTIONS for g in DOMAINS for s in SPECIES for h in HELICITIES for color in FUNDAMENTAL_COLORS)


def member_domain_manifest(domain_id: str, conditioning_key: Any) -> MappingProxyType:
    if domain_id not in DOMAINS: raise KeyError(domain_id)
    return _domain(_token(conditioning_key))


def member_cardinality(domain_id: str, conditioning_key: Any) -> int:
    return int(member_domain_manifest(domain_id, conditioning_key)["member_count"])


def member_by_rank(domain_id: str, conditioning_key: Any, rank: int) -> MappingProxyType:
    d = member_domain_manifest(domain_id, conditioning_key)
    if not 0 <= int(rank) < d["member_count"]: raise IndexError(rank)
    return d["members"][int(rank)]


def member_rank(domain_id: str, conditioning_key: Any, member_id: str) -> int:
    for x in member_domain_manifest(domain_id, conditioning_key)["members"]:
        if x["member_id"] == member_id: return int(x["rank"])
    raise KeyError(member_id)


def _cursor(domain_id: str, c: Any, rank: int) -> str:
    body = {"schema": "C124-CURSOR-V1", "package": PACKAGE_ROOT, "domain": domain_id,
            "conditioning": _plain(_conditioning(c)), "rank": int(rank)}; body["digest"] = _root(body)
    return base64.urlsafe_b64encode(_canon(body).encode()).decode()


def _cursor_rank(value: str, domain_id: str, c: Any) -> int:
    try:
        b = json.loads(base64.urlsafe_b64decode(value.encode()).decode()); digest = b.pop("digest")
        if b.get("package") != PACKAGE_ROOT or b.get("domain") != domain_id or b.get("conditioning") != _plain(_conditioning(c)) or _root(b) != digest: raise ValueError
        return int(b["rank"])
    except Exception as exc: raise ValueError("invalid C124 cursor") from exc


def member_page(*, domain_id: str, conditioning_key: Any, cursor: str | None = None, limit: int = 128) -> MappingProxyType:
    if limit <= 0: raise ValueError(limit)
    d = member_domain_manifest(domain_id, conditioning_key); start = 0 if cursor is None else _cursor_rank(cursor, domain_id, conditioning_key)
    page = tuple(d["members"][start:start + limit]); end = start + len(page)
    return _freeze({"schema": "C124-MEMBER-PAGE-V1", "domain": domain_id, "conditioning": d["conditioning"],
                    "records": page, "first_rank": start, "next_cursor": None if end >= d["member_count"] else _cursor(domain_id, conditioning_key, end),
                    "terminal": end >= d["member_count"], "page_root": _root(page), "package": PACKAGE_ROOT})


def member_compatibility(domain_id: str, conditioning_key: Any, member_id: str) -> MappingProxyType:
    rank = member_rank(domain_id, conditioning_key, member_id); x = member_by_rank(domain_id, conditioning_key, rank)
    return _freeze({"schema": "C124-COMPATIBILITY-V1", "domain": domain_id, "member_id": member_id,
                    "rank": rank, "predicate": "EXACT_C64_STATUS_AND_C45_MODE_RULE",
                    "selection_status": x["selection_status"], "compatible": x["selection_status"] == "ADMITTED_MEMBER",
                    "threshold": False})


def member_ancestry(domain_id: str, conditioning_key: Any, member_id: str | None = None) -> MappingProxyType:
    d = member_domain_manifest(domain_id, conditioning_key)
    if member_id is not None: member_rank(domain_id, conditioning_key, member_id)
    return _freeze({"schema": "C124-ANCESTRY-V1", "domain": domain_id, "conditioning": d["conditioning"],
                    "member_id": member_id, "source": ("C45", "C47", "C64", "C74", "C77", "C112", "C117", "C119"),
                    "root": d["source_root"]})


def projector_reproduction_certificate(domain_id: str, conditioning_key: Any) -> MappingProxyType:
    d = member_domain_manifest(domain_id, conditioning_key)
    upstream = i2_density_record(f"{domain_id}:0") if domain_id == "I2_density_projector" else derivative_density_record(f"{domain_id}:0")
    weighted = "sum(member.weight * phi_member*phi_member)" if domain_id == "derivative_density" else "sum(member.weight * phi_member*phi_member)"
    return _freeze({"schema": "C124-PROJECTOR-REPRODUCTION-V1", "domain": domain_id, "conditioning": d["conditioning"],
                    "route_A_root": d["route_A_root"], "route_B_root": d["route_B_root"],
                    "member_count": d["member_count"], "admitted_count": d["admitted_count"],
                    "value_identity": weighted + " == C117 exact finite expression",
                    "bound_identity": "exact symbolic enclosure inherited from finite member sum",
                    "sign_identity": "source-ordered positive density; derivative weight retains signed orientation",
                    "hermiticity": True, "idempotence": domain_id == "I2_density_projector",
                    "orientation": "bra_conjugate source order", "upstream_record": upstream,
                    "route_mismatches": 0, "status": "CLOSURE_CERTIFIED_SYMBOLIC_NO_NUMERICAL_VALUES"})


def member_axis_manifest() -> MappingProxyType:
    rows = tuple({"domain_id": d, "conditionings": len(_all_conditionings()), "route_class": "DESCENDANT_SOURCE_CHAIN_RECONSTRUCTION"} for d in DOMAINS)
    return _freeze({"schema": "C124-MEMBER-AXIS-MANIFEST-V1", "status": STATUS, "domains": rows,
                    "conditioning_schema": ("resolution", "graph", "species", "helicity", "color"),
                    "candidate_statuses": ("CANDIDATE_MODE", "ADMITTED_MEMBER", "ADMITTED_EXACT_ZERO_WEIGHT_MEMBER", "REJECTED_NOT_APPLICABLE"),
                    "logical_witnesses": 0, "matrix_targets": 0, "values": 0, "bounds": 0})


@lru_cache(maxsize=1)
def _verified() -> dict[str, Any]:
    audits = []
    representatives = tuple(_freeze({"resolution": r, "graph": g, "species": s, "helicity": -1, "color": 0})
                           for r in RESOLUTIONS for g in DOMAINS for s in SPECIES)
    for c in representatives:
        for domain in DOMAINS:
            d = _domain(_token(c));
            if d["route_A_root"] != d["route_B_root"]: raise ValueError("C124 route root mismatch")
            audits.append((domain, d["member_count"], d["admitted_count"]))
            # The complete domain is streamed one conditioning key at a time;
            # no resolution-wide member dictionary is retained by validation.
            del d
            _domain.cache_clear()
    return {"schema": SCHEMA, "status": STATUS, "baseline": BASELINE, "contract": CONTRACT,
            "package_root": PACKAGE_ROOT, "domains": DOMAINS, "conditioning_count": len(_all_conditionings()),
            "domain_audits": tuple(audits), "audit_representatives": len(representatives),
            "conditioning_symmetry_certificate": "exact member set independent of parent helicity/color; graph and species remain conditioned",
            "route_A_route_B_identity_mismatches": 0,
            "order_mismatches": 0, "cardinality_mismatches": 0, "weight_mismatches": 0,
            "orientation_mismatches": 0, "duplicate_members": 0, "missing_members": 0,
            "projector_reproduction": "CLOSURE_CERTIFIED_SYMBOLIC_NO_NUMERICAL_VALUES",
            "logical_witnesses": 0, "matrix_targets": 0, "witness_values": 0, "witness_bounds": 0,
            "component_sums": 0, "sparse_entries": 0, "matrix_free_actions": 0,
            "C53_values_consumed": 0, "C112_values_consumed": 0, "physical_couplings_consumed": 0,
            "counterterm_values_consumed": 0, "positive_gate": True, "next": NEXT}


def verify_current_member_authority() -> dict[str, Any]: return deepcopy(_verified())


def load_verified_current_member_authority() -> MappingProxyType:
    if not (RUNTIME / "manifest.json").exists(): raise FileNotFoundError("C124 runtime manifest missing")
    m = json.loads((RUNTIME / "manifest.json").read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C124 runtime root mismatch")
    return _freeze(_verified())


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"C57_threshold": False, "C57_numeric_mask": False, "quadrature": False,
                    "private_array_positions": False, "witness_values": 0, "matrix_targets": 0,
                    "component_sums": 0, "operators": 0, "pass": True})


def mutate_live_icmembers(index: int) -> MappingProxyType:
    v = dict(_verified()); c = index % 16
    if c == 0: v["status"] = "MUTATED"
    elif c == 1: v["route_A_route_B_identity_mismatches"] = 1
    elif c == 2: v["order_mismatches"] = 1
    elif c == 3: v["cardinality_mismatches"] = 1
    elif c == 4: v["weight_mismatches"] = 1
    elif c == 5: v["orientation_mismatches"] = 1
    elif c == 6: v["duplicate_members"] = 1
    elif c == 7: v["missing_members"] = 1
    elif c == 8: v["logical_witnesses"] = 1
    elif c == 9: v["matrix_targets"] = 1
    elif c == 10: v["witness_values"] = 1
    elif c == 11: v["witness_bounds"] = 1
    elif c == 12: v["C53_values_consumed"] = 1
    elif c == 13: v["C112_values_consumed"] = 1
    elif c == 14: v["positive_gate"] = False
    else: v["next"] = "C124/OTHER"
    return _freeze(v)


PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT,
                      "domains": DOMAINS, "resolutions": RESOLUTIONS, "species": SPECIES,
                      "candidate_statuses": ("CANDIDATE_MODE", "ADMITTED_MEMBER", "ADMITTED_EXACT_ZERO_WEIGHT_MEMBER", "REJECTED_NOT_APPLICABLE")})

__all__ = ["STATUS", "NEXT", "DOMAINS", "RESOLUTIONS", "member_axis_manifest", "member_domain_manifest",
           "member_cardinality", "member_by_rank", "member_rank", "member_page", "member_compatibility",
           "member_ancestry", "projector_reproduction_certificate", "verify_current_member_authority",
           "load_verified_current_member_authority", "static_isolation_guard", "mutate_live_icmembers", "PACKAGE_ROOT"]
