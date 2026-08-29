"""Source-locked action-level contracts; deliberately no numerical QCD matrices."""
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[4]
SOURCES=(
 ("BPP","hep-ph/9705477v1","hep-ph-9705477v1.pdf","hep-ph-9705477v1.tar","Brodsky, Pauli, Pinsky","Quantum Chromodynamics and Other Field Theories on the Light Cone",206,"review: LF Fock normalization, DLCQ and Hamiltonian context"),
 ("SB","hep-ph/0011372v2","hep-ph-0011372v2.pdf","hep-ph-0011372v2.tar","Srivastava, Brodsky","Light-Front-Quantized QCD in Light-Cone Gauge: The Doubly Transverse Gauge Propagator",32,"canonical action authority: Eqs. (1), (5)-(9), (24)-(25)"),
 ("BJY","hep-ph/0208038v2","hep-ph-0208038v2.pdf","hep-ph-0208038v2.tar","Belitsky, Ji, Yuan","Final State Interactions and Gauge Invariant Parton Distributions",35,"residual boundary and transverse-link authority: Secs. II, III"),
 ("JMY","hep-ph/0404183v1","hep-ph-0404183v1.pdf","hep-ph-0404183v1.tar","Ji, Ma, Yuan","QCD Factorization for Semi-Inclusive Deep-Inelastic Scattering at Low Transverse Momentum",28,"fixed selected spacelike TMD authority: Sec. II"),
 ("HEINZL","hep-th/0008096v1","hep-th-0008096v1.pdf","hep-th-0008096v1.tar","Heinzl","Light-Cone Quantization: Foundations and Applications",90,"supporting finite-volume/inverse-derivative/zero-mode audit"),
 ("GAO","1005.4305v1","1005.4305v1.pdf","1005.4305v1.tar","Gao","Derivation of the Gauge Link in Light Cone Gauge",18,"independent transverse-link boundary cross-check"),
)
RAW=ROOT/"data/raw/c43_sources"
def _digest(p): return sha256(p.read_bytes()).hexdigest()
def source_manifest():
    rows=[]
    for key,ident,pdf,archive,authors,title,pages,role in SOURCES:
        pp,aa=RAW/pdf,RAW/archive
        rows.append({"key":key,"arxiv":ident,"authors":authors,"title":title,"pdf_path":str(pp.relative_to(ROOT)),"archive_path":str(aa.relative_to(ROOT)),"pdf_sha256":_digest(pp),"archive_sha256":_digest(aa),"pdf_bytes":pp.stat().st_size,"archive_bytes":aa.stat().st_size,"pdf_pages":pages,"role":role,"download_command":f"curl -fL https://arxiv.org/pdf/{ident} -o {pp.relative_to(ROOT)}; curl -fL https://arxiv.org/e-print/{ident} -o {aa.relative_to(ROOT)}"})
    return {"status":"HASH_LOCKED","official_host":"arxiv.org","rows":rows}

def validate_source_manifest(manifest):
    return manifest == source_manifest()

def conventions():
    return {"coordinates":"x^plus=(x^0+x^3)/sqrt(2), x^minus=(x^0-x^3)/sqrt(2), x^plus is time","metric":"g=diag(1,-1,-1,-1); a.b=a+ b- + a- b+ - aT.bT","n":{"plus":0,"minus":1,"transverse":[0,0]},"nbar":{"plus":1,"minus":0,"transverse":[0,0]},"gauge_condition":"n.A=A^+=A_-=0","derivatives":"partial^+=partial_-=d/dx^-; partial^-=partial_+=d/dx^+","gamma":"gamma^plus=(gamma^0+gamma^3)/sqrt(2); Lambda_plus=gamma^- gamma^+/2","D":"D_mu=partial_mu+i g A_mu^a T^a; F=partial A-partial A+g f A A","color":"T^a=lambda^a/2; Tr(Ta Tb)=delta_ab/2; C_F=4/3"}

def action_contract():
    return {"gauge":"G0-LIGHT-FRONT-GAUGE","source":"SB hep-ph/0011372v2, Eqs. (1), (5)-(9), (24)-(25)","scope":"one external quark; qg intermediate/real state; rank-zero T-even bilocal; terms through O(g^2)","dynamical_fields":["psi_plus=Lambda_plus psi","A_perp^a"],"constrained_fields":["psi_minus","A_minus=A^+ (fixed to zero)","A_plus=A^- (Gauss-law dependent)","B^a multiplier"],"canonical_momenta":{"pi_plus":"0","pi_perp":"F_-perp","pi_minus":"F_+-","pi_B":"0"},"constraints":["pi_plus=0","pi_B=0","pi_perp-partial_- A_perp+partial_perp A_-=0","A_-=0","partial_- pi^-+partial_perp pi^perp-g j^+=0","pi^-+partial_- A_+=0","B=0"],"fermion_constraint":"i sqrt(2) D_- psi_- = -(i gamma^0 gamma^perp D_perp-m gamma^0) psi_+","gauss_law":"partial_- (partial_- A_+^a-partial_perp A_perp^a)=-g f_abc A_perp^b partial_- A_perp^c+g psibar gamma^+ T^a psi","inverse_derivative":{"prescription":"ANTISYMMETRIC_OR_PV","kernel":"(partial^+)^{-1}(1-P0)f(x^-)=1/2 integral dy^- epsilon(x^- - y^-) (1-P0)f(y^-)","zero_projector":"P0 f=L^-1 integral_{-L/2}^{L/2} dy^- f(y^-)","property":"anti-Hermitian on nonzero-mode domain"},"interactions":{"canonical_qg":"-g psibar gamma^mu T^a psi A_mu^a","three_gluon":"g f_abc (partial_mu A_nu^a-partial_nu A_mu^a)A_b^mu A_c^nu/2","four_gluon":"g^2 f_abc f_ade A_bmu A_dmu A_cnu A_enu/4","instantaneous_fermion":"-g^2/2 psibar gamma^+ gamma^mu A_mu^a T^a (i partial_-)^-1 gamma^nu A_nu^b T^b psi","instantaneous_current":"-g^2/2 [(i partial_-)^-1 j_a^+]^2"},"ghost_status":"decoupled in this axial/light-front gauge at declared perturbative nonzero-mode scope; global zero modes retained by contract"}

def validate_contract(contract=None):
    c=action_contract() if contract is None else contract; v=conventions()
    assert c == action_contract()
    assert c["gauge"]=="G0-LIGHT-FRONT-GAUGE"
    assert v["n"]["plus"]==0 and v["n"]["minus"]==1 and v["nbar"]["plus"]==1
    assert "psi_minus" in c["constrained_fields"] and "A_perp^a" in c["dynamical_fields"]
    assert c["inverse_derivative"]["prescription"]=="ANTISYMMETRIC_OR_PV"
    assert set(("canonical_qg","instantaneous_fermion","instantaneous_current"))<=set(c["interactions"])
    assert "Gauss" in c["gauss_law"] or "partial_-" in c["gauss_law"]
    return True

def symbolic_hash(value): return sha256(json.dumps(value,sort_keys=True,separators=(",",":" )).encode()).hexdigest()
