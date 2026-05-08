"""
"SCRAMBLE" mutation operator implemention.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Functions
# =============================================================================================== #

def scramble(individual: list[int], probability: float) -> list[int]:

    """
    Randomly, scrambles the genes of an individual's cromosome.
    
    Args:
        individual (List[int]): Individual whose genes will be inverted.
        probability (float): Probability required to apply the invertion.

    Returns:
        mutated_individual (List[int]): Mutated individual.
    """

    # Applies the mutation with the given probability.
    if random.random() >= probability:
        return individual.copy()

    # Creates a copy to avoid modifying the original individual.
    mutated_individual = individual.copy()

    n = len(mutated_individual)

    # Selects a random start index.
    start = random.randint(0, n - 1)

    # Selects a random end index greater than or equal to the start index.
    end = random.randint(start, n)

    # Extracts the subsegment to be shuffled.
    sub = mutated_individual[start:end]

    # Shuffles the selected subsegment in place.
    random.shuffle(sub)

    # Assigns the shuffled subsegment back to the individual.
    mutated_individual[start:end] = sub

    return mutated_individual

# =============================================================================================== #
