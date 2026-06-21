"""
Matrix loading algorithm with caching.
"""

from functools import lru_cache

# =============================================================================================== #
# Constants
# =============================================================================================== #

INSTANCES_PATH = "resources/atsp-instances/"

# =============================================================================================== #
# Function
# =============================================================================================== #

@lru_cache(maxsize=None)
def load_matrix(instance: str) -> tuple[tuple[int]]:
    """
    Loads an instance's cost matrix handling TSPLIB format (header and EOF).
    Uses LRU cache to avoid redundant disk I/O when multiple configurations
    use the same instance.
    
    Args:
        instance (str): Instance's name.
    
    Returns:
        matrix (tuple[tuple[int]]): Cost matrix as an immutable structure.
    
    Raises:
        ValueError: If the matrix is not square.
    """

    raw_numbers = []
    dimension = 0

    with open(f"{INSTANCES_PATH}{instance}.atsp", "r", encoding="UTF-8") as f:
        lines = f.readlines()

    reading_data = False
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Extracts dimension from header.
        if "DIMENSION" in line:
            # We split by ':' or whitespace to be more robust.
            dimension = int(line.replace(":", " ").split()[-1])
            continue

        # Detects start of data.
        if "EDGE_WEIGHT_SECTION" in line:
            reading_data = True
            continue

        # Stops at EOF.
        if "EOF" in line:
            break

        if reading_data:
            # Adds all numbers found in the line the flat list.
            raw_numbers.extend(map(int, line.split()))

    # Reconstructs the square matrix using the dimension.
    # We use a tuple of tuples to ensure the return value is hashable for lru_cache.
    matrix = tuple(
        tuple(raw_numbers[i : i + dimension])
        for i in range(0, len(raw_numbers), dimension)
        if i + dimension <= len(raw_numbers)
    )
    
    # Verifies that the matriz is square.
    if len(matrix) != dimension:
        raise ValueError(
            f"ERROR: Instance '{instance}' has an invalid matrix: "
            f"expected {dimension} rows, got {len(matrix)}."
        )

    for row_index, row in enumerate(matrix):
        if len(row) != dimension:
            raise ValueError(
                f"ERROR: Instance '{instance}' has an invalid matrix: "
                f"row {row_index} has {len(row)} columns, expected {dimension}."
            )

    return matrix

# =============================================================================================== #
