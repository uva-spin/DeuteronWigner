# C100/IFPRIMENUM implementation report

C100 adds authenticated primitive-domain enumeration over unchanged C98.  It
preserves C98's three public methods and exposes only:

```python
historical_primitive_domain_manifest()
historical_primitive_record_page(*, family_id=None, cursor=None, limit=...)
```

The manifest and pages contain identity/location metadata only.  Primitive
content remains available solely through C98's
`historical_primitive_record(family_id, record_id)`.  The C100 loader never
opens C98's private location index and has no builder or repair fallback.

The C99 no-go is superseded only at its public enumeration interface boundary.
No C99 semantic equivalence decision, expanded record stream, C80 evaluation,
or downstream physics object is created here.
