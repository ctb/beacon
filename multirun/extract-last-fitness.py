#! /usr/bin/env python
# for weigelem?
import sys
import math

store_fp = open(sys.argv[-1], 'w')

# Assume everything passed in via the command line is a run directory
for run_dir in sys.argv[1:-1]:
    print 'Opening directory', run_dir
    data_dir = run_dir + '/data'
    filename = data_dir + '/average.dat'

    print 'Opening file', filename
    fp = open(filename)
    
    # Load in updates and average fitness and save them in info dictionary
    info = {}
    for line in fp:
        line = line.strip()         # remove whitespace
        if not line:                # ignore empty lines
            continue

        if line.startswith('#'):    # ignore comments
            continue

        line = line.split()         # "split" the line into fields on spaces
        last_line = line

    update = last_line[0]            # pick out the update & fitness columns
    fitness = last_line[3]

    update = int(update)    # convert to numbers (integer and floating)
    fitness = float(fitness)

    print >>store_fp, update, fitness, run_dir
