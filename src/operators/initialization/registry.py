"""
Defines the protocol and enum for initialization operators.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from enum import Enum, member

from typing_extensions import Protocol

from .algorithms import randomization, nearest_neighbour

# =============================================================================================== #
# Protocol
# =============================================================================================== #

class InitializationOperator(Protocol): # pylint: disable=too-few-public-methods

    """
    Class (protocol) for initialization operators.
    """

    def __call__(
        self,
        number_of_inidivuals_to_generate: int,
        cost_matrix: list[list[int]]
    ) -> list[int]:
        ...

# =============================================================================================== #
# Strategies
# =============================================================================================== #

class InitializationStrategy(Enum):

    """
    Enum for initialization strategies.
    """

    RANDOMIZATION = member(randomization)
    NEAREST_NEIGHBOUR = member(nearest_neighbour)

    def __call__(
        self,
        number_of_inidivuals_to_generate: int,
        cost_matrix: list[list[int]]
    ) -> list[int]:
        return self.value(number_of_inidivuals_to_generate, cost_matrix)

# =============================================================================================== #
