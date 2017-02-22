set size ratio -1

set terminal pdf
set output 'plot.pdf'

set view equal xy

set style line 1 lt 0 lw 1 linecolor rgb "black"

plot "data.angles" with lines
