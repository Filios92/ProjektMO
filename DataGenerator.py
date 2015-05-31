import csv
import random

# CSV Parsing positions
POS_NAME = 4
POS_LATUTUDE = 6
POS_LONGITUDE = 7

# price range per flight
PRICE_MIN = 100
PRICE_MAX = 2000

# destinations count range
DESTINATIONS_MIN = 2
DESTINATIONS_MAX = 4

class DataGenerator:
    test_airports = []
    test_graph = {}

    def __init__(self, limit=10):
        self.read_file(limit)
        self.assign_id()
        pass

    def read_file(self, limit):
        airports = []

        with open('airports.dat', 'r', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')

            # iterate over CSV file
            for row in reader:
                # airport name shall not be empty
                if "" != row[POS_NAME]:
                    # [0] position for further id
                    airports.append([None, float(row[POS_LATUTUDE]), float(row[POS_LONGITUDE]), row[POS_NAME]])

            self.test_airports = random.sample(airports, limit)

    def assign_id(self):
        id = 0

        for current_airport in self.test_airports:
            current_airport[0] = id
            id += 1
        pass

    def create_graph(self):
        for current_airport in self.test_airports:
            #    count of destinations in current airport
            current_dest_count = random.randint(DESTINATIONS_MIN, DESTINATIONS_MAX)

            # selected target airports for current airport
            current_dest_airports = random.sample(self.test_airports, current_dest_count)

            # create graph edges
            current_nodes = []
            for current_dest_airport in current_dest_airports:

                # prevent selection destination airport same as start airport
                if current_airport[0] != current_dest_airport[0]:

                    # rand price
                    current_price = random.randint(PRICE_MIN, PRICE_MAX)
                    current_departure_time = round(random.uniform(0, 24), 2)
                    current_nodes.append([current_dest_airport[0], current_departure_time, current_price])

            # assign edges to current node
            self.test_graph[current_airport[0]] = current_nodes
            # print(str(current_airport[0]) + ":" + str(self.test_graph[current_airport[0]]) + '\n')

        # print(self.test_graph)

    def get_airports(self):
        return self.test_airports

    def get_graph(self):
        return self.test_graph
