# ADR 129: all-member execution

Use independent processes, content-addressed member records, and immutable
joint IDs. Never share ARTEMIDE's mutable replica state across threads and
never impute a failed member.
