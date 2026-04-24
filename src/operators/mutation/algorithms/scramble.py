"""
Docstring for mutation.scramble
"""
import random

def scramble(individual, probability: float):

    """
    Given an individual and a probability, it scrambles the genes
    of the individual's cromosome.
    
    :param individual: Description
    :param probability: Description
    """
    mutated = individual.copy()

    if random.random() < probability:
        start = random.randint(0, len(mutated) - 1)
        end = random.randint(start, len(mutated) - 1)

        sub = mutated[start:end]
        random.shuffle(sub)
        mutated[start:end] = sub

    return mutated
