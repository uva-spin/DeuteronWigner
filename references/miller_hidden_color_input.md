# Miller hidden-color six-quark scenario

`hidden_color.py` implements Eq. (14) of G. A. Miller, *Phys. Rev. C* **89**,
045203 (2014), arXiv:1311.4561. The model mixes harmonic-oscillator six-quark
\(s\)- and \(d\)-states with \(R=1.2\) fm and constituent mass \(m=338\) MeV.
Its amplitude-product parameter \(P_{6q}=0.0015\) was chosen in the source to
reproduce the HERMES point at \(x=0.452\).

This is a model-dependent, observable-level \(b_1\) scenario—not an
independently validated six-quark probability or a production
flavor-resolved light-front correlator. The source fixes the charge-weighted
observable but not its \(u,d,\bar u,\bar d\) decomposition. The code therefore
does not invent that decomposition or install the term as a generic
non-nucleonic TMD parent.

Tests reproduce the source's rounded HERMES-bin table, exact probability
scaling and zero switch, support \(0<x<2\), and the valence tensor sum rule
to better than \(10^{-8}\). Published \(\pm10\%\) radius and mass variants
are named explicitly. The combined diagnostic HERMES chi-square is 3.56;
this is not independent validation because the final bin calibrated
\(P_{6q}\).

```text
PYTHONPATH=src python -m pytest -q tests/test_hidden_color.py
PYTHONPATH=src python scripts/compare_b1_pion_exchange_to_hermes.py
```
