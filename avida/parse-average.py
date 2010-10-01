import sys, os

# retrieve the 'data' directory name from the command line
dirname = sys.argv[1]
print 'FOO'
print dirname

# construct the filename of the 'average.dat' file
filename = os.path.join(dirname, 'average.dat')
print 'BAR'
print filename

# open said file for reading
fp = open(filename)

# for every line,
for line in fp:
    print 'BIF'
    line = line.strip()         # remove whitespace
    if not line:                # ignore empty lines
        continue

    if line.startswith('#'):    # ignore comments
        continue

    line = line.split()         # "split" the line into fields on spaces

    update = line[0]            # pick out the update & fitness columns
    fitness = line[3]

    print update, fitness       # print 'em
