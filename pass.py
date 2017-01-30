#!/bin/python
import random

Words = {}
with open('Words/working', 'r') as f:
    for line in f:
        Words = [line.strip() for line in f]


out = (random.choice(Words),'_',random.choice(Words),'_',random.choice(Words))
print ''.join(map(str, out))
