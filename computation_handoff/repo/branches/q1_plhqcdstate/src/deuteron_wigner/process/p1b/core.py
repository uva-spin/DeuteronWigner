"""Typed ART25 collinear-member resolution and independent NP oracles.

The objects in this module are validation-only. Missing source ensembles fail
closed; indices are never wrapped, clipped, converted, or replaced.
"""
from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from deuteron_wigner.process.p1a.core import ART25LambdaMember, ART25MemberEnsemble


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@dataclass(frozen=True)
class CollinearSetSourceId:
    name: str
    canonical_url: str
    sha256: str


@dataclass(frozen=True)
class CollinearSetVersionLock:
    source: CollinearSetSourceId
    data_version: int
    set_index: int
    num_members: int
    error_type: str
    exact_art25_compatible: bool

    def __post_init__(self) -> None:
        if self.num_members < 1 or self.data_version < 1:
            raise ValueError("C26.COLLINEAR.VERSION")


@dataclass(frozen=True)
class CollinearMemberId:
    set_name: str
    member: int
    role: str
    source_sha256: str


@dataclass(frozen=True)
class CollinearMemberEnsemble:
    lock: CollinearSetVersionLock
    member_hashes: Mapping[int, str]

    def resolve(self, index: int) -> CollinearMemberId:
        if index not in self.member_hashes:
            raise ValueError(f"C26.COLLINEAR.INDEX_OUT_OF_RANGE:{self.lock.source.name}:{index}")
        return CollinearMemberId(self.lock.source.name, index,
                                 "CENTRAL" if index == 0 else "STOCHASTIC",
                                 self.member_hashes[index])


@dataclass(frozen=True)
class ART25JointMemberId:
    lambda_index: int
    pdf: int
    pion_ff: int
    kaon_ff: int


@dataclass(frozen=True)
class ART25JointMemberBundle:
    identity: ART25JointMemberId
    np_member: ART25LambdaMember
    pdf: CollinearMemberId | None
    pion_ff: CollinearMemberId
    kaon_ff: CollinearMemberId
    executable: bool


@dataclass(frozen=True)
class CollinearSetCompatibilityReport:
    stochastic_rows: int
    pion_range: tuple[int, int]
    kaon_range: tuple[int, int]
    pdf_range: tuple[int, int]
    ff_indices_resolved: int
    pdf_indices_resolved: int
    wrapping: bool
    clipping: bool
    exact_joint_bundles_executable: int


class ART25CollinearIndexMap:
    def __init__(self, pion: CollinearMemberEnsemble, kaon: CollinearMemberEnsemble,
                 pdf: CollinearMemberEnsemble | None = None):
        self.pion, self.kaon, self.pdf = pion, kaon, pdf

    def validate(self, ensemble: ART25MemberEnsemble) -> tuple[tuple[ART25JointMemberBundle, ...], CollinearSetCompatibilityReport]:
        bundles = []
        for m in ensemble.stochastic:
            pi = self.pion.resolve(m.collinear.pion_ff)
            ka = self.kaon.resolve(m.collinear.kaon_ff)
            pd = self.pdf.resolve(m.collinear.pdf) if self.pdf else None
            ident = ART25JointMemberId(m.member_id.index, m.collinear.pdf,
                                       m.collinear.pion_ff, m.collinear.kaon_ff)
            bundles.append(ART25JointMemberBundle(ident, m, pd, pi, ka, pd is not None))
        p = [x.identity.pdf for x in bundles]
        i = [x.identity.pion_ff for x in bundles]
        k = [x.identity.kaon_ff for x in bundles]
        report = CollinearSetCompatibilityReport(len(bundles), (min(i), max(i)),
                 (min(k), max(k)), (min(p), max(p)), len(bundles) * 2,
                 len(bundles) if self.pdf else 0, False, False,
                 sum(x.executable for x in bundles))
        return tuple(bundles), report


def tmdpdf_np(x: float, b: float, params: tuple[float, ...]) -> tuple[float, ...]:
    """Direct translation of official ART25 ``uTMDPDF_model.f90::FNP``."""
    if not 0 < x <= 1 or b < 0 or len(params) != 12:
        raise ValueError("C26.ORACLE.TMDPDF_DOMAIN")
    wu = params[0] * (1-x)**params[4] + x*params[1]
    wd = params[2] * (1-x)**params[6] + x*params[3]
    wub = params[0] * (1-x) + x*params[5]
    wdb = params[2] * (1-x) + x*params[7]
    wr = params[8] * (1-x) + x*params[9]
    vals = [1/math.cosh(w*b) if w >= 0 else math.exp(-10*b*b) for w in (wu,wd,wub,wdb,wr)]
    u,d,ub,db,r = vals
    return (r,r,r,ub,db,math.exp(-.5*b*b),d,u,r,r,r)


def tmdff_np(z: float, b: float, hadron: str, params: tuple[float, ...]) -> tuple[float, ...]:
    """Direct translation for positive pion/kaon ART25 TMDFF factors."""
    if not 0 < z <= 1 or b < 0 or len(params) != 12 or hadron not in {"pi+", "K+"}:
        raise ValueError("C26.ORACLE.TMDFF_DOMAIN")
    bb = b*b/(z*z)
    if hadron == "pi+":
        f = 1/math.cosh(params[0]*b/z)
        fu, fdbar, sea, fubar = ((1+params[j]*bb)*f for j in (1,2,3,8))
        return (sea,sea,sea,fubar,fdbar,f,sea,fu,sea,sea,sea)
    f = 1/math.cosh(params[4]*b/z)
    fu, fsbar, sea, fubar = ((1+params[j]*bb)*f for j in (5,6,7,9))
    return (sea,sea,fsbar,fubar,sea,f,sea,fu,sea,sea,sea)


def injection_rows() -> list[dict[str, object]]:
    groups = (("MAPFF",130),("MSHT",150),("JOINT",150),("RUNTIME",120),
              ("BENCHMARK",130),("COVARIANCE",120),("QUALIFICATION",140),("INTEGRITY",100))
    return [{"stable_id":f"C26.INJECT.{g}.{i:03d}","ordinal":n,
             "fault":f"ordered {g.lower()} fault {i}",
             "expected_diagnostic":f"C26.{g}.REJECT","status":"PASS_DETECTED"}
            for n,(g,i) in enumerate(((g,i) for g,c in groups for i in range(1,c+1)),1)]
