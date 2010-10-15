#! /bin/bash

# run things for the first time.
cp -r run.template run.1
cd run.1
avida
cd ..

# now, run forever and use CTRL-C to exit.  if you want to do only a
# limited set of serial transfers, then use a 'for' loop instead; see
# http://tldp.org/LDP/Bash-Beginners-Guide/html/chap_09.html
while true;
do
   python /root/beacon/ltee/run-next.py . || break
done
