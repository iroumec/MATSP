"""
Docstring for crossover.OX1
"""
import random

# ----------------------------------------------------------------------------------------------- #

def crossover_ox1(parent1, parent2):
    """
    Perform Order Crossover 1 (OX1) between two parent permutations.

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
    point1 = random.randint(0, size - 1)
    point2 = random.randint(0, size - 1)

    if point1 > point2:
        point1, point2 = point2, point1

    # Copy the segment from parent1 to offspring1
    offspring1[point1:point2 + 1] = parent1[point1:point2 + 1]
    # Fill the remaining positions in offspring1 with genes from parent2
    current_pos_offspring = (point2 + 1) % size
    current_pos_parent= (point2 + 1) % size
    for _ in range(size):
        gene = parent2[current_pos_parent]
        if gene not in offspring1:
            offspring1[current_pos_offspring] = gene
            current_pos_offspring = (current_pos_offspring + 1) % size
        current_pos_parent = (current_pos_parent + 1) % size

    # Copy the segment from parent2 to offspring2
    offspring2[point1:point2 + 1] = parent2[point1:point2 + 1]
    # Fill the remaining positions in offspring2 with genes from parent1
    current_pos_offspring = (point2 + 1) % size
    current_pos_parent= (point2 + 1) % size
    for _ in range(size):
        gene = parent1[current_pos_parent]
        if gene not in offspring2:
            offspring2[current_pos_offspring] = gene
            current_pos_offspring = (current_pos_offspring + 1) % size
        current_pos_parent = (current_pos_parent + 1) % size

    return [offspring1, offspring2]

# ----------------------------------------------------------------------------------------------- #