from fractions import Fraction
import numpy as np
import pytest
from deuteron_wigner.bridge.qgtm.core import (assert_ready_c62,circular_cartesian_shell,exact_tm_block,mutate_live_c62,one_dimensional_tm_bracket,polar_to_circular_state,snapshot,validate_c62)
def test_c62_exact_phase_bracket_and_residues():
 v=assert_ready_c62();assert polar_to_circular_state(1,0)['phase_value']==-1
 assert one_dimensional_tm_bracket(0,0,0,0,Fraction(7,9)).value_re==1
 assert [r['EXACT_ZERO_QUADRATURE_NOISE'] for r in v['residue']['rows']]==[4032,15840,48048]
 b=exact_tm_block(7,9,2)['numeric'];assert np.linalg.norm(b.conj().T@b-np.eye(b.shape[1]))<1e-12
 assert circular_cartesian_shell(2)['unitarity_residual']==0 and validate_c62(snapshot())
@pytest.mark.parametrize('fault_id',range(256))
def test_c62_live_mutations_fail(fault_id):assert not validate_c62(mutate_live_c62(fault_id))
