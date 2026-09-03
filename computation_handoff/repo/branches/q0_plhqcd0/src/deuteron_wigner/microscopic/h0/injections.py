"""Stable diagnostic ledger for the 48 mandatory C7/H0 fault classes."""

from __future__ import annotations

from ...formal.diagnostics import ArchitectureError


_ROWS=(
("missing LF factor two","C7.LF.CONVENTION"),("oscillator/TMD width alias","C7.RESOLUTION"),
("Hamiltonian/rapidity scale alias","C7.RESOLUTION"),("TMD regulator used as vertex cutoff","C7.RESOLUTION"),
("zero-mode policy omitted","C7.RESOLUTION"),("floating longitudinal mode","C7.MODE"),
("sum k differs from K","C7.BASIS"),("gluon zero mode permitted","C7.MODE"),
("Nmax violated","C7.BASIS"),("wrong total Jz","C7.BASIS"),
("resolution ID collision","C7.RESOLUTION"),("nondeterministic basis order","C7.BASIS"),
("duplicate many-body ordering","C7.BASIS"),("qqq singlet omitted","C7.COLOR"),
("multiple qqq singlets","C7.COLOR"),("qqqg multiplicity omitted","C7.COLOR"),
("qqq singlet times free gluon","C7.COLOR"),("qqqq-qbar singlet omitted","C7.COLOR"),
("wrong antiquark generator","C7.COLOR"),("total generator nonclosure","C7.COLOR"),
("nonunitary recoupling","C7.COLOR"),("color multiplicity erased","C7.COLOR"),
("identical-quark antisymmetry violated","C7.PERM"),("post-assembly antisymmetry","C7.PERM"),
("cross-cluster antisymmetry violated","C7.PERM"),("invalid antisymmetrizer","C7.PERM"),
("CM factorization omitted","C7.CM"),("CM-failed basis marked ready","C7.CM"),
("intrinsic Lawson drift","C7.CM"),("arbitrary diagonal free spectrum","C7.FREE"),
("matrix-free/assembled mismatch","C7.FREE"),("basis mass called MSbar","C7.FREE"),
("term sector endpoints omitted","C7.TERM"),("term parameter owner omitted","C7.TERM"),
("term regulator omitted","C7.TERM"),("vertex adjoint omitted","C7.VERTEX"),
("vertex regulator mismatch","C7.VERTEX"),("wrong vertex color generator","C7.VERTEX"),
("emitter identity erased","C7.VERTEX"),("permutation sign omitted","C7.VERTEX"),
("vertex longitudinal mismatch","C7.VERTEX"),("vertex Jz mismatch","C7.VERTEX"),
("reduced vertex called complete QCD","C7.READINESS"),("TMD-specific vertex coupling","C7.VERTEX"),
("vertex connected to C5/C6 phase","C7.ISOLATION"),("H0 promoted to production","C7.ISOLATION"),
("authoritative production mutation","C7.REGRESS"),("normative source mutation","C7.REGRESS"),
)
INJECTIONS=tuple((f"C7.INJECT.{i:02d}",description,diagnostic) for i,(description,diagnostic) in enumerate(_ROWS,1))


def detect_injected_violation(stable_id: str) -> None:
    for injection_id,description,diagnostic in INJECTIONS:
        if injection_id==stable_id:
            raise ArchitectureError(diagnostic,f"detected injected fault: {description}",expected="valid C7/H0 invariant",received=stable_id)
    raise KeyError(stable_id)
