# C40 boundary and exact next calculation

C40 contains executable finite-basis operator infrastructure, not a bare
one-loop calculation.  The missing inputs for C41/R2B are the regulated real
qg, virtual q, Wilson, endpoint/transverse, instantaneous, constrained,
zero-mode, boundary, and counterterm *bare correlator residuals* in these
arrays, together with the selected-continuum calculation under the common IR
mass prescription.  Only those residuals may populate `A_CT c_CT=r_bare`.

C41 must execute universal soft/overlap subtraction exactly once and extract a
state-independent common-IR finite-basis-minus-continuum difference.  It must
not substitute C40's synthetic RHS, use ART25 points as an x grid, apply a
kernel to a proton, or infer a normalization.
