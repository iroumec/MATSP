"""
Docstring for mutation.common
"""
from crossover.types import CrossoverOperator

def cross_parents(
    first_parent: int,
    second_parent: int,
    probability: float,
    operator: CrossoverOperator,
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
    return operator(first_parent, second_parent, probability)
