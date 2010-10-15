#! /usr/bin/env python
import sys
import math

# Create a dictionary to store fitness information per-run
run_fitness = {}

# Assume everything passed in via the command line is a run directory
for run_dir in sys.argv[1:]:
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

        update = line[0]            # pick out the update & fitness columns
        fitness = line[3]

        update = int(update)    # convert to numbers (integer and floating)
        fitness = float(fitness)

        info[update] = fitness  # store fitness associated with this update

    print 'loaded', len(info), 'for', run_dir

    # store this information for each run
    run_fitness[run_dir] = info

# Next, for each update, for each run, average information across runs.
fitness_by_update = {}
stderr_by_update = {}

# use the last 'info' as a source of information about updates:
for update in info:
    n = 0
    total = 0.0
    
    # go across all runs
    for run_dir in run_fitness:
        update_info = run_fitness[run_dir]
        update_fitness = update_info[update]

        n = n + 1
        total = total + update_fitness
    
    # compute average
    average = total / float(n)
    
    # store average
    fitness_by_update[update] = average

    dev = 0.0
    for run_dir in run_fitness:
        update_info = run_fitness[run_dir]
        update_fitness = update_info[update]

        dev = dev + (update_fitness - average)**2

    if n > 1:
       dev = dev / float(n - 1)
       dev = math.sqrt(dev)
       dev = dev / math.sqrt(n)
    else:
       dev = 0

    stderr_by_update[update] = dev

# finally, output!
outfp = open('multiple-averages.txt', 'w')

# we want to output in order sorted by update, though.
updates = fitness_by_update.keys()
updates.sort()

for update in updates:
    average = fitness_by_update[update]
    dev = stderr_by_update[update]

    print >>outfp, update, average, dev

