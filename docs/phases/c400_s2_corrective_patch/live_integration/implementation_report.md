# C400.S2 live-integration implementation report

The supplied corrective patch was verified against its package manifest and exact patch SHA-256, applied cleanly to the isolated C400 worktree, compiled, tested, and regenerated.

The focused acceptance suite passed all 43 tests. Generated invariants match the supplied acceptance specification: 57 C396 binding rows with zero complete numerical apply paths; 33/33 corrected C144 derivative rows verified; six historical derivative mismatches exposed; semantic replay passing; and no physical fit, rank, current selection, averaging, or activation.

The relevant upstream regression recorded 41 passes and two strict failures caused by the missing `data/runtime/c64_qgtm2/index.json`. The full local pytest profile stopped during collection with 76 errors from the same absent read-only C64 artifact. No substitute or regeneration was used.

The default compile command encountered a macOS Python cache permission error; the equivalent compile completed successfully with `PYTHONPYCACHEPREFIX=/tmp/c400_s2_pycache`.

No manual reconciliation was required. No local commit, merge, push, historical-evidence rewrite, or next-phase launch was performed. Ownership returns to USER_CHATGPT for scientific review and any separate commit/merge decision.
