"""
Docstring for mutation.types
"""
from enum import Enum
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
    OX1: CrossoverOperator = ox1
    PMX: CrossoverOperator = pmx
    
    def __call__(
        self,
        first_parent: List[int],
        second_parent: List[int],
        probability: float
    ) -> List[int]:
        self.value(first_parent, second_parent, probability)
