"""Typed light-front and transverse kinematics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

import numpy as np

TTransverse = TypeVar("TTransverse", bound="TransverseVector")


@dataclass(frozen=True)
class TransverseVector:
    x: float
    y: float

    def array(self) -> np.ndarray:
        return np.array([self.x, self.y], dtype=np.float64)

    def dot(self, other: "TransverseVector") -> float:
        return float(self.x * other.x + self.y * other.y)

    def norm_squared(self) -> float:
        return self.dot(self)

    def scale(self: TTransverse, factor: float) -> TTransverse:
        return type(self)(factor * self.x, factor * self.y)


@dataclass(frozen=True)
class MomentumTransfer(TransverseVector):
    """GTMD transverse momentum transfer Delta_T, in momentum units."""


@dataclass(frozen=True)
class PartonMomentum(TransverseVector):
    """Partonic transverse momentum k_T, in momentum units."""


@dataclass(frozen=True)
class BDelta(TransverseVector):
    """Transverse imaging coordinate conjugate to Delta_T."""


@dataclass(frozen=True)
class BTMD(TransverseVector):
    """TMD impact parameter conjugate to k_T."""


@dataclass(frozen=True)
class LightFrontVector:
    """Contravariant components (plus, minus, transverse) with v^±=(v0±v3)/sqrt(2)."""

    plus: float
    minus: float
    transverse: TransverseVector = TransverseVector(0.0, 0.0)

    def dot(self, other: "LightFrontVector") -> float:
        return (
            self.plus * other.minus
            + self.minus * other.plus
            - self.transverse.dot(other.transverse)
        )

    def mass_squared(self) -> float:
        return self.dot(self)

    @classmethod
    def on_shell_collinear(cls, plus: float, mass: float) -> "LightFrontVector":
        if plus <= 0.0:
            raise ValueError("plus momentum must be positive")
        if mass < 0.0:
            raise ValueError("mass cannot be negative")
        return cls(plus=plus, minus=mass**2 / (2.0 * plus))


@dataclass(frozen=True)
class ZeroSkewnessKinematics:
    """Symmetric-frame zero-skewness deuteron kinematics."""

    average: LightFrontVector
    delta_t: MomentumTransfer

    def __post_init__(self) -> None:
        if self.average.plus <= 0.0:
            raise ValueError("average plus momentum must be positive")
        if self.average.transverse.norm_squared() != 0.0:
            raise ValueError("symmetric-frame average transverse momentum must vanish")

    @classmethod
    def symmetric(
        cls, *, plus: float, mass: float, delta_t: MomentumTransfer
    ) -> "ZeroSkewnessKinematics":
        """Construct a frame in which incoming and outgoing states are on shell."""

        if plus <= 0.0:
            raise ValueError("plus momentum must be positive")
        if mass < 0.0:
            raise ValueError("mass cannot be negative")
        average_minus = (mass**2 + 0.25 * delta_t.norm_squared()) / (2.0 * plus)
        return cls(
            average=LightFrontVector(plus=plus, minus=average_minus),
            delta_t=delta_t,
        )

    @property
    def skewness(self) -> float:
        return 0.0

    @property
    def invariant_t(self) -> float:
        return -self.delta_t.norm_squared()

    @property
    def incoming(self) -> LightFrontVector:
        return LightFrontVector(
            plus=self.average.plus,
            minus=self.average.minus,
            transverse=TransverseVector(-0.5 * self.delta_t.x, -0.5 * self.delta_t.y),
        )

    @property
    def outgoing(self) -> LightFrontVector:
        return LightFrontVector(
            plus=self.average.plus,
            minus=self.average.minus,
            transverse=TransverseVector(0.5 * self.delta_t.x, 0.5 * self.delta_t.y),
        )


def require_fraction(value: float, *, name: str = "fraction", closed_upper: bool = True) -> float:
    upper_ok = value <= 1.0 if closed_upper else value < 1.0
    if value <= 0.0 or not upper_ok:
        interval = "(0, 1]" if closed_upper else "(0, 1)"
        raise ValueError(f"{name} must lie in {interval}")
    return value
