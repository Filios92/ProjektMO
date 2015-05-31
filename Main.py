from GraphManager import *
from GeneticAlgorithm import *
from DataGenerator import *

# Tests
data = DataGenerator(5)
data.create_graph()
testsuite_airports = data.get_airports()
testsuite_graph = data.get_graph()

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
