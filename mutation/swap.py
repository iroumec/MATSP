"""
Docstring for mutation.swap
"""
import random

# ----------------------------------------------------------------------------------------------- #

def get_random_int(n):

    """
    Docstring for get_random_int
    
    :param n: Description
    """

    return random.randint(0, n)

# ----------------------------------------------------------------------------------------------- #

def get_random_int_different_from(n, different):

    """
    Docstring for get_random_int_different_from
    
    :param n: Description
    :param different: Description
    """

    number = different

    while number == different:
        number = random.randint(0, n)

    return number

# ----------------------------------------------------------------------------------------------- #

def swap_individual(individual, probability):

    """
    Swap two elements of a permutation.
    
    :param permutation: Permutation.
    :param probability: Probability of swapping.
    """

    p = random.random()
    
    mutated_individual = individual.copy()
    

    if p < probability:

        number_of_elements = len(mutated_individual)
        
        first_index = get_random_int(number_of_elements - 1)
        second_index = get_random_int_different_from(number_of_elements - 1, first_index)

        auxiliar = mutated_individual[first_index]
        mutated_individual[first_index] = mutated_individual[second_index]
        mutated_individual[second_index] = auxiliar
        
    return mutated_individual

# ----------------------------------------------------------------------------------------------- #

def swap(individuals, probability):
    
    """
    Docstring for swap
    
    :param individual: Description
    :param probability: Description
    """
    
    mutated_individuals = []

    for individual in individuals:
        
        mutated_individuals.append(swap_individual(individual, probability))
        
    return mutated_individuals

# ----------------------------------------------------------------------------------------------- #