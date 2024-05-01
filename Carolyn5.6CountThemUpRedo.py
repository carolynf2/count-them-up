'''
Carolyn Fang
5.6 Count Them Up Redo
Started May 1, 2024
'''

import random

iRandomNumbers = []

rng = random.Random()

for Numbers in range(100001):
        iRandomNumbers.append(rng.randint(1, 10))

for iIndex in range(1, 11, 1):
        print(iIndex, iRandomNumbers.count(iIndex))
