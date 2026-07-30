"""Stable ledger for all mandatory C5 negative injections."""

from __future__ import annotations

from ...formal.diagnostics import ArchitectureError


_DESCRIPTIONS = (
    "future path with past pole", "past path with future pole",
    "manual pole sign", "endpoint reversal without color conjugation",
    "incompatible path endpoints", "raw future-minus-past subtraction",
    "conjugation without momentum reversal", "conjugation without spin map",
    "link reversal without ordered gluon links", "link odd at zero coupling",
    "link odd with cut disabled", "link odd without required OAM",
    "epsilon stored as physical width", "epsilon convergence failure",
    "cut Jacobian omitted", "duplicate physical cut",
    "equal denominators incorrectly deduplicated", "off-shell discrete absorption",
    "Sivers route uses Boer-Mulders projector", "Boer-Mulders route uses Sivers projector",
    "scalar projector proportionality", "wrong active species or flavor",
    "negative-x quark substituted for antiquark", "nonzero skewness",
    "off-diagonal sector without rescattering source", "Wilson order zero phase",
    "Wilson order above one", "fundamental-adjoint mismatch",
    "ordered gluon links swapped", "f/d color relabeling",
    "generic gluon T-odd output", "unresolved matching marked complete",
    "C5 sent to Volume V evolution", "C5 sent to PROC",
    "C5 inserted in 216-route registry", "C5 connected to production root",
    "authoritative artifact changed", "C3/C4 manifest changed",
    "pilot fitted to production data", "arbitrary imaginary kernel constant",
    "Volume IV without helicity matrices", "Volume IV without correlated p/n",
    "Volume IV without phase/soft/covariance", "Volume V without closed basis",
    "Volume V without LF-QCD matching", "process without link/color/Glauber",
    "normative source changed", "C4 architecture record changed",
)

_DIAGNOSTICS = (
    "C5.POLE.1", "C5.POLE.1", "C5.POLE.1", "C5.TIME.1", "C5.PATH.2",
    "C5.TIME.1", "C5.TIME.1", "C5.TIME.1", "C5.GLUON.1", "C5.ZERO.1",
    "C5.ZERO.1", "C5.ZERO.1", "C5.DIST.2", "C5.DIST.3", "C5.DIST.1",
    "C5.CUT.2", "C5.CUT.3", "C5.CUT.1", "C5.QUARK.2", "C5.QUARK.2",
    "C5.QUARK.2", "C5.KERNEL.2", "C5.KERNEL.2", "C3.FIBER.XI",
    "C5.KERNEL.1", "C5.PATH.2", "C5.PATH.2", "C5.KERNEL.1",
    "C5.GLUON.1", "C5.GLUON.2", "C5.GLUON.2", "C5.STATUS.1",
    "C5.STATUS.2", "C5.STATUS.2", "C5.ISOLATE", "C5.ISOLATE",
    "C5.REGRESS", "C5.REGRESS", "C5.STATUS.1", "C5.KERNEL.3",
    "C5.STATUS.2", "C5.STATUS.2", "C5.STATUS.2", "C5.STATUS.2",
    "C5.STATUS.2", "C5.STATUS.2", "C5.REGRESS", "C5.REGRESS",
)

INJECTIONS = tuple(
    (f"C5.INJECT.{index:02d}", description, diagnostic)
    for index, (description, diagnostic) in enumerate(zip(_DESCRIPTIONS, _DIAGNOSTICS), 1)
)


def detect_injected_violation(stable_id: str) -> None:
    for injection_id, description, diagnostic in INJECTIONS:
        if stable_id == injection_id:
            raise ArchitectureError(diagnostic, f"detected injected fault: {description}", expected="valid C5 invariant", received=stable_id)
    raise KeyError(stable_id)
