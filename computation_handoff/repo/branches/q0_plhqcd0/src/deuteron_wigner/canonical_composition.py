"""Fail-closed composition graph for the canonical spin-1 TMD model.

The production member ledger records *available* calculations.  This module
records which of those calculations may form one physical model.  It prevents
an alternative scenario, a duplicated amplitude, or a scheme-incompatible
input from entering the canonical parent merely because it has valid numbers.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Iterable, Mapping


class CompositionRole(str, Enum):
    BASELINE = "baseline"
    ADDITIVE = "additive"
    ALTERNATIVE = "alternative"
    UNCERTAINTY_MEMBER = "uncertainty_member"
    COMPARISON_ONLY = "comparison_only"


class CanonicalStatus(str, Enum):
    ACTIVE = "active"
    CONDITIONAL = "conditional"
    BLOCKED = "blocked"
    EXCLUDED = "excluded"


@dataclass(frozen=True)
class CanonicalComponent:
    component_id: str
    role: CompositionRole
    status: CanonicalStatus
    sectors: tuple[str, ...]
    tmds: tuple[str, ...]
    amplitude_identity: str
    source_artifact: str
    scheme_id: str
    dependencies: tuple[str, ...] = ()
    exclusive_with: tuple[str, ...] = ()
    validity: str = ""
    evidence_class: str = ""
    reason: str = ""
    replacement_task: str = ""

    @staticmethod
    def from_mapping(values: Mapping[str, object]) -> "CanonicalComponent":
        return CanonicalComponent(
            component_id=str(values["component_id"]),
            role=CompositionRole(str(values["role"])),
            status=CanonicalStatus(str(values["status"])),
            sectors=tuple(str(x) for x in values["sectors"]),
            tmds=tuple(str(x) for x in values["tmds"]),
            amplitude_identity=str(values["amplitude_identity"]),
            source_artifact=str(values["source_artifact"]),
            scheme_id=str(values["scheme_id"]),
            dependencies=tuple(str(x) for x in values.get("dependencies", ())),
            exclusive_with=tuple(str(x) for x in values.get("exclusive_with", ())),
            validity=str(values.get("validity", "")),
            evidence_class=str(values.get("evidence_class", "")),
            reason=str(values.get("reason", "")),
            replacement_task=str(values.get("replacement_task", "")),
        )


class CanonicalCompositionGraph:
    """Validated directed graph with explicit exclusion and readiness rules."""

    def __init__(self, components: Iterable[CanonicalComponent], scheme_id: str):
        items = tuple(components)
        self.components = {item.component_id: item for item in items}
        self.scheme_id = scheme_id
        if len(self.components) != len(items):
            raise ValueError("canonical component IDs must be unique")
        self._validate_structure()

    @classmethod
    def from_json(cls, path: str | Path) -> "CanonicalCompositionGraph":
        payload = json.loads(Path(path).read_text())
        return cls(
            (CanonicalComponent.from_mapping(x) for x in payload["components"]),
            scheme_id=str(payload["canonical_scheme_id"]),
        )

    def _validate_structure(self) -> None:
        known = set(self.components)
        for item in self.components.values():
            if not item.component_id or not item.amplitude_identity:
                raise ValueError("components require IDs and amplitude identities")
            missing = (set(item.dependencies) | set(item.exclusive_with)) - known
            if missing:
                raise ValueError(
                    f"{item.component_id} references unknown components {sorted(missing)}"
                )
            if item.status == CanonicalStatus.BLOCKED and not item.replacement_task:
                raise ValueError("blocked components require an executable replacement task")
            if item.status == CanonicalStatus.ACTIVE and item.role in {
                CompositionRole.ALTERNATIVE,
                CompositionRole.COMPARISON_ONLY,
            }:
                raise ValueError("alternative/comparison components cannot be active")

    def validate_selection(self, selected_ids: Iterable[str]) -> None:
        selected = tuple(selected_ids)
        if len(set(selected)) != len(selected):
            raise ValueError("a component cannot be selected twice")
        unknown = set(selected) - set(self.components)
        if unknown:
            raise ValueError(f"unknown canonical components: {sorted(unknown)}")
        chosen = [self.components[x] for x in selected]
        identities: dict[str, str] = {}
        for item in chosen:
            if item.status not in {CanonicalStatus.ACTIVE, CanonicalStatus.CONDITIONAL}:
                raise ValueError(
                    f"{item.component_id} is {item.status.value}, not canonical-selectable"
                )
            if item.scheme_id != self.scheme_id:
                raise ValueError(
                    f"{item.component_id} has scheme {item.scheme_id}, expected "
                    f"{self.scheme_id}"
                )
            absent = set(item.dependencies) - set(selected)
            if absent:
                raise ValueError(
                    f"{item.component_id} lacks dependencies {sorted(absent)}"
                )
            conflict = set(item.exclusive_with) & set(selected)
            if conflict:
                raise ValueError(
                    f"{item.component_id} conflicts with {sorted(conflict)}"
                )
            previous = identities.get(item.amplitude_identity)
            if previous is not None:
                raise ValueError(
                    f"amplitude {item.amplitude_identity} duplicated by "
                    f"{previous} and {item.component_id}"
                )
            identities[item.amplitude_identity] = item.component_id

    def blockers(self) -> tuple[CanonicalComponent, ...]:
        return tuple(
            x for x in self.components.values()
            if x.status == CanonicalStatus.BLOCKED
        )

    def active_ids(self) -> tuple[str, ...]:
        return tuple(
            x.component_id for x in self.components.values()
            if x.status in {CanonicalStatus.ACTIVE, CanonicalStatus.CONDITIONAL}
        )

