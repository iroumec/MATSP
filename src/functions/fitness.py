"""
Fitness function implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from typing import List, Tuple

from functions import select_best_individual

# =============================================================================================== #
# Functions
# =============================================================================================== #

def calculate_fitness(individual: tuple, cost_matrix):
    """
    Given an individual (sequence of n locations), calculates
    it fitness, which is defined as 1/travel_cost, where the travel cost
    is defined as the cost from travelling from the location 0 to the
    location 1, plus the cost from travelling from the location 1 to the
    location 2, ..., plus the cost from travelling from the location n-1
    to the location n.
    
    A sequence whose cost is smaller will have a grater fitness.

    Args:
        individual (list): Sequence of locations.
        cost_matrix: Matrix containing the costs from travelling from one city
            to another.

    Returns:
        float: Updated population after replacement.
    """

    number_of_cities = len(individual)

    travel_cost = 0

    for city in range(number_of_cities - 1):

        travel_cost += cost_matrix[individual[city]][individual[city+1]]

    travel_cost += cost_matrix[individual[number_of_cities - 1]][individual[0]]

    return 1/travel_cost

# =============================================================================================== #

def get_best_fitness(
    population: List[int],
    fitness_function: callable,
    cost_matrix: List[List[int]]
) -> float:
    """
    Docstring.
    """

    current_best_individual: List[int] = select_best_individual(
        population,
        fitness_function,
        cost_matrix
    )

    return fitness_function(current_best_individual, cost_matrix)

# =============================================================================================== #

def calculate_average_best_fitness_through_time(
    best_fitness_through_time: List[List[float]]
) -> Tuple[List[float], List[float]]:
    """
    
    The `best_fitness_through_time` saves, for each execution, the best fitness for
    each generation.
    
    If not all executions run the same amount of generations, this could cause valleys
    in the graphs. For this reason, the algorithm applies a padding, which fill
    all the next values with the best previous one.
    
    De esta forma, la curva no presenta valles. Visualmente, lo que se ve es un
    "estancamiento" del fitness. This is an standar criteria in genetic algorithms.
    """

    if not best_fitness_through_time:
        return [], []

    max_generations = max(len(exec_) for exec_ in best_fitness_through_time)

    sums = [0.0] * max_generations
    sums_sq = [0.0] * max_generations

    for execution in best_fitness_through_time:
        last_value = execution[-1]

        for i in range(max_generations):
            value = execution[i] if i < len(execution) else last_value
            sums[i] += value
            sums_sq[i] += value * value

    n_runs = len(best_fitness_through_time)

    means = [s / n_runs for s in sums]

    stds = [
        max(0.0, (sums_sq[i] / n_runs) - (means[i] ** 2)) ** 0.5
        for i in range(max_generations)
    ]

    return means, stds

# =============================================================================================== #
