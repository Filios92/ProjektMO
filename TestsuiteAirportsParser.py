__author__ = 'Pawel'
class Testsuite_airports_parser(object):

        def __init__(self, testsuite_airports):
            self._x_coordinates = []
            self._y_coordinates = []
            self._names_of_airports = []
            for airport in testsuite_airports:
                self._x_coordinates.append(airport[1])
                self._y_coordinates.append(airport[2])
                self._names_of_airports.append("{index} {name}".format(index=airport[0], name=airport[3]))

        def get_x_coordinates(self):
            return self._x_coordinates

        def get_y_coordinates(self):
            return self._y_coordinates

        def get_names_of_airports(self):
            return self._names_of_airports