from enum import Enum
from typing import Dict
from mutation.types import MutationOperator

from .algorithms.swap import swap
from .algorithms.scramble import scramble
from .algorithms.invertion import invertion

# Mutation Strategies.
class MutationStrategy(Enum):
    SWAP = "swap"
    SCRAMBLE = "scramble"
    INVERTION = "invertion"

# Registry.
_MUTATION_REGISTRY: Dict[MutationStrategy, MutationOperator] = {
    MutationStrategy.SWAP: swap,
    MutationStrategy.SCRAMBLE: scramble,
    MutationStrategy.INVERTION: invertion,
}

# Returns a mutation operator given a mutation registry.
def get_mutation_operator(strategy: MutationStrategy) -> MutationOperator:
    if strategy not in _MUTATION_REGISTRY:
        raise ValueError(f"El operador {strategy} no está registrado.")
    return _MUTATION_REGISTRY[strategy]