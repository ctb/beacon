import sys
import os, glob
import shutil
import subprocess

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
# retrieve dominant organism from the last run
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
dominant_genotype = last_line[-2]

### now get the actual genome from the 'detail-' file:

population_file = 'detail-' + last_update + '.spop'
population_file = os.path.join(last_run_data, population_file)

fp = open(population_file)
for line in fp:
    line = line.strip()
    if not line:
        continue

    organism = line.split()[0]
    if organism == dominant_genotype:
        genome = line.split()[15]
        break

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

org_name = 'run.%d-dominant.org' % last_run
org_filename = os.path.join(new_run_dir, org_name)
orgfp = open(org_filename, 'w')

for ch in genome:
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

subprocess.call('avida', cwd=new_run_dir)
