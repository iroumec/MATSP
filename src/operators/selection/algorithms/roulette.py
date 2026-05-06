"""
"ROULETTE" selection operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random
import bisect
import itertools
from typing import List

# =============================================================================================== #
# Functions
# =============================================================================================== #

def roulette(
    population: List[int],
    fitness_function: callable,
    num_selections: int,
    cost_matrix: List[List[int]],
    **_kwargs
) -> List[int]:
    """
    Performs roulette wheel selection on a population.

    Args:
        population (List[int]): A list of individuals in the population.
        fitness_function (callable): A function that takes an individual and the cost
            matrix and returns its fitness score.
        num_selections (int): The number of individuals to select.
        cost_matrix (List[List[int]]): The cost matrix for evaluating fitness.
        **kwargs: Additional keyword arguments for the selection process.

    Returns:
        selected_individuals (List[int]): A list of selected individuals.
    """

    # Calculates fitness scores.
    fitness_scores = [fitness_function(ind, cost_matrix) for ind in population]

    # Calculates total fitness.
    total_fitness = sum(fitness_scores)

    # Calculates cumulative probabilities.
    cumulative_probs = list(itertools.accumulate(score / total_fitness for score in fitness_scores))

    # Performs selection.
    selected_individuals = []
    for _ in range(num_selections):
        r = random.random()
        index = bisect.bisect_left(cumulative_probs, r)
        selected_individuals.append(population[index])

    return selected_individuals

# =============================================================================================== #
