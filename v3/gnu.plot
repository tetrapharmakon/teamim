set size ratio -1

unset border
unset xtics
unset ytics
unset label
unset key

set terminal pdf
set output 'plot.pdf'

set view equal xy

set style line 1 lt 0 lw 1 linecolor rgb "black"

plot "$1-data.angles" with lines
