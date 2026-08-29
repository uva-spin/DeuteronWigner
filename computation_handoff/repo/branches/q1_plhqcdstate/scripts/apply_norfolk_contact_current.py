#!/usr/bin/env python3
"""Apply the printed-2019 Norfolk contact current as a flagged diagnostic."""

import argparse
import csv
from pathlib import Path

from deuteron_wigner.form_factors import (
    elastic_observables,
    load_av18_electromagnetic_tables,
)
from deuteron_wigner.two_body_current import norfolk_n3lo_magnetic_moment
from deuteron_wigner.wavefunctions.norfolk import load_norfolk_coordinate

HBARC_GEV_FM = 0.1973269804


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=("nvia", "nvib", "nviia", "nviib"), required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    wave = load_norfolk_coordinate(f"data/raw/norfolk/fdeut.{arguments.model}")
    moments = norfolk_n3lo_magnetic_moment(wave, model=arguments.model)
    contact_moment = moments["minimal_contact"] + moments["nonminimal_contact"]
    reference = load_av18_electromagnetic_tables("data/raw/av18/fdeut.av18")
    deuteron_to_nucleon_mass = reference.deuteron_mass_mev / 938.9
    with arguments.source.open(encoding="utf-8") as stream:
        source_rows = list(csv.DictReader(stream))
    rows = []
    for source in source_rows:
        q_gev = float(source["DeltaT_GeV"])
        q_fm = q_gev / HBARC_GEV_FM
        # Schiavilla et al. note that the contact-current falloff is G_E^S.
        isoscalar_electric = 2.0 * float(reference.isoscalar_electric(q_fm))
        delta_gm = (
            deuteron_to_nucleon_mass * contact_moment * isoscalar_electric
        )
        gm = float(source["GM"]) + delta_gm
        structure_a, structure_b, t20 = elastic_observables(
            q_fm=q_fm,
            gc=float(source["GC"]),
            gm=gm,
            gq=float(source["GQ"]),
            deuteron_mass_mev=reference.deuteron_mass_mev,
        )
        rows.append(
            {
                "model": arguments.model,
                "DeltaT_GeV": q_gev,
                "contact_moment_nm": contact_moment,
                "G_E_isoscalar": isoscalar_electric,
                "delta_GM_contact": delta_gm,
                "GM_one_body": float(source["GM"]),
                "GM_with_contact": gm,
                "A_with_contact": float(structure_a),
                "B_with_contact": float(structure_b),
                "t20_with_contact": float(t20),
                "ope_included": 0,
                "legacy_2019_uncorrected_lecs": 1,
            }
        )
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    with arguments.output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
