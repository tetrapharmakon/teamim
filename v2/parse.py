#!/usr/bin/env python
# coding: utf-8

from argparse import ArgumentParser
import re
import string

#=====================[ COMMANDLINE PARSING ]===================================

PARSER = ArgumentParser(
    description='Do neat stuff.')

PARSER.add_argument(
    '--input', type=str, required=True,
    help='input file')

PARSER.add_argument(
    '--output', type=str, required=True,
    help='output file')

ARGS = PARSER.parse_args()

#=====================[ MAIN LOOP ]=============================================


prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359]
# 41st is 179

with open(ARGS.input, 'r') as file:
    text = file.read()

punctuation = re.sub('[^,;:.!?]', '', text)

angle = 0

jumps = {
    ',' : prime[32],
    ';' : prime[35],
    ':' : prime[38],
    '.' : prime[20],
    '!' : prime[40],
    '?' : prime[40]
}


output = open(ARGS.output, 'w')
output.write(str(0)+"\t1\n")

for sign in punctuation:
    angle = (angle + jumps[sign]) % 360
    output.write(str(angle)+"\t1\n")

output.close()
