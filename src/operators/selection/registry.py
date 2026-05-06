"""
Defines the protocol and enum for selection operators.
"""
from enum import Enum, member
from typing import List, Callable, Any
from typing_extensions import Protocol
from .algorithms import (
    roulette,
    tournament
)

class SelectionOperator(Protocol):
    """
    Class (protocol) for selection operators.
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
    Enum for selection strategies.
    """
    ROULETTE: SelectionOperator = member(roulette)
    TOURNAMENT: SelectionOperator = member(tournament)

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
