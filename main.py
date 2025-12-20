"""
Docstring for main
"""
import initialization.randomization as random_init
import initialization.nearest_neighbour as heuristically_init
import selection.tournament as tournament_selection
import selection.roulette as roulette_selection
import fitness.fitness as fitness
import crossover.pmx as pmx
import crossover.ox1 as ox1
import mutation.swap as swap
import mutation.scramble as scramble
import local_search.invertion as invertion
import survivors.replace_worst as replace_worst

# ----------------------------------------------------------------------------------------------- #
# Definición de constantes
# ----------------------------------------------------------------------------------------------- #

POPULATION_SIZE = 10

PERCENTAGE_OF_RANDOM_GENERATED_INDIVIDUALS = 0.8

MAX_NUMBER_OF_GENERATIONS = 1000

NUMBER_OF_INVIDUALS_SELECTED = 10

TOURNAMENT_SIZE = 2

NUMBER_OF_SURVIVORS = 10

SELECTION_ALGORITHM = tournament_selection

FITNESS_FUNCTION = fitness.calculate

CROSSOVER_FUNCTION = pmx

CROSSOVER_PROBABILITY = 0.9

MUTATION_ALGORITHM = swap

MUTATION_PROBABILITY = 0.7

LOCAL_SEARCH_ALGORITHM = invertion

LOCAL_SEARCH_PROBABILITY = 0.7

SURVIVORS_SELECTION_ALGORITHM = replace_worst

NUMBER_OF_INDIVIDUALS_TO_REPLACE = 10

# ----------------------------------------------------------------------------------------------- #
# Definición de variables
# ----------------------------------------------------------------------------------------------- #

population = []

cost_matrix = [
    [0.3, 4.5, 6.7, 8.9],
    [1.4, 6.7, 5.3, 2.1],
    [1.4, 6.7, 5.3, 2.1],
    [1.4, 6.7, 5.3, 2.1]
]

# ----------------------------------------------------------------------------------------------- #
# Generación de la población inicial
# ----------------------------------------------------------------------------------------------- #

number_of_random_generated_individuals = int(PERCENTAGE_OF_RANDOM_GENERATED_INDIVIDUALS * POPULATION_SIZE)
population += random_init.initialize(number_of_random_generated_individuals, cost_matrix)

#print(population)

number_of_heuristically_generated_individuals = POPULATION_SIZE - number_of_random_generated_individuals
population += heuristically_init.initialize(number_of_heuristically_generated_individuals, cost_matrix)

#print(population)

# ----------------------------------------------------------------------------------------------- #
# Algorithm
# ----------------------------------------------------------------------------------------------- #

current_generation = 0

while current_generation < 1:
    
    # ------------------------------------------------------------------------------------------- #
    # Parents Selection
    # ------------------------------------------------------------------------------------------- #
    
    parents = SELECTION_ALGORITHM.tournament_selection(population, FITNESS_FUNCTION, NUMBER_OF_INVIDUALS_SELECTED, cost_matrix, TOURNAMENT_SIZE)
    
    print(parents)
    
    # ------------------------------------------------------------------------------------------- #
    # Crossover
    # ------------------------------------------------------------------------------------------- #

    children = []

    for i in range(0, len(parents) - 1, 2):
        # iría una probabilidad de cruce?
        children += CROSSOVER_FUNCTION.crossover_pmx(parents[i], parents[i+1])
        
    print(children)
    
    # ------------------------------------------------------------------------------------------- #
    # Mutation
    # ------------------------------------------------------------------------------------------- #
    
    children = MUTATION_ALGORITHM.swap(children, MUTATION_PROBABILITY)
    
    print(children)
    
    # ------------------------------------------------------------------------------------------- #
    # Local search
    # ------------------------------------------------------------------------------------------- #
    
    children = LOCAL_SEARCH_ALGORITHM.invert(children, LOCAL_SEARCH_PROBABILITY)
    
    print(children)
    
    # ------------------------------------------------------------------------------------------- #
    # Survivors selection
    # ------------------------------------------------------------------------------------------- #

    print("\n")
    print(population)
    population = replace_worst.replace_worst(population, children, NUMBER_OF_INDIVIDUALS_TO_REPLACE, FITNESS_FUNCTION, cost_matrix)
    print(population)

    # ------------------------------------------------------------------------------------------- #
    # Increase of generation
    # ------------------------------------------------------------------------------------------- #
    
    current_generation += 1