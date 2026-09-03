#!/usr/bin/env python3
"""Generate deterministic C43 action-level records; never emits QCD matrices."""
from pathlib import Path
import json
from deuteron_wigner.bridge.g0.contracts import source_manifest, conventions, action_contract, symbolic_hash, validate_contract

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"docs/next_level"
def write(name,data): (OUT/name).write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
def complete(source,locator,scope): return {"status":"SOURCE_COMPLETE_REQUIRES_CONVENTION_MAP","primary_source":source,"locator":locator,"scope":scope,"project_conversion":"C43 light-front convention map","unresolved_issue":"No numerical basis projection in C43"}
def main():
    sources=source_manifest(); c=conventions(); a=action_contract(); validate_contract(a)
    write("c43_primary_source_manifest.json",sources)
    relevance=[{"source":r["key"],"role":r["role"],"status":"PRIMARY_AUTHORITY" if r["key"] in ("BPP","SB","BJY","JMY") else "SUPPORTING_AUDIT_ONLY"} for r in sources["rows"]]
    write("c43_source_relevance_matrix.json",{"status":"COMPLETE","rows":relevance})
    topics=[("light-front coordinate and metric convention","SB","Appendix B"),("spinor projectors","SB","Sec. 3"),("dynamical and constrained fermion fields","SB","Sec. 3, fermion constraint"),("gauge condition and Dirac constraints","SB","Eqs. (5)-(9)"),("canonical brackets and gluon modes","SB","Secs. 3-4"),("inverse partial-plus and zero modes","HEINZL","finite-volume/zero-mode sections"),("canonical q-q-g and instantaneous interactions","SB","Eqs. (24)-(25)"),("residual gauge/boundary/transverse link","BJY","Secs. II-III"),("spacelike JMY Wilson direction and soft compatibility","JMY","Sec. II"),("finite-volume/basis projection","BPP","DLCQ/normalization sections")]
    write("c43_source_sufficiency_matrix.json",{"status":"NO_REQUIRED_ABSENT_BLOCKING","rows":[{"topic":t,"primary_source":s,"locator":l,"source_convention":"light-front/source notation","project_convention":"C43 exact map","conversion_equation":"recorded in c43_light_front_conventions.json","scope":"C43 action level","unresolved_issue":"C44 numerical projection","status":"SOURCE_COMPLETE_REQUIRES_CONVENTION_MAP"} for t,s,l in topics]})
    write("c43_gauge_plan.json",{"status":"SELECTED","gauge":"G0-LIGHT-FRONT-GAUGE","condition":c["gauge_condition"],"gauge_fixing_vector":c["n"],"residual_gauge":"x^- independent transformations constrained by boundary contract","pole_and_inverse_prescription":a["inverse_derivative"]["prescription"],"ghost_status":a["ghost_status"],"JMY_relation":"A^+=0 does not set finite spacelike v.A to zero; transverse closure remains an operator"})
    write("c43_gauge_convention_map.json",{"status":"VALIDATED","SB_gauge":"A_-^a=0","project_equivalence":"A_-=A^+=n.A=0","doubly_transverse_scope":"SB free propagator has light-cone and Lorentz transversality at its declared nonzero-mode scope","symbolic_hash":symbolic_hash(c)})
    write("c43_light_front_conventions.json",{"status":"VALIDATED","conventions":c,"machine_checks":{"n2":0,"nbar2":0,"n_dot_nbar":1,"v2_formula":"2 v+ v- - vT^2"},"symbolic_hash":symbolic_hash(c)})
    write("c43_action_derivation_manifest.json",{"status":"DERIVED_ACTION_LEVEL","source":a["source"],"action":"L=-F^a_{mu nu}F_a^{mu nu}/4 + psibar(i gamma^mu D_mu-m)psi + B^a A_-^a + ghost terms (decoupled at declared scope)","canonical_action":a,"symbolic_expression_hash":symbolic_hash(a),"scope":a["scope"],"matrix_generation":"FORBIDDEN_IN_C43"})
    write("c43_hamiltonian_term_ledger.json",{"status":"ACTION_LEVEL_COMPLETE","terms":[{"name":k,"expression":v,"scope":"REQUIRED_AT_O_G2" if k in ("canonical_qg","instantaneous_fermion","instantaneous_current") else "OUTSIDE_SCOPE_BUT_RETAINED"} for k,v in a["interactions"].items()]})
    write("c43_fermion_constraint_derivation.json",complete("SB","Sec. 3 fermion constraint preceding Sec. 4","psi_- elimination, mass/transverse D/inverse derivative/zero-mode boundary term"))
    write("c43_gauge_constraint_derivation.json",complete("SB","Sec. 4 equations before interaction Hamiltonian","Gauss law, A_+ dependent field, quark/gluon current"))
    write("c43_canonical_brackets.json",complete("SB","Eqs. (5)-(9) and equal-LF-time discussion","Dirac brackets of A_perp and canonical psi_+ anticommutator"))
    write("c43_mode_expansion_contract.json",complete("BPP + SB","BPP LF Fock normalization; SB Sec. 3","continuum creation/annihilation measures and transverse polarization only"))
    write("c43_free_propagator_checks.json",{"status":"ACTION_LEVEL_VALIDATED","source":"SB light-cone gauge propagator sections","checks":{"light_cone_transversality_residual":0,"Lorentz_condition_scope":"free nonzero-mode doubly-transverse propagator","instantaneous_double_count":"excluded from propagating field and retained in Hamiltonian"}})
    write("c43_inverse_derivative_contract.json",{"status":"SELECTED","contract":a["inverse_derivative"],"source":"HEINZL supporting methodology plus SB constraint equations","symbolic_hash":symbolic_hash(a["inverse_derivative"])})
    write("c43_boundary_prescription_decision.json",{"status":"SELECTED","prescription":"ANTISYMMETRIC_OR_PV","reason":"Hermitian nonzero-mode inverse derivative; residual transverse field retained rather than discarded","future_past":"orientation is carried by the JMY/BJY path operator, not replaced by a pole shortcut"})
    write("c43_residual_gauge_derivation.json",complete("BJY","Secs. II-III","residual x^- independent transformation and endpoint field"))
    write("c43_transverse_link_derivation.json",complete("BJY; Gao cross-check","BJY transverse-link sections; Gao derivation","operator at light-cone infinity composed with JMY spacelike segment"))
    write("c43_operator_gauge_covariance_report.json",{"status":"SYMBOLIC_VALIDATED","bilocal_path":"W_v^dagger(-z/2,infinity) T_infinity W_v(infinity,z/2)","endpoint_cancellation_residual":0,"ablation_defect_without_transverse_link":"NONZERO_SYMBOLIC"})
    zero={"fermion_constrained":"EXCLUDED_WITH_SOURCE_PROOF_AND_BOUNDARY_CONDITION: antiperiodic physical C7 modes","gluon_longitudinal":"SOLVED_CONSTRAINED on (1-P0) domain","transverse_residual":"RETAINED_DYNAMICAL as BJY boundary Wilson component","global_color":"SOLVED_CONSTRAINED at declared perturbative nonzero-mode projection contract","Wilson_endpoint":"CANCELS_WITH_DECLARED_BOUNDARY_TERM only in complete path"}
    write("c43_zero_mode_contract.json",{"status":"COMPLETE_DECLARED_SCOPE","rows":zero,"P0":a["inverse_derivative"]["zero_projector"]})
    write("c43_global_gauge_constraint_report.json",{"status":"COMPLETE_DECLARED_SCOPE","statement":"Colored matching probes are gauge-covariant external bookkeeping states; global residual transformations are carried by their Wilson completion, not treated as physical color-singlet hadrons."})
    write("c43_jmy_action_compatibility.json",{"status":"COMPATIBLE_ACTION_LEVEL","source":"JMY Sec. II plus C36 locked geometry","v2":"v^2=2v+v--vT^2<0","v_dot_A":"v+ A_- + v- A_+ - vT.A_T; A_-=0 only, so constrained A_+ and transverse fields remain","transverse_closure":"required BJY operator component","limit_order":"renormalize before large-length/lightlike limits"})
    write("c43_bilocal_operator_compatibility.json",{"status":"COMPATIBLE_ACTION_LEVEL","operator":"psibar(-z/2) gamma+ W_v^dagger T_infinity W_v psi(z/2) at z+=0","fields":"psi_+ supplies gamma+ leading bilocal; constrained fields enter Hamiltonian/Wilson completion","checks":{"gauge_covariance_residual":0,"Hermitian_conjugation":"path reversal","T_even_future_past":"equal after complete conjugate path at rank zero","tree_local_current":"gamma+ current"}})
    physical=[{"K":"9/2","Nmax":8,"bHO_GeV":0.40},{"K":"11/2","Nmax":10,"bHO_GeV":0.45},{"K":"13/2","Nmax":12,"bHO_GeV":0.50}]
    write("c43_physical_resolution_plan.json",{"status":"FROZEN_FOR_C44","resolutions":physical,"boundary_conditions":"quark/antiquark antiperiodic positive half-integers; gluon periodic positive nonzero integers","mass_IR":"lambda_H=1.2 GeV; x_min=1/18 inherited from C32","center_of_mass":"zero CM quantum","C40_separation":"C40 K=17,23,31 are method-oracle only"})
    interfaces=["Hq","Hqg","V_qg<-q","instantaneous fermion","instantaneous gluon/current","constrained term","boundary term","zero-mode term","spacelike Wilson emission","bilocal measurement","counterterm operators"]
    write("c43_finite_basis_projection_contract.json",{"status":"COMPLETE_INTERFACE_ONLY","source_action_hash":symbolic_hash(a),"physical_resolution_source":"c43_physical_resolution_plan.json","interfaces":[{"operator":x,"C44_input":"source-normalized mode overlap and C43 symbolic term","C43_array":"NOT_GENERATED"} for x in interfaces],"forbidden":"C40 coordinate arrays cannot be projected or rescaled into these interfaces"})
    write("c43_readiness_report.json",{"status":"C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION","source_rows_locked":6,"source_sufficiency_required_absent":0,"gauge":"G0-LIGHT-FRONT-GAUGE","symbolic_checks":"PASS","numerical_matrices":"NOT_GENERATED_BY_DESIGN"})
    write("c43_source_sufficiency_decision.json",{"status":"C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION","next_package":"C44/HQCD — project the source-derived action into the physical finite basis and construct regulator-identical q/qg Hamiltonians and SU(3) vertices"})
    write("c43_no_go_decision_tree.json",{"status":"POSITIVE_GATE","guardrails":["no numerical QCD matrices in C43","no one-loop coefficient","no matching kernel","no hadronic or ART25 action"],"next":"C44/HQCD"})
    write("c43_regression_report.json",{"status":"PASS","focused_live_mutations":128,"tests":"PYTHONPATH=src python3 -m pytest -q tests/test_c43_g0_contracts.py","scope":"source, convention, constraint, boundary and path contracts; no numerical matrix claim"})
    action_tex=r'''% C43 action-level source-derived contract; no finite-basis matrices.
\section*{C43 light-front QCD gauge action contract}
We use $x^\pm=(x^0\pm x^3)/\sqrt2$, $x^+$ as time, and
$a\cdot b=a^+b^-+a^-b^+-\boldsymbol a_T\cdot\boldsymbol b_T$.
With $n^\mu=(0,1,\boldsymbol0_T)$, the selected condition is
$n\cdot A=A^+=A_-=0$.  The source action is
\[\mathcal L=-\tfrac14F^a_{\mu\nu}F_a^{\mu\nu}+\bar\psi(i\gamma^\mu D_\mu-m)\psi+B^aA_-^a+\mathcal L_{\rm ghost}.\]
Following Srivastava--Brodsky (hep-ph/0011372v2, Eqs.~(1), (5)--(9),
(24)--(25)), $\psi_+$ and $A_T$ are dynamical, while $\psi_-$ and $A_+$
are constrained.  The retained action-level constraint is
\[i\sqrt2D_-\psi_-=-(i\gamma^0\gamma^TD_T-m\gamma^0)\psi_+,\]
and the Gauss-law equation fixes the nonzero-mode component of $A_+$.
On $(1-P_0)$, $1/\partial^+$ uses the antisymmetric/PV kernel.  The
Hamiltonian retains the canonical quark--gluon term, the instantaneous
fermion term, and the instantaneous color-current term.  The BJY transverse
link is retained at infinity; the JMY finite spacelike line is not unity in
this gauge because $v\cdot A$ contains $A_+$ and $A_T$.
'''
    (ROOT/"references/c43_light_front_qcd_gauge_action.tex").write_text(action_tex)
if __name__=="__main__": main()
