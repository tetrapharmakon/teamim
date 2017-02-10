#!/usr/bin/env bash
grep -o "[.,;:?\!]" $1 | tr -d "\n" > $1.intpunct
#      |             |       |
#      |             |       |
#      |             -       -
# grep filters the group of punctuation symbols:
# it is obviously easy to customize (adding the
# Unicode symbols of a non-Latin alphabet)
#                    -       -
#                    |       |
# filename here:-----'       |
#                            |
# pipes to tr (tr removes newlines and
# gives output on a single string)
