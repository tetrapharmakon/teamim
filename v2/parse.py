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


with open(ARGS.input, 'r') as file:
    text = file.read()

punctuation = re.sub('[^,;:.!?]', '', text)

angle = 0

jumps = {
    ',' : 10,
    ';' : 20,
    ':' : 30,
    '.' : 40,
    '!' : 50,
    '?' : 60
}


output = open(ARGS.output, 'w')
output.write(str(0)+"\n")

for sign in punctuation:
    angle = (angle + jumps[sign]) % 360
    output.write(str(angle)+"\n")

output.close()
