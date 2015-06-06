from GraphManager import *
from GeneticAlgorithm import *
from DataGenerator import *


load_q = input("Load from saved file? y/n\n")

if load_q == 'y':
    data = DataGenerator()
    data.load_saved_graph()
else:
    airport_q = int(input("How many airports shall be used to create graph?\n"))
    data = DataGenerator()
    data.load_new_data(airport_q)
    data.create_graph()
    data.save_graph()

testsuite_airports = data.get_airports()
testsuite_graph = data.get_graph()

graph = GraphManager()
graph.set_graph(testsuite_graph, testsuite_airports)
graph.print_airports()
graph.print_flights()
graph.print_graph()

# print('Graph finding tests')
# t = Tour(graph, 0, 1)
# t.find_path()
# print(t)

# t = Tour(graph, 0, 1)
# t.find_random_path()
# print(t)

# Parameters
params = {
    'start_idx'  : 1,
    'end_idx'    : 4,
    'max_flights': 5,
    'cost_weight': 0.2,
    'time_weight': 0.1,
    'pop_size'   : 10,
    'generations': 10
}

print(' === GeneticAlgorithm tests ===')
# Make popoulation
pop = Population(5, graph, params['start_idx'], params['end_idx'], True)

if not pop.tour_exists():
    print('Tour from {} to {} doesnt exist :('.format(pop.get_start_idx(), pop.get_end_idx()))

else:
    # Get best one
    fittest = pop.get_fittest()
    print('Initial {}'.format(fittest))

    # Transmutation!
    pop = GA.evolve_population(pop)
    for x in range(1,10):
        pop = GA.evolve_population(pop)

    # Get best best one
    fittest = pop.get_fittest()
    print('Finished')
    print('Final {}'.format(fittest))

    GA.mutate(fittest)