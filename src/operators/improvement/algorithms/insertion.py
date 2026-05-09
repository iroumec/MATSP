"""
"INSERTION" improvement (local search) operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Functions
# =============================================================================================== #

def insertion(
    individual: list[int],
    probability: float,
    fitness_function: callable,
    cost_matrix: tuple[tuple[int]]
) -> list[int]:

    """
    Randomly, selects a gen in the cromosome and tries to place it in another position.
    
    Args:
        individual (list[int]): Individual to which apply the operator.
        probability (float): Probability of applying the operator.
        fitness_function (callable): Function that allows to calculate an individual fitness.
        cost_matrix (tuple[tuple[int]]): Cost matrix. Required for the fitness function.
    
    Returns:
        invidual (list[int]): Individual post operator aplication. If the expected probability
            was not achieved, it's the same as the indiviudal in the argument.
    """

    best_individual = list(individual)

    # Applies the operator with the given probability.
    if random.random() < probability:

        best_fitness = fitness_function(best_individual, cost_matrix)

        number_of_elements = len(best_individual)

        # Removes a random element to reinsert it in the best position.
        index_to_remove = random.randint(0, number_of_elements - 1)
        element_removed = best_individual.pop(index_to_remove)

        best_index = index_to_remove

        # Tests inserting the element in every possible position.
        for index in range(number_of_elements):

            # Inserts temporarily to evaluate fitness.
            best_individual.insert(index, element_removed)

            current_fitness = fitness_function(best_individual, cost_matrix)

            # Updates the best position found so far.
            if current_fitness > best_fitness:
                best_fitness = current_fitness
                best_index = index

            # Restores the previous state before the next iteration.
            best_individual.pop(index)

        # Inserts the element in the best position found.
        best_individual.insert(best_index, element_removed)

    return best_individual

# =============================================================================================== #
