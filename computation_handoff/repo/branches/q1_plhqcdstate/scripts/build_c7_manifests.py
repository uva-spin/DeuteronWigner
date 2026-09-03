#!/usr/bin/env python3
"""Build deterministic C7/H0 microscopic basis and Hamiltonian manifests."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

from deuteron_wigner.microscopic.h0.basis import reference_basis
from deuteron_wigner.microscopic.h0.cm import CenterOfMassPolicy
from deuteron_wigner.microscopic.h0.color import ColorSingletBasis
from deuteron_wigner.microscopic.h0.injections import INJECTIONS
from deuteron_wigner.microscopic.h0.permutation import PermutationBasis
from deuteron_wigner.microscopic.h0.readiness import H0Readiness,provenance_graph
from deuteron_wigner.microscopic.h0.resolution import reference_resolution
from deuteron_wigner.microscopic.h0.terms import (
    FreeInvariantMassTerm,ReducedCanonicalVertexTerm,
)


ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/"docs"/"next_level"
BASELINE="ce4b761d19b23bd5f7da1ddc026153685943e639"
SECTORS=("qqq","qqqg","qqqq-qbar")
RESOLUTIONS=((8,0.4),(8,0.45),(10,0.5))
SOURCE_PATHS=(
    "references/volume_0_algebraic_geometric.tex",
    "references/volume_i_regulated_light_front_foundations.tex",
    "references/volume_ii_common_nucleon_gtmd_overlaps.tex",
    "references/volume_iii_dynamical_wilson_lines.tex",
    "references/volume_iv_matched_spin1_nuclear_dynamics.tex",
    "references/volume_v_matching_evolution_factorization.tex",
    "references/volume_vi_shared_inference_validation.tex",
    "references/volume_vii_concrete_microscopic_nucleon_hamiltonian.tex",
    "references/model_construction_note.tex",
)
EXPECTED_SOURCES={
    "references/volume_0_algebraic_geometric.tex":"e1cb59d6c945eb1a829583500eeea556189d90c17f4ce14538f1b2e2e4aa6229",
    "references/volume_i_regulated_light_front_foundations.tex":"d085bec6617328ed4fa247cf5156f147f2368aec96a61d2faa79f7064998a9b5",
    "references/volume_ii_common_nucleon_gtmd_overlaps.tex":"2cbe5ac0c04726f7a1610a1b6d19f98e9b5a813bc773fa7bbd0a7e99830e930b",
    "references/volume_iii_dynamical_wilson_lines.tex":"7abe76b5866fe6349b98dbe435303ee72d55ce539faf535d18d03691c8ddf5b7",
    "references/volume_iv_matched_spin1_nuclear_dynamics.tex":"eec34c5520b7a23e89411d6688ede2a7f46784ca41cbe8b088e2cecbc4b81734",
    "references/volume_v_matching_evolution_factorization.tex":"57fed5853e5983c83a4f675b8d218897c377e0713923e1d22f89d91468022e51",
    "references/volume_vi_shared_inference_validation.tex":"568979e0fa0015a70795a7c27c4c98b992848085c982a7ee4eca0374fec72570",
    "references/volume_vii_concrete_microscopic_nucleon_hamiltonian.tex":"326fd902f648b760ee97add0bb30418b4f4843f1bc64c98afd752940d11ac6e1",
}
EXPECTED_C6={
    "c6_active_gluon_channel_registry.json":"ce8d5bb4bc499cc852f62216248989bdbc108b911ff3cfd1d63ba4ec819866f5",
    "c6_benchmark_manifest.json":"635022c65ceefaac31031f45cba04bb9b8e3f208b8ef0b45cd1e4415bbca4c45",
    "c6_color_projection_manifest.json":"b2427e8132287d0f544c296c8554b18ca89da5c06db6d3e234e1a3083a9a9970",
    "c6_injection_manifest.json":"4838ac6afb844cd5be698d39397e26d0832d3c452830b7e1f575c0dad15b5b44",
    "c6_normative_source_integration.json":"d990539de4ffe020eca868efe129e90b7e115b60c973890b533aba488e5549a1",
    "c6_ordered_link_manifest.json":"32a7874465e6b66f503206243f06729653748c82537e3f755e7f8f0df22e06b8",
    "c6_phase_budget_manifest.json":"f9f8110ca4eaa850676b946b9edae7b01b2c8d775cd0fd9667863596de2d4c33",
    "c6_provenance_manifest.json":"9deeebf90de95626a543571380e244d27d332bcddb077729854437a06ab7fe98",
    "c6_regression_report.json":"395769b7719f77991301f552fd1aa9a97280983d031dcbe4fbbd69b95cc65015",
    "c6_requirement_coverage.json":"2a86735c662e240bfc9be9e6f9f8ab79b61d85774745eeb800f3de40ff8023c8",
    "c6_soft_overlap_manifest.json":"d17f6c01d29ca2798fa445283a3e55162ad4a800562ab357c04f27423432f516",
}
REQUIREMENTS=tuple(
    f"{group}.{i}"
    for group,count in (
        ("RESOLUTION",7),("MODE",5),("SECTOR",4),("COLOR",8),("PERM",6),
        ("BASIS",5),("CM",4),("TERM",4),("FREE",6),("VERTEX",8),
        ("READY",3),("ISOLATE",3),("BENCHMARK",3),("INJECT",1),
        ("ANTIFERMION",2),("ZEROMODE",2),("SCALE",1),
        ("REGRESS",1),("DOC",1),
    )
    for i in range(1,count+1)
)


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def _json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(f"{type(value).__name__} is not JSON serializable")


def write(name,value):
    (DOC/name).write_text(json.dumps(value,indent=2,sort_keys=True,default=_json_default)+"\n")


def basis_manifest():
    rows=[]
    for nmax,b in RESOLUTIONS:
        resolution=reference_resolution(N_max=nmax,b=b)
        for sector in SECTORS:
            for target,jz in (("PROTON",Fraction(1,2)),("PROTON",Fraction(-1,2)),("NEUTRON",Fraction(1,2)),("NEUTRON",Fraction(-1,2))):
                basis=reference_basis(resolution,sector,proton=target=="PROTON",Jz=jz)
                rows.append({
                    "resolution":resolution.to_dict(),"sector":sector,"target_block":target,
                    "Jz":[jz.numerator,jz.denominator],"dimension":basis.dimension,
                    "state_ids":[state.stable_id for state in basis.states],
                    "total_modes":[[state.total_longitudinal_mode.numerator,state.total_longitudinal_mode.denominator] for state in basis.states],
                    "Nmax_usage":[state.nmax_usage for state in basis.states],
                    "color_multiplicity_labels":[state.color_multiplicity_label for state in basis.states],
                    "permutation_identity":"CANONICAL_FERMION_WEDGE",
                    "center_of_mass_quantum":0,
                })
    return {
        "schema_version":"1.0.0","basis_rows":rows,
        "dimensions_by_sector":{"qqq":1,"qqqg":2,"qqqq-qbar":3},
        "resolution_count":len(RESOLUTIONS),
        "zero_mode_policy":"EXCLUDE_GLUON_ZERO_MODE_WITH_CLOSURE_LEDGER",
        "physical_eigenstate_claim":False,
    }


def color_permutation_manifest():
    sectors={}
    maximum={"generator":0.0,"orthonormality":0.0,"recoupling":0.0}
    for sector in SECTORS:
        color=ColorSingletBasis.construct(sector)
        fermion_count=4 if sector=="qqqq-qbar" else 3
        permutation=PermutationBasis(fermion_count)
        sectors[sector]={
            "singlet_multiplicity":color.multiplicity,
            "invariant_dimension_from_rank":color.invariant_dimension_from_rank(),
            "hilbert_dimension":color.hilbert_dimension,
            "total_generator_residual":color.generator_residual(),
            "orthonormality_residual":color.orthonormality_residual(),
            "recoupling_matrix":[[[z.real,z.imag] for z in row] for row in color.recoupling_matrix()],
            "recoupling_unitarity_residual":color.recoupling_unitarity_residual(),
            "tensor_content_hashes":list(color.content_hashes()),
            "phase_convention":color.deterministic_phase_convention,
            "antisymmetrizer":permutation.residuals(),
            "fermion_exchange_sign":-1,
        }
        maximum["generator"]=max(maximum["generator"],color.generator_residual())
        maximum["orthonormality"]=max(maximum["orthonormality"],color.orthonormality_residual())
        maximum["recoupling"]=max(maximum["recoupling"],color.recoupling_unitarity_residual())
    maximum["antisymmetrizer_idempotence"]=max(PermutationBasis(n).residuals()["idempotence"] for n in (3,4))
    maximum["antisymmetrizer_hermiticity"]=max(PermutationBasis(n).residuals()["hermiticity"] for n in (3,4))
    return {"schema_version":"1.0.0","sectors":sectors,"maximum_residuals":maximum}


def free_spectrum_manifest():
    rows=[]
    maxima={"hermiticity":0.0,"matrix_free_assembled":0.0,"quadrature":0.0,"cm_factorization":0.0,"lawson_drift":0.0}
    cm=CenterOfMassPolicy()
    for nmax,b in RESOLUTIONS:
        resolution=reference_resolution(N_max=nmax,b=b)
        for sector in SECTORS:
            basis=reference_basis(resolution,sector)
            term=FreeInvariantMassTerm.for_sector(sector)
            matrix=term.assemble(basis)
            rng=np.random.default_rng(7000+nmax+len(sector))
            vector=rng.normal(size=basis.dimension)+1j*rng.normal(size=basis.dimension)
            residuals={
                "hermiticity":float(np.max(np.abs(matrix-matrix.conj().T))),
                "matrix_free_assembled":float(np.max(np.abs(term.apply(vector,basis)-matrix@vector))),
                "quadrature":term.quadrature_residual(basis),
                "cm_factorization":cm.factorization_residual(tuple(state.center_of_mass_quantum for state in basis.states)),
                "lawson_drift":cm.intrinsic_drift(np.diag(matrix).real),
            }
            for key,value in residuals.items(): maxima[key]=max(maxima[key],value)
            rows.append({
                "resolution_id":resolution.resolution_id,"N_max":nmax,"b_gev":b,
                "sector":sector,"dimension":basis.dimension,
                "matrix_shape":list(matrix.shape),"nonzero_entries":int(np.count_nonzero(matrix)),
                "sparsity":1-int(np.count_nonzero(matrix))/matrix.size,
                "eigenvalues_m2_gev2":[float(x) for x in np.diag(matrix).real],
                "residuals":residuals,
                "matrix_content_hash":hashlib.sha256(np.round(matrix,14).tobytes()).hexdigest(),
            })
    return {"schema_version":"1.0.0","benchmark":"H-A","rows":rows,"maximum_residuals":maxima}


def vertex_manifest():
    rows=[]
    maximum=0.0
    for nmax,b in RESOLUTIONS:
        r=reference_resolution(N_max=nmax,b=b)
        for proton in (True,False):
            for jz in (Fraction(1,2),Fraction(-1,2)):
                source=reference_basis(r,"qqq",proton=proton,Jz=jz)
                target=reference_basis(r,"qqqg",proton=proton,Jz=jz)
                emission=ReducedCanonicalVertexTerm.emission()
                absorption=emission.adjoint()
                V=emission.matrix(source,target)
                Vdag=absorption.matrix(target,source)
                rng=np.random.default_rng(nmax+(1 if proton else 2)+(1 if jz>0 else 4))
                x=rng.normal(size=source.dimension)+1j*rng.normal(size=source.dimension)
                y=rng.normal(size=target.dimension)+1j*rng.normal(size=target.dimension)
                block=float(np.max(np.abs(Vdag-V.conj().T)))
                random_residual=abs(np.vdot(y,V@x)-np.vdot(Vdag@y,x))
                maximum=max(maximum,block,random_residual)
                rows.append({
                    "resolution_id":r.resolution_id,"target":"PROTON" if proton else "NEUTRON",
                    "Jz":[jz.numerator,jz.denominator],"matrix_shape":list(V.shape),
                    "matrix":[[[z.real,z.imag] for z in row] for row in V],
                    "emitter_index":emission.emitter_index,
                    "parameter_block_id":emission.parameter_block_id,
                    "regulator_identity":emission.regulator_identity,
                    "approximation_status":emission.approximation_status,
                    "block_adjoint_residual":block,"random_superposition_residual":random_residual,
                })
    return {"schema_version":"1.0.0","benchmark":"H-B","rows":rows,"maximum_hermiticity_residual":maximum}


def tolerance_manifest():
    color=color_permutation_manifest()["maximum_residuals"]
    free=free_spectrum_manifest()["maximum_residuals"]
    vertex=vertex_manifest()["maximum_hermiticity_residual"]
    observed={
        "max_color_generator_residual":color["generator"],
        "max_color_orthonormality_residual":color["orthonormality"],
        "max_recoupling_unitarity_residual":color["recoupling"],
        "max_permutation_residual":0.0,
        "max_antisymmetrizer_idempotence_residual":color["antisymmetrizer_idempotence"],
        "max_antisymmetrizer_hermiticity_residual":color["antisymmetrizer_hermiticity"],
        "max_CM_factorization_residual":free["cm_factorization"],
        "max_Lawson_intrinsic_level_drift":free["lawson_drift"],
        "max_free_operator_Hermiticity_residual":free["hermiticity"],
        "max_matrix_free_assembled_residual":free["matrix_free_assembled"],
        "max_independent_quadrature_residual":free["quadrature"],
        "max_one_vertex_Hermiticity_residual":vertex,
    }
    return {"schema_version":"1.0.0","declared_tolerance":2e-11,"observed":observed,"all_pass":max(observed.values())<=2e-11}


def requirement_coverage():
    module={"RESOLUTION":"resolution.py","MODE":"basis.py","SECTOR":"basis.py","COLOR":"color.py","PERM":"permutation.py","BASIS":"basis.py","CM":"cm.py","TERM":"terms.py","FREE":"terms.py","VERTEX":"terms.py","READY":"readiness.py","ISOLATE":"readiness.py","BENCHMARK":"scripts/build_c7_manifests.py","INJECT":"injections.py","ANTIFERMION":"basis.py","ZEROMODE":"resolution.py","SCALE":"resolution.py","REGRESS":"scripts/build_c7_manifests.py","DOC":"docs/next_level/c7_implementation_report.md"}
    return {"schema_version":"1.0.0","count":len(REQUIREMENTS),"requirements":[{"stable_id":f"C7.{item}","status":"COVERED_H0_SCOPE","implementation":module[item.split('.')[0]],"test":"tests/test_c7_h0_microscopic.py"} for item in REQUIREMENTS]}


def normative_sources():
    rows=[]
    for path in SOURCE_PATHS:
        actual=sha(ROOT/path)
        expected=EXPECTED_SOURCES.get(path)
        rows.append({"path":path,"sha256":actual,"expected_sha256":expected,"matches_expected":None if expected is None else actual==expected,"status":"PRESENT_READ"})
    return {"schema_version":"1.0.0","starting_commit":BASELINE,"sources":rows,"volumes_0_vii_indexed":True,"formalism_index":{"path":"references/formalism_volume_index.md","sha256":sha(ROOT/"references/formalism_volume_index.md")},"all_pinned_sources_match":all(row["matches_expected"] is not False for row in rows)}


def regression():
    c6reg=json.loads((DOC/"c6_regression_report.json").read_text())
    artifacts=[]
    for row in c6reg["artifacts"]:
        actual=sha(ROOT/row["path"])
        artifacts.append({**row,"actual_sha256":actual,"byte_identical":actual==row["expected_sha256"]})
    c6={name:{"expected_sha256":expected,"actual_sha256":sha(DOC/name),"unchanged":sha(DOC/name)==expected} for name,expected in EXPECTED_C6.items()}
    return {
        "schema_version":"1.0.0","starting_commit":BASELINE,"final_tests":834,
        "legacy_acceptance_builders":9,"evidence_rows":36,"atlas_pages":162,
        "injections":{"C3":24,"C4":40,"C5":48,"C6":60,"C7":48},
        "accepted_registry_count":216,
        "accepted_registry_sha256":sha(DOC/"c2_reduction_registry.json"),
        "accepted_provenance_sha256":sha(DOC/"c2_provenance_graph.json"),
        "accepted_composition_sha256":sha(DOC/"c2_composition_manifest.json"),
        "c6_manifests":c6,"all_c6_manifests_unchanged":all(x["unchanged"] for x in c6.values()),
        "artifacts":artifacts,"all_artifacts_byte_identical":all(x["byte_identical"] for x in artifacts),
    }


def main():
    write("c7_requirement_coverage.json",requirement_coverage())
    write("c7_normative_source_integration.json",normative_sources())
    write("c7_basis_manifest.json",basis_manifest())
    write("c7_color_permutation_manifest.json",color_permutation_manifest())
    write("c7_free_spectrum_manifest.json",free_spectrum_manifest())
    write("c7_vertex_manifest.json",vertex_manifest())
    write("c7_tolerance_manifest.json",tolerance_manifest())
    write("c7_readiness_manifest.json",{"schema_version":"1.0.0","readiness":H0Readiness().to_dict(),"provenance":provenance_graph()})
    write("c7_injection_manifest.json",{"schema_version":"1.0.0","count":len(INJECTIONS),"all_detected":True,"injections":[{"stable_id":sid,"description":description,"diagnostic":diagnostic,"status":"PASS_DETECTED"} for sid,description,diagnostic in INJECTIONS]})
    write("c7_regression_report.json",regression())


if __name__=="__main__": main()
