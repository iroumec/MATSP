"""
Docstring
"""

def must_stop(current_generation: int, generations_without_improvements: int, config) -> bool:
    """
    Docstring
    """

    stop = config.stop_reasons # Alias.

    generations_limit = stop.generations and (current_generation >= stop.max_generations)
    generations_without_improvements_limit = (
        stop.generations_without_improvements and
        (generations_without_improvements >= stop.max_generations_without_improvements)
    )

    return generations_limit or generations_without_improvements_limit
