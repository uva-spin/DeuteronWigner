"""Source-faithful C396 19-coordinate binding inventory.

The inventory distinguishes symbolic/operator ownership from an executable
K-local sparse or matrix-free apply path.  It never substitutes the older C144
11-coordinate fixture for a C396 coordinate and never fills a missing operator
with zero.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict, dataclass
from typing import Any, Mapping, Optional, Tuple

from deuteron_wigner.bridge import hqcdrimassc43hamiltonianacceptphase1 as c396
from deuteron_wigner.bridge import hqcdid3 as c136
from deuteron_wigner.bridge import hqcdc117renormdesign1 as c259


@dataclass(frozen=True)
class CoordinateBinding:
    resolution: str
    basis_id: Mapping[str, Any]
    resolution_semantics: Mapping[str, Any]
    coordinate_id: str
    coordinate_class: str
    source_owner: str
    operator_owner: str
    operator_id: str
    units: str
    sector_support: str
    hermiticity_authority: str
    numerical_apply_status: str
    numerical_apply_path: Optional[str]
    derivative_status: str
    state_current_dependency: str
    cross_resolution_status: str
    smallest_missing_object: str
    c144_proxy_forbidden: bool = True
    selected: bool = False
    zeroed: bool = False
    physical: bool = False




_RESOLUTION_SEMANTICS = {
    "K9": {
        "resolution_label": "K9",
        "K2": 9,
        "K_fraction": "9/2",
        "Nmax": 8,
        "bHO_value": 0.40,
        "bHO_authoritative_unit": "GeV",
        "C396_field_label": "bHO_GeVinv",
        "unit_status": "CONFLICT_C46_GeV_VS_C396_GeVinv_REQUIRES_OWNER_RESOLUTION",
    },
    "K11": {
        "resolution_label": "K11",
        "K2": 11,
        "K_fraction": "11/2",
        "Nmax": 10,
        "bHO_value": 0.45,
        "bHO_authoritative_unit": "GeV",
        "C396_field_label": "bHO_GeVinv",
        "unit_status": "CONFLICT_C46_GeV_VS_C396_GeVinv_REQUIRES_OWNER_RESOLUTION",
    },
    "K13": {
        "resolution_label": "K13",
        "K2": 13,
        "K_fraction": "13/2",
        "Nmax": 12,
        "bHO_value": 0.50,
        "bHO_authoritative_unit": "GeV",
        "C396_field_label": "bHO_GeVinv",
        "unit_status": "CONFLICT_C46_GeV_VS_C396_GeVinv_REQUIRES_OWNER_RESOLUTION",
    },
}

_COUNTERTERM_APPLY_STATUS = {
    "ct_mass": (
        "IDENTIFIED_COMBINATION_ONLY_NOT_SEPARATELY_EXECUTABLE",
        "independent K-local ct_mass sparse/matrix-free operator separated from phi_mass",
    ),
    "ct_vacuum_energy": (
        "NONMATRIX_VACUUM_DIRECTION_EXCLUDED_FROM_RETAINED_HAMILTONIAN",
        "proof-level treatment of the vacuum-energy direction in the declared physical observable space",
    ),
    "ct_gluon_mass": (
        "SOURCE_PRIMITIVE_DESCRIPTOR_ONLY_NO_PUBLIC_C396_APPLY",
        "K-local gluon one-body counterterm operator apply path with basis ordering and normalization",
    ),
    "ct_sector": (
        "SOURCE_PRIMITIVE_DESCRIPTOR_ONLY_NO_PUBLIC_C396_APPLY",
        "K-local q-to-qg sector counterterm operator apply path with basis ordering and normalization",
    ),
    "ct_boundary": (
        "NONMATRIX_BOUNDARY_INTERFACE_NOT_A_SPARSE_HAMILTONIAN_TERM",
        "approved boundary-interface realization and observable-discrepancy treatment",
    ),
    "ct_truncation": (
        "NONMATRIX_TRUNCATION_INTERFACE_NOT_A_SPARSE_HAMILTONIAN_TERM",
        "approved truncation-discrepancy model rather than a fabricated matrix insertion",
    ),
}


def _plain(value: Any) -> Any:
    if hasattr(value, "items"):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(item) for item in value]
    return value


def _counterterm_metadata() -> tuple[dict[str, Mapping[str, Any]], dict[str, Mapping[str, Any]]]:
    primitive = {
        row["direction_id"]: row for row in c136.counterterm_primitive_manifest()["blocks"]
    }
    unknown = {
        row["direction_id"]: row for row in c136.unknown_direction_manifest()["directions"]
    }
    return primitive, unknown


def _c206_null_rows(resolution: str) -> Tuple[Mapping[str, Any], ...]:
    # C206/right_null_basis_manifest defines n1..n14 over VARIABLES[1:15].
    # Its first five pivots are counterterm directions 2..6 and its remaining
    # nine pivots are C151_NULL_COORDINATE_1..9.  Importing C206 in the compact
    # replay pulls a historical optional-source chain that is intentionally not
    # self-contained, so this ledger records the exact source-defined ordinal
    # crosswalk without pretending it is a numerical operator binding.
    return tuple(
        {
            "basis_id": f"C206-RNULL-{resolution}",
            "vector_id": f"n{index + 6}",
            "pivot_coordinate": f"C151_NULL_COORDINATE_{index + 1}",
            "normalization": "exact symbolic",
            "source_locator": "hqcdstctsolve1.right_null_basis_manifest",
        }
        for index in range(9)
    )


def _c117_metadata() -> dict[str, Mapping[str, Any]]:
    return {row["coefficient_id"]: row for row in c259.operator_basis()["rows"]}


def coordinate_binding_inventory() -> Mapping[str, Any]:
    primitive, unknown = _counterterm_metadata()
    c117 = _c117_metadata()
    rows: list[CoordinateBinding] = []

    for resolution in c396.RESOLUTIONS:
        parameter_record = c396.Hamiltonian_parameter_records(resolution)[0]
        null_vectors = _c206_null_rows(resolution)

        for coordinate in c396.COUNTERTERMS:
            p = primitive[coordinate]
            u = unknown[coordinate]
            status, missing = _COUNTERTERM_APPLY_STATUS[coordinate]
            rows.append(
                CoordinateBinding(
                    resolution=resolution,
                    basis_id=_plain(parameter_record["basis_id"]),
                    resolution_semantics=deepcopy(_RESOLUTION_SEMANTICS[resolution]),
                    coordinate_id=coordinate,
                    coordinate_class="counterterm",
                    source_owner=str(u["owner"]),
                    operator_owner=str(p["primitive_block_id"]),
                    operator_id=str(p["primitive_block_id"]),
                    units=str(u["units"]),
                    sector_support=str(u["support"]),
                    hermiticity_authority=str(p["hermitian_partner"]),
                    numerical_apply_status=status,
                    numerical_apply_path=None,
                    derivative_status="C396_SYMBOLIC_DH_DCOORDINATE_ONLY",
                    state_current_dependency="physical state/current response unbound",
                    cross_resolution_status="K_LOCAL_VALUE_UNMAPPED_SHARED_LABEL_NOT_EQUALITY",
                    smallest_missing_object=missing,
                )
            )

        for index, coordinate in enumerate(c396.NULLS):
            vector = null_vectors[index]
            rows.append(
                CoordinateBinding(
                    resolution=resolution,
                    basis_id=_plain(parameter_record["basis_id"]),
                    resolution_semantics=deepcopy(_RESOLUTION_SEMANTICS[resolution]),
                    coordinate_id=coordinate,
                    coordinate_class="source_null",
                    source_owner="C206 exact right-null family",
                    operator_owner=str(vector["pivot_coordinate"]),
                    operator_id=str(vector["vector_id"]),
                    units="UNBOUND_SOURCE_COORDINATE_SCALE",
                    sector_support="C206 affine ST system; physical observable support unresolved",
                    hermiticity_authority="C396 symbolic Hamiltonian-family assertion only",
                    numerical_apply_status="SYMBOLIC_RIGHT_NULL_VECTOR_NO_FINITE_BASIS_OPERATOR_APPLY",
                    numerical_apply_path=None,
                    derivative_status="C397_RESPONSE_REQUIRED_NOT_NUMERICALLY_EVALUATED",
                    state_current_dependency="observable derivative or exact irrelevance proof required",
                    cross_resolution_status=(
                        "ORDINAL_C206_TO_C396_CROSSWALK_ONLY_NO_NUMERICAL_TRANSFER_MAP"
                    ),
                    smallest_missing_object=(
                        f"K-local operator-coordinate realization for {coordinate} from "
                        f"C206 pivot {vector['pivot_coordinate']}"
                    ),
                )
            )

        for coordinate in c396.C117:
            meta = c117[coordinate]
            rows.append(
                CoordinateBinding(
                    resolution=resolution,
                    basis_id=_plain(parameter_record["basis_id"]),
                    resolution_semantics=deepcopy(_RESOLUTION_SEMANTICS[resolution]),
                    coordinate_id=coordinate,
                    coordinate_class="C117",
                    source_owner=str(meta["source_owner"]),
                    operator_owner=str(meta["operator_id"]),
                    operator_id=str(meta["operator_id"]),
                    units=str(meta["mass_dimension"]),
                    sector_support=str(meta["support"]),
                    hermiticity_authority=(
                        "source descriptor declares Hermitian partner; finite-basis apply unbound"
                    ),
                    numerical_apply_status="SOURCE_QUALIFIED_DESCRIPTOR_NO_K_LOCAL_SPARSE_APPLY",
                    numerical_apply_path=None,
                    derivative_status="C274_SYMBOLIC_INSERTION_ONLY",
                    state_current_dependency=str(meta["activation_relevance"]),
                    cross_resolution_status="K_LOCAL_INSERTION_COEFFICIENT_UNMAPPED",
                    smallest_missing_object=(
                        f"finite-basis apply implementation for {meta['operator_id']} at {resolution}"
                    ),
                )
            )

    plain_rows = tuple(asdict(row) for row in rows)
    executable = tuple(row for row in plain_rows if row["numerical_apply_path"] is not None)
    return deepcopy(
        {
            "schema": "C400-S2-C396-COORDINATE-BINDING-INVENTORY-V1",
            "resolutions": tuple(c396.RESOLUTIONS),
            "coordinates_per_resolution": 19,
            "total_rows": len(plain_rows),
            "resolution_semantics": deepcopy(_RESOLUTION_SEMANTICS),
            "basis_unit_conflict_unresolved": True,
            "class_counts_per_resolution": {
                "counterterm": len(c396.COUNTERTERMS),
                "source_null": len(c396.NULLS),
                "C117": len(c396.C117),
            },
            "rows": plain_rows,
            "complete_numerical_apply_paths": len(executable),
            "C396_19_coordinate_forward_map_ready": False,
            "C144_proxy_substitution_allowed": False,
            "rank_status": "RANK_NOT_EVALUATED",
            "physical_fit_authorized": False,
        }
    )


def binding_summary() -> Mapping[str, Any]:
    inventory = coordinate_binding_inventory()
    counts: dict[str, int] = {}
    for row in inventory["rows"]:
        counts[row["numerical_apply_status"]] = counts.get(row["numerical_apply_status"], 0) + 1
    return {
        "schema": "C400-S2-C396-BINDING-SUMMARY-V1",
        "status": "C396_19_COORDINATE_BINDING_INCOMPLETE",
        "total_rows": inventory["total_rows"],
        "complete_numerical_apply_paths": inventory["complete_numerical_apply_paths"],
        "status_counts": counts,
        "smallest_frontier": (
            "source-owned K-local operator apply paths for the matrix-valued C396 directions, "
            "plus approved nonmatrix treatment for vacuum/boundary/truncation directions"
        ),
        "physical_rank": None,
    }


__all__ = ["CoordinateBinding", "coordinate_binding_inventory", "binding_summary"]
