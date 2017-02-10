#!/usr/bin/env bash
echo "\documentclass[margin=2mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc}
\def\angle{60}
\begin{document}
\begin{tikzpicture}
\draw (0,0)" >> dirs.tex

sym=`grep -o "[.,;:?\!]" babel.txt | tr -d "\n" | sed -e 's/\(.\)/\1 /g'`
ar=( $sym )
j=1
for i in "${ar[@]}"
do
case $i in
	"?") echo "-- +(60:$j)" >> dirs.tex
		;;
	"!") echo "-- +(-120:$j)" >> dirs.tex
		;;
	".") echo "-- +(0:$j)" >> dirs.tex
		;;
	",") echo "-- +(180:$j)" >> dirs.tex
		;;
	";") echo "-- +(-60:$j)" >> dirs.tex
		;;
	":") echo "-- +(120:$j)" >> dirs.tex
		;;
esac
((j++))
done
echo ";
\end{tikzpicture}
\end{document}" >> dirs.tex
