"""
"NEAREST_NEIGHBOUR" initialization operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Function
# =============================================================================================== #

def nearest_neighbour(
    number_of_individuals_to_generate: int,
    cost_matrix: tuple[tuple[int]]
) -> list[list[int]]:

    """
    Generates individuals using a nearest neighbour heuristic.
    
    Args:
        number_of_individuals_to_generate (int): Number of individuals to generate.
        cost_matrix (tuple[tuple[int]]): Cost matrix.
    
    Returns:
        population (list[list[int]]): A list of individuals.
    """

    individuals: list[list[int]] = []
    number_of_cities = len(cost_matrix)

    for _ in range(number_of_individuals_to_generate):

        starting_city = random.randint(0, number_of_cities - 1)
        new_individual = [starting_city]

        unvisited = set(range(number_of_cities)) - {starting_city}

        while unvisited:
            last = new_individual[-1]
            nearest = min(unvisited, key=lambda city, l=last: cost_matrix[l][city])
            new_individual.append(nearest)
            unvisited.remove(nearest)

        individuals.append(new_individual)

    return individuals

# =============================================================================================== #
