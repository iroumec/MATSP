"""
Docstring for mutation.scramble
"""
import random

# ----------------------------------------------------------------------------------------------- #

def scramble_individual(invididual, probability):

    """
    Docstring for scramble
    
    :param permutation: Description
    :param probability: Description
    """

    p = random.random()
    
    mutated_individual = invididual.copy()

    if p < probability:

        number_of_elements = len(mutated_individual)

        start_index = random.randint(0, number_of_elements - 1)
        end_index = random.randint(start_index, number_of_elements - 1)

        sub_permutation = mutated_individual[start_index:end_index]
        random.shuffle(sub_permutation)
        mutated_individual[start_index:end_index] = sub_permutation
        
    return mutated_individual

# ----------------------------------------------------------------------------------------------- #

def scramble(children, probability):
    
    """
    Docstring for scramble
    
    :param children: Description
    :param probability: Description
    """
    
    mutated_children = []
    
    for child in children:
        mutated_children.append(scramble_individual(child, probability))
        
    return mutated_children
