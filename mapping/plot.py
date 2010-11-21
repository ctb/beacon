import sys, csv
import matplotlib
matplotlib.use('Cairo')

from pylab import *

positions = []
counts = []
percents = []
for pos, count, percent in csv.reader(open(sys.argv[1])):
    positions.append(pos)
    counts.append(count)
    percents.append(percent)

print 'plotting'
plot(positions, percents, 'r-')

xlabel('position in read')
ylabel('fraction of reads that differ at position')

print 'saving to posvar.pdf'
savefig('posvar.pdf')
