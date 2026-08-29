"""Stable diagnostic ledger for the forty mandatory C4 fault injections."""

from __future__ import annotations

from ..formal.diagnostics import ArchitectureError


INJECTIONS = (
    ("C4.INJECT.01", "non-unit sector probabilities", "C4.STATE.PROBABILITY"),
    ("C4.INJECT.02", "wrong baryon number", "C4.SEA_LEDGER.BARYON"),
    ("C4.INJECT.03", "pair changes electric charge", "C4.SEA_LEDGER.CHARGE"),
    ("C4.INJECT.04", "wrong antiquark generator sign", "C4.SEA_COLOR.ANTISIGN"),
    ("C4.INJECT.05", "non-singlet five-parton tensor", "C4.SEA_COLOR.NONSINGLET"),
    ("C4.INJECT.06", "duplicate antiquark active multiplicity", "C4.ACTIVE.DUPLICATE"),
    ("C4.INJECT.07", "negative-x antiquark copy", "C4.ACTIVE.NEGATIVE_X"),
    ("C4.INJECT.08", "antiquark without sea or induced sector", "C4.ZERO.ANTIQUARK"),
    ("C4.INJECT.09", "qqq singlet times free gluon", "C4.GLUON_COLOR.FREE_GLUON"),
    ("C4.INJECT.10", "non-singlet qqqg tensor", "C4.GLUON_COLOR.NONSINGLET"),
    ("C4.INJECT.11", "omitted adjoint generator", "C4.GLUON_COLOR.ADJOINT"),
    ("C4.INJECT.12", "wrong gluon active slot", "C4.ACTIVE.SPECIES"),
    ("C4.INJECT.13", "gluon without explicit or induced sector", "C4.ZERO.GLUON"),
    ("C4.INJECT.14", "non-unit plus momentum", "C4.LEDGER.MOMENTUM"),
    ("C4.INJECT.15", "copied or sign-flipped recoil", "C3.RECOIL.PHYSICAL"),
    ("C4.INJECT.16", "incompatible momentum fibers", "C3.FIBER"),
    ("C4.INJECT.17", "off-diagonal overlap without source", "C3.KERNEL.SECTOR"),
    ("C4.INJECT.18", "physical f/d assignment at order zero", "C4.GLUON.TODD"),
    ("C4.INJECT.19", "TMD route at nonzero transfer", "C4.TMD_ROUTE.TRANSFER"),
    ("C4.INJECT.20", "GPD discards path identity", "C4.GPD_ROUTE.IDENTITY"),
    ("C4.INJECT.21", "regulated staple promoted to physical", "C4.MATCHING_STATUS.PHYSICAL"),
    ("C4.INJECT.22", "PDF route mismatch", "C4.PDF_ROUTE.CLOSURE"),
    ("C4.INJECT.23", "post-reduction normalization", "C4.ROUTE.NORMALIZATION"),
    ("C4.INJECT.24", "quark current uses q plus qbar", "C4.CURRENT_ROUTE.SIGN"),
    ("C4.INJECT.25", "gluon number current", "C4.CURRENT_ROUTE.GLUON_NUMBER"),
    ("C4.INJECT.26", "quark Mellin convention on gluon", "C4.GLUON_LEDGER.MELLIN"),
    ("C4.INJECT.27", "direct sequential current mismatch", "C4.ROUTE_CLOSURE"),
    ("C4.INJECT.28", "singular Feshbach resolvent", "C4.FESHBACH.SINGULAR"),
    ("C4.INJECT.29", "POP omits induced term", "C4.FESHBACH.POP_ONLY"),
    ("C4.INJECT.30", "explicit and induced enabled together", "C4.INDUCED_OPERATOR.DOUBLE_COUNT"),
    ("C4.INJECT.31", "C4 connects to production root", "C4.ISOLATE.PROVENANCE"),
    ("C4.INJECT.32", "production registry mutation", "C4.REGRESS.REGISTRY"),
    ("C4.INJECT.33", "C2 graph or plan mutation", "C4.REGRESS.C2_GRAPH"),
    ("C4.INJECT.34", "C3 benchmark mutation", "C4.REGRESS.C3_MANIFEST"),
    ("C4.INJECT.35", "C4 overlap enters production builder", "C4.ISOLATE.BUILDER"),
    ("C4.INJECT.36", "nonzero skewness", "C3.FIBER.XI"),
    ("C4.INJECT.37", "nonzero Wilson order", "C4.ZERO.WILSON"),
    ("C4.INJECT.38", "T-odd phase in analytic core", "C4.GLUON.TODD"),
    ("C4.INJECT.39", "required unspecified metadata", "C4.MATCHING_STATUS.UNSPECIFIED"),
    ("C4.INJECT.40", "nondeterministic serialization", "C4.DOC.ORDERING"),
)


def detect_injected_violation(injection_id: str) -> None:
    """Fail closed after a test deliberately selects a named invalid state."""
    for stable_id, description, diagnostic in INJECTIONS:
        if stable_id == injection_id:
            raise ArchitectureError(
                diagnostic, f"detected injected fault: {description}",
                expected="valid C4 invariant", received=injection_id,
            )
    raise KeyError(injection_id)
