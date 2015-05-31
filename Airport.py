import random
import math

from ManagerBase import *

MAX_X = 90
MAX_Y = 180

# Airport part
class Airport:
    """
    Class representing an airport.
    """
    def __init__(self, x=None, y=None):
        if x is None:
            self._x = random.uniform(-1, 1) * MAX_X
        else:
            self._x = x

        if y is None:
            self._y = random.uniform(-1, 1) * MAX_Y
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
        return 'Airport #{} x: {:6.2f} y: {:6.2f}'.format(self._index, self._x, self._y)

class AirportManager(ManagerBase):
    """
    Class representing an airport manager.
    """
    def __init__(self):
        super(AirportManager, self).__init__()
