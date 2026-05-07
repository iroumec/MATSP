"""
Configuration dataclasses.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from dataclasses import dataclass

from operators import (
    SelectionStrategy,
    CrossoverStrategy,
    MutationStrategy,
    ImprovementStrategy,
    SurvivorsStrategy,
)

# =============================================================================================== #
# Dataclasses
# =============================================================================================== #

@dataclass
class ExecutionConfig:
    """
    Dataclass for execution configuration parameters.
    """
    instance: str
    population_size: int
    random_percentage: float
    executions: int

# =============================================================================================== #

@dataclass
class StopReasonsConfig:
    """
    Dataclass for stop reasons configuration parameters.
    """
    generations: bool
    max_generations: int
    generations_without_improvements: bool
    max_generations_without_improvements: int

# =============================================================================================== #

@dataclass
class SelectionConfig:
    """
    Dataclass for selection configuration parameters.
    """
    operator: SelectionStrategy
    selected_individuals: int
    tournament_size: int

# =============================================================================================== #

@dataclass
class CrossoverConfig:
    """
    Dataclass for crossover configuration parameters.
    """
    operator: CrossoverStrategy
    probability: float

# =============================================================================================== #

@dataclass
class MutationConfig:
    """
    Dataclass for mutation configuration parameters.
    """
    operator: MutationStrategy
    probability: float

# =============================================================================================== #

@dataclass
class ImprovementConfig:
    """
    Dataclass for improvement configuration parameters.
    """
    operator: ImprovementStrategy
    probability: float

# =============================================================================================== #

@dataclass
class SurvivorsConfig:
    """
    Dataclass for survivors configuration parameters.
    """
    operator: SurvivorsStrategy
    individuals_to_replace: int

# =============================================================================================== #

@dataclass
class Config:
    """
    Dataclass for all configuration parameters.
    """
    execution: ExecutionConfig
    stop_reasons: StopReasonsConfig
    selection: SelectionConfig
    crossover: CrossoverConfig
    mutation: MutationConfig
    improvement: ImprovementConfig
    survivors: SurvivorsConfig

# =============================================================================================== #
