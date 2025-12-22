"""
Docstring for mutation.common
"""
from typing import Iterable
from mutation.types import MutationOperator

def mutate_population(
    individuals: Iterable,
    probability: float,
    operator: MutationOperator
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
    return [operator(ind, probability) for ind in individuals]
