from deuteron_wigner.bridge.ifequiv.core import audit_historical_reconstruction,STATUS
def test_c85_historical_dependency_blocker():
 x=audit_historical_reconstruction();assert x['status']==STATUS and not x['scientific_stream_generated']
