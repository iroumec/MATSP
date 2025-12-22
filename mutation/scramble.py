"""
Docstring for mutation.scramble
"""
import random

def scramble(individual, probability):

    """
    Docstring for scramble
    
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
