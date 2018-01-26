#!/usr/bin/python
import sys
import pickle
import json
import glob

indir = sys.argv[1]

setFiles = glob.glob(indir + "*.json")
print setFiles
ignoreLanguages = ['de', 'es', 'fr', 'it', 'cn', 'ru']
for setFile in setFiles:
'''
allcards = []
for setFile in setFiles:
    with open(infile) as json_file:
        d = json.load(json_file)
    setcards = []
    for card in d['cards']:
        #print json.dumps(card, indent=2)
        out = [card['cmc'], card['name']]
        setcards.append(', '.join([str(c) for c in out]))

    cards = list(set(cards))

    for card in cards:
        print(card)
'''
