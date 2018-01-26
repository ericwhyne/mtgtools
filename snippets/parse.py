#!/usr/bin/python
import sys
import pickle

infile = sys.argv[1]
d = pickle.load( open(infile, "rb" ) )

print d['name']
