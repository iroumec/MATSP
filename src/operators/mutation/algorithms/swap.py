"""
Docstring for mutation.swap
"""
import random

def swap(individual, probability: float):

    """
    Docstring for swap
    
    :param individual: Description
    :param probability: Description
    """
    mutated = individual.copy()

    if random.random() < probability:
        i = random.randint(0, len(mutated) - 1)
        j = random.randint(0, len(mutated) - 1)
        while j == i:
            j = random.randint(0, len(mutated) - 1)

        mutated[i], mutated[j] = mutated[j], mutated[i]

    return mutated
