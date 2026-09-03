GROUPS=(("CONTINUUM",44),("TRANSITION",34),("CURRENT",52),("CONTINUITY",34),("SEPARATOR",38),("COHERENT_CP",38),("TTN",32),("DOWNSTREAM",36),("BASELINE",32))
INJECTIONS=tuple((f"C17.INJECT.{g}.{i:03d}",f"ordered {g.lower()} mutation {i}",f"C17.{g}.BOUNDARY") for g,n in GROUPS for i in range(1,n+1))
