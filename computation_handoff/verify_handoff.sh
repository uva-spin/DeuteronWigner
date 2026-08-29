#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ZIP_NAME=DeuteronWigner_Computation_Handoff_2026-08-28.zip
EXPECTED_SHA256=9f807d32be336e5ce68fbfef5d5add9a2bc63675a70de6df55ba8c8fad80df9e
TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/deuteron-wigner-handoff.XXXXXX")
ASSEMBLED="$TMP_DIR/$ZIP_NAME"

cleanup() {
    rm -rf "$TMP_DIR"
}
trap cleanup EXIT HUP INT TERM

for suffix in aa ab ac ad ae af; do
    part="$SCRIPT_DIR/$ZIP_NAME.part-$suffix"
    if [ ! -f "$part" ]; then
        echo "missing handoff part: $part" >&2
        exit 1
    fi
done

cat "$SCRIPT_DIR/$ZIP_NAME.part-aa" \
    "$SCRIPT_DIR/$ZIP_NAME.part-ab" \
    "$SCRIPT_DIR/$ZIP_NAME.part-ac" \
    "$SCRIPT_DIR/$ZIP_NAME.part-ad" \
    "$SCRIPT_DIR/$ZIP_NAME.part-ae" \
    "$SCRIPT_DIR/$ZIP_NAME.part-af" > "$ASSEMBLED"

if command -v shasum >/dev/null 2>&1; then
    actual_sha256=$(shasum -a 256 "$ASSEMBLED" | awk '{print $1}')
elif command -v sha256sum >/dev/null 2>&1; then
    actual_sha256=$(sha256sum "$ASSEMBLED" | awk '{print $1}')
else
    echo "neither shasum nor sha256sum is available" >&2
    exit 1
fi

if [ "$actual_sha256" != "$EXPECTED_SHA256" ]; then
    echo "handoff checksum mismatch" >&2
    echo "expected: $EXPECTED_SHA256" >&2
    echo "actual:   $actual_sha256" >&2
    exit 1
fi

unzip -tq "$ASSEMBLED"
echo "verified $ZIP_NAME"
echo "sha256: $actual_sha256"
