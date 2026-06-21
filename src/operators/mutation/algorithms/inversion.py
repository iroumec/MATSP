"""
"INVERSION" mutation operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Functions
# =============================================================================================== #

def inversion(individual: list[int], probability: float) -> list[int]:

    """
    Randomly, inverts a contiguous segment of genes of an individual's chromosome.
    
    Selects two random indices and reverses the genes between them, preserving
    all genes while altering their order. If the mutation is not triggered,
    returns an unmodified copy of the individual.

    Args:
        individual (list[int]): Individual whose genes will be inverted.
        probability (float): Probability required to apply the invertion.

    Returns:
        mutated_individual (list[int]): Mutated individual.
    """

    # Applies the mutation only with the given probability.
    if random.random() >= probability:
        return list(individual)

    # Creates a copy to avoid modifying the original individual.
    mutated_individual = list(individual)

    # Selects a random start index and a random end index.
    # sorted() ensures start is before end.
    start_index, end_index = sorted(random.sample(range(len(mutated_individual)), 2))

    # Slices the original array and assign the reversed slice back to the same location.
    mutated_individual[start_index:end_index+1] = mutated_individual[start_index:end_index+1][::-1]

    return mutated_individual

# =============================================================================================== #
