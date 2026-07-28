#!/usr/bin/env python3
"""Package the two WP12 inspection overviews as an inline visualization."""

from __future__ import annotations

import base64
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "output/figures/wp12_inspection"
DESTINATION = ROOT / (
    ".codex/visualizations/2026/07/27/"
    "019f97af-fcbd-7861-85e4-c4824cfe67b8/tmd-inspection.html"
)


def uri(name: str) -> str:
    encoded = base64.b64encode((SOURCE / name).read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def main() -> None:
    quark = uri("wp12_quark_all_tmd_F_x010.png")
    gluon = uri("wp12_gluon_all_tmd_F_x010.png")
    fragment = f"""<div id="wp12-tmd-inspection">
  <style>
    #wp12-tmd-inspection {{
      display: grid;
      gap: 20px;
      color: var(--foreground);
    }}
    #wp12-tmd-inspection figure {{
      margin: 0;
      display: grid;
      gap: 6px;
    }}
    #wp12-tmd-inspection img {{
      display: block;
      width: 100%;
      height: auto;
    }}
    #wp12-tmd-inspection figcaption {{
      color: var(--muted-foreground);
      text-align: center;
    }}
  </style>
  <figure>
    <img src="{quark}" alt="Eighteen small-multiple quark and antiquark TMD plots versus transverse momentum, with u, d, anti-u and anti-d central curves and uncertainty bands.">
    <figcaption>Quarks and antiquarks: dimensional F, future staple.</figcaption>
  </figure>
  <figure>
    <img src="{gluon}" alt="Eighteen small-multiple gluon TMD plots versus transverse momentum, with f-type and d-type color structures and uncertainty bands.">
    <figcaption>Gluons: dimensional F, independent f-type and d-type components.</figcaption>
  </figure>
</div>
"""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(fragment)
    print(f"{DESTINATION}: {DESTINATION.stat().st_size} bytes")


if __name__ == "__main__":
    main()
