#! /usr/bin/env python
import sys
import math
import os.path

def get_fitness(fp):
    for line in fp:
        line = line.strip()         # remove whitespace
        if not line:                # ignore empty lines
            continue

        if line.startswith('#'):    # ignore comments
            continue

        line = line.split()         # "split" the line into fields on spaces

        fitness = line[3]       # pick out the fitness & convert to number
        fitness = float(fitness)

    return fitness

### actual script

# Create a dictionary to store fitness information per-run
run_fitness = {}

# Assume everything passed in via the command line is a run directory
for run_dir in sys.argv[1:-1]:
    pos = run_dir.rsplit('.')[-1]
    try:
        pos = int(pos)
    except ValueError:
        continue

    print 'Opening directory', run_dir, pos
    data_dir = run_dir + '/data'
    filename = data_dir + '/average.dat'

    print 'Opening file', filename
    fp = open(filename)
    
    # Load in updates and average fitness and save them in info dictionary
    run_fitness[pos] = get_fitness(fp)

# get the unmutated fitness, too, from 'run.orig'
unmut_run = os.path.dirname(run_dir)
fp = open(unmut_run + 'run.orig/data/average.dat')
unmut_fitness = get_fitness(fp)

## sort and output

items = run_fitness.items()
items.sort()

outfp = open(sys.argv[-1], 'w')
for k, v in items:
    print >>outfp, k, v

print >>outfp, -1, unmut_fitness
