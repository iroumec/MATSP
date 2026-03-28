"""
Docstring for main
"""
from datetime import datetime
import time

import fitness.fitness as fitness
import survivors.replace_worst as replace_worst
import data_loader as data_loader
import data_saver as data_saver
from initialization.registry import InitializationStrategy
from crossover.registry import get_crossover_operator, CrossoverStrategy
from selection.registry import get_operator, SelectionStrategy
from mutation.registry import MutationStrategy
from improvement.registry import ImprovementStrategy

# ----------------------------------------------------------------------------------------------- #
# Definition of Parameters (only this can be changed)
# ----------------------------------------------------------------------------------------------- #

POPULATION_SIZE = 40

PERCENTAGE_OF_RANDOM_GENERATED_INDIVIDUALS = 0.8

MAX_NUMBER_OF_GENERATIONS = 1000

NUMBER_OF_INVIDUALS_SELECTED = 10

TOURNAMENT_SIZE = 3

SELECTION_OPERATOR = SelectionStrategy.TOURNAMENT

FITNESS_FUNCTION = fitness.calculate

CROSSOVER_OPERATOR= CrossoverStrategy.PMX

CROSSOVER_PROBABILITY = 0.9

MUTATION_OPERATOR = MutationStrategy.SWAP

MUTATION_PROBABILITY = 1/POPULATION_SIZE

LOCAL_SEARCH_OPERATOR = ImprovementStrategy.INSERTION

LOCAL_SEARCH_PROBABILITY = 0.8

SURVIVORS_SELECTION_ALGORITHM = replace_worst.replace_worst

NUMBER_OF_INDIVIDUALS_TO_REPLACE = 10

# ----------------------------------------------------------------------------------------------- #
# Load of Algorithms
# ----------------------------------------------------------------------------------------------- #

SELECTION_ALGORITHM = get_operator(SELECTION_OPERATOR)

CROSSOVER_ALGORITHM = get_crossover_operator(CROSSOVER_OPERATOR)

LOCAL_SEARCH_ALGORITHM = LOCAL_SEARCH_OPERATOR

# ----------------------------------------------------------------------------------------------- #
# Definición de variables
# ----------------------------------------------------------------------------------------------- #

best_fitness_through_time = []

population = []

cost_matrix = data_loader.load_matrix("p43")

# ----------------------------------------------------------------------------------------------- #
# Inicio del Contador
# ----------------------------------------------------------------------------------------------- #

start_time = time.time()

# ----------------------------------------------------------------------------------------------- #
# Generación de la población inicial
# ----------------------------------------------------------------------------------------------- #

number_of_random_generated_individuals = int(PERCENTAGE_OF_RANDOM_GENERATED_INDIVIDUALS * POPULATION_SIZE)
population += InitializationStrategy.RANDOMIZATION(number_of_random_generated_individuals, cost_matrix)

#print(population)

number_of_heuristically_generated_individuals = POPULATION_SIZE - number_of_random_generated_individuals
population += InitializationStrategy.NEAREST_NEIGHBOUR(number_of_heuristically_generated_individuals, cost_matrix)

#print(population)

# ----------------------------------------------------------------------------------------------- #
# Algorithm
# ----------------------------------------------------------------------------------------------- #

current_generation = 0

while current_generation < MAX_NUMBER_OF_GENERATIONS:
    
    # ------------------------------------------------------------------------------------------- #
    # Parents Selection
    # ------------------------------------------------------------------------------------------- #
    
    parents = SELECTION_ALGORITHM(
        population=population,
        fitness_function=FITNESS_FUNCTION,
        num_selections=NUMBER_OF_INVIDUALS_SELECTED,
        cost_matrix=cost_matrix,
        tournament_size=TOURNAMENT_SIZE, # Only used if the selection algorithm is tournament.
    )
    
    # ------------------------------------------------------------------------------------------- #
    # Crossover
    # ------------------------------------------------------------------------------------------- #

    children = []

    for i in range(0, len(parents) - 1, 2):
        
        children += CROSSOVER_ALGORITHM(
            parents[i],
            parents[i+1],
            CROSSOVER_PROBABILITY
        )

    # ------------------------------------------------------------------------------------------- #
    # Mutation
    # ------------------------------------------------------------------------------------------- #
    
    children = [MUTATION_OPERATOR(child, MUTATION_PROBABILITY) for child in children]

    # ------------------------------------------------------------------------------------------- #
    # Local search
    # ------------------------------------------------------------------------------------------- #

    children = [LOCAL_SEARCH_OPERATOR(
        child,
        LOCAL_SEARCH_PROBABILITY,
        FITNESS_FUNCTION,
        cost_matrix
    ) for child in children]

    # ------------------------------------------------------------------------------------------- #
    # Survivors selection
    # ------------------------------------------------------------------------------------------- #

    population = replace_worst.replace_worst(population, children, NUMBER_OF_INDIVIDUALS_TO_REPLACE, FITNESS_FUNCTION, cost_matrix)
    #print(population)

    # ------------------------------------------------------------------------------------------- #
    # Selecting the best solution of the current generation
    # ------------------------------------------------------------------------------------------- #

    # best_fitness_through_time.append()
    
    # ------------------------------------------------------------------------------------------- #
    # Increase of generation
    # ------------------------------------------------------------------------------------------- #
    
    current_generation += 1
    
def calculate_cost(individual, cost_matrix):

    """
    Docstring for calculate
    
    :param individual: Description
    :param cost_matrix: Description
    """

    number_of_cities = len(individual)

    travel_cost = 0

    for city in range(number_of_cities - 1):

        travel_cost += cost_matrix[individual[city]][individual[city+1]]
        
    travel_cost += cost_matrix[individual[number_of_cities - 1]][individual[0]]

    return travel_cost
    
    
raw_result = []
result = []
    
for individual in population:
    
    # print(calculate_cost(individual, cost_matrix))
    raw_result.append(calculate_cost(individual, cost_matrix))
    result.append({
        "individual": individual,
        "fitness": calculate_cost(individual, cost_matrix)
    })

print(raw_result)

# data_saver.save_output(result)

# ----------------------------------------------------------------------------------------------- #
# Fin del Contador
# ----------------------------------------------------------------------------------------------- #

end_time = time.time()
execution_time = end_time - start_time

print(execution_time)

def generate_output_file():
    # Get the current local date and time as a datetime object.
    now = datetime.now()

    # Format the datetime object as a string (e.g., "YYYY-MM-DD HH:MM:SS")
    time_string = now.strftime("%d-%m-%Y %H:%M:%S")
    
    file_path = "outputs/" + time_string + ".txt"

    with open(file_path, "w", encoding="UTF-8") as output_file:
        output_file.write("=" * 50 + "\n")
        output_file.write("GENETIC ALGORITHM PARAMETERS\n")
        output_file.write("=" * 50 + "\n")
        output_file.write(f"Population size: {POPULATION_SIZE}\n")
        output_file.write(f"Percentage of random generated individual: {PERCENTAGE_OF_RANDOM_GENERATED_INDIVIDUALS}\n")
        output_file.write(f"Max numbers of generations: {MAX_NUMBER_OF_GENERATIONS}\n")
        output_file.write(f"Number of individuals selected: {NUMBER_OF_INVIDUALS_SELECTED}\n")
        output_file.write(f"Torunament size: {TOURNAMENT_SIZE}\n")
        output_file.write(f"Selection operator: {SELECTION_OPERATOR.name}\n")
        output_file.write(f"Crossover operator: {CROSSOVER_OPERATOR.name}\n")
        output_file.write(f"Crossover probability: {CROSSOVER_PROBABILITY}\n")
        output_file.write(f"Mutation operator: {MUTATION_OPERATOR.name}\n")
        output_file.write(f"Mutation probability: {MUTATION_PROBABILITY}\n")
        output_file.write(f"Local search operator: {LOCAL_SEARCH_OPERATOR.__name__.upper()}\n")
        output_file.write(f"Local search probability: {LOCAL_SEARCH_PROBABILITY}\n")
        output_file.write(f"Survivors selection algorithm: {SURVIVORS_SELECTION_ALGORITHM.__name__.upper()}\n")
        output_file.write(f"Number of individuals to replace: {NUMBER_OF_INDIVIDUALS_TO_REPLACE}\n")

        output_file.write("\n")
        output_file.write("=" * 50 + "\n")
        output_file.write("BEST SOLUTION\n")
        output_file.write("=" * 50 + "\n")
        output_file.write(f"Best solution {result[0]["individual"]}\n")
        output_file.write(f"Fitness value {result[0]["fitness"]}\n")

        output_file.write("\n")
        output_file.write("=" * 50 + "\n")
        output_file.write("EXECUTION TIME\n")
        output_file.write("=" * 50 + "\n")
        output_file.write(f"Execution time: {execution_time}\n")

generate_output_file()