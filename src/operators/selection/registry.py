"""
Defines the protocol and enum for selection operators.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from enum import Enum, member
from typing_extensions import Protocol
from .algorithms import roulette, tournament

# =============================================================================================== #
# Protocol
# =============================================================================================== #

class SelectionOperator(Protocol): # pylint: disable=too-few-public-methods

    """
    Class (protocol) for selection operators.
    """

    def __call__(
        self,
        population: list[list[int]],
        fitness_function: callable,
        num_selections: int,
        cost_matrix: tuple[tuple[int]],
        **kwargs: any
    ) -> list[list[int]]:
        ...

# =============================================================================================== #
# Strategies
# =============================================================================================== #

class SelectionStrategy(Enum):

    """
    Enum for selection strategies.
    """

    ROULETTE: SelectionOperator = member(roulette)
    TOURNAMENT: SelectionOperator = member(tournament)

    def __call__(
        self,
        population: list[list[int]],
        fitness_function: callable,
        num_selections: int,
        cost_matrix: tuple[tuple[int]],
        **kwargs
    ):
        return self.value(
            population,
            fitness_function,
            num_selections,
            cost_matrix,
            **kwargs
        )

# =============================================================================================== #
