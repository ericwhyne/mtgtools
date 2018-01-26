#!/usr/bin/python
import json
import sys

infile = sys.argv[1]

with open(infile) as json_file:
    d = json.load(json_file)

print d['name']
