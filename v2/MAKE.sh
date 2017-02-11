#!/usr/bin/env bash

basename=${1##*/}
basename=${basename%.*}

python2.7 parse.py --input $1 --output data.angles
gnuplot gnu.plot
mv plot.pdf ${basename}.pdf
