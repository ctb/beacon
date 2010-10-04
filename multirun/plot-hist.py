import sys

# use plotting code
import matplotlib
matplotlib.use('GtkCairo')
from pylab import *

# record the data in a list
data = []

# open the data file(s) and load in all the intervals
for filename in sys.argv[1:]:
    print 'opening', filename
    fp = open(filename)

    for line in fp:
        n = float(line)
        data.append(n)

# now, plot a histogram for all the data
hist(data, bins=100, log=True)

# print default axes...
print axis()

# ...and fix if necessary
#axis([-100000.0, 100000.0, 0.0, 4000.0])

#yscale('log')

show()

print 'Saving figure dist.pdf'
savefig('dist.pdf')
