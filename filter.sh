#!/bin/bash
grep -o "[.,;:?\!]" $1 | tr -d "\n" | fold -w40 > $1.punct
#      |             |       |           |           |
#      |             |       |           |           |
#      --- grep filters the group of punctuation symbols:
#		   it is obviously easy to customize (adding the
# 		   Unicode symbols of a non-Latin alphabet)  |
#                    |       |           |           |
# filename here:-----'       |           |           |
#                            |           |           |
# pipes to tr (tr removes newlines and   |           |
# gives output on a single string)       |           |
#                                        |           |
# pipes to fold: outputs the punctuation in 40       |
# chars per line. No reason to explain why 40.       |
#                                                    |
# saves the formatted output on a .punct file--------'