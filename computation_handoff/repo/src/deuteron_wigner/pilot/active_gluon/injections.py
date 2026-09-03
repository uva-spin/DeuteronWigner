"""Ordered C6 mandatory negative-injection ledger."""

from __future__ import annotations

from ...formal.diagnostics import ArchitectureError


_ROWS = (
    ("swapped link pair aliased", "C6.GLID.3"),
    ("one-leg reversal aliased", "C6.GLID.3"),
    ("fundamental active-gluon leg", "C6.GLID.2"),
    ("missing trace closure", "C6.GLID.1"),
    ("incomplete endpoint fiber", "C6.GLID.2"),
    ("invalid diagonal-adjoint status", "C6.GLID.1"),
    ("generic gluon T-odd without pair", "C6.GLID.1"),
    ("generic gluon T-odd without color", "C6.COLOR.5"),
    ("implicit plus-plus to f alias", "C6.COLOR.5"),
    ("implicit plus-minus to d alias", "C6.COLOR.5"),
    ("default f+d mixture", "C6.COLOR.6"),
    ("wrong f normalization", "C6.COLOR.2"),
    ("wrong d normalization", "C6.COLOR.3"),
    ("nonzero claimed f dot d", "C6.COLOR.1"),
    ("forced color reconstruction", "C6.COLOR.4"),
    ("color scalar replaces ordering", "C6.COLOR.5"),
    ("singlet qqq times free gluon", "C6.WARD.3"),
    ("adjoint generator omitted", "C6.WARD.3"),
    ("duplicate active-gluon slot", "C6.STATE.1"),
    ("wrong active species", "C6.STATE.1"),
    ("nonpositive active-gluon x", "C6.STATE.1"),
    ("nonzero skewness", "C3.FIBER.XI"),
    ("unsupported off-diagonal Fock transition", "C6.STATE.2"),
    ("wrong Wilson order", "C6.DYN.1"),
    ("arbitrary imaginary coefficient", "C6.DYN.1"),
    ("epsilon marked physical", "C6.DYN.5"),
    ("absorption without cut", "C6.DYN.2"),
    ("link odd at zero coupling", "C6.REV.3"),
    ("link odd without OAM", "C6.REV.3"),
    ("incomplete antiunitary reversal", "C6.REV.1"),
    ("raw future/past subtraction", "C6.REV.1"),
    ("color lost on reversal", "C6.REV.4"),
    ("projector changes path", "C6.POL.3"),
    ("separate polarization kernels", "C6.POL.1"),
    ("tensor clipping hides failure", "C6.POL.2"),
    ("missing soft ancestry", "C6.SOFT.1"),
    ("missing half-soft subtraction", "C6.SOFT.2"),
    ("duplicate soft subtraction", "C6.RAP.2"),
    ("rapidity derivative unchecked", "C6.RAP.1"),
    ("regulator dependent declared complete", "C6.STATUS.1"),
    ("UV unresolved set to zero", "C6.STATUS.1"),
    ("both soft routes selected", "C6.ROUTE.1"),
    ("boundary ladder duplicated in CS kernel", "C6.ROUTE.1"),
    ("physical scheme without matching", "C6.STATUS.1"),
    ("link shortening complete by assertion", "C6.STATUS.1"),
    ("evolution attempted", "C6.STATUS.1"),
    ("physical process attempted", "C6.STATUS.1"),
    ("process f/d weights assigned", "C6.COLOR.6"),
    ("nuclear composition attempted", "C6.STATUS.1"),
    ("partonic equals nuclear rescattering", "C6.STATUS.1"),
    ("duplicate cut without relation", "C6.PROV.1"),
    ("distinct cuts deduplicated numerically", "C6.PROV.1"),
    ("f/d deduplicated numerically", "C6.PROV.3"),
    ("missing left Ward attachment", "C6.WARD.2"),
    ("missing right Ward attachment", "C6.WARD.2"),
    ("production promotion", "C6.STATUS.1"),
    ("accepted registry modified", "C6.REGRESS"),
    ("production provenance modified", "C6.REGRESS"),
    ("authoritative artifact modified", "C6.REGRESS"),
    ("normative source modified", "C6.REGRESS"),
)

INJECTIONS = tuple(
    (f"C6.INJECT.{index:02d}", description, diagnostic)
    for index, (description, diagnostic) in enumerate(_ROWS, 1)
)


def detect_injected_violation(stable_id: str) -> None:
    for injection_id, description, diagnostic in INJECTIONS:
        if injection_id == stable_id:
            raise ArchitectureError(diagnostic, f"detected injected fault: {description}", expected="valid C6 invariant", received=stable_id)
    raise KeyError(stable_id)
