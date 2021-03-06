import matplotlib
matplotlib.use('Cairo')
from pylab import *

## define a function to load in a 'multiple-averages.txt' file
def load_averages(filename):
    updates = []
    averages = []
    stderr = []

    print 'loading'
    for line in open(filename):
        update, avg, err = line.split()
        update = int(update)
        avg = float(avg)
        err = float(err)

        updates.append(update)
        averages.append(avg)
        stderr.append(err)

    return updates, averages, stderr

## code to actually run
    
updates_1, averages_1, stderr_1 = load_averages(sys.argv[1])
updates_2, averages_2, stderr_2 = load_averages(sys.argv[2])

print 'plotting'
errorbar(updates_1, averages_1, stderr_1, fmt='r-')
errorbar(updates_2, averages_2, stderr_2, fmt='b.')

print 'saving to avg.pdf'
savefig('avg.pdf')
