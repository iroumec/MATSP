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

# def generate_output_file():
#     # Get the current local date and time as a datetime object.
#     now = datetime.now()

#     # Format the datetime object as a string (e.g., "YYYY-MM-DD HH:MM:SS")
#     time_string = now.strftime("%d-%m-%Y %H:%M:%S")
    
#     file_path = "outputs/" + time_string + ".txt"

#     with open(file_path, "w", encoding="UTF-8") as output_file:
#         output_file.write("=" * 50 + "\n")
#         output_file.write("GENETIC ALGORITHM PARAMETERS\n")
#         output_file.write("=" * 50 + "\n")
#         output_file.write(f"Population size: {POPULATION_SIZE}\n")
#         output_file.write(f"Percentage of random generated individual: {PERCENTAGE_OF_RANDOM_GENERATED_INDIVIDUALS}\n")
#         output_file.write(f"Max numbers of generations: {MAX_NUMBER_OF_GENERATIONS}\n")
#         output_file.write(f"Number of individuals selected: {NUMBER_OF_INVIDUALS_SELECTED}\n")
#         output_file.write(f"Torunament size: {TOURNAMENT_SIZE}\n")
#         output_file.write(f"Selection operator: {SELECTION_OPERATOR}\n")
#         output_file.write(f"Crossover operator: {CROSSOVER_OPERATOR}\n")
#         output_file.write(f"Crossover probability: {CROSSOVER_PROBABILITY}\n")
#         output_file.write(f"Mutation operator: {MUTATION_OPERATOR}\n")
#         output_file.write(f"Mutation probability: {MUTATION_PROBABILITY}\n")
#         output_file.write(f"Local search operator: {LOCAL_SEARCH_OPERATOR}\n")
#         output_file.write(f"Local search probability: {LOCAL_SEARCH_PROBABILITY}\n")
#         output_file.write(f"Survivors selection algorithm: {SURVIVORS_SELECTION_ALGORITHM}\n")
#         output_file.write(f"Number of individuals to replace: {NUMBER_OF_INDIVIDUALS_TO_REPLACE}\n")

#         output_file.write("\n=" * 50 + "\n")
#         output_file.write("BEST SOLUTION\n")
#         output_file.write("=" * 50 + "\n")
#         output_file.write(f"Best solution {result[0]["individual"]}")
#         output_file.write(f"Fitness value {result[0]["fitness"]}")

#         output_file.write("\n=" * 50 + "\n")
#         output_file.write("EXECUTION TIME\n")
#         output_file.write("=" * 50 + "\n")
#         output_file.write(f"Execution time: {execution_time}")
