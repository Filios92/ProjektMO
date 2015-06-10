import subprocess, time

nbr_of_iterations = 10
algo_start_time = time.clock()

# TEST parametru ROZMIAR POLPULACJI
for pop_size in range(5,125,20):
    failure_counter = 0
    start_time = time.clock()
    for index in range(0,nbr_of_iterations):
        failure_counter += subprocess.call("python Main.py -i graph.txt -v 1 --pop_size " + str(pop_size), shell=True)

    with open('performance.txt', 'a') as file:
        file.write("Pop size: {}, the rest of params: DEFAULT \n".format(pop_size))
        file.write("Failure ratio: " + str(failure_counter/nbr_of_iterations) + "\n")
        file.write("Elapsed time: " + str(time.clock() - start_time) + " seconds\n\n")

# print("Failure ratio: " + str(failure_counter/nbr_of_iterations))
# print("Elapsed time: " + str(time.clock() - start_time) + " seconds")


# TEST parametru ILOSC GENERACJI
for generations in range(10,40,10):
    failure_counter = 0
    start_time = time.clock()
    for index in range(0,nbr_of_iterations):
        failure_counter += subprocess.call("python Main.py -i graph.txt -v 1 --generations " + str(generations), shell=True)

    with open('performance.txt', 'a') as file:
        file.write("Generations: {}, the rest of params: DEFAULT \n".format(generations))
        file.write("Failure ratio: " + str(failure_counter/nbr_of_iterations) + "\n")
        file.write("Elapsed time: " + str(time.clock() - start_time) + " seconds\n\n")

print("Finished")
print("Elapsed time: " + str(time.clock() - algo_start_time) + " seconds")


# TEST parametru WSKAZNIK MUTACJI
for mutation_rate in range(1,101,10):
    mutation_rate = mutation_rate * 0.01
    failure_counter = 0
    start_time = time.clock()
    for index in range(0,nbr_of_iterations):
        failure_counter += subprocess.call("python Main.py -i graph.txt -v 1 --mutation_rate " + str(mutation_rate), shell=True)

    with open('performance.txt', 'a') as file:
        file.write("Mutation rate: {}, the rest of params: DEFAULT \n".format(mutation_rate))
        file.write("Failure ratio: " + str(failure_counter/nbr_of_iterations) + "\n")
        file.write("Elapsed time: " + str(time.clock() - start_time) + " seconds\n\n")
        

# TEST parametru ROZMIAR TURNIEJU
for tournament_size in range(2,12,2):
    failure_counter = 0
    start_time = time.clock()
    for index in range(0,nbr_of_iterations):
        failure_counter += subprocess.call("python Main.py -i graph.txt -v 1 --tournament_size " + str(tournament_size), shell=True)

    with open('performance.txt', 'a') as file:
        file.write("Tournament size: {}, the rest of params: DEFAULT \n".format(tournament_size))
        file.write("Failure ratio: " + str(failure_counter/nbr_of_iterations) + "\n")
        file.write("Elapsed time: " + str(time.clock() - start_time) + " seconds\n\n")
        
        
 # TEST parametru ELITARNOSC
for elitism in (True, False):
    failure_counter = 0
    start_time = time.clock()
    for index in range(0,nbr_of_iterations):
        failure_counter += subprocess.call("python Main.py -i graph.txt -v 1 --elitism " + str(elitism), shell=True)

    with open('performance.txt', 'a') as file:
        file.write("Elitism: {}, the rest of params: DEFAULT \n".format(elitism))
        file.write("Failure ratio: " + str(failure_counter/nbr_of_iterations) + "\n")
        file.write("Elapsed time: " + str(time.clock() - start_time) + " seconds\n\n")       
        
print("Finished")
print("Elapsed time: " + str(time.clock() - algo_start_time) + " seconds")