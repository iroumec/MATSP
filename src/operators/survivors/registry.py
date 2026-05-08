"""
Defines the protocol and enum for survivors operators.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from enum import Enum, member

from typing_extensions import Protocol

from .algorithms import replace_worst

# =============================================================================================== #
# Protocol
# =============================================================================================== #

class SurvivorsOperator(Protocol): # pylint: disable=too-few-public-methods

    """
    Class (protocol) for survivors operators.
    """

    def __call__( # pylint: disable=too-many-arguments, too-many-positional-arguments
        self,
        actual_population: list[list[int]],
        new_individuals: list[list[int]],
        number_to_replace: int,
        fitness_function: callable,
        cost_matrix: list[list[int]],
    ) -> list[list[int]]:
        ...

# =========================================================================== #
# Strategies
# =========================================================================== #

class SurvivorsStrategy(Enum):

    """
    Enum for survivors strategies.
    """

    REPLACE_WORST: SurvivorsOperator = member(replace_worst)

    def __call__( # pylint: disable=too-many-arguments, too-many-positional-arguments
        self,
        actual_population: list[list[int]],
        new_individuals: list[list[int]],
        number_to_replace: int,
        fitness_function: callable,
        cost_matrix: list[list[int]],
    ) -> list[list[int]]:
        return self.value(
            actual_population,
            new_individuals,
            number_to_replace,
            fitness_function,
            cost_matrix
        )

# =========================================================================== #
