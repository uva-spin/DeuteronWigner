# C406 live integration report

C406 was integrated in the required isolated worktree from baseline `4dbb0b8bbadc540f0da2337c46040afb971fffc1` on branch `codex/c406-c117-i2-gluon-normal-order-descendant`. The supplied package verified with 95 files and 33 replacement files; its patch SHA256 is `3404d2b8615abb679258f20246d96436604b2937b52f600a684c53d3664a2fe7`.

The patch applied cleanly, compiled successfully, and the canonical generator reproduced package root `c5805fa4a0f22fecd6f58c0668a0fa4d9a28990e5e176f052d07d317da65390e`. Two independent clean output builds produced 16/16 byte-identical generated artifacts.

Required tests passed: C406 24, C405 21, C404 15, C403 16, C401 14, C400.S2 26, C114/C115/C117/C119 12, selected C45/C47 4, and C151 4, for 136 passed and zero failures. The optional C192 historical check failed closed during collection because `C64 artifact bundle is absent; read-only import must not regenerate it`.

The frozen scientific boundary remains: one-gluon normal-order descent and mixed-current routing are ready, while same-species contractions remain unresolved. C117 completion, rank, physical fitting, activation, merge, and push are not claimed.

All 45 scoped paths were committed at final `HEAD` with message `C406 derive C117 I2 gluon normal-order descendant`. A follow-up ordinary add encountered the external worktree index-lock permission error, but the standard commit command refreshed tracked evidence and completed the commit. No merge or push was performed.
