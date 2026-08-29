GROUPS=(("SCHEME",70),("BASIS",58),("MATCHING",66),("UV_SOFT",62),("SMALL_B",58),("EVOLUTION",66),("NUCLEAR",54),("LEAKAGE",46))
INJECTIONS=tuple((f"C19.INJECT.{g}.{i:03d}",f"ordered {g.lower()} fault {i}",f"C19.{g}.REJECT") for g,n in GROUPS for i in range(1,n+1))
