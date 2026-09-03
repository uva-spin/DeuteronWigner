#!/usr/bin/env python3
"""Materialize/verify C97's metadata-only C93 normal-form transport index."""
from __future__ import annotations
import argparse
from pathlib import Path

from deuteron_wigner.bridge.ifequivapi2 import load_verified_c93_public_authority
from deuteron_wigner.bridge.ifproofinput.normal_form_index import build_normal_form_key_index
from deuteron_wigner.bridge.ifproofinput.zran_runtime import build_persistent_zran_index, compile_adapter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/runtime/c93_ifc90payload/capsule/normal_forms.jsonl.gz"
TARGET = ROOT / "data/runtime/c97_ifproofinput/transport"

def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--span", type=int, default=1 << 20); args = parser.parse_args()
    TARGET.mkdir(parents=True, exist_ok=True)
    adapter = TARGET / "c97_zran"; compile_adapter(adapter)
    transport = build_persistent_zran_index(SOURCE, TARGET / "normal_forms.zran", adapter, span=args.span)
    authority = load_verified_c93_public_authority()
    index = build_normal_form_key_index(SOURCE, TARGET / "normal_forms.keyindex", transport, c93_root=authority["capsule_root"], c94_root=authority["package_root"])
    print(index["root"])

if __name__ == "__main__":
    main()
