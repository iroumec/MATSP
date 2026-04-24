"""
Docstring for mutation.types
"""
from enum import Enum, member

from typing import List, Callable
from typing_extensions import Protocol

from .algorithms import replace_worst

class SurvivorsOperator(Protocol):
    """
    Docstring for MutationOperator
    """
    def __call__(
        self,
        actual_population: List[List[int]],
        new_individuals: List[List[int]],
        number_to_replace: int,
        fitness_function: Callable,
        cost_matrix: List[List[int]],
    ) -> List[List[int]]:
        ...

class SurvivorsStrategy(Enum):
    """
    Enumerate that the defines the survivor strategies.
    """

    REPLACE_WORST: SurvivorsOperator = member(replace_worst)

    def __call__(
        self,
        actual_population: List[List[int]],
        new_individuals: List[List[int]],
        number_to_replace: int,
        fitness_function: Callable,
        cost_matrix: List[List[int]],
    ) -> List[List[int]]:
        return self.value(
            actual_population,
            new_individuals,
            number_to_replace,
            fitness_function,
            cost_matrix
        )