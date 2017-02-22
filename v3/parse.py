#!/usr/bin/env python
# coding: utf-8

from argparse import ArgumentParser
import re
import string
import numpy
import math
import random

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

output = open(ARGS.output, 'w')
output.write(str(0)+"\t1\n")


angle = 0
turtle = numpy.array([0.0,1.0])

r = .5

random.seed(1)

for sign in punctuation:
    if sign in ['.','!','?']:
      angle += random.uniform(-math.pi,math.pi)/10
      jump = 1*numpy.array([math.cos(angle),math.sin(angle)])
      turtle += jump
    else:
      a = random.uniform(-math.pi,math.pi)
      jump = 1*r*numpy.array([math.cos(a),math.sin(a)])
      turtle += jump
      angle = a

    output.write(str(turtle[0])+"\t"+str(turtle[1])+"\n")









output.close()
