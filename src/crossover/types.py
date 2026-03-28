"""
Docstring for mutation.types
"""
from typing import List
from typing_extensions import Protocol

class CrossoverOperator(Protocol):
    """
    Docstring for MutationOperator
    """
    def __call__(
        self,
        individual: List[int],
        probability: float
    ) -> List[int]:
        ...
