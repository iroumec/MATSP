"""
Genetic algorithm implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import time
import statistics
from typing import List

from configuration import Config
from functions import (
    must_stop,
    get_best_fitness,
    calculate_fitness,
    select_best_individual,
    calculate_average_best_fitness_through_time,
    generate_initial_population,
)

from data_managers import (
    load_matrix,
    AlgorithmResult,
)

# =============================================================================================== #
# Public Functions
# =============================================================================================== #

def run_algorithm(config: Config) -> AlgorithmResult:
    """
    Given a configuration, uses its parameters to run a genetic algorithm.
    
    Args:
        config (Config): Algorithm configuration.

    Returns:
        result (AlgorithmResult): Algorithm results.
    """

    # ------------------------------------------------------------------------------------------- #
    # Variable declarations and initializations
    # ------------------------------------------------------------------------------------------- #

    fitness_function = calculate_fitness

    best_fitness_through_time: List[float] = []

    best_individuals: List[int] = []

    execution_times: List[float] = []

    cost_matrix: List[List[int]] = load_matrix(config.execution.instance)

    # ------------------------------------------------------------------------------------------- #
    # Algorithm execution
    # ------------------------------------------------------------------------------------------- #

    for _ in range(config.execution.executions):
        current_best_individual, current_execution_time, current_best_fitness_through_time = (
            _execute_algorithm(config, fitness_function, cost_matrix)
        )
        best_individuals.append(current_best_individual)
        execution_times.append(current_execution_time)
        best_fitness_through_time.append(current_best_fitness_through_time)

    # ------------------------------------------------------------------------------------------- #
    # Output saving
    # ------------------------------------------------------------------------------------------- #

    mean, std = calculate_average_best_fitness_through_time(best_fitness_through_time)

    return AlgorithmResult(
        config,
        fitness_function,
        select_best_individual(best_individuals, fitness_function, cost_matrix),
        cost_matrix,
        statistics.mean(execution_times),
        mean,
        std,
    )

# =============================================================================================== #
# Private Functions
# =============================================================================================== #

def _execute_algorithm(
    config: Config,
    fitness_function,
    cost_matrix: List[List[int]]
):

    # ------------------------------------------------------------------------------------------- #
    # Variable declaration and initializations
    # ------------------------------------------------------------------------------------------- #

    current_generation: int = 0
    last_best_fitness: float = 0.0
    best_fitness_through_time: list = []
    generations_without_improvements: int = 0

    # ------------------------------------------------------------------------------------------- #
    # Initial population generation
    # ------------------------------------------------------------------------------------------- #

    population: List[int] = generate_initial_population(config, cost_matrix)

    # ------------------------------------------------------------------------------------------- #
    # Timer initialization
    # ------------------------------------------------------------------------------------------- #

    start_time: float = time.time()

    # ------------------------------------------------------------------------------------------- #
    # Algorithm
    # ------------------------------------------------------------------------------------------- #

    while not must_stop(current_generation, generations_without_improvements, config):

        # --------------------------------------------------------------------------------------- #
        # Parents Selection
        # --------------------------------------------------------------------------------------- #

        parents = config.selection.operator(
            population=population,
            fitness_function=fitness_function,
            num_selections=config.selection.selected_individuals,
            cost_matrix=cost_matrix,
            tournament_size=config.selection.tournament_size,
            # Only used if the selection algorithm is tournament.
        )

        # --------------------------------------------------------------------------------------- #
        # Crossover
        # --------------------------------------------------------------------------------------- #

        children = []

        for i in range(0, len(parents) - 1, 2):

            # The parents cannot be equals, so endogamy (which is translated to prematured
            # convergence) is avoided and the population isn't filled with all equals individuals.
            if parents[i] != parents[i+1]:

                children += config.crossover.operator(
                    parents[i],
                    parents[i+1],
                    config.crossover.probability
                )

        # --------------------------------------------------------------------------------------- #
        # Mutation
        # --------------------------------------------------------------------------------------- #

        children = [
            config.mutation.operator(child, config.mutation.probability)
            for child in children
        ]

        # --------------------------------------------------------------------------------------- #
        # Local search
        # --------------------------------------------------------------------------------------- #

        children = [config.improvement.operator(
            child,
            config.improvement.probability,
            fitness_function,
            cost_matrix
        ) for child in children]

        # --------------------------------------------------------------------------------------- #
        # Survivors selection
        # --------------------------------------------------------------------------------------- #

        population = config.survivors.operator(
            population,
            children,
            config.survivors.individuals_to_replace,
            fitness_function,
            cost_matrix
        )

        # --------------------------------------------------------------------------------------- #
        # Selecting the best solution of the current generation
        # --------------------------------------------------------------------------------------- #

        current_best_fitness: float = get_best_fitness(population, fitness_function, cost_matrix)

        best_fitness_through_time.append(current_best_fitness)

        if last_best_fitness == current_best_fitness:
            generations_without_improvements += 1
        else:
            generations_without_improvements = 0
            last_best_fitness = current_best_fitness

        # --------------------------------------------------------------------------------------- #
        # Increase of generation
        # --------------------------------------------------------------------------------------- #

        current_generation += 1

    # ------------------------------------------------------------------------------------------- #
    # Timer finalization
    # ------------------------------------------------------------------------------------------- #

    end_time: float = time.time()
    execution_time: float = end_time - start_time

    # ------------------------------------------------------------------------------------------- #
    # Best individual selection
    # ------------------------------------------------------------------------------------------- #

    best_individual = select_best_individual(population, fitness_function, cost_matrix)

    # ------------------------------------------------------------------------------------------- #
    # Return
    # ------------------------------------------------------------------------------------------- #

    return best_individual, execution_time, best_fitness_through_time

# =============================================================================================== #
