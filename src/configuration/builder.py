"""
Docstring
"""

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

def build_config(raw: dict) -> Config:
    """
    Given a dict of paramaters, builds a configuration.
    """

    exec_cfg = ExecutionConfig(
        instance=raw["execution"]["instance"],
        population_size=raw["execution"]["population_size"],
        random_percentage=raw["execution"]["random_percentage"],
        executions=raw["execution"]["executions"]
    )

    if exec_cfg.population_size <= 0:
        raise ValueError("ERROR: The population size must be greater than zero.")

    if exec_cfg.random_percentage < 0 or exec_cfg.random_percentage > 1:
        raise ValueError(
            "ERROR: The random percentage must be greater or equal than zero, "
            "or less or equal than one"
        )

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

    cross_cfg = CrossoverConfig(
        operator=CrossoverStrategy[raw["crossover"]["operator"]],
        probability=raw["crossover"]["probability"],
    )

    mut_prob = raw["mutation"]["probability"]
    if mut_prob == "Default":
        mut_prob = 1 / exec_cfg.population_size

    mut_cfg = MutationConfig(
        operator=MutationStrategy[raw["mutation"]["operator"]],
        probability=mut_prob,
    )

    imp_cfg = ImprovementConfig(
        operator=ImprovementStrategy[raw["improvement"]["operator"]],
        probability=raw["improvement"]["probability"],
    )

    surv_cfg = SurvivorsConfig(
        operator=SurvivorsStrategy[raw["survivors"]["operator"]],
        individuals_to_replace=raw["survivors"]["individuals_to_replace"],
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
