"""
Docstring for mutation.types
"""
from enum import Enum, member

from typing import List
from typing_extensions import Protocol

from .algorithms.randomization import randomization
from .algorithms.nearest_neighbour import nearest_neighbour

class InitializationOperator(Protocol):
    """
    Docstring for MutationOperator
    """
    def __call__(
        self,
        number_of_inidivuals_to_generate: int,
        cost_matrix: List[List[int]]
    ) -> List[int]:
        ...

class InitializationStrategy(Enum):
    RANDOMIZATION = member(randomization)
    NEAREST_NEIGHBOUR = member(nearest_neighbour)
    
    def __call__(
        self,
        number_of_inidivuals_to_generate: int,
        cost_matrix: List[List[int]]
    ) -> List[int]:
        return self.value(number_of_inidivuals_to_generate, cost_matrix)