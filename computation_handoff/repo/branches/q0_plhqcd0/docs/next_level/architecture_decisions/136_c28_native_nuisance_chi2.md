# ADR 136: preserve source nuisance and chi2 semantics

Status: accepted.

Use DataProcessor’s native variance columns, correlated systematic columns,
normalization directions, A-matrix profiling, best normalization, chi2, and
decomposition. A generic covariance replacement is not accepted merely because
it looks algebraically similar. Raw-central, ensemble-mean-prediction, and
mean-member chi2 remain separately named quantities.

