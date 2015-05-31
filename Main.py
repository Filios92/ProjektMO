import math
import random

from Airport import *
from Flight import *
from Tour import *
from GraphManager import *
from GeneticAlgorithm import *

# Tests
testsuite_airports = [
    [10, 20],
    [20, 40],
    [20, 50],
    [30, 20],
    [None, 20],
]

testsuite_flights = [
    [0, 2, 1100, 350],
    [1, 2, 1200, 450],
    [2, 1, 1600, 650],
    [2, 0, 1400, 250],
    [2, 3, 1400, 250],
    [0, 3, 1800, 950],
    [4, 2, 1100, 950],
]

testsuite_tours = [
    [0, 1, 2, 3],
    [0, 2, 1, 3],
]

testsuite_graph = {
    0: [ [3, 1800, 950], [2, 1100, 350], [2, 1600, 450] ],
    1: [ [2, 1200, 450] ],
    2: [ [1, 1600, 650], [0, 1400, 250], [3, 1400, 250], [4, 1100, 500] ],
    3: [  ],
    4: [ [2, 1322, 600], [1, 1000, 900] ],
}

graph = GraphManager()
graph.set_graph(testsuite_graph, testsuite_airports)
graph.print_airports()
graph.print_flights()
graph.print_graph()

print('Graph finding tests')
t = Tour(graph, 0, 1)
t.find_path()
print(t)

t = Tour(graph, 0, 1)
t.find_random_path()
print(t)

# Parameters
params = {
    'start_idx'  : 1,
    'end_idx'    : 9,
    'max_flights': 5,
    'cost_weight': 0.2,
    'time_weight': 0.1,
    'pop_size'   : 5,
    'generations': 10
}

# Make popoulation
# pop = Population(5, graph, params['start_idx'], params['end_idx'], True)

# Get best one
# fittest = pop.get_fittest()
# print('Initial\n\tduration: {}\n\tcost: {}\n\tflights: #{}: {}'
#     .format(
#         fittest.get_duration(),
#         fittest.get_cost(),
#         fittest.get_size(),
#         fittest.get_list()))

# # Transmutation!
# pop = GA.evolve_population(pop)
# for x in range(1,10):
#     pop = GA.evolve_population(pop)

# # Get best best one
# fittest = pop.get_fittest()
# print('Finished')
# print('Final\n\tduration: {}\n\tcost: {}\n\tflights: #{}: {}'
#     .format(
#         fittest.get_duration(),
#         fittest.get_cost(),
#         fittest.get_size(),
#         fittest.get_list()))
