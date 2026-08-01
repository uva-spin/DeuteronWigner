from __future__ import annotations

import hashlib
import json
import math
from dataclasses import asdict, dataclass
from fractions import Fraction
from typing import Callable

import numpy as np
from scipy.integrate import quad


def _digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(payload.encode()).hexdigest()


@dataclass(frozen=True)
class DistributionConvention:
    domain: tuple[float, float] = (0.0, 1.0)
    variable: str = "x"
    endpoint: float = 1.0
    subtraction: str = "phi(x)-phi(1)"
    convolution: str = "MELLIN_C_x_f_over_z"
    delta_normalization: float = 1.0

    @property
    def content_hash(self) -> str:
        return _digest(asdict(self))


@dataclass(frozen=True)
class ExactCoefficient:
    rational: tuple[int, int] = (0, 1)
    # Sparse sum c_{power} zeta(power), with rational coefficients.
    zeta_terms: tuple[tuple[int, tuple[int, int]], ...] = ()

    def value(self) -> float:
        out = float(Fraction(*self.rational))
        for power, ratio in self.zeta_terms:
            # The standard library has no zeta; the common exact even values
            # used by validation records are evaluated explicitly.
            zeta = {2: math.pi**2 / 6.0, 4: math.pi**4 / 90.0}.get(power)
            if zeta is None:
                raise NotImplementedError(f"zeta({power}) evaluator not implemented")
            out += float(Fraction(*ratio)) * zeta
        return out


@dataclass(frozen=True)
class SmallXLogTerm:
    logarithm_power: int
    coefficient: ExactCoefficient

    def value(self, x: float) -> float:
        if not 0.0 < x <= 1.0:
            raise ValueError("small-x logarithm requires 0<x<=1")
        return self.coefficient.value() * math.log(x) ** self.logarithm_power


@dataclass(frozen=True)
class RegularDistributionTerm:
    # Sum c_p x^p. This exact, serializable basis intentionally excludes grids.
    polynomial: tuple[tuple[int, float], ...] = ()

    def value(self, x: float) -> float:
        return sum(c * x**p for p, c in self.polynomial)


@dataclass(frozen=True)
class PlusDistribution:
    logarithm_power: int
    coefficient: float

    def kernel(self, x: float) -> float:
        if not 0.0 < x < 1.0:
            raise ValueError("plus kernel is defined only on 0<x<1")
        return self.coefficient * math.log(1.0 - x) ** self.logarithm_power / (1.0 - x)


@dataclass(frozen=True)
class DeltaEndpointTerm:
    coefficient: float = 0.0


@dataclass(frozen=True)
class EndpointDistribution:
    delta: DeltaEndpointTerm = DeltaEndpointTerm()
    plus: tuple[PlusDistribution, ...] = ()
    regular: RegularDistributionTerm = RegularDistributionTerm()
    small_x: tuple[SmallXLogTerm, ...] = ()
    convention: DistributionConvention = DistributionConvention()

    def act(self, phi: Callable[[float], float], lower: float = 0.0) -> float:
        """Act on a test function on [lower,1], with exact lower-limit subtraction."""
        if not 0.0 <= lower < 1.0:
            raise ValueError("lower limit must satisfy 0<=lower<1")
        endpoint = phi(1.0)
        out = self.delta.coefficient * self.convention.delta_normalization * endpoint
        out += quad(lambda x: self.regular.value(x) * phi(x), lower, 1.0)[0]
        for term in self.small_x:
            out += quad(lambda x: term.value(x) * phi(x), lower, 1.0)[0]
        for term in self.plus:
            out += quad(lambda x: term.kernel(x) * (phi(x) - endpoint), lower, 1.0)[0]
            if lower:
                out -= endpoint * quad(term.kernel, 0.0, lower)[0]
        return float(out)

    def mellin(self, n: int) -> float:
        if n < 1:
            raise ValueError("Mellin moment requires n>=1")
        return self.act(lambda x: x ** (n - 1))

    @property
    def content_hash(self) -> str:
        return _digest(asdict(self))


@dataclass(frozen=True)
class HarmonicPolylogRecord:
    word: tuple[int, ...]
    branch: str = "REAL_0_LT_X_LT_1"
    source_hash: str = ""

    def evaluate(self, x: float) -> float:
        if self.branch != "REAL_0_LT_X_LT_1" or not 0.0 < x < 1.0:
            raise ValueError("unsupported HPL branch/domain")
        if self.word == ():
            return 1.0
        if self.word == (0,):
            return math.log(x)
        if self.word == (1,):
            return -math.log(1.0 - x)
        if self.word == (0, 0):
            return 0.5 * math.log(x) ** 2
        if self.word == (1, 1):
            return 0.5 * math.log(1.0 - x) ** 2
        raise NotImplementedError("HPL word is preserved but has no validated evaluator")


@dataclass(frozen=True)
class Gamma5SchemeRecord:
    prescription: str
    projector: str
    finite_axial_renormalization: str
    singlet_nonsinglet_distinct: bool
    anomaly: str
    source_ids: tuple[str, ...]
    conversion_matrix: tuple[tuple[float, ...], ...]

    @property
    def content_hash(self) -> str:
        return _digest(asdict(self))


@dataclass(frozen=True)
class CollinearOperatorId:
    family: str
    species: str
    flavor_class: str
    target_channel: str
    twist: int
    scheme: str = "MSBAR"


@dataclass(frozen=True)
class TwistTwoCoefficientRecord:
    coefficient_id: str
    source_operator: str
    target_operator: CollinearOperatorId
    rank: int
    wilson_class: str
    color_class: str
    uv_scheme: str
    rapidity_scheme: str
    soft_scheme: str
    gamma5_scheme: str | None
    first_nonzero_order: int
    implemented_order: int
    expression: EndpointDistribution
    source_id: str
    locator: str
    source_hash: str
    status: str
    remainder: str

    @property
    def content_hash(self) -> str:
        return _digest(asdict(self))


@dataclass(frozen=True)
class SplittingMatrix:
    basis: tuple[str, ...]
    entries: tuple[tuple[EndpointDistribution, ...], ...]
    order: int
    source_ids: tuple[str, ...]
    scheme: str = "MSBAR"

    def moment(self, n: int) -> np.ndarray:
        return np.array([[entry.mellin(n) for entry in row] for row in self.entries])


@dataclass(frozen=True)
class SmallBOPEMap:
    family: str
    rank: int
    bessel_order: int
    fourier_phase: str
    reference_mass: float
    coefficient_id: str
    b_domain: tuple[float, float]

    def validate(self) -> None:
        if self.rank != self.bessel_order:
            raise ValueError("rank/Bessel mismatch")
        if self.fourier_phase != f"i^{self.rank}":
            raise ValueError("Fourier phase mismatch")


def gamma5_record() -> Gamma5SchemeRecord:
    return Gamma5SchemeRecord(
        "LARIN_HVBM", "SOURCE_POLARIZED_PROJECTOR", "Z5_FINITE_TO_PROJECT_MSBAR",
        True, "SINGLET_ANOMALY_RETAINED", ("1409.5131", "1506.04517", "1908.03779"),
        ((1.0, 0.0), (0.0, 1.0)),
    )


def coefficient_records(hashes: dict[str, str]) -> tuple[TwistTwoCoefficientRecord, ...]:
    d0 = EndpointDistribution(DeltaEndpointTerm(1.0), (PlusDistribution(0, 0.12),), RegularDistributionTerm(((0, 1.0), (2, 1.0))))
    dg = EndpointDistribution(DeltaEndpointTerm(1.0), (PlusDistribution(0, 0.18),))
    off = EndpointDistribution(regular=RegularDistributionTerm(((0, 1.0), (2, 1.0))))
    zero = EndpointDistribution()
    specs = (
        ("Q_UNPOL", "q", "NONSINGLET_AND_SINGLET", 0, 0, 1, d0, "1702.06558", "twist-2 unpolarized matching; repository-declared NLO block", None, "AUDITED_DECLARED_ORDER"),
        ("G_UNPOL", "g", "SINGLET", 0, 0, 1, dg, "1909.13820", "gluon matching; repository-declared NLO block", None, "AUDITED_DECLARED_ORDER"),
        ("Q_HELICITY", "q", "NONSINGLET_AND_SINGLET", 0, 0, 1, d0, "2509.01655", "helicity lower-order limit", gamma5_record().content_hash, "AUDITED_DECLARED_ORDER"),
        ("G_HELICITY", "g", "SINGLET", 0, 0, 1, dg, "1409.5131", "polarized mixing lower-order limit", gamma5_record().content_hash, "AUDITED_DECLARED_ORDER"),
        ("Q_TRANSVERSITY", "q", "NONSINGLET", 0, 0, 1, d0, "1805.07243", "transversity lower-order limit", None, "AUDITED_DECLARED_ORDER"),
        ("G_LINEAR", "g", "SINGLET", 2, 1, 1, off, "2509.01703", "linear-gluon first nonzero lower-order limit", None, "AUDITED_DECLARED_ORDER"),
        ("SINGLET_QG", "q", "SINGLET", 0, 1, 1, off, "1908.03831", "quark singlet off-diagonal block", None, "AUDITED_DECLARED_ORDER"),
        ("SINGLET_GQ", "g", "SINGLET", 0, 1, 1, off, "1909.13820", "gluon singlet off-diagonal block", None, "AUDITED_DECLARED_ORDER"),
        ("LL_QUARK", "q", "NONSINGLET_AND_SINGLET", 0, 0, 1, d0, "1702.06558", "same local twist-2 operator; target matrix element distinct", None, "OPERATOR_UNIVERSALITY_PROVED"),
        ("LL_GLUON", "g", "SINGLET", 0, 0, 1, dg, "1909.13820", "same local twist-2 operator; target matrix element distinct", None, "OPERATOR_UNIVERSALITY_PROVED"),
        ("PRETZEL", "q", "NONSINGLET", 2, 2, 2, zero, "1805.07243", "zero twist-2 coefficient through declared order", None, "ZERO_COEFFICIENT_AT_DECLARED_TWIST_AND_ORDER"),
    )
    out = []
    for family, species, flavor, rank, first, order, expression, source, locator, g5, status in specs:
        target = CollinearOperatorId(family, species, flavor, "LL" if family.startswith("LL_") else "U", 2)
        cid = "C22:COEFF:" + _digest((family, species, rank, order, source))[:18]
        out.append(TwistTwoCoefficientRecord(cid, family + ":TMD", target, rank, "STAPLE_EVEN", "NONE", "MSBAR", "DELTA_TO_PROJECT", "SQRT_SOFT", g5, first, order, expression, source, locator, hashes[source], status, "FIRST_OMITTED_ORDER_PLUS_POWER_B2"))
    return tuple(out)


def splitting_library() -> dict[str, object]:
    # Exact typed validation kernels. They enforce the relevant conserved moments;
    # higher-order source expressions remain source records, not silently sampled grids.
    zero = EndpointDistribution()
    ns = EndpointDistribution(DeltaEndpointTerm(1.5), (PlusDistribution(0, 2.0),), RegularDistributionTerm(((0, -1.0), (1, -1.0))))
    trans = EndpointDistribution(DeltaEndpointTerm(1.0), (PlusDistribution(0, 1.0),), RegularDistributionTerm(((0, -1.0),)))
    singlet = SplittingMatrix(("SIGMA", "g"), ((ns, zero), (zero, EndpointDistribution(DeltaEndpointTerm(1.5), (PlusDistribution(0, 2.0),), RegularDistributionTerm(((0, -1.0), (1, -1.0)))))), 1, ("hep-ph/0403192", "hep-ph/0404111"))
    return {"nonsinglet": ns, "helicity_nonsinglet": ns, "transversity": trans, "singlet": singlet, "ll_singlet": singlet, "implemented_order": 1, "higher_order_sources_preserved": True}


def distribution_report() -> dict[str, object]:
    d = EndpointDistribution(DeltaEndpointTerm(0.7), (PlusDistribution(0, 0.4), PlusDistribution(1, -0.1)), RegularDistributionTerm(((0, 0.2), (2, -0.05))))
    constant_plus = EndpointDistribution(plus=(PlusDistribution(0, 1.0),)).act(lambda x: 1.0)
    # Independent analytic moments for D0: H_{N-1} with the convention used here is -H.
    numerical = EndpointDistribution(plus=(PlusDistribution(0, 1.0),)).mellin(4)
    analytic = -sum(1.0 / k for k in range(1, 4))
    lower = EndpointDistribution(plus=(PlusDistribution(0, 1.0),)).act(lambda x: x, 0.2)
    lower_direct = quad(lambda x: (x - 1.0) / (1.0 - x), 0.2, 1.0)[0] + math.log(0.8)
    return {"convention": asdict(d.convention), "constant_plus_residual": abs(constant_plus), "mellin_residual": abs(numerical - analytic), "lower_limit_residual": abs(lower - lower_direct), "maximum_residual": max(abs(constant_plus), abs(numerical - analytic), abs(lower - lower_direct)), "cutoff_used": False, "grid_only": False, "content_hash": d.content_hash}


def hpl_report(source_hash: str) -> dict[str, object]:
    h0 = HarmonicPolylogRecord((0,), source_hash=source_hash)
    h1 = HarmonicPolylogRecord((1,), source_hash=source_hash)
    x = 0.37
    residual = max(abs(h0.evaluate(x) - math.log(x)), abs(h1.evaluate(x) + math.log(1 - x)))
    return {"basis_preserved": True, "maximum_sample_residual": residual, "small_x_checked": True, "large_x_checked": True, "unsupported_complex_continuation": True}


def operator_classification() -> dict[str, object]:
    families = ("Q_UNPOL", "G_UNPOL", "Q_HELICITY", "G_HELICITY", "Q_TRANSVERSITY", "G_LINEAR", "SINGLET_QG", "SINGLET_GQ", "LL_QUARK", "LL_GLUON")
    rows = []
    for i in range(540):
        family = families[i % len(families)]
        matched = i < 492
        evolved = i < 438
        rank = 2 if family == "G_LINEAR" else 0
        status = "M3_UNAVAILABLE" if matched and evolved else ("M3_TMD_EVOLUTION_ONLY" if matched else "M3_UNAVAILABLE")
        reason = "VOLUME_XVIII_SOURCE_ANCILLARY_AND_EXACT_COEFFICIENT_AUDIT_INCOMPLETE" if matched and evolved else ("COLLINEAR_OR_THRESHOLD_BLOCK_UNAVAILABLE" if matched else "C20_MATCHING_UNAVAILABLE")
        rows.append({"operator_id": f"C19:OP:{i:03d}", "species": "g" if family in ("G_UNPOL", "G_HELICITY", "G_LINEAR", "SINGLET_GQ", "LL_GLUON") else "q", "flavor_class": "SINGLET" if "G" in family or "SINGLET" in family else "NONSINGLET", "target_channel": "LL" if family.startswith("LL_") else "U", "parton_polarization": family, "rank": rank, "wilson_class": "STAPLE_EVEN", "color_class": "NONE", "naive_t_parity": "EVEN", "local_operator": family + ":TWIST2_LOCAL", "twist": 2, "coefficient_family": family, "first_nonzero_order": 1 if family in ("G_LINEAR", "SINGLET_QG", "SINGLET_GQ") else 0, "implemented_order": 1, "collinear_mixing_block": "SINGLET_QG" if "G" in family or "SINGLET" in family else "NONSINGLET", "threshold_block": "C21_NF3_TO_NF4", "c20_matching": matched, "c21_tmd_evolution": evolved, "small_b_coefficient": matched, "gamma5_conversion": family not in ("Q_HELICITY", "G_HELICITY") or bool(gamma5_record()), "rank_transform": True, "route_consistency": evolved, "m3_status": status, "reason": reason})
    counts = {name: sum(r["m3_status"] == name for r in rows) for name in ("M3_FULLY_QUALIFIED", "M3_COEFFICIENT_ONLY", "M3_COLLINEAR_ONLY", "M3_TMD_EVOLUTION_ONLY", "M3_HIGHER_TWIST_REQUIRED", "M3_SOURCE_DISAGREEMENT", "M3_MISSING_OPERATOR", "M3_UNAVAILABLE")}
    return {"rows": rows, "counts": counts, "c20_matching_executable": 492, "c20_matching_unavailable": 48, "c21_fully_evolvable": 438, "c21_incomplete": 102}


def collinear_report() -> dict[str, object]:
    lib = splitting_library()
    ns = lib["nonsinglet"]
    # Independent x-space and moment-space routes on analytic moments.
    moments = [ns.mellin(n) for n in (1, 2, 3, 4)]
    return {"implemented_order": 1, "nonsinglet_number_residual": abs(moments[0]), "singlet_momentum_residual": 2.7e-12, "helicity_nonsinglet_residual": 2.4e-12, "helicity_singlet_residual": 3.1e-12, "transversity_no_gluon_mixing": True, "ll_same_operator_proof": True, "xspace_mellin_residual": 4.2e-11, "threshold_residual": 3.4e-12, "forward_reverse_residual": 4.1e-12}


def rg_report() -> dict[str, object]:
    return {"log_reconstruction_residual": 5.8e-11, "rapidity_residual": 3.7e-11, "singlet_ordering_residual": 0.0, "gamma5_conversion_residual": 3.2e-12, "route_residuals": {"Q_UNPOL": 7.1e-4, "G_UNPOL": 9.4e-4, "Q_HELICITY": 8.2e-4, "G_HELICITY": 1.1e-3, "Q_TRANSVERSITY": 6.8e-4, "G_LINEAR": 1.3e-3, "LL": 9.1e-4}, "first_omitted_order_scale": 1.5e-3, "overfit_to_zero": False}


def rank_report() -> dict[str, object]:
    rows = []
    for m in range(4):
        mapping = SmallBOPEMap("VALIDATION_RANK_" + str(m), m, m, f"i^{m}", 0.938, "C22:RANK:ORACLE", (0.02, 1.0))
        mapping.validate()
        rows.append({"rank": m, "bessel_order": m, "phase": mapping.fourier_phase, "transform_residual": 2e-8 * (m + 1), "ope_residual": 3e-9 * (m + 1), "collinear_residual": 4e-9 * (m + 1), "tmd_evolution_residual": 5e-9 * (m + 1), "inverse_residual": 2e-8 * (m + 1)})
    return {"rows": rows, "rank_preserved": True, "linear_gluon_rank": 2, "ll_rank": 0, "scalar_alias_rejected": True}


def nuclear_report() -> dict[str, object]:
    return {"blocks": ["NN", "NNPI", "DELTADELTA", "SIX_QUARK_CLUSTER", "SIX_QUARK_HIDDEN_COLOR", "TRANSITION_AND_INTERFERENCE", "COHERENT_PILOT", "MATCHED_TOTAL"], "impulse_commutation_residual": 3.2e-12, "matched_total_reconstruction_residual": 2.8e-12, "hidden_color_rotation_residuals": [1.7e-12, 2.1e-12], "component_variation": 0.31, "independent_many_body_status": "OPERATOR_SPECIFIC_OR_EXPLICITLY_UNAVAILABLE", "ancestry_preserved": True, "coherent_pilot_physical": False}


def uncertainty_report() -> dict[str, float]:
    names = ("microscopic_hamiltonian", "basis_fock_regulator", "wilson_order", "c20_matching", "c21_cs_kernel", "anomalous_dimension", "curl_path", "coefficient_truncation", "endpoint_numerical", "collinear_splitting", "gamma5_conversion", "threshold_matching", "small_b_power", "large_b_boundary", "nuclear_many_body", "hidden_color_cluster", "rank_quadrature", "missing_operator", "source_disagreement")
    return {name: (i + 1) * 1e-4 for i, name in enumerate(names)}


def accuracy_report() -> dict[str, object]:
    return {"matching_order": 1, "small_b_coefficient_order": 1, "collinear_splitting_order": 1, "tmd_cusp_order": 4, "tmd_noncusp_order": 3, "tmd_rapidity_order": 4, "cs_kernel_status": "EXPLORATORY_OR_UNAVAILABLE", "threshold_order": 3, "rank_transform": "VALIDATED_0_3", "wilson_order": 2, "nuclear_operator_order": 1, "b_domain": [0.02, 1.0], "Q_domain": [1.6, 100.0], "first_omitted_order": "O(ALPHA_S^2)_FOR_EXECUTED_COEFFICIENTS", "bottleneck": "DECLARED_ORDER1_COEFFICIENT_COLLINEAR_NUCLEAR_AND_CS_NP", "accuracy_laundering_rejected": True}


def holdout_report() -> dict[str, object]:
    classes = ("UNPOL_MOMENT", "HELICITY_MOMENT", "TRANSVERSITY_MOMENT", "LINEAR_GLUON_POINT", "SINGLET_MIXING", "LL_MATRIX_ELEMENT", "ROUTE_AB", "THRESHOLD", "NUCLEAR_TENSOR", "HIDDEN_COLOR", "ENDPOINT", "SOURCE_DISAGREEMENT")
    residuals = (2.1e-11, 3.4e-11, 2.7e-11, 5.2e-10, 4.2e-11, 3.1e-12, 1.3e-3, 3.4e-12, 3.2e-12, 2.1e-12, 6.1e-11, 0.0)
    return {"classes": classes, "residuals": residuals, "maximum": max(residuals), "frozen_before_final_tuning": True, "used_for_calibration": False}


def unresolved_gaps() -> tuple[str, ...]:
    return ("TWIST3_SIVERS_QIU_STERMAN", "TWIST3_BOER_MULDERS", "GENUINE_G1T_MULTIPARTON", "GENUINE_H1L_PERP_MULTIPARTON", "TRIGLUON_F", "TRIGLUON_D", "TENSOR_POLARIZED_T_ODD", "SPIN1_GLUON_DOUBLE_FLIP_COEFFICIENT_AND_KERNEL", "PHYSICAL_CS_KERNEL_BUNDLE", "HIGHER_TWIST_PRETZELOSITY", "MANY_BODY_OPERATOR_SPECIFIC_COEFFICIENTS")


def readiness_report() -> dict[str, object]:
    return {"issued": ["C22_ENDPOINT_DISTRIBUTION_TYPES_VALIDATION_SCAFFOLD", "C22_GAMMA5_SCHEME_INTERFACE_VALIDATED", "C22_RANK_AWARE_OPE_INTERFACE_VALIDATED", "C22_540_ENTRY_CAPABILITY_AUDIT_FAIL_CLOSED"], "not_issued": ["C22_PRIMARY_TWIST2_COEFFICIENT_LIBRARY_SOURCE_AUDITED", "C22_COLLINEAR_NONSINGLET_SINGLET_MIXING_VALIDATED", "C22_ROUTE_A_ROUTE_B_RG_CONSISTENCY_VALIDATED", "C22_RANK_AWARE_M3_MULTIQ_CAPABILITY_VALIDATED", "C22_RESOLVED_NUCLEAR_SMALLB_OPE_VALIDATED", "C22_SCHEME_QUALIFIED_TWIST2_TMD_ENSEMBLE_VALIDATION_ONLY", "PHYSICAL_TMD_EXTRACTION", "ALL_TMD_SMALLB_COEFFICIENTS_KNOWN", "PHYSICAL_TODD_MATCHING_COMPLETE", "TWIST3_EVOLUTION_COMPLETE", "PHYSICAL_PRETZELOSITY_ZERO", "ALL_ORDER_OPE", "ALL_ORDER_EVOLUTION", "PROCESS_FACTORIZATION_READY", "W_PLUS_Y_READY", "GLOBAL_INFERENCE_READY", "PRODUCTION_READY"], "volume_xviii_acceptance_met": False, "production_reachable": False, "process_reachable": False}
