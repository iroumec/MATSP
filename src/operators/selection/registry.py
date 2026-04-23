"""
Docstring for mutation.types
"""
from enum import Enum
from typing import List, Callable, Any
from typing_extensions import Protocol

from .algorithms.roulette import roulette
from .algorithms.tournament import tournament

class SelectionOperator(Protocol):
    """
    Docstring for MutationOperator
    """
    def __call__(
        self,
        population: List[List[int]],
        fitness_function: Callable,
        num_selections: int,
        cost_matrix: List[List[int]],
        **kwargs: Any
    ) -> List[int]:
        ...

class SelectionStrategy(Enum):
    """
    Dcostring
    """
    ROULETTE = roulette
    TOURNAMENT = tournament

    def __call__(
        self,
        population,
        fitness_function,
        num_selections,
        cost_matrix,
        **kwargs
    ):
        return self.value(
            population,
            fitness_function,
            num_selections,
            cost_matrix,
            **kwargs
        )