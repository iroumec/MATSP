"""
Docstring for survivors.replace_worst
"""

def replace_worst(
    actual_population,
    new_individuals,
    number_to_replace,
    fitness_function,
    cost_matrix
):
    """
    Replace the worst-performing individuals in the actual_population with the best-performing
    individuals in new_individuals.

    Args:
        actual_population (list): List of current individuals in the population.
        new_individuals (list): List of new individuals to be added to the population.
        number_to_replace (int): Number of worst individuals to replace.
        fitness_function (function): A function that takes an individual and returns its fitness
        score.

    Returns:
        list: Updated population after replacement.
    """
    
    number_to_replace = min(len(new_individuals), number_to_replace)

    # Validations.
    if number_to_replace == 0:
        return actual_population

    if number_to_replace > len(new_individuals):
        raise ValueError(f"Cannot be replaced {number_to_replace} individuals because there aren't {len(new_individuals)} new individuals.")

    if number_to_replace > len(actual_population):
        raise ValueError("Cannot replace more individuals than the population size.")

    # Sort actual population by fitness
    actual_population_fitness_scores = [
        (ind, fitness_function(ind, cost_matrix)) for ind in actual_population
    ]
    actual_population_fitness_scores.sort(reverse=True, key=lambda ind: ind[1])

    # Sort new possible individuals by fitness
    new_individuals_fitness_scores = [
        (ind, fitness_function(ind, cost_matrix)) for ind in new_individuals
    ]
    new_individuals_fitness_scores.sort(reverse=True, key=lambda ind: ind[1])

    # Select individuals to keep and to add
    individuals_to_keep = [ind for ind, _ in actual_population_fitness_scores[:-number_to_replace]]
    individuals_to_add = [ind for ind, _ in new_individuals_fitness_scores[:number_to_replace]]
    updated_population = individuals_to_keep + individuals_to_add

    return updated_population
