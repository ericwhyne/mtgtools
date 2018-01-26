#!/usr/bin/python
import json
import pickle
import sys
import logging
from os import path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LoadJson")

infile = sys.argv[1]
datadir = 'data/'

try:
    with open(infile) as json_file:
        d = json.load(json_file)
except:
    logger.error("Failed to load " + infile)

outfilename = datadir + path.splitext(path.basename(infile))[0] + '.pickle'

print outfilename

try:
    pickle.dump(d, open( outfilename, "wb" ) )
except:
    logger.error("Failed to write " + outfilename)

logger.info("Wrote data to " + outfilename)
