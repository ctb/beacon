import sys, os

dirname = sys.argv[1]

dominant_file = os.path.join(dirname, 'dominant.dat')
fp = open(dominant_file)

last_line = None
for line in fp:
    line = line.strip()
    if line:
        last_line = line

last_line = last_line.split()

last_update = last_line[0]
dominant_genotype = last_line[-2]

###

population_file = 'detail-' + last_update + '.spop'
population_file = os.path.join(dirname, population_file)

fp = open(population_file)
for line in fp:
    line = line.strip()
    if not line:
        continue

    organism = line.split()[0]
    if organism == dominant_genotype:
        genome = line.split()[15]
        print genome
        break
