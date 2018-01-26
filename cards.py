#!/usr/bin/python
import sys
import pickle
import json

infile = sys.argv[1]
d = pickle.load( open(infile, "rb" ) )


cards = []
for card in d['cards']:
    #print json.dumps(card, indent=2)
    out = [card['cmc'], card['name']]
    cards.append(', '.join([str(c) for c in out]))

cards = list(set(cards))

for card in cards:
    print(card)
