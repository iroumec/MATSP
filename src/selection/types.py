"""
Docstring for mutation.types
"""
from typing import List, Callable, Any
from typing_extensions import Protocol

class SelectionOperator(Protocol):
    """
    Docstring for MutationOperator
    """
    def __call__(
        self,
        population: List[List[int]],
        fitness_function: Callable,
        num_selections: int,
        cost_matrix: List[List[int]],
        **kwargs: Any
    ) -> List[int]:
        ...