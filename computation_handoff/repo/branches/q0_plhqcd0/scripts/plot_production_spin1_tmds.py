#!/usr/bin/env python3
"""Fail-closed guard for a superseded, misleading historical entry point."""

raise RuntimeError(
    "The reduced-correlator closure atlas is not a production prediction. "
    "Use scripts/build_parent_tmd_ensemble.py for current parent-derived "
    "figures, or scripts/plot_exploratory_closure_spin1_tmds.py only for "
    "the explicitly superseded regression fixture."
)
