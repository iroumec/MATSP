"""
Docstring
"""

def calculate(individual, cost_matrix):

    """
    Docstring for calculate
    
    :param individual: Description
    :param cost_matrix: Description
    """

    number_of_cities = len(individual)

    travel_cost = 0

    for city in range(number_of_cities - 1):

        travel_cost += cost_matrix[individual[city]][individual[city+1]]
        
    travel_cost += cost_matrix[individual[number_of_cities - 1]][individual[0]]

    return 1/travel_cost
