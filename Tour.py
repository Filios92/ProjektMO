from Airport import *
from Flight import *

# Tour, specific solution, list of flight indeces / flights / airports
class Tour:
    """
    Class representing a tour.
    """
    def __init__(self, graph, start_idx, end_idx):
        self.graph   = graph
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
        for flight in self.as_flights_full():
            cost += flight.cost
        return cost

    def get_duration(self):
        _flights = iter(self.as_flights_full())
        current_flight = next(_flights)

        duration = 0;
        current_time = current_flight.departure_time
        current_time %= 24

        try:
            while True:

                # Flight
                print("Departure: " + str(current_time%24))
                duration += current_flight.duration
                current_time += current_flight.duration
                print("Arrival: " + str(current_time%24))
                next_flight = next(_flights)

                current_time %= 24

                # Waiting for next flight
                if current_time > next_flight.departure_time:
                    time_to_add = 24 - current_time
                    duration += time_to_add
                    current_time += time_to_add
                    duration += next_flight.departure_time
                else:
                    time_to_add = next_flight.departure_time - current_time
                    duration += time_to_add
                    current_time += time_to_add

                current_time %= 24

                current_flight = next_flight
        except StopIteration:
            print("\n")
            return duration

        # TODO: do dokonczenia!!! nie dziala dobrze we wszystkich przypadkach

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

    def __repr__(self):
        return 'Tour from {} to {} \n  airports: {}\n  flights idx: {}\n  flights full: \n{}\n  Total cost: {}$ duration: {}h\n'.format(
                self.get_src(),
                self.get_dst(),
                self.as_airports(), 
                self.as_flights_idx(), 
                '\n'.join('    ' + str(x) for x in self.as_flights_full()),
                self.get_cost(),
                round(self.get_duration(), 2))
