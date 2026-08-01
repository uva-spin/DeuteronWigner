GROUPS=(("SOURCE",84),("KERNEL",96),("EVOLUTION",96),("COLLINEAR",76),("NUCLEAR",78),("UNCERTAINTY",86),("LEAKAGE",64),("THRESHOLD",60))
INJECTIONS=tuple((f"C21.INJECT.{g}.{i:03d}",f"ordered {g.lower()} fault {i}",f"C21.{g}.REJECT") for g,n in GROUPS for i in range(1,n+1))
