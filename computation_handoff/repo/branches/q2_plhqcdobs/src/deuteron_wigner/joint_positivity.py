"""Member-preserving target–parton joint-density positivity audits."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

import numpy as np

from .gluon_correlator import Spin1GluonCorrelator
from .quark_correlator import Spin1QuarkCorrelator


@dataclass(frozen=True)
class MemberPositivityResult:
    member: str
    points: int
    minimum_eigenvalue: float
    violating_points: int
    compatible: bool


@dataclass(frozen=True)
class JointPositivityAudit:
    sector: str
    tolerance: float
    members: tuple[MemberPositivityResult, ...]
    tensions_are_clipped: bool = False

    @property
    def all_compatible(self) -> bool:
        return all(member.compatible for member in self.members)

    @property
    def global_minimum_eigenvalue(self) -> float:
        return min(member.minimum_eigenvalue for member in self.members)


def audit_gluon_correlator_members(
    members: Mapping[str, Sequence[np.ndarray]],
    *,
    tolerance: float = 1.0e-10,
) -> JointPositivityAudit:
    if not members or tolerance < 0.0:
        raise ValueError("gluon positivity audit requires members and tolerance")
    results = []
    for member, matrices in members.items():
        if not matrices:
            raise ValueError(f"gluon member {member} has no full correlator points")
        eigenvalues = []
        for values in matrices:
            eigenvalues.append(
                Spin1GluonCorrelator(np.asarray(values)).minimum_positivity_eigenvalue()
            )
        array = np.asarray(eigenvalues, dtype=float)
        results.append(MemberPositivityResult(
            member=str(member),
            points=len(array),
            minimum_eigenvalue=float(array.min()),
            violating_points=int(np.count_nonzero(array < -tolerance)),
            compatible=bool(np.all(array >= -tolerance)),
        ))
    return JointPositivityAudit("spin1_gluon", tolerance, tuple(results))


def audit_quark_correlator_members(
    members: Mapping[str, Sequence[Spin1QuarkCorrelator]],
    *,
    tolerance: float = 1.0e-10,
) -> JointPositivityAudit:
    if not members or tolerance < 0.0:
        raise ValueError("quark positivity audit requires members and tolerance")
    results = []
    for member, correlators in members.items():
        if not correlators:
            raise ValueError(f"quark member {member} has no full correlator points")
        array = np.asarray(
            [item.minimum_positivity_eigenvalue() for item in correlators],
            dtype=float,
        )
        results.append(MemberPositivityResult(
            member=str(member),
            points=len(array),
            minimum_eigenvalue=float(array.min()),
            violating_points=int(np.count_nonzero(array < -tolerance)),
            compatible=bool(np.all(array >= -tolerance)),
        ))
    return JointPositivityAudit("spin1_quark", tolerance, tuple(results))


def refuse_projection_only_joint_audit(
    *,
    available_tmds: Sequence[str],
    required_identifiable_tmds: Sequence[str],
    ensemble_name: str,
) -> None:
    missing = sorted(set(required_identifiable_tmds) - set(available_tmds))
    if missing:
        raise ValueError(
            f"{ensemble_name} is projection-only and cannot establish joint "
            f"positivity; missing reconstructing TMDs: {missing}"
        )
    raise ValueError(
        f"{ensemble_name} supplies named projections but not their correlated "
        "member-level full matrices; joint positivity reconstruction is refused"
    )

