from GeneticAlgorithm import *
from Airport import *
from Flight import *

# Tour, specific solution, list of flight indeces / flights / airports
class Tour:
    """
    Class representing a tour.
    """
    # Adjust
    COST_TO_DURATION_RATIO = 100

    def __init__(self, graph, start_idx, end_idx):
        self.graph   = graph
        self.src_idx = start_idx
        self.dst_idx = end_idx
        self.flights = []
        self.duration = 0
        self.cost = 0
        self.fitness = 0

    def make_basic_copy(self):
        return Tour(self.graph, self.src_idx, self.dst_idx)

    def get_src(self):
        return self.src_idx

    def get_dst(self):
        return self.dst_idx

    def set_flights(self, flights):
        self.flights  = flights;
        self.duration = 0
        self.cost     = 0

    def is_valid(self):
        return len(self.as_airports()) == len(set(self.as_airports()))

    def get_cost(self):
        if not self.cost:
            self.cost = 0
            for flight in self.as_flights_full():
                self.cost += flight.cost

        return self.cost

    def get_duration(self):
        if not self.duration:
            first = True
            duration = 0;

            for flight in self.as_flights_full():
                if not first:
                    # ...and wait...
                    wait_for = (flight.departure_time - current_time) % 24
                    # print('We wait :( for {}'.format(wait_for))
                    duration     += wait_for
                    current_time += wait_for
                    current_time %= 24
                    # print('and now it\'s {}'.format(current_time))
                else:
                    # First, we get to the airport...
                    current_time = flight.departure_time
                    # print('We got to the airport! It\'s {}'.format(current_time))
                    first = False
                # ...we fly...
                duration     += flight.duration
                # print('  We\'re flying for {}'.format(flight.duration))
                # ...we land...
                current_time += flight.duration
                current_time %= 24
                # print('  We have landed! <claps_a_lot> It\'s {}'.format(current_time))

            # print('We\'re done... \n')
            self.duration = duration

        return self.duration

    def get_graph(self):
        return self.graph

    def get_size(self):
        return len(self.flights)

    def as_flights_idx(self):
        return self.flights

    def as_flights_full(self):
        if self.flights:
            return self.graph.get_flight_manager().get_full(self.flights) if self.flights else None
        else:
            return []

    def as_airports(self):
        return [self.src_idx] + list(x.dst.index for x in self.as_flights_full()) if self.flights else None

    def airports_to_flights(self):
        pass

    def find_path(self):
        self.set_flights(self.graph.find_path(self.src_idx, self.dst_idx))

    def find_random_path(self):
        a = self.graph.find_random_path(self.src_idx, self.dst_idx)
        self.set_flights(a)

    def get_fitness(self, time_weight, cost_weight, max_flights):
        if self.fitness:
            return self.fitness
        else:
            if not self.flights:
                return 0
                
            # Lower is better
            f = cost_weight * self.get_cost() + Tour.COST_TO_DURATION_RATIO * time_weight * self.get_duration()

            # Funkcja kary (?)
            # if self.get_size() > max_flights:
                # f += 5

            # So higher is better
            # self.fitness = 1/f
            
            # LOWER is BETTER
            self.fitness = f

            return self.fitness

    def __repr__(self):
        return 'Tour from {} to {} (fitness: {})\n  airports:  {}\n  flights idx: {}\n  flights full: \n{}\n  Total cost: {}$ duration: {}h\n'.format(
                self.get_src(),
                self.get_dst(),
                self.fitness,
                ' '.join('%2d,' % x for x in self.as_airports()) if self.flights else None,
                ' '.join('%2d,' % x for x in self.as_flights_idx()) if self.flights else None,
                '\n'.join('    ' + str(x) for x in self.as_flights_full()) if self.flights else None,
                self.get_cost(),
                round(self.get_duration(), 2))
