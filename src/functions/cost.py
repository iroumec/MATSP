"""
Cost calculation algorithm implementation.
"""

# =============================================================================================== #
# Function
# =============================================================================================== #

def calculate_cost(individual: list[int], cost_matrix: list[list[int]]):

    """
    Calculates the cost of an individual based on a cost matrix.
    
    Args:
        individual (list[int]): Sequence of locations.
        cost_matrix (list[list[int]]): Cost matrix.

    Returns:
        travel_cost (float): Travel cost.
    """

    number_of_cities = len(individual)

    travel_cost = 0

    for city in range(number_of_cities - 1):

        travel_cost += cost_matrix[individual[city]][individual[city+1]]

    travel_cost += cost_matrix[individual[number_of_cities - 1]][individual[0]]

    return travel_cost

# =============================================================================================== #
