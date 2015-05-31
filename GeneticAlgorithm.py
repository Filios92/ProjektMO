from Tour import *

class Population:
    """
    Manages a population of candidate tours
    """
    def __init__(self, population_size, graph, start_idx, end_idx, do_initialization=True):
        self.population_size = population_size
        self.tours = []
        if do_initialization: 
            for x in range(1,population_size):
                # t = Tour(graph, start_idx, end_idx)
                # t.find_random_path()
                # t = graph.find_random_path()
                # self.tours.append(t)
                pass

    # Gets the best tour in the population
    def get_fittest(self):
        return Tour(None, 1, 2)

class GA:
    """
    Manages algorithms for evolving population
    """
    mutation_rate = 0.015
    tournament_size = 5
    elitism = True

    # Evolves a population over one generation
    def evolve_population(population):
        return population

    # Applies crossover to a set of parents and creates offspring
    def crossover(parent1, parent2):
        pass

    # Mutate a tour using swap mutation
    def mutate(tour):
        pass

    # Selects candidate tour for crossover
    def tournament_selection(population):
        pass