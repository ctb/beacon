#! /bin/bash

# set locale settings for python/matplotlib
echo export LOCALE=C >> ~/.bashrc
echo export LANGUAGE=C >> ~/.bashrc
echo export LC_ALL=C >> ~/.bashrc
echo export LC_CTYPE=C >> ~/.bashrc
source ~/.bashrc

# make matplotlib default to pdf
if [ \! -d ~/.matplotlib ]; then
   mkdir ~/.matplotlib
fi

echo backend      : Cairo > ~/.matplotlib/matplotlibrc

echo 'Congratulations!  You have successfully configured your AWS EC2 supermachne'
