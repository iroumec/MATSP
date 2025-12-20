"""
Docstring for initialization.nearest_neighbour

The mutation operator selected is different from the ones selected as mutation operators.
"""
import random

# ----------------------------------------------------------------------------------------------- #

def invert_invidual(individual, probability):

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

# ----------------------------------------------------------------------------------------------- #

def invert(individuals, probability):
    
    """
    Docstring for swap
    
    :param individual: Description
    :param probability: Description
    """
    
    mutated_individuals = []

    for individual in individuals:
        
        mutated_individuals.append(invert_invidual(individual, probability))
        
    return mutated_individuals

# ----------------------------------------------------------------------------------------------- #
