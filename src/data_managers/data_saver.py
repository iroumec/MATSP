"""
Output (summary and graphs) generation algorithms.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from dataclasses import dataclass
from matplotlib.lines import Line2D

from functions import calculate_cost
from configuration.structures import Config

# =============================================================================================== #
# Constants
# =============================================================================================== #

# ----------------------------------------------------------------------------------------------- #
# Generals
# ----------------------------------------------------------------------------------------------- #

SEPARATOR_LENGTH: int = 100

# ----------------------------------------------------------------------------------------------- #
# Related to the Plots
# ----------------------------------------------------------------------------------------------- #

DRAW_STD_LINES: bool = True
FILL_STD_LINES: bool = True
SUMMARY_FILE_NAME: str = "summary.md"
CONVERGENCE_PLOT_X_AXIS_LABEL: str = "Generation"
CONVERGENCE_PLOT_Y_AXIS_LABEL: str = "Average Best Fitness"
AVERAGE_EXECUTION_TIME_PLOT_TITLE: str = "Average Execution Time (Seconds)"

# =============================================================================================== #
# Dataclass
# =============================================================================================== #

@dataclass
class AlgorithmResult:

    """
    Dataclass for algorithm results.
    """

    configuration: Config
    fitness_function: callable
    best_individual: list[int]
    cost_matrix: list[list[int]]
    average_execution_time: float
    average_best_fitness_through_time: list[float]
    std_best_fitness_through_time: list[float]

# =============================================================================================== #
# Functions
# =============================================================================================== #

def save_output(algorithm_results: list[AlgorithmResult]):

    """
    Saves the execution parameters and results and generates a plot 
    of the best fitness through time.
    
    Args:
        algorithm_results (list[AlgorithmResult]): List of algorithm results.
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

    unique_file = len(algorithm_results) == 1

    if unique_file:
        _generate_individual_plot(algorithm_results[0], run_dir)
    elif algorithm_results:
        plot_path = os.path.join(run_dir, "comparison.png")
        _generate_combined_and_individuals_plots(algorithm_results, plot_path)

    # Generates TXT per configuration.
    for idx, algorithm_result in enumerate(algorithm_results):

        _generate_summary(
            idx,
            algorithm_result,
            unique_file,
            run_dir
        )

    return run_dir

# =============================================================================================== #

def _generate_summary(
    idx: int,
    algorithm_result: AlgorithmResult,
    unique_summary: bool,
    base_path: str,
):

    if unique_summary:
        file_path = os.path.join(base_path, SUMMARY_FILE_NAME)
    else:
        file_path = os.path.join(base_path, f"C{idx+1}_{SUMMARY_FILE_NAME}")

    # Writes the markdown file.
    with open(file_path, "w", encoding="UTF-8") as output_file:
        if unique_summary:
            output_file.write("# Configuration Summary\n\n")
        else:
            output_file.write(f"# Configuration C{idx+1} Summary\n\n")

        # Paramters summary.
        _generate_parameters_summary(algorithm_result, output_file)

        # Best solution summary.
        _generate_best_solution_summary(algorithm_result, output_file)

        # Execution time summary.
        _generate_execution_time_summary(algorithm_result, output_file)

        # Fitness through time summary.
        _generate_fitness_through_time_summary(algorithm_result, unique_summary, idx, output_file)

# =============================================================================================== #

def _generate_parameters_summary(algorithm_result: AlgorithmResult, output_file):

    config = algorithm_result.configuration

    output_file.write("## GENETIC ALGORITHM PARAMETERS\n\n")
    output_file.write("| Parameter | Value |\n")
    output_file.write("| :---------: | :-----: |\n")

    output_file.write(f"| Instance | {config.execution.instance} |\n")
    output_file.write(f"| Population Size | {config.execution.population_size} |\n")
    output_file.write(f"| Random Percentage | {config.execution.random_percentage} |\n")

    if config.stop_reasons.generations:
        output_file.write(f"| Max Generations | {config.stop_reasons.max_generations} |\n")

    if config.stop_reasons.generations_without_improvements:
        output_file.write(
            "| Max Generations without Improvements | "
            f"{config.stop_reasons.max_generations_without_improvements} |\n"
        )

    output_file.write(
        "| Selection Operator | "
        f"{config.selection.operator.name.upper()} |\n"
    )
    output_file.write(
        "| Selected Individuals | "
        f"{config.selection.selected_individuals} |\n"
    )

    if config.selection.operator.name.upper() == "TOURNAMENT":
        output_file.write(f"| Tournament Size | {config.selection.tournament_size} |\n")

    output_file.write(
        "| Crossover Operator | "
        f"{config.crossover.operator.name.upper()} |\n"
    )
    output_file.write(
        "| Crossover Probability | "
        f"{config.crossover.probability} |\n"
    )
    output_file.write(
        "| Mutation Operator | "
        f"{config.mutation.operator.name.upper()} |\n"
    )
    output_file.write(
        "| Mutation Probability | "
        f"{config.mutation.probability} |\n"
    )
    output_file.write(
        "| Local Search Operator | "
        f"{config.improvement.operator.name.upper()} |\n"
    )
    output_file.write(
        "| Local Search Probability | "
        f"{config.improvement.probability} |\n"
    )
    output_file.write(
        "| Survivors Operator | "
        f"{config.survivors.operator.name.upper().replace("_", " ")} |\n"
    )
    output_file.write(
        "| Individuals to Replace | "
        f"{config.survivors.individuals_to_replace} |\n"
    )

# =============================================================================================== #

def _generate_best_solution_summary(algorithm_result: AlgorithmResult, output_file):

    cost_matrix = algorithm_result.cost_matrix

    # Precalculation of values to keep f-strings clean.
    best_individual = algorithm_result.best_individual
    best_fitness = (
        algorithm_result
            .fitness_function(best_individual, cost_matrix)
    )
    best_cost = calculate_cost(best_individual, cost_matrix)

    output_file.write("\n## BEST SOLUTION\n\n")
    output_file.write("| Metric | Value |\n")
    output_file.write("| :------: | :-----: |\n")
    output_file.write(f"| Best Solution | {best_individual} |\n")
    output_file.write(f"| Fitness Value | {best_fitness} |\n")
    output_file.write(f"| Cost | {best_cost} |\n")

def _generate_execution_time_summary(algorithm_result: AlgorithmResult, output_file):

    multiprocessing_state = (
        "ON" if algorithm_result.configuration.execution.multiprocessing
            else "OFF"
    )
    execution_time = algorithm_result.average_execution_time

    output_file.write("\n## EXECUTION TIME\n\n")
    output_file.write("| Metric | Value |\n")
    output_file.write("| :------: | :-----: |\n")
    output_file.write(f"| Multiprocessing | {multiprocessing_state} |\n")
    output_file.write(f"| Average Execution Time (s) | {execution_time} |\n")

# =============================================================================================== #

def _generate_fitness_through_time_summary(
    algorithm_result: AlgorithmResult,
    unique_summary: bool,
    configuration_id: int,
    output_file
):

    best_fitness_through_time = algorithm_result.average_best_fitness_through_time

    output_file.write("\n## AVERAGE BEST FITNESS THROUGH TIME\n\n")

    if unique_summary:
        output_file.write("![convergence](./convergence.png)\n\n")
    else:
        output_file.write(f"![convergence](./C{configuration_id+1}_convergence.png)\n\n")

    output_file.write("| Generation | Fitness |\n")
    output_file.write("| :----------: | :-------: |\n")

    for i, fitness_value in enumerate(best_fitness_through_time):
        output_file.write(f"| {i+1} | {fitness_value:.7f} |\n")

# =============================================================================================== #

def _generate_combined_and_individuals_plots(algorithm_results: list[AlgorithmResult], path: str):

    fig = plt.figure(figsize=(12, 10))
    gs = fig.add_gridspec(2, 2)
    colours: list[str] = []
    instance = algorithm_results[0].configuration.execution.instance

    # ------------------------------------------------------------------------------------------- #
    # Top: Convergence Curves
    # ------------------------------------------------------------------------------------------- #

    ax1 = fig.add_subplot(gs[0, :])

    for idx, algorithm_result in enumerate(algorithm_results):
        best_fitness_through_time = algorithm_result.average_best_fitness_through_time
        std = algorithm_result.std_best_fitness_through_time
        generations = list(range(1, len(best_fitness_through_time) + 1))

        line, = ax1.plot(
            generations,
            best_fitness_through_time,
            linewidth=3,
            label=f"C{idx+1}"
        )

        # Lower and upper std lines.
        lower = [m - s for m, s in zip(best_fitness_through_time, std)]
        upper = [m + s for m, s in zip(best_fitness_through_time, std)]

        if FILL_STD_LINES:
            ax1.fill_between(generations, lower, upper, color=line.get_color(), alpha=0.1)

        if DRAW_STD_LINES:
            ax1.plot(generations, lower, linestyle="--", linewidth=0.5, color=line.get_color())
            ax1.plot(generations, upper, linestyle="--", linewidth=0.5, color=line.get_color())

        colours.append(line.get_color())

        _generate_individual_plot_optimized_for_combined_context(
            idx,
            instance,
            line,
            best_fitness_through_time,
            generations,
            lower,
            upper,
            os.path.dirname(path),
        )

    ax1.set_title(
        f"Convergence Curves - {instance}"
    )
    ax1.set_xlabel(CONVERGENCE_PLOT_X_AXIS_LABEL)
    ax1.set_ylabel(CONVERGENCE_PLOT_Y_AXIS_LABEL)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend()

    # ------------------------------------------------------------------------------------------- #
    # Bottom left: Best cost
    # ------------------------------------------------------------------------------------------- #

    ax2 = fig.add_subplot(gs[1, 0])

    labels: list[str] = []
    costs: list[int] = []

    for idx, result in enumerate(algorithm_results):
        labels.append(f"C{idx+1}")
        best_cost = calculate_cost(result.best_individual, result.cost_matrix)
        costs.append(best_cost)

    x = list(range(len(labels)))

    _generate_best_cost_graph(ax2, labels, costs, colours, x)

    # ------------------------------------------------------------------------------------------- #
    # Bottom right: Average execution time
    # ------------------------------------------------------------------------------------------- #

    ax3 = fig.add_subplot(gs[1, 1])

    times = [result.average_execution_time for result in algorithm_results]

    _generate_average_execution_time_graph(ax3, times, labels, colours, x)

    # ------------------------------------------------------------------------------------------- #
    # Save
    # ------------------------------------------------------------------------------------------- #

    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()

# =============================================================================================== #

def _generate_best_cost_graph(
    ax: Axes,
    labels: list[str],
    costs: list[str],
    colours: list[str],
    x: list[int]
):

    ax.bar(x, costs, color=colours)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title("Best Cost per Configuration")
    ax.bar_label(ax.containers[0])
    ax.grid(True, linestyle='--', alpha=0.7)

# =============================================================================================== #

def _generate_average_execution_time_graph(
    ax: Axes,
    times: list[float],
    labels: list[str],
    colours: list[str],
    x: list[int]
):

    ax.bar(x, times, color=colours)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title(AVERAGE_EXECUTION_TIME_PLOT_TITLE)
    ax.bar_label(ax.containers[0], fmt="%.2f")
    ax.grid(True, linestyle='--', alpha=0.7)

# =============================================================================================== #

def _generate_individual_plot(algorithm_result: AlgorithmResult, path: str):

    fig, ax = plt.subplots(figsize=(8, 5))
    instance = algorithm_result.configuration.execution.instance

    best_fitness_through_time = algorithm_result.average_best_fitness_through_time
    std = algorithm_result.std_best_fitness_through_time
    generations = list(range(1, len(best_fitness_through_time) + 1))

    line, = ax.plot(
        generations,
        best_fitness_through_time,
        linewidth=3,
    )

    # Lower and upper std lines.
    lower = [m - s for m, s in zip(best_fitness_through_time, std)]
    upper = [m + s for m, s in zip(best_fitness_through_time, std)]

    ax.plot(generations, best_fitness_through_time, linewidth=3, color=line.get_color())

    if FILL_STD_LINES:
        ax.fill_between(generations, lower, upper, color=line.get_color(), alpha=0.1)

    if DRAW_STD_LINES:
        ax.plot(generations, lower, linestyle="--", linewidth=0.5, color=line.get_color())
        ax.plot(generations, upper, linestyle="--", linewidth=0.5, color=line.get_color())

    ax.set_title(f"Convergence - {instance}")
    ax.set_xlabel(CONVERGENCE_PLOT_X_AXIS_LABEL)
    ax.set_ylabel(CONVERGENCE_PLOT_Y_AXIS_LABEL)
    ax.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(os.path.join(path, "convergence.png"), dpi=300)
    plt.close(fig)

# =============================================================================================== #

def _generate_individual_plot_optimized_for_combined_context(
    idx: int,
    instance: str,
    line: Line2D,
    best_fitness_through_time: list[float],
    generations,
    lower,
    upper,
    path: str,
):

    fig_i, ax_i = plt.subplots(figsize=(8, 5))

    ax_i.plot(generations, best_fitness_through_time, linewidth=3, color=line.get_color())

    if FILL_STD_LINES:
        ax_i.fill_between(generations, lower, upper, color=line.get_color(), alpha=0.1)

    if DRAW_STD_LINES:
        ax_i.plot(generations, lower, linestyle="--", linewidth=0.5, color=line.get_color())
        ax_i.plot(generations, upper, linestyle="--", linewidth=0.5, color=line.get_color())

    ax_i.set_title(f"Convergence C{idx+1} - {instance}")
    ax_i.set_xlabel(CONVERGENCE_PLOT_X_AXIS_LABEL)
    ax_i.set_ylabel(CONVERGENCE_PLOT_Y_AXIS_LABEL)
    ax_i.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(os.path.join(path, f"C{idx+1}_convergence.png"), dpi=300)
    plt.close(fig_i)

# =============================================================================================== #
