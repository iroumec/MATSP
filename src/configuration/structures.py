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
    instance: str
    population_size: int
    random_percentage: float

@dataclass
class StopReasonsConfig:
    """
    Docstring
    """
    generations: bool
    max_generations: int
    generations_without_improvements: bool
    max_generations_without_improvements: int


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
    stop_reasons: StopReasonsConfig
    selection: SelectionConfig
    crossover: CrossoverConfig
    mutation: MutationConfig
    improvement: ImprovementConfig
    survivors: SurvivorsConfig
