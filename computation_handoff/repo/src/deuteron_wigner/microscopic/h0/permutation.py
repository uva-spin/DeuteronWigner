"""Canonical fermion wedge and exact finite antisymmetrizer."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations

import numpy as np


def permutation_sign(items: tuple[int,...]) -> int:
    inversions=sum(items[i]>items[j] for i in range(len(items)) for j in range(i+1,len(items)))
    return -1 if inversions%2 else 1


@dataclass(frozen=True)
class PermutationBasis:
    particle_count: int
    convention_id: str = "CANONICAL_CREATION_WEDGE_LEXICOGRAPHIC"

    @property
    def permutations(self): return tuple(permutations(range(self.particle_count)))

    def exchange_sign(self, left: int, right: int) -> int:
        if left==right: return 1
        return -1

    def antisymmetrizer(self) -> np.ndarray:
        group=self.permutations
        matrix=np.zeros((len(group),len(group)))
        # Regular-representation projector A=sum sign(g) R_g / n!.
        inverse={p:i for i,p in enumerate(group)}
        for col,p in enumerate(group):
            for g in group:
                composed=tuple(p[g[i]] for i in range(self.particle_count))
                matrix[inverse[composed],col]+=permutation_sign(g)/len(group)
        return matrix

    def residuals(self) -> dict[str,float]:
        A=self.antisymmetrizer()
        return {
            "idempotence":float(np.max(np.abs(A@A-A))),
            "hermiticity":float(np.max(np.abs(A-A.T.conj()))),
        }
