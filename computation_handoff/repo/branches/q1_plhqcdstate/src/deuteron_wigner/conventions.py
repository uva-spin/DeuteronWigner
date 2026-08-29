"""Project-wide convention declarations.

No physics module should encode Fourier signs, helicity ordering, or light-front
normalization independently of this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final

import numpy as np

HELICITIES: Final[tuple[int, int, int]] = (1, 0, -1)
HELICITY_INDEX: Final[dict[int, int]] = {helicity: i for i, helicity in enumerate(HELICITIES)}
TWO_PI: Final[float] = 2.0 * np.pi


class FourierRole(str, Enum):
    """Distinct transverse Fourier pairs in the formalism."""

    GTMD_IMAGING = "delta_to_b_delta"
    TMD_EVOLUTION = "k_to_b_tmd"


@dataclass(frozen=True)
class FourierConvention:
    """Sign and normalization for a two-dimensional Fourier transform.

    ``forward`` means momentum-like to coordinate-like. The project uses

    - GTMD imaging: W(b_delta) = int d2Delta/(2pi)^2 exp(-i Delta.b) W(Delta)
    - TMD b-space: F~(b_tmd) = int d2k exp(+i b.k) F(k)
    """

    role: FourierRole
    forward_sign: int
    forward_normalization: float

    def __post_init__(self) -> None:
        if self.forward_sign not in (-1, 1):
            raise ValueError("Fourier exponent sign must be +1 or -1")
        if self.forward_normalization <= 0.0:
            raise ValueError("Fourier normalization must be positive")


GTMD_IMAGING_CONVENTION: Final = FourierConvention(
    role=FourierRole.GTMD_IMAGING,
    forward_sign=-1,
    forward_normalization=1.0 / TWO_PI**2,
)
TMD_EVOLUTION_CONVENTION: Final = FourierConvention(
    role=FourierRole.TMD_EVOLUTION,
    forward_sign=1,
    forward_normalization=1.0,
)


def delta_t_to_f1ll(delta_t: np.ndarray | float) -> np.ndarray:
    """Convert the stored helicity difference to the standard spin-1 f1LL.

    With ``S_LL(+1)=S_LL(-1)=1/2`` and ``S_LL(0)=-1``,
    ``delta_T f = f^0-(f^+ + f^-)/2 = -3 f1LL/2``.
    """

    return -2.0 * np.asarray(delta_t) / 3.0


def f1ll_to_delta_t(f1ll: np.ndarray | float) -> np.ndarray:
    """Inverse of :func:`delta_t_to_f1ll`."""

    return -1.5 * np.asarray(f1ll)
