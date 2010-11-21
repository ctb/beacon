#! /usr/bin/env python
import sys
import csv
import optparse

##

import bowtie_parser

##

mismatch_d = {}

###

parser = optparse.OptionParser()
parser.add_option('-M', '--max-reads', dest='max_reads', default=0, type=int,
                  help='only use first M reads, then exit')

(options, args) = parser.parse_args()

bowtie_mapping_file, = args
bowtie_fp = open(bowtie_mapping_file)

###

# iterate over the bowtie mapping file (output from bowtie)
for n, line in enumerate(bowtie_parser.read(bowtie_fp)):
    # print out status/progress.
    if n % 10000 == 0:
        print>>sys.stderr, 'scanning reads', n

        if options.max_reads and n > options.max_reads:
            print>>sys.stderr, 'EXITING EARLY; -M specified as %d' % \
                               options.max_reads
            break
            
    # retrieve mismatches from the bowtie mapping
    mismatches = line.mismatches.strip()

    # record the mismatch positions
    if mismatches:
        mismatches = [ x for x in mismatches.split(',') if 'N' not in x ]

    for x in mismatches:
        pos, mismatch = x.split(':', 1)

        pos = int(pos)

        count = mismatch_d.get(pos, 0)
        count += 1
        mismatch_d[pos] = count

### output

output = csv.writer(sys.stdout)

keys = mismatch_d.keys()
keys.sort()

for pos in keys:
    count = mismatch_d[pos]
    frac = float(count) / float(n)

    output.writerow([pos, count, frac])
