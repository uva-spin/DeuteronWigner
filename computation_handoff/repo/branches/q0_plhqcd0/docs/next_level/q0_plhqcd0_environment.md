# Q0/PLHQCD0 environment

Q0 uses a separate Python 3.11 environment at `.venv311`. The existing
project Python 3.9 environment is not modified.

```bash
conda create -p .venv311 python=3.11 pip -y
.venv311/bin/python -m pip install -e '.[analysis]'
.venv311/bin/python -m pip install \
  'PennyLane==0.38.0' \
  'PennyLane-Lightning==0.38.0' \
  'autoray==0.6.12'
```

The primary exact oracle uses `lightning.qubit`, `shots=None`, and
`complex128`. The production compiler remains sparse and does not construct a
generic full Pauli decomposition.
