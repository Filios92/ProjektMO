from Tour import *

class Population:
    """
    Manages a population of candidate tours
    """
    def __init__(self, population_size, graph=None, start_idx=0, end_idx=0, do_initialization=False):
        self.population_size = population_size
        self.tours = [Tour(graph, start_idx, end_idx) for x in range(0, population_size)]
        self.tour_idx = 0
        self.start_idx = start_idx
        self.end_idx = end_idx

        if do_initialization: 
            for x in range(0,population_size):
                self.tours[x].find_random_path()

    # Gets the best tour in the population
    def get_fittest(self):
        # fit = 0          # for HIGHER is BETTER
        fit = 1000000000 # for LOWER  is BETTER
        for x in self.tours:
            tmp_fit = x.get_fitness(GA.time_weight, GA.cost_weight, GA.max_flights)
            # if fit < tmp_fit: # for HIGHER is BETTER
            if fit > tmp_fit: # for LOWER  is BETTER
                fit = tmp_fit
                ret = x
        return ret

    def get_tour(self, idx=None):
        if idx is None:
            return self.tours
        else:
            return self.tours[idx]

    def get_population_size(self):
        return len(self.tours)
    
    def save_tour(self, tour, index=None):
        if index is None:
            self.tours[self.tour_idx] = tour
            self.tour_idx += 1
        else:
            self.tours[index] = tour

    def get_start_idx(self):
        return self.start_idx

    def get_end_idx(self):
        return self.end_idx

    def tour_exists(self):
        for x in self.tours:
            if not x.as_flights_idx():
                return False
        return True

    def drop_fitness(self):
        return list(int(x.get_fitness(GA.time_weight, GA.cost_weight, GA.max_flights)) for x in self.tours)

class GA:
    """
    Manages algorithms for evolving population
    """
    mutation_rate   = 0
    tournament_size = 0
    elitism         = True
    cost_weight     = 0
    time_weight     = 0
    max_flights     = 0

    # Evolves a population over one generation
    def evolve_population(population):
        new_pop = Population(population.get_population_size())
        elitism_offset = 0

        # Save the best one?
        if GA.elitism:
            new_pop.save_tour(population.get_fittest())
            elitism_offset = 1

        # Crossover pop
        print('Crossovering number...', end='')
        for x in range(elitism_offset, population.get_population_size()):
            parent1 = GA.tournament_selection(population)
            parent2 = GA.tournament_selection(population)
            print('{:2} '.format(x), end='')
            child = GA.crossover(parent1, parent2)

            new_pop.save_tour(child)
        print('')
        # Mutate
        print('Mutating number...', end='')
        for x in range(elitism_offset, population.get_population_size()):
            if random.random() < GA.mutation_rate:
                print('{:2} '.format(x), end='')
                mutated = GA.mutate(new_pop.get_tour(x))
                new_pop.save_tour(mutated, index=x)
        print('')

        return new_pop

    # Applies crossover to a set of parents and creates offspring
    def crossover(parent1, parent2):
        a1 = parent1.as_airports()
        a2 = parent2.as_airports()
        f1 = parent1.as_flights_idx()
        f2 = parent2.as_flights_idx()

        # Test only
        # a1 = [1, 2, 3, 4, 5, 6, 7]
        # a2 = [1, 8, 5, 9, 4, 10, 7]
        # f1 = ['a', 'b', 'c', 'd', 'e', 'f' ]
        # f2 = ['g', 'h', 'i', 'j', 'k', 'l' ]

        child = []
        child_flights = []

        # Common airports (with the last one)
        common_airports = [ x for x in a1[1:] if x in a2[1:] ]

        # If there are commong airports
        if common_airports[:-1]:
            # Choose starting parent randomly
            if random.random() > 0.5:
                airports = a1
                flights  = f1
            else:
                airports = a2
                flights  = f2

            # First iteration
            c1 = 0  # start index
            c2 = -1 # end   index
            c = random.choice(common_airports[:-1])
            c2 = airports.index(c)

            while not child or child[-1] is not a1[-1]:
                # print('Before {}, c1 {} c2 {} airports {} c {}'.format(child, c1, c2, airports, c))
                child         = child         + airports[c1:c2]
                child_flights = child_flights + flights [c1:c2]
                # print('After {}'.format(child))

                # Check and add last one
                if airports[c2] is a1[-1]:
                    child = child + [airports[c2]]
                    break

                # Another check (not required?)
                if child[-1] is a1[-1]:
                    break

                # Choose from the other one
                if airports is a1: 
                    airports = a2 
                    flights  = f2
                else:
                    airports = a1
                    flights  = f1

                # Next iterations
                c1 = airports.index(c)
                common_airports.remove(c)
                c  = random.choice(common_airports)
                c2 = airports.index(c)
                # print('  Choosing next airport')
                while c2 < c1:
                    c = random.choice(common_airports)
                    c2 = airports.index(c)
        else:
            # TODO: when no common airports
            return parent1 if parent1.get_fitness(GA.time_weight, GA.cost_weight, GA.max_flights) < parent2.get_fitness(GA.time_weight, GA.cost_weight, GA.max_flights) else parent2

        # print('Fliths are {}'.format(child_flights))

        child = parent1.make_basic_copy()
        child.set_flights(child_flights)

        return child

    # Mutate a tour 
    def mutate(tour):
        mutation_tries = 5
        for x in range(mutation_tries):
            org_flights = tour.as_flights_idx()

            # Choose random position to cut from
            pos1 =        math.floor(random.random() * tour.get_size()             )
            pos2 = pos1 + math.floor(random.random() * (tour.get_size() - pos1) - 1) + 1

            start_airport = tour.as_airports()[pos1]
            end_airport   = tour.as_airports()[pos2+1]
            
            # Find random path in the hole
            tmp = Tour(tour.get_graph(), start_airport, end_airport)
            tmp.find_random_path()

            # Put new flights in the hole
            new_flights = org_flights[:pos1] + tmp.as_flights_idx() + org_flights[pos2+1:]

            # Make new Tour and set new flights
            ret = tour.make_basic_copy()
            ret.set_flights(new_flights)

            # print('Mutation complete: \nOrg {} Mutated {}'.format(None, ret))
            # print('Vars were:\n pos1 {}\n pos2 {}\n size: {}\n start_airport {}\n end_airport {}'
            #     .format(pos1, pos2, tour.get_size(), start_airport, end_airport))
            
            if ret.is_valid():
                return ret
            else:
                continue

        print('Couldnt mutate valid... :(')
        return tour


    # Selects candidate tour for crossover
    def tournament_selection(population):
        # Create tournament pop
        tournament = Population(GA.tournament_size)

        # Get random for each place
        for x in range(0, GA.tournament_size):
            random_id = math.floor(random.random() * population.get_population_size())
            tournament.save_tour(population.get_tour(random_id))

        # print('Tournament fitness are {}'.format(tournament.drop_fitness()))
        # Get fittest
        return tournament.get_fittest()

    def run_with_params(params):
        GA.time_weight = params['time_weight']
        GA.cost_weight = params['cost_weight']
        GA.max_flights = params['max_flights']
        GA.mutation_rate = params['mutation_rate']
        GA.tournament_size = params['tournament_size']
        GA.elitism = params['elitism']

        # Make popoulation
        pop = Population(params['pop_size'], params['graph'], params['start_idx'], params['end_idx'], True)

        if not pop.tour_exists():
            print('Tour from {} to {} doesnt exist :('.format(pop.get_start_idx(), pop.get_end_idx()))

        else:
            # Get best one
            fittest = pop.get_fittest()
            print('Initial fittest {}'.format(fittest))
            print('Fitneses: {} '.format(pop.drop_fitness()))

            # Transmutation!
            pop = GA.evolve_population(pop)
            print('Fitneses: {} '.format(pop.drop_fitness()))
            for x in range( params['generations'] ):
                print('Evolution # {}'.format(x))
                pop = GA.evolve_population(pop)
                print('Fitneses: {} '.format(pop.drop_fitness()))

            # Get best best one
            fittest = pop.get_fittest()
            print('Final fittest {}'.format(fittest))
