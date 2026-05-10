"""
"OX1" crossover operator implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import random

# =============================================================================================== #
# Functions
# =============================================================================================== #

def pmx(parent1: list[int], parent2: list[int], probability: float) -> tuple[list[int], list[int]]:
    """
    Perform Partially Mapped Crossover (PMX) between two parent permutations.

    Selects a random segment from each parent and copies it directly into the
    corresponding offspring. Conflicting genes outside the segment are placed
    using a mapping derived from the segment: each conflicting gene is
    repeatedly remapped through the segment until a free position is found.
    Any remaining unplaced genes are filled left to right.

    Args:
        parent1 (list[int]): The first parent permutation.
        parent2 (list[int]): The second parent permutation.
        probability (float): Probability of crossover occurring. If not triggered,
            returns an empty list.

    Returns:
        offsprings (tuple[list[int], list[int]]): Two offspring permutations resulting from
            the crossover.
    """

    # No crossover.
    if random.random() > probability:
        return []

    size = len(parent1)

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
