"""
"NEAREST_NEIGHBOUR" initialization operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Public Functions
# =============================================================================================== #

def nearest_neighbour(
    number_of_inviduals_to_generate: int,
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

    for _ in range(number_of_inviduals_to_generate):

        # The cost matriz is always square.
        # We suppose that it's always possible to go from one city to another.
        starting_city = random.randint(0, number_of_cities - 1)

        new_individual = [starting_city]

        # -1 due to the starting city being already determined.
        for _ in range(number_of_cities - 1):

            current_nearest_neighbour = None

            for city in range(number_of_cities):

                if _is_candidate(city, new_individual, current_nearest_neighbour, cost_matrix):
                    current_nearest_neighbour = city

            if current_nearest_neighbour is not None:
                new_individual.append(current_nearest_neighbour)
            else:
                print("Unexpected error")

        individuals.append(new_individual)

    return individuals

# =============================================================================================== #
# Private Functions
# =============================================================================================== #

def _is_candidate(city, individual, current_nearest_neighbour, cost_matrix):

    last_element_of_individual = individual[len(individual) - 1]

    return city not in individual and (
        current_nearest_neighbour is None or
        cost_matrix[last_element_of_individual][city] <
            cost_matrix[last_element_of_individual][current_nearest_neighbour]
    )

# =============================================================================================== #
