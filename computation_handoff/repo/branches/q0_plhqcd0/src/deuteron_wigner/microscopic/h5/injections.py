DESCRIPTIONS=tuple(f"C12 H5 required failure class {i:03d}" for i in range(1,125))
INJECTIONS=tuple((f"C12.INJECT.{i:03d}",d,"ORDERED_TYPED_FAIL_CLOSED") for i,d in enumerate(DESCRIPTIONS,1))
