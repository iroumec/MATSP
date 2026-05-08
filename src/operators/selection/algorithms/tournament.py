"""
"TOURNAMENT" selection operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Functions
# =============================================================================================== #

def tournament(
    population: list[list[int]],
    fitness_function: callable,
    num_selections: int,
    cost_matrix: list[list[int]],
    tournament_size: int = 3,
    **_kwargs
) -> list[list[int]]:

    """
    Performs tournament selection on a population.

    Args:
        population (list[list[int]]): A list of individuals in the population.
        fitness_function (callable): A function that takes an individual and a cost matrix and
            returns its fitness score.
        num_selections (int): The number of individuals to select.
        cost_matrix (list[list[int]]): Cost matrix.
        tournament_size (int): The number of individuals to select for the tournament.

    Returns:
        selected_individuals (list[list[int]]): A list of selected individuals.
    """

    # Precomputes fitness for all individuals.
    fitness_map = {id(ind): fitness_function(ind, cost_matrix) for ind in population}

    selected_individuals = []

    for _ in range(num_selections):
        # Randomly selects individuals for the tournament.
        tournament_result = random.sample(population, tournament_size)

        # Selects the best individual from the tournament.
        winner = max(tournament_result, key=lambda ind: fitness_map[id(ind)])
        selected_individuals.append(winner)

    return selected_individuals

# =============================================================================================== #
