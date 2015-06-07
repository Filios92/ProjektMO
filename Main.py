import sys, getopt

from GraphManager import *
from GeneticAlgorithm import *
from DataGenerator import *

def print_help():
    print('Usage: {} [-i <input_file>] [-s <output_file>] [-p <input_params_file>] \n'.format('Main.py'))
    print('  -i, --ifile <input_file>         - reads graph from file')
    print('  -s, --save <output_file>         - saves generated graph to file')
    print('  -p, --params <input_params_file> - reads params from file')
    print('  -a, --airports <number>          - number of airports')
    print('  -g, --generate                   - dont run GA, just generate data')
    print('  -v, --verbose                    - verbosity level')
    print('  --start_idx <int>                - param options')
    print('  --end_idx <int>                  - param options')
    print('  --max_flights <int>              - param options')
    print('  --cost_weight <int>              - param options')
    print('  --time_weight <int>              - param options')
    print('  --pop_size <int>                 - param options')
    print('  --generations <int>              - param options')
    print('  --mutation_rate <float>          - param options')
    print('  --tournament_size <int>          - param options')
    print('  --elitism <boolean>              - param options')
    print('No options - generates graph and runs GeneticAlgorithm')

def save_graph_file(graph_save_file):
    pass

def load_graph_from_file(input_graph_file):
    pass

def get_verbosity_info(verbosity):
    if verbosity > 1:
        return 'everything'
    elif verbosity == 1:
        return 'no graph info'
    elif verbosity == 0:
        return 'nothing'

def main(argv):

    input_graph_file = None
    graph_save_file = None
    input_params_file = None
    airport_q = 10
    only_generate = False
    verbosity = 5

    data = None
    graph = None

    # Parameters
    params = {
        'graph'           : graph,
        'start_idx'       : 1,
        'end_idx'         : 4,
        'max_flights'     : 5,
        'cost_weight'     : 2,
        'time_weight'     : 1,
        'pop_size'        : 10,
        'generations'     : 10,
        'mutation_rate'   : 0.015,
        'tournament_size' : 5,
        'elitism'         : True
    }

    # Parse command line options
    try:
        opts, args = getopt.getopt(argv, "hi:s:p:a:gv:", 
            ["ifile=", "save=", "params=", "airports=", "verbose=", 
            "start_idx="  ,
            "end_idx="    ,
            "max_flights=",
            "cost_weight=",
            "time_weight=",
            "pop_size="   ,
            "generations=",
            "mutation_rate=",
            "tournament_size=",
            "elitism="
            ])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()

        elif opt in ("-i", "--ifile"):
            input_graph_file = arg
            print('Will read data from: {}'.format(input_graph_file))

        elif opt in ("-s", "--save"):
            graph_save_file = arg
            print('Will save graph to: {}'.format(graph_save_file))

        elif opt in ("-p", "--params"):
            input_params_file = arg
            print('Will read params from: {}'.format(input_params_file))

        elif opt in ("-a", "--airports"):
            airport_q = int(arg)
            print('Number of airports = {}'.format(airport_q))

        elif opt in ("-g", "--generate"):
            only_generate = True
            print('Will just generate data')

        elif opt in ("-v", "--verbose"):
            verbosity = int(arg)
            print('Verbosity level = {} ({})'.format(verbosity, get_verbosity_info(verbosity)))

        elif opt in list("--" + x for x in params.keys()):
            if opt[2:] == 'mutation_rate':
                params[opt[2:]] = float(arg)
            elif opt[2:] == 'elitism':
                params[opt[2:]] = arg.lower() in ['true', 't', 'tak', 'yes', 'y', '1']
            else:
                params[opt[2:]] = int(arg)

    print('Params are: \n{} \n'.format('\n'.join('  {:{}}: {}'.format(k, len(max(params.keys()))+1, v) for k,v in sorted(params.items()))))

    # DataGenerator
    data = DataGenerator()
    
    if input_graph_file is not None:
        data.load_saved_graph(input_graph_file)

    else:
        data.load_new_data(airport_q)
        data.create_graph()

        if graph_save_file is not None:
            data.save_graph(graph_save_file)

    testsuite_airports = data.get_airports()
    testsuite_graph = data.get_graph()

    graph = GraphManager(params['max_flights'])
    graph.set_graph(testsuite_graph, testsuite_airports)

    if verbosity > 1:
        graph.print_airports()
        graph.print_flights()
        graph.print_graph()

    if not only_generate:
        print(' === GeneticAlgorithm tests ===')
        params['graph'] = graph
        GA.run_with_params(params)

if __name__ == '__main__':
    main(sys.argv[1:])

