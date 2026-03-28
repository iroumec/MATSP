"""
Docstring for main
"""
import initialization.randomization as random_init
import initialization.nearest_neighbour as heuristically_init
import selection.tournament as tournament_selection
import fitness.fitness as fitness
import survivors.replace_worst as replace_worst
import data_loader as data_loader
import data_saver as data_saver
from crossover.common import cross_parents
from crossover.loader import load_crossover_operator
from mutation.common import mutate_population
from mutation.registry import get_mutation_operator, MutationStrategy

# ----------------------------------------------------------------------------------------------- #
# Definition of Parameters (only this can be changed)
# ----------------------------------------------------------------------------------------------- #

POPULATION_SIZE = 40

PERCENTAGE_OF_RANDOM_GENERATED_INDIVIDUALS = 0.8

MAX_NUMBER_OF_GENERATIONS = 1000

NUMBER_OF_INVIDUALS_SELECTED = 10

TOURNAMENT_SIZE = 3

SELECTION_ALGORITHM = tournament_selection

FITNESS_FUNCTION = fitness.calculate

CROSSOVER_OPERATOR= "pmx"

CROSSOVER_PROBABILITY = 0.9

MUTATION_OPERATOR = MutationStrategy.SWAP

MUTATION_PROBABILITY = 1/POPULATION_SIZE

LOCAL_SEARCH_OPERATOR = MutationStrategy.INVERTION

LOCAL_SEARCH_PROBABILITY = 0.8

SURVIVORS_SELECTION_ALGORITHM = replace_worst

NUMBER_OF_INDIVIDUALS_TO_REPLACE = 10

# ----------------------------------------------------------------------------------------------- #
# Load of Algorithms
# ----------------------------------------------------------------------------------------------- #

CROSSOVER_ALGORITHM = load_crossover_operator(CROSSOVER_OPERATOR)

MUTATION_ALGORITHM = get_mutation_operator(MUTATION_OPERATOR)

LOCAL_SEARCH_ALGORITHM = get_mutation_operator(LOCAL_SEARCH_OPERATOR)


# ----------------------------------------------------------------------------------------------- #
# Definición de variables
# ----------------------------------------------------------------------------------------------- #

population = []

cost_matrix = data_loader.load_matrix("p43")

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

while current_generation < MAX_NUMBER_OF_GENERATIONS:
    
    # ------------------------------------------------------------------------------------------- #
    # Parents Selection
    # ------------------------------------------------------------------------------------------- #
    
    parents = SELECTION_ALGORITHM.tournament_selection(population, FITNESS_FUNCTION, NUMBER_OF_INVIDUALS_SELECTED, cost_matrix, TOURNAMENT_SIZE)
    #parents = SELECTION_ALGORITHM.roulette_selection(population, FITNESS_FUNCTION, NUMBER_OF_INVIDUALS_SELECTED, cost_matrix)
    
    #print(parents)
    
    # ------------------------------------------------------------------------------------------- #
    # Crossover
    # ------------------------------------------------------------------------------------------- #

    children = []

    for i in range(0, len(parents) - 1, 2):
        # iría una probabilidad de cruce?
        children += cross_parents(parents[i], parents[i+1], CROSSOVER_PROBABILITY, CROSSOVER_ALGORITHM)
        
    #print(children)
    
    # ------------------------------------------------------------------------------------------- #
    # Mutation
    # ------------------------------------------------------------------------------------------- #
    
    #children = MUTATION_ALGORITHM.swap(children, MUTATION_PROBABILITY)
    children = mutate_population(children, MUTATION_PROBABILITY, MUTATION_ALGORITHM)
    
    #print(children)
    
    # ------------------------------------------------------------------------------------------- #
    # Local search
    # ------------------------------------------------------------------------------------------- #
    
    children = mutate_population(children, LOCAL_SEARCH_PROBABILITY, LOCAL_SEARCH_ALGORITHM)
    
    #print(children)
    
    # ------------------------------------------------------------------------------------------- #
    # Survivors selection
    # ------------------------------------------------------------------------------------------- #

    #print("\n")
    #print(population)
    population = replace_worst.replace_worst(population, children, NUMBER_OF_INDIVIDUALS_TO_REPLACE, FITNESS_FUNCTION, cost_matrix)
    #print(population)

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
    
result = []
    
for individual in population:
    
    # print(calculate_cost(individual, cost_matrix))
    result.append(calculate_cost(individual, cost_matrix))

print(result)

data_saver.save_output(result)

import customtkinter

def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()