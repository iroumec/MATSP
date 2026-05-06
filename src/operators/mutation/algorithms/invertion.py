"""
"INVERTION" mutation operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random
from typing import List

# =============================================================================================== #
# Functions
# =============================================================================================== #

def invertion(individual: List[int], probability: float) -> List[int]:

    """
    Randomly, inverts the genes of an individual's cromosome.
    
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
