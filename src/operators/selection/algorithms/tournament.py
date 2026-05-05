"""
"TOURNAMENT" selection operator implementation.
"""

import random

def tournament(
    population,
    fitness_function,
    num_selections,
    cost_matrix,
    tournament_size = 2,
    **_kwargs
):
    """
    Perform tournament selection on a population.

    Args:
        population (list): A list of individuals in the population.
        fitness_function (function): A function that takes an individual and a cost matrix and
        returns its fitness score.
        num_selections (int): The number of individuals to select.
        tournament_size (int): The number of individuals to select for the tournament.

    Returns:
        The individual with the highest fitness score from the tournament.
    """

    selected_individuals = []

    for _ in range(num_selections):
        #Randomly select individuals for the tournament
        tournament_result = random.sample(population, tournament_size)

        #Select the best individual from the tournament
        winner = max(tournament_result, key=lambda ind: fitness_function(ind, cost_matrix))
        selected_individuals.append(winner)

    return selected_individuals
