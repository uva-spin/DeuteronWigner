"""Stable C11 negative-injection inventory."""
DESCRIPTIONS=tuple(f"C11 H4 required failure class {i:03d}" for i in range(1,105))
INJECTIONS=tuple((f"C11.INJECT.{i:03d}",d,"ORDERED_TYPED_FAIL_CLOSED") for i,d in enumerate(DESCRIPTIONS,1))
