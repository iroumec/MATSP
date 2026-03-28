import random

from typing import List, Callable

def insertion(
    individual: List[int],
    probability: float,
    fitness_function: Callable,
    cost_matrix: List[List[int]]
) -> List[int]:
    
    """
    Docstring for insertion
    """

    p = random.random()
    
    best_individual = list(individual)

    if p < probability:

        best_fitness = fitness_function(best_individual, cost_matrix)

        number_of_elements = len(best_individual)

        index_to_remove = random.randint(0, number_of_elements - 1)
        element_removed = best_individual.pop(index_to_remove)
        
        best_index = index_to_remove
        
        # Se prueba de ubicar el elemento en cada uno de los índices.
        for index in range(number_of_elements):
            
            best_individual.insert(index, element_removed)
            
            current_fitness = fitness_function(best_individual, cost_matrix)
            
            if (current_fitness > best_fitness):
                best_fitness = current_fitness
                best_index = index
            
            best_individual.pop(index)
            
        best_individual.insert(best_index, element_removed)

    return best_individual