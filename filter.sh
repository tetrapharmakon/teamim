#!/bin/bash
grep -o 
# grep filters the group of punctuation symbols:
# it is obviously easy to customize (adding the
# Unicode symbols of a non-Latin alphabet)
"[.,;:?\!]" 
# filename here:
$1 
# pipes to tr (tr removes newlines and
# gives output on a single string)
| tr -d "\n" 
# pipes to fold: outputs the punctuation in 40
# chars per line. No reason to explain why 40.
| fold -w40; 
# saves the formatted output on a .punct file
> $1.punct
