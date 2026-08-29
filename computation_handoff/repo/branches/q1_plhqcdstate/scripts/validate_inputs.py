#!/usr/bin/env python3
"""Print the normalization checks recorded in the hand-off log."""

from deuteron_wigner.wavefunctions.av18 import (
    av18_asymptotic_tail_norm,
    load_av18_coordinate,
    load_av18_momentum,
)
from deuteron_wigner.wavefunctions.cd_bonn import cd_bonn_parameters


def main() -> None:
    coordinate = load_av18_coordinate("data/raw/av18/deut.wf")
    momentum = load_av18_momentum("data/raw/av18/deut.wfk")
    coordinate_norms = coordinate.component_norms()
    tail = av18_asymptotic_tail_norm(coordinate.grid[-1])
    momentum_norms = momentum.component_norms()
    cd_bonn = cd_bonn_parameters()
    cd_coordinate = cd_bonn.coordinate_norms()
    cd_momentum = cd_bonn.momentum_norms()
    print(f"AV18 coordinate completed norm: {sum(coordinate_norms) + sum(tail):.12f}")
    print(f"AV18 coordinate completed P_D:  {coordinate_norms[1] + tail[1]:.12f}")
    print(f"AV18 momentum norm:             {sum(momentum_norms):.12f}")
    print(f"AV18 momentum P_D:              {momentum_norms[1]:.12f}")
    print(f"CD-Bonn coordinate norm:        {sum(cd_coordinate):.12f}")
    print(f"CD-Bonn coordinate P_D:         {cd_coordinate[1]:.12f}")
    print(f"CD-Bonn momentum norm:          {sum(cd_momentum):.12f}")
    print(f"CD-Bonn momentum P_D:           {cd_momentum[1]:.12f}")


if __name__ == "__main__":
    main()

