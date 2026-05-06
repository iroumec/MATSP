"""
Docstring for survivors.select_best
"""

from typing import List

from configuration import Config
from operators import InitializationStrategy

def select_best_individual(actual_population, fitness_function, cost_matrix) -> List[int]:
    """
    Select the best performing individual of the actual generation.

    Args:
        actual_population (list): List of current individuals in the population.
        fitness_function (function): A function that takes an individual and
            returns its fitness score.

    Returns: 
        best fitness of current population.
    """

    # Sort actual population by fitness
    actual_population_fitness_scores = [
        (ind, fitness_function(ind, cost_matrix)) for ind in actual_population
    ]
    actual_population_fitness_scores.sort(reverse=True, key=lambda x: x[1])

    return actual_population_fitness_scores[0][0]

def generate_initial_population(config: Config, cost_matrix: List[List[int]]) -> List[int]:
    """
    Docstring
    """

    population: List[int] = []

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
