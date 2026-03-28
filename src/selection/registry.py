from enum import Enum
from typing import Dict
from .types import SelectionOperator

from .algorithms.roulette import roulette
from .algorithms.tournament import tournament

# Strategies.
class SelectionStrategy(Enum):
    ROULETTE = "roulette"
    TOURNAMENT = "tournament"

# Registry.
_SELECTION_REGISTRY: Dict[SelectionStrategy, SelectionOperator] = {
    SelectionStrategy.ROULETTE: roulette,
    SelectionStrategy.TOURNAMENT: tournament,
}

# Returns a mutation operator given a mutation registry.
def get_operator(strategy: SelectionStrategy) -> SelectionOperator:
    if strategy not in _SELECTION_REGISTRY:
        raise ValueError(f"El operador {strategy} no está registrado.")
    return _SELECTION_REGISTRY[strategy]