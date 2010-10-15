import sys, shutil

shutil.move('avida.cfg', 'avida.cfg.bak')

outfp = open('avida.cfg', 'w')
for line in open('avida.cfg.bak'):
    if line.startswith('WORLD_X'):
        print 'FOUND line', line,
        print >>outfp, 'WORLD_X 20  # CHANGED'
    else:
        outfp.write(line)
