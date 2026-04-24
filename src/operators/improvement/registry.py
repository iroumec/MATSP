"""
Docstring for mutation.types
"""
from enum import Enum, member

from typing import List, Callable
from typing_extensions import Protocol

from .algorithms.insertion import insertion

class ImprovementOperator(Protocol):
    """
    Docstring for MutationOperator
    """
    def __call__(
        self,
        individual: List[int],
        probability: float,
        fitness_function: Callable,
        cost_matrix: List[List[int]]
    ) -> List[int]:
        ...

class ImprovementStrategy(Enum):
    INSERTION = member(insertion)
    
    def __call__(
        self,
        individual: List[int],
        probability: float,
        fitness_function: Callable,
        cost_matrix: List[List[int]]
    ) -> List[int]:
        return self.value(individual, probability, fitness_function, cost_matrix)