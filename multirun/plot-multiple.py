import matplotlib
matplotlib.use('Cairo')

from pylab import *

## define a function to load in a 'multiple-averages.txt' file
def load_averages(filename):
    updates = []
    averages = []

    print 'loading'
    for line in open('multiple-averages.txt'):
        update, avg = line.split()
        update = int(update)
        avg = float(avg)

        updates.append(update)
        averages.append(avg)

    return updates, averages
    
updates_1, averages_1 = load_averages('multiple-averages.txt')

print 'plotting'
plot(updates_1, averages_1, 'r-')

print 'saving'
savefig('avg.pdf')
