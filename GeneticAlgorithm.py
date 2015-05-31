from Tour import *

class Population:
    """
    Manages a population of candidate tours
    """
    def __init__(self, population_size, graph=None, start_idx=0, end_idx=0, do_initialization=False):
        self.population_size = population_size
        self.tours = [Tour(graph, start_idx, end_idx) for x in range(0, population_size)]
        self.tour_idx = 0
        
        if do_initialization: 
            for x in range(0,population_size):
                self.tours[x].find_random_path()

    # Gets the best tour in the population
    # TODO: implement, funkcja celu :D
    def get_fittest(self):
        return self.tours[0]

    def get_tour(self, idx=None):
        if idx is None:
            return self.tours
        else:
            return self.tours[idx]

    def get_population_size(self):
        return len(self.tours)
    
    def save_tour(self, tour):
        self.tours[self.tour_idx] = tour
        self.tour_idx += 1

class GA:
    """
    Manages algorithms for evolving population
    """
    mutation_rate = 0.015
    tournament_size = 5
    elitism = True

    # Evolves a population over one generation
    def evolve_population(population):
        new_pop = Population(population.get_population_size())
        elitism_offset = 0

        # Save the best one?
        if GA.elitism:
            new_pop.save_tour(population.get_fittest())
            elitism_offset = 1

        # Crossover pop
        for x in range(elitism_offset, population.get_population_size()):
            parent1 = GA.tournament_selection(population)
            parent2 = GA.tournament_selection(population)

            child = GA.crossover(parent1, parent2)

            new_pop.save_tour(child)

        # Mutate
        for x in range(elitism_offset-1, population.get_population_size()):
            GA.mutate(new_pop.get_tour(x))

        return new_pop

    # Applies crossover to a set of parents and creates offspring
    # TODO: implement
    def crossover(parent1, parent2):
        return parent1

    # Mutate a tour using swap mutation
    # TODO: implement
    def mutate(tour):
        pass

    # Selects candidate tour for crossover
    def tournament_selection(population):
        # Create tournament pop
        tournament = Population(GA.tournament_size)

        # Get random for each place
        for x in range(0, GA.tournament_size):
            random_id = math.floor(random.random() * population.get_population_size())
            tournament.save_tour(population.get_tour(random_id))

        # Get fittest
        return tournament.get_fittest()
