"""Reject executable C40 method arrays that lack regulator-identical derivation."""
from pathlib import Path
import inspect
from deuteron_wigner.bridge.m0b import basis, hamiltonian, vertices, wilson, constrained, counterterms, distributions, refinement

STATUS="C41_C40_SUBSTRATE_NOT_REGULATOR_IDENTICAL"
TOY="EXECUTABLE_TOY_NOT_PHYSICS_IDENTICAL"

_OBJECTS=(
 ("Hq","hamiltonian._matrix",hamiltonian,"hand-set diagonal mass array and nearest-neighbour stencil", "no source-derived light-front kinetic measure or C36 normalization"),
 ("Hqg","hamiltonian._matrix",hamiltonian,"hand-set diagonal mass array and nearest-neighbour stencil", "no source-derived qg phase space, polarization, or interaction completion"),
 ("V_qg_q","vertices.vertex",vertices,"local color_generator and selection recipe", "not an SU(3) generator representation or source-normalized LF vertex"),
 ("V_q_qg","vertices.vertex.conj().T",vertices,"generated adjoint of the local vertex recipe", "inherits non-identical emission operator"),
 ("instantaneous_fermion","constrained.operators",constrained,"fixed diagonal numerical stencil", "no constrained-field derivation"),
 ("instantaneous_gluon","constrained.operators",constrained,"fixed diagonal numerical stencil", "no constrained-field derivation"),
 ("constrained","constrained.operators",constrained,"fixed diagonal numerical stencil", "no constraint equation or gauge completion"),
 ("boundary","constrained.operators",constrained,"fixed diagonal numerical stencil", "no boundary condition or infinity-junction derivation"),
 ("zero_mode","constrained.operators",constrained,"fixed diagonal numerical stencil", "no zero-mode solution or exact absence proof"),
 ("Wilson_longitudinal","wilson.wilson",wilson,"local trapezoidal phase recipe", "no C36 finite-basis mode function or path-ordered field operator"),
 ("Wilson_endpoint","wilson.wilson",wilson,"local 0.11 endpoint coefficient", "no source-defined cusp/junction operator"),
 ("Wilson_transverse","wilson.wilson",wilson,"local 0.07 transverse phase coefficient", "no transverse closure mode realization"),
 ("counterterm_operator_basis","counterterms.counterterms",counterterms,"ten hand-assigned diagonal stencils", "no partonic renormalization-condition derivation"),
 ("counterterm_matrix","counterterms.counterterms",counterterms,"fixed tridiagonal 10x10 test matrix", "explicitly synthetic, not physical conditions"),
 ("distributional_measurements","distributions.measurements",distributions,"local finite-vector weights and cutoff convention", "no regulator-identical x/bT bilocal measurement map"),
 ("refinement_maps","refinement.maps",refinement,"coordinate padding/truncation", "no source-derived finite-basis embedding or trajectory map"),
)

def audit_c40_substrate():
    """Return an evidence-rich audit; no member is eligible for C41 diagrams."""
    records=[]
    for name,formula,module,recipe,gap in _OBJECTS:
        text=inspect.getsource(module)
        records.append({"object":name,"status":TOY,"source_or_first_principles_formula":recipe,
          "local_generator":str(Path(module.__file__).relative_to(Path.cwd())),"generator_present":bool(text),
          "normalization_convention":"local numerical convention only; no source-qualified C36/C38 normalization",
          "basis_ordering":"C40 coordinate ordering only", "color_action":"local recipe or not applicable; not an audited SU(3) action",
          "helicity_action":"local selection recipe or not applicable", "momentum_conservation":"integer table constraint only where present",
          "spacelike_direction_dependence":"local RAPIDITY=0.73 phase only where present", "IR_mass_dependence":"local IR_MASS=0.37 literal or absent",
          "perturbative_order":"not established", "independent_numerical_check":"C40 internal algebra only; not independent regulator-identity evidence",
          "blocking_reason":gap})
    return {"status":STATUS,"eligible_object_count":0,"required_object_count":len(records),"records":records,
            "decision":"No C40 numerical object may enter a C41 one-loop contribution ledger."}

def assert_c40_not_eligible():
    audit=audit_c40_substrate()
    assert audit["status"]==STATUS and audit["eligible_object_count"]==0
    assert all(x["status"]==TOY for x in audit["records"])
    return audit
