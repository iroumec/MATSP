"""
"OX1" crossover operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random
from typing import List, Tuple

# =============================================================================================== #
# Functions
# =============================================================================================== #

def ox1(parent1: List[int], parent2: List[int], probability: float) -> Tuple[List[int]]:
    """
    Perform Order Crossover 1 (OX1) between two parent permutations.

    Args:
        parent1 (List[int]): The first parent permutation.
        parent2 (List[int]): The second parent permutation.

    Returns:
        offsprings (Tuple[List[int]]): Two offspring permutations resulting from the crossover.
    """

    # No crossover.
    if random.random() > probability:
        return []

    size = len(parent1)

    # Initializes offsprings with None.
    offspring1 = [None] * size
    offspring2 = [None] * size

    # Selects two random crossover points.
    point1, point2 = sorted(random.sample(range(size), 2))

    def build_offspring(base_parent, fill_parent):
        # Initializes offspring with None.
        offspring = [None] * size

        # Copies the segment from base_parent.
        offspring[point1:point2 + 1] = base_parent[point1:point2 + 1]

        # Tracks genes already in offspring.
        used = set(offspring[point1:point2 + 1])

        # Fills the remaining positions with genes from fill_parent.
        current_pos_offspring = (point2 + 1) % size
        current_pos_parent = (point2 + 1) % size

        for _ in range(size):
            gene = fill_parent[current_pos_parent]
            if gene not in used:
                offspring[current_pos_offspring] = gene
                used.add(gene)
                current_pos_offspring = (current_pos_offspring + 1) % size
            current_pos_parent = (current_pos_parent + 1) % size

        return offspring

    offspring1 = build_offspring(parent1, parent2)
    offspring2 = build_offspring(parent2, parent1)

    return [offspring1, offspring2]

# =============================================================================================== #
