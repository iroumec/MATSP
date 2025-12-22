"""
Docstring for mutation.types
"""
from typing import List
from typing_extensions import Protocol

class MutationOperator(Protocol):
    """
    Docstring for MutationOperator
    """
    def __call__(
        self,
        individual: List[int],
        probability: float
    ) -> List[int]:
        ...
