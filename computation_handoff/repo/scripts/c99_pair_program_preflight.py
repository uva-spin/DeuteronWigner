#!/usr/bin/env python3
"""C99 pair-program preflight with strict descendant-before-historical order.

This is deliberately a bounded, resolution-local diagnostic.  It compiles
the current program, verifies it against a separately frozen descendant
ledger, and only then obtains the corresponding historical program through
the C98 public normal-form method.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import resource
import time

from deuteron_wigner.bridge.ifequiv6.core import compile_descendant_programs, sha


def plain(value):
    if hasattr(value, "items"):
        return {key: plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(item) for item in value]
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--freeze", type=Path, required=True)
    parser.add_argument("--resolution", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((args.freeze / "manifest.json").read_text())
    drop = set(manifest["drop_instance_keys"])

    # This delayed import is the executable historical-access barrier.
    from deuteron_wigner.bridge.ifhistpublic2 import historical_pair_normal_form

    def normalize(program):
        program = json.loads(json.dumps(program))
        program["primitive_roots"] = {
            key: value for key, value in program["primitive_roots"].items()
            if key not in drop
        }
        program["normal_form_root"] = sha({
            key: value for key, value in program.items()
            if key != "normal_form_root"
        })
        return program

    start = time.monotonic()
    mismatch = {key: 0 for key in (
        "frozen_root", "pair_identity", "pair_order", "normal_form_root",
        "normal_form_content", "logical_count",
    )}
    rolling = ""
    logical = 0
    # Stream the frozen ledger: retaining 43,350/95,256 decoded Python
    # records is intentionally forbidden by the C99 bounded-memory policy.
    frozen_count = 0
    with (args.freeze / "descendant.jsonl").open() as stream:
        selected = (json.loads(raw) for raw in stream)
        selected = (entry for entry in selected if entry["pair"]["resolution"] == args.resolution)
        for local, program in enumerate(compile_descendant_programs(args.resolution)):
            try:
                frozen_entry = next(selected)
            except StopIteration as exc:
                raise RuntimeError("frozen descendant ledger is missing a pair") from exc
            normalized = normalize(program)
            mismatch["frozen_root"] += int(
                frozen_entry["raw_program_root"] != program["normal_form_root"]
                or frozen_entry["normalized_program_root"] != normalized["normal_form_root"]
            )
            historical = plain(historical_pair_normal_form(program["pair"]["id"], args.resolution))
            node = historical["normal_form"]
            mismatch["pair_identity"] += int(node["pair"] != program["pair"])
            mismatch["pair_order"] += int(
                historical["resolution_sequence"] != local
                or historical["global_sequence"] != frozen_entry["global_sequence"]
            )
            mismatch["normal_form_root"] += int(node["normal_form_root"] != normalized["normal_form_root"])
            mismatch["normal_form_content"] += int(canonical(node) != canonical(normalized))
            mismatch["logical_count"] += int(node["cardinality"] != frozen_entry["cardinality"])
            rolling = sha({"previous": rolling, "pair": program["pair"]["id"],
                           "historical": node["normal_form_root"],
                           "descendant": normalized["normal_form_root"]})
            logical += program["cardinality"]; frozen_count += 1
        try:
            next(selected)
            raise RuntimeError("frozen descendant ledger has an extra pair")
        except StopIteration:
            pass

    body = {
        "schema": "C99-PAIR-PROGRAM-PUBLIC-CROSSWALK-PREFLIGHT-V1",
        "descendant_freeze_root": manifest["root"],
        "resolution": args.resolution,
        "pairs": frozen_count,
        "logical_records": logical,
        "mismatches": mismatch,
        "rolling_root": rolling,
        "elapsed_seconds": time.monotonic() - start,
        "peak_rss": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    body["root"] = sha(body)
    args.output.write_text(canonical(body) + "\n")
    if any(mismatch.values()):
        raise SystemExit("C99 pair-program mismatch")


if __name__ == "__main__":
    main()
