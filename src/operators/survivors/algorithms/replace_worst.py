"""
"REPLACE_WORST" survivors operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import heapq

# =============================================================================================== #
# Functions
# =============================================================================================== #

def replace_worst(
    actual_population: list[list[int]],
    new_individuals: list[list[int]],
    number_to_replace: int,
    fitness_function: callable,
    cost_matrix: tuple[tuple[int]],
) -> list[list[int]]:

    """
    Replaces the worst-performing individuals in the actual_population with the best-performing
    individuals in new_individuals.

    Args:
        actual_population (list[list[int]]): List of current individuals in the population.
        new_individuals (list[list[int]]): List of new individuals to be added to the population.
        number_to_replace (int): Number of worst individuals to replace.
        fitness_function (callable): A function that takes an individual and returns its fitness
            score.
        cost_matrix (list[list[int]]): Cost matrix. Required for the fitness function.

    Returns:
        updated_population (list[list[int]]): Updated population after replacement.
    """

    # Limits the number of individuals to replace to the available new individuals.
    number_to_replace = min(len(new_individuals), number_to_replace)

    # Validations.
    if number_to_replace == 0:
        return actual_population

    if number_to_replace > len(actual_population):
        raise ValueError("Cannot replace more individuals than the population size.")

    # Evaluates fitness once for the actual population.
    actual_population_fitness = [
        (ind, fitness_function(ind, cost_matrix)) for ind in actual_population
    ]

    # Evaluates fitness once for the new individuals.
    new_individuals_fitness = [
        (ind, fitness_function(ind, cost_matrix)) for ind in new_individuals
    ]

    # Selects the worst individuals to remove from the current population.
    worst_current = heapq.nsmallest(
        number_to_replace,
        actual_population_fitness,
        key=lambda x: x[1]
    )

    # Selects the best individuals to add from the new candidates.
    best_new = heapq.nlargest(number_to_replace, new_individuals_fitness, key=lambda x: x[1])

    # Keeps all individuals except the worst ones selected for replacement.
    worst_indices = {id(ind) for ind, _ in worst_current}
    individuals_to_keep = [ind for ind in actual_population if id(ind) not in worst_indices]

    # Extracts individuals to add.
    individuals_to_add = [ind for ind, _ in best_new]

    # Combines both groups to form the updated population.
    updated_population = individuals_to_keep + individuals_to_add

    return updated_population

# =============================================================================================== #
