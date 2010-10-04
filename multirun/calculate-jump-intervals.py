#! /usr/bin/env python
import sys

THRESHOLD=100                   # threshold for a "real" fitness jump

run_dir = sys.argv[1]           # the run directory is the first argument
outfile = sys.argv[2]           # the output file is the second argument

# (the below is copied from parse-multiple.py)

# first, load in all the data from the given directory
print 'Opening directory', run_dir
data_dir = run_dir + '/data'
filename = data_dir + '/average.dat'

print 'Opening file', filename
fp = open(filename)

# Load in updates and average fitness and save them in info dictionary
info = {}
updates = []
for line in fp:
    line = line.strip()         # remove whitespace
    if not line:                # ignore empty lines
        continue

    if line.startswith('#'):    # ignore comments
        continue

    line = line.split()         # "split" the line into fields on spaces

    update = line[0]            # pick out the update & fitness columns
    fitness = line[3]

    update = int(update)    # convert to numbers (integer and floating)
    fitness = float(fitness)

    info[update] = fitness  # store fitness associated with this update
    updates.append(update)  # keep track of updates, too

# open the output file
print 'opening output file', outfile
outfp = open(outfile, 'w')

# now, iterate over updates, and record distance *between* fitness jumps

i = 0
last_update = updates[i]

while i < len(updates):
    last_fitness = info[last_update]

    this_update = updates[i]
    this_fitness = info[this_update]

    if this_fitness - last_fitness > THRESHOLD:
        print >>outfp, this_update - last_update
        last_update = this_update

    i = i + 1
