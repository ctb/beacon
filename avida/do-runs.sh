#! /bin/bash
for i in $*
do
    cd $i && avida && cd ../
done