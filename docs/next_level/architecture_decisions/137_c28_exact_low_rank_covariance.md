# ADR 137: store exact theory covariance as an anomaly factor

Status: accepted.

Store A_is = (T_is - mean_i)/sqrt(641), retaining indivisible joint ART25
member identities. Covariance blocks are queried as A_I^T A_J. This is exact
for the 642-member empirical ensemble, avoids an unnecessary dense matrix, and
preserves DY–SIDIS and distribution–process correlations. Independent marginal
reshuffling is forbidden.

