#!/bin/python
import random

Words = {}
Seps = ['_','-','^','#','~','+','=']
with open('words.txt', 'r') as f:
    for line in f:
        Words = [line.strip() for line in f]


out = (random.choice(Words),random.choice(Seps),random.choice(Words),random.choice(Seps),random.choice(Words))
print ''.join(map(str, out))
