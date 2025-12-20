"""
Docstring for data_loader
"""

def load_matrix(file_path):

    """
    Docstring for load_matrix
    
    :param file_path: Description
    """

    matrix = []

    with open(file_path, "r", encoding="UTF-8") as matrix_file:
        for line in matrix_file:
            row = list(map(int, line.split()))
            matrix.append(row)

    return matrix
