"""C93-owned serializer adapter for one exact C90 compiler route."""
from __future__ import annotations

import argparse
import gzip
from hashlib import sha256
import json
from pathlib import Path


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--route", choices=("A", "B"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    # PYTHONPATH is set by the caller to the exact detached C90 source tree.
    from deuteron_wigner.bridge.ifboundrestart.core import RESOLUTION_ORDER, check_proof, compile_route_a, compile_route_b
    compiler = compile_route_a if args.route == "A" else compile_route_b
    args.output.parent.mkdir(parents=True, exist_ok=True)
    digest = sha256(); count = 0
    with args.output.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as output:
            for resolution in RESOLUTION_ORDER:
                for program in compiler(resolution):
                    record = {"pair": program["pair"], "normal_form_root": program["normal_form_root"], "normal_form": program,
                              "proof": check_proof(program), "route": args.route}
                    line = canonical(record).encode() + b"\n"
                    output.write(line); digest.update(line); count += 1
    print(json.dumps({"route": args.route, "records": count, "logical_sha256": digest.hexdigest(), "file_sha256": sha256(args.output.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
