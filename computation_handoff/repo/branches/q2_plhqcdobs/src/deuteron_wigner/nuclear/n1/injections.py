GROUPS=(("BASELINE",20),("COORDINATES",32),("QUANTUM",32),("HAMILTONIAN",28),("PION_OPERATOR",28),("PION_SUBTRACTION",28),("CURRENT",28),("COHERENT",30),("OVERLAP",22),("CP",20),("TTN",20),("DOWNSTREAM",20))
INJECTIONS=tuple((f"C16.INJECT.{g}.{i:03d}",f"ordered {g.lower()} mutation {i}",f"C16.{g}.BOUNDARY") for g,n in GROUPS for i in range(1,n+1))
