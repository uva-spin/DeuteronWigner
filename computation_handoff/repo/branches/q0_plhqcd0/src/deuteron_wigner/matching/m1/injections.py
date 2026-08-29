GROUPS=(("SOURCE",62),("IDENTITY",62),("DISTRIBUTION",58),("PARAMETERS",62),("EXTERNAL",58),("STEP",56),("OPE_RANK",58),("SCHEME_EVOLUTION",56),("NUCLEAR",48),("LEAKAGE",40))
INJECTIONS=tuple((f"C20.INJECT.{g}.{i:03d}",f"ordered {g.lower()} fault {i}",f"C20.{g}.REJECT") for g,n in GROUPS for i in range(1,n+1))
