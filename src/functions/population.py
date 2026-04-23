"""
Docstring for survivors.select_best
"""

# ----------------------------------------------------------------------------------------------- #

def select_best_individual(actual_population, fitness_function, cost_matrix):
    """
    Select the best performing individual of the actual generation.

    Args:
        actual_population (list): List of current individuals in the population.
        fitness_function (function): A function that takes an individual and returns its fitness score.

    Returns: 
        best fitness of current population.
    """
    # Sort actual population by fitness
    actual_population_fitness_scores = [(ind, fitness_function(ind, cost_matrix)) for ind in actual_population]
    actual_population_fitness_scores.sort(reverse=True, key=lambda x: x[1])
    
    return actual_population_fitness_scores[0][1]
    
# --------------------------------------------------------------------------------------------- #
