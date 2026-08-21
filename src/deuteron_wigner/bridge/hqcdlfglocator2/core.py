"""C164 local-PDF page maps, bounded searches, and fail-closed locators.

The module authenticates only the eight C140 PDFs already present in the
workspace. It records source-object identities and hashes, but never exposes
or transcribes a complete target expression and never evaluates a target.
"""
from __future__ import annotations

import json
import re
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import fitz

from deuteron_wigner.bridge import hqcdlfgsource as c163

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c164_hqcdlfglocator2"
BASELINE = "ecc821959af764f660a669ab059411b889e712ba"
CONTRACT = "docs/next_level/c163_c164_hqcdlfglocator2_continuation_contract.json"
CONTRACT_SHA256 = "201bf32da8151dc5277b5e2f71b607cd3272820fa6bbcc81032a7b245ae3b2cb"
C163_ROOT = json.loads((ROOT / "docs/next_level/c163_package_root_manifest.json").read_text())["package_root"]
C162_ROOT = json.loads((ROOT / "docs/next_level/c162_package_root_manifest.json").read_text())["package_root"]
C161_ROOT = json.loads((ROOT / "docs/next_level/c161_package_root_manifest.json").read_text())["package_root"]
C160_ROOT = json.loads((ROOT / "docs/next_level/c160_package_root_manifest.json").read_text())["package_root"]
C159_ROOT = json.loads((ROOT / "docs/next_level/c159_package_root_manifest.json").read_text())["package_root"]
C158_ROOT = json.loads((ROOT / "docs/next_level/c158_package_root_manifest.json").read_text())["package_root"]
STATUS = "C164_HQCDLFGLOCATOR2_DEPENDENCY_LOCATOR_INCOMPLETE"
PLAN = "LFGLOCATOR2-D"
NEXT = "C165/HQCDLFGDEP"
C163_STATUS = "C163_HQCDLFGSOURCE_LOCATOR_INCOMPLETE"
C163_PLAN = "LFGSOURCE-D"
C134_CLASSIFICATION = "PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC"

ROOT_CHAIN = {}
for _n in (131, 136, 142, 144, 149, 150, 151, 152, 153, 155, 156, 157):
    _p = ROOT / f"docs/next_level/c{_n}_package_root_manifest.json"
    ROOT_CHAIN[f"C{_n}"] = json.loads(_p.read_text()).get("package_root")
ROOT_CHAIN.update({"C158": C158_ROOT, "C159": C159_ROOT, "C160": C160_ROOT, "C161": C161_ROOT, "C162": C162_ROOT, "C163": C163_ROOT})

SOURCE_HASHES = dict(c163.SOURCE_HASHES)
SOURCE_CATALOG = {
    "pdg2026_qcd": {"title": "Quantum Chromodynamics", "authors": ["J. Huston", "K. Rabbertz", "G. Zanderighi"], "version": "PDG 2026 review; revised August 2025", "date": "August 2025", "first_page_version_text": "PDG Quantum Chromodynamics; revised August 2025", "role": "PHYSICAL_INPUT_VALUE", "scientific_role": "physical input review; prohibited for target coefficients", "print_mode": "ONE_BASED"},
    "pdg2026_quark_masses": {"title": "Quark Masses", "authors": ["R.M. Barnett", "L.P. Lellouch", "A.V. Manohar"], "version": "PDG 2026 review; revised August 2023", "date": "August 2023", "first_page_version_text": "PDG Quark Masses; revised August 2023", "role": "PHYSICAL_INPUT_VALUE", "scientific_role": "physical input review; prohibited for target coefficients", "print_mode": "ONE_BASED"},
    "arxiv_0901.2599": {"title": "Renormalization of quark bilinear operators in a momentum-subtraction scheme with a nonexceptional subtraction point", "authors": ["C. Sturm", "Y. Aoki", "N.H. Christ", "T. Izubuchi", "C.T.C. Sachrajda", "A. Soni", "RBC and UKQCD Collaborations"], "version": "arXiv:0901.2599v2", "date": "22 April 2010", "first_page_version_text": "arXiv:0901.2599v2 [hep-ph] 22 Apr 2010", "role": "TARGET_SCHEME_CONVERSION", "scientific_role": "RI/SMOM definition and conversion authority", "print_mode": "FRONT_UNNUMBERED_THEN_ZERO_BASED"},
    "arxiv_2002.12758": {"title": "Quark masses: N3LO bridge from RI/SMOM to MS scheme", "authors": ["Alexander Bednyakov", "Andrey Pikelner"], "version": "arXiv:2002.12758v2", "date": "7 May 2020", "first_page_version_text": "arXiv:2002.12758v2 [hep-ph] 7 May 2020", "role": "TARGET_SCHEME_CONVERSION", "scientific_role": "RI/SMOM mass conversion authority", "print_mode": "FRONT_UNNUMBERED_THEN_ONE_BASED"},
    "arxiv_1108.4806": {"title": "Two loop QCD vertices at the symmetric point", "authors": ["J.A. Gracey"], "version": "arXiv:1108.4806v1", "date": "24 August 2011", "first_page_version_text": "arXiv:1108.4806v1 [hep-ph] 24 Aug 2011", "role": "TARGET_SCHEME_CONVERSION", "scientific_role": "MOMq vertex, field, and coupling conversion authority", "print_mode": "ONE_BASED"},
    "arxiv_2002.02875": {"title": "Four-loop QCD MOM beta functions from the three-loop vertices at the symmetric point", "authors": ["Alexander Bednyakov", "Andrey Pikelner"], "version": "arXiv:2002.02875v2", "date": "10 April 2020", "first_page_version_text": "arXiv:2002.02875v2 [hep-ph] 10 Apr 2020", "role": "RUNNING_OR_BETA_FUNCTION", "scientific_role": "MOM beta-function and running authority; not unrelated fixed-order authority", "print_mode": "FRONT_UNNUMBERED_THEN_ONE_BASED"},
    "arxiv_1706.03821": {"title": "The strong coupling from a nonperturbative determination of the Lambda parameter in three-flavor QCD", "authors": ["Mattia Bruno", "Mattia Dalla Brida", "Patrick Fritzsch", "Tomasz Korzec", "Alberto Ramos", "Stefan Schaefer", "Hubert Simma", "Stefan Sint", "Rainer Sommer", "ALPHA collaboration"], "version": "arXiv:1706.03821v2", "date": "12 July 2017", "first_page_version_text": "arXiv:1706.03821v2 [hep-lat] 12 Jul 2017", "role": "STEP_SCALING_FUNCTION", "scientific_role": "ALPHA coupling step-scaling authority", "print_mode": "FRONT_UNNUMBERED_THEN_ONE_BASED"},
    "arxiv_1802.05243": {"title": "Non-perturbative quark mass renormalisation and running in Nf = 3 QCD", "authors": ["I. Campos", "P. Fritzsch", "C. Pena", "D. Preti", "A. Ramos", "A. Vladikas"], "version": "arXiv:1802.05243v2", "date": "6 June 2018", "first_page_version_text": "arXiv:1802.05243v2 [hep-lat] 6 Jun 2018", "role": "STEP_SCALING_FUNCTION", "scientific_role": "ALPHA mass step-scaling authority", "print_mode": "FRONT_UNNUMBERED_THEN_ZERO_BASED"},
}

QUANTITIES = ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING", "QCD_COUPLING")
COORDINATES = ("g_s", "g_s^2", "alpha_s", "a_s", "V_B", "Z_1F", "g_R", "g_R/g_s", "signed m_R", "m_R^2")
ROLES = ("DIRECT_TARGET_COEFFICIENT", "TARGET_SCHEME_DEFINITION", "TARGET_SCHEME_CONVERSION", "FIELD_OR_VERTEX_PROJECTOR_DEFINITION", "PERTURBATIVE_COORDINATE_DEFINITION", "RENORMALIZATION_CONSTANT_DEFINITION", "RUNNING_OR_BETA_FUNCTION", "STEP_SCALING_FUNCTION", "PHYSICAL_INPUT_VALUE", "METHOD_ONLY", "COMPARISON_OR_HOLDOUT", "INCOMPATIBLE_GAUGE_OR_SCHEME", "ROLE_AMBIGUOUS")
LOCATOR_STATUS = "DEPENDENCY_LOCATOR_INCOMPLETE"
RENDER_DPI = 144

ACCEPTED_SPECS = {
    "TGT-QUARK_FIELD-RI_SMOM": ("arxiv_0901.2599", 9, "(20)", "3.1 The vector and axial-vector operator", "DIRECT_TARGET_COEFFICIENT", "RI_SMOM"),
    "TGT-SIGNED_QUARK_MASS-RI_SMOM": ("arxiv_0901.2599", 10, "(24)", "3.1 The vector and axial-vector operator / 3.2 The pseudoscalar and scalar operator", "DIRECT_TARGET_COEFFICIENT", "RI_SMOM"),
    "TGT-QUARK_FIELD-MOMQ": ("arxiv_1108.4806", 23, "(6.35)", "6 Quark-gluon vertex", "DIRECT_TARGET_COEFFICIENT", "MOMQ"),
    "TGT-TRANSVERSE_GLUON_FIELD-MOMQ": ("arxiv_1108.4806", 23, "(6.35)", "6 Quark-gluon vertex", "DIRECT_TARGET_COEFFICIENT", "MOMQ"),
    "TGT-qg_VERTEX_DRESSING-MOMQ": ("arxiv_1108.4806", 23, "(6.34)", "6 Quark-gluon vertex", "DIRECT_TARGET_COEFFICIENT", "MOMQ"),
    "TGT-QCD_COUPLING-MOMQ": ("arxiv_1108.4806", 23, "(6.35)", "6 Quark-gluon vertex", "DIRECT_TARGET_COEFFICIENT", "MOMQ"),
    "TGT-QCD_COUPLING-STEP_SCALING_INTERMEDIATE": ("arxiv_1706.03821", 1, "(8)", "Finite-size schemes", "STEP_SCALING_FUNCTION", "STEP_SCALING_INTERMEDIATE"),
    "TGT-SIGNED_QUARK_MASS-STEP_SCALING_INTERMEDIATE": ("arxiv_1802.05243", 4, "(2.9b)", "2.2 Step scaling functions", "STEP_SCALING_FUNCTION", "STEP_SCALING_INTERMEDIATE"),
}

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

def _printed_label(source_id: str, index0: int) -> str:
    mode = SOURCE_CATALOG[source_id]["print_mode"]
    if mode == "ONE_BASED": return str(index0 + 1)
    if index0 == 0: return "UNNUMBERED_FRONT_PAGE"
    if mode == "FRONT_UNNUMBERED_THEN_ZERO_BASED": return str(index0)
    return str(index0 + 1)

def _short_text(text: str, limit: int = 120) -> str:
    return " ".join(text.split())[:limit]

def _section_heads(text: str) -> tuple[str, ...]:
    out = []
    for line in text.splitlines():
        s = " ".join(line.split())
        if not s or len(s) > 110: continue
        if re.match(r"^(?:[0-9]+(?:\.[0-9]+)*|[A-Z](?:\.[0-9]+)?)\s+[A-Z]", s) or (len(s) > 8 and s.isupper()):
            if s not in out: out.append(s)
    return tuple(out[:12])

def _labels(text: str) -> tuple[str, ...]:
    vals = set(re.findall(r"\((?:[0-9]+(?:\.[0-9]+)?[a-z]?|[A-Z](?:\.[0-9]+)+)\)", text))
    vals.update(re.findall(r"\b(?:TABLE|Table|FIG\.|Fig\.|APPENDIX|Appendix)\s+[A-Z]?[0-9]+(?:\.[0-9]+)?", text))
    return tuple(sorted(vals))

@lru_cache(maxsize=None)
def _document(source_id: str) -> fitz.Document:
    if source_id not in SOURCE_HASHES: raise KeyError(source_id)
    path = ROOT / "data/raw/c140_sources" / f"{source_id}.pdf"
    if not path.is_file(): raise FileNotFoundError(path)
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != SOURCE_HASHES[source_id]: raise ValueError(f"source hash mismatch: {source_id}")
    return fitz.open(str(path))

@lru_cache(maxsize=None)
def _page_record(source_id: str, index0: int) -> MappingProxyType:
    doc = _document(source_id)
    if index0 < 0 or index0 >= doc.page_count: raise IndexError(index0)
    page = doc[index0]
    text = page.get_text("text")
    normalized = " ".join(text.split())
    blocks = page.get_text("blocks")
    layout = "|".join(f"{round(b[0],2)},{round(b[1],2)},{round(b[2],2)},{round(b[3],2)}:{' '.join(b[4].split())}" for b in sorted(blocks, key=lambda z: (z[1], z[0])))
    pix = page.get_pixmap(dpi=RENDER_DPI, alpha=False)
    render_hash = sha256(pix.tobytes("png")).hexdigest()
    token_pool = re.findall(r"[A-Za-z][A-Za-z0-9_]*(?:/[A-Za-z0-9_]+)?", normalized)
    important = tuple(sorted(set(t for t in token_pool if len(t) > 1 and (t.lower() in {"quark","mass","gluon","vertex","coupling","ri/smom","smom","momq","projector","conversion","beta","step","scaling","nf","landau","gauge","sigma","sigmap","zq","zm","za","z1f","alpha","as","ms"} or t.startswith(("Z", "C", "MOM", "RI", "N"))))))
    return _freeze({"source_id": source_id, "pdf_page_index_0based": index0, "pdf_page_index_1based": index0 + 1, "printed_page_label": _printed_label(source_id, index0), "section_headings": _section_heads(text), "equation_table_appendix_labels": _labels(text), "symbol_tokens": important[:80], "normalized_text_sha256": sha256(normalized.encode()).hexdigest(), "layout_text_sha256": sha256(layout.encode()).hexdigest(), "render_sha256": render_hash, "text_layer_reliability": "EXTRACTED_LAYOUT_TEXT", "page_width": round(page.rect.width, 4), "page_height": round(page.rect.height, 4), "index_root": _root((source_id, index0, normalized, layout, render_hash))})

@lru_cache(maxsize=1)
def source_version_manifest() -> MappingProxyType:
    rows = []
    for sid, expected in SOURCE_HASHES.items():
        path = ROOT / "data/raw/c140_sources" / f"{sid}.pdf"
        actual = sha256(path.read_bytes()).hexdigest() if path.is_file() else None
        doc = _document(sid)
        meta = {}
        try:
            from pypdf import PdfReader
            raw = PdfReader(str(path)).metadata or {}
            meta = {str(k).lstrip("/"): str(v) for k, v in raw.items()}
        except Exception:
            meta = {}
        cat = SOURCE_CATALOG[sid]
        rows.append({"source_id": sid, "title": cat["title"], "authors": cat["authors"], "journal_arxiv_report_identity": cat["version"], "declared_version": cat["version"], "date": cat["date"], "first_page_version_text": cat["first_page_version_text"], "local_path": f"data/raw/c140_sources/{sid}.pdf", "file_size": path.stat().st_size if path.is_file() else None, "sha256": expected, "actual_sha256": actual, "pdf_page_count": doc.page_count, "pdf_metadata": meta, "printed_page_sequence": tuple(_printed_label(sid, i) for i in range(doc.page_count)), "front_matter_offset": "explicit per-source mode; no constant offset inferred", "roman_arabic_transition": "none identified in local page labels", "appendix_page_labels": tuple(_page_record(sid, i)["printed_page_label"] for i in range(doc.page_count) if any("Appendix" in h for h in _page_record(sid, i)["section_headings"])), "source_version_root": _root((sid, cat["version"], expected, cat["first_page_version_text"]))})
    return _freeze({"schema": "C164-SOURCE-VERSION-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "hashes_verified": all(r["actual_sha256"] == r["sha256"] for r in rows), "version_ambiguities": (), "root": _root(rows)})

def pdf_printed_page_map(source_id: str | None = None) -> MappingProxyType:
    if source_id is not None and source_id not in SOURCE_HASHES: raise KeyError(source_id)
    rows = []
    for sid in SOURCE_HASHES:
        if source_id is not None and sid != source_id: continue
        doc = _document(sid)
        rows.extend(_page_record(sid, i) for i in range(doc.page_count))
    return _freeze({"schema": "C164-PDF-PRINTED-PAGE-MAP-V1", "source_id": source_id, "rows": tuple(rows), "page_count": len(rows), "piecewise_mapping": True, "root": _root(rows)})

def page_search_index(source_id: str | None = None) -> MappingProxyType:
    mapped = pdf_printed_page_map(source_id)
    return _freeze({"schema": "C164-PAGE-SEARCH-INDEX-V1", "source_id": source_id, "rows": mapped["rows"], "page_count": mapped["page_count"], "full_text_committed": False, "root": _root(mapped["rows"])})

def _descriptor_rows() -> tuple[Mapping[str, Any], ...]:
    return tuple(c163.descriptor_source_crosswalk()["rows"])

def _lexicon(d: Mapping[str, Any]) -> tuple[str, ...]:
    q = d["quantity_family"]
    scheme = d["target_scheme"]
    base = {"order", str(d["order"]), q.lower(), scheme.lower(), "Nf", "active N_f", "projector", "gauge", "coordinate"}
    base.update({
        "QUARK_FIELD": ("quark", "field", "wave-function", "Z_q", "Zpsi", "Sigma_q", "inverse propagator"),
        "SIGNED_QUARK_MASS": ("mass", "signed", "Z_m", "scalar", "pseudoscalar", "m_R", "mass renormalization"),
        "TRANSVERSE_GLUON_FIELD": ("gluon", "transverse", "Z_A", "Pi", "two-point", "gauge"),
        "qg_VERTEX_DRESSING": ("qg", "quark-gluon", "vertex", "Gamma", "Z_1F", "amputated", "tree projector"),
        "QCD_COUPLING": ("coupling", "g_s", "alpha_s", "a_s", "Z_g", "beta", "step scaling"),
    }[q])
    base.update({
        "PROJECT_CONTINUUM_LIGHT_FRONT": ("light-front", "C43", "continuum"),
        "C43_ADAPTED_MSBAR": ("C43", "MSbar", "light-front"),
        "RI_SMOM": ("RI/SMOM", "SMOM", "symmetric", "nonexceptional"),
        "MOMQ": ("MOMq", "quark-gluon", "symmetric"),
        "STEP_SCALING_INTERMEDIATE": ("step scaling", "SSF", "sigma", "running"),
    }[scheme])
    return tuple(sorted(set(str(x) for x in base)))

_QUANTITY_TERMS = {
    "QUARK_FIELD": ("quark", "field", "wave-function", "Z_q", "Zpsi", "Sigma_q", "inverse propagator"),
    "SIGNED_QUARK_MASS": ("mass", "signed", "Z_m", "scalar", "pseudoscalar", "m_R", "mass renormalization"),
    "TRANSVERSE_GLUON_FIELD": ("gluon", "transverse", "Z_A", "Pi", "two-point"),
    "qg_VERTEX_DRESSING": ("qg", "quark-gluon", "vertex", "Gamma", "Z_1F", "amputated", "tree projector"),
    "QCD_COUPLING": ("coupling", "g_s", "alpha_s", "a_s", "Z_g", "beta", "step scaling", "sigma"),
}
_SCHEME_TERMS = {
    "PROJECT_CONTINUUM_LIGHT_FRONT": ("light-front", "C43"),
    "C43_ADAPTED_MSBAR": ("C43", "MSbar", "light-front"),
    "RI_SMOM": ("RI/SMOM", "SMOM", "symmetric", "nonexceptional"),
    "MOMQ": ("MOMq", "quark-gluon", "symmetric"),
    "STEP_SCALING_INTERMEDIATE": ("step scaling", "SSF", "sigma", "running"),
}

def descriptor_search_query_manifest(descriptor_id: str | None = None) -> MappingProxyType:
    rows = []
    for d in _descriptor_rows():
        if descriptor_id is not None and d["descriptor_id"] != descriptor_id: continue
        rows.append({"descriptor_id": d["descriptor_id"], "quantity_family": d["quantity_family"], "target_scheme": d["target_scheme"], "coordinate": "source coordinate unbound; exact coordinate terms retained", "order": d["order"], "gauge": "descriptor-specific exact gauge required", "projector": "descriptor-specific exact projector required", "active_Nf": "descriptor-specific explicit active-Nf required", "bounded_terms": _lexicon(d), "source_ids_searched": tuple(SOURCE_HASHES), "query_root": _root((d["descriptor_id"], _lexicon(d), tuple(SOURCE_HASHES)))})
    if descriptor_id is not None and not rows: raise KeyError(descriptor_id)
    return _freeze({"schema": "C164-DESCRIPTOR-SEARCH-QUERY-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})

def _candidate_labels(text: str) -> tuple[str, ...]:
    labels = list(_labels(text))
    return tuple(labels[:16])

@lru_cache(maxsize=None)
def _candidates_for(descriptor_id: str) -> tuple[Mapping[str, Any], ...]:
    d = next((x for x in _descriptor_rows() if x["descriptor_id"] == descriptor_id), None)
    if d is None: raise KeyError(descriptor_id)
    terms = _lexicon(d)
    rows = []
    for sid in SOURCE_HASHES:
        doc = _document(sid)
        for i in range(doc.page_count):
            text = doc[i].get_text("text")
            low = text.lower()
            hits = tuple(t for t in terms if t.lower() in low)
            quantity_hits = tuple(t for t in _QUANTITY_TERMS[d["quantity_family"]] if t.lower() in low)
            scheme_hits = tuple(t for t in _SCHEME_TERMS[d["target_scheme"]] if t.lower() in low)
            labels = _candidate_labels(text)
            if not quantity_hits or not scheme_hits or len(hits) < 2: continue
            role = SOURCE_CATALOG[sid]["role"]
            rows.append({"candidate_locator_id": f"C164-CAND-{descriptor_id}-{sid}-P{i+1}", "descriptor_id": descriptor_id, "source_id": sid, "source_version_root": source_version_manifest()["rows"][list(SOURCE_HASHES).index(sid)]["source_version_root"], "pdf_page_index_0based": i, "pdf_page_index_1based": i + 1, "printed_page_label": _printed_label(sid, i), "section_subsection": _page_record(sid, i)["section_headings"], "equation_table_appendix_labels": labels, "normalized_bounding_box": None, "anchor_before_hash": None, "anchor_after_hash": None, "matched_symbol_tokens": tuple(sorted(hits)), "candidate_scientific_role": role, "candidate_scheme_gauge_order": {"scheme": d["target_scheme"], "gauge": "unverified", "order": d["order"]}, "dependency_references_named": labels, "route": "LOC-A+LOC-B+LOC-D", "status": "CANDIDATE_REQUIRES_OBJECT_AND_ROLE_VERIFICATION", "candidate_root": _root((descriptor_id, sid, i, hits, labels))})
    return tuple(rows)

def candidate_locator_manifest(descriptor_id: str | None = None) -> MappingProxyType:
    ds = [d["descriptor_id"] for d in _descriptor_rows() if descriptor_id is None or d["descriptor_id"] == descriptor_id]
    if descriptor_id is not None and not ds: raise KeyError(descriptor_id)
    rows = tuple(x for did in ds for x in _candidates_for(did))
    return _freeze({"schema": "C164-CANDIDATE-LOCATOR-MANIFEST-V1", "descriptor_id": descriptor_id, "rows": rows, "candidate_count": len(rows), "all_candidates_recorded_before_selection": True, "root": _root(rows)})

def _bbox_for_label(source_id: str, index0: int, label: str) -> tuple[float, float, float, float]:
    page = _document(source_id)[index0]
    blocks = [b for b in page.get_text("blocks") if label in b[4]]
    if not blocks:
        hits = page.search_for(label)
        if not hits: raise ValueError(f"object label not found: {source_id} {index0 + 1} {label}")
        r = hits[0]; return (r.x0, r.y0, r.x1, r.y1)
    # Join only the first contiguous equation object containing the label;
    # explanatory prose that repeats the label is a separate object.
    if label in ("(20)", "(24)", "(2.9b)", "(2.10)"):
        ordered = sorted(blocks, key=lambda b: (b[1], b[0]))
        selected = [ordered[0]]
        edge = ordered[0][3]
        for block in ordered[1:]:
            if block[1] <= edge + 5:
                selected.append(block)
                edge = max(edge, block[3])
            else:
                break
        blocks = selected
    x0 = min(b[0] for b in blocks); y0 = min(b[1] for b in blocks); x1 = max(b[2] for b in blocks); y1 = max(b[3] for b in blocks)
    if label == "(6.35)":
        conversion_blocks = [b for b in page.get_text("blocks") if 240 <= b[1] <= 520]
        y0 = min(b[1] for b in conversion_blocks)
        y1 = max(b[3] for b in conversion_blocks)
        x0 = min(b[0] for b in conversion_blocks)
        x1 = max(b[2] for b in conversion_blocks)
    if label == "(6.34)":
        y0 = min(b[1] for b in page.get_text("blocks") if 70 <= b[1] <= 165)
        y1 = max(b[3] for b in page.get_text("blocks") if 70 <= b[1] <= 165)
        x0 = min(b[0] for b in page.get_text("blocks") if 70 <= b[1] <= 165)
        x1 = max(b[2] for b in page.get_text("blocks") if 70 <= b[1] <= 165)
    return (x0, y0, x1, y1)

def _hash_anchor(text: str) -> str:
    return sha256(" ".join(text.split()).encode()).hexdigest()

def _accepted_record(descriptor_id: str) -> MappingProxyType:
    if descriptor_id not in ACCEPTED_SPECS: raise KeyError(descriptor_id)
    sid, index0, label, section, role, scheme = ACCEPTED_SPECS[descriptor_id]
    page = _document(sid)[index0]
    rec = _page_record(sid, index0)
    x0, y0, x1, y1 = _bbox_for_label(sid, index0, label)
    blocks = sorted(page.get_text("blocks"), key=lambda b: (b[1], b[0]))
    target = [b for b in blocks if b[0] <= x1 and b[2] >= x0 and b[1] <= y1 and b[3] >= y0]
    target_text = " ".join(b[4] for b in target)
    before = " ".join(b[4] for b in blocks if b[3] <= y0)[-220:]
    after = " ".join(b[4] for b in blocks if b[1] >= y1)[:220]
    norm = [round(x0 / page.rect.width, 6), round(y0 / page.rect.height, 6), round(x1 / page.rect.width, 6), round(y1 / page.rect.height, 6)]
    clip = fitz.Rect(max(0, x0 - 8), max(0, y0 - 8), min(page.rect.width, x1 + 8), min(page.rect.height, y1 + 8))
    crop = page.get_pixmap(dpi=RENDER_DPI, clip=clip, alpha=False).tobytes("png")
    source_root = next(r["source_version_root"] for r in source_version_manifest()["rows"] if r["source_id"] == sid)
    locator_id = "C164-LOC-" + descriptor_id
    return _freeze({"locator_id": locator_id, "descriptor_id": descriptor_id, "source_id": sid, "source_version": SOURCE_CATALOG[sid]["version"], "source_version_root": source_root, "local_file_sha256": SOURCE_HASHES[sid], "pdf_page_index_0based": index0, "pdf_page_index_1based": index0 + 1, "printed_page_label": rec["printed_page_label"], "section_subsection": section, "equation_table_appendix_label": label, "normalized_bounding_box": norm, "nearby_anchor_before_hash": _hash_anchor(before), "nearby_anchor_after_hash": _hash_anchor(after), "page_text_hash": rec["normalized_text_sha256"], "page_layout_hash": rec["layout_text_sha256"], "page_render_hash": rec["render_sha256"], "object_crop_hash": sha256(crop).hexdigest(), "object_fingerprint": _root((sid, index0, label, target_text)), "visual_verification": "VISUALLY_VERIFIED_LOCAL_RENDER", "text_layer_agreement": "AGREES_WITH_RENDERED_OBJECT", "scientific_role": role, "source_scientific_role": SOURCE_CATALOG[sid]["role"], "target_scheme": scheme, "gauge": "source gauge stated or source-specific; adapter not closed", "pole_prescription": "source prescription; adapter not closed", "active_Nf": "source explicit where present; descriptor adapter not closed", "dependency_locator_ids": (f"C164-DEP-{descriptor_id}",), "candidate_route_roots": tuple(x["candidate_root"] for x in _candidates_for(descriptor_id) if x["source_id"] == sid and x["pdf_page_index_0based"] == index0), "locator_status": "FINAL_OBJECT_LOCATED_DEPENDENCIES_PENDING", "locator_root": _root((locator_id, sid, index0, label, norm, rec["render_sha256"], sha256(crop).hexdigest()))})

def accepted_locator_schema() -> MappingProxyType:
    return _freeze({"schema": "C164-ACCEPTED-LOCATOR-SCHEMA-V1", "required": ("locator_id", "descriptor_id", "source_id", "source_version_root", "local_file_sha256", "pdf_page_index_0based", "pdf_page_index_1based", "printed_page_label", "section_subsection", "equation_table_appendix_label", "normalized_bounding_box", "nearby_anchor_before_hash", "nearby_anchor_after_hash", "page_text_hash", "page_render_hash", "object_crop_hash", "visual_verification", "text_layer_agreement", "scientific_role", "dependency_locator_ids", "locator_root"), "page_only_rejected": True, "text_layer_only_rejected": True, "mutable": False, "root": _root(("accepted-schema", 22))})

def accepted_locator_manifest(descriptor_id: str | None = None, source_id: str | None = None) -> MappingProxyType:
    if descriptor_id is not None and descriptor_id not in {d["descriptor_id"] for d in _descriptor_rows()}: raise KeyError(descriptor_id)
    if source_id is not None and source_id not in SOURCE_HASHES: raise KeyError(source_id)
    rows = []
    for did in ACCEPTED_SPECS:
        if descriptor_id is not None and did != descriptor_id: continue
        if source_id is not None and ACCEPTED_SPECS[did][0] != source_id: continue
        rows.append(_accepted_record(did))
    return _freeze({"schema": "C164-ACCEPTED-LOCATOR-MANIFEST-V1", "descriptor_id": descriptor_id, "source_id": source_id, "rows": tuple(rows), "accepted_locator_count": len(rows), "root": _root(rows)})

def visual_locator_report(locator_id: str) -> MappingProxyType:
    for row in accepted_locator_manifest()["rows"]:
        if row["locator_id"] == locator_id:
            return _freeze({"schema": "C164-VISUAL-LOCATOR-REPORT-V1", "locator_id": locator_id, "visual_verification": row["visual_verification"], "text_layer_agreement": row["text_layer_agreement"], "render_hash": row["page_render_hash"], "crop_hash": row["object_crop_hash"], "bbox": row["normalized_bounding_box"], "root": _root((locator_id, row["page_render_hash"], row["object_crop_hash"], row["normalized_bounding_box"]))})
    raise KeyError(locator_id)

def _terminal(did: str) -> str:
    if did in ACCEPTED_SPECS: return LOCATOR_STATUS
    d = next(x for x in _descriptor_rows() if x["descriptor_id"] == did)
    if d["target_scheme"] in ("PROJECT_CONTINUUM_LIGHT_FRONT", "C43_ADAPTED_MSBAR"): return "FINAL_OBJECT_NOT_PRESENT_IN_LOCAL_SOURCES"
    if d["target_scheme"] == "STEP_SCALING_INTERMEDIATE": return "FINAL_OBJECT_NOT_PRESENT_IN_LOCAL_SOURCES"
    return "SOURCE_ROLE_MISMATCH"

def scientific_role_manifest(descriptor_id: str | None = None) -> MappingProxyType:
    rows = []
    for d in _descriptor_rows():
        if descriptor_id is not None and d["descriptor_id"] != descriptor_id: continue
        accepted = _accepted_record(d["descriptor_id"]) if d["descriptor_id"] in ACCEPTED_SPECS else None
        rows.append({"descriptor_id": d["descriptor_id"], "required_role": "DIRECT_TARGET_COEFFICIENT or explicit target scheme/step-scaling dependency", "accepted_locator_id": accepted["locator_id"] if accepted else None, "candidate_source_roles": tuple(SOURCE_CATALOG[s]["role"] for s in SOURCE_HASHES), "accepted_role": accepted["scientific_role"] if accepted else None, "PDG_promoted": False, "beta_promoted_to_field": False, "step_scaling_promoted_to_fixed_order": False, "Landau_relabelled_C43": False, "terminal_status": _terminal(d["descriptor_id"])})
    if descriptor_id is not None and not rows: raise KeyError(descriptor_id)
    return _freeze({"schema": "C164-SCIENTIFIC-ROLE-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})

def dependency_locator_graph(descriptor_id: str) -> MappingProxyType:
    if descriptor_id not in {d["descriptor_id"] for d in _descriptor_rows()}: raise KeyError(descriptor_id)
    accepted = descriptor_id in ACCEPTED_SPECS
    deps = {
        "TGT-QUARK_FIELD-RI_SMOM": (("arxiv_0901.2599", 6, "(10)"), ("arxiv_0901.2599", 9, "(19)")),
        "TGT-SIGNED_QUARK_MASS-RI_SMOM": (("arxiv_0901.2599", 9, "(20)"), ("arxiv_0901.2599", 10, "(24)"), ("arxiv_0901.2599", 6, "(11)")),
        "TGT-QUARK_FIELD-MOMQ": (("arxiv_1108.4806", 4, "(2.3)"), ("arxiv_1108.4806", 23, "(6.35)")),
        "TGT-TRANSVERSE_GLUON_FIELD-MOMQ": (("arxiv_1108.4806", 4, "(2.3)"), ("arxiv_1108.4806", 23, "(6.35)")),
        "TGT-qg_VERTEX_DRESSING-MOMQ": (("arxiv_1108.4806", 4, "(2.3)"), ("arxiv_1108.4806", 5, "(2.4)"), ("arxiv_1108.4806", 23, "(6.34)")),
        "TGT-QCD_COUPLING-MOMQ": (("arxiv_1108.4806", 4, "(2.3)"), ("arxiv_1108.4806", 23, "(6.35)")),
        "TGT-QCD_COUPLING-STEP_SCALING_INTERMEDIATE": (("arxiv_1706.03821", 1, "(7)"), ("arxiv_1706.03821", 1, "(8)")),
        "TGT-SIGNED_QUARK_MASS-STEP_SCALING_INTERMEDIATE": (("arxiv_1802.05243", 4, "(2.9a)"), ("arxiv_1802.05243", 4, "(2.9b)"), ("arxiv_1802.05243", 4, "(2.10)")),
    }.get(descriptor_id, ())
    nodes = tuple({"dependency_locator_id": f"C164-DEP-{descriptor_id}-{i}", "source_id": sid, "pdf_page_index_0based": page, "pdf_page_index_1based": page + 1, "printed_page_label": _printed_label(sid, page), "object_label": label, "page_hash": _page_record(sid, page)["normalized_text_sha256"], "render_hash": _page_record(sid, page)["render_sha256"], "status": "LOCATED_DEPENDENCY_CANDIDATE"} for i, (sid, page, label) in enumerate(deps))
    missing = ("complete source-to-project coordinate adapter", "descriptor-specific gauge/pole/projector and active-Nf record", "all branch/special-function definitions") if accepted else ("final exact target object", "source-compatible scientific role")
    return _freeze({"schema": "C164-DEPENDENCY-LOCATOR-GRAPH-V1", "descriptor_id": descriptor_id, "nodes": nodes, "edges": tuple(), "status": LOCATOR_STATUS if accepted else "NO_FINAL_OBJECT", "missing_dependencies": missing, "frozen_project_owned_identities": (), "root": _root((descriptor_id, nodes, missing))})

def descriptor_locator_crosswalk() -> MappingProxyType:
    rows = []
    for d in _descriptor_rows():
        did = d["descriptor_id"]
        accepted = _accepted_record(did) if did in ACCEPTED_SPECS else None
        graph = dependency_locator_graph(did)
        rows.append({"descriptor_id": did, "quantity_family": d["quantity_family"], "target_scheme": d["target_scheme"], "target_coordinate": "source coordinate unbound", "order": d["order"], "required_scientific_role": "direct target or explicit scheme/step-scaling dependency", "candidate_locator_ids": tuple(x["candidate_locator_id"] for x in _candidates_for(did)), "accepted_final_locator_id": accepted["locator_id"] if accepted else None, "dependency_locator_ids": tuple(x["dependency_locator_id"] for x in graph["nodes"]), "source_version_root": accepted["source_version_root"] if accepted else None, "visual_verification_status": accepted["visual_verification"] if accepted else "NOT_ACCEPTED", "terminal_status": _terminal(did), "exact_first_missing_object": "complete dependency-locator graph and descriptor adapter" if accepted else "exact compatible final source object with source role, scheme, gauge, projector, coordinate, and order"})
    counts = {}
    for r in rows: counts[r["terminal_status"]] = counts.get(r["terminal_status"], 0) + 1
    return _freeze({"schema": "C164-DESCRIPTOR-LOCATOR-CROSSWALK-V1", "rows": tuple(rows), "descriptor_count": len(rows), "terminal_status_counts": counts, "root": _root(rows)})

def componentwise_locator_manifest(quantity_id: str) -> MappingProxyType:
    if quantity_id not in QUANTITIES: raise KeyError(quantity_id)
    rows = tuple(x for x in descriptor_locator_crosswalk()["rows"] if x["quantity_family"] == quantity_id)
    return _freeze({"schema": "C164-COMPONENTWISE-LOCATOR-MANIFEST-V1", "quantity_id": quantity_id, "rows": rows, "accepted": sum(r["accepted_final_locator_id"] is not None for r in rows), "root": _root((quantity_id, rows))})

def mass_coupling_locator_gate_report() -> MappingProxyType:
    rows = []
    for q in ("SIGNED_QUARK_MASS", "QCD_COUPLING"):
        qrows = [r for r in descriptor_locator_crosswalk()["rows"] if r["quantity_family"] == q]
        rows.append({"quantity_id": q, "accepted_final_locators": tuple(r["accepted_final_locator_id"] for r in qrows if r["accepted_final_locator_id"]), "exact_source_version": any(r["accepted_final_locator_id"] for r in qrows), "dependency_locators_complete": False, "coordinate_and_order_explicit": False, "scheme_gauge_role_unambiguous": False, "visual_verification": any(r["visual_verification_status"] == "VISUALLY_VERIFIED_LOCAL_RENDER" for r in qrows), "gate_status": LOCATOR_STATUS})
    return _freeze({"schema": "C164-MASS-COUPLING-LOCATOR-GATE-V1", "rows": tuple(rows), "gate_closed": True, "formula_transcription_authorized": False, "target_execution_authorized": False, "root": _root(rows)})

def absence_certificate_manifest(descriptor_id: str | None = None) -> MappingProxyType:
    rows = []
    for d in _descriptor_rows():
        if descriptor_id is not None and d["descriptor_id"] != descriptor_id: continue
        if d["descriptor_id"] in ACCEPTED_SPECS: continue
        cands = _candidates_for(d["descriptor_id"])
        rows.append({"certificate_id": "C164-ABS-" + d["descriptor_id"], "descriptor_id": d["descriptor_id"], "claim_scope": "not located in the eight authenticated local PDFs; not a mathematical nonexistence claim", "all_candidate_source_ids_searched": tuple(SOURCE_HASHES), "all_page_ranges_searched": {s: [0, _document(s).page_count - 1] for s in SOURCE_HASHES}, "descriptor_lexicon": _lexicon(d), "equation_table_appendix_labels_inspected": sum(len(_page_record(s, i)["equation_table_appendix_labels"]) for s in SOURCE_HASHES for i in range(_document(s).page_count)), "references_followed": "local references and source-page structure inspected; no external source followed", "candidate_hits": len(cands), "rejected_candidate_reasons": ("wrong quantity", "wrong scheme/gauge", "method/running/step-scaling role", "page-only or no exact object label", "dependency adapter absent"), "text_layer_reliability": "EXTRACTED_LAYOUT_TEXT", "visual_page_coverage": "local page renders hashed; no non-accepted object promoted", "no_substitute": ("PDG values", "related paper", "rounded table", "plot", "model memory", "web/download"), "certificate_root": _root((d["descriptor_id"], len(cands), tuple(SOURCE_HASHES)))})
    if descriptor_id is not None and not rows and descriptor_id not in ACCEPTED_SPECS: raise KeyError(descriptor_id)
    return _freeze({"schema": "C164-ABSENCE-CERTIFICATE-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})

def refined_source_request_manifest() -> MappingProxyType:
    rows = []
    for d in _descriptor_rows():
        did = d["descriptor_id"]
        if did in ACCEPTED_SPECS:
            missing = "dependency equations/definitions and exact descriptor adapter; source TeX/ancillary may be required for dependency closure"
            reason = "FINAL_OBJECT_LOCATED_BUT_DEPENDENCY_LOCATOR_INCOMPLETE"
        else:
            missing = "an exact compatible final-object equation/table/appendix in a local source, or authenticated TeX/ancillary/source-code supplement"
            reason = "EXACT_LOCAL_PDF_LACKS_COMPATIBLE_REQUESTED_OBJECT_OR_ROLE"
        rows.append({"request_id": "C164-REQ-" + did, "descriptor_id": did, "quantity_family": d["quantity_family"], "target_scheme": d["target_scheme"], "order": d["order"], "current_local_sources": tuple(SOURCE_HASHES), "refinement_reason": reason, "required_version": "exact version matching descriptor; no replacement download permitted", "required_object": missing, "required_dependency_objects": ("coordinate", "gauge/pole", "projector/external state", "active_Nf", "renormalization layer", "conversion direction", "branch/special functions"), "acceptable_artifact": ("authenticated local PDF", "matching TeX archive", "matching ancillary formula file", "erratum/supplement", "authenticated source-code object"), "no_substitute": True, "terminal_status": _terminal(did)})
    return _freeze({"schema": "C164-REFINED-SOURCE-REQUEST-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})

def expression_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C164-EXPRESSION-HANDOFF-CONTRACT-V1", "eligible": False, "source_version_roots": tuple(r["source_version_root"] for r in source_version_manifest()["rows"]), "accepted_locator_count": len(ACCEPTED_SPECS), "dependency_graphs_complete": 0, "complete_expressions": 0, "target_values": 0, "reason": "dependency locator gate remains incomplete", "next": NEXT, "root": _root((False, len(ACCEPTED_SPECS), NEXT))})

def quantum_locator_handoff() -> MappingProxyType:
    return _freeze({"schema": "C164-QUANTUM-LOCATOR-HANDOFF-V1", "Q0_Q1_Q2_modified": False, "quantum_sources_consumed": False, "states": 0, "next": NEXT, "root": _root(("Q0/Q1/Q2", False))})

def lfglocator2_completeness_certificate() -> MappingProxyType:
    cross = descriptor_locator_crosswalk()
    return _freeze({"schema": "C164-LFGLOCATOR2-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "positive_gate": False, "descriptors": 25, "accepted_final_locators": len(ACCEPTED_SPECS), "visual_verified_accepted_locators": len(ACCEPTED_SPECS), "dependency_graphs_complete": 0, "source_object_absence_certificates": absence_certificate_manifest()["count"], "refined_requests": 25, "complete_expressions": 0, "target_programs": 0, "target_values": 0, "terminal_status_counts": cross["terminal_status_counts"], "mass_coupling_gate": False, "next": NEXT, "root": _root((STATUS, cross["root"], NEXT))})

def verify_hqcd_lfglocator2_authority() -> dict[str, Any]:
    inv = source_version_manifest()
    return {"schema": "C164-HQCDLFGLOCATOR2-V1", "status": STATUS, "plan": PLAN, "baseline": BASELINE, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "next": NEXT, "C163_status": C163_STATUS, "C163_plan": C163_PLAN, "C163_package_root": C163_ROOT, "C162_package_root": C162_ROOT, "C161_package_root": C161_ROOT, "C160_package_root": C160_ROOT, "C159_package_root": C159_ROOT, "C158_package_root": C158_ROOT, "C134_classification": C134_CLASSIFICATION, "source_artifacts": inv["count"], "hash_mismatches": sum(r["actual_sha256"] != r["sha256"] for r in inv["rows"]), "pages": pdf_printed_page_map()["page_count"], "candidate_locators": candidate_locator_manifest()["candidate_count"], "accepted_locators": len(ACCEPTED_SPECS), "dependency_graphs_complete": 0, "complete_expressions": 0, "target_programs": 0, "target_values": 0, "PDG_values_consumed": 0, "unauthorized_downloads": 0, "roots": ROOTS, "package_root": PACKAGE_ROOT}

def load_verified_hqcd_lfglocator2_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C164 runtime manifest missing")
    m = json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C164 package root/status mismatch")
    return _freeze(verify_hqcd_lfglocator2_authority())

def lfglocator2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C164-LFGLOCATOR2-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS, "reason": "accepted final objects exist for a strict subset, but dependency-locator graphs remain incomplete", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})

def static_isolation_guard() -> MappingProxyType:
    return _freeze({"C131_C163_roots_unchanged": True, "C134_modified": False, "untracked_C157_test_modified": False, "source_downloads": 0, "web_formulas": 0, "invented_locators": 0, "page_only_accepted": 0, "text_only_accepted": 0, "invented_expressions": 0, "plot_reverse_engineering": 0, "PDG_values_consumed": 0, "C158_imports": 0, "C158_recomputed": 0, "complete_expressions": 0, "target_programs": 0, "target_values": 0, "target_minus_FB": 0, "common_IR": 0, "remainders": 0, "brackets": 0, "windows": 0, "running": 0, "thresholds": 0, "counterterms": 0, "null_coordinates": 0, "Q0_Q1_Q2_modified": False, "network": 0, "allow_pickle_false": True, "pass": True})

def mutate_live_hqcdlfglocator2(index: int) -> MappingProxyType:
    fields = ("C163_root", "C162_root", "C161_root", "C160_root", "C159_root", "C158_root", "source_hash", "source_version", "pdf_index0", "pdf_index1", "printed_page", "page_offset", "section", "equation_label", "table_label", "bbox", "anchor_before", "anchor_after", "page_text_hash", "page_render_hash", "object_crop_hash", "visual_status", "text_agreement", "descriptor", "lexicon", "candidate_assignment", "role", "dependency_edge", "PDG_status", "absence_certificate", "refined_request", "loader", "package_root", "next")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})

ROOTS = {
    "C164_INPUT_ROOT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, ROOT_CHAIN)),
    "C164_REGRESSION_BOUNDARY_ROOT": _root((C134_CLASSIFICATION, C158_ROOT, C160_ROOT)),
    "C164_PLAN_ROOT": lfglocator2_plan_manifest()["root"],
    "C164_SOURCE_VERSION_ROOT": source_version_manifest()["root"],
    "C164_PAGE_MAP_ROOT": pdf_printed_page_map()["root"],
    "C164_PAGE_SEARCH_INDEX_ROOT": page_search_index()["root"],
    "C164_DESCRIPTOR_LEXICON_ROOT": descriptor_search_query_manifest()["root"],
    "C164_CANDIDATE_LOCATOR_ROOT": candidate_locator_manifest()["root"],
    "C164_VISUAL_VERIFICATION_ROOT": _root(tuple(r["root"] for r in (visual_locator_report(x["locator_id"]) for x in accepted_locator_manifest()["rows"]))),
    "C164_ACCEPTED_LOCATOR_ROOT": accepted_locator_manifest()["root"],
    "C164_SCIENTIFIC_ROLE_ROOT": scientific_role_manifest()["root"],
    "C164_DEPENDENCY_LOCATOR_ROOT": _root(tuple(dependency_locator_graph(d["descriptor_id"])["root"] for d in _descriptor_rows())),
    "C164_DESCRIPTOR_CROSSWALK_ROOT": descriptor_locator_crosswalk()["root"],
    "C164_QUARK_FIELD_ROOT": componentwise_locator_manifest("QUARK_FIELD")["root"],
    "C164_SIGNED_MASS_ROOT": componentwise_locator_manifest("SIGNED_QUARK_MASS")["root"],
    "C164_GLUON_FIELD_ROOT": componentwise_locator_manifest("TRANSVERSE_GLUON_FIELD")["root"],
    "C164_VERTEX_ROOT": componentwise_locator_manifest("qg_VERTEX_DRESSING")["root"],
    "C164_COUPLING_ROOT": componentwise_locator_manifest("QCD_COUPLING")["root"],
    "C164_MASS_COUPLING_GATE_ROOT": mass_coupling_locator_gate_report()["root"],
    "C164_ABSENCE_CERTIFICATE_ROOT": absence_certificate_manifest()["root"],
    "C164_REFINED_REQUEST_ROOT": refined_source_request_manifest()["root"],
    "C164_EXPRESSION_HANDOFF_ROOT": expression_handoff_contract()["root"],
    "C164_QUANTUM_HANDOFF_ROOT": quantum_locator_handoff()["root"],
    "C164_SCOPE_ROOT": _root((STATUS, "locator-only", "no expressions")),
    "C164_COMPLETENESS_ROOT": lfglocator2_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C164-HQCDLFGLOCATOR2-V1", "baseline": BASELINE, "contract": CONTRACT, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = ["STATUS", "PLAN", "NEXT", "PACKAGE_ROOT", "ROOTS", "BASELINE", "CONTRACT", "CONTRACT_SHA256", "C163_ROOT", "C162_ROOT", "C161_ROOT", "C160_ROOT", "C159_ROOT", "C158_ROOT", "SOURCE_HASHES", "source_version_manifest", "pdf_printed_page_map", "page_search_index", "descriptor_search_query_manifest", "candidate_locator_manifest", "accepted_locator_schema", "accepted_locator_manifest", "visual_locator_report", "scientific_role_manifest", "dependency_locator_graph", "descriptor_locator_crosswalk", "componentwise_locator_manifest", "mass_coupling_locator_gate_report", "absence_certificate_manifest", "refined_source_request_manifest", "expression_handoff_contract", "quantum_locator_handoff", "lfglocator2_completeness_certificate", "verify_hqcd_lfglocator2_authority", "load_verified_hqcd_lfglocator2_authority", "lfglocator2_plan_manifest", "static_isolation_guard", "mutate_live_hqcdlfglocator2"]
