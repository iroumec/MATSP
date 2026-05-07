"""
Package declaration for general functions implementations.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from .stop import must_stop
from .cost import calculate_cost
from .instance import assert_same_instance
from .population import select_best_individual, generate_initial_population

from .fitness import (
    get_best_fitness,
    calculate_fitness,
    calculate_average_best_fitness_through_time,
)

# =============================================================================================== #
# Declarations
# =============================================================================================== #

__all__ = [
    "calculate_cost",
    "calculate_fitness",
    "select_best_individual",
    "must_stop",
    "calculate_average_best_fitness_through_time",
    "assert_same_instance",
    "get_best_fitness",
    "generate_initial_population",
]

# =============================================================================================== #
