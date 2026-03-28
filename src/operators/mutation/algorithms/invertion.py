"""
Docstring for mutation.invertion
"""
import random

def invertion(individual, probability):

    """
    Docstring for invert
    """

    p = random.random()

    mutated_individual = individual.copy()

    if p < probability:

        number_of_elements = len(mutated_individual)

        start_index = random.randint(0, number_of_elements - 1)

        end_index = random.randint(start_index, number_of_elements - 1)

        # Slice the original array and assign the reversed slice back to the same location.
        # It doesn't include the end index.
        mutated_individual[start_index:end_index] = mutated_individual[start_index:end_index][::-1]

    return mutated_individual
