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
updates_1, averages_1, stderr_1 = load_averages('multiple-a.txt')
updates_2, averages_2, stderr_2 = load_averages('multiple-b.txt')

# normalize averages_2 to the maximum value in averages_1
scale_factor = max(averages_1) / max(averages_2)
averages_2 = [ x * scale_factor for x in averages_2 ]
stderr_2 = [ x * scale_factor for x in stderr_2 ]

print 'plotting'
errorbar(updates_1, averages_1, stderr_1, fmt='r-')
errorbar(updates_2, averages_2, stderr_2, fmt='b.')

yscale('log')
#print axis()
axis([0, 20000, .1, 10000000.0])

print 'saving to log-scaled-avg.pdf'
savefig('log-scaled-avg.pdf')
