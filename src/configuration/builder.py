"""
Configuration building implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from operators import (
    SelectionStrategy,
    CrossoverStrategy,
    MutationStrategy,
    ImprovementStrategy,
    SurvivorsStrategy,
)

from .structures import (
    Config,
    CrossoverConfig,
    ExecutionConfig,
    StopReasonsConfig,
    ImprovementConfig,
    MutationConfig,
    SelectionConfig,
    SurvivorsConfig,
)

# =============================================================================================== #
# Functions
# =============================================================================================== #

def build_config(raw: dict) -> Config:
    """
    Given a dict of paramaters, builds a configuration.
    
    Args:
        raw (dict): Raw list of parameters.
    
    Returns:
        configuration (Config): Algorithm configuration.
    """

    exec_cfg = ExecutionConfig(
        instance=raw["execution"]["instance"],
        population_size=raw["execution"]["population_size"],
        random_percentage=raw["execution"]["random_percentage"],
        executions=raw["execution"]["executions"],
        multiprocessing=raw["execution"]["multiprocessing"]
    )

    if exec_cfg.population_size <= 0:
        raise ValueError("ERROR: The population size must be greater than zero.")

    if exec_cfg.random_percentage < 0 or exec_cfg.random_percentage > 1:
        raise ValueError("ERROR: The random percentage must be a number in [0.0, 1.0].")

    if exec_cfg.executions < 1:
        raise ValueError("ERROR: The number of executions must be greater or equal than 1")

    stop_cfg = StopReasonsConfig(
        generations=raw["stop-reasons"]["generations"],
        max_generations=raw["stop-reasons"]["max_generations"],
        generations_without_improvements=raw["stop-reasons"]["generations_without_improvements"],
        max_generations_without_improvements=(
            raw["stop-reasons"]["max_generations_without_improvements"]
        ),
    )

    if not stop_cfg.generations and not stop_cfg.generations_without_improvements:
        raise ValueError("ERROR: The algorithm needs at least a stop condition.")

    sel_cfg = SelectionConfig(
        operator=SelectionStrategy[raw["selection"]["operator"]],
        selected_individuals=raw["selection"]["selected_individuals"],
        tournament_size=raw["selection"]["tournament_size"],
    )

    if sel_cfg.selected_individuals > exec_cfg.population_size:
        raise ValueError(
            "ERROR: The number of individuals selected in the selection process "
            "cannot be greater than the population size"
        )

    if raw["selection"]["operator"] == "TOURNAMENT":
        if sel_cfg.tournament_size > exec_cfg.population_size:
            raise ValueError(
                "ERROR: The number of individuals participating in the tournament process "
                "cannot be greater than the population size"
            )

    cross_cfg = CrossoverConfig(
        operator=CrossoverStrategy[raw["crossover"]["operator"]],
        probability=raw["crossover"]["probability"],
    )

    if cross_cfg.probability < 0 or cross_cfg.probability > 1:
        raise ValueError("ERROR: The crossover probability must be a number in [0.0, 1.0].")

    mut_prob = raw["mutation"]["probability"]
    if mut_prob == "Default":
        mut_prob = 1 / exec_cfg.population_size

    if mut_prob < 0 or mut_prob > 1:
        raise ValueError("ERROR: The mutation probability must be a number in [0.0, 1.0].")

    mut_cfg = MutationConfig(
        operator=MutationStrategy[raw["mutation"]["operator"]],
        probability=mut_prob,
    )

    imp_cfg = ImprovementConfig(
        operator=ImprovementStrategy[raw["improvement"]["operator"]],
        probability=raw["improvement"]["probability"],
    )

    if imp_cfg.probability < 0 or imp_cfg.probability > 1:
        raise ValueError("ERROR: The improvement (local search) must be a number in [0.0, 1.0].")

    surv_cfg = SurvivorsConfig(
        operator=SurvivorsStrategy[raw["survivors"]["operator"]],
        individuals_to_replace=raw["survivors"]["individuals_to_replace"],
    )

    if surv_cfg.individuals_to_replace > exec_cfg.population_size:
        raise ValueError(
            "ERROR: The number of individuals to replace in the survivors selection "
            "cannot be greater than the population size"
        )

    return Config(
        execution=exec_cfg,
        stop_reasons=stop_cfg,
        selection=sel_cfg,
        crossover=cross_cfg,
        mutation=mut_cfg,
        improvement=imp_cfg,
        survivors=surv_cfg,
    )

# =============================================================================================== #
