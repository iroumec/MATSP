"""
Fitness function implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from functions import calculate_cost

# =============================================================================================== #
# Functions
# =============================================================================================== #

def calculate_fitness(individual: list[int], cost_matrix: tuple[tuple[int]]) -> float:
    """
    Given an individual (sequence of n locations), calculates
    it fitness, which is defined as 1/travel_cost, where the travel cost
    is defined as the cost from travelling from the location 0 to the
    location 1, plus the cost from travelling from the location 1 to the
    location 2, ..., plus the cost from travelling from the location n-1
    to the location n.
    
    A sequence whose cost is smaller will have a grater fitness.

    Args:
        individual (list[list[int]]): Sequence of locations.
        cost_matrix (tuple[tuple[int]]): Matrix containing the costs from travelling from one city
            to another.

    Returns:
        fitness_value (float): Updated population after replacement.
    """

    return 1/calculate_cost(individual, cost_matrix)

# =============================================================================================== #

def get_best_fitness(
    population: list[int],
    fitness_function: callable,
    cost_matrix: tuple[tuple[int]]
) -> float:

    """
    Given a population, it looks for the best fitness.

    Args:
        population (list[int]): Population to look for.
        fitness_function (callable): Fitness function used to calculate the fitness of each
            individual in the population.
        cost_matrix (tuple[tuple[int]]): Cost matrix, necessary to calculate the fitness.

    Returns:
        best_fitness (float): The highest fitness value found in the population.
    """

    return max(fitness_function(ind, cost_matrix) for ind in population)

# =============================================================================================== #

def calculate_average_best_fitness_through_time(
    best_fitness_through_time: list[list[float]]
) -> tuple[list[float], list[float]]:

    """
    The `best_fitness_through_time` saves, for each execution, the best fitness for
    each generation.
    
    If not all executions run the same amount of generations, this could cause valleys
    in the graphs. For this reason, the algorithm applies a padding, which fill
    all the next values with the best previous one.
    
    In this way, the curve doesn't have valleys. Visually, it's seen a fitness
    stagnation. This is an standar criteria in genetic algorithms.
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
