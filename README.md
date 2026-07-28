# DeuteronWigner

DeuteronWigner is a research codebase for constructing and validating a
flavor-resolved, spin-resolved, leading-twist spin-1 light-front GTMD/TMD
model for the deuteron.

The present implementation is a constrained phenomenological synthesis, not
yet a fundamental prediction from a single solved microscopic QCD state.
The governing scientific objective, implemented scope, limitations, and
next-level microscopic requirements are documented in:

- [`references/model_construction_note.tex`](references/model_construction_note.tex)
- [`references/algebraic_geometric_next_level_model_note.tex`](references/algebraic_geometric_next_level_model_note.tex)
- [`handoff/ROADMAP.md`](handoff/ROADMAP.md)
- [`AGENTS.md`](AGENTS.md)

## Environment

Create the main environment with:

```bash
conda env create -f environment.yml
conda activate deuteron-wigner
```

Additional reproducible environments are described by
`environment-artemide.yml` and `environment-latex.yml`.

## Validation

From the repository root:

```bash
PYTHONPATH=src MPLCONFIGDIR=/tmp/deuteron-mpl python -m pytest -q
```

The accepted checkpoint has 482 passing tests. See `handoff/worklog.md` for
the exact validation history and `handoff/ROADMAP.md` for open requirements.

## Scientific status

The model retains explicit proton/neutron, quark/antiquark/gluon, flavor,
target-polarization, OAM, gauge-link/color, wave-function, nuclear-mechanism,
and uncertainty identities. Named TMDs are projections of typed parent
correlators rather than unrelated plotting functions.

Complete rank-aware evolution and the microscopic WP13 model-class transition
remain governed by the roadmap. Outputs must be interpreted according to
their documented evidence class and domain of validity.

## License

No license has yet been granted. The repository is publicly readable, but
reuse, modification, and redistribution rights have not been specified.
