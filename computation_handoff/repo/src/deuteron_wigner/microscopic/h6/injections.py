DESCRIPTIONS=tuple(f"C13 H6 required failure class {i:03d}" for i in range(1,149))
INJECTIONS=tuple((f"C13.INJECT.{i:03d}",d,"ORDERED_TYPED_FAIL_CLOSED") for i,d in enumerate(DESCRIPTIONS,1))
