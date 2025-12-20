"""
Docstring for initialization.nearest_neighbour

The mutation operator selected is different from the ones selected as mutation operators.
"""
import random

# ----------------------------------------------------------------------------------------------- #

def invert(permutation, probability):

    """
    Docstring for invert
    """
    
    p = random.random()
    
    if p < probability:
    
        number_of_elements = len(permutation)
        
        start_index = random.randint(0, number_of_elements)
        
        end_index = random.randint(start_index, number_of_elements)
        
        # Slice the original array and assign the reversed slice back to the same location.
        # It doesn't include the end index.
        permutation[start_index:end_index] = permutation[start_index:end_index][::-1]

# ----------------------------------------------------------------------------------------------- #
