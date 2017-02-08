#!/usr/bin/env bash

cat $1 | tr --delete --complement '[:punct:]' > $1.punc

# NOTE: [:punct:] is a standard POSIX regexp character group
# equivalent to [!"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]
