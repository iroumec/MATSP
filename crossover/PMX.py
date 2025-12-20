"""
Docstring for crossover.PMX
"""

# ----------------------------------------------------------------------------------------------- #

def element_in_list(element, lst):
    """
    Check if an element is present in a list.

    Args:
        element: The element to check.
        lst (list): The list to search in.
    """
    for item in lst:
        if item == element:
            return True
    return False

# ----------------------------------------------------------------------------------------------- #

def crossover_pmx(parent1, parent2):
    """
    Perform Partially Mapped Crossover (PMX) between two parent permutations.

    Args:
        parent1 (list): The first parent permutation.
        parent2 (list): The second parent permutation.

    Returns:
        tuple: Two offspring permutations resulting from the crossover.
    """

    size = len(parent1)
    # Initialize offspring with None
    offspring1 = [None] * size
    offspring2 = [None] * size

    # Select two random crossover points
    import random
    point1 = random.randint(0, size - 1)
    point2 = random.randint(0, size - 1)

    if point1 > point2:
        point1, point2 = point2, point1

    # Copy the segment from parent1 to offspring1
    offspring1[point1:point2 + 1] = parent1[point1:point2 + 1]

    # Fill the remaining positions in offspring1 with genes from parent2
    # First the elements in the crossover segment
    current_position = point1
    for i in range(point1, point2 + 1):
        element = parent2[i]
        current_position = i
        if element not in offspring1:
            while True:
                mapped_element = parent1[current_position]
                index_in_parent2 = parent2.index(mapped_element)
                if offspring1[index_in_parent2] is None:
                    offspring1[index_in_parent2] = element
                    break
                else:
                    current_position = index_in_parent2        
    # Then the rest of the elements
    for gene_p2 in parent2:
        if gene_p2 not in offspring1:
            for gene_off1 in offspring1:
                if gene_off1 is None:
                    gene_off1 = gene_p2 


    # Copy the segment from parent2 to offspring2
    offspring2[point1:point2 + 1] = parent2[point1:point2 + 1]

    # Fill the remaining positions in offspring2 with genes from parent1
    current_position = point1
    for i in range(point1, point2 + 1):
        element = parent1[i]
        current_position = i
        if element not in offspring2:
            while True:
                mapped_element = parent2[current_position]
                index_in_parent1 = parent1.index(mapped_element)
                if offspring2[index_in_parent1] is None:
                    offspring2[index_in_parent1] = element
                    break
                else:
                    current_position = index_in_parent1   
    
    # Then the rest of the elements
    for gene_p1 in parent2:
        if gene_p1 not in offspring1:
            for gene_off1 in offspring1:
                if gene_off1 is None:
                    gene_off1 = gene_p2 

# ----------------------------------------------------------------------------------------------- #
