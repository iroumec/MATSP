"""
"INVERTION" mutation operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Functions
# =============================================================================================== #

def invertion(individual: list[int], probability: float) -> list[int]:

    """
    Randomly, inverts a contiguous segment of genes of an individual's chromosome.
    
    Selects two random indices and reverses the genes between them, preserving
    all genes while altering their order. If the mutation is not triggered,
    returns an unmodified copy of the individual.

    Args:
        individual (List[int]): Individual whose genes will be inverted.
        probability (float): Probability required to apply the invertion.

    Returns:
        mutated_individual (List[int]): Mutated individual.
    """

    # Applies the mutation only with the given probability.
    if random.random() >= probability:
        return individual.copy()

    # Creates a copy to avoid modifying the original individual.
    mutated_individual = individual.copy()

    number_of_elements = len(mutated_individual)

    # Selects a random start index.
    start_index = random.randint(0, number_of_elements - 1)

    # Selects a random end index greater than or equal to the start index.
    end_index = random.randint(start_index, number_of_elements)

    # Slices the original array and assign the reversed slice back to the same location.
    # It doesn't include the end index.
    mutated_individual[start_index:end_index] = reversed(mutated_individual[start_index:end_index])

    return mutated_individual

# =============================================================================================== #
