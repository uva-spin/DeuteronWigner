GROUPS=(("DELTA",52),("SIXQ_COLOR",64),("MATCHING",58),("HAMILTONIAN_CURRENT",62),("PARTONIC",46),("COHERENT_CP",42),("TTN",42),("ISOLATION",34))
INJECTIONS=tuple((f"C18.INJECT.{g}.{i:03d}",f"ordered {g.lower()} fault {i}",f"C18.{g}.REJECT") for g,n in GROUPS for i in range(1,n+1))
