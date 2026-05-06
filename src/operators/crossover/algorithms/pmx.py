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

def pmx(parent1: List[int], parent2: List[int], probability: float) -> Tuple[List[int]]:
    """
    Perform Partially Mapped Crossover (PMX) between two parent permutations.

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

    # Precomputes index maps for O(1) lookup.
    index_p1 = {gene: i for i, gene in enumerate(parent1)}
    index_p2 = {gene: i for i, gene in enumerate(parent2)}

    # Selects two random crossover points.
    point1, point2 = sorted(random.sample(range(size), 2))

    def build_offspring(p_base, p_fill, index_fill):
        # Initializes offsprings with None.
        offspring = [None] * size

        # Copies the segment from base parent.
        offspring[point1:point2 + 1] = p_base[point1:point2 + 1]

        # Tracks used genes.
        used = set(offspring[point1:point2 + 1])

        # Fills the remaining positions.
        # First the elements in the crossover segment.
        for i in range(point1, point2 + 1):
            element = p_fill[i]

            if element not in used:
                current_position = i

                while True:
                    mapped_element = p_base[current_position]
                    index_in_fill = index_fill[mapped_element]

                    if offspring[index_in_fill] is None:
                        offspring[index_in_fill] = element
                        used.add(element)
                        break

                    current_position = index_in_fill

        # Then the rest of the elements.
        for gene in p_fill:
            if gene not in used:
                for i in range(size):
                    if offspring[i] is None:
                        offspring[i] = gene
                        used.add(gene)
                        break

        return offspring


    offspring1 = build_offspring(parent1, parent2, index_p2)
    offspring2 = build_offspring(parent2, parent1, index_p1)

    return [offspring1, offspring2]

# =============================================================================================== #
