# ADR 151: diagnostic versus likelihood semantics

Decision: whitening uses the exact nonzero covariance eigenspace and reports
null-space residuals. Whitened norms are diagnostics, not probabilities,
p-values, likelihoods, or optimization objectives. C29 changes no parameter or
member weight.
