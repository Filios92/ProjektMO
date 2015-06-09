from GraphManager import GraphManager
from TestsuiteAirportsParser import Testsuite_airports_parser

__author__ = 'Pawel'

from PySide.QtGui import QLabel, QLineEdit, QPushButton, QComboBox, QWidget, QApplication, QIcon, QTextEdit
import sys
from GeneticAlgorithm import GA
from DataGenerator import DataGenerator

import matplotlib.pyplot as plt

###  Starting QT_app, when import module
#qt_app = QApplication(sys.argv)
###

class Airport_project_UI(QWidget):

    airports = [
        'KRK',
        'LA',
        'LIS'
    ]

    elitism_possibly_values = ['true', 'false']

    max_flights_list = ['1', '2', '3', '4', '5']

    def __init__(self):
        QWidget.__init__(self)
        self.params = {}

       # self.setMinimumSize(600, 250)
        #self.setWindowTitle("Medody Optymalizacji - Projekt")
       # self.setIcon()

        self.start_airport_label = QLabel("Start airport:", self)
        self.start_airport_label.move(5, 10)
        self.start_airport = QLineEdit(self)
        self.start_airport.setText('1')
        #self.start_airport.addItems(self.airports)
        self.start_airport.setMinimumHeight(20)
        self.start_airport.setMaximumHeight(20)
        self.start_airport.setMinimumWidth(60)
        self.start_airport.setMaximumWidth(60)
        self.start_airport.move(150, 5)

#TODO function to convert names of airport to indexes

        self.destination_airport_label = QLabel("Destination airport:", self)
        self.destination_airport_label.move(5, 40)
        self.destination_airport = QLineEdit(self)
        self.destination_airport.setText('2')
       # self.destination_airport.addItems(self.airports)
        self.destination_airport.setMinimumHeight(20)
        self.destination_airport.setMaximumHeight(20)
        self.destination_airport.setMaximumWidth(60)
        self.destination_airport.setMinimumWidth(60)
        self.destination_airport.move(150, 35)

        self.max_flights_label = QLabel("max number of flights:", self)
        self.max_flights_label.move(5, 70)
        self.max_flights = QLineEdit(self)
        self.max_flights.setText("3")
        #self.max_flights.addItems(self.max_flights_list)
        self.max_flights.setMaximumHeight(20)
        self.max_flights.setMinimumHeight(20)
        self.max_flights.setMaximumWidth(60)
        self.max_flights.setMinimumWidth(60)
        #self.max_flights.setMinimumWidth(60)
        self.max_flights.move(150, 65)

        self.cost_weight_label = QLabel("max cost weights:", self)
        self.cost_weight_label.move(5, 100)
        self.cost_weight = QLineEdit(self)
        self.cost_weight.setText("4")
        self.cost_weight.setMinimumWidth(60)
        self.cost_weight.setMaximumWidth(60)
        self.cost_weight.setMinimumHeight(20)
        self.cost_weight.setMaximumHeight(20)
        self.cost_weight.move(150, 95)


        self.time_weight_label = QLabel("time weight:", self)
        self.time_weight_label.move(5, 130)
        self.time_weight = QLineEdit(self)
        self.time_weight.setText("5")
        self.time_weight.setMinimumWidth(60)
        self.time_weight.setMaximumWidth(60)
        self.time_weight.setMinimumHeight(20)
        self.time_weight.setMaximumHeight(20)
        self.time_weight.move(150, 125)

        self.pop_size_label = QLabel("pop size:", self)
        self.pop_size_label.move(5, 160)  # +30

        self.pop_size = QLineEdit(self)
        self.pop_size.setText("6")
        self.pop_size.setMinimumWidth(60)
        self.pop_size.setMaximumWidth(60)
        self.pop_size.setMinimumHeight(20)
        self.pop_size.setMaximumHeight(20)
        self.pop_size.move(150, 155) # +30

        self.generation_label = QLabel("generations:", self)
        self.generation_label.move(5, 190)  # +30

        self.generation = QLineEdit(self)
        self.generation.setText("7")
        self.generation.setMinimumWidth(60)
        self.generation.setMaximumWidth(60)
        self.generation.setMinimumHeight(20)
        self.generation.setMaximumHeight(20)
        self.generation.move(150, 185) # +30

        self.mutation_rate_label = QLabel("mutation rate:", self)
        self.mutation_rate_label.move(5, 210)  # +30

        self.mutation_rate = QLineEdit(self)
        self.mutation_rate.setText("8")
        self.mutation_rate.setMinimumWidth(60)
        self.mutation_rate.setMaximumWidth(60)
        self.mutation_rate.setMinimumHeight(20)
        self.mutation_rate.setMaximumHeight(20)
        self.mutation_rate.move(150, 215) # +30


        self.tournament_size_label = QLabel("tournament size:", self)
        self.tournament_size_label.move(5, 240)  # +30

        self.tournament_size = QLineEdit(self)
        self.tournament_size.setText("9")
        self.tournament_size.setMinimumWidth(60)
        self.tournament_size.setMaximumWidth(60)
        self.tournament_size.setMinimumHeight(20)
        self.tournament_size.setMaximumHeight(20)
        self.tournament_size.move(150, 245) # +30

        self.elitism_label = QLabel("elitism:", self)
        self.elitism_label.move(5, 270)  # +30

        self.elitism = QComboBox(self)
        self.elitism.addItems(self.elitism_possibly_values)
        self.elitism.setMinimumWidth(60)
        self.elitism.setMaximumWidth(60)
        self.elitism.setMinimumHeight(20)
        self.elitism.setMaximumHeight(20)
        self.elitism.move(150, 275) # +30

        self.destination_min_label = QLabel("dest min:", self)
        self.destination_min_label.move(5, 300)  # +30

        self.dest_min = QLineEdit(self)
        self.dest_min.setText("4")
        self.dest_min.setMinimumWidth(60)
        self.dest_min.setMaximumWidth(60)
        self.dest_min.setMinimumHeight(20)
        self.dest_min.setMaximumHeight(20)
        self.dest_min.move(150, 305) # +30

        self.destination_max_label = QLabel("dest max:", self)
        self.destination_max_label.move(5, 330)  # +30

        self.dest_max = QLineEdit(self)
        self.dest_max.setText("10")
        self.dest_max.setMinimumWidth(60)
        self.dest_max.setMaximumWidth(60)
        self.dest_max.setMinimumHeight(20)
        self.dest_max.setMaximumHeight(20)
        self.dest_max.move(150, 335) # +30

        self.generate_graph_button = QPushButton("Generate graph!", self)
        self.generate_graph_button.setMinimumWidth(170)
        self.generate_graph_button.move(25, 365)

        self.start_evolution_button = QPushButton("Start evolution!", self)
        self.start_evolution_button.setMinimumWidth(170)
        self.start_evolution_button.move(25, 395)

        self.start_evolution_button.clicked.connect(self.start_evolution)
        self.generate_graph_button.clicked.connect(self.generate_graph)
        #self.get_list_of_possibly_airports() #TODO to have full list of airports in QComboBox

    def generate_graph(self):
        self.params = {
            'graph'           : None,
            'start_idx'       : int(self.start_airport.text()),
            'end_idx'         : int(self.destination_airport.text()),
            'max_flights'     : int(self.max_flights.text()),
            'cost_weight'     : int(self.cost_weight.text()),
            'time_weight'     : int(self.time_weight.text()),
            'pop_size'        : int(self.pop_size.text()),
            'generations'     : int(self.generation.text()),
            'mutation_rate'   : float(self.mutation_rate.text()),
            'tournament_size' : int(self.tournament_size.text()),
            'elitism'         : bool(self.elitism.currentText()),
            'dest_min'        : int(self.dest_min.text()),
            'dest_max'        : int(self.dest_max.text()),
            'max_flights'     : 4,
        }
        data = DataGenerator()
        DataGenerator.DESTINATIONS_MIN = self.params['dest_min']
        DataGenerator.DESTINATIONS_MAX = self.params['dest_max']

        # if input_graph_file is not None:
        #     data.load_saved_graph(input_graph_file)
        #
        # else:
        #TODO ilosc lotnisk
        data.load_new_data(10)
        data.create_graph()

        # if graph_save_file is not None:
        #     data.save_graph(graph_save_file)

        testsuite_airports = data.get_airports()
        testsuite_graph = data.get_graph()

        self.graph = GraphManager(self.params['max_flights'])
        self.graph.set_graph(testsuite_graph, testsuite_airports)

        airports_parser = Testsuite_airports_parser(testsuite_airports)


    def start_evolution(self):
        import pprint
        self.params = {
        'graph'           : self.graph,
        'start_idx'       : int(self.start_airport.text()),
        'end_idx'         : int(self.destination_airport.text()),
        'max_flights'     : int(self.max_flights.text()),
        'cost_weight'     : int(self.cost_weight.text()),
        'time_weight'     : int(self.time_weight.text()),
        'pop_size'        : int(self.pop_size.text()),
        'generations'     : int(self.generation.text()),
        'mutation_rate'   : float(self.mutation_rate.text()),
        'tournament_size' : int(self.tournament_size.text()),
        'elitism'         : bool(self.elitism.currentText()),
        'dest_min'        : int(self.dest_min.text()),
        'dest_max'        : int(self.dest_max.text()),
        }
        # pprint.pprint(params)
        self.output_of_algorithm = sys.__stdout__
        GA.run_with_params(self.params)
        self.newwindow()

    def newwindow(self):
        import pprint
        print("##############")
        pprint.pprint(self.output_of_algorithm)
        print("##############")
        self.wid = QWidget()
        self.wid.resize(250, 150)
        self.wid.setWindowTitle('NewWindow')
        self.result = QTextEdit(self.wid)
        self.result.setText(str(self.output_of_algorithm))
        #self.start_airport.addItems(self.airports)
        self.result.setMinimumHeight(200)
        self.result.setMaximumHeight(200)
        self.result.setMinimumWidth(600)
        self.start_airport.setMaximumWidth(600)
        # self.start_airport.move(150, 5)
        self.output_of_algorithm = None
        self.wid.show()



if __name__ == "__main__":
    try:
        myApp = QApplication(sys.argv)
        mainWindow = Airport_project_UI()
        #mainWindow.createStatusBar()
        #mainWindow.SetupComponents()
        mainWindow.show()
        #mainWindow.showProgress()
        myApp.exec_()
        sys.exit(0)
    except Exception:
        print(sys.exc_info()[1])
