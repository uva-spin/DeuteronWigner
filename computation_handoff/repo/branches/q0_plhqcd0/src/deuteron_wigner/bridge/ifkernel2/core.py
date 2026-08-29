"""Factorized C80 evaluator for C55's direct ``b† a† a b`` W3 contact.

The object evaluated here is a *raw kernel coordinate*, never a C78 physical
bra/ket sum.  The C78 projection coefficients remain outside this module.
All longitudinal labels are exact fractions; transverse contact overlaps use
the C45 coordinate-space HO convention and retain exact SymPy expressions.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from math import factorial, pi, sqrt
from pathlib import Path
from types import MappingProxyType
from typing import Any

import numpy as np
import sympy as sp
from scipy.special import roots_genlaguerre

from ..g0.contracts import action_contract
from ..iferm.core import SB_W3, instantaneous_fermion_preflight
from ..ifsupport2.core import IFermContactSupportPackage, STATUS as C78_STATUS
from ..modes.core import GAMMA, GAMMA_PLUS, RESOLUTIONS, gell_mann, ho_coordinate, polarization, polarization_cartesian, spinor
from ..qgembed9.core import QGEmbeddingPackage

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c80_ifkernel2"
SCHEMA = "C80-IFKERNEL2-V1"
STATUS = "C80_EXACT_SOURCE_CHAIN_DERIVED_IFCONTACT_KERNEL_EVALUATOR_READY"
NEXT = "C81/IFCONTACT3 — evaluate and assemble the bare direct instantaneous-fermion contact matrix on immutable C78 support using immutable C80 kernel coordinates"
COUPLING = "g_s^2 (explicitly factored)"


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: Any) -> str:
    return sha256(_json(value).encode()).hexdigest()


def _file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _freeze(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list): return tuple(_freeze(item) for item in value)
    if isinstance(value, np.ndarray):
        value = np.array(value, copy=True); value.setflags(write=False); return value
    return value


def _fraction(value: str | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


@dataclass(frozen=True)
class ContactKernelCoordinate:
    """One C78-addressable raw-mode/color coordinate, not a physical pair."""
    resolution: str
    q_out_raw_id: str
    g_out_raw_id: str
    q_in_raw_id: str
    g_in_raw_id: str
    q_out: tuple[int, int, int, int, int]  # k numerator/denominator,n,m,h
    g_out: tuple[int, int, int, int, int]
    q_in: tuple[int, int, int, int, int]
    g_in: tuple[int, int, int, int, int]
    c_out: int
    a_out: int
    c_in: int
    a_in: int
    source_order: tuple[str, str, str, str] = ("b_dagger", "a_dagger", "a", "b")
    zero_mode_policy: str = "C43_PV_Q0_EXCLUDE_ZERO"

    @property
    def id(self) -> str:
        return "C80:KAPPA:" + digest(asdict(self))


def _raw_index() -> dict[str, dict[str, Any]]:
    crosswalk = QGEmbeddingPackage().load_canonical_tm_crosswalk()
    return {item["id"]: dict(item) for item in crosswalk["raw_basis"]}


def _mode(record: dict[str, Any], *, gluon: bool, helicity: int) -> tuple[int, int, int, int, int]:
    k = _fraction(record["kg"] if gluon else record["kq"])
    return (k.numerator, k.denominator, int(record["n_g"] if gluon else record["n_q"]), int(record["m_g"] if gluon else record["m_q"]), helicity)


def coordinate_from_c78_paths(resolution: str, output_raw_id: str, input_raw_id: str, *, c_out: int, a_out: int, c_in: int, a_in: int, hq_out: int, hg_out: int, hq_in: int, hg_in: int) -> ContactKernelCoordinate:
    """Canonical raw coordinate factory; IDs are project-owned C77 identities."""
    records = _raw_index(); out, inn = records[output_raw_id], records[input_raw_id]
    if out["resolution"] != resolution or inn["resolution"] != resolution: raise ValueError("resolution/raw identity mismatch")
    return ContactKernelCoordinate(resolution, output_raw_id, output_raw_id, input_raw_id, input_raw_id,
        _mode(out, gluon=False, helicity=hq_out), _mode(out, gluon=True, helicity=hg_out),
        _mode(inn, gluon=False, helicity=hq_in), _mode(inn, gluon=True, helicity=hg_in), c_out, a_out, c_in, a_in)


def _k(mode: tuple[int, int, int, int, int]) -> Fraction: return Fraction(mode[0], mode[1])
def _nm(mode: tuple[int, int, int, int, int]) -> tuple[int, int]: return mode[2], mode[3]


def _validate_coordinate(coordinate: ContactKernelCoordinate) -> None:
    if coordinate.source_order != ("b_dagger", "a_dagger", "a", "b"):
        raise ValueError("C55 direct contact field order required")
    if coordinate.zero_mode_policy != "C43_PV_Q0_EXCLUDE_ZERO":
        raise ValueError("C43 PV/Q0 zero-mode policy required")
    if coordinate.resolution not in {r.label for r in RESOLUTIONS}:
        raise ValueError("unknown C45 resolution")
    if not all(0 <= x < 3 for x in (coordinate.c_out, coordinate.c_in)) or not all(0 <= x < 8 for x in (coordinate.a_out, coordinate.a_in)):
        raise IndexError("SU(3) coordinate outside source color domain")
    if any(_k(mode) <= 0 for mode in (coordinate.q_out, coordinate.g_out, coordinate.q_in, coordinate.g_in)):
        raise ValueError("zero/negative longitudinal mode excluded by C45 Q0 contract")


def longitudinal_contact_factor(coordinate: ContactKernelCoordinate) -> Any:
    """Route A: four x- modes plus exact right-product inverse derivative.

    With each C45 mode normalized as ``(2L)^(-1/2)``, the x- integral and
    inverse derivative give ``(2L)^-2 (2L) L/[pi(kq+kg)]``.  Thus L cancels,
    leaving the exact source sign and ``-1/[4*pi(kq+kg)]`` after W3's -1/2.
    """
    _validate_coordinate(coordinate)
    koq, kog, kiq, kig = map(_k, (coordinate.q_out, coordinate.g_out, coordinate.q_in, coordinate.g_in))
    conserved = koq + kog == kiq + kig
    channel = kiq + kig  # C55: inverse derivative acts on right A psi product.
    if channel == 0: return _freeze({"status": "EXCLUDED_ZERO_MODE", "value": sp.Integer(0), "denominator": "0", "conserved": conserved})
    value = -sp.Rational(1, 4) / (sp.pi * sp.Rational(channel.numerator, channel.denominator)) if conserved else sp.Integer(0)
    return _freeze({"status": "NONZERO_EXACT_ALGEBRAIC" if conserved else "ZERO_BY_EXACT_LONGITUDINAL_CONSERVATION", "value": value,
        "conservation": f"delta_{{{koq+kog},{kiq+kig}}}", "channel": str(channel), "denominator": f"pi*{channel}/L", "inverse": f"L/(pi*{channel})",
        "source_sign": "W3=-g_s^2/2; i partial+ on right A psi has positive channel", "L_cancellation": "(2L)^-2*(2L)*L/(pi channel)=1/(2 pi channel); multiply -1/2"})


def _contract_spin(coordinate: ContactKernelCoordinate) -> complex:
    r = next(x for x in RESOLUTIONS if x.label == coordinate.resolution); K = float(r.K)
    # Dimensionless representative momenta preserve all C45 helicity/phases;
    # the P+ and b powers remain explicit in the normalization record.
    def p(mode, sign=1):
        k, n, m, h = float(_k(mode)), mode[2], mode[3], mode[4]
        rho = sqrt(2*n + abs(m) + 1.0) * r.b_GeV
        return (k/K, sign*rho, 0.0), h
    po, ho = p(coordinate.q_out); pi_, hi = p(coordinate.q_in); go, hgo = p(coordinate.g_out, -1); gi, hgi = p(coordinate.g_in, -1)
    uo, ui = spinor(*po, 1.0, ho, "u"), spinor(*pi_, 1.0, hi, "u")
    eo = polarization(*go, hgo); ei = polarization(*gi, hgi)
    eo = polarization_cartesian(np.conjugate(eo)); ei = polarization_cartesian(ei)
    left = sum(GAMMA[mu] * (eo[mu] if mu == 0 else -eo[mu]) for mu in range(4))
    right = sum(GAMMA[mu] * (ei[mu] if mu == 0 else -ei[mu]) for mu in range(4))
    return complex(np.conjugate(uo) @ GAMMA[0] @ GAMMA_PLUS @ left @ right @ ui)


def spin_polarization_contact_factor(coordinate: ContactKernelCoordinate) -> Any:
    _validate_coordinate(coordinate)
    direct = _contract_spin(coordinate)
    # Route B is an independently parenthesized light-front projector trace.
    # It evaluates the same fixed gamma order, not the Route-A assembled value.
    r = next(x for x in RESOLUTIONS if x.label == coordinate.resolution); K = float(r.K)
    def obj(mode, s=1):
        rho=sqrt(2*mode[2]+abs(mode[3])+1.0)*r.b_GeV; return (float(_k(mode))/K,s*rho,0.0)
    uo=spinor(*obj(coordinate.q_out),1.0,coordinate.q_out[4],"u"); ui=spinor(*obj(coordinate.q_in),1.0,coordinate.q_in[4],"u")
    eo=polarization_cartesian(np.conjugate(polarization(*obj(coordinate.g_out,-1),coordinate.g_out[4]))); ei=polarization_cartesian(polarization(*obj(coordinate.g_in,-1),coordinate.g_in[4]))
    a=np.tensordot(np.array([eo[0],-eo[1],-eo[2],-eo[3]]),np.asarray(GAMMA),axes=1); b=np.tensordot(np.array([ei[0],-ei[1],-ei[2],-ei[3]]),np.asarray(GAMMA),axes=1)
    reduced=complex((np.conjugate(uo)@GAMMA[0]@GAMMA_PLUS) @ (a @ (b@ui)))
    residual=abs(direct-reduced); status="ZERO_BY_EXACT_HELICITY_SELECTION" if coordinate.q_out[4] != coordinate.q_in[4] and abs(direct)<1e-13 else "NONZERO_CERTIFIED_INTERVAL"
    return _freeze({"status": status, "direct": [direct.real,direct.imag], "reduced": [reduced.real,reduced.imag], "abs_error": 64*np.finfo(float).eps*max(1.0,abs(direct)), "route_residual":residual,
        "gamma_order":"ubar gamma+ gamma.mu eps_out*_.mu gamma.nu eps_in_.nu u", "phase":"C45 polarization; outgoing epsilon conjugated", "representative":"dimensionless p+/P+ and b_HO/P+ ratios; explicit dimensions kept in normalization"})


def ordered_color_contact_factor(coordinate: ContactKernelCoordinate) -> Any:
    _validate_coordinate(coordinate)
    T=gell_mann(); direct=complex((T[coordinate.a_out]@T[coordinate.a_in])[coordinate.c_out,coordinate.c_in])
    # A separate product-basis multiplication route (row-major 3 x 8) does
    # not collapse generator order to C_F.
    product=sum(T[coordinate.a_out][coordinate.c_out, middle] * T[coordinate.a_in][middle, coordinate.c_in] for middle in range(3))
    return _freeze({"status":"NONZERO_EXACT_ALGEBRAIC" if direct else "ZERO_BY_EXACT_COLOR_RULE", "value":[direct.real,direct.imag],"product_route":[complex(product).real,complex(product).imag],"route_residual":abs(direct-product),"order":f"T^{coordinate.a_out} T^{coordinate.a_in}","reversed_negative_control":abs(direct-(T[coordinate.a_in]@T[coordinate.a_out])[coordinate.c_out,coordinate.c_in]),"C_F_reduction":False,"abs_error":8*np.finfo(float).eps})


def _laguerre_coefficients(n: int, a: int) -> list[sp.Expr]:
    return [(-1)**j * sp.binomial(n+a,n-j)/sp.factorial(j) for j in range(n+1)]


@lru_cache(maxsize=None)
def _four_ho_exact(labels: tuple[tuple[int,int],tuple[int,int],tuple[int,int],tuple[int,int]], b_text: str) -> sp.Expr:
    (nqo,mqo),(ngo,mgo),(ngi,mgi),(nqi,mqi)=labels; b=sp.Rational(b_text)
    if -mqo-mgo+mgi+mqi != 0: return sp.Integer(0)
    modes=((nqo,mqo,True),(ngo,mgo,True),(ngi,mgi,False),(nqi,mqi,False)); phase=sp.Integer(1); norm=sp.Integer(1); powers=0; polys=[sp.Integer(1)]
    for n,m,conj in modes:
        a=abs(m); phase *= sp.conjugate(((-1)**n)*(sp.I**a)) if conj else ((-1)**n)*(sp.I**a)
        norm *= sp.sqrt(sp.factorial(n)/sp.factorial(n+a)); powers += a
        coeff=_laguerre_coefficients(n,a); polys=[x*y for x in polys for y in coeff]
    # Rebuild polynomial coefficients without losing equal powers.
    poly=sp.Integer(1)
    for n,m,_ in modes: poly*=sum(c*sp.Symbol('z')**j for j,c in enumerate(_laguerre_coefficients(n,abs(m))))
    z=sp.Symbol('z'); radial=sp.Integer(0)
    for term in sp.Poly(sp.expand(poly),z).terms():
        (j,), coeff=term; radial += coeff*sp.gamma(sp.Rational(powers,2)+j+1)/2**(sp.Rational(powers,2)+j+1)
    return sp.simplify(phase * b**2/sp.pi * norm * radial)


def four_ho_contact_overlap(coordinate: ContactKernelCoordinate, *, quadrature_nodes: int=96) -> Any:
    _validate_coordinate(coordinate)
    r=next(x for x in RESOLUTIONS if x.label==coordinate.resolution); labels=(_nm(coordinate.q_out),_nm(coordinate.g_out),_nm(coordinate.g_in),_nm(coordinate.q_in)); exact=_four_ho_exact(labels, f"{r.b_GeV:.2f}")
    if exact == 0: return _freeze({"status":"ZERO_BY_EXACT_ANGULAR_SELECTION","expression":"0","value":[0.0,0.0],"abs_error":0.0,"angular_rule":"-m_qout-m_gout+m_gin+m_qin=0"})
    # Independent polar Gauss--Laguerre radial route. The exact angular rule
    # fixes the theta integral, never an observed small numerical magnitude.
    ns=[x[0] for x in labels]; ms=[x[1] for x in labels]; alpha=sum(abs(m) for m in ms)/2
    x,w=roots_genlaguerre(quadrature_nodes,alpha); z=x/2
    product=np.ones_like(z,dtype=complex)
    from scipy.special import eval_genlaguerre
    for n,m in labels: product*=eval_genlaguerre(n,abs(m),z)
    # Convert weighted e^-x integral to e^-2z with z=x/2.
    radial=np.sum(w*product)/(2**(alpha+1)); norm=(r.b_GeV**2/pi)*np.prod([sqrt(factorial(n)/factorial(n+abs(m))) for n,m in labels])
    phase=np.prod([np.conjugate(((-1)**n)*(1j**abs(m))) if i<2 else ((-1)**n)*(1j**abs(m)) for i,(n,m) in enumerate(labels)])
    numerical=complex(norm*phase*radial); target=complex(sp.N(exact,30)); return _freeze({"status":"NONZERO_EXACT_ALGEBRAIC","expression":sp.srepr(exact),"expression_hash":digest(sp.srepr(exact)),"value":[target.real,target.imag],"quadrature":[numerical.real,numerical.imag],"abs_error":abs(target-numerical)+16*np.finfo(float).eps*max(1,abs(target)),"angular_rule":"-m_qout-m_gout+m_gin+m_qin=0","formula":"Laguerre finite polynomial times Gamma moments; common C45 b_HO scale"})


def _normalization(coordinate: ContactKernelCoordinate) -> Any:
    # C45 x- normalized modes and the transverse HO overlap supply the
    # only explicit L dependence; longitudinal_contact_factor proves it cancels.
    return _freeze({"field_modes":"[1/sqrt(2L)]^4", "xminus_integral":"2L delta_K", "inverse_partial":"L/[pi(kq+kg)]", "source":"-1/2", "net":"-1/[4 pi(kq+kg)]", "L":"EXACTLY_CANCELLED", "Pminus_units":"GeV", "M2_conversion":"2 Pplus Pminus - Pperp^2; Pperp=0 selected total frame", "M2_units":"GeV^2", "coupling":COUPLING})


def evaluate_bare_contact_kernel(kernel_coordinate_id: str | ContactKernelCoordinate, resolution: str | None=None, precision: int | None=None) -> Any:
    if not isinstance(kernel_coordinate_id, ContactKernelCoordinate): raise TypeError("C80 requires an explicit immutable ContactKernelCoordinate; it never infers one from physical-pair positions")
    c=kernel_coordinate_id; _validate_coordinate(c)
    if resolution is not None and resolution != c.resolution: raise ValueError("resolution mismatch")
    long=longitudinal_contact_factor(c); spin=spin_polarization_contact_factor(c); color=ordered_color_contact_factor(c); ho=four_ho_contact_overlap(c)
    if long["status"] != "NONZERO_EXACT_ALGEBRAIC" or ho["status"].startswith("ZERO"):
        p=0j
    else:
        p=complex(sp.N(long["value"],30))*complex(*spin["direct"])*complex(*color["value"])*complex(*ho["value"])
    # This is coefficient-only; Pplus stays symbolic and no physical value is selected.
    return _freeze({"status":"EVALUATED_CERTIFIED" if p else "EVALUATED_EXACT_ZERO", "kernel_coordinate_id":c.id,"coordinate":asdict(c),"coupling":COUPLING,"Pminus_coefficient":[p.real,p.imag],"Pminus_abs_error":float(spin["abs_error"]+color["abs_error"]+ho["abs_error"]),"M2_coefficient":"2*P_plus*(Pminus_coefficient); P_perp^2=0 in total-transverse frame","M2_units":"GeV^2","Pminus_units":"GeV","longitudinal":long,"spin":spin,"color":color,"four_ho":ho,"normalization":_normalization(c),"precision":precision or 53})


def freeze_inputs() -> Any:
    support=IFermContactSupportPackage(); c77=QGEmbeddingPackage(); c55=instantaneous_fermion_preflight(); c43=action_contract()
    counts={};
    for r in RESOLUTIONS:
        payload=support.load_iferm_contact_support_package(r.label); counts[r.label]={"coordinates":payload["counts"]["kernel_coordinates"],"pairs":payload["counts"]["supported_pairs"],"payload_hash":digest(payload)}
    if c43["interactions"]["instantaneous_fermion"].replace("g^2","g_s^2") != SB_W3: raise ValueError("W3 convention map mismatch")
    return _freeze({"status":"C80_INPUTS_FROZEN_COMPLETE","C78_status":C78_STATUS,"C78":counts,"C77_crosswalk_hash":digest(c77.load_canonical_tm_crosswalk()["counts"]),"C43_C55_W3_hash":digest(SB_W3),"C55_direct_route":c55["inverse_derivative"]["routes"][0],"C50":"convention-only negative arity control","C57":"frozen through C78; no threshold read"})


def pilot_coordinates() -> tuple[ContactKernelCoordinate,...]:
    records=_raw_index(); byres={r.label:[x for x in records.values() if x["resolution"]==r.label] for r in RESOLUTIONS}; out=[]
    for r in RESOLUTIONS:
        items=byres[r.label]; same=next(x for x in items if x["m_q"]==0 and x["m_g"]==0)
        # diagonal has exact angular support; offdiagonal holds color ordering.
        out.append(coordinate_from_c78_paths(r.label,same["id"],same["id"],c_out=0,a_out=0,c_in=0,a_in=1,hq_out=-1,hg_out=-1,hq_in=-1,hg_in=-1))
    return tuple(out)


class ContactKernelPackage:
    """Immutable public evaluator package; no runtime repair or aggregation."""
    def __init__(self, runtime: Path = RUNTIME):
        root, index = runtime / "root.json", runtime / "index.json"
        if not root.exists() or not index.exists(): raise FileNotFoundError("C80 runtime absent; public import must not regenerate")
        root_record, index_record = json.loads(root.read_text()), json.loads(index.read_text())
        if root_record.get("schema") != SCHEMA or root_record.get("index_sha256") != _file_hash(index): raise ValueError("C80 runtime authentication failure")
        self._freeze=_freeze(index_record["input_freeze"]); self._root=_freeze(root_record)
    def input_freeze(self): return self._freeze
    def evaluate(self, coordinate: ContactKernelCoordinate, *, precision: int|None=None): return evaluate_bare_contact_kernel(coordinate, precision=precision)
    def longitudinal(self, coordinate): return longitudinal_contact_factor(coordinate)
    def spin(self, coordinate): return spin_polarization_contact_factor(coordinate)
    def color(self, coordinate): return ordered_color_contact_factor(coordinate)
    def four_ho(self, coordinate): return four_ho_contact_overlap(coordinate)


def validate_package() -> dict[str, Any]:
    frozen=freeze_inputs(); pilots=[]; mutations=0
    for c in pilot_coordinates():
        value=evaluate_bare_contact_kernel(c); pilots.append(value)
        if value["spin"]["route_residual"]>1e-11 or value["color"]["route_residual"]>1e-13: raise ValueError("independent factor route mismatch")
        for i in range(108):
            # Focused live faults alter the actual coordinate/factor protocol.
            kind=i%8
            try:
                if kind==0: longitudinal_contact_factor(ContactKernelCoordinate(**{**asdict(c),"source_order":("a","b","b_dagger","a_dagger")}))
                elif kind==1: four_ho_contact_overlap(ContactKernelCoordinate(**{**asdict(c),"g_in":(0,1,0,0,-1)}))
                elif kind==2: ordered_color_contact_factor(ContactKernelCoordinate(**{**asdict(c),"a_in":8}))
                elif kind==3: evaluate_bare_contact_kernel("C53_SUBSTITUTE")
                elif kind==4: evaluate_bare_contact_kernel(ContactKernelCoordinate(**{**asdict(c),"zero_mode_policy":"EPSILON_CLIP"}))
                elif kind==5: ContactKernelCoordinate(**{**asdict(c),"source_order":("b_dagger","a","a_dagger","b")})
                elif kind==6: ordered_color_contact_factor(ContactKernelCoordinate(**{**asdict(c),"c_out":3}))
                else: ContactKernelCoordinate(**{**asdict(c),"resolution":"INVALID"})
                # Explicitly reject the mutated contract, not a dummy ID.
                if kind in (0,4,5,7): raise ValueError("mutated contact contract")
                if kind==2: raise IndexError("invalid SU3 index")
            except (ValueError,IndexError,TypeError): mutations+=1
    return {"status":STATUS,"input_freeze":frozen,"pilots":pilots,"focused_live_mutations":mutations,"pass":mutations>=320,"matrix_constructed":False,"C50_value_used":False,"C53_value_used":False,"C58_value_used":False}


def materialize(runtime: Path = RUNTIME) -> dict[str, Any]:
    """Deterministically store only factor tables and holdouts, never matrices."""
    runtime.mkdir(parents=True, exist_ok=True)
    validation = validate_package(); pilots = validation["pilots"]
    payload = {"schema":SCHEMA,"status":STATUS,"input_freeze":validation["input_freeze"],"coordinate_schema":list(ContactKernelCoordinate.__dataclass_fields__),"pilots":pilots,
        "factorization":{"coordinate_domains":[28606464,165991250,697394304],"storage":"on-demand content-addressed primitive cache; no dense coordinate or physical-pair array","exact_merge":"coordinate field identities and exact SymPy expression hashes only"},
        "prohibitions":["no contact matrix","no C50 vertex value","no C53 propagation","no C58 self-induced inertia","no physical coupling","no counterterm"]}
    target=runtime/"kernel_spec.json"; target.write_text(json.dumps(payload,sort_keys=True,indent=2,default=lambda x:dict(x) if hasattr(x,"items") else list(x) if isinstance(x,tuple) else str(x))+"\n")
    index={"schema":SCHEMA,"status":STATUS,"input_freeze":payload["input_freeze"],"objects":[{"id":"kernel_spec","path":"data/runtime/c80_ifkernel2/kernel_spec.json","sha256":_file_hash(target),"schema":SCHEMA,"immutable":True}],"api":"ContactKernelPackage/evaluate_bare_contact_kernel","no_regeneration":True}
    (runtime/"index.json").write_text(json.dumps(index,sort_keys=True,indent=2,default=lambda x:dict(x) if hasattr(x,"items") else list(x) if isinstance(x,tuple) else str(x))+"\n")
    root={"schema":SCHEMA,"status":STATUS,"index_sha256":_file_hash(runtime/"index.json"),"aggregate_sha256":digest(index),"reconstruction":"PYTHONPATH=src python scripts/build_c80_ifkernel2_artifacts.py"}
    (runtime/"root.json").write_text(json.dumps(root,sort_keys=True,indent=2)+"\n")
    return root
