"""Constituent-resolved nuclear parents that never collapse to an isoscalar."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .gluon_correlator import Spin1GluonCorrelator
from .quark_correlator import Spin1QuarkCorrelator


def _qadd(left, right):
    return Spin1QuarkCorrelator(
        left.vector+right.vector,
        left.axial+right.axial,
        left.transverse+right.transverse,
    )


def _qsub(left, right):
    return Spin1QuarkCorrelator(
        left.vector-right.vector,
        left.axial-right.axial,
        left.transverse-right.transverse,
    )


@dataclass(frozen=True)
class ResolvedQuarkNuclearParent:
    """Proton, neutron, nuclear, and total quark parents at one phase point."""

    proton: Spin1QuarkCorrelator
    neutron: Spin1QuarkCorrelator
    canonical_total: Spin1QuarkCorrelator

    @property
    def nucleon_sum(self):
        return _qadd(self.proton, self.neutron)

    @property
    def proton_minus_neutron(self):
        return _qsub(self.proton, self.neutron)

    @property
    def nuclear_correction(self):
        return _qsub(self.canonical_total, self.nucleon_sum)

    def components(self):
        return {
            "proton_in_deuteron": self.proton,
            "neutron_in_deuteron": self.neutron,
            "nucleon_sum": self.nucleon_sum,
            "proton_minus_neutron": self.proton_minus_neutron,
            "nuclear_correction": self.nuclear_correction,
            "canonical_spin1_total": self.canonical_total,
        }

    def closure_residual(self) -> float:
        closed = _qadd(self.nucleon_sum, self.nuclear_correction)
        return float(max(
            np.max(np.abs(closed.vector-self.canonical_total.vector)),
            np.max(np.abs(closed.axial-self.canonical_total.axial)),
            np.max(np.abs(
                closed.transverse-self.canonical_total.transverse
            )),
        ))


@dataclass(frozen=True)
class ResolvedGluonNuclearParent:
    """Proton, neutron, nuclear, and total gluon parents at one phase point."""

    proton: Spin1GluonCorrelator
    neutron: Spin1GluonCorrelator
    canonical_total: Spin1GluonCorrelator

    @property
    def nucleon_sum(self):
        return Spin1GluonCorrelator(
            self.proton.values+self.neutron.values
        )

    @property
    def proton_minus_neutron(self):
        return Spin1GluonCorrelator(
            self.proton.values-self.neutron.values
        )

    @property
    def nuclear_correction(self):
        return Spin1GluonCorrelator(
            self.canonical_total.values-self.nucleon_sum.values
        )

    def components(self):
        return {
            "proton_in_deuteron": self.proton,
            "neutron_in_deuteron": self.neutron,
            "nucleon_sum": self.nucleon_sum,
            "proton_minus_neutron": self.proton_minus_neutron,
            "nuclear_correction": self.nuclear_correction,
            "canonical_spin1_total": self.canonical_total,
        }

    def closure_residual(self) -> float:
        closed = self.nucleon_sum.values+self.nuclear_correction.values
        return float(np.max(np.abs(closed-self.canonical_total.values)))
