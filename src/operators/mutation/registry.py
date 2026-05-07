"""
Defines the protocol and enum for mutation operators.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from enum import Enum, member
from typing import List
from typing_extensions import Protocol

from .algorithms import swap, scramble, invertion

# =============================================================================================== #
# Protocol
# =============================================================================================== #

class MutationOperator(Protocol):
    """
    Class (protocol) for mutation operators.
    """
    def __call__(
        self,
        individual: List[int],
        probability: float
    ) -> List[int]:
        ...

# =============================================================================================== #
# Strategies
# =============================================================================================== #

class MutationStrategy(Enum): # pylint: disable=too-few-public-methods
    """
    Enum for mutation strategies.
    """
    SWAP: MutationOperator = member(swap)
    SCRAMBLE: MutationOperator = member(scramble)
    INVERTION: MutationOperator = member(invertion)

    def __call__(
        self,
        individual: List[int],
        probability: float
    ) -> List[int]:
        return self.value(individual, probability)

# =============================================================================================== #
