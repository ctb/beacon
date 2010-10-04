import sys

# use plotting code
import matplotlib
matplotlib.use('Cairo')
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

print 'Saving figure dist.pdf'
savefig('dist.pdf')
