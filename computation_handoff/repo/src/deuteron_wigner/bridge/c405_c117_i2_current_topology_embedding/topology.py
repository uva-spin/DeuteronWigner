"""C405 source-owner reconciliation for the first C117 I2 direction.

C114--C127 contain the source current, symbolic current factors, finite-member
programs, and aggregate ledgers.  Those records are valuable, but they do not
supply one internally consistent numerical map from an ordered current product
to a finite q/qg matrix element.  C405 therefore authenticates the historical
surfaces, records the exact agreements and conflicts, and exposes only the
identities common to all source-qualified records:

* four ordered current products;
* q->q and qg->qg diagonal sectors;
* exact q<->qg zero blocks from even-gluon-number parity;
* mixed-current adjoint reversal;
* two current identities in every ordered product.

No product-to-projector choice, normal-ordering branch, derivative leg,
normalization multiplicity, or coefficient is inferred by convenience.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Dict, Mapping, Sequence, Tuple

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.icho import core as c115
from deuteron_wigner.bridge.icreg2 import core as c117
from deuteron_wigner.bridge.icnorm3 import core as c119

STATUS = (
    "C405_C117_I2_CURRENT_ORDER_DERIVATIVE_FAMILY_AND_DIRECT_SUM_EMBEDDING_READY_"
    "PRODUCT_NORMAL_ORDERING_UNRESOLVED"
)
PRODUCTS: Tuple[str, ...] = ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g")
SECTORS: Tuple[str, ...] = ("q->q", "qg->qg")

ROOT = Path(__file__).resolve().parents[4]
_SOURCE_HASHES = {
    "C114": (
        "src/deuteron_wigner/bridge/icurrent/core.py",
        "a9a972db4cbf098f1e5342cefaee2692a1e2ad78ba9e11659ec1cc92ae815688",
    ),
    "C115": (
        "src/deuteron_wigner/bridge/icho/core.py",
        "b912ca76b840b0e3cc8bb4ba6a9d291e6c0e4230d2148505b9006885bceff7cb",
    ),
    "C117": (
        "src/deuteron_wigner/bridge/icreg2/core.py",
        "bd44d3cc3da0a3b864557bf5032ce9107de2e969cb0568afb4ea3987c4987fc0",
    ),
    "C119": (
        "src/deuteron_wigner/bridge/icnorm3/core.py",
        "e4f8ade1629caac07e09ad55b7122d06b14bc6d08e584e40bd9e5731865aa0b9",
    ),
    "C124": (
        "src/deuteron_wigner/bridge/icmembers/core.py",
        "e10176332daec337e26efd649fc6abda379763b5fb9cbb9d66992e90199535c1",
    ),
    "C125": (
        "src/deuteron_wigner/bridge/icdomain2/core.py",
        "8daab3d2ca2ba6f0d11f43967fcccc43c8030ca03f1f5142a515a7c98e4cbac8",
    ),
    "C126": (
        "src/deuteron_wigner/bridge/icsum3/core.py",
        "59d6daf4b229a6180ccc99933682ea9b62ad529d80705e5bddccdd3383d46557",
    ),
    "C127": (
        "src/deuteron_wigner/bridge/icagg3/core.py",
        "632aa0e8a3a8935fbfae41dc1793c8583c50098d0135345c78fb11fb3765768f",
    ),
    "C190": (
        "src/deuteron_wigner/bridge/hqcdb1qggsource2/core.py",
        "f88e1a11a9a7de7e9d801ea779e8707da3ba8be8df471508bd5307b3fa2c757c",
    ),
    "C192": (
        "src/deuteron_wigner/bridge/hqcdb1qgggcurr1/core.py",
        "4f68826835715f5ef08a3e5e1f6a594610f9e0a99319701f6d35a89696cfbe73",
    ),
    "C193": (
        "src/deuteron_wigner/bridge/hqcdb1qggcontact2/core.py",
        "9e00983334136695bebb6748388eba0576362bc55036fca5f5063c4447b2a2a4",
    ),
    "C249": (
        "src/deuteron_wigner/bridge/hqcdriquarkfixedkv2currentmap1/core.py",
        "b12a509ae0bdb261c243eec2e368891e9a76281270d7cf051a38635a058c729e",
    ),
    "C250": (
        "src/deuteron_wigner/bridge/hqcdriquarkfixedkv2currenteval1/core.py",
        "eb91ec69939d48029d4258366d888eaa6ea1b532ba7e0e95e7f6166c2f24fdc0",
    ),
}

# C125's historical product-to-member-graph rule.  It is deliberately kept
# separate from C115 because the two records disagree for three products.
_C125_GRAPH = {
    "J_qJ_q": "I2_density_projector",
    "J_qJ_g": "I2_density_projector",
    "J_gJ_q": "derivative_density",
    "J_gJ_g": "derivative_density",
}


@dataclass(frozen=True)
class ProductStructure:
    product: str
    currents: Tuple[str, str]
    gluon_current_count: int
    adjoint_product: str

    def to_record(self) -> Dict[str, Any]:
        return {
            "product": self.product,
            "currents": self.currents,
            "gluon_current_count": self.gluon_current_count,
            "adjoint_product": self.adjoint_product,
        }


def source_file_hashes() -> Mapping[str, Any]:
    rows = []
    for owner, (relative, expected) in _SOURCE_HASHES.items():
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        actual = sha256(path.read_bytes()).hexdigest()
        rows.append(
            {
                "owner": owner,
                "path": relative,
                "expected_sha256": expected,
                "actual_sha256": actual,
                "pass": actual == expected,
            }
        )
    payload = {
        "schema": "C405-SOURCE-FILE-HASH-AUDIT-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "all_match": all(row["pass"] for row in rows),
    }
    if not payload["all_match"]:
        mismatches = tuple(row["owner"] for row in rows if not row["pass"])
        raise ValueError("frozen source surface changed: " + ", ".join(mismatches))
    return {**payload, "root": content_root(payload)}


def product_structure(product: str) -> ProductStructure:
    if product not in PRODUCTS:
        raise KeyError(product)
    encoded = product.removeprefix("J_")
    left, right = encoded.split("J_")
    currents = (
        "quark_current" if left == "q" else "gluon_current",
        "quark_current" if right == "q" else "gluon_current",
    )
    partner = {
        "J_qJ_g": "J_gJ_q",
        "J_gJ_q": "J_qJ_g",
    }.get(product, product)
    return ProductStructure(
        product=product,
        currents=currents,
        gluon_current_count=sum(current == "gluon_current" for current in currents),
        adjoint_product=partner,
    )


def _source_contains(owner: str, snippets: Sequence[str]) -> bool:
    relative, _expected = _SOURCE_HASHES[owner]
    text = (ROOT / relative).read_text(encoding="utf-8")
    return all(snippet in text for snippet in snippets)


def _c115_graph(product: str) -> str:
    records = c115.diagonal_component_manifest()
    rows = [row for row in records if row["product"] == product]
    if len(rows) != len(SECTORS):
        raise ValueError("C115 component census changed")
    classes = {str(row["ho_class"]) for row in rows}
    if len(classes) != 1:
        raise ValueError("C115 graph class unexpectedly sector dependent")
    return classes.pop()


def _c117_class_program_status(product: str, class_id: str) -> bool:
    program_ids = {f"{product}:{sector}" for sector in SECTORS}
    graph = next(row for row in c117.graph_manifest()["graphs"] if row["class_id"] == class_id)
    return program_ids.issubset(set(graph["programs"]))


def _c119_program_leaf_audit(product: str) -> Tuple[Mapping[str, Any], ...]:
    required = product_structure(product).currents
    rows = []
    inventory = tuple(c119.current_factor_leaf_inventory())
    for sector in SECTORS:
        program_id = f"{product}:{sector}"
        factors = tuple(
            str(row["factor_id"])
            for row in inventory
            if row["program_id"] == program_id
        )
        actual_current_factors = tuple(
            factor for factor in factors if factor in ("quark_current", "gluon_current")
        )
        missing = list(required)
        for factor in actual_current_factors:
            if factor in missing:
                missing.remove(factor)
        duplicate_derivative = (
            "gluon_current" in actual_current_factors
            and "derivative_or_helicity" in factors
            and "pi*k_c/L" in str(c119.factor_value("gluon_current", c119.ROUTES[0])["expression"])
        )
        rows.append(
            {
                "program_id": program_id,
                "required_current_factors": required,
                "historical_leaf_factors": factors,
                "historical_current_factors": actual_current_factors,
                "missing_current_factors": tuple(missing),
                "required_current_factor_count": 2,
                "historical_current_factor_count": len(actual_current_factors),
                "current_pair_complete": actual_current_factors == required,
                "derivative_factor_potentially_duplicated": duplicate_derivative,
            }
        )
    return tuple(rows)


def gluon_source_slot_authority() -> Mapping[str, Any]:
    """Return the strongest source-qualified gluon-current ordering statement.

    C192 resolves the ordered source field slots and places ``partial_-`` on
    the second source field.  It also keeps the two mixed current owners
    separate and forbids a factor-two merge.  What it does *not* resolve is
    the product-specific normal-ordering map from that second source field to
    an external qg BRA or KET gluon.  C405 therefore narrows, but does not
    remove, the derivative-leg ambiguity.
    """
    checks = {
        "C190_gauss_current_was_incomplete": _source_contains(
            "C190",
            (
                '"status":"GAUSS_CURRENT_INCOMPLETE"',
                '"C127":"INCOMPLETE"',
            ),
        ),
        "C192_source_current_expression_bound": _source_contains(
            "C192",
            (
                '"current_expression":"- f_abc A_perp^b partial_- A_perp^c"',
                '"ordered_field_slots":("A_perp^b first","A_perp^c second")',
            ),
        ),
        "C192_derivative_source_slot_is_second": _source_contains(
            "C192",
            (
                '"derivative_placement":"partial_- acts on second slot"',
                '"derivative":"second-slot momentum factor"',
            ),
        ),
        "C192_mixed_orders_separate_no_factor_two": _source_contains(
            "C192",
            (
                '"mixed_owner_factor":"each J_q K J_g and J_g K J_q retains source -g^2/2; no factor two merge"',
            ),
        ),
        "C192_integration_by_parts_boundary_retained": _source_contains(
            "C192",
            (
                '"boundary_defect":"C130 finite-cell boundary/nonmatrix remainder retained"',
                '"field_slot_order":"not swapped"',
            ),
        ),
        "C193_mixed_orders_still_separate": _source_contains(
            "C193",
            (
                '"C127_mixed_orders_separate":True,"factor_two_assumed":False',
            ),
        ),
    }
    if not all(checks.values()):
        failed = tuple(key for key, value in checks.items() if not value)
        raise ValueError("gluon source-slot authority changed: " + ", ".join(failed))
    payload = {
        "schema": "C405-C117-I2-GLUON-SOURCE-SLOT-AUTHORITY-V1",
        "status": STATUS,
        "source_current_expression": "- f_abc A_perp^b partial_- A_perp^c",
        "ordered_source_field_slots": ("A_perp^b", "A_perp^c"),
        "derivative_source_field_slot": 2,
        "derivative_source_color_slot": "c",
        "number_preserving_branch_source_derivative": "second-slot momentum factor",
        "integration_by_parts_alternate_slot": 1,
        "integration_by_parts_boundary_owner": "C130/C182 retained; not discarded",
        "mixed_current_owner_orders": ("J_q K J_g", "J_g K J_q"),
        "mixed_current_orders_kept_separate": True,
        "factor_two_merge_forbidden": True,
        "external_BRA_KET_leg_mapping": "MISSING_NOT_ZERO",
        "normal_ordering_descendant_bound": False,
        "complete_numerical_gluon_current_matrix": False,
        "classification": (
            "SOURCE_FIELD_SLOT_ORDER_CLOSED_EXTERNAL_LEG_NORMAL_ORDER_MAPPING_UNRESOLVED"
        ),
        "source_checks": checks,
    }
    return {**payload, "root": content_root(payload)}


def topology_authority_audit() -> Mapping[str, Any]:
    source_hashes = source_file_hashes()
    source_slot = gluon_source_slot_authority()
    # Authenticate the historical mappings without importing C125/C126/C249/
    # C250, whose import chains require unrelated runtime artifacts.
    static_checks = {
        "C124_graph_dependent_member_weight": _source_contains(
            "C124",
            (
                "return f\"pi*{mode['k']}/L\" if c[\"graph\"] == \"derivative_density\" else \"1\"",
            ),
        ),
        "C125_graph_mapping": _source_contains(
            "C125",
            (
                'return "I2_density_projector" if product in ("J_qJ_q", "J_qJ_g") else "derivative_density"',
            ),
        ),
        "C125_count_once_identity": _source_contains(
            "C125",
            (
                '"count_once_id": "C125:one-member-one-target"',
                '"target_assignment": "exactly one target span per witness"',
            ),
        ),
        "C126_single_current_reference": _source_contains(
            "C126",
            (
                'current = "gluon_current" if product.startswith("J_g") else "quark_current"',
                '"C119:" + current',
            ),
        ),
        "C119_gluon_current_contains_ordered_derivative": _source_contains(
            "C119",
            (
                'elif factor_id=="gluon_current": expr="-f^(abc) * delta_polarization * (pi*k_c/L) * (2L)^(-1)"',
            ),
        ),
        "C119_gluon_leaf_repeats_derivative_factor": _source_contains(
            "C119",
            (
                'if species=="gluon": leaves += ("derivative_or_helicity",)',
            ),
        ),
        "C126_extra_gluon_derivative_reference": _source_contains(
            "C126",
            (
                'if product.startswith("J_g"): factors += ("C115:derivative_or_helicity",)',
            ),
        ),
        "C249_single_current_reference": _source_contains(
            "C249",
            (
                'current="gluon_current" if product.startswith("J_g") else "quark_current"',
            ),
        ),
        "C250_two_current_reference": _source_contains(
            "C250",
            (
                "left,right=_current_ids(x.product)",
                "currents=(c119.factor_value(left,route),c119.factor_value(right,route))",
            ),
        ),
        "C250_does_not_add_separate_derivative_factor": not _source_contains(
            "C250",
            ("derivative_or_helicity",),
        ),
        "C127_no_numerical_entries": _source_contains(
            "C127",
            (
                '"sparse_operator_entries": 0',
                '"matrix_free_actions": 0',
            ),
        ),
        "C190_gauss_current_split_incomplete_before_C192": _source_contains(
            "C190",
            (
                '"status":"GAUSS_CURRENT_INCOMPLETE"',
                '"C127":"INCOMPLETE"',
            ),
        ),
        "C192_ordered_gluon_source_slot_closed": _source_contains(
            "C192",
            (
                '"derivative_placement":"partial_- acts on second slot"',
                '"mixed_owner_factor":"each J_q K J_g and J_g K J_q retains source -g^2/2; no factor two merge"',
            ),
        ),
        "C193_no_finite_HO_numeric": _source_contains(
            "C193",
            (
                '"finite_HO_numeric_evaluations":0',
                '"contact_matrices":0',
            ),
        ),
    }
    if not all(static_checks.values()):
        raise ValueError("one or more frozen topology source checks failed")

    rows = []
    graph_conflicts = 0
    incomplete_c119_programs = 0
    derivative_overlap_programs = 0
    c126_extra_derivative_products = 0
    c126_extra_derivative_programs = 0
    for product in PRODUCTS:
        structure = product_structure(product)
        c115_graph = _c115_graph(product)
        c125_graph = _C125_GRAPH[product]
        graph_agreement = c115_graph == c125_graph
        if not graph_agreement:
            graph_conflicts += 1
        leaf_rows = _c119_program_leaf_audit(product)
        incomplete_c119_programs += sum(not row["current_pair_complete"] for row in leaf_rows)
        derivative_overlap_programs += sum(
            row["derivative_factor_potentially_duplicated"] for row in leaf_rows
        )
        if product.startswith("J_g"):
            c126_extra_derivative_products += 1
            c126_extra_derivative_programs += len(SECTORS)
        rows.append(
            {
                "product": product,
                "currents": structure.currents,
                "adjoint_product": structure.adjoint_product,
                "gluon_current_count": structure.gluon_current_count,
                "C115_HO_class": c115_graph,
                "C125_member_graph": c125_graph,
                "C115_C125_graph_agreement": graph_agreement,
                "C117_I2_lists_product": _c117_class_program_status(
                    product, "I2_density_projector"
                ),
                "C117_derivative_lists_product": _c117_class_program_status(
                    product, "derivative_density"
                ),
                "C119_program_leaf_audit": leaf_rows,
                "C126_current_factor_reference_count": 1,
                "C126_adds_separate_derivative_factor": product.startswith("J_g"),
                "C126_derivative_double_count_risk": product.startswith("J_g"),
                "C250_current_factor_reference_count": 2,
                "C250_adds_separate_derivative_factor": False,
                "C250_current_ids": structure.currents,
                "ordered_gluon_derivative_leg_required": structure.gluon_current_count > 0,
                "C192_derivative_source_field_slot": (
                    2 if structure.gluon_current_count > 0 else None
                ),
                "C192_source_field_slot_bound": structure.gluon_current_count > 0,
                "ordered_gluon_external_BRA_KET_leg_bound": False,
                "ordered_gluon_derivative_leg_bound": False,
                "C125_witness_count_once_identity_bound": True,
                "C125_target_assignment_bound": True,
                "C405_conditional_kernel_to_C125_witness_map_bound": False,
                "normal_ordering_descendant_bound": False,
                "source_qualified_product_topology_bound": False,
                "classification": (
                    "GRAPH_CLASS_AGREES_BUT_NORMAL_ORDERING_AND_DERIVATIVE_LEG_UNBOUND"
                    if graph_agreement
                    else "HISTORICAL_GRAPH_CLASS_CONFLICT_REQUIRES_SOURCE_DESCENDANT_BINDING"
                ),
            }
        )

    payload = {
        "schema": "C405-C117-I2-TOPOLOGY-AUTHORITY-AUDIT-V2",
        "status": STATUS,
        "products": tuple(rows),
        "product_count": len(rows),
        "sector_count": len(SECTORS),
        "program_count": len(rows) * len(SECTORS),
        "graph_mapping_conflicts": graph_conflicts,
        "C119_incomplete_current_pair_programs": incomplete_c119_programs,
        "C119_leaf_programs_with_derivative_overlap_risk": derivative_overlap_programs,
        "C119_or_C126_derivative_overlap_programs": derivative_overlap_programs,
        "C126_products_with_extra_derivative_reference": c126_extra_derivative_products,
        "C126_programs_with_extra_derivative_reference": c126_extra_derivative_programs,
        "single_current_reference_defects": len(PRODUCTS),
        "C126_product_level_single_current_reference_defects": len(PRODUCTS),
        "C126_program_level_single_current_reference_defects": len(PRODUCTS) * len(SECTORS),
        "C249_product_level_single_current_reference_defects": len(PRODUCTS),
        "C250_two_current_reference_repairs_pair_identity": True,
        "C192_source_gluon_derivative_field_slot_bound": True,
        "C192_external_BRA_KET_leg_mapping_bound": False,
        "C192_mixed_current_orders_kept_separate": True,
        "C192_factor_two_merge_forbidden": True,
        "historical_derivative_assignment_is_not_authoritative": True,
        "source_field_slot_order_is_authoritative": True,
        "external_leg_normal_order_mapping_is_not_authoritative": True,
        "C125_witness_count_once_identity_bound": True,
        "C405_conditional_kernel_to_C125_witness_map_bound": False,
        "count_once_status": (
            "WITNESS_COUNT_ONCE_IDENTITY_SOURCE_BOUND_NUMERICAL_TARGET_AGGREGATION_UNBOUND"
        ),
        "common_closed_identities": (
            "four ordered current products",
            "q->q and qg->qg diagonal sectors",
            "q<->qg cross-sector blocks exact zero by even-gluon parity",
            "J_qJ_g and J_gJ_q are source-order adjoints",
            "both left and right current identities are required",
            "C192 fixes the gluon-current derivative on the second ordered source field",
            "C192/C193 keep J_q K J_g and J_g K J_q separate with no factor-two merge",
        ),
        "C190_classification": "GAUSS_CURRENT_SPLIT_INCOMPLETE_SUPERSEDED_BY_C192",
        "C192_classification": (
            "ORDERED_GLUON_SOURCE_AST_CLOSED_FINITE_HO_EXTERNAL_LEG_MAPPING_UNRESOLVED"
        ),
        "C127_classification": (
            "SYMBOLIC_TARGET_PROGRAM_COMPLETE_NUMERICAL_OPERATOR_ENTRIES_ZERO"
        ),
        "C193_classification": (
            "SYMBOLIC_NONPHYSICAL_CONTACT_AUTHORITY_FINITE_HO_NUMERICS_ZERO"
        ),
        "source_qualified_product_topology_rows": 0,
        "complete_C117_action": False,
        "smallest_missing_object": (
            "source-qualified normal-ordering descendant table assigning, for every ordered product and sector, "
            "the graph class, contracted member species, map from each C192 source-ordered derivative field to an "
            "external BRA/KET gluon leg, finite-cell/state normalization ownership and multiplicities, source phase, "
            "q/qg target block, and count-once multiplicity"
        ),
        "source_hash_audit": source_hashes,
        "gluon_source_slot_authority": source_slot,
        "static_source_checks": static_checks,
    }
    return {**payload, "root": content_root(payload)}


def current_pair_grammar() -> Mapping[str, Any]:
    rows = []
    for product in PRODUCTS:
        structure = product_structure(product)
        source_factors = tuple(
            c119.factor_value(current, "RouteA_source_field_insertion")["expression"]
            for current in structure.currents
        )
        rows.append(
            {
                **structure.to_record(),
                "left_current_expression": source_factors[0],
                "right_current_expression": source_factors[1],
                "source_order": "C114_LEFT_CURRENT_Q0_INV_DPLUS2_RIGHT_CURRENT",
                "adjoint_rule": (
                    "complex conjugation, bra/ket reversal, current-order reversal"
                ),
                "current_pair_identity_complete": True,
                "normal_ordered_matrix_element_complete": False,
                "historical_C119_leaf_program_reused_as_complete_pair": False,
            }
        )
    payload = {
        "schema": "C405-C117-I2-CURRENT-PAIR-GRAMMAR-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "all_products_have_two_current_ids": all(len(row["currents"]) == 2 for row in rows),
        "mixed_adjoint_pair": ("J_qJ_g", "J_gJ_q"),
        "posthoc_symmetrization": False,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "STATUS",
    "PRODUCTS",
    "SECTORS",
    "ProductStructure",
    "source_file_hashes",
    "product_structure",
    "gluon_source_slot_authority",
    "topology_authority_audit",
    "current_pair_grammar",
]
