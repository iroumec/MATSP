"""
Docstring for mutation.common
"""
from typing import Callable, List, Dict

def select_individuals(
    self,
    population: List[List[int]],
    fitness_function: Callable,
    num_selections: int,
    cost_matrix: List[List[int]],
    **kwargs: Dict[str, any],
):
    """
    Docstring for mutate_population
    
    :param individuals: Description
    :type individuals: Iterable
    :param probability: Description
    :type probability: float
    :param operator: Description
    :type operator: MutationOperator
    """
    return self(population, fitness_function, num_selections, cost_matrix, kwargs)
