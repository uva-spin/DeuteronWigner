#!/usr/bin/env python3
"""Benchmark the author-recommended PRC106 set-A Norfolk isoscalar terms."""

from __future__ import annotations

import csv
from pathlib import Path

from deuteron_wigner.two_body_current import (
    NORFOLK_PRC106_SET_A_DEUTERON_MOMENTS,
    NORFOLK_PRC106_SET_A_ISOSCALAR_LECS,
    norfolk_n3lo_magnetic_moment,
)
from deuteron_wigner.wavefunctions.norfolk import load_norfolk_coordinate


def main() -> None:
    destination = Path(
        "outputs/stage0/norfolk_prc106_set_a_isoscalar_benchmark.csv"
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, float | str | bool]] = []
    for model, lecs in NORFOLK_PRC106_SET_A_ISOSCALAR_LECS.items():
        wave = load_norfolk_coordinate(f"data/raw/norfolk/fdeut.{model}")
        result = norfolk_n3lo_magnetic_moment(
            wave,
            model=model,
            isoscalar_lecs=lecs,
        )
        target = NORFOLK_PRC106_SET_A_DEUTERON_MOMENTS[model]
        row: dict[str, float | str | bool] = {
            "model": model,
            "source": "PRC106 Table II set A and Table IV",
            "d1_set_a": lecs[0],
            "d2_set_a": lecs[1],
            "d1_calculated": result["nonminimal_contact"],
            "d1_table_iv": target["d1"],
            "d1_table_iv_error": target["d1_error"],
            "d1_residual": result["nonminimal_contact"] - target["d1"],
            "d2_calculated": result["ope"],
            "d2_table_iv": target["d2"],
            "d2_table_iv_error": target["d2_error"],
            "d2_residual": result["ope"] - target["d2"],
            "d2_i1_calculated": result["ope_i1"],
            "d2_i2_calculated": result["ope_i2"],
            "unit_d1_contact": result["contact_unit_d1"],
            "unit_d2_i1": result["ope_i1_unit_d2"],
            "unit_d2_i2": result["ope_i2_unit_d2"],
            "unit_d2_total": result["ope_unit_d2"],
            "regulator": "I_k(r) -> C_RL(r) I_k(r)",
            "d1_compatible_with_table_iv_error": abs(
                result["nonminimal_contact"] - target["d1"]
            ) <= target["d1_error"],
            "d2_compatible_with_table_iv_error": abs(
                result["ope"] - target["d2"]
            ) <= target["d2_error"],
        }
        rows.append(row)

    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(row)
    print(f"Wrote {destination}")


if __name__ == "__main__":
    main()
