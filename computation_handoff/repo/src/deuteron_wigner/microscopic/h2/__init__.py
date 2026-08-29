"""C9/H2 coupled qqq + qqqg validation architecture."""

from .core import (
    CoupledH2Basis, CoupledH2Hamiltonian, H2AssumptionBundle, H2BasisState,
    H2InstantaneousTerm, H2Plan, H2RenormalizationTrajectory,
    H2VectorCurrent, MicroscopicRescatteringInput,
    MicroscopicWilsonInputAdapter, build_coupled_basis_tower,
    build_hamiltonian, compile_h2_plan, fit_h2_trajectory,
)
from .diagnostics import (
    coupled_ttn_benchmark, feshbach_comparison, gluon_oam_ledger,
    sector_tracking_benchmark, ward_benchmark,
)

__all__ = [
    "CoupledH2Basis","CoupledH2Hamiltonian","H2AssumptionBundle",
    "H2BasisState","H2InstantaneousTerm","H2Plan",
    "H2RenormalizationTrajectory","H2VectorCurrent",
    "MicroscopicRescatteringInput","MicroscopicWilsonInputAdapter",
    "build_coupled_basis_tower","build_hamiltonian","compile_h2_plan",
    "coupled_ttn_benchmark","feshbach_comparison","fit_h2_trajectory",
    "gluon_oam_ledger","sector_tracking_benchmark","ward_benchmark",
]
