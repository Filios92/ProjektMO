__author__ = 'Pawel'

import matplotlib.pyplot as plt

class AirportPlotCreator(object):
    def __init__(self):
        self.labels = []

    def create_graph(self, x_values, y_values, labels):
        if len(labels) == len(x_values) == len(y_values):
            plt.scatter(
                x_values, y_values, marker='o', cmap= plt.get_cmap('Spectral')
            )
            for label, x, y in zip(labels, x_values, y_values):
                plt.annotate(label, xy = (x,y), xytest = (-20, 20),
                             textcoords = 'offset points', ha = 'right', va = 'bottom',
                             bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                             arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
            plt.show()
