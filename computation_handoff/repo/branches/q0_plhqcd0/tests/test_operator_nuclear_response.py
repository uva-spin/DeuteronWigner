import numpy as np

from deuteron_wigner.operator_nuclear_response import (
    MEMBERS,
    NuclearResponseMechanism,
    gluon_response_correction,
    gluon_response_map,
    quark_response_correction,
    quark_response_map,
)
from deuteron_wigner.gluon_correlator import Spin1GluonCorrelator
from deuteron_wigner.quark_correlator import (
    SPIN1_QUARK_TMD_NAMES,
    compose_spin1_quark_correlator,
)


def qparent():
    values = {name: 0.0 for name in SPIN1_QUARK_TMD_NAMES}
    values.update(f1=2.0, g1=0.2, h1=0.1, f1LL=0.04)
    return compose_spin1_quark_correlator((0.3, 0.1), 1.8756, values)


def gparent():
    values = np.eye(6).reshape(3, 2, 3, 2).transpose(0, 2, 1, 3)
    return Spin1GluonCorrelator(values)


def test_every_mechanism_member_is_complete_positive_and_correlated():
    for mechanism in NuclearResponseMechanism:
        for member in MEMBERS:
            qmap = quark_response_map(mechanism, 0.05, member)
            gmap = gluon_response_map(mechanism, 0.05, member)
            assert qmap.apply(qparent()).minimum_positivity_eigenvalue() >= -1e-12
            assert gmap.apply(gparent()).minimum_positivity_eigenvalue() >= -1e-12
            assert member.correlation_group == "wp12_joint_nuclear_response"


def test_response_corrections_close_exactly_to_mapped_parent():
    for mechanism in NuclearResponseMechanism:
        member = MEMBERS[1]
        q = qparent()
        qc = quark_response_correction(q, mechanism, 0.4, member)
        qm = quark_response_map(mechanism, 0.4, member).apply(q)
        assert np.allclose(q.vector+qc.vector, qm.vector)
        assert np.allclose(q.axial+qc.axial, qm.axial)
        assert np.allclose(q.transverse+qc.transverse, qm.transverse)
        g = gparent()
        gc = gluon_response_correction(g, mechanism, 0.4, member)
        gm = gluon_response_map(mechanism, 0.4, member).apply(g)
        assert np.allclose(g.values+gc.values, gm.values)


def test_shadowing_domain_turns_off_at_x_point_one():
    q = qparent()
    correction = quark_response_correction(
        q, NuclearResponseMechanism.SHADOWING, 0.1, MEMBERS[1]
    )
    assert np.allclose(correction.vector, 0.0)
    assert np.allclose(correction.axial, 0.0)
    assert np.allclose(correction.transverse, 0.0)
