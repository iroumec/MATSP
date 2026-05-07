"""
"INSERTION" improvement (local search) operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

from typing import List, Callable

# =============================================================================================== #
# Functions
# =============================================================================================== #

def insertion(
    individual: List[int],
    probability: float,
    fitness_function: Callable,
    cost_matrix: List[List[int]]
) -> List[int]:

    """
    Dcostring.
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
