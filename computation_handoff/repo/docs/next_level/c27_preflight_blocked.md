# C27/P1C blocked preflight

C27 has not begun. The mandatory incoming-source gate failed because
`data/incoming/c27_art25/` does not exist and no admissible exact
`MSHT20_REP` archive, directory, or complete generator state was found in the
workspace or Downloads.

Status: `C27_BLOCKED_MISSING_EXACT_MSHT20_REP`.

No C27 capability matrix, runtime, distribution, process output, covariance,
qualification status, or completion deliverable was created. C26 remains the
authoritative scientific state at commit
`8c2ed28abadf73663e2c816ac49b13541fae6a3b`.

To unblock C27, stage the author/source payload in
`data/incoming/c27_art25/`. It must contain either the exact `MSHT20_REP`
source with members covering 0--999 plus checksum and permission, or the full
deterministic generator contract specified in `c27_p1c_codex_prompt.md`.
Then run:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/preflight_c27.py
```

The preferred source-owned frozen-output bundle may be staged alongside it.
Its absence does not block source-regenerated validation once the exact PDF
ensemble is available, but it must remain visibly unavailable.
