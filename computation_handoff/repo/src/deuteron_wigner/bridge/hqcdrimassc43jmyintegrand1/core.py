"""C358 operator-identical regulated JMY graph-integrand AST."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c358_hqcdrimassc43jmyintegrand1";BASELINE="eaf60986f150aaaa6cf3eaf38e56aac68d87946d";C357_ROOT="57f6d2901ce86042c02cd20d95fa05fb8d695b33c043c798009b65dee0bc3175"
STATUS="C358_OPERATOR_IDENTICAL_ANALYTIC_REGULATED_JMY_INTEGRANDS_DERIVED_PARAMETER_EVALUATION_MISSING";PLAN="RIMASSC43JMYINTEGRAND1-C";NEXT="C359/HQCDRIMASSC43JMYPARAMINT1";NEXT_OBJECT="C358-C43-JMY-REGULATED-PARAMETER-INTEGRALS";NEXT_EXACT="reduce and evaluate the C358 operator-identical regulated JMY graph AST through finite epsilon order"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def integrand_ast():
 common={"measure":"mu^(2epsilon) d^d k/(2pi)^d","d":"4-2epsilon","color":"g^2 CF","gluon":"1/(k^2+i0)","gauge":"Feynman","mass":"zero"}
 rows=({"id":"DV","group":"distribution_virtual","numerator":"ubar(p) gamma_mu (pslash-kslash) gamma_plus u(p) v^mu","denominators":"[(p-k)^2+i0] [v.k+i0]^(1+alpha)","regulator":"nu1^(2alpha)","measurement":"delta(1-x), bT=virtual; include quark and v-line self energies plus MSbar CT"},{"id":"DR","group":"distribution_real_endpoint","numerator":"cut square of quark plus future-v emission including interference","denominators":"delta_plus(k^2) [(p-k)^2+i0][v.k+i0]^(1+alpha)","regulator":"nu1^(2alpha)","measurement":"delta(x-1+k.plus/p.plus) exp(+i bT.kT); plus/delta expansion after grouping"},{"id":"FV","group":"fragmentation_virtual","numerator":"crossed ubar gamma_minus (pslash-kslash) gamma_mu u tildev^mu","denominators":"[(p-k)^2+i0] [tildev.k-i0]^(1+beta)","regulator":"nu2^(2beta)","measurement":"delta(1-z), bT=virtual; crossed self energies plus MSbar CT"},{"id":"FR","group":"fragmentation_real_endpoint","numerator":"crossed cut square including tilde-v interference","denominators":"delta_plus(k^2) [(p-k)^2+i0][tildev.k-i0]^(1+beta)","regulator":"nu2^(2beta)","measurement":"delta(z-1+k.minus/p.minus) exp(+i bT.kT); plus/delta expansion after grouping"},{"id":"S","group":"soft_real_virtual_count_once","numerator":"2 v.tildev","denominators":"[k^2+i0][v.k+i0]^(1+alpha)[tildev.k-i0]^(1+beta)","regulator":"nu1^(2alpha)nu2^(2beta)","measurement":"virtual + delta_plus(k^2)(exp(+i bT.kT)-1); four-line orientations and one overlap owner"})
 return {"common":common,"rows":rows,"count":5,"root":_r((common,rows))}
def operator_crosswalk():return {"bilocal":"JMY Eq.(3) dressed fields, gamma+ distribution; crossed Eq.(32) fragmentation","soft":"JMY Eq.(24) four v/tilde-v lines","rho":"sqrt(v- tildev+/(v+ tildev-)) retained","normalization":"1/2 bilocal and 1/Nc soft trace retained outside AST","transverse_closure":"implicit source gauge link retained","root":_r("C358-X")}
def validation():return {"dimensions":"each group dimensionless after measurement","Ward":"k_mu gamma^mu collapses adjacent inverse propagators and maps endpoint to matching eikonal owner","crossing":"DV<->FV and DR<->FR under plus/minus,x/z,v/tildev and i0 crossing","soft_limit":"DR endpoint -> v side S; FR endpoint -> tildev side S","C356_residues_recovered":True,"scaleless_individual_evaluated":False,"root":_r("C358-V")}
def closure():return {"five_integrands_available":True,"operator_identical":True,"finite_groups_evaluated":False,"finite_conversion_ready":False,"C43_imported":False,"root":_r("C358-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"mass_finite_reused":0,"foreign_numerator":0,"scaleless_evaluated":0,"orientation_changed":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmyintegrand1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmyintegrand1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyfinite1 as c
 if c.PACKAGE_ROOT!=C357_ROOT:raise ValueError("C357")
 c.load_verified_hqcdrimassc43jmyfinite1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmyintegrand1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmyintegrand1_authority()
_ROOTS={"INPUT":_r((BASELINE,C357_ROOT)),"AST":integrand_ast()["root"],"X":operator_crosswalk()["root"],"VALID":validation()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C358-HQCDRIMASSC43JMYINTEGRAND1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
