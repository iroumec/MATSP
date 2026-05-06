"""
Docstring
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import os
from typing import List
from datetime import datetime
import matplotlib.pyplot as plt
from dataclasses import dataclass

from functions import calculate_cost
from configuration.structures import Config

# =============================================================================================== #
# Constants
# =============================================================================================== #

SEPARATOR_LENGTH = 100

# =============================================================================================== #
# Dataclass
# =============================================================================================== #

@dataclass
class AlgorithmResult:
    """
    Docstring
    """
    configuration: Config
    fitness_function: callable
    best_individual: List[int]
    cost_matrix: List[List[int]]
    average_execution_time: float
    average_best_fitness_through_time: List[float]

# =============================================================================================== #
# Functions
# =============================================================================================== #

def save_output(algorithm_results: List[AlgorithmResult]):
    """
    Saves the execution parameters, results, and generates a plot 
    of the best fitness through time.
    """

    # Formats the datetime object as a safe string for filenames.
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Output directory creation.
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Execution directory creation.
    run_dir = os.path.join(output_dir, f"{time_string}")
    os.makedirs(run_dir, exist_ok=True)

    # Base paths.
    plot_path = os.path.join(run_dir, "comparison.png")

    # Generates TXT per configuration.
    for idx, algorithm_result in enumerate(algorithm_results):

        file_path = os.path.join(run_dir, f"config_{idx+1}.txt")

        # Result variables extraction.
        config = algorithm_result.configuration
        cost_matrix = algorithm_result.cost_matrix
        execution_time = algorithm_result.average_execution_time
        fitness_function = algorithm_result.fitness_function
        best_fitness_through_time = algorithm_result.average_best_fitness_through_time

        # Precalculation of values to keep f-strings clean.
        best_individual = algorithm_result.best_individual
        best_fitness = fitness_function(best_individual, cost_matrix)
        best_cost = calculate_cost(best_individual, cost_matrix)

        # Writes the TXT file.
        with open(file_path, "w", encoding="UTF-8") as output_file:
            output_file.write("=" * SEPARATOR_LENGTH + "\n")
            output_file.write("GENETIC ALGORITHM PARAMETERS\n")
            output_file.write("=" * SEPARATOR_LENGTH + "\n")
            output_file.write(f"Instance:                   {config.execution.instance}\n")
            output_file.write(f"Population size:            {config.execution.population_size}\n")
            output_file.write(f"Random percentage:          {config.execution.random_percentage}\n")
            if config.stop_reasons.generations:
                output_file.write(
                    "Max generations:            "
                    f"{config.stop_reasons.max_generations}\n"
                )
            if config.stop_reasons.generations_without_improvements:
                output_file.write(f"Max gens. no improvements:  {config.stop_reasons.max_generations_without_improvements}\n")
            output_file.write(f"Selection operator:         {config.selection.operator.name.upper()}\n")
            output_file.write(f"Selected individuals:       {config.selection.selected_individuals}\n")
            if (config.selection.operator.name.upper() == "TOURNAMENT"):
                output_file.write(f"Tournament size:            {config.selection.tournament_size}\n")
            output_file.write(f"Crossover operator:         {config.crossover.operator.name.upper()}\n")
            output_file.write(f"Crossover probability:      {config.crossover.probability}\n")
            output_file.write(f"Mutation operator:          {config.mutation.operator.name.upper()}\n")
            output_file.write(f"Mutation probability:       {config.mutation.probability}\n")
            output_file.write(f"Local search operator:      {config.improvement.operator.name.upper()}\n")
            output_file.write(f"Local search probability:   {config.improvement.probability}\n")
            output_file.write(f"Survivors operator:         {config.survivors.operator.name.upper()}\n")
            output_file.write(f"Individuals to replace:     {config.survivors.individuals_to_replace}\n")

            output_file.write("\n")
            output_file.write("=" * SEPARATOR_LENGTH + "\n")
            output_file.write("BEST SOLUTION\n")
            output_file.write("=" * SEPARATOR_LENGTH + "\n")
            output_file.write(f"Best solution:  {best_individual}\n")
            output_file.write(f"Fitness value:  {best_fitness}\n")
            output_file.write(f"Cost:           {best_cost}\n")

            output_file.write("\n")
            output_file.write("=" * SEPARATOR_LENGTH + "\n")
            output_file.write("EXECUTION TIME\n")
            output_file.write("=" * SEPARATOR_LENGTH + "\n")
            output_file.write(
                "Average execution time: "
                f"{execution_time} seconds\n"
            )

            output_file.write("\n")
            output_file.write("=" * SEPARATOR_LENGTH + "\n")
            output_file.write("AVERAGE BEST FITNESS THROUGH TIME\n")
            output_file.write("=" * SEPARATOR_LENGTH + "\n")

            for i, fitness_value in enumerate(best_fitness_through_time):
                output_file.write(f"{'Generation':<12}{i+1:>4d}: {fitness_value:12.7f}\n")
            output_file.write("=" * SEPARATOR_LENGTH + "\n")

    generate_plot(algorithm_results, plot_path)

    return run_dir

# =============================================================================================== #

def generate_plot(algorithm_results: List[AlgorithmResult], path: str):
    """
    Docstring
    """

    fig = plt.figure(figsize=(12, 10))
    gs = fig.add_gridspec(2, 2)
    colours = []

    # ------------------------------------------------------------------------------------------- #
    # Top: Convergence
    # ------------------------------------------------------------------------------------------- #

    ax1 = fig.add_subplot(gs[0, :])

    for idx, algorithm_result in enumerate(algorithm_results):
        best_fitness_through_time = algorithm_result.average_best_fitness_through_time
        generations = list(range(1, len(best_fitness_through_time) + 1))

        line, = ax1.plot(generations, best_fitness_through_time, linewidth=2, label=f"C{idx+1}")
        colours.append(line.get_color())

    ax1.set_title(
        f"Convergence - {algorithm_results[0].configuration.execution.instance}"
    )
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Average Best Fitness")
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend()

    # ------------------------------------------------------------------------------------------- #
    # Bottom left: Best cost
    # ------------------------------------------------------------------------------------------- #

    ax2 = fig.add_subplot(gs[1, 0])

    labels = []
    costs = []

    for idx, result in enumerate(algorithm_results):
        labels.append(f"C{idx+1}")
        best_cost = calculate_cost(result.best_individual, result.cost_matrix)
        costs.append(best_cost)

    x = list(range(len(labels)))

    ax2.bar(x, costs, color=colours)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels)
    ax2.set_title("Best Cost per Configuration")
    ax2.bar_label(ax2.containers[0])
    ax2.grid(True, linestyle='--', alpha=0.7)

    # ------------------------------------------------------------------------------------------- #
    # Bottom right: Average execution time
    # ------------------------------------------------------------------------------------------- #

    ax3 = fig.add_subplot(gs[1, 1])

    times = [result.average_execution_time for result in algorithm_results]

    ax3.bar(x, times, color=colours)
    ax3.set_xticks(x)
    ax3.set_xticklabels(labels)
    ax3.set_title("Average Execution Time (Seconds)")
    ax3.bar_label(ax3.containers[0], fmt="%.2f")
    ax3.grid(True, linestyle='--', alpha=0.7)

    # ------------------------------------------------------------------------------------------- #
    # Save
    # ------------------------------------------------------------------------------------------- #

    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
