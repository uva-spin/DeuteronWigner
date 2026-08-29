from deuteron_wigner.bridge.ifhistenv.core import audit_capsule,STATUS
def test_c86_requires_bound_producer_roots():
 x=audit_capsule();assert x['status']==STATUS and not x['historical_C72_root_hash_bound']
