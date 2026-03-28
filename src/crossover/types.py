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
        first_parent: List[int],
        second_parent: List[int],
        probability: float
    ) -> List[int]:
        ...
