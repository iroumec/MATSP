"""
Implementation of the "scramble" mutation operator.
"""
import random

def scramble(individual, probability: float):

    """
    Given an individual and a probability, it scrambles the genes
    of the individual's cromosome.
    
    :param individual: Description
    :param probability: Description
    """

    mutated_individual = individual.copy()

    if random.random() < probability:

        start = random.randint(0, len(mutated_individual) - 1)
        end = random.randint(start, len(mutated_individual) - 1)

        sub = mutated_individual[start:end]
        random.shuffle(sub)
        mutated_individual[start:end] = sub

    return mutated_individual
