"""Exact C409 derivative-count and longitudinal-factor reconciliation."""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Any, Mapping

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    RESOLUTION_LABELS,
    content_root,
)
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.color_spin import (
    EXPECTED_SCALARS,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.axis import (
    external_mode_axis,
    intermediate_axis,
)
from deuteron_wigner.bridge.c407_c117_i2_same_species_descendants.descendants import (
    gluon_current_pair_factor_exact,
    same_species_weight_exact,
)

from .authority import STATUS, derivative_count_authority, scale_power_reconciliation


def _exact(value: Fraction) -> Mapping[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "exact": str(value),
        "float": float(value),
    }


def c114_inverse_square_exact(external_k: Fraction, intermediate_k: Fraction) -> Fraction:
    transfer = intermediate_k - external_k
    if transfer == 0:
        raise ValueError("Q0 excludes zero transfer")
    if transfer.denominator != 1:
        raise ValueError("same-boundary longitudinal transfer must be integer")
    return Fraction(1, 1) / (transfer * transfer)


def c406_gluon_current_pair_exact(
    external_k: Fraction,
    intermediate_k: Fraction,
) -> Fraction:
    """Product of two normalized C406 one-gluon current magnitudes.

    The two minus signs cancel.  Color is not included here.
    """
    return gluon_current_pair_factor_exact(external_k, intermediate_k)


def c409_reconstructed_jgjg_weight_exact(
    external_k: Fraction,
    intermediate_k: Fraction,
) -> Fraction:
    return (
        EXPECTED_SCALARS["J_gJ_g"]
        * c406_gluon_current_pair_exact(external_k, intermediate_k)
        * c114_inverse_square_exact(external_k, intermediate_k)
    )


def extra_derivative_multiplier_exact(mode_k: Fraction) -> Fraction:
    """Dimensionless k factor represented by a historical extra pi*k/L leaf.

    This function exists only for the over-counting audit.  It is never used by
    the C409 numerical product-block implementation.
    """
    if mode_k <= 0:
        raise ValueError("positive longitudinal mode required")
    return mode_k


@lru_cache(maxsize=1)
def derivative_count_validation() -> Mapping[str, Any]:
    rows = []
    maximum_float_residual = 0.0
    extra_c119_changed = 0
    extra_c124_changed = 0
    for resolution in RESOLUTION_LABELS:
        external = external_mode_axis(resolution, "GLUON", "qg->qg")
        for external_id, external_k in external:
            for item in intermediate_axis(
                resolution,
                "GLUON",
                "qg->qg",
                external_k,
                external_id,
            ):
                reconstructed = c409_reconstructed_jgjg_weight_exact(
                    external_k, item.intermediate_k
                )
                c407 = same_species_weight_exact(
                    "GLUON", external_k, item.intermediate_k
                )
                exact_match = reconstructed == c407
                residual = abs(float(reconstructed) - float(c407))
                maximum_float_residual = max(maximum_float_residual, residual)
                with_c119 = reconstructed * extra_derivative_multiplier_exact(
                    item.intermediate_k
                )
                with_c124 = reconstructed * extra_derivative_multiplier_exact(
                    item.intermediate_k
                )
                if with_c119 != reconstructed:
                    extra_c119_changed += 1
                if with_c124 != reconstructed:
                    extra_c124_changed += 1
                rows.append(
                    {
                        "resolution": resolution,
                        "external_id": external_id,
                        "external_k": _exact(external_k),
                        "intermediate_k": _exact(item.intermediate_k),
                        "transfer_q": _exact(item.transfer_q),
                        "C114_inverse_square": _exact(
                            c114_inverse_square_exact(external_k, item.intermediate_k)
                        ),
                        "C406_current_pair_factor": _exact(
                            c406_gluon_current_pair_exact(
                                external_k, item.intermediate_k
                            )
                        ),
                        "C_A": _exact(EXPECTED_SCALARS["J_gJ_g"]),
                        "C409_reconstructed_weight": _exact(reconstructed),
                        "C407_weight": _exact(c407),
                        "exact_match": exact_match,
                        "C119_extra_leaf_would_change_weight": with_c119 != reconstructed,
                        "C124_extra_member_derivative_would_change_weight": with_c124
                        != reconstructed,
                    }
                )
    payload = {
        "schema": "C409-C117-I2-JGJG-DERIVATIVE-COUNT-VALIDATION-V1",
        "status": STATUS,
        "authority_root": derivative_count_authority()["root"],
        "scale_power_root": scale_power_reconciliation()["root"],
        "rows": tuple(rows),
        "row_count": len(rows),
        "expected_row_count": 62,
        "all_exact_C407_reconstructions": all(row["exact_match"] for row in rows),
        "maximum_float_residual": maximum_float_residual,
        "rows_changed_by_illicit_C119_extra_leaf": extra_c119_changed,
        "rows_changed_by_illicit_C124_extra_member_derivative": extra_c124_changed,
        "extra_derivative_factors_used_in_C409": 0,
        "pass": bool(
            len(rows) == 62
            and all(row["exact_match"] for row in rows)
            and maximum_float_residual == 0.0
            and extra_c119_changed > 0
            and extra_c124_changed > 0
        ),
        "complete_C117_action": False,
    }
    if payload["row_count"] != payload["expected_row_count"]:
        raise RuntimeError("C409 J_gJ_g derivative-validation row count changed")
    if not payload["pass"]:
        raise RuntimeError("C409 derivative-count validation failed")
    return dict(payload, root=content_root(payload))


__all__ = [
    "c114_inverse_square_exact",
    "c406_gluon_current_pair_exact",
    "c409_reconstructed_jgjg_weight_exact",
    "extra_derivative_multiplier_exact",
    "derivative_count_validation",
]
