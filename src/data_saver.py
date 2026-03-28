"""
Docstring for data_loader
"""

from datetime import datetime

def save_output(results):

    """
    Docstring for load_matrix
    
    :param file_path: Description
    """
    
    # Get the current local date and time as a datetime object.
    now = datetime.now()

    # Format the datetime object as a string (e.g., "YYYY-MM-DD HH:MM:SS")
    time_string = now.strftime("%d-%m-%Y %H:%M:%S")
    
    file_path = "outputs/" + time_string + ".txt"

    with open(file_path, "w", encoding="UTF-8") as output_file:
        output_file.write('\n'.join(str(item) for item in results))