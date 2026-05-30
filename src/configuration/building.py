"""
Configuration building implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import itertools
from pathlib import Path

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

from data_loaders import load_config

# =============================================================================================== #
# Constants
# =============================================================================================== #

REQUIRED_SECTIONS = {
    "execution", "stop-reasons", "selection",
    "crossover", "mutation", "improvement", "survivors"
}

# Rules controlling whether a parameter actively participates in the
# combinatorial expansion process.
#
# Key format:
#     "<section>.<parameter>"
#
# Rule semantics:
#     True  -> parameter expands combinations normally.
#     False -> parameter keeps only its first/default value and does not
#              increase the number of generated configurations.
#
# This mechanism prevents the creation of redundant configurations while
# preserving a consistent configuration structure.
#
# Example:
#     If the selection operator is not TOURNAMENT, tournament_size keeps
#     only its first value and does not generate extra combinations.
DEPENDENCY_RULES = {
    "selection.tournament_size": lambda config: (
        config["selection"]["operator"] == "TOURNAMENT"
    ),

    "stop-reasons.max_generations": lambda config: (
        config["stop-reasons"]["generations"]
    ),

    "stop-reasons.max_generations_without_improvements": lambda config: (
        config["stop-reasons"]["generations_without_improvements"]
    ),
}

# =============================================================================================== #
# Functions
# =============================================================================================== #

def build_configurations(path: Path) -> list[Config]:

    """
    Builds a list of unique valid configurations from a file or a directory.
    If a configuration field contains a list of values, it generates the 
    cartesian product of all possible combinations (Grid Search).

    Args:
        path (Path): Path to a YAML file or a directory containing YAML files.

    Returns:
        configurations (List[Config]): List of unique configuration objects.
    """

    configurations: list[Config] = []

    # Just one file.
    if path.is_file():
        raw_data = load_config(str(path))
        configurations.extend(_expand_raw_config(raw_data))

    # A directory with at least one YAML file.
    elif path.is_dir():
        files = sorted([
            p for p in path.iterdir()
            if p.suffix in (".yml", ".yaml")
        ])

        if not files:
            raise ValueError(f"ERROR: No .yml or .yaml files found in {path}")

        for file in files:
            raw_data = load_config(str(file))
            configurations.extend(_expand_raw_config(raw_data))
    else:
        raise ValueError(f"ERROR: Invalid path {path}")

    return configurations

# =============================================================================================== #

def _expand_raw_config(raw_data: dict[str, any]) -> list[Config]:

    """
    Helper function to expand YAML lists into unique valid Config objects.
    """

    missing = REQUIRED_SECTIONS - set(raw_data.keys())
    if missing:
        raise ValueError(f"ERROR: Missing sections in YAML: {missing}")

    # Normalizes everything to lists and removes duplicates.
    options_map: dict[str, dict[str, list[any]]] = {}

    for section, parameters in raw_data.items():
        options_map[section] = {}
        for param_name, param_value in parameters.items():
            if isinstance(param_value, list):
                # Removes duplicates like ["SWAP", "SWAP"].
                options_map[section][param_name] = list(dict.fromkeys(param_value))
            else:
                options_map[section][param_name] = [param_value]

    # Generates all combinations per section.
    sections = options_map.keys()
    options_per_section = []
    for section in sections:
        section_combos = _generate_section_combinations(
            section,
            options_map[section]
        )
        options_per_section.append(section_combos)

    # Generates global combinations and builds them.
    expanded_configs: list[Config] = []
    for global_combination in itertools.product(*options_per_section):
        final_raw = dict(zip(sections, global_combination))
        expanded_configs.append(_build_config(final_raw))

    return expanded_configs

# =============================================================================================== #

def _generate_section_combinations(
    section: str,
    parameters: dict[str, list[any]]
) -> list[dict[str, any]]:

    """
    Generates all valid parameter combinations for a configuration section.

    Parameters whose dependency rules are active participate normally in the
    cartesian expansion process.

    Parameters whose dependency rules are inactive do not expand the number
    of generated combinations. Instead, they are assigned only their first
    available value, which acts as a default/fallback value.

    This prevents the generation of redundant configurations while preserving
    a consistent structure across all generated configurations.

    Example:
        operator = [TOURNAMENT, ROULETTE]
        tournament_size = [3, 5, 10]

    Generates:
        TOURNAMENT + 3
        TOURNAMENT + 5
        TOURNAMENT + 10
        ROULETTE + 3

    instead of:
        ROULETTE + 3
        ROULETTE + 5
        ROULETTE + 10

    Args:
        section (str):
            Name of the configuration section being expanded
            (e.g. "selection", "stop-reasons").

        parameters (dict[str, list[any]]):
            Mapping between parameter names and their possible values.

    Returns:
        list[dict[str, any]]:
            List of valid parameter combinations for the section.
    """

    combinations = [{}]

    for parameter, values in parameters.items():

        new_combinations = []

        for current_config in combinations:

            partial_config = {
                section: current_config
            }

            parameter_is_active = _is_parameter_active(
                section,
                parameter,
                partial_config
            )

            # ACTIVE -> Parameter is expanded.
            if parameter_is_active:

                for value in values:
                    new_config = current_config.copy()
                    new_config[parameter] = value
                    new_combinations.append(new_config)

            # INACTIVE -> Keeps parameter with ONLY first/default value.
            # Does not expand combinations.
            else:

                new_config = current_config.copy()
                new_config[parameter] = values[0]
                new_combinations.append(new_config)

        combinations = new_combinations

    return combinations

# =============================================================================================== #

def _is_parameter_active(
    section: str,
    parameter: str,
    partial_config: dict[str, any]
) -> bool:

    """
    Determines whether a parameter should actively participate in the
    combinatorial expansion process.

    If a dependency rule exists for the parameter, the corresponding rule
    is evaluated using the current partial configuration.

    If no dependency rule exists, the parameter is considered active by
    default.

    Active parameters:
        - participate in cartesian expansion;
        - generate multiple configurations.

    Inactive parameters:
        - do not expand combinations;
        - keep only their first/default value.

    Args:
        section (str):
            Name of the configuration section containing the parameter.

        parameter (str):
            Name of the parameter to evaluate.

        partial_config (dict[str, any]):
            Partial configuration built so far for the current section.

    Returns:
        bool:
            True if the parameter should expand combinations,
            False otherwise.
    """

    rule_key = f"{section}.{parameter}"

    if rule_key not in DEPENDENCY_RULES:
        return True

    return DEPENDENCY_RULES[rule_key](partial_config)

# =============================================================================================== #

def _build_config(raw: dict) -> Config:

    """
    Given a dict of parameters, builds a configuration.
    
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

    if sel_cfg.selected_individuals % 2 != 0:
        raise ValueError(
            "ERROR: 'selected_individuals' must be an even number. "
            "The crossover operator pairs parents in groups of two; an odd number "
            "leaves the last parent without a partner and excludes it from crossover."
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
