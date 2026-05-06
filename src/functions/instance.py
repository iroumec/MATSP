"""
Docstring
"""

from typing import List
from configuration.structures import Config

def assert_same_instance(configurations: List[Config]) -> bool:
    """
    Docstring
    """
    if not configurations:
        raise ValueError("ERROR: No configurations.")

    first_instance = configurations[0].execution.instance

    for configuration in configurations:
        if configuration.execution.instance != first_instance:
            raise ValueError("ERROR: Not all executions use the same instance.")
