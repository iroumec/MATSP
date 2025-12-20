"""
Docstring for selection.tournament
"""

import random

# ----------------------------------------------------------------------------------------------- #

def tournament_selection(population,  fitness_function, tournament_size = 2):
    """
    Perform tournament selection on a population.

    Args:
        population (list): A list of individuals in the population.
        fitness_function (function): A function that takes an individual and returns its fitness score.
        tournament_size (int): The number of individuals to select for the tournament.

    Returns:
        The individual with the highest fitness score from the tournament.
    """

    #Randomly select individuals for the tournament
    tournament = random.sample(population, tournament_size)

    #Select the best individual from the tournament
    winner = max(tournament, key=fitness_function)
    return winner

# ----------------------------------------------------------------------------------------------- #
