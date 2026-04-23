"""
Docstring for data_loader
"""

import yaml

file_path = "resources/atsp-instances/cleaned-instances/"

def load_matrix(instance):

    """
    Docstring for load_matrix
    
    :param file_path: Description
    """

    matrix = []

    with open(file_path + instance + ".atsp", "r", encoding="UTF-8") as matrix_file:
        for line in matrix_file:
            row = list(map(int, line.split()))
            matrix.append(row)

    return matrix

def load_config(path: str):
    
    """
    Docstring.
    """
    
    with open(path, "r", encoding="utf-8") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(f"An error ocurred while reading the YAML configuration: {exc}")
            return None