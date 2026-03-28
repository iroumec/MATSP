"""
Docstring for mutation.types
"""
from enum import Enum
from typing import List
from typing_extensions import Protocol

from .algorithms.swap import swap
from .algorithms.scramble import scramble
from .algorithms.invertion import invertion

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

class MutationStrategy(Enum):
    SWAP: MutationOperator = swap
    SCRAMBLE: MutationOperator = scramble
    INVERTION: MutationOperator = invertion
    
    def __call__(
        self,
        individual: List[int],
        probability: float
    ) -> List[int]:
        return self.value(individual, probability)