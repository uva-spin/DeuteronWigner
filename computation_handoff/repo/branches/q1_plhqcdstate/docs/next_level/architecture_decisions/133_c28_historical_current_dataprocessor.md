# ADR 133: historical and current DataProcessor are distinct

Status: accepted.

Use commit `761f3fcdd3701c5cf69e822f9ffbbd5db394fc58` for the historical ART25
dataset list, loader, cuts, and native call path. Treat current public commit
`9f9dda71b69dd26e288be189a396736827cfeed3` only as a comparison route. A
complete Git bundle preserves the historical source. Silent master
substitution fails closed because source changes can alter scientific meaning.

