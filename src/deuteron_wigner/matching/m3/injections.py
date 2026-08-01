GROUPS = (
    ("SOURCE", 90), ("DISTRIBUTION", 90), ("OPERATOR", 90),
    ("GAMMA5", 72), ("COLLINEAR", 84), ("RANK_OPE", 84),
    ("NUCLEAR", 78), ("ACCURACY", 72), ("LEAKAGE", 60),
)

INJECTIONS = tuple(
    (f"C22.INJECT.{group}.{i:03d}", f"ordered {group.lower()} fault {i}", f"C22.{group}.REJECT")
    for group, count in GROUPS for i in range(1, count + 1)
)
