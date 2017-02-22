#!/usr/bin/env bash

./draw.py babel --split="\s\s"
./draw.py bible --split="The.*?Book of"
./draw.py cathedral
./draw.py hegel
./draw.py proust --split="CHAPITRE"
./draw.py ulysses --split="-- I+ --"
./draw.py wallace
