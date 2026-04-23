"""
Docstring for data_loader
"""

from typing import List
from datetime import datetime

from configuration.structures import Config

def save_output(
    config: Config,
    fitness_function,
    result, cost_matrix: List[List[int]],
    execution_time: float,
    best_fitness_through_time: List[float]
):

    """
    Docstring for load_matrix
    
    :param file_path: Description
    """
    
    # Get the current local date and time as a datetime object.
    now = datetime.now()

    # Format the datetime object as a string (e.g., "DD-MM-YYYY HH:MM:SS").
    time_string = now.strftime("%d-%m-%Y %H:%M:%S")
    
    file_path = "outputs/" + time_string + ".txt"

    with open(file_path, "w", encoding="UTF-8") as output_file:
        output_file.write("=" * 50 + "\n")
        output_file.write("GENETIC ALGORITHM PARAMETERS\n")
        output_file.write("=" * 50 + "\n")
        output_file.write(f"Population size: {config.execution.population_size}\n")
        output_file.write(f"Percentage of random generated individual: {config.execution.random_percentage}\n")
        output_file.write(f"Max numbers of generations: {config.execution.max_generations}\n")
        output_file.write(f"Number of individuals selected: {config.selection.selected_individuals}\n")
        output_file.write(f"Selection operator: {config.selection.operator.__name__.upper()}\n")
        if (config.selection.operator.__name__.upper() == "TOURNAMENT"):
            output_file.write(f"Torunament size: {config.selection.tournament_size}\n")
        output_file.write(f"Crossover operator: {config.crossover.operator.__name__.upper()}\n")
        output_file.write(f"Crossover probability: {config.crossover.probability}\n")
        output_file.write(f"Mutation operator: {config.mutation.operator.__name__.upper()}\n")
        output_file.write(f"Mutation probability: {config.mutation.probability}\n")
        output_file.write(f"Local search operator: {config.improvement.operator.__name__.upper()}\n")
        output_file.write(f"Local search probability: {config.improvement.probability}\n")
        output_file.write(f"Survivors selection operator: {config.survivors.operator.__name__.upper()}\n")
        output_file.write(f"Number of individuals to replace: {config.survivors.individuals_to_replace}\n")

        output_file.write("\n")
        output_file.write("=" * 50 + "\n")
        output_file.write("BEST SOLUTION\n")
        output_file.write("=" * 50 + "\n")
        output_file.write(f"Best solution {result[0]["individual"]}\n")
        output_file.write(f"Fitness value {fitness_function(result[0]["individual"], cost_matrix)}\n")

        output_file.write("\n")
        output_file.write("=" * 50 + "\n")
        output_file.write("EXECUTION TIME\n")
        output_file.write("=" * 50 + "\n")
        output_file.write(f"Execution time: {execution_time}\n")

        output_file.write("\n")
        output_file.write("=" * 50 + "\n")
        output_file.write("BEST FITNESS THROUGH TIME\n")
        for i, fitness_value in enumerate(best_fitness_through_time):
            output_file.write(f"Generation {i+1}: {round(fitness_value, 7)}\n")
        output_file.write("=" * 50 + "\n")