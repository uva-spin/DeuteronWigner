"""Validation-only sea/gluon Fock-sector superpositions and ledgers."""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, pi, sqrt

from ..formal.diagnostics import ArchitectureError
from ..formal.sector_space import ResolutionLayer, SectorId
from ..gtmd import Species
from ..kinematics import PartonMomentum
from .configuration import ColorLabel, Constituent, IntrinsicConfiguration


_CHARGE_THIRDS = {"u": 2, "d": -1, "s": -1}


def _sector(
    basis_id: str, quarks: tuple[str, ...], antiquarks: tuple[str, ...] = (),
    gluons: int = 0,
) -> SectorId:
    q = tuple(sorted((f, quarks.count(f)) for f in set(quarks)))
    aq = tuple(sorted((f, antiquarks.count(f)) for f in set(antiquarks)))
    charge = sum(_CHARGE_THIRDS[f] for f in quarks)
    charge -= sum(_CHARGE_THIRDS[f] for f in antiquarks)
    return SectorId(
        ResolutionLayer.MICROSCOPIC_FOCK, q, aq, gluons, charge,
        "benchmark-helicity", "positive", "verified-singlet", basis_id,
        "VALIDATION_ONLY",
    )


@dataclass(frozen=True)
class ProductGaussianState:
    """Arbitrary-particle analytic state consumed by the C3 evaluator."""

    stable_id: str
    width_gev: float = 0.45
    member_id: str = "VALIDATION_ONLY_PRODUCT_GAUSSIAN"
    production_authorized: bool = False

    def __post_init__(self) -> None:
        if self.width_gev <= 0:
            raise ArchitectureError(
                "C4.STATE.WIDTH", "analytic width must be positive",
                expected=">0", received=self.width_gev,
            )

    def amplitude(self, configuration: IntrinsicConfiguration) -> complex:
        """Delta-normalized longitudinal basis times normalized transverse state.

        With the last intrinsic momentum fixed by closure, the quadratic form
        has determinant ``n`` in each transverse Cartesian pair.
        """
        count = len(configuration.constituents)
        exponent = sum(item.k_t.norm_squared() for item in configuration.constituents)
        return complex(
            self.normalization(count)
            * exp(-exponent / (2 * self.width_gev**2))
        )

    def normalization(self, constituent_count: int) -> float:
        if constituent_count < 1:
            raise ArchitectureError(
                "C4.STATE.NORMALIZATION", "empty Fock sector",
                expected="at least one constituent",
                received=constituent_count,
            )
        return sqrt(constituent_count) / (
            (pi * self.width_gev**2) ** ((constituent_count - 1) / 2)
        )

    def transverse_norm_oracle(self, constituent_count: int) -> float:
        normalization = self.normalization(constituent_count)
        integral = (
            (pi * self.width_gev**2) ** (constituent_count - 1)
            / constituent_count
        )
        return normalization**2 * integral


@dataclass(frozen=True)
class SectorRecord:
    stable_id: str
    configuration: IntrinsicConfiguration
    probability: float
    state: ProductGaussianState
    color_tensor_id: str
    multiplicity_channel: str
    permutation_orbits: tuple[str, ...]
    oam_labels: tuple[int, ...]
    status: str = "VALIDATION_ONLY"

    def __post_init__(self) -> None:
        if not 0 <= self.probability <= 1:
            raise ArchitectureError(
                "C4.STATE.PROBABILITY", "sector probability outside [0,1]",
                expected="[0,1]", received=self.probability,
            )


@dataclass(frozen=True)
class SectorSuperposition:
    stable_id: str
    sectors: tuple[SectorRecord, ...]
    status: str = "VALIDATION_ONLY"

    def __post_init__(self) -> None:
        total = sum(item.probability for item in self.sectors)
        if abs(total - 1) > 1e-14:
            raise ArchitectureError(
                "C4.STATE.PROBABILITY", "sector probabilities are not unit",
                expected=1.0, received=total,
            )
        if len({item.stable_id for item in self.sectors}) != len(self.sectors):
            raise ArchitectureError(
                "C4.STATE.DUPLICATE", "duplicate sector identity",
                expected="unique sectors",
                received=tuple(item.stable_id for item in self.sectors),
            )

    def amplitude_ledger(self) -> tuple[tuple[str, float], ...]:
        return tuple((item.stable_id, sqrt(item.probability)) for item in self.sectors)

    def ledger(self) -> dict[str, object]:
        net: dict[str, float] = {}
        occupation: dict[str, float] = {}
        charge_thirds = baryon_thirds = momentum = 0.0
        for sector in self.sectors:
            for item in sector.configuration.constituents:
                weight = sector.probability
                momentum += weight * item.x
                if item.species == Species.QUARK:
                    net[item.flavor] = net.get(item.flavor, 0.0) + weight
                    occupation[item.flavor] = occupation.get(item.flavor, 0.0) + weight
                    charge_thirds += weight * _CHARGE_THIRDS.get(item.flavor, 0)
                    baryon_thirds += weight
                elif item.species == Species.ANTIQUARK:
                    net[item.flavor] = net.get(item.flavor, 0.0) - weight
                    occupation[item.flavor] = occupation.get(item.flavor, 0.0) + weight
                    charge_thirds -= weight * _CHARGE_THIRDS.get(item.flavor, 0)
                    baryon_thirds -= weight
        return {
            "net_flavor": dict(sorted(net.items())),
            "occupation": dict(sorted(occupation.items())),
            "baryon_number": baryon_thirds / 3,
            "electric_charge": charge_thirds / 3,
            "plus_momentum": momentum,
        }

    def require_proton_ledger(self, tolerance: float = 1e-13) -> None:
        ledger = self.ledger()
        expected = {"u": 2.0, "d": 1.0}
        if any(abs(ledger["net_flavor"].get(f, 0) - value) > tolerance for f, value in expected.items()):
            raise ArchitectureError(
                "C4.SEA_LEDGER.FLAVOR", "wrong proton net-flavor ledger",
                expected=expected, received=ledger["net_flavor"],
            )
        if abs(ledger["baryon_number"] - 1) > tolerance:
            raise ArchitectureError(
                "C4.SEA_LEDGER.BARYON", "wrong baryon number",
                expected=1.0, received=ledger["baryon_number"],
            )
        if abs(ledger["electric_charge"] - 1) > tolerance:
            raise ArchitectureError(
                "C4.SEA_LEDGER.CHARGE", "wrong electric charge",
                expected=1.0, received=ledger["electric_charge"],
            )
        if abs(ledger["plus_momentum"] - 1) > tolerance:
            raise ArchitectureError(
                "C4.LEDGER.MOMENTUM", "non-unit plus-momentum ledger",
                expected=1.0, received=ledger["plus_momentum"],
            )


def _configuration(
    basis_id: str, species_flavors: tuple[tuple[Species, str], ...],
    fractions: tuple[float, ...], permutation: str,
) -> IntrinsicConfiguration:
    quarks = tuple(flavor for species, flavor in species_flavors if species == Species.QUARK)
    antiquarks = tuple(flavor for species, flavor in species_flavors if species == Species.ANTIQUARK)
    gluons = sum(species == Species.GLUON for species, _ in species_flavors)
    sector = _sector(basis_id, quarks, antiquarks, gluons)
    momenta = []
    for index in range(len(fractions) - 1):
        momenta.append(PartonMomentum(0.025 * (index + 1), -0.015 * (index + 1)))
    momenta.append(PartonMomentum(
        -sum(item.x for item in momenta), -sum(item.y for item in momenta)
    ))
    colors = (ColorLabel.RED, ColorLabel.GREEN, ColorLabel.BLUE)
    constituents = []
    q_index = 0
    for index, ((species, flavor), x, momentum) in enumerate(zip(species_flavors, fractions, momenta)):
        color = colors[q_index % 3] if species != Species.GLUON else ColorLabel.NONE
        if species == Species.QUARK:
            q_index += 1
        constituents.append(Constituent(
            f"{basis_id}:slot:{index}", x, momentum, species, flavor, color,
            1 if index % 2 == 0 else -1, 0, basis_id,
        ))
    return IntrinsicConfiguration(
        tuple(constituents), 0, sector, basis_id, "REAL_NO_WILSON_PHASE",
        permutation,
    )


def valence_sector(probability: float = 1.0) -> SectorRecord:
    config = _configuration(
        "C4:QQQ", ((Species.QUARK, "u"), (Species.QUARK, "u"), (Species.QUARK, "d")),
        (0.4, 0.35, 0.25), "S3_DECLARED",
    )
    return SectorRecord(
        "C4:SECTOR:QQQ", config, probability,
        ProductGaussianState("C4:STATE:QQQ"), "epsilon_abc/sqrt6",
        "qqq-singlet", ("u:S2", "d:S1"), (0, 0, 0),
    )


def sea_state(p_sea: float, pair_flavor: str = "d") -> SectorSuperposition:
    if pair_flavor not in _CHARGE_THIRDS:
        raise ArchitectureError(
            "C4.SEA.FLAVOR", "unsupported explicit pair flavor",
            expected=tuple(sorted(_CHARGE_THIRDS)), received=pair_flavor,
        )
    config = _configuration(
        f"C4:QQQQQBAR:{pair_flavor}",
        ((Species.QUARK, "u"), (Species.QUARK, "u"), (Species.QUARK, "d"),
         (Species.QUARK, pair_flavor), (Species.ANTIQUARK, pair_flavor)),
        (0.28, 0.24, 0.20, 0.16, 0.12), "CLUSTER_S3xPAIR",
    )
    higher = SectorRecord(
        f"C4:SECTOR:QQQQQBAR:{pair_flavor}", config, p_sea,
        ProductGaussianState(f"C4:STATE:QQQQQBAR:{pair_flavor}"),
        "epsilon_abc/sqrt6 times delta_de/sqrt3",
        "singlet-baryon_times_singlet-pair_cluster",
        ("valence:S3", "pair:q-qbar"), (0, 0, 0, 0, 0),
    )
    state = SectorSuperposition(
        f"C4:SEA_SUPERPOSITION:{pair_flavor}",
        (valence_sector(1 - p_sea), higher),
    )
    state.require_proton_ledger()
    return state


def gluon_state(p_gluon: float) -> SectorSuperposition:
    config = _configuration(
        "C4:QQQG",
        ((Species.QUARK, "u"), (Species.QUARK, "u"), (Species.QUARK, "d"),
         (Species.GLUON, "NOT_APPLICABLE")),
        (0.32, 0.28, 0.20, 0.20), "QQ_ANTISYMMETRIC_OCTET_CHANNEL",
    )
    higher = SectorRecord(
        "C4:SECTOR:QQQG", config, p_gluon,
        ProductGaussianState("C4:STATE:QQQG"),
        "N epsilon_ijm (t^a)_km",
        "rho-octet_antisymmetric-pair_to_adjoint-singlet",
        ("quarks:S2_antisymmetric_pair", "gluon:S1"), (0, 0, 0, 0),
    )
    state = SectorSuperposition(
        "C4:GLUON_SUPERPOSITION",
        (valence_sector(1 - p_gluon), higher),
    )
    state.require_proton_ledger()
    return state
