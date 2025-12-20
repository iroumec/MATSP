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

# ----------------------------------------------------------------------------------------------- #
# Definición de constantes
# ----------------------------------------------------------------------------------------------- #

POPULATION_SIZE = 50

PERCENTAGE_OF_RANDOM_GENERATED_INDIVIDUALS = 0.8

MAX_NUMBER_OF_GENERATIONS = 1000

NUMBER_OF_INVIDUALS_SELECTED = 10

TOURNAMENT_SIZE = 2

NUMBER_OF_SURVIVORS = 10

SELECTION_ALGORITHM = tournament_selection

FITNESS_FUNCTION = fitness.calculate

CROSSOVER_FUNCTION = pmx

CROSSOVER_PROBABILITY = 0.9

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
# Algoritmo
# ----------------------------------------------------------------------------------------------- #

current_generation = 0

while current_generation < 1:
    
    # ------------------------------------------------------------------------------------------- #
    # Selección de padres
    # ------------------------------------------------------------------------------------------- #
    
    parents = SELECTION_ALGORITHM.tournament_selection(population, FITNESS_FUNCTION, NUMBER_OF_INVIDUALS_SELECTED, cost_matrix, TOURNAMENT_SIZE)
    
    print(parents)
    
    # ------------------------------------------------------------------------------------------- #
    # Cruce de padres
    # ------------------------------------------------------------------------------------------- #

    children = []

    for i in range(0, len(parents) - 1, 2):
        
        children += CROSSOVER_FUNCTION.crossover_pmx(parents[i], parents[i+1])
        
    print(children)
    
    # ------------------------------------------------------------------------------------------- #
    # Incremento de la generación
    # ------------------------------------------------------------------------------------------- #
    
    current_generation += 1