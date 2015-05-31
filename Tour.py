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
