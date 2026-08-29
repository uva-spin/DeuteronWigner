GROUPS=(("BASELINE",16),("KINEMATICS",24),("STATE_SPIN",28),("SPECTRAL",20),("OPERATOR",24),
        ("REDUCTION",18),("TENSOR_B1",18),("CURRENT_OFFSHELL",22),("WILSON",20),("TAGGED_CP",18),
        ("PROVENANCE",20),("DOWNSTREAM",16))
INJECTIONS=tuple((f"C15.INJECT.{g}.{i:03d}",f"ordered {g.lower()} mutation {i}",f"C15.{g}.BOUNDARY")
                 for g,n in GROUPS for i in range(1,n+1))
