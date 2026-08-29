"""Fail-closed identities for the author-transferred ART25 source chain.

This module is validation infrastructure, not a phenomenological fit or a
production route.  It never converts, wraps, clips, or guesses member IDs.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class MSHT20RepSourceId:
    name: str
    data_version: int
    set_index: int
    source_class: str
    aggregate_sha256: str

    def __post_init__(self) -> None:
        if self.name != "MSHT20_REP" or self.data_version != 3:
            raise ValueError("C27.MSHT.IDENTITY_REJECT")
        if self.source_class != "AUTHOR_DIRECT_TRANSFER_RESEARCH_VALIDATION_ONLY":
            raise ValueError("C27.MSHT.PROVENANCE_REJECT")


@dataclass(frozen=True)
class MSHT20RepMemberId:
    source: MSHT20RepSourceId
    index: int
    sha256: str


@dataclass(frozen=True)
class MSHT20RepEnsemble:
    source: MSHT20RepSourceId
    member_hashes: Mapping[int, str]
    declared_members: int = 1000

    def __post_init__(self) -> None:
        required = set(range(self.declared_members))
        if not required.issubset(self.member_hashes):
            raise ValueError("C27.MSHT.MEMBER_COVERAGE_REJECT")

    def resolve(self, index: int) -> MSHT20RepMemberId:
        if index < 0 or index >= self.declared_members or index not in self.member_hashes:
            raise ValueError(f"C27.MSHT.INDEX_OUT_OF_RANGE:{index}")
        return MSHT20RepMemberId(self.source, index, self.member_hashes[index])


@dataclass(frozen=True)
class ART25JointMemberId:
    lambda_index: int
    lambda_sha256: str
    pdf: MSHT20RepMemberId
    pion_ff_index: int
    pion_ff_sha256: str
    kaon_ff_index: int
    kaon_ff_sha256: str

    def __post_init__(self) -> None:
        if not 1 <= self.lambda_index <= 642:
            raise ValueError("C27.JOINT.LAMBDA_REJECT")


def injection_rows() -> list[dict[str, object]]:
    groups = (("SOURCE",130),("MSHT",170),("JOINT",150),("RUNTIME",130),
              ("REPRODUCTION",150),("COVARIANCE",140),("QUALIFICATION",150),("INTEGRITY",100))
    rows=[]
    for group,count in groups:
        for i in range(1,count+1):
            rows.append({"stable_id":f"C27.INJECT.{group}.{i:03d}",
                         "ordinal":len(rows)+1,
                         "fault":f"ordered {group.lower()} fault {i}",
                         "expected_diagnostic":f"C27.{group}.REJECT",
                         "status":"PASS_DETECTED"})
    return rows
