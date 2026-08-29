"""Typed positive-x active-parton selection for analytic pilot sectors."""

from __future__ import annotations

from dataclasses import dataclass

from ..formal.diagnostics import ArchitectureError
from ..gtmd import Species
from .configuration import IntrinsicConfiguration


@dataclass(frozen=True)
class ActiveSelection:
    sector_id: str
    slot_id: str
    slot_index: int
    species: Species
    flavor: str
    helicity: int
    color_representation: str
    permutation_orbit: str
    multiplicity: int
    operator_compatibility: str
    x_domain: str = "POSITIVE_X"
    version: int = 1

    def __post_init__(self) -> None:
        if self.slot_index < 0 or self.multiplicity <= 0:
            raise ArchitectureError(
                "C4.ACTIVE.MULTIPLICITY", "invalid active-slot multiplicity",
                expected="slot>=0 and multiplicity>0",
                received=(self.slot_index, self.multiplicity),
            )
        if self.species == Species.GLUON and self.flavor != "NOT_APPLICABLE":
            raise ArchitectureError(
                "C4.ACTIVE.FLAVOR", "gluon active flavor must be explicit N/A",
                expected="NOT_APPLICABLE", received=self.flavor,
            )
        if self.x_domain != "POSITIVE_X":
            raise ArchitectureError(
                "C4.ACTIVE.NEGATIVE_X", "negative-x copying is forbidden",
                expected="POSITIVE_X explicit slot", received=self.x_domain,
            )


class PositiveXActiveSelector:
    """Select explicit slots; an empty selection is an exact structural zero."""

    stable_id = "C4:POSITIVE_X_ACTIVE_SELECTOR"

    def select(
        self, configuration: IntrinsicConfiguration, species: Species,
        *, flavor: str | None = None,
    ) -> tuple[ActiveSelection, ...]:
        selected = []
        for index, item in enumerate(configuration.constituents):
            if item.species != species or (
                flavor is not None and item.flavor != flavor
            ):
                continue
            selected.append(ActiveSelection(
                configuration.sector.basis_id, item.stable_id, index, species,
                "NOT_APPLICABLE" if species == Species.GLUON else item.flavor,
                item.helicity,
                "adjoint" if species == Species.GLUON else (
                    "anti-fundamental" if species == Species.ANTIQUARK
                    else "fundamental"
                ),
                configuration.permutation_class, 1,
                f"diagonal_{species.value}_zeroth_rescattering",
            ))
        self.require_unique(selected)
        return tuple(selected)

    @staticmethod
    def require_unique(selections) -> None:
        keys = [(item.sector_id, item.slot_id) for item in selections]
        if len(keys) != len(set(keys)):
            raise ArchitectureError(
                "C4.ACTIVE.DUPLICATE",
                "duplicate active-slot multiplicity",
                expected="one entry per sector/slot", received=keys,
            )

    @staticmethod
    def require_compatible(
        configuration: IntrinsicConfiguration, selection: ActiveSelection,
        expected_species: Species,
    ) -> None:
        if selection.sector_id != configuration.sector.basis_id:
            raise ArchitectureError(
                "C4.ACTIVE.SECTOR", "active selector has wrong sector",
                expected=configuration.sector.basis_id,
                received=selection.sector_id,
            )
        item = configuration.constituents[selection.slot_index]
        if item.stable_id != selection.slot_id or item.species != expected_species:
            raise ArchitectureError(
                "C4.ACTIVE.SPECIES", "wrong-species active selection",
                expected=expected_species.value,
                received=(item.stable_id, item.species.value),
            )
