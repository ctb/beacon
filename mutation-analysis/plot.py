import matplotlib
matplotlib.use('Cairo')

from pylab import *

## define a function to load in a 'multiple-averages.txt' file
def load_fitness(filename):
    positions = []
    fitnesses = []

    print 'loading'
    for line in open(filename):
        position, fitness = line.split()
        position = int(position)
        fitness = float(fitness)

        positions.append(position)
        fitnesses.append(fitness)

    return positions, fitnesses

## code to actually run
positions, fitnesses = load_fitness(sys.argv[1])

# make sure that the last 'fitness' loaded is for position '-1',
# aka the fitness of the original (unmutated) guy
assert positions[-1] == -1
unmut_fitness = fitnesses[-1]

# trim this last bit of info off the lists
positions = positions[:-1]
fitnesses = fitnesses[:-1]

# construct a new line for the original (unmut) fitness
unmut_fitline = []
for pos in positions:
    unmut_fitline.append(unmut_fitness)

print 'plotting'
plot(positions, fitnesses, 'r.')
plot(positions, unmut_fitline, 'g-')

xlabel('position in genome')
ylabel('measured fitness of nop mutant')
yscale('log')

print 'saving to mutations.pdf'
savefig('mutations.pdf')
