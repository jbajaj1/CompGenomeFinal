#!/usr/bin/python

import sys
import random

"""
def parse_input(f):
    data = ""
    counter = 0
    for line in f:
        if (line[0] != '>'):
            for char in line.lower():
                if (char != 'n'):
                    print(char)
                    data += char
                    counter += 1
# if (counter > 100):
#               break
    return data
"""

def generate_inversions(seq, numInversions, minLen, maxLen):
    compliments = {'A':'T','T':'A','C':'G','G':'C'}
    for i in range(numInversions):
        inversionLen = random.randint(minLen, maxLen)
        inversionIndex = random.randint(0, len(seq) - inversionLen)
        originalSeq = seq[inversionIndex:inversionIndex + inversionLen]
        print("Inversion %d: index = %d, len = %d" % (i, inversionIndex, inversionLen))
        invertedSegment = ""
        for n in range(inversionLen):
            invertedSegment += compliments[originalSeq[-n]]
    return seq[:inversionIndex] + invertedSegment + seq[inversionIndex + inversionLen:]

# Hardcoded example sequence
data = "ACGTTTTTTAAAAA"
invertedData = generate_inversions(data, 1, 3, 5)
print(data)
print(invertedData)


