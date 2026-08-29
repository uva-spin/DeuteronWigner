"""Stable ordered C9 fault catalogue."""

DESCRIPTIONS=tuple(f"C9 required failure class {i:02d}" for i in range(1,73))+(
"separately supplied Wilson coupling","finite epsilon used as cut support","off-shell discrete absorption",
"duplicated C5/C6 types","lost ordered gluon-link identity","collapsed f/d channels",
"false WILSON_READY","downstream nuclear/evolution/process/inference promotion",
"production registry mutation","authoritative artifact mutation","normative source mutation",
)
INJECTIONS=tuple((f"C9.INJECT.{i:03d}",d,"ORDERED_STRUCTURED_FAIL_CLOSED") for i,d in enumerate(DESCRIPTIONS,1))
