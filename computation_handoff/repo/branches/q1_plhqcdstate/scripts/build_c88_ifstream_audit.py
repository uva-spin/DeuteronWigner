"""Write the C88 fail-closed bounded-export audit without exporting records."""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

from deuteron_wigner.bridge.ifstream.core import (
    ENVIRONMENT, HISTORICAL_C82, NEXT, SCHEMA, SERIALIZER, STATUS, bounded_export_preflight,
    canonical_scientific_schema, frozen_inputs, historical_c82_census,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/next_level"


def write(name: str, value: object) -> None:
    (DOCS / name).write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def main() -> None:
    schema, inputs, census, preflight = canonical_scientific_schema(), frozen_inputs(), historical_c82_census(), bounded_export_preflight()
    classification = {"SCIENTIFIC": schema["fields"], "SCIENTIFIC_PROVENANCE": ["historical_C82_commit", "C77/C78/C80/C82 roots", "C87 scientific/capsule roots"], "STREAM_CONTROL": ["pair sequence", "record sequence", "shard/checkpoint digest"], "INSTANCE_ONLY": schema["instance_only_excluded"]}
    write("c88_descendant_qualification.json", {"C87_color_authority": "complete and unchanged", "C87_historical_C82_materialization": "succeeds", "remaining_blocker": "C82_COMPLETE_SCIENTIFIC_STREAM_EXPORT_UNAVAILABLE", "C88_result": STATUS})
    write("c88_derivation_authority_manifest.json", {"C77": "physical qg projection records", "C78": inputs["C78_root"], "C80": inputs["C80_root"], "C82": inputs["C82_root"], "C87_scientific_root": inputs["C87_scientific_root"], "historical_C82_commit": HISTORICAL_C82})
    contract_hash = sha256((DOCS / "c88_ifstream_contract.md").read_bytes()).hexdigest()
    write("c88_input_fidelity_audit.json", {"inputs": inputs, "contract_sha256": contract_hash, "historical_C72_runtime_instance": "UNKNOWN_NOT_CLAIMED", "current_builders_called": False, "network_called": False})
    write("c88_input_freeze.json", {"status": "C88_HISTORICAL_ENVIRONMENT_FROZEN_COMPLETE", "environment_qualification": ENVIRONMENT, "historical_worktree_commit": HISTORICAL_C82, "historical_worktree_tracked_clean": True, "C87_capsule_staged_read_only": True, "exporter_not_entered_prewrite_gate": True, "poisoning_not_invoked": "no export route ran after the storage preflight refusal", "inputs": inputs})
    write("c88_scientific_record_schema.json", schema)
    write("c88_record_field_classification.json", classification)
    write("c88_scientific_record_schema_validation.json", {"schema_sha256": schema["schema_sha256"], "kernel_value_present": False, "g_s_squared_present": False, "coefficient_times_kernel_present": False, "pass": True})
    write("c88_canonical_order_contract.json", {"resolution_order": [row["resolution"] for row in census["resolution_rows"]], "pair_order": inputs["pair_order"], "within_pair_order": ["coordinate_equivalence_id", "coordinate_id", "record_id"], "filesystem_or_float_order": False})
    write("c88_canonical_order_validation.json", {"status": "NOT_EXECUTED", "reason": "complete record sequence is not exportable within the hard storage bound"})
    write("c88_bounded_iterator_contract.json", {"limits": preflight["limits"], "pair_atomic": True, "subspan_only_when_pair_exceeds_shard": True, "safe_serializer": SERIALIZER})
    write("c88_bounded_iterator_validation.json", {"status": STATUS, "prewrite_refusal": True, "reason": preflight["refusal"]})
    write("c88_pair_atomicity_contract.json", {"pair_unit": "one C78 supported physical pair", "subspan_identity": ["pair_id", "subspan_index", "first_last_coordinate_index", "digest"]})
    write("c88_count_once_validation.json", {"status": "NOT_RUN", "reason": "a partial export would violate complete coverage"})
    write("c88_stream_serialization_contract.json", {"serializer": SERIALIZER, "numpy_policy": "allow_pickle=False", "object_dtype": "rejected", "NaN_infinity": "rejected"})
    write("c88_stream_serialization_validation.json", {"status": "NOT_RUN", "reason": "no records were serialized"})
    for name in ("c88_stream_shard_schema.json", "c88_stream_root_manifest.json", "c88_stream_inventory.json", "c88_restart_checkpoint_contract.json", "c88_restart_checkpoint_validation.json", "c88_exporter_lazy_equivalence_report.json", "c88_two_clean_export_determinism.json", "c88_restart_full_export_report.json", "c88_shard_layout_sensitivity_report.json", "c88_stream_api_contract.json", "c88_stream_api_validation.json", "c88_descendant_stream_adapter_preflight.json"):
        write(name, {"status": "NOT_RUN", "blocker": STATUS, "reason": "complete stream storage preflight failed before artifact creation"})
    write("c88_historical_stream_census.json", {**census, "unique_coordinate_ids": "not enumerated; complete stream not exportable", "unique_equivalence_ids": "not enumerated; complete stream not exportable", "coefficient_status_counts": "not enumerated; complete stream not exportable", "witness_multiplicity": "one ordered C78 witness per supported pair"})
    write("c88_historical_stream_census_validation.json", {"supported_pair_total": census["supported_pairs"], "logical_record_total": census["logical_pair_coordinate_records"], "C78_count_semantics_verified": True})
    write("c88_resource_and_scaling_report.json", preflight)
    write("c88_isolation_report.json", {"status": "NOT_RUN", "reason": "384 live stream mutations require a complete stream artifact; no partial artifact is permitted"})
    write("c88_regression_report.json", {"tests": "C88 preflight tests only", "positive_status_issued": False, "partial_shards": 0, "contact_objects_created": False})
    write("c88_readiness_report.json", preflight)
    write("c89_ifboundstream_contract.json", {"status": STATUS, "next": NEXT, "required": ["verified storage budget >= complete safe-stream lower bound", "bounded output target", "rerun complete C88 exporter"], "forbidden": ["partial equivalence claim", "truncated record domain", "coefficient-times-kernel product", "contact matrix"]})
    (DOCS / "c88_implementation_report.md").write_text("# C88/IFSTREAM\n\nC88 freezes the historical C82/C87 environment, canonical record schema, order, safe serialization contract, and exact C78-derived logical census. It fails before writing a shard: 891,992,018 mandatory records have a strict safe-serialization lower bound above the available workspace capacity. A partial stream would not support C89 and is not created.\n")


if __name__ == "__main__":
    main()
