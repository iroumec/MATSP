"""
Docstring for mutation.loader
"""
import importlib

def load_crossover_operator(name: str):
    """
    Docstring for load_mutation_operator
    
    :param name: Description
    :type name: str
    """
    module = importlib.import_module(f"crossover.{name}")
    return getattr(module, name)
