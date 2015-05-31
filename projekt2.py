import math
import random

MAX_X = 200
MAX_Y = 200
SPEED = 8

# Manager base
class ManagerBase:
    """docstring for ManagerBase"""

    def __init__(self):
        self._array = []

    def add(self, element):
        self.get_next_index_for_array(element)
        self._array.append(element)
        return element.index

    @property
    def size(self):
        return len(self._array)

    def get_list(self):
        return self._array

    def get(self, index):
        return self._array[index]

    def get_index(self, element):
        return self._array.index(element)

    def get_next_index_for_array(self, element):
        element.set_index(len(self._array))

    def get_full(self, indeces):
        return list(x for x in self._array if x.index in indeces)


# Airport part
class Airport:
    """
    Class representing an airport.
    """

    def __init__(self, x=None, y=None):
        if x is None:
            self._x = random.random() * MAX_X
        else:
            self._x = x

        if y is None:
            self._y = random.random() * MAX_Y
        else:
            self._y = y

        self._index = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def index(self):
        return self._index

    def set_index(self, index):
        self._index = index

    def distance_to_airport(self, a):
        xDistance = math.fabs(a.x - self.x)
        yDistance = math.fabs(a.y - self.y)
        return math.sqrt(xDistance ** 2 + yDistance ** 2)

    def __repr__(self):
        # return 'Airport #{} x: {} y: {}'.format(self._index, self._x, self._y)
        return '{}'.format(self._index)


class AirportManager(ManagerBase):
    """
    Class representing an airport manager.
    """

    def __init__(self):
        super(AirportManager, self).__init__()


# Flight part
class Flight:
    """
    Class representing a flight.
    """

    def __init__(self, src, dst, departure_time, cost, index=None):
        self._src = src
        self._dst = dst
        self._departure_time = departure_time
        self._cost = cost
        self._duration = 0
        self._speed = SPEED
        self._duration = src.distance_to_airport(dst) / self._speed
        if index is not None:
            self._index = index

    @property
    def src(self):
        return self._src

    @property
    def dst(self):
        return self._dst

    @property
    def departure_time(self):
        return self._departure_time

    @property
    def cost(self):
        return self._cost

    @property
    def duration(self):
        return self._duration

    @property
    def index(self):
        return self._index

    def set_index(self, index):
        self._index = index

    def __repr__(self):
        # return 'Flight #{} x: {} y: {}'
        # .format(
        # 	self._index,
        # 	self._x,
        # 	self._y)
        return '{}'.format(self._index)


class FlightManager(ManagerBase):
    """
    Class representing an airport manager.
    """

    def __init__(self):
        super(FlightManager, self).__init__()


# Tour, specific solution, list of flight indeces / flights / airports
class Tour:
    """
    Class representing a tour.
    """

    def __init__(self, graph, start_idx, end_idx):
        self.graph = graph
        self.src_idx = start_idx
        self.dst_idx = end_idx
        self.flights = []

    def get_src(self):
        return self.src_idx

    def get_dst(self):
        return self.dst_idx

    def set_flights(self, flights):
        self.flights = flights;

    def is_valid(self):
        return True

    def get_cost(self):
        cost = 0
        # for flight in self.as_full_flights():
        # cost += flight.cost
        return cost

    def get_duration(self):
        # duration = 0;
        # old_one = None
        # for flight in self.flights:
        # 	duration += flight.duration
        # 	if old_one is None:
        # 		old_one = flight
        # 	else
        # 		duration += flight.departure_time - old_one.departure_time + old_one.duration
        # Different approach
        # TODO: check order?
        # flights = self.as_full_flights
        # duration = flights[-1].departure_time + flights[-1].duration - flights[0].departure_time
        return 0

    def get_size(self):
        return len(self.flights)

    def get_list(self):
        return self.flights

    def as_full_flights(self):
        full = self.graph.get_flight_manager().get_full(self.flights)
        return list(Airport(x) for x in full)

    # return []

    def as_airports(self):
        return self.graph.get_airport_manager().get_full(self.flights)

    # return []

    def airports_to_flights(self):
        pass

    def __repr__(self):
        return 'Tour from {} to {} \n\tflights: {}\n\tairports: {}\n\tfull: {}'.format(
            self.get_src(),
            self.get_dst(),
            self.get_list(),
            self.as_airports(),
            self.as_full_flights())


class GraphManager:
    """
    This is GraphManager class. It parses the test suites which are in lists format.
    """

    def __init__(self):
        self.flight_manager = FlightManager()
        self.airport_manager = AirportManager()
        self.graph = {}

    def get_flight_manager(self):
        return self.flight_manager

    def get_airport_manager(self):
        return self.airport_manager

    def get_graph(self):
        return self.graph

    # Graph as dict { src_airport_index : [ [ dst_index, departure_time, cost ] ] }
    def set_graph(self, graph, airport_suite=None):
        if airport_suite is not None:
            self.add_airport_suite(airport_suite)
        for x in graph:
            self.add_flight_suite_for_airport(x, graph[x])
        self.graph = graph

    # Suite as list of lists [ x, y ]
    def add_airport_suite(self, suite):
        for x in suite:
            coor_x = x[0]
            coor_y = x[1]
            self.airport_manager.add(Airport(coor_x, coor_y))

    # Suite as list of lists [ src_index, dst_index, departure_time, cost ]
    def add_flight_suite(self, suite):
        for x in suite:
            src = self.airport_manager.get(x[0])
            dst = self.airport_manager.get(x[1])
            departure_time = x[2]
            cost = x[3]
            self.flight_manager.add(Flight(src, dst, departure_time, cost))

    # Suite as list of lists [ dst_index, departure_time, cost ] + src airport index
    def add_flight_suite_for_airport(self, airport_index, suite):
        for x in suite:
            src = self.airport_manager.get(airport_index)
            dst = self.airport_manager.get(x[0])
            departure_time = x[1]
            cost = x[2]
            index = self.flight_manager.add(Flight(src, dst, departure_time, cost))
            x.insert(0, index)

    # Search graph
    # Return full arc / flight
    def find_path(self, start, end, path=[], flights=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            flights.pop()
            return None
        for node in self.graph[start]:
            if node[1] not in path:
                flights.append(node[0])
                newpath = self.find_path(node[1], end, path, flights)
                if newpath:
                    return newpath
                else:
                    flights.pop()
        # flights.pop()
        return None

    # Search graph with arc shuffling
    # Return full arc / flight
    def find_random_path(self, start, end, path=[], flights=[]):
        path = path + [start]
        if start == end:
            return flights
        if start not in self.graph:
            flights.pop()
            return None
        posibilities = self.graph[start]
        random.shuffle(posibilities)
        for node in posibilities:
            if node[1] not in path:
                flights.append(node[0])
                newpath = self.find_random_path(node[1], end, path, flights)
                if newpath: return newpath
        return None

    def print_airports(self):
        for x in self.airport_manager.get_list():
            print('Airport #{} at x = {:6.2f} y = {:6.2f}'
                .format(
                x.index,
                x.x,
                x.y))
        print('')

    def print_flights(self):
        for x in self.flight_manager.get_list():
            print('Flight #{} from {} to {} at {}h for {}$ and {:6.2f}'
                .format(
                x.index,
                self.airport_manager.get_index(x.src),
                self.airport_manager.get_index(x.dst),
                x.departure_time,
                x.cost,
                x.duration))
        print('')

    def print_graph(self):
        # print(self.graph)
        print('Graph:')
        for x in self.graph:
            print('Airport #{:2}'.format(x))
            for y in self.graph[x]:
                print('         {:2} dest: {:2} price: {:5} cost: {:5}'
                    .format(
                    y[0],
                    y[1],
                    y[2],
                    y[3]))
        print('')


class Population:
    """
    Manages a population of candidate tours
    """

    def __init__(self, population_size, graph, start_idx, end_idx, do_initialization=True):
        self.population_size = population_size
        self.tours = []
        if do_initialization:
            for x in range(1, population_size):
                # t = Tour(graph, start_idx, end_idx)
                # t.find_random_path()
                # t = graph.find_random_path()
                # self.tours.append(t)
                pass

    # Gets the best tour in the population
    def get_fittest(self):
        return Tour(None, 1, 2)


class GA:
    """
    Manages algorithms for evolving population
    """
    mutation_rate = 0.015
    tournament_size = 5
    elitism = True

    # Evolves a population over one generation
    def evolve_population(population):
        return population

    # Applies crossover to a set of parents and creates offspring
    def crossover(parent1, parent2):
        pass

    # Mutate a tour using swap mutation
    def mutate(tour):
        pass

    # Selects candidate tour for crossover
    def tournament_selection(population):
        pass

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


# blablabla TEST COMMIT

testsuite_tours = [
    [0, 1, 2, 3],
    [0, 2, 1, 3],
]

testsuite_graph = {
    0: [[3, 1800, 950], [2, 1100, 350], [2, 1600, 450]],
    1: [[2, 1200, 450]],
    2: [[1, 1600, 650], [0, 1400, 250], [3, 1400, 250], [4, 1100, 500]],
    3: [],
    4: [[2, 1322, 600], [1, 1000, 900]],
}

graph = GraphManager()
graph.set_graph(testsuite_graph, testsuite_airports)
graph.print_airports()
graph.print_flights()
graph.print_graph()

print('Graph finding tests')
t = Tour(graph, 0, 1)
t.set_flights(graph.find_path(0, 1))
print(t)

f = []
print(graph.find_path(2, 3, flights=f))
print(f)
# f=graph.find_random_path(1, 3)
# print(f)

# Parameters
params = {
    'start_idx': 1,
    'end_idx': 9,
    'max_flights': 5,
    'cost_weight': 0.2,
    'time_weight': 0.1,
    'pop_size': 5,
    'generations': 10
}

# Make popoulation
pop = Population(5, graph, params['start_idx'], params['end_idx'], True)

# Get best one
fittest = pop.get_fittest()
print('Initial\n\tduration: {}\n\tcost: {}\n\tflights: #{}: {}'
    .format(
    fittest.get_duration(),
    fittest.get_cost(),
    fittest.get_size(),
    fittest.get_list()))

# Transmutation!
pop = GA.evolve_population(pop)
for x in range(1, 10):
    pop = GA.evolve_population(pop)

# Get best best one
fittest = pop.get_fittest()
print('Finished')
print('Final\n\tduration: {}\n\tcost: {}\n\tflights: #{}: {}'
    .format(
    fittest.get_duration(),
    fittest.get_cost(),
    fittest.get_size(),
    fittest.get_list()))
