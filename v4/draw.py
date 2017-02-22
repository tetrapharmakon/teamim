#!/usr/bin/env python
# coding: utf-8

from argparse import ArgumentParser
import re
import string
import numpy as np
import math
import random
import os

#=====================[ COMMANDLINE PARSING ]===================================

PARSER = ArgumentParser(
    description='Do neat stuff.')

PARSER.add_argument(
    'input', type=str,
    help='input file')

PARSER.add_argument(
    '--output', type=str, required=False,
    help='output file')

PARSER.add_argument(
    '--split', type=str, required=False,
    help='splitting regexp')

ARGS = PARSER.parse_args()

#=====================[ MAIN LOOP ]=============================================

with open(os.path.join('../texts',ARGS.input)+'.txt', 'r') as file:
    text = file.read()

# praragraphs for babel
#split_text = re.split('\s\s',text)

# sections for ulysses
# split_text = re.split('-- I+ --',text)

if ARGS.split == None:
    split_text = [text]
else:
    split_text = re.split(ARGS.split,text)


split_punctuation = [re.sub('[^,;:.!?]', '', segment) for segment in split_text]

angle = 0
r = .5
random.seed(1)

turtle = np.array([0.0,0.0])
walk = []

for punctuation in split_punctuation:
    steps = np.array([turtle])
    for sign in punctuation:
        if sign in ['.','!','?']:
            angle += random.uniform(-math.pi,math.pi)/10
            jump = 1*np.array([math.cos(angle),math.sin(angle)])
            turtle += jump
        else:
            a = random.uniform(-math.pi,math.pi)
            jump = 1*r*np.array([math.cos(a),math.sin(a)])
            turtle += jump
            angle = a
        steps = np.append(steps, np.array([turtle]), axis=0)
        # print(steps)
    walk += [steps]




import plotly
from plotly.graph_objs import Scatter, Layout

data = []
for segment in walk:
    data += [Scatter(x=segment[:,0], y=segment[:,1])]

plotly.offline.plot(
    {
        "data": data,
        "layout": Layout(title=ARGS.input)
    },
    filename= 'graphs/' + (ARGS.output or ARGS.input) + '.html'
)





