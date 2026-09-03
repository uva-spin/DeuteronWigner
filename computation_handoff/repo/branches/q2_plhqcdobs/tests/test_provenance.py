import unittest

from deuteron_wigner.provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    PredictionTrace,
    ValidityDomain,
)


class ProvenanceTests(unittest.TestCase):
    def component(self, evidence=EvidenceClass.PHENOMENOLOGY, uncertainty="replicas"):
        return ComponentProvenance(
            name="flavor PDF",
            evidence=evidence,
            mechanism=Mechanism.NUCLEON_IMPULSE,
            sources=("CT18NNLO",),
            assumptions=("leading one-body term",),
            validity=ValidityDomain(1e-5, 1.0, 1.3, 1e5),
            uncertainty_kind=uncertainty,
            replaceable_interface="NucleonCollinearInput",
        )

    def test_trace_reports_evidence_and_accepts_explicit_components(self):
        trace = PredictionTrace(
            species="q",
            flavor=2,
            operator_projection="gamma+",
            target_channel="U",
            gauge_link="[+,+]",
            components=(self.component(),),
        )
        trace.require_no_hidden_completion()
        self.assertEqual(trace.evidence_summary()["phenomenology_constrained"], 1)

    def test_unconstrained_component_requires_parameter_uncertainty(self):
        trace = PredictionTrace(
            species="q",
            flavor=2,
            operator_projection="gamma+",
            target_channel="U",
            gauge_link="[+,+]",
            components=(self.component(EvidenceClass.UNCONSTRAINED, "none"),),
        )
        with self.assertRaises(ValueError):
            trace.require_no_hidden_completion()


if __name__ == "__main__":
    unittest.main()
