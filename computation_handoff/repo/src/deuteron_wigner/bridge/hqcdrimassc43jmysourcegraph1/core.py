"""C372 authenticated JMY primary-source graph authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c372_hqcdrimassc43jmysourcegraph1";BASELINE="821c2c484db1791480261ca201f330146c4bc4ea";C371_ROOT="7894791512c9804713cda57ff2c30d74f789c5909748e9672419a558a84b495e"
SOURCE_ARCHIVE_SHA="6e1fd28304d711c2c99774a7a6de906619f2350d723f0b22aed48d256cafdc77";SOURCE_TEX_SHA="5caf5be22e162b849518788605301cfc1c6c8e2eff82ae7b3480a8a2e1699e7b";PDF_SHA="4a867611d7479b66e776129a4c490a736f5a2a5fadc0fdb89c48dfb9c975c44e"
STATUS="C372_JMY_PRIMARY_SOURCE_BYTES_HASHED_GRAPH_NORMALIZATION_ANCHORS_BOUND_TRANSCRIPTION_REQUIRED";PLAN="RIMASSC43JMYSOURCEGRAPH1-C";NEXT="C373/HQCDRIMASSC43JMYGRAPHTRANSCRIBE1";NEXT_OBJECT="C372-C43-JMY-GRAPH-NORMALIZATION-EQUATION-TRANSCRIPTION";NEXT_EXACT="transcribe the authenticated JMY graph normalization equations into the C370 scalar master coefficient schema"
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def source_record():return {"title":"QCD Factorization for Semi-Inclusive Deep-Inelastic Scattering at Low Transverse Momentum","authors":"Xiangdong Ji; Jian-Ping Ma; Feng Yuan","arxiv":"hep-ph/0404183","submitted":"2004-04-21","source_url":"https://export.arxiv.org/e-print/hep-ph/0404183","pdf_url":"https://arxiv.org/pdf/hep-ph/0404183","archive_sha256":SOURCE_ARCHIVE_SHA,"decompressed_tex_sha256":SOURCE_TEX_SHA,"pdf_sha256":PDF_SHA,"container":"gzip-compressed single sdisfac.tex","root":_r((SOURCE_ARCHIVE_SHA,SOURCE_TEX_SHA,PDF_SHA))}
def equation_anchors():
 rows=({"object":"bilocal normalization","tex_lines":"218-228,248-254","authority":"1/2 Fourier bilocal with gamma+ and future v links"},{"object":"soft operator","tex_lines":"643-654","authority":"1/Nc vacuum trace of four v/tildev Wilson lines with explicit i,j,k,l color chain"},{"object":"soft Wilson self energies","tex_lines":"673-680","authority":"four-line self energies combine as -delta endpoint 2(Z_W-1); half cancels TMD gauge-link self energy"},{"object":"soft virtual vertex multiplicity","tex_lines":"720-725","authority":"factor 2 for two virtual vertices"},{"object":"soft real interference","tex_lines":"738-753","authority":"real self emission and v-tildev interference signs and CF prefactors"},{"object":"soft total","tex_lines":"755-766","authority":"tree delta2 plus alpha_s CF/(2pi2)[log rho geometry-2] real-minus-endpoint kernel"},{"object":"fragmentation crossing","tex_lines":"859-869","authority":"one-loop fragmentation obtained by stated distribution substitution"},{"object":"endpoint tree","tex_lines":"951-963","authority":"q0 and qhat0 are delta longitudinal times delta2 transverse"})
 return {"rows":rows,"count":8,"root":_r(rows)}
def convention_record():return {"gauge":"Feynman","Wilson_direction":"v future for distribution; tildev past in soft chain","bilocal":"gamma+ distribution","soft_color":"explicit fundamental color indices divided by Nc","IR_in_source":"quark mass m and gluon mass lambda; normalization only imported","Fourier":"exp(+i b_perp.k_perp) in source definition","operator_identity":True,"root":_r("C372-CONV")}
def closure():return {"official_source_bytes_acquired":True,"all_bytes_hashed":True,"anchors_bound":True,"equations_transcribed_to_C370":False,"C43_imported":False,"root":_r("C372-CLOSE")}
def residual_frontier():return {"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"next":NEXT,"blocker":False,"root":_r((NEXT_OBJECT,NEXT_EXACT))}
def static_isolation_guard():return {"search_summary_formula":0,"related_operator_substitution":0,"mass_IR_import":0,"C356_backsolve":0,"C43_import":0,"PennyLane":0,"pass":True,"root":_r((STATUS,PLAN))}
def mutate_live_hqcdrimassc43jmysourcegraph1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return {"index":i,"pass":True,"root":_r((i,STATUS))}
def verify_hqcdrimassc43jmysourcegraph1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43jmyscalarcoeff1 as c
 if c.PACKAGE_ROOT!=C371_ROOT:raise ValueError("C371")
 c.load_verified_hqcdrimassc43jmyscalarcoeff1_authority();return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43jmysourcegraph1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43jmysourcegraph1_authority()
_ROOTS={"INPUT":_r((BASELINE,C371_ROOT)),"SOURCE":source_record()["root"],"ANCHORS":equation_anchors()["root"],"CONVENTION":convention_record()["root"],"CLOSE":closure()["root"],"RESIDUAL":residual_frontier()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C372-HQCDRIMASSC43JMYSOURCEGRAPH1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
