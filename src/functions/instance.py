"""
Instance assert implementation.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from configuration.structures import Config

# =============================================================================================== #
# Function
# =============================================================================================== #

def assert_same_instance(configurations: list[Config]):

    """
    Checks that all configurations share the same instance. Otherwise, it raises an error.
    
    Args:
        configurations (list[Config]): List of configurations.
    """
    if not configurations:
        raise ValueError("ERROR: No configurations.")

    first_instance = configurations[0].execution.instance

    for configuration in configurations:
        if configuration.execution.instance != first_instance:
            raise ValueError("ERROR: Not all executions use the same instance.")

# =============================================================================================== #
