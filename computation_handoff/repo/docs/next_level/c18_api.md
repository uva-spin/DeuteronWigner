# C18/N3 validation API

`deuteron_wigner.nuclear.n3` extends the immutable N2 root with four mutually
exclusive, content-addressed assumption plans. `delta_report` supplies the
charge-complete isospin-zero DeltaDelta basis, allowed 3S1/3D1/7D1 channels,
exchange certificate, and closed-channel threshold oracle.

`six_quark_color_report`, `antisymmetry_report`, and `hidden_color_report`
expose the five-dimensional SU(3) singlet multiplicity, signed S6 contract,
one cluster plus four hidden-color basis directions, and a second unitarily
rotated hidden basis. `cluster_report` supplies typed NN and DeltaDelta
embeddings, their Gram projector, and the orthogonal compact complement.

`hamiltonian_report`, `current_report`, and `continuity_report` expose the
coupled four-sector state and its declared-order operator attachments.
`parent_report`, `tensor_report`, `coherent_report`, and `cp_report` retain
resolved amplitudes through composition and trace only afterward.
`ttn_report` records full- and reduced-bond behavior. All APIs are
validation-only, unmatched, unevolved, and unreachable from production.
