"""
Docstring for data_loader
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from typing import List

import yaml

# =============================================================================================== #
# Constants
# =============================================================================================== #

INSTANCES_PATH = "resources/atsp-instances/cleaned-instances/"

# =============================================================================================== #
# Functions
# =============================================================================================== #

def load_matrix(instance: str) -> List[List[int]]:

    """
    Loads an instance's matrix.

    Args:
        instance (str): Instance's name.
    
    Returns:
        matrix (List[List[int]]): Instance's cost matrix.
    """

    matrix = []

    with open(INSTANCES_PATH + instance + ".atsp", "r", encoding="UTF-8") as matrix_file:
        for line in matrix_file:
            row = list(map(int, line.split()))
            matrix.append(row)

    return matrix

# =============================================================================================== #

def load_config(path: str) -> any:

    """
    Loads a YAML configuration.
    
    Args:
        path (srt): Configuration path.

    Returns:
        stream (any): If the YAML file is valid, it returns its stream
    """

    with open(path, "r", encoding="utf-8") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise ValueError(
                f"UNEXPECTED ERROR: Could not read the YAML configuration: {exc}."
            ) from exc

# =============================================================================================== #
