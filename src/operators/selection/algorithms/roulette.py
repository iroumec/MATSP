"""
Docstring for selection.roulette
"""

import random

def roulette(population, fitness_function, num_selections, cost_matrix, **_kwargs):
    """
    Perform roulette wheel selection on a population.

    Args:
        population (list): A list of individuals in the population.
        fitness_function (callable): A function that takes an individual and the cost
            matrix and returns its fitness score.
        num_selections (int): The number of individuals to select.
        cost_matrix (list): The cost matrix for evaluating fitness.
        **kwargs: Additional keyword arguments for the selection process.

    Returns:
        list: A list of selected individuals.
    """
    # Calculate fitness scores
    fitness_scores = [fitness_function(ind, cost_matrix) for ind in population]

    # Calculate total fitness
    total_fitness = sum(fitness_scores)

    # Calculate selection probabilities
    selection_probs = [score / total_fitness for score in fitness_scores]

    # Perform selection
    selected_individuals = []
    for _ in range(num_selections):
        r = random.random()
        cumulative_prob = 0.0
        for ind, prob in zip(population, selection_probs):
            cumulative_prob += prob
            if r <= cumulative_prob:
                selected_individuals.append(ind)
                break

    return selected_individuals
