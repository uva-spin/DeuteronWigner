from deuteron_wigner.bridge.ifcoord2.core import audit_c82_determinism,STATUS
def test_c84_detects_c82_snapshot_nondeterminism():
 x=audit_c82_determinism();assert x['status']==STATUS and 'metadata only' in x['C82_payload_role'] and not x['matrix_created']
