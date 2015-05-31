from Airport import *
from Flight import *

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
				if newpath: return newpath
				else: flights.pop()
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
