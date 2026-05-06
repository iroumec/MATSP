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
    calculate_fitness,
    select_best_individual,
    must_stop,
    calculate_average_best_fitness_through_time,
)

from data_managers import (
    load_matrix,
    AlgorithmResult,
)

from operators import (
    InitializationStrategy,
)

# =============================================================================================== #
# Functions
# =============================================================================================== #

def run_algorithm(config: Config) -> AlgorithmResult:
    """
    Given a configuration, uses its parameters to run a genetic algorithm
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

    return AlgorithmResult(
        config,
        fitness_function,
        select_best_individual(best_individuals, fitness_function, cost_matrix),
        cost_matrix,
        statistics.mean(execution_times),
        calculate_average_best_fitness_through_time(best_fitness_through_time),
    )

# =============================================================================================== #

def _execute_algorithm(
    config: Config,
    fitness_function,
    cost_matrix: List[List[int]]
):

    # ------------------------------------------------------------------------------------------- #
    # Variable definitions
    # ------------------------------------------------------------------------------------------- #

    best_fitness_through_time: list = []

    population: list = []

    # ------------------------------------------------------------------------------------------- #
    # Timer initialization
    # ------------------------------------------------------------------------------------------- #

    start_time: float = time.time()

    # ------------------------------------------------------------------------------------------- #
    # Initial population generation
    # ------------------------------------------------------------------------------------------- #

    number_of_random_generated_individuals = int(
        config.execution.random_percentage * config.execution.population_size
    )

    population += InitializationStrategy.RANDOMIZATION(
        number_of_random_generated_individuals,
        cost_matrix
    )

    number_of_heuristically_generated_individuals = (
        config.execution.population_size - number_of_random_generated_individuals
    )

    population += InitializationStrategy.NEAREST_NEIGHBOUR(
        number_of_heuristically_generated_individuals,
        cost_matrix
    )

    # ------------------------------------------------------------------------------------------- #
    # Algorithm
    # ------------------------------------------------------------------------------------------- #

    current_generation: int = 0
    last_best_fitness: float = 0.0
    generations_without_improvements: int = 0

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

        current_best_individual: List[int] = select_best_individual(
            population,
            fitness_function,
            cost_matrix
        )

        current_best_fitness: float = fitness_function(current_best_individual, cost_matrix)

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
