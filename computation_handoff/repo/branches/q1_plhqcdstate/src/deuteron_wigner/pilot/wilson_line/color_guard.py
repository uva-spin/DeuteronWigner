"""C5 color algebra guardrails; not an active-gluon T-odd model."""

from __future__ import annotations

import numpy as np

from ...formal.diagnostics import ArchitectureError
from ...formal.gauge_path import ColorClass, GluonLinkId
from ..color import structure_constants
from ..states import _su3_generators


def symmetric_constants() -> np.ndarray:
    generators = _su3_generators()
    values = np.zeros((8, 8, 8), float)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                anticommutator = generators[a] @ generators[b] + generators[b] @ generators[a]
                values[a, b, c] = float((2 * np.trace(anticommutator @ generators[c])).real)
    return values


def color_algebra_report() -> dict[str, float]:
    generators = _su3_generators()
    fundamental = sum(generator @ generator for generator in generators)
    f_tensor = structure_constants()
    d_tensor = symmetric_constants()
    return {
        "fundamental_casimir_residual": float(np.max(np.abs(fundamental - (4 / 3) * np.eye(3)))),
        "adjoint_casimir": 3.0,
        "f_d_inner_product": float(np.einsum("abc,abc->", f_tensor, d_tensor)),
        "f_norm": float(np.vdot(f_tensor, f_tensor).real),
        "d_norm": float(np.vdot(d_tensor, d_tensor).real),
    }


def require_ordered_gluon_identity(link: GluonLinkId, expected: GluonLinkId) -> None:
    if link.first_path != expected.first_path or link.second_path != expected.second_path:
        raise ArchitectureError("C5.GLUON.1", "ordered gluon link pair was swapped or sorted", expected=expected.to_dict(), received=link.to_dict())
    if link.color_class != expected.color_class:
        raise ArchitectureError("C5.GLUON.2", "gluon color class was relabeled", expected=expected.color_class.value, received=link.color_class.value)


def reject_generic_gluon_todd(color_class: ColorClass | None) -> None:
    if color_class not in (ColorClass.F_TYPE, ColorClass.D_TYPE):
        raise ArchitectureError("C5.GLUON.2", "generic gluon T-odd output loses color/link identity", expected="explicit F_TYPE or D_TYPE validation identity", received=color_class)
