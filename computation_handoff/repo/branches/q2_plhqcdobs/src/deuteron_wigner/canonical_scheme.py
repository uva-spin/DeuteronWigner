"""Per-input scale, subtraction, matching, and rank evolution contract."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Iterable, Mapping


class EvolutionRoute(str, Enum):
    FIT_NATIVE = "fit_native"
    PROJECT_CSS = "project_css"
    COMMON_KERNEL_MODEL = "common_kernel_model"
    FROZEN_COMPARISON = "frozen_comparison"
    MISSING = "missing"


class MatchingStatus(str, Enum):
    IMPLEMENTED = "implemented"
    ZERO_COEFFICIENT = "zero_coefficient"
    MODEL_BOUNDARY = "model_boundary"
    MISSING = "missing"


@dataclass(frozen=True)
class CanonicalSchemeRecord:
    input_id: str
    component_id: str
    tmds: tuple[str, ...]
    ranks: tuple[int, ...]
    initial_scale_gev: float
    target_scale_gev: float
    scheme_id: str
    soft_subtraction: str
    rapidity_prescription: str
    matching_order: str
    matching_status: MatchingStatus
    evolution_route: EvolutionRoute
    evolution_implementation: str
    canonical_eligible: bool
    reason: str

    @staticmethod
    def from_mapping(values: Mapping[str, object]) -> "CanonicalSchemeRecord":
        return CanonicalSchemeRecord(
            input_id=str(values["input_id"]),
            component_id=str(values["component_id"]),
            tmds=tuple(str(x) for x in values["tmds"]),
            ranks=tuple(int(x) for x in values["ranks"]),
            initial_scale_gev=float(values["initial_scale_gev"]),
            target_scale_gev=float(values["target_scale_gev"]),
            scheme_id=str(values["scheme_id"]),
            soft_subtraction=str(values["soft_subtraction"]),
            rapidity_prescription=str(values["rapidity_prescription"]),
            matching_order=str(values["matching_order"]),
            matching_status=MatchingStatus(str(values["matching_status"])),
            evolution_route=EvolutionRoute(str(values["evolution_route"])),
            evolution_implementation=str(values["evolution_implementation"]),
            canonical_eligible=bool(values["canonical_eligible"]),
            reason=str(values["reason"]),
        )

    def validate(self, canonical_scheme_id: str) -> None:
        if not self.input_id or not self.component_id or not self.tmds:
            raise ValueError("scheme records require input/component/TMD identity")
        if len(self.ranks) != len(self.tmds) or any(rank < 0 for rank in self.ranks):
            raise ValueError("every TMD requires a nonnegative transverse rank")
        if self.initial_scale_gev <= 0 or self.target_scale_gev <= 0:
            raise ValueError("scheme records require positive scales")
        if self.canonical_eligible:
            if self.scheme_id != canonical_scheme_id:
                raise ValueError("canonical input has an incompatible scheme")
            if self.evolution_route in {
                EvolutionRoute.FROZEN_COMPARISON, EvolutionRoute.MISSING
            }:
                raise ValueError("canonical input lacks a physical evolution route")
            if self.matching_status == MatchingStatus.MISSING:
                raise ValueError("canonical input lacks a matching declaration")
            if not self.evolution_implementation:
                raise ValueError("canonical evolution implementation is required")


class CanonicalSchemeLedger:
    def __init__(
        self, records: Iterable[CanonicalSchemeRecord], canonical_scheme_id: str
    ):
        items = tuple(records)
        self.records = {item.input_id: item for item in items}
        self.canonical_scheme_id = canonical_scheme_id
        if len(items) != len(self.records):
            raise ValueError("scheme input IDs must be unique")
        for item in items:
            item.validate(canonical_scheme_id)

    @classmethod
    def from_json(cls, path: str | Path) -> "CanonicalSchemeLedger":
        values = json.loads(Path(path).read_text())
        return cls(
            (CanonicalSchemeRecord.from_mapping(x) for x in values["inputs"]),
            str(values["canonical_scheme_id"]),
        )

    def require_canonical(self, input_ids: Iterable[str]) -> None:
        for input_id in input_ids:
            try:
                record = self.records[input_id]
            except KeyError as error:
                raise ValueError(f"input {input_id} lacks scheme metadata") from error
            if not record.canonical_eligible:
                raise ValueError(
                    f"input {input_id} is comparison-only: {record.reason}"
                )

    def blockers(self) -> tuple[CanonicalSchemeRecord, ...]:
        return tuple(x for x in self.records.values() if not x.canonical_eligible)

