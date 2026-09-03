import pytest
from deuteron_wigner.bridge import m0a
def test_metadata_cannot_open_a_numerical_readiness_gate():
 q,qg,w,x=m0a.infrastructure()
 with pytest.raises(AttributeError):
  q.vector
 with pytest.raises(AttributeError):
  w.matrix
 assert x.number_moment()==1
