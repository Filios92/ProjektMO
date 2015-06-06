import random
import math

from ManagerBase import *

# Flight part
class Flight:
    """
    Class representing a flight.
    """
    SPEED = 900000 # Boeing 747, m/h

    def __init__(self, src, dst, departure_time, cost, index=None):
        self._src = src
        self._dst = dst
        self._departure_time = departure_time
        self._cost = cost
        self._duration = 0
        self._speed = Flight.SPEED
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
        return 'Flight {:>3} from {:2} to {:2} @{:5}h for {:7.2f}$ and {:4.2f}h'.format(
                        '#{}'.format(self._index),
                        self._src.index,
                        self._dst.index,
                        self._departure_time,
                        self._cost,
                        self._duration)

class FlightManager(ManagerBase):
    """
    Class representing an airport manager.
    """
    def __init__(self):
        super(FlightManager, self).__init__()
