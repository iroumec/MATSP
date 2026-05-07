"""
Defines the protocol and enum for survivors operators.
"""
from enum import Enum, member

from typing import List, Callable
from typing_extensions import Protocol

from .algorithms import replace_worst

# =========================================================================== #
# Operator
# =========================================================================== #

class SurvivorsOperator(Protocol):
    """
    Class (protocol) for survivors operators.
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

# =========================================================================== #
# Strategies
# =========================================================================== #

class SurvivorsStrategy(Enum):
    """
    Enum for survivors strategies.
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
