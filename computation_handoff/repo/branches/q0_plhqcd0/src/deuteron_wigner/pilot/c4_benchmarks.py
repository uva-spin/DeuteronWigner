"""Construction helpers for C4 Benchmark E sea/gluon parents."""

from __future__ import annotations

from ..formal.diagnostics import ArchitectureError
from ..gtmd import Species
from .active import PositiveXActiveSelector
from .routes import RegulatedParent
from .sectors import SectorSuperposition


def parents_from_state(
    state: SectorSuperposition, species: Species, *, flavor: str | None = None,
) -> tuple[RegulatedParent, ...]:
    selector = PositiveXActiveSelector()
    parents = []
    for sector in state.sectors:
        if sector.probability == 0:
            continue
        for selection in selector.select(
            sector.configuration, species, flavor=flavor
        ):
            item = sector.configuration.constituents[selection.slot_index]
            coefficient = sector.probability * (
                item.x if species == Species.GLUON else 1.0
            )
            concentration = 20.0
            alpha = concentration * item.x - 1.0
            beta = concentration * (1.0 - item.x) - 1.0
            parents.append(RegulatedParent(
                f"C4:PARENT:{sector.stable_id}:{selection.slot_id}",
                species,
                "NOT_APPLICABLE" if species == Species.GLUON else item.flavor,
                sector.configuration.sector.basis_id,
                (
                    "GLUON_TRACE_DIAGONAL_ADJOINT"
                    if species == Species.GLUON else "QUARK_VECTOR_DIAGONAL"
                ),
                "ZEROTH_RESCATTERING_NO_PHYSICAL_FD_CLASS",
                selection.slot_id, coefficient, alpha, beta,
                sector.state.width_gev,
                0.35,
                "H_G_EQUALS_XG" if species == Species.GLUON else "H_Q",
                (
                    ("gluon-link-1:identity", "gluon-link-2:identity")
                    if species == Species.GLUON
                    else ("quark-link:identity",)
                ),
                "DIAGONAL_ADJOINT" if species == Species.GLUON
                else "NOT_APPLICABLE",
            ))
    return tuple(parents)


def exact_structural_zero(
    state: SectorSuperposition, species: Species,
    *, induced_enabled: bool = False,
) -> float:
    if induced_enabled:
        raise ArchitectureError(
            "C4.ZERO.INDUCED_UNSPECIFIED",
            "induced contribution requires a separately named operator",
            expected="explicit induced operator identity", received=True,
        )
    return float(sum(
        parent.coefficient for parent in parents_from_state(state, species)
    ))


def integrated_parent_ledger(state: SectorSuperposition) -> dict[str, object]:
    net, occupation, momentum = {}, {}, 0.0
    for species in (Species.QUARK, Species.ANTIQUARK, Species.GLUON):
        for parent in parents_from_state(state, species):
            if species == Species.GLUON:
                momentum += parent.coefficient
                continue
            sign = -1.0 if species == Species.ANTIQUARK else 1.0
            net[parent.flavor] = net.get(parent.flavor, 0.0) + sign * parent.coefficient
            occupation[parent.flavor] = occupation.get(parent.flavor, 0.0) + parent.coefficient
            mean_x = (parent.alpha + 1) / (parent.alpha + parent.beta + 2)
            momentum += parent.coefficient * mean_x
    return {
        "net_flavor": dict(sorted(net.items())),
        "occupation": dict(sorted(occupation.items())),
        "plus_momentum": momentum,
    }


def require_diagonal_core_label(label: str) -> None:
    forbidden = ("SIVERS", "BOER", "T_ODD", "F_TYPE", "D_TYPE", "GLUONIC_POLE")
    if any(item in label.upper() for item in forbidden):
        raise ArchitectureError(
            "C4.GLUON.TODD",
            "zeroth-rescattering core has no physical f/d or T-odd label",
            expected="DIAGONAL_ADJOINT", received=label,
        )
