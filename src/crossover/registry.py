from enum import Enum
from typing import Dict
from crossover.types import CrossoverOperator

from .algorithms.ox1 import ox1
from .algorithms.pmx import pmx

# Crossover Strategies.
class CrossoverStrategy(Enum):
    OX1 = "ox1"
    PMX = "pmx"

# Registry.
_CROSSOVER_REGISTRY: Dict[CrossoverStrategy, CrossoverOperator] = {
    CrossoverStrategy.OX1: ox1,
    CrossoverStrategy.PMX: pmx,
}

# Returns a operator given a strategy.
def get_crossover_operator(strategy: CrossoverStrategy) -> CrossoverOperator:
    if strategy not in _CROSSOVER_REGISTRY:
        raise ValueError(f"El operador {strategy} no está registrado.")
    return _CROSSOVER_REGISTRY[strategy]