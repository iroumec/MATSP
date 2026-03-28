"""
Docstring for survivors.replace_worst
"""

# ----------------------------------------------------------------------------------------------- #

def replace_worst(actual_population, new_individuals, number_to_replace, fitness_function, cost_matrix):
    """
    Replace the worst-performing individuals in the actual_population with the best-performing individuals
    in new_individuals.

    Args:
        actual_population (list): List of current individuals in the population.
        new_individuals (list): List of new individuals to be added to the population.
        number_to_replace (int): Number of worst individuals to replace.
        fitness_function (function): A function that takes an individual and returns its fitness score.

    Returns:
        list: Updated population after replacement.
    """
    # Sort actual population by fitness
    actual_population_fitness_scores = [(ind, fitness_function(ind, cost_matrix)) for ind in actual_population]
    actual_population_fitness_scores.sort(reverse=True, key=lambda ind: ind[1])

    # Sort new possible individuals by fitness
    new_individuals_fitness_scores = [(ind, fitness_function(ind, cost_matrix)) for ind in new_individuals]
    new_individuals_fitness_scores.sort(reverse=True, key=lambda ind: ind[1])

    # Select individuals to keep and to add
    individuals_to_keep = [ind for ind, fitness in actual_population_fitness_scores[:-number_to_replace]]
    individuals_to_add = [ind for ind, fitness in new_individuals_fitness_scores[:number_to_replace]]
    updated_population = individuals_to_keep + individuals_to_add

    return updated_population

# ----------------------------------------------------------------------------------------------- #
