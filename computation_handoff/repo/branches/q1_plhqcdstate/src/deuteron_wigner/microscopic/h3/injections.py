DESCRIPTIONS=tuple(f"C10 required failure class {i:03d}" for i in range(1,91))
INJECTIONS=tuple((f"C10.INJECT.{i:03d}",d,"ORDERED_STRUCTURED_FAIL_CLOSED") for i,d in enumerate(DESCRIPTIONS,1))
