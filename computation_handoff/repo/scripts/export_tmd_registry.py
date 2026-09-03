#!/usr/bin/env python3
"""Export complete leading-twist spin-1 quark, antiquark, and gluon registries."""

from __future__ import annotations

import csv
from pathlib import Path

from deuteron_wigner.gtmd import Species
from deuteron_wigner.registry import (
    leading_twist_gluon_registry,
    leading_twist_quark_registry,
)


def main() -> None:
    entries = []
    for registry in (
        leading_twist_quark_registry(Species.QUARK),
        leading_twist_quark_registry(Species.ANTIQUARK),
        leading_twist_gluon_registry(),
    ):
        entries.extend(registry.select())
    destination = Path("outputs/stage0/leading_twist_tmd_registry.csv")
    destination.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        {
            "species": entry.species.value,
            "name": entry.name,
            "target_channel": entry.target_channel.value,
            "parton_polarization": entry.parton_polarization,
            "transverse_rank": entry.transverse_rank,
            "parent_projection": entry.parent_projection,
            "gauge_link_required": int(entry.gauge_link_required),
            "collinear_limit": entry.collinear_limit.value,
            "matching_status": entry.matching_status.value,
            "positivity_block": entry.positivity_block,
            "time_reversal": "odd" if "T-odd" in entry.notes else "even",
            "notes": entry.notes,
        }
        for entry in entries
    ]
    with destination.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"# entries={len(rows)} output={destination}")


if __name__ == "__main__":
    main()
