"""
"SWAP" mutation operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Functions
# =============================================================================================== #

def swap(individual: list[int], probability: float) -> list[int]:

    """
    Swaps two random genes from an individual's cromosome.
    
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
    mutated = individual.copy()

    n = len(mutated)

    # Selects two distinct indices without replacement.
    i, j = random.sample(range(n), 2)

    # Swaps the selected positions.
    mutated[i], mutated[j] = mutated[j], mutated[i]

    return mutated

# =============================================================================================== #
