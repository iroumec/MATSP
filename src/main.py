"""
Entry point for the genetic algorithm implementation.
"""

# ------------------------------------------------------------------------------------------------ #
# Imports
# ------------------------------------------------------------------------------------------------ #

import time

from configuration import build_config

from functions import (
    calculate_cost,
    calculate_fitness,
    select_best_individual
)

from data_managers import (
    load_matrix,
    load_config,
    save_output,
)

from operators import (
    InitializationStrategy,
)

# ------------------------------------------------------------------------------------------------ #
# Config Loading
# ------------------------------------------------------------------------------------------------ #

config = build_config(load_config("resources/configuration.example.yml"))

# ------------------------------------------------------------------------------------------------ #
# Variable definitions
# ------------------------------------------------------------------------------------------------ #

best_fitness_through_time = []

population = []

cost_matrix = load_matrix("ft53")

# ------------------------------------------------------------------------------------------------ #
# Timer initialization
# ------------------------------------------------------------------------------------------------ #

start_time: float = time.time()

# ------------------------------------------------------------------------------------------------ #
# Initial population generation
# ------------------------------------------------------------------------------------------------ #

number_of_random_generated_individuals = int(
    config.execution.random_percentage * config.execution.population_size
)

population += InitializationStrategy.RANDOMIZATION(
    number_of_random_generated_individuals,
    cost_matrix
)

number_of_heuristically_generated_individuals = (
    config.execution.population_size - number_of_random_generated_individuals
)

population += InitializationStrategy.NEAREST_NEIGHBOUR(
    number_of_heuristically_generated_individuals,
    cost_matrix
)

# ------------------------------------------------------------------------------------------------ #
# Algorithm
# ------------------------------------------------------------------------------------------------ #

current_generation: int = 0

while current_generation < config.execution.max_generations:

    # ------------------------------------------------------------------------------------------- #
    # Parents Selection
    # ------------------------------------------------------------------------------------------- #

    parents = config.selection.operator(
        population=population,
        fitness_function=calculate_fitness,
        num_selections=config.selection.selected_individuals,
        cost_matrix=cost_matrix,
        tournament_size=config.selection.tournament_size,
        # Only used if the selection algorithm is tournament.
    )

    # ------------------------------------------------------------------------------------------- #
    # Crossover
    # ------------------------------------------------------------------------------------------- #

    children = []

    for i in range(0, len(parents) - 1, 2):

        children += config.crossover.operator(
            parents[i],
            parents[i+1],
            config.crossover.probability
        )

    # ------------------------------------------------------------------------------------------- #
    # Mutation
    # ------------------------------------------------------------------------------------------- #

    children = [config.mutation.operator(child, config.mutation.probability) for child in children]

    # ------------------------------------------------------------------------------------------- #
    # Local search
    # ------------------------------------------------------------------------------------------- #

    children = [config.improvement.operator(
        child,
        config.improvement.probability,
        calculate_fitness,
        cost_matrix
    ) for child in children]

    # ------------------------------------------------------------------------------------------- #
    # Survivors selection
    # ------------------------------------------------------------------------------------------- #

    population = config.survivors.operator(
        population,
        children,
        config.survivors.individuals_to_replace,
        calculate_fitness,
        cost_matrix
    )

    # ------------------------------------------------------------------------------------------- #
    # Selecting the best solution of the current generation
    # ------------------------------------------------------------------------------------------- #

    best_fitness_through_time.append(
        select_best_individual(
            population,
            calculate_fitness,
            cost_matrix
        )
    )

    # ------------------------------------------------------------------------------------------- #
    # Increase of generation
    # ------------------------------------------------------------------------------------------- #

    current_generation += 1

# ----------------------------------------------------------------------------------------------- #
# Results creation
# ----------------------------------------------------------------------------------------------- #

result = []

for individual in population:

    result.append({
        "individual": individual,
        "cost": calculate_cost(individual, cost_matrix)
    })

# ----------------------------------------------------------------------------------------------- #
# Timer finalization
# ----------------------------------------------------------------------------------------------- #

end_time: float = time.time()
execution_time: float = end_time - start_time

# ----------------------------------------------------------------------------------------------- #
# Output saving
# ----------------------------------------------------------------------------------------------- #

output_path = save_output(
    config,
    calculate_fitness,
    result, cost_matrix,
    execution_time,
    best_fitness_through_time
)

print(f"Results saved in {output_path}!")
