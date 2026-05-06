"""
Defines the protocol and enum for crossover operators.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from typing import List
from enum import Enum, member
from typing_extensions import Protocol

from .algorithms.ox1 import ox1
from .algorithms.pmx import pmx

# =============================================================================================== #
# Protocol
# =============================================================================================== #

class CrossoverOperator(Protocol): # pylint: disable=too-few-public-methods
    """
    Class (protocol) for initialization operators.
    """
    def __call__(
        self,
        first_parent: List[int],
        second_parent: List[int],
        probability: float
    ) -> List[int]:
        ...

# =============================================================================================== #
# Strategies
# =============================================================================================== #

class CrossoverStrategy(Enum):
    """
    Enum for initialization strategies.
    """

    OX1 = member(ox1)
    PMX = member(pmx)

    def __call__(
        self,
        first_parent: List[int],
        second_parent: List[int],
        probability: float
    ) -> List[int]:
        return self.value(first_parent, second_parent, probability)

# =============================================================================================== #
