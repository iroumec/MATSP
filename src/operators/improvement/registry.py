"""
Defines the protocol and enum for improvement operators.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from enum import Enum, member

from typing import List, Callable
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
        individual: List[int],
        probability: float,
        fitness_function: Callable,
        cost_matrix: List[List[int]]
    ) -> List[int]:
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
        individual: List[int],
        probability: float,
        fitness_function: Callable,
        cost_matrix: List[List[int]]
    ) -> List[int]:
        return self.value(
            individual,
            probability,
            fitness_function,
            cost_matrix
        )

# =============================================================================================== #
