if [ \! -d avida/beacon ]; then
   echo "I don't think you are in the right directory; no avida/beacon/."
   exit -1
fi

cd avida/beacon

if [ \! -f avida.cfg ]; then
    echo "This doesn't look like an avida-configured directory... no avida.cfg"
    exit -1
fi

for i in {1..10}
do
    echo starting run $i
    avida && mv data data.$i
done
