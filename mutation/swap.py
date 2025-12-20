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

    while number not in different:
        number = random.randint(0, n)

    return number

# ----------------------------------------------------------------------------------------------- #

def swap(permutation, probability):

    """
    Swap two elements of a permutation.
    
    :param permutation: Permutation.
    :param probability: Probability of swapping.
    """

    p = random.random()
    
    number_of_elements = len(permutation)

    if p < probability:

        first_index = get_random_int(number_of_elements)
        second_index = get_random_int_different_from(number_of_elements, first_index)

        auxiliar = permutation[first_index]
        permutation[first_index] = permutation[second_index]
        permutation[second_index] = auxiliar

# ----------------------------------------------------------------------------------------------- #
