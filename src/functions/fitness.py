"""
Fitness function implementation.
"""

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