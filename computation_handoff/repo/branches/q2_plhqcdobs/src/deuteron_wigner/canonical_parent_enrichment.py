"""Parent-level enrichment objects shared by every leading-twist spin-1 TMD.

The classes in this module act on complete correlators.  They intentionally
do not accept a TMD name, preventing a mechanism from being attached to one
projection while silently omitting the other projections of the same parent.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

from .quark_correlator import Spin1QuarkCorrelator
from .gluon_correlator import Spin1GluonCorrelator
from .nucleon_quark_correlator import (
    NUCLEON_QUARK_TMD_NAMES,
    SpinHalfQuarkCorrelator,
    compose_spin_half_quark_correlator,
)
from .spin import spin_one_basis


class WilsonChannel(str, Enum):
    QUARK_SPECTATOR = "quark_spectator"
    GLUON_SPECTATOR = "gluon_spectator"
    SP = "S_P"
    SD = "S_D"
    PP = "P_P"


def project_spin1_quark_parent_positivity(
    parent: Spin1QuarkCorrelator,
    *,
    safety_fraction: float = 0.98,
    tolerance: float = 1e-12,
) -> tuple[Spin1QuarkCorrelator, float]:
    """Scale the complete polarized spin-1 parent into the PSD cone.

    The trace-normalized unpolarized target x quark-spin density is fixed.
    Every vector-polarized, tensor-polarized, axial, transverse, T-even, and
    T-odd displacement receives one common factor.  This is therefore a
    joint-parent completion, never a per-TMD clip.
    """

    if not 0.0 < safety_fraction <= 1.0:
        raise ValueError("positivity safety fraction must lie in (0,1]")
    if not parent.is_target_hermitian():
        raise ValueError("cannot positivity-project a non-Hermitian parent")
    if parent.minimum_positivity_eigenvalue() >= -tolerance:
        return parent, 1.0
    scalar = float(np.trace(parent.vector).real / 3.0)
    if scalar <= 0.0:
        zero = Spin1QuarkCorrelator(
            np.zeros((3, 3), complex), np.zeros((3, 3), complex),
            np.zeros((2, 3, 3), complex),
        )
        return zero, 0.0
    identity = scalar*np.eye(3, dtype=np.complex128)

    def candidate(scale: float) -> Spin1QuarkCorrelator:
        return Spin1QuarkCorrelator(
            identity + scale*(parent.vector-identity),
            scale*parent.axial, scale*parent.transverse,
        )

    low, high = 0.0, 1.0
    for _ in range(64):
        middle = 0.5*(low+high)
        if candidate(middle).minimum_positivity_eigenvalue() >= 0.0:
            low = middle
        else:
            high = middle
    result = candidate(safety_fraction*low)
    if result.minimum_positivity_eigenvalue() < -tolerance:
        raise ValueError("spin-1 parent positivity projection failed")
    return result, float(safety_fraction*low)


def project_spin1_gluon_parent_positivity(
    parent: Spin1GluonCorrelator,
    momentum_gev: tuple[float, float],
    mass_gev: float,
    *,
    safety_fraction: float = 0.98,
    tolerance: float = 1.0e-12,
) -> tuple[Spin1GluonCorrelator, float]:
    """Project a complete gluon parent into the allowed PSD model cone.

    ``f1`` is held fixed and every other allowed spin, tensor,
    linear-polarization, and T-odd coefficient receives one common factor.
    """

    from .gluon_correlator import (
        compose_spin1_gluon_correlator,
        project_to_allowed_spin1_gluon_basis,
    )

    if not 0.0 < safety_fraction <= 1.0:
        raise ValueError("positivity safety fraction must lie in (0,1]")
    _, values, _ = project_to_allowed_spin1_gluon_basis(
        parent.values, momentum_gev, mass_gev
    )

    def candidate(scale: float) -> Spin1GluonCorrelator:
        trial = {
            name: value if name == "f1" else scale*value
            for name, value in values.items()
        }
        return compose_spin1_gluon_correlator(
            momentum_gev, mass_gev, trial
        )

    if candidate(1.0).minimum_positivity_eigenvalue() >= -tolerance:
        return candidate(1.0), 1.0
    low, high = 0.0, 1.0
    for _ in range(64):
        middle = 0.5*(low+high)
        if candidate(middle).minimum_positivity_eigenvalue() >= 0.0:
            low = middle
        else:
            high = middle
    scale = safety_fraction*low
    result = candidate(scale)
    if result.minimum_positivity_eigenvalue() < -tolerance:
        raise ValueError("spin-1 gluon parent positivity projection failed")
    return result, float(scale)


@dataclass(frozen=True)
class WilsonChannelMember:
    """One correlated member of an exponentiated spin-1 Wilson operator."""

    label: str
    strengths: Mapping[WilsonChannel, float]
    correlation_group: str = "wilson_common"

    def __post_init__(self) -> None:
        missing = set(WilsonChannel) - set(self.strengths)
        if missing:
            raise ValueError(f"missing Wilson channels: {sorted(x.value for x in missing)}")
        if not all(np.isfinite(v) for v in self.strengths.values()):
            raise ValueError("Wilson strengths must be finite")


@dataclass(frozen=True)
class ExponentiatedSpin1WilsonOperator:
    """Unitary multi-channel Wilson operator with exact staple reversal."""

    member: WilsonChannelMember
    staple_sign: int

    def __post_init__(self) -> None:
        if self.staple_sign not in (-1, 1):
            raise ValueError("staple_sign must be +1 or -1")

    def unitary(self, k_x: float, k_y: float) -> np.ndarray:
        k = float(np.hypot(k_x, k_y))
        if k == 0.0:
            return np.eye(3, dtype=np.complex128)
        phi = float(np.arctan2(k_y, k_x))
        basis = spin_one_basis()
        generators = {
            WilsonChannel.QUARK_SPECTATOR:
                np.cos(phi) * basis["LT_x"] + np.sin(phi) * basis["LT_y"],
            WilsonChannel.GLUON_SPECTATOR:
                np.cos(2 * phi) * basis["TT_x"] + np.sin(2 * phi) * basis["TT_y"],
            WilsonChannel.SP:
                np.cos(phi) * basis["LT_x"] - np.sin(phi) * basis["LT_y"],
            WilsonChannel.SD:
                np.cos(2 * phi) * basis["TT_x"] - np.sin(2 * phi) * basis["TT_y"],
            WilsonChannel.PP: basis["LL"],
        }
        generator = sum(
            float(self.member.strengths[channel]) * generators[channel]
            for channel in WilsonChannel
        )
        return expm(1j * self.staple_sign * k * generator)

    def apply(self, parent: Spin1QuarkCorrelator, k_x: float, k_y: float) -> Spin1QuarkCorrelator:
        u = self.unitary(k_x, k_y)

        def rotate(block: np.ndarray) -> np.ndarray:
            return u @ block @ u.conj().T

        result = Spin1QuarkCorrelator(
            rotate(parent.vector), rotate(parent.axial),
            np.asarray([rotate(x) for x in parent.transverse]),
        )
        if parent.is_target_hermitian():
            before = np.linalg.eigvalsh(parent.quark_target_density_matrix())
            after = np.linalg.eigvalsh(result.quark_target_density_matrix())
            if not np.allclose(before, after, atol=2e-11, rtol=2e-11):
                raise ValueError("Wilson operator changed the density spectrum")
        return result


@dataclass(frozen=True)
class FockAmplitude:
    label: str
    spectator: str
    lz: int
    amplitude: complex
    evidence: str

    def __post_init__(self) -> None:
        if self.spectator not in ("scalar", "axial", "quark_gluon"):
            raise ValueError("unsupported spectator/Fock sector")
        if self.lz not in (-2, -1, 0, 1, 2):
            raise ValueError("Fock amplitude requires Lz in -2..2")
        if not np.isfinite(self.amplitude.real + self.amplitude.imag):
            raise ValueError("amplitude must be finite")


@dataclass(frozen=True)
class SharedFockOAMLedger:
    """Normalized amplitude ledger and its shared interference bilinears."""

    amplitudes: tuple[FockAmplitude, ...]

    def __post_init__(self) -> None:
        if not self.amplitudes:
            raise ValueError("empty Fock ledger")
        labels = [x.label for x in self.amplitudes]
        if len(labels) != len(set(labels)):
            raise ValueError("Fock labels must be unique")

    @property
    def norm(self) -> float:
        return float(sum(abs(x.amplitude) ** 2 for x in self.amplitudes))

    def normalized(self) -> "SharedFockOAMLedger":
        if self.norm <= 0.0:
            raise ValueError("Fock norm must be positive")
        scale = np.sqrt(self.norm)
        return SharedFockOAMLedger(tuple(
            FockAmplitude(x.label, x.spectator, x.lz, x.amplitude / scale, x.evidence)
            for x in self.amplitudes
        ))

    def interference(self, delta_lz: int) -> complex:
        """Sum ordered bilinears sharing the requested orbital mismatch."""
        return sum(
            left.amplitude * right.amplitude.conjugate()
            for left in self.amplitudes for right in self.amplitudes
            if left.lz - right.lz == delta_lz
        )

    def shared_tmd_coordinates(self) -> dict[str, float]:
        """Coordinates feeding coupled TMD families from one amplitude state."""
        return {
            "rank0_density": float(self.interference(0).real),
            "rank1_even": float(self.interference(1).real),
            "rank1_odd": float(self.interference(1).imag),
            "rank2_even": float(self.interference(2).real),
            "rank2_odd": float(self.interference(2).imag),
        }


def calibrate_shared_fock_oam_ledger(
    targets: Mapping[str, float],
    *,
    evidence: str = "fit-informed shared-amplitude calibration",
) -> tuple[SharedFockOAMLedger, float]:
    """Fit one Lz=0,1,2 amplitude state to four shared bilinears.

    The fit never adjusts TMDs independently.  Its four real parameters are
    the real/imaginary parts of the Lz=1 and Lz=2 amplitudes; all coupled
    rank-one/rank-two even/odd structures follow from their bilinears.
    """

    required = {"rank1_even", "rank1_odd", "rank2_even", "rank2_odd"}
    if set(targets) != required or not all(np.isfinite(list(targets.values()))):
        raise ValueError("Fock calibration requires four finite rank targets")

    def ledger(parameters) -> SharedFockOAMLedger:
        return SharedFockOAMLedger((
            FockAmplitude("fit_L0", "scalar", 0, 1.0, evidence),
            FockAmplitude(
                "fit_L1", "axial", 1,
                complex(parameters[0], parameters[1]), evidence,
            ),
            FockAmplitude(
                "fit_L2", "quark_gluon", 2,
                complex(parameters[2], parameters[3]), evidence,
            ),
        )).normalized()

    ordered = ("rank1_even", "rank1_odd", "rank2_even", "rank2_odd")

    def residual(parameters):
        values = ledger(parameters).shared_tmd_coordinates()
        return np.asarray([values[name]-targets[name] for name in ordered])

    result = least_squares(
        residual, np.zeros(4), bounds=(-0.8, 0.8),
        xtol=1e-13, ftol=1e-13, gtol=1e-13, max_nfev=4000,
    )
    fitted = ledger(result.x)
    return fitted, float(np.linalg.norm(residual(result.x)))


@dataclass(frozen=True)
class FockResolvedNucleonBoundary:
    """Complete spin-half correlator derived from one shared Fock ledger.

    ``density`` fixes the flavor-resolved rank-zero normalization.  All
    spin/OAM structures are ratios of common ledger bilinears, so changing
    an amplitude coherently changes every coupled TMD.
    """

    ledger: SharedFockOAMLedger
    density: Mapping[int, float]
    width_gev2: Mapping[int, float]
    nucleon_mass_gev: float = 0.93891897

    def __post_init__(self) -> None:
        if set(self.density) != set(self.width_gev2):
            raise ValueError("density and width flavor sets must match")
        if any(v < 0.0 for v in self.density.values()):
            raise ValueError("Fock boundary density cannot be negative")
        if any(v <= 0.0 for v in self.width_gev2.values()):
            raise ValueError("Fock widths must be positive")

    def tmd_values(self, flavor: int, k_x: float, k_y: float, staple_sign: int) -> dict[str, float]:
        if flavor not in self.density or staple_sign not in (-1, 1):
            raise ValueError("unsupported flavor or staple")
        coordinates = self.ledger.normalized().shared_tmd_coordinates()
        width = self.width_gev2[flavor]
        radial = self.density[flavor] * np.exp(
            -(k_x**2 + k_y**2) / width
        ) / (np.pi * width)
        result = {name: 0.0 for name in NUCLEON_QUARK_TMD_NAMES}
        result["f1"] = radial
        result["g1"] = radial * 0.55 * coordinates["rank0_density"]
        result["h1"] = radial * 0.45 * coordinates["rank0_density"]
        result["g1T"] = radial * coordinates["rank1_even"]
        result["h1Lperp"] = -radial * coordinates["rank1_even"]
        result["h1Tperp"] = radial * coordinates["rank2_even"]
        result["f1Tperp"] = staple_sign * radial * coordinates["rank1_odd"]
        result["h1perp"] = -staple_sign * radial * coordinates["rank1_odd"]
        return result

    def correlator(self, flavor: int, k_x: float, k_y: float, staple_sign: int) -> SpinHalfQuarkCorrelator:
        return compose_spin_half_quark_correlator(
            values=self.tmd_values(flavor, k_x, k_y, staple_sign),
            k_x_gev=k_x, k_y_gev=k_y,
            delta_x_gev=0.0, delta_y_gev=0.0,
            nucleon_mass_gev=self.nucleon_mass_gev,
        )


@dataclass(frozen=True)
class FockResolvedSpinHalfGluonBoundary:
    """Positive spin-half target x gluon-polarization Fock/OAM boundary."""

    ledger: SharedFockOAMLedger
    density: float
    width_gev2: float
    positivity_safety: float = 0.95

    def __post_init__(self) -> None:
        if self.density < 0.0 or self.width_gev2 <= 0.0:
            raise ValueError("invalid gluon Fock boundary normalization")
        if not 0.0 < self.positivity_safety <= 1.0:
            raise ValueError("invalid gluon positivity safety")

    def correlator(self, k_x: float, k_y: float, staple_sign: int) -> np.ndarray:
        if staple_sign not in (-1, 1):
            raise ValueError("staple sign must be +/-1")
        c = self.ledger.normalized().shared_tmd_coordinates()
        identity = np.eye(2, dtype=np.complex128)
        sx = np.asarray(((0, 1), (1, 0)), dtype=np.complex128)
        sy = np.asarray(((0, -1j), (1j, 0)), dtype=np.complex128)
        sz = np.asarray(((1, 0), (0, -1)), dtype=np.complex128)
        spin_part = (
            0.55 * c["rank0_density"] * np.kron(sz, sz)
            + c["rank1_even"] * np.kron(sx, sz)
            + c["rank2_even"] * np.kron(sx, sx)
            + staple_sign * c["rank1_odd"] * np.kron(sy, identity)
            + staple_sign * c["rank2_odd"] * np.kron(sy, sx)
        )
        eig = np.linalg.eigvalsh(spin_part)
        scale = (
            min(1.0, self.positivity_safety / max(abs(eig[0]), abs(eig[-1])))
            if np.max(abs(eig)) > 0.0 else 1.0
        )
        radial = self.density * np.exp(
            -(k_x**2 + k_y**2) / self.width_gev2
        ) / (np.pi * self.width_gev2)
        joint = 0.25 * radial * (np.eye(4) + scale * spin_part)
        if np.linalg.eigvalsh(joint)[0] < -1e-12:
            raise ValueError("gluon Fock boundary positivity projection failed")
        return joint.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3)


class NonNucleonicSector(str, Enum):
    NNPI = "NNpi"
    DELTADELTA = "DeltaDelta"
    HIDDEN_COLOR = "hidden_color_6q"
    SRC = "short_range_NN"


@dataclass(frozen=True)
class NonNucleonicFockLedger:
    """Probability and plus-momentum accounting for replaceable sectors."""

    probabilities: Mapping[NonNucleonicSector, float]
    momentum_fractions: Mapping[NonNucleonicSector, float]
    central_enabled: Mapping[NonNucleonicSector, bool] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if set(self.probabilities) != set(NonNucleonicSector):
            raise ValueError("all non-nucleonic sector probabilities are required")
        if set(self.momentum_fractions) != set(NonNucleonicSector):
            raise ValueError("all non-nucleonic sector momenta are required")
        if any(v < 0.0 for v in self.probabilities.values()):
            raise ValueError("sector probabilities cannot be negative")
        if sum(self.probabilities.values()) > 1.0 + 1e-12:
            raise ValueError("non-nucleonic probabilities exceed unity")
        if any(v < 0.0 for v in self.momentum_fractions.values()):
            raise ValueError("sector momentum fractions cannot be negative")

    @property
    def nucleonic_probability(self) -> float:
        return 1.0 - float(sum(self.probabilities.values()))

    def central_weight(self, sector: NonNucleonicSector) -> float:
        return (
            float(self.probabilities[sector])
            if self.central_enabled.get(sector, False) else 0.0
        )


@dataclass(frozen=True)
class NonNucleonicParentSector:
    """A complete replaceable parent plus its Fock-ledger interpretation."""

    sector: NonNucleonicSector
    parent: Spin1QuarkCorrelator
    ledger: NonNucleonicFockLedger
    provenance: str
    sensitivity_only: bool = False

    def central_parent(self) -> Spin1QuarkCorrelator:
        weight = self.ledger.central_weight(self.sector)
        if self.sensitivity_only:
            weight = 0.0
        return Spin1QuarkCorrelator(
            weight * self.parent.vector,
            weight * self.parent.axial,
            weight * self.parent.transverse,
        )

    def sensitivity_parent(self) -> Spin1QuarkCorrelator:
        weight = float(self.ledger.probabilities[self.sector])
        return Spin1QuarkCorrelator(
            weight * self.parent.vector,
            weight * self.parent.axial,
            weight * self.parent.transverse,
        )


@dataclass(frozen=True)
class OperatorResponseMap:
    """Completely-positive target-spin response applied to every operator."""

    kraus: tuple[np.ndarray, ...]
    normalization: float = 1.0
    label: str = "operator_response"

    def __post_init__(self) -> None:
        if self.normalization < 0.0:
            raise ValueError("response normalization cannot be negative")
        if not self.kraus:
            raise ValueError("at least one Kraus operator is required")
        if any(np.asarray(k).shape != (3, 3) for k in self.kraus):
            raise ValueError("target-spin Kraus operators must be 3x3")

    @classmethod
    def identity(cls, factor: float = 1.0) -> "OperatorResponseMap":
        return cls((np.eye(3, dtype=np.complex128),), factor, "scalar_identity_limit")

    def apply(self, parent: Spin1QuarkCorrelator) -> Spin1QuarkCorrelator:
        def channel(block: np.ndarray) -> np.ndarray:
            return self.normalization * sum(
                k @ block @ k.conj().T for k in self.kraus
            )

        result = Spin1QuarkCorrelator(
            channel(parent.vector), channel(parent.axial),
            np.asarray([channel(x) for x in parent.transverse]),
        )
        if not result.is_target_hermitian():
            raise ValueError("operator response broke target Hermiticity")
        return result

    def completeness(self) -> np.ndarray:
        return sum(k.conj().T @ k for k in self.kraus)


def polarized_tensor_response_map(
    *,
    unpolarized_factor: float,
    vector_asymmetry: float,
    tensor_alignment: float,
    label: str,
) -> OperatorResponseMap:
    """Construct a CP spin-1 response from U, vector, and tensor eigenmodes.

    The helicity response rates are
    ``r_+=U+V+T/3``, ``r_0=U-2T/3``, and ``r_-=U-V+T/3``.
    Their square roots form one diagonal Kraus operator, so the map preserves
    Hermiticity and positivity while modifying off-diagonal LT/TT coherence.
    """

    rates = np.asarray((
        unpolarized_factor + vector_asymmetry + tensor_alignment / 3.0,
        unpolarized_factor - 2.0 * tensor_alignment / 3.0,
        unpolarized_factor - vector_asymmetry + tensor_alignment / 3.0,
    ))
    if np.any(rates < 0.0):
        raise ValueError("polarized/tensor response has a negative helicity rate")
    return OperatorResponseMap(
        (np.diag(np.sqrt(rates)).astype(np.complex128),),
        normalization=1.0, label=label,
    )


@dataclass(frozen=True)
class JointSpinResponseMap:
    """Completely-positive response on target-spin x quark-spin density."""

    kraus: tuple[np.ndarray, ...]
    label: str

    def __post_init__(self) -> None:
        if not self.kraus or any(np.asarray(k).shape != (6, 6) for k in self.kraus):
            raise ValueError("joint-spin Kraus operators must be 6x6")

    @staticmethod
    def _from_density(density: np.ndarray) -> Spin1QuarkCorrelator:
        blocks = density.reshape(3, 2, 3, 2).transpose(0, 2, 1, 3)
        identity = np.eye(2, dtype=np.complex128)
        sigma_x = np.asarray(((0, 1), (1, 0)), dtype=np.complex128)
        sigma_y = np.asarray(((0, -1j), (1j, 0)), dtype=np.complex128)
        sigma_z = np.asarray(((1, 0), (0, -1)), dtype=np.complex128)
        # rho = 1/2 sum_a Phi_a tensor sigma_a, hence
        # Phi_a = Tr_quark[rho sigma_a].
        contraction = lambda sigma: np.einsum("ABij,ji->AB", blocks, sigma)
        return Spin1QuarkCorrelator(
            contraction(identity), contraction(sigma_z),
            np.asarray((contraction(sigma_x), contraction(sigma_y))),
        )

    def apply(self, parent: Spin1QuarkCorrelator) -> Spin1QuarkCorrelator:
        density = parent.quark_target_density_matrix()
        transformed = sum(k @ density @ k.conj().T for k in self.kraus)
        result = self._from_density(transformed)
        if result.minimum_positivity_eigenvalue() < -1e-12:
            raise ValueError("joint-spin CP map failed positivity")
        return result


@dataclass(frozen=True)
class GluonJointSpinResponseMap:
    """Completely-positive response on target-spin x gluon-polarization."""

    kraus: tuple[np.ndarray, ...]
    label: str

    def __post_init__(self) -> None:
        if not self.kraus or any(np.asarray(k).shape != (6, 6) for k in self.kraus):
            raise ValueError("gluon joint-spin Kraus operators must be 6x6")

    def apply(self, parent: Spin1GluonCorrelator) -> Spin1GluonCorrelator:
        density = parent.joint_density_matrix()
        transformed = sum(k @ density @ k.conj().T for k in self.kraus)
        values = transformed.reshape(3, 2, 3, 2).transpose(0, 2, 1, 3)
        result = Spin1GluonCorrelator(values)
        if result.minimum_positivity_eigenvalue() < -1e-12:
            raise ValueError("gluon joint-spin CP map failed positivity")
        return result


def gluon_polarized_tensor_response_map(
    *,
    unpolarized_factor: float,
    target_vector: float,
    target_tensor: float,
    gluon_helicity: float,
    linear_polarization: float,
    label: str,
) -> GluonJointSpinResponseMap:
    """CP spin response with target and gluon circular/linear eigenmodes."""

    target_rates = np.asarray((
        unpolarized_factor + target_vector + target_tensor / 3.0,
        unpolarized_factor - 2.0 * target_tensor / 3.0,
        unpolarized_factor - target_vector + target_tensor / 3.0,
    ))
    gluon_matrix = np.asarray((
        (1.0 + gluon_helicity, linear_polarization),
        (linear_polarization, 1.0 - gluon_helicity),
    ))
    if np.any(target_rates < 0.0) or np.linalg.eigvalsh(gluon_matrix)[0] < 0.0:
        raise ValueError("gluon response has a negative spin rate")
    target_root = np.diag(np.sqrt(target_rates))
    eigenvalues, eigenvectors = np.linalg.eigh(gluon_matrix)
    gluon_root = eigenvectors @ np.diag(np.sqrt(eigenvalues)) @ eigenvectors.conj().T
    return GluonJointSpinResponseMap(
        (np.kron(target_root, gluon_root),), label
    )


def joint_polarized_tensor_response_map(
    *,
    unpolarized_factor: float,
    target_vector: float,
    target_tensor: float,
    quark_helicity: float,
    label: str,
) -> JointSpinResponseMap:
    """Diagonal CP response with independently visible target/quark modes."""

    target_rates = np.asarray((
        unpolarized_factor + target_vector + target_tensor / 3.0,
        unpolarized_factor - 2.0 * target_tensor / 3.0,
        unpolarized_factor - target_vector + target_tensor / 3.0,
    ))
    quark_rates = np.asarray((1.0 + quark_helicity, 1.0 - quark_helicity))
    if np.any(target_rates < 0.0) or np.any(quark_rates < 0.0):
        raise ValueError("joint response has a negative spin rate")
    rates = np.kron(target_rates, quark_rates)
    return JointSpinResponseMap(
        (np.diag(np.sqrt(rates)).astype(np.complex128),), label
    )


@dataclass(frozen=True)
class CanonicalParentEnricher:
    """Ordered parent-level composition used identically by all projections."""

    wilson: ExponentiatedSpin1WilsonOperator | None = None
    responses: tuple[OperatorResponseMap, ...] = ()
    nonnucleonic: tuple[NonNucleonicParentSector, ...] = ()

    @staticmethod
    def _sum(left: Spin1QuarkCorrelator, right: Spin1QuarkCorrelator) -> Spin1QuarkCorrelator:
        return Spin1QuarkCorrelator(
            left.vector + right.vector,
            left.axial + right.axial,
            left.transverse + right.transverse,
        )

    def apply(self, parent: Spin1QuarkCorrelator, k_x: float, k_y: float) -> Spin1QuarkCorrelator:
        result = parent
        for sector in self.nonnucleonic:
            result = self._sum(result, sector.central_parent())
        for response in self.responses:
            result = response.apply(result)
        if self.wilson is not None:
            result = self.wilson.apply(result, k_x, k_y)
        if not result.is_target_hermitian():
            raise ValueError("canonical enrichment produced non-Hermitian parent")
        return result


@dataclass(frozen=True)
class CanonicalGluonParentEnricher:
    """Ordered complete-parent response composition for spin-1 gluons."""

    responses: tuple[GluonJointSpinResponseMap, ...] = ()

    def apply(self, parent: Spin1GluonCorrelator) -> Spin1GluonCorrelator:
        result = parent
        for response in self.responses:
            result = response.apply(result)
        return result
