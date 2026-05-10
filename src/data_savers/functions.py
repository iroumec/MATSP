"""
Output (summary and graphs) generation algorithms.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import os
from tabulate import tabulate
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

from functions import calculate_cost
from .structures import AlgorithmResult

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
        plot_path = os.path.join(run_dir, "comparison")

        _generate_combined_and_individuals_plots(
            algorithm_results,
            f"{plot_path}_with_std.png",
            show_std=True
        )

        _generate_combined_and_individuals_plots(
            algorithm_results,
            f"{plot_path}_without_std.png",
            show_std=False
        )

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
    """
    Generates a markdown summary file for a single algorithm configuration.

    Args:
        idx (int): Index of the configuration (used for file naming when multiple configs exist).
        algorithm_result (AlgorithmResult): Result object containing the configuration,
            best individual, cost matrix, and fitness data.
        unique_summary (bool): If True, a single configuration is being summarized and the
            file is named 'summary.md'; otherwise it is named 'C{idx+1}_summary.md'.
        base_path (str): Directory path where the summary file will be saved.
    """

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

        # Parameters summary.
        _generate_parameters_summary(algorithm_result, output_file)

        # Best solution summary.
        _generate_best_solution_summary(algorithm_result, output_file)

        # Execution time summary.
        _generate_execution_time_summary(algorithm_result, output_file)

        # Fitness through time summary.
        _generate_fitness_through_time_summary(algorithm_result, unique_summary, idx, output_file)

# =============================================================================================== #

def _generate_parameters_summary(algorithm_result: AlgorithmResult, output_file):

    """
    Writes the genetic algorithm parameters section to the summary file.

    Args:
        algorithm_result (AlgorithmResult): Result object containing the algorithm configuration.
        output_file: Writable file object where the markdown content will be written.
    """

    config = algorithm_result.configuration

    output_file.write("## GENETIC ALGORITHM PARAMETERS\n\n")

    headers: list[str] = ["Parameter", "Value"]

    rows: list[list[any]] = [
        ["Instance", config.execution.instance],
        ["Population Size", config.execution.population_size],
        ["Random Percentage", config.execution.random_percentage],
    ]

    if config.stop_reasons.generations:
        rows.append(["Max Generations", config.stop_reasons.max_generations])

    if config.stop_reasons.generations_without_improvements:
        rows.append(
            [
                "Max Generations without Improvements",
                config.stop_reasons.max_generations_without_improvements
            ]
        )

    rows.extend([
        ["Selection Operator", f"{config.selection.operator.name.upper()}"],
        ["Selected Individuals", f"{config.selection.selected_individuals}"]
    ])

    if config.selection.operator.name.upper() == "TOURNAMENT":
        rows.append(["Tournament Size", config.selection.tournament_size])

    rows.extend([
        ["Crossover Operator", f"{config.crossover.operator.name.upper()}"],
        ["Crossover Probability", config.crossover.probability],
        ["Mutation Operator", f"{config.mutation.operator.name.upper()}"],
        ["Mutation Probability", config.mutation.probability],
        ["Local Search Operator", f"{config.improvement.operator.name.upper()}"],
        ["Local Search Probability", config.improvement.probability],
        ["Survivors Operator", f"{config.survivors.operator.name.upper().replace("_", " ")}"],
        ["Individuals to Replace", config.survivors.individuals_to_replace],
    ])

    _write_markdown_table(output_file, headers, rows)

# =============================================================================================== #

def _generate_best_solution_summary(algorithm_result: AlgorithmResult, output_file):

    """
    Writes the best solution section to the summary file, including the individual
    representation, its fitness value, and its cost.

    Args:
        algorithm_result (AlgorithmResult): Result object containing the best individual,
            cost matrix, and fitness function.
        output_file: Writable file object where the markdown content will be written.
    """

    cost_matrix = algorithm_result.cost_matrix

    # Precalculation of values to keep f-strings clean.
    best_individual = algorithm_result.best_individual
    best_fitness = (
        algorithm_result
            .fitness_function(best_individual, cost_matrix)
    )
    best_cost = calculate_cost(best_individual, cost_matrix)

    output_file.write("\n## BEST SOLUTION\n\n")

    output_file.write(f"```text\n{best_individual}\n```\n\n")

    headers: list[str] = ["Metric", "Value"]

    rows: list[list[any]] = [
        ["Fitness Value", best_fitness],
        ["Cost", best_cost]
    ]

    _write_markdown_table(output_file, headers, rows)

def _generate_execution_time_summary(algorithm_result: AlgorithmResult, output_file):

    """
    Writes the execution time section to the summary file, including the
    multiprocessing state and the average execution time.

    Args:
        algorithm_result (AlgorithmResult): Result object containing execution configuration
            and timing data.
        output_file: Writable file object where the markdown content will be written.
    """

    multiprocessing_state: str = (
        "ON" if algorithm_result.configuration.execution.multiprocessing
            else "OFF"
    )
    execution_time = algorithm_result.average_execution_time

    output_file.write("\n## EXECUTION TIME\n\n")

    headers: list[str] = ["Metric", "Value"]
    rows: list[list[any]] = [
        ["Multiprocessing", multiprocessing_state],
        ["Average Execution Time (seconds)", execution_time],
    ]

    _write_markdown_table(output_file, headers, rows)

# =============================================================================================== #

def _generate_fitness_through_time_summary(
    algorithm_result: AlgorithmResult,
    unique_summary: bool,
    configuration_id: int,
    output_file
):
    """
    Writes the average best fitness through time section to the summary file,
    including a reference to the convergence plot and a table of per-generation values.

    Args:
        algorithm_result (AlgorithmResult): Result object containing the fitness history.
        unique_summary (bool): If True, references 'convergence.png'; otherwise references
            'C{configuration_id+1}_convergence.png'.
        configuration_id (int): Index of the configuration, used to build the image reference
            when multiple configurations exist.
        output_file: Writable file object where the markdown content will be written.
    """

    best_fitness_through_time = algorithm_result.average_best_fitness_through_time

    output_file.write("\n## AVERAGE BEST FITNESS THROUGH TIME\n\n")

    if unique_summary:
        output_file.write("![convergence](./convergence.png)\n\n")
    else:
        output_file.write(f"![convergence](./C{configuration_id+1}_convergence.png)\n\n")

    headers: list[str] = ["Generation", "Average Best Fitness"]
    rows: list[list[any]] = []

    for i, fitness_value in enumerate(best_fitness_through_time):
        rows.append([str(i+1), f"{fitness_value:.7f}"])

    _write_markdown_table(output_file, headers, rows)

# =============================================================================================== #

def _write_markdown_table(output_file, headers: list[str], rows: list[list[any]]):

    """
    Formats and writes a markdown table to the output file.

    Args:
        output_file: Writable file object where the table will be written.
        headers (list[str]): Column header labels.
        rows (list[list[any]]): Table rows.
    """

    markdown = tabulate(
        rows,
        headers=headers,
        tablefmt="github",
        colalign=("center", "center")
    )

    output_file.write(markdown)
    output_file.write("\n")

# =============================================================================================== #

def _generate_combined_and_individuals_plots(
    algorithm_results: list[AlgorithmResult],
    path: str,
    show_std: bool,
):

    """
    Generates and saves a combined comparison figure containing convergence curves
    for all configurations, a best cost bar chart, and an average execution time bar chart.
    Also saves an individual convergence plot for each configuration.

    Args:
        algorithm_results (list[AlgorithmResult]): List of results for each configuration.
        path (str): Full file path where the combined comparison figure will be saved.
    """

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

        if show_std and FILL_STD_LINES:
            ax1.fill_between(generations, lower, upper, color=line.get_color(), alpha=0.1)

        if show_std and DRAW_STD_LINES:
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
    """
    Renders a bar chart of the best cost per configuration onto the given axes.

    Args:
        ax (Axes): Matplotlib axes object where the chart will be drawn.
        labels (list[str]): Configuration labels for the x-axis ticks (e.g. ['C1', 'C2']).
        costs (list[str]): Best cost value for each configuration.
        colours (list[str]): Bar colours, one per configuration.
        x (list[int]): Numeric x positions for each bar.
    """

    ax.bar(x, costs, color=colours)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title("Best Cost per Configuration")
    ax.bar_label(
        ax.containers[0],
        fontsize=8,
        padding=3,
        rotation=45
    )
    ax.margins(y=0.15)
    ax.grid(True, linestyle='--', alpha=0.7)

# =============================================================================================== #

def _generate_average_execution_time_graph(
    ax: Axes,
    times: list[float],
    labels: list[str],
    colours: list[str],
    x: list[int]
):
    """
    Renders a bar chart of the average execution time per configuration onto the given axes.

    Args:
        ax (Axes): Matplotlib axes object where the chart will be drawn.
        times (list[float]): Average execution time in seconds for each configuration.
        labels (list[str]): Configuration labels for the x-axis ticks (e.g. ['C1', 'C2']).
        colours (list[str]): Bar colours, one per configuration.
        x (list[int]): Numeric x positions for each bar.
    """

    ax.bar(x, times, color=colours)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title(AVERAGE_EXECUTION_TIME_PLOT_TITLE)
    ax.bar_label(
        ax.containers[0],
        fmt="%.2f",
        fontsize=8,
        padding=3,
        rotation=45
    )
    ax.margins(y=0.15)
    ax.grid(True, linestyle='--', alpha=0.7)

# =============================================================================================== #

def _generate_individual_plot(algorithm_result: AlgorithmResult, path: str):

    """
    Generates and saves a convergence plot for a single algorithm configuration,
    including standard deviation bands.

    Args:
        algorithm_result (AlgorithmResult): Result object containing the fitness history
            and standard deviation data.
        path (str): Directory path where 'convergence.png' will be saved.
    """

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
    """
    Generates and saves an individual convergence plot for a single configuration,
    reusing precomputed data from a combined plotting context to avoid redundant computation.

    Args:
        idx (int): Configuration index, used for the plot title and output filename.
        instance (str): Problem instance name, included in the plot title.
        line (Line2D): The line object from the combined plot, used to match the colour.
        best_fitness_through_time (list[float]): Average best fitness at each generation.
        generations: Sequence of generation indices for the x-axis.
        lower: Per-generation lower standard deviation bound.
        upper: Per-generation upper standard deviation bound.
        path (str): Directory path where 'C{idx+1}_convergence.png' will be saved.
    """

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
