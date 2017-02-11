set size square

set terminal pdf
set output 'plot.pdf'

unset border
unset key
unset tics
unset raxis

set polar
set angles degrees

set style line 1 lt 0 lw 1 linecolor rgb "black"

plot "data.angles" with lines ls 1
