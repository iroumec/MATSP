"""
Docstring for initialization.nearest_neighbour
"""
import random

# ----------------------------------------------------------------------------------------------- #

def is_candidate(city, individual, current_nearest_neighbour, cost_matrix):

    """
    Docstring for is_candidate
    
    :param city: Description
    :param individual: Description
    :param current_nearest_neighbour: Description
    :param cost_matrix: Description
    """

    return city not in individual and (current_nearest_neighbour is None or cost_matrix[individual.last][city] < cost_matrix[individual.last][current_nearest_neighbour])

# ----------------------------------------------------------------------------------------------- #

def initialize(number_of_inviduals_to_generate, cost_matrix):

    """
    Docstring for initialize
    
    :param number_of_inviduals_to_generate: Description
    :param cost_matrix: Description
    """

    individuals = []

    number_of_cities = len(cost_matrix)

    for _ in range(number_of_inviduals_to_generate):

        # The cost matriz is always square.
        # We suppose that it's always possible to go from one city to another.
        starting_city = random.randint(0, number_of_cities - 1)

        new_individual = [starting_city]

        # -1 due to the starting city being already determined.
        for _ in range(number_of_cities - 1):

            nearest_neighbour = None

            for city in range(number_of_cities):

                if is_candidate(city, new_individual, nearest_neighbour, cost_matrix):
                    nearest_neighbour = city

            if nearest_neighbour is not None:
                new_individual.append(nearest_neighbour)
            else:
                print("Unexpected error")

        individuals.append(new_individual)

    return individuals

# ----------------------------------------------------------------------------------------------- #
