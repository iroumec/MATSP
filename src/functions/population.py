"""
Population general functions implementations.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from configuration import Config
from operators import InitializationStrategy

# =============================================================================================== #
# Functions
# =============================================================================================== #

def select_best_individual(
    actual_population: list[int],
    fitness_function: callable,
    cost_matrix: tuple[tuple[int]]
) -> list[int]:
    """
    Selects the best performing individual in the population.

    Args:
        actual_population (list[int]): Population.
        fitness_function (callable): A function that takes an individual and
            returns its fitness score.
        cost_matrix (tuple[tuple[int]]): Necessary to calculate the fitness.

    Returns: 
        best_individual (list[int]): Best individual in the population.
    """

    # Sort actual population by fitness
    actual_population_fitness_scores = [
        (ind, fitness_function(ind, cost_matrix)) for ind in actual_population
    ]
    actual_population_fitness_scores.sort(reverse=True, key=lambda x: x[1])

    return actual_population_fitness_scores[0][0]

# =============================================================================================== #

def generate_initial_population(config: Config, cost_matrix: tuple[tuple[int]]) -> list[int]:
    """
    Generates an initial population according to the configuration parameters.
    
    Args:
        config (Config): Configuration parameters.
        cost_matrix (tuple[tuple[int]]): Cost matrix.

    Returns:
        initial_population (list[int]): Initial population.
    """

    population: list[int] = []

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

    return population

# =============================================================================================== #
