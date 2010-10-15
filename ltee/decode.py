import sys

# load the genome in on the command line
genome = sys.argv[1]

# assume we're in an avida run directory
instructions = open('instset-heads.cfg')

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

for ch in genome:
    print char_to_inst[ch]
