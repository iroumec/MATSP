"""
Docstring for mutation.scramble
"""
import random

# ----------------------------------------------------------------------------------------------- #

def scramble(permutation, probability):

    """
    Docstring for scramble
    
    :param permutation: Description
    :param probability: Description
    """

    p = random.random()

    if p < probability:

        number_of_elements = len(permutation)

        start_index = random.randint(0, number_of_elements - 1)
        end_index = random.randint(start_index, number_of_elements - 1)

        sub_permutation = permutation[start_index:end_index]
        random.shuffle(sub_permutation)
        permutation[start_index:end_index] = sub_permutation

# ----------------------------------------------------------------------------------------------- #

array = [1, 2, 3, 4, 5, 6, 7]
print(array)

scramble(array, 0.99)
print(array)
