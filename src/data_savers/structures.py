"""
Data saving dataclasses.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from dataclasses import dataclass

from configuration import Config

# =============================================================================================== #
# Dataclass
# =============================================================================================== #

@dataclass
class AlgorithmResult:

    """
    Dataclass for algorithm results.
    """

    configuration: Config
    fitness_function: callable
    best_individual: list[int]
    cost_matrix: tuple[tuple[int]]
    average_execution_time: float
    average_best_fitness_through_time: list[float]
    std_best_fitness_through_time: list[float]

# =============================================================================================== #
