#!/bin/bash
echo "\documentclass[margin=2mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc}
\def\angle{60}
\begin{document}
\begin{tikzpicture}
\draw (0,0)" >> dirs.tex

sym=`grep -o "[.,;:?\!]" babel.txt | tr -d "\n" | sed -e 's/\(.\)/\1 /g'`
ar=( $sym )
for i in "${ar[@]}"
do
case $i in
	"?") echo "-- +(60:1)" >> dirs.tex
		;;
	"!") echo "-- +(-120:1)" >> dirs.tex
		;;
	".") echo "-- +(0:1)" >> dirs.tex
		;;
	",") echo "-- +(180:1)" >> dirs.tex
		;;
	";") echo "-- +(-60:1)" >> dirs.tex
		;;
	":") echo "-- +(120:1)" >> dirs.tex
		;;
esac
done
echo ";
\end{tikzpicture}
\end{document}" >> dirs.tex