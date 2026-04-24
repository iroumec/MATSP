"""
Docstring for mutation.types
"""
from enum import Enum, member
from typing import List
from typing_extensions import Protocol

from .algorithms.ox1 import ox1
from .algorithms.pmx import pmx

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

class CrossoverStrategy(Enum):
    OX1 = member(ox1)
    PMX = member(pmx)
    
    def __call__(
        self,
        first_parent: List[int],
        second_parent: List[int],
        probability: float
    ) -> List[int]:
        return self.value(first_parent, second_parent, probability)
