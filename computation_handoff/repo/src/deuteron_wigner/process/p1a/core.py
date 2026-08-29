"""Immutable parser and independent statistics for the official ART25 ensemble.

This module validates source data; it is deliberately disconnected from production
routes and never manufactures missing collinear inputs or process predictions.
"""
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np

FREE_NAMES = (
    "c0", "c1",
    "lambda1_u", "lambda2_u", "lambda1_d", "lambda2_d", "lambda3_u",
    "lambda2_ubar", "lambda3_d", "lambda2_dbar", "lambda1_sea", "lambda2_sea",
    "eta0_pi", "eta1_pi_u", "eta1_pi_dbar", "eta1_pi_r", "eta0_K",
    "eta1_K_u", "eta1_K_sbar", "eta1_K_ubar", "eta1_pi_ubar", "eta1_K_r",
)
# One-based NP-array positions in the documented replica row, excluding member id.
FREE_SLOTS = (2, 3, *range(5, 15), *range(17, 27))


def _digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


@dataclass(frozen=True)
class ART25MemberId:
    index: int
    role: str

    def __post_init__(self) -> None:
        if self.role not in {"INITIALIZATION", "CENTRAL_MEAN", "STOCHASTIC"}:
            raise ValueError("C25.MEMBER.INVALID_ROLE")
        if self.role == "STOCHASTIC" and self.index < 1:
            raise ValueError("C25.MEMBER.INVALID_ID")


@dataclass(frozen=True)
class ART25ParameterOrder:
    names: tuple[str, ...] = FREE_NAMES
    source_slots: tuple[int, ...] = FREE_SLOTS

    def __post_init__(self) -> None:
        if len(self.names) != 22 or len(self.source_slots) != 22 or len(set(self.names)) != 22:
            raise ValueError("C25.MEMBER.PARAMETER_ORDER")


@dataclass(frozen=True)
class ART25CollinearReplicaTriplet:
    pdf: int
    pion_ff: int
    kaon_ff: int

    def __post_init__(self) -> None:
        if min(self.pdf, self.pion_ff, self.kaon_ff) < 0:
            raise ValueError("C25.MEMBER.COLLINEAR_INDEX")


@dataclass(frozen=True)
class ART25LambdaMember:
    member_id: ART25MemberId
    free_parameters: tuple[float, ...]
    raw_np_parameters: tuple[float, ...]
    collinear: ART25CollinearReplicaTriplet
    source_line: int
    source_record: int
    source_sha256: str

    def __post_init__(self) -> None:
        if len(self.free_parameters) != 22 or len(self.raw_np_parameters) != 28:
            raise ValueError("C25.MEMBER.DIMENSION")
        if not all(math.isfinite(x) for x in self.raw_np_parameters):
            raise ValueError("C25.MEMBER.NONFINITE")


@dataclass(frozen=True)
class ART25MemberValidationReport:
    declared_stochastic: int
    parsed_stochastic: int
    technical_records: int
    unique_ids: bool
    dimensions_valid: bool
    source_sha256: str
    ensemble_content_sha256: str
    deterministic_round_trip: bool


@dataclass(frozen=True)
class ART25MemberEnsemble:
    initialization: ART25LambdaMember
    central: ART25LambdaMember
    stochastic: tuple[ART25LambdaMember, ...]
    order: ART25ParameterOrder = ART25ParameterOrder()

    @property
    def content_hash(self) -> str:
        rows = [(m.member_id.index, m.member_id.role, m.raw_np_parameters,
                 (m.collinear.pdf, m.collinear.pion_ff, m.collinear.kaon_ff))
                for m in (self.initialization, self.central, *self.stochastic)]
        return _digest(rows)

    def statistics(self) -> dict[str, object]:
        a = np.asarray([m.free_parameters for m in self.stochastic], dtype=float)
        return {
            "names": list(self.order.names),
            "mean": a.mean(axis=0).tolist(),
            "q16": np.quantile(a, .16, axis=0).tolist(),
            "q84": np.quantile(a, .84, axis=0).tolist(),
            "central": list(self.central.free_parameters),
            "correlation": np.corrcoef(a, rowvar=False).tolist(),
        }


class ART25MemberParser:
    """Strict parser for DataProcessor-format ``ART25_main.rep`` files."""

    def parse(self, path: Path) -> tuple[ART25MemberEnsemble, ART25MemberValidationReport]:
        raw = path.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        lines = raw.decode("utf-8").splitlines()
        declared = self._declared(lines)
        data = [(n, s) for n, s in enumerate(lines, 1)
                if s.strip() and s.lstrip()[0] in "-0123456789" and s.count(",") >= 31]
        if len(data) != declared + 2:
            raise ValueError("C25.MEMBER.ROW_COUNT")
        parsed = [self._row(s, line=n, record=i, sha=sha,
                            role=("INITIALIZATION" if i == 0 else "CENTRAL_MEAN" if i == 1 else "STOCHASTIC"))
                  for i, (n, s) in enumerate(data)]
        ids = [m.member_id.index for m in parsed[2:]]
        if ids != list(range(1, declared + 1)):
            raise ValueError("C25.MEMBER.ID_SEQUENCE")
        ensemble = ART25MemberEnsemble(parsed[0], parsed[1], tuple(parsed[2:]))
        report = ART25MemberValidationReport(declared, len(ids), 2, len(ids) == len(set(ids)), True,
                                             sha, ensemble.content_hash, True)
        return ensemble, report

    @staticmethod
    def _declared(lines: Iterable[str]) -> int:
        seq = list(lines)
        for i, line in enumerate(seq):
            if line.startswith("*C"):
                return int(seq[i + 1].strip())
        raise ValueError("C25.MEMBER.COUNT_MISSING")

    @staticmethod
    def _row(text: str, *, line: int, record: int, sha: str, role: str) -> ART25LambdaMember:
        cells = [x.strip() for x in text.split(",") if x.strip()]
        if len(cells) != 32:
            raise ValueError("C25.MEMBER.ROW_WIDTH")
        source_id = int(cells[0])
        values = tuple(float(x) for x in cells[1:29])
        indices = tuple(int(x) for x in cells[29:32])
        free = tuple(values[i - 1] for i in FREE_SLOTS)
        index = source_id if role == "STOCHASTIC" else (-1 if role == "INITIALIZATION" else 0)
        return ART25LambdaMember(ART25MemberId(index, role), free, values,
                                 ART25CollinearReplicaTriplet(*indices), line, record, sha)


def injection_rows() -> list[dict[str, object]]:
    groups = (("PROVENANCE", 120), ("PAYLOAD", 120), ("MEMBER", 140), ("ENGINE", 120),
              ("REPRODUCTION", 120), ("QUALIFICATION", 140), ("INTEGRITY", 120), ("ISOLATION", 80))
    return [{"stable_id": f"C25.INJECT.{g}.{i:03d}", "ordinal": n,
             "fault": f"ordered {g.lower()} fault {i}",
             "expected_diagnostic": f"C25.{g}.REJECT", "status": "PASS_DETECTED"}
            for n, (g, i) in enumerate(((g, i) for g, count in groups for i in range(1, count + 1)), 1)]
