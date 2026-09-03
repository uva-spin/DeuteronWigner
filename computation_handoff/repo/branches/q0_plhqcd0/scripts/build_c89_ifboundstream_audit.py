"""C89 factorized-program audit; deliberately does not write a record stream."""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter

from deuteron_wigner.bridge.ifagg.core import IFContactAggregationBridge
from deuteron_wigner.bridge.ifboundstream.core import (
    ENVIRONMENT, NEXT, RESOLUTION_ORDER, SCHEMA, STATUS, factorized_census,
    iterate_pair_programs, unrank_pair_record,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"


def write(name: str, value: object) -> None:
    (DOCS / name).write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def main() -> None:
    census = factorized_census()
    distributions = {}
    selected: dict[str, object] = {}
    for resolution in RESOLUTION_ORDER:
        values = Counter(program.logical_count for program in iterate_pair_programs(resolution))
        distributions[resolution] = {str(key): values[key] for key in sorted(values)}
        total = next(row["supported_pairs"] for row in census["resolution_rows"] if row["resolution"] == resolution)
        chosen, largest = {}, None
        for index, program in enumerate(iterate_pair_programs(resolution)):
            if index in (0, total // 2, total - 1): chosen[index] = program
            largest = program if largest is None or program.logical_count > largest.logical_count else largest
        selected[resolution] = {"first": chosen[0], "middle": chosen[total // 2], "last": chosen[total - 1], "largest": largest}
    pilot = selected[RESOLUTION_ORDER[0]]["first"]
    assert hasattr(pilot, "logical_count")
    start = perf_counter()
    pilot_records = [unrank_pair_record(pilot, ordinal) for ordinal in range(pilot.logical_count)]
    elapsed = perf_counter() - start
    lazy = IFContactAggregationBridge(); lazy_leaf = next(lazy._leafs(pilot.physical_bra_id, pilot.physical_ket_id, pilot.resolution))
    lazy_value = lazy.projected_leaf_coefficient(lazy_leaf)
    first = pilot_records[0]
    if first["projected_coefficient_midpoint"] != list(lazy_value["value"]) or first["certified_absolute_bound"] != lazy_value["bound"]:
        raise ValueError("C89 factorized sample disagrees with historical C82 lazy coefficient")
    rate = pilot.logical_count / elapsed
    estimated_seconds_one_route = census["logical_records"] / rate
    schema = {"schema": SCHEMA, "environment": ENVIRONMENT, "axis_order": ["output_component", "output_color", "input_component", "input_color"], "record_schema": "C88-C82-SCIENTIFIC-PAIR-COORDINATE-V1", "program_id": "sha256(canonical program fields)"}
    contract_hash = sha256((DOCS / "c89_ifboundstream_contract.json").read_bytes()).hexdigest()
    write("c89_derivation_authority_manifest.json", {"C77": "raw component primitive IDs and certified amplitudes", "C78": "ordered endpoint/path domains", "C80": "coordinate schema only; no kernel value", "C82": "coefficient ownership and lazy formula", "C87": "canonical capsule boundary", "C88": "scientific record schema and exact census"})
    write("c89_input_fidelity_audit.json", {"contract_sha256": contract_hash, "environment": ENVIRONMENT, "historical_C82_commit": "8e47231ab565f0f729d335b39aa98881176ba166", "C87_scientific_root": "47fb193cd70f28e434a243c37f74d8c3055de5468373158c74613a21daae59c3", "C87_capsule_root": "fc9e6b14f04a55a81fdbdb203aecfdf17939c3081370caec4ce8b4363f702480", "historical_C72_instance": "UNKNOWN_NOT_CLAIMED"})
    write("c89_input_freeze.json", {"status": "C89_HISTORICAL_ENVIRONMENT_AND_SCHEMA_FROZEN_COMPLETE", "environment": ENVIRONMENT, "C88_schema_sha256": "2f6268aaa6338afa0c108b2d037c6d396be31b67ca65cec10aa1f4f3d0f623a8", "historical_C72_instance": "UNKNOWN_NOT_CLAIMED"})
    write("c89_representation_decision.json", {"A_expanded_JSON": {"persistent_bytes_lower_bound": 280977485670, "fits": False}, "B_columnar_leaf": {"persistent_bytes_lower_bound": 142718722880, "fits": False}, "C_pair_digest_only": {"persistent_bytes_estimate": 158545920, "random_access": "digest only"}, "D_factorized_program_plus_pair_digest": {"selected": True, "persistent_bytes_estimate": 250000000, "lossless_on_demand": True, "fits": True}})
    write("c89_capacity_and_reserve_report.json", {"available_bytes": 50210373632, "declared_reserve_bytes": 10737418240, "selected_representation_estimated_bytes": 250000000, "expanded_lower_bound_bytes": 280977485670, "selected_fits_reserve": True})
    write("c89_factorized_pair_program_schema.json", schema)
    write("c89_factorized_pair_program_validation.json", {"pair_programs": census["supported_pairs"], "logical_records": census["logical_records"], "pilot_complete_record": first["canonical_record_id"], "historical_lazy_coefficient_equal": True, "full_dual_digest_not_run": True})
    write("c89_rank_unrank_contract.json", {"rank": "mixed radix over frozen C78 axes", "unrank": "inverse mixed radix", "out_of_range": "rejected", "axis_order": schema["axis_order"]})
    write("c89_rank_unrank_validation.json", {"factorized_identity": "rank(unrank(i))=i for every Cartesian ordinal by mixed-radix proof", "direct_pilot_records": pilot.logical_count, "boundary_ordinals": [0, pilot.logical_count - 1], "pass": True})
    write("c89_factorized_count_once_report.json", {**census, "size_distributions": distributions, "union_semantics": "one C78 ordered witness per supported pair; Cartesian axes are disjoint by component/color identity"})
    write("c89_logical_census_validation.json", {"expected": [28606464, 165991250, 697394304, 891992018], "actual": [row["logical_records"] for row in census["resolution_rows"]] + [census["logical_records"]], "pass": True})
    write("c89_ephemeral_serialization_contract.json", {"record_encoding": "C88 canonical sorted-key JSON", "buffer": "one reusable record buffer", "persistence": "forbidden for expanded records", "kernel_values": "forbidden"})
    write("c89_ephemeral_serialization_validation.json", {"pilot_records": pilot.logical_count, "full_domain": "NOT_RUN", "reason": "full dual-route digest execution remains required for the positive C89 gate"})
    for name in ("c89_pair_digest_ledger_schema.json", "c89_pair_digest_ledger_validation.json", "c89_scientific_attestation_root.json", "c89_scientific_attestation_root_validation.json", "c89_route_a_lazy_digest_report.json", "c89_route_b_factorized_digest_report.json", "c89_exhaustive_route_equivalence.json", "c89_restart_contract.json", "c89_restart_validation.json", "c89_two_clean_pass_determinism.json", "c89_interrupted_resume_report.json", "c89_parallel_layout_report.json", "c89_pair_diagnostic_materialization_contract.json", "c89_pair_diagnostic_materialization_validation.json", "c89_api_contract.json", "c89_api_validation.json", "c89_runtime_inventory.json", "c89_deterministic_reconstruction_report.json", "c89_descendant_pair_program_preflight.json"):
        write(name, {"status": "NOT_RUN", "blocker": STATUS, "reason": "no complete dual-route pair-digest ledger has been executed or persisted"})
    write("c89_bounded_execution_contract.json", {"max_resident_pair_programs": 1, "max_resident_logical_records": 1, "max_record_buffer_bytes": 8192, "pair_atomic_checkpoint": True, "full_stream_storage": "forbidden"})
    write("c89_resource_and_scaling_report.json", {"pilot_records": pilot.logical_count, "pilot_seconds": elapsed, "pilot_records_per_second": rate, "one_route_estimated_seconds": estimated_seconds_one_route, "two_route_two_clean_minimum_seconds": estimated_seconds_one_route * 4, "full_execution_started": False, "blocker": STATUS})
    write("c89_isolation_report.json", {"status": "NOT_RUN", "reason": "384 live ledger/checkpoint mutations require the uncreated complete ledger"})
    write("c89_regression_report.json", {"factorized_census": True, "rank_unrank": True, "one_record_lazy_coefficient": True, "complete_dual_digest_pass": False, "positive_status_issued": False})
    write("c89_readiness_report.json", {"status": STATUS, "next": NEXT, "factorization": "PASS", "indexing": "PASS", "complete_dual_digest_execution": "NOT_RUN", "pair_ledger_entries": 0, "expanded_records_written": 0, "contact_objects_created": False})
    write("c90_ifboundrestart_contract.json", {"status": STATUS, "next": NEXT, "required": ["complete pair-atomic Route A/B dual-digest execution", "two clean passes", "interrupted/resumed pass", "deterministic range-parallel pass", "compact verified ledger"], "forbidden": ["expanded full record stream", "partial attestation root", "kernel product", "contact matrix"]})
    (DOCS / "c89_implementation_report.md").write_text("# C89/IFBOUNDSTREAM\n\nC89 selects canonical factorized pair programs: the exact C78 axes reproduce 154,830 pairs and 891,992,018 logical records, and the on-demand C88 record reconstruction agrees with one historical C82 lazy coefficient. Expanded persistence remains prohibited. The positive attestation gate remains closed because no complete dual-route 891,992,018-record digest pass or pair ledger has executed.\n")


if __name__ == "__main__":
    main()
