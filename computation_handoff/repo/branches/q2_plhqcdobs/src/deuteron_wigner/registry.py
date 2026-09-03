"""Machine-readable leading-twist TMD registry."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Optional

from .gtmd import Species


class TargetChannel(str, Enum):
    U = "U"
    L = "L"
    T = "T"
    LL = "LL"
    LT = "LT"
    TT = "TT"


class CollinearLimit(str, Enum):
    NONZERO = "nonzero"
    ZERO_UNWEIGHTED = "zero_unweighted"
    MOMENT_ONLY = "moment_only"
    NONE = "none"


class MatchingStatus(str, Enum):
    KNOWN = "known"
    TREE = "tree"
    DERIVED = "derived"
    MODELED = "modeled"
    OPEN = "open"


@dataclass(frozen=True)
class TMDEntry:
    name: str
    species: Species
    parent_projection: str
    target_channel: TargetChannel
    parton_polarization: str
    transverse_rank: int
    gauge_link_required: bool
    collinear_limit: CollinearLimit
    matching_status: MatchingStatus
    positivity_block: str
    t_odd: bool = False
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("TMD name cannot be empty")
        if self.transverse_rank < 0:
            raise ValueError("transverse rank cannot be negative")
        if self.transverse_rank > 0 and self.collinear_limit == CollinearLimit.NONZERO:
            raise ValueError("positive-rank TMD cannot have a nonzero unweighted collinear limit")


class TMDRegistry:
    def __init__(self, entries: Iterable[TMDEntry] = ()) -> None:
        self._entries: dict[tuple[Species, str], TMDEntry] = {}
        for entry in entries:
            self.register(entry)

    def register(self, entry: TMDEntry) -> None:
        key = (entry.species, entry.name)
        if key in self._entries:
            raise ValueError(f"duplicate TMD registry entry {entry.species.value}:{entry.name}")
        self._entries[key] = entry

    def get(self, species: Species, name: str) -> TMDEntry:
        try:
            return self._entries[(species, name)]
        except KeyError as exc:
            raise KeyError(f"unknown TMD {species.value}:{name}") from exc

    def select(
        self,
        *,
        species: Optional[Species] = None,
        target_channel: Optional[TargetChannel] = None,
    ) -> tuple[TMDEntry, ...]:
        entries = self._entries.values()
        if species is not None:
            entries = (entry for entry in entries if entry.species == species)
        if target_channel is not None:
            entries = (entry for entry in entries if entry.target_channel == target_channel)
        return tuple(entries)

    def __len__(self) -> int:
        return len(self._entries)


def baseline_registry() -> TMDRegistry:
    """Initial rank-zero entries needed for the b1-anchored milestone.

    This is intentionally smaller than the eventual full leading-twist registry.
    Entries are added only when their rank and convention mapping are explicit.
    """

    entries = []
    for species in (Species.QUARK, Species.ANTIQUARK):
        entries.extend(
            (
                TMDEntry(
                    name="f1",
                    species=species,
                    parent_projection="gamma+",
                    target_channel=TargetChannel.U,
                    parton_polarization="unpolarized",
                    transverse_rank=0,
                    gauge_link_required=True,
                    collinear_limit=CollinearLimit.NONZERO,
                    matching_status=MatchingStatus.KNOWN,
                    positivity_block="quark_unpolarized",
                ),
                TMDEntry(
                    name="deltaT_f1",
                    species=species,
                    parent_projection="gamma+",
                    target_channel=TargetChannel.LL,
                    parton_polarization="unpolarized",
                    transverse_rank=0,
                    gauge_link_required=True,
                    collinear_limit=CollinearLimit.NONZERO,
                    matching_status=MatchingStatus.TREE,
                    positivity_block="quark_unpolarized",
                    notes="Convention-safe helicity difference; convert to f1LL explicitly.",
                ),
            )
        )
    entries.extend(
        (
            TMDEntry(
                name="f1",
                species=Species.GLUON,
                parent_projection="Gamma_trace",
                target_channel=TargetChannel.U,
                parton_polarization="unpolarized",
                transverse_rank=0,
                gauge_link_required=True,
                collinear_limit=CollinearLimit.NONZERO,
                matching_status=MatchingStatus.KNOWN,
                positivity_block="gluon_trace",
            ),
            TMDEntry(
                name="deltaT_f1",
                species=Species.GLUON,
                parent_projection="Gamma_trace",
                target_channel=TargetChannel.LL,
                parton_polarization="unpolarized",
                transverse_rank=0,
                gauge_link_required=True,
                collinear_limit=CollinearLimit.NONZERO,
                matching_status=MatchingStatus.TREE,
                positivity_block="gluon_trace",
                notes="Convention-safe helicity difference.",
            ),
        )
    )
    return TMDRegistry(entries)


def leading_twist_gluon_registry() -> TMDRegistry:
    """Complete spin-1 leading-twist gluon basis of arXiv:2603.15224v1."""

    # name, target channel, gluon polarization, transverse rank, T-odd
    definitions = (
        ("f1", TargetChannel.U, "unpolarized", 0, False),
        ("h1perp", TargetChannel.U, "linear", 2, False),
        ("g1", TargetChannel.L, "circular", 0, False),
        ("h1Lperp", TargetChannel.L, "linear", 2, True),
        ("f1Tperp", TargetChannel.T, "unpolarized", 1, True),
        ("g1T", TargetChannel.T, "circular", 1, False),
        ("h1", TargetChannel.T, "linear", 1, True),
        ("h1Tperp", TargetChannel.T, "linear", 3, True),
        ("f1LL", TargetChannel.LL, "unpolarized", 0, False),
        ("h1LLperp", TargetChannel.LL, "linear", 2, False),
        ("f1LT", TargetChannel.LT, "unpolarized", 1, False),
        ("g1LT", TargetChannel.LT, "circular", 1, True),
        ("h1LT", TargetChannel.LT, "linear", 1, False),
        ("h1LTperp", TargetChannel.LT, "linear", 3, False),
        ("f1TT", TargetChannel.TT, "unpolarized", 2, False),
        ("g1TT", TargetChannel.TT, "circular", 2, True),
        ("h1TT", TargetChannel.TT, "linear", 0, False),
        ("h1TTperp", TargetChannel.TT, "linear", 2, False),
        ("h1TTperpperp", TargetChannel.TT, "linear", 4, False),
    )
    entries = []
    for name, channel, polarization, rank, t_odd in definitions:
        entries.append(
            TMDEntry(
                name=name,
                species=Species.GLUON,
                parent_projection=f"Phi_ij:{channel.value}:{polarization}",
                target_channel=channel,
                parton_polarization=polarization,
                transverse_rank=rank,
                gauge_link_required=True,
                collinear_limit=(
                    CollinearLimit.NONZERO
                    if rank == 0 else CollinearLimit.MOMENT_ONLY
                ),
                matching_status=(
                    MatchingStatus.OPEN if t_odd else MatchingStatus.MODELED
                ),
                positivity_block=f"gluon_{channel.value.lower()}",
                t_odd=t_odd,
                notes=(
                    "T-odd; zero in the tree-level spectator model and "
                    "requires gauge-link phases."
                    if t_odd else
                    "T-even; modeled at tree level in arXiv:2603.15224v1."
                ),
            )
        )
    return TMDRegistry(entries)


def leading_twist_quark_registry(
    species: Species = Species.QUARK,
) -> TMDRegistry:
    """Complete definite-rank spin-1 quark or antiquark TMD basis.

    Names, ranks, and time-reversal properties follow Eqs. (11)-(20) and
    Table I of arXiv:1612.06585. The exceptional rank-zero ``h1LT`` is T-odd
    and has no collinear PDF despite surviving angular integration.
    """

    if species not in (Species.QUARK, Species.ANTIQUARK):
        raise ValueError("quark registry species must be q or qbar")
    # name, target channel, quark polarization, transverse rank, T-odd
    definitions = (
        ("f1", TargetChannel.U, "unpolarized", 0, False),
        ("h1perp", TargetChannel.U, "transverse", 1, True),
        ("g1", TargetChannel.L, "longitudinal", 0, False),
        ("h1Lperp", TargetChannel.L, "transverse", 1, False),
        ("f1Tperp", TargetChannel.T, "unpolarized", 1, True),
        ("g1T", TargetChannel.T, "longitudinal", 1, False),
        ("h1", TargetChannel.T, "transverse", 0, False),
        ("h1Tperp", TargetChannel.T, "transverse", 2, False),
        ("f1LL", TargetChannel.LL, "unpolarized", 0, False),
        ("h1LLperp", TargetChannel.LL, "transverse", 1, True),
        ("f1LT", TargetChannel.LT, "unpolarized", 1, False),
        ("g1LT", TargetChannel.LT, "longitudinal", 1, True),
        ("h1LT", TargetChannel.LT, "transverse", 0, True),
        ("h1LTperp", TargetChannel.LT, "transverse", 2, True),
        ("f1TT", TargetChannel.TT, "unpolarized", 2, False),
        ("g1TT", TargetChannel.TT, "longitudinal", 2, True),
        ("h1TT", TargetChannel.TT, "transverse", 1, True),
        ("h1TTperp", TargetChannel.TT, "transverse", 3, True),
    )
    entries = []
    for name, channel, polarization, rank, t_odd in definitions:
        if name == "h1LT":
            collinear = CollinearLimit.NONE
        elif rank == 0:
            collinear = CollinearLimit.NONZERO
        else:
            collinear = CollinearLimit.MOMENT_ONLY
        entries.append(
            TMDEntry(
                name=name,
                species=species,
                parent_projection=(
                    f"Phi:{channel.value}:"
                    + {
                        "unpolarized": "gamma+",
                        "longitudinal": "gamma+gamma5",
                        "transverse": "i_sigma_i+_gamma5",
                    }[polarization]
                ),
                target_channel=channel,
                parton_polarization=polarization,
                transverse_rank=rank,
                gauge_link_required=True,
                collinear_limit=collinear,
                matching_status=MatchingStatus.KNOWN,
                positivity_block=f"{species.value}_{channel.value.lower()}",
                t_odd=t_odd,
                notes=(
                    "T-odd; changes sign with the appropriate future/past "
                    "gauge-link reversal."
                    + (
                        " Rank-zero exception with no collinear PDF by "
                        "hermiticity and time reversal."
                        if name == "h1LT" else ""
                    )
                    if t_odd else
                    "T-even leading-twist definite-rank quark TMD."
                ),
            )
        )
    return TMDRegistry(entries)
