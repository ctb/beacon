# run-next-2: run a serial transfer experiment, always transferring N
#    random organisms

N = 10

assert N >= 1, "invalid N! must be positive."

###

import sys
import os, glob
import shutil
import subprocess
import random

# retrieve parent directory from command line
parent_dir = sys.argv[1]
run_dirs = os.path.join(parent_dir, 'run.*')
run_dirs = glob.glob(run_dirs)

# find the last one -- not alphabetic last, but numeric last!
run_nums = []
for dir in run_dirs:
    num = dir.split('.')[-1]
    print num
    try:
        num = int(num)
    except ValueError:
        continue

    run_nums.append(num)

last_run = max(run_nums)

last_run_dir = 'run.%d' % last_run
last_run_dir = os.path.join(parent_dir, last_run_dir)

assert os.path.isdir(os.path.join(last_run_dir, 'data'))

# ok, we've got the last one.  make a new one!
new_run_dir = 'run.%d' % (last_run + 1)
new_run_dir = os.path.join(parent_dir, new_run_dir)

template_dir = os.path.join(parent_dir, 'run.template')

shutil.copytree(template_dir, new_run_dir)

#
# use 'dominant.dat' to figure out what the last update was.
#

last_run_data = os.path.join(parent_dir, last_run_dir, 'data')
dominant_file = os.path.join(last_run_data, 'dominant.dat')
fp = open(dominant_file)

last_line = None
for line in fp:
    line = line.strip()
    if line:
        last_line = line

last_line = last_line.split()

last_update = last_line[0]

### now get the actual genomes from the 'detail-' file:

population_file = 'detail-' + last_update + '.spop'
population_file = os.path.join(last_run_data, population_file)

all_organisms = []

fp = open(population_file)
for line in fp:
    line = line.strip()
    if not line or line.startswith('#'):
        continue

    line = line.split(' ')
    organism = line[0]
    genome = line[16]
    all_organisms.append((organism, genome))

# choose N, randomly.
transfer_pop = random.sample(all_organisms, N)

# ok, now we have to do two things: first, we have to stick in the *starting*
# organism, which we'll make the first of the critters we selected.  All others
# will be inserted using 'InjectSequence'.

# get first organism.
(org_id, first_genome) = transfer_pop[0]
print transfer_pop[0]

# OK!  now translate.
instset_filename = os.path.join(new_run_dir, 'instset-heads.cfg')
instructions = open(instset_filename)

# build the dictionary mapping instruction characters to instructions
char_to_inst = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

n = 0
for line in instructions:
    line = line.strip()

    if not line:
        continue
    if line.startswith('#'):
        continue

    # all right, non-empty line... save instruction with corresp character
    the_inst = line.split()[0]
    char = alphabet[n]
    char_to_inst[char] = the_inst
    n += 1

##

org_name = 'run.%d-first.org' % last_run
org_filename = os.path.join(new_run_dir, org_name)
orgfp = open(org_filename, 'w')

print >>orgfp, "# organism %s from run %d" % (org_id, last_run)
for ch in first_genome:
    print >>orgfp, char_to_inst[ch]
orgfp.close()

###

old_cfg = os.path.join(new_run_dir, 'avida.cfg.bak')
new_cfg = os.path.join(new_run_dir, 'avida.cfg')
shutil.move(new_cfg, old_cfg)

outfp = open(new_cfg, 'w')
for line in open(old_cfg):
    if line.startswith('START_CREATURE'):
        print >>outfp, 'START_CREATURE', org_name
    else:
        outfp.write(line)
outfp.close()

###

# now, also modify the events file to inject the remaining critters
eventsfp = open('events.cfg', 'a')

print >>eventsfp, "\n# injecting as part of serial transfer:"
for (org_id, genome) in transfer_pop[1:]:
    print >>eventsfp, "u 0 InjectSequence %s  # organism %s from run %d" % \
        (genome, org_id, last_run)

###

subprocess.call('avida', cwd=new_run_dir)
