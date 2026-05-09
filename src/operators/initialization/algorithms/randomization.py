"""
"RANDOMIZATION" initialization operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Functions
# =============================================================================================== #

def randomization(
    number_of_inviduals_to_generate: int,
    cost_matrix: tuple[tuple[int]]
) -> list[list[int]]:

    """
    Generates individuals using a randomization approach.
    
    Args:
        number_of_individuals_to_generate (int): Number of individuals to generate.
        cost_matrix (tuple[tuple[int]]): Cost matrix.
    
    Returns:
        population (list[list[int]]): A list of individuals.
    """

    individuals: list[list[int]] = []

    number_of_cities = len(cost_matrix)

    for _ in range(number_of_inviduals_to_generate):

        new_individual = []

        for _ in range(number_of_cities):

            next_city = random.randint(0, number_of_cities - 1)

            while next_city in new_individual:

                next_city = random.randint(0, number_of_cities - 1)

            new_individual.append(next_city)

        individuals.append(new_individual)

    return individuals

# =============================================================================================== #
