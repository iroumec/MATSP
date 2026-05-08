"""
Defines the protocol and enum for improvement operators.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from enum import Enum, member

from typing_extensions import Protocol

from .algorithms import insertion

# =============================================================================================== #
# Protocol
# =============================================================================================== #

class ImprovementOperator(Protocol): # pylint: disable=too-few-public-methods

    """
    Class (protocol) for improvement operators.
    """

    def __call__(
        self,
        individual: list[int],
        probability: float,
        fitness_function: callable,
        cost_matrix: list[list[int]]
    ) -> list[int]:
        ...

# =============================================================================================== #
# Strategies
# =============================================================================================== #

class ImprovementStrategy(Enum):

    """
    Enum for improvement strategies.
    """

    INSERTION = member(insertion)

    def __call__(
        self,
        individual: list[int],
        probability: float,
        fitness_function: callable,
        cost_matrix: list[list[int]]
    ) -> list[int]:
        return self.value(
            individual,
            probability,
            fitness_function,
            cost_matrix
        )

# =============================================================================================== #
