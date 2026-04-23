"""
Docstring
"""
from dataclasses import dataclass

from operators import (
    SelectionStrategy,
    CrossoverStrategy,
    MutationStrategy,
    ImprovementStrategy,
    SurvivorsStrategy,
)

@dataclass
class ExecutionConfig:
    """
    Docstring
    """
    population_size: int
    random_percentage: float
    max_generations: int


@dataclass
class SelectionConfig:
    """
    Docstring
    """
    operator: SelectionStrategy
    selected_individuals: int
    tournament_size: int

@dataclass
class CrossoverConfig:
    """
    Docstring
    """
    operator: CrossoverStrategy
    probability: float

@dataclass
class MutationConfig:
    """
    Docstring
    """
    operator: MutationStrategy
    probability: float

@dataclass
class ImprovementConfig:
    """
    Docstring
    """
    operator: ImprovementStrategy
    probability: float

@dataclass
class SurvivorsConfig:
    """
    Docstring
    """
    operator: SurvivorsStrategy
    individuals_to_replace: int

@dataclass
class Config:
    """
    Docstring
    """
    execution: ExecutionConfig
    selection: SelectionConfig
    crossover: CrossoverConfig
    mutation: MutationConfig
    improvement: ImprovementConfig
    survivors: SurvivorsConfig