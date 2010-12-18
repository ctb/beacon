import os
import sys, shutil

def setup_run(rundir, inflow, outflow, update1, initial1, update2, initial2):
    os.chdir(rundir)
    shutil.copy('avida.cfg', 'avida.cfg.bak')
    shutil.copy('environment.cfg', 'environment.cfg.bak')
    shutil.copy('events.cfg', 'events.cfg.bak')

    # modify environment.cfg
    fp = open('environment.cfg', 'a')
    fp.write('''
RESOURCE Echose:inflow=%s:outflow=%s
REACTION ECHO echo process:resource=Echose:value=1.0:type=pow
''' % (inflow, outflow))
    fp.close()
    
    # modify events.cfg
    fp = open('events.cfg', 'a')
    fp.write('''
u %s SetResourceInflow Echose initial=%s
u %s SetResourceInflow Echose initial=%s
''' % (update1, initial1, update2, initial2))
    fp.close()

###

shutil.rmtree('/mnt/run.1')
shutil.copytree('/root/run.template', '/mnt/run.1')
setup_run('/mnt/run.1', 100, .01, 500, 1, 1000, 1000)
