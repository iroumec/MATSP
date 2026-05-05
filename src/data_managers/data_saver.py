import os
import matplotlib.pyplot as plt
from typing import List
from datetime import datetime

from configuration.structures import Config
from functions import calculate_cost

def save_output(
    config: Config,
    fitness_function,
    result,
    cost_matrix: List[List[int]],
    execution_time: float,
    best_fitness_through_time: List[float]
):
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

    # Base paths
    file_path = os.path.join(output_dir, f"{time_string}.txt")
    plot_path = os.path.join(output_dir, f"{time_string}.png")

    # Precalculation of values to keep f-strings clean.
    best_individual = result[0]['individual']
    best_fitness = fitness_function(best_individual, cost_matrix)
    best_cost = calculate_cost(best_individual, cost_matrix)

    # Writes the TXT file.
    with open(file_path, "w", encoding="UTF-8") as output_file:
        output_file.write("=" * 50 + "\n")
        output_file.write("GENETIC ALGORITHM PARAMETERS\n")
        output_file.write("=" * 50 + "\n")
        output_file.write(f"Instance:                   {config.execution.instance}\n")
        output_file.write(f"Population size:            {config.execution.population_size}\n")
        output_file.write(f"Random percentage:          {config.execution.random_percentage}\n")
        if config.stop_reasons.generations:
            output_file.write(f"Max generations:            {config.stop_reasons.max_generations}\n")
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
        output_file.write("=" * 50 + "\n")
        output_file.write("BEST SOLUTION\n")
        output_file.write("=" * 50 + "\n")
        output_file.write(f"Best solution:  {best_individual}\n")
        output_file.write(f"Fitness value:  {best_fitness}\n")
        output_file.write(f"Cost:           {best_cost}\n")

        output_file.write("\n")
        output_file.write("=" * 50 + "\n")
        output_file.write("EXECUTION TIME\n")
        output_file.write("=" * 50 + "\n")
        output_file.write(f"Execution time: {execution_time} seconds\n")

        output_file.write("\n")
        output_file.write("=" * 50 + "\n")
        output_file.write("BEST FITNESS THROUGH TIME\n")
        output_file.write("=" * 50 + "\n")
        for i, fitness_value in enumerate(best_fitness_through_time):
            output_file.write(f"{'Generation':<12}{i+1:>4d}: {fitness_value:12.7f}\n")
        output_file.write("=" * 50 + "\n")

    # Generates and saved a plot.
    plt.figure(figsize=(10, 6))

    # X axis (generations), Y axis (fitness).
    generations = list(range(1, len(best_fitness_through_time) + 1))
    plt.plot(generations, best_fitness_through_time, color='blue', linewidth=2)

    # Graphic style.
    plt.title(f"Convergence Curve - Instance: {config.execution.instance}", fontsize=14, fontweight='bold')
    plt.xlabel("Generation", fontsize=12)
    plt.ylabel("Best Fitness", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Margins adjustment.
    plt.tight_layout()

    # Save and close.
    plt.savefig(plot_path, dpi=300) # dpi=300 for high resolution.
    plt.close()

    return file_path
