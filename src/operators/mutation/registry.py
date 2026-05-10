"""
Defines the protocol and enum for mutation operators.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from enum import Enum, member
from typing_extensions import Protocol

from .algorithms import swap, scramble, inversion

# =============================================================================================== #
# Protocol
# =============================================================================================== #

class MutationOperator(Protocol): # pylint: disable=too-few-public-methods

    """
    Class (protocol) for mutation operators.
    """

    def __call__(
        self,
        individual: list[int],
        probability: float
    ) -> list[int]:
        ...

# =============================================================================================== #
# Strategies
# =============================================================================================== #

class MutationStrategy(Enum):

    """
    Enum for mutation strategies.
    """

    SWAP: MutationOperator = member(swap)
    SCRAMBLE: MutationOperator = member(scramble)
    INVERSION: MutationOperator = member(inversion)

    def __call__(
        self,
        individual: list[int],
        probability: float
    ) -> list[int]:
        return self.value(individual, probability)

# =============================================================================================== #
