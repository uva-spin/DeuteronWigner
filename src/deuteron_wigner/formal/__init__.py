"""Typed, dependency-light identities wrapping the accepted numerical model."""

from .coordinates import CoordinateKind, CoordinateSpec, coordinate_spec
from .diagnostics import ArchitectureError
from .gauge_path import (
    ColorClass, ColorRepresentation, GluonLinkId, StapleOrientation,
    WilsonPathId, standard_staple,
)
from .maps import AdapterRegistry, MapClass, TypedAdapter, TypedMap
from .operator_identity import (
    DecoratedOperatorId, IdentityState, OperationKind, assess_completeness,
)
from .sector_space import ResolutionLayer, SectorId
from .transverse_rank import CoefficientRole, RankSpec, rank_spec

__all__ = [
    "AdapterRegistry", "ArchitectureError", "CoefficientRole", "ColorClass",
    "ColorRepresentation", "CoordinateKind", "CoordinateSpec",
    "DecoratedOperatorId", "GluonLinkId", "IdentityState", "MapClass",
    "OperationKind", "RankSpec", "ResolutionLayer", "SectorId",
    "StapleOrientation", "TypedAdapter", "TypedMap", "WilsonPathId",
    "assess_completeness", "coordinate_spec", "rank_spec", "standard_staple",
]
