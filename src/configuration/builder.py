"""
Docstring
"""

from .parser import parse_enum
from .structures import (
    Config,
    CrossoverConfig,
    CrossoverStrategy,
    ExecutionConfig,
    ImprovementConfig,
    ImprovementStrategy,
    MutationConfig, MutationStrategy,
    SelectionConfig,
    SelectionStrategy,
    SurvivorsConfig,
    SurvivorsStrategy
)

def build_config(raw: dict) -> Config:
    
    """
    Docstring
    """
    
    exec_cfg = ExecutionConfig(
        population_size=raw["execution"]["population_size"],
        random_percentage=raw["execution"]["percentage_of_random_generated_individuals"],
        max_generations=raw["execution"]["max_generations"],
    )

    sel_cfg = SelectionConfig(
        operator=parse_enum(SelectionStrategy, raw["selection"]["operator"]),
        selected_individuals=raw["selection"]["selected_individuals"],
        tournament_size=raw["selection"]["tournament_size"],
    )

    cross_cfg = CrossoverConfig(
        operator=parse_enum(CrossoverStrategy, raw["crossover"]["operator"]),
        probability=raw["crossover"]["probability"],
    )

    mut_prob = raw["mutation"]["probability"]
    if mut_prob == "Default":
        mut_prob = 1 / exec_cfg.population_size

    mut_cfg = MutationConfig(
        operator=parse_enum(MutationStrategy, raw["mutation"]["operator"]),
        probability=mut_prob,
    )

    imp_cfg = ImprovementConfig(
        operator=parse_enum(ImprovementStrategy, raw["improvement"]["operator"]),
        probability=raw["improvement"]["probability"],
    )

    surv_cfg = SurvivorsConfig(
        operator=parse_enum(SurvivorsStrategy, raw["survivors"]["operator"]),
        individuals_to_replace=raw["survivors"]["individuals_to_replace"],
    )

    return Config(
        execution=exec_cfg,
        selection=sel_cfg,
        crossover=cross_cfg,
        mutation=mut_cfg,
        improvement=imp_cfg,
        survivors=surv_cfg,
    )