"""
Docstring for data_loader
"""

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
