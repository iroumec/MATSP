"""
Stop reasons checking implementation.
"""

# =============================================================================================== #
# Function
# =============================================================================================== #

def must_stop(current_generation: int, generations_without_improvements: int, config) -> bool:

    """
    Checks if the algorithm must be stopped.
    
    Args:
        current_generation (int): Current generation.
        generation_without_improvements (int): Generations without improvements (the fitness
            value of its best member is the same as the one in the previous generations).
        config (Config): Algorithm configuration.
    
    Returns:
        must_stop (bool): `True` if the algorithm must be stopped. Otherwise, `false`.
    """

    stop = config.stop_reasons # Alias.

    generations_limit = stop.generations and (current_generation >= stop.max_generations)
    generations_without_improvements_limit = (
        stop.generations_without_improvements and
        (generations_without_improvements >= stop.max_generations_without_improvements)
    )

    return generations_limit or generations_without_improvements_limit

# =============================================================================================== #
