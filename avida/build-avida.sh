# this will install things into your current directory
echo 'getting a copy of avida'
svn co https://avida.devosoft.org/svn/development avida

cd avida
cmake .
make

cp bin/avida /usr/local/bin

mkdir beacon
cd beacon
cp ../support/config/{avida,environment,instset-heads}.cfg .
cp ../support/config/default-heads.org .

curl -O http://ged.msu.edu/angus/files/events.cfg

echo 'Done\! Installed Avida and configured it in avida/beacon'

