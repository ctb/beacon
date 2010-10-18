import sys, shutil

# a function to decode genome strings => actual base organisms.
def decode(s, instruction_filename):
    instructions = open(instruction_filename)

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

    x = []
    for ch in s:
        x.append(char_to_inst[ch])

    return x

###
# actual script code

genomestr = sys.argv[1]
instructionset = 'run.template/instset-heads.cfg'

for n in range(len(genomestr)):
    mutated_genome = ""
    for m in range(len(genomestr)):
        if m == n:              # mutate THIS POSITION
            if genomestr[m] == 'a':
                mutated_genome += 'b' # change nop-A to nop-B
            else:
                mutated_genome += 'a' # change nop-B to nop-A
        else:
            mutated_genome += genomestr[m] # no change

    mutated_org = decode(mutated_genome, instructionset)
    mutated_org = "\n".join(mutated_org)

    shutil.copytree('run.template', 'run.%d' % n)
    fp = open('run.%d/default-heads.org' % n, 'w')
    fp.write(mutated_org)
    fp.close()
