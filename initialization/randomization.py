"""
Docstring for initialization.nearest_neighbour
"""
import random

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

        new_individual = []

        for _ in range(number_of_cities):

            next_city = random.randint(0, number_of_cities - 1)

            while next_city in new_individual:

                next_city = random.randint(0, number_of_cities - 1)

            new_individual.append(next_city)

        individuals.append(new_individual)

    return individuals

# ----------------------------------------------------------------------------------------------- #
