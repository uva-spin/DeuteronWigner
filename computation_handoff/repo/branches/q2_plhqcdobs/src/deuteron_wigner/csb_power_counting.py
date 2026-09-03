"""Conservative charge-symmetry-breaking envelopes for unsupported TMDs."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TMDChargeSymmetryBreakingEnvelope:
    """Zero-centered CSB power-counting sensitivity.

    This is not a fitted central correction. It prevents the exact-isospin
    limit from carrying zero uncertainty into sectors without a dedicated
    QCD+QED calculation.
    """

    quark_fraction: float = 0.05
    gluon_fraction: float = 0.02
    source_floor_fraction: float = 0.10

    def __post_init__(self) -> None:
        for value in (
            self.quark_fraction, self.gluon_fraction,
            self.source_floor_fraction,
        ):
            if not 0.0 <= value <= 1.0:
                raise ValueError("CSB fractions must lie in [0,1]")

    def halfwidth(
        self, *, central: float, f1: float, rank_weight: float,
        species: str,
    ) -> float:
        if species not in ("quark", "gluon"):
            raise ValueError("species must be quark or gluon")
        fraction = (
            self.quark_fraction if species == "quark"
            else self.gluon_fraction
        )
        reference = max(
            abs(float(central)),
            self.source_floor_fraction*abs(float(f1))*abs(float(rank_weight)),
        )
        return fraction*reference

    @property
    def interpretation(self) -> str:
        return (
            "zero-centered model sensitivity, not a fitted correction or "
            "statistical confidence interval"
        )

    @property
    def sources(self) -> tuple[str, ...]:
        return (
            "Horsley et al., arXiv:1012.0215, lattice PDF CSV moments",
            "Wang, Thomas, Young, arXiv:1512.04139, QCD+QED CSV",
            "Cao and Signal, arXiv:hep-ph/0001146, sub-percent collinear CSV",
        )
