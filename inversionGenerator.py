#!/usr/bin/python

import sys
import random

def parse_input():
    data = ""
    for line in sys.stdin:
        data += line.strip()
    return data

def generate_inversions(seq, numInversions, minLen, maxLen):
    compliments = {'A':'T','T':'A','C':'G','G':'C'} # Reverse complement map
    invertedSegments = [] # Keep track of inverted segments to prevent overlapping inversions

    for i in range(numInversions):
        collision = True
        
        while (collision):
            collision = False
            inversionLen = random.randint(minLen, maxLen)
            inversionIndex = random.randint(0, len(seq) - inversionLen)
            
            for prevInversion in invertedSegments:
                if ((inversionIndex <= prevInversion[0] and inversionIndex + inversionLen >= prevInversion[0]) or (inversionIndex <= prevInversion[1] and inversionIndex + inversionLen >= prevInversion[1])):
                    collision = True
                    print("Collision!")


        originalSeq = seq[inversionIndex:inversionIndex + inversionLen]
        invertedSegments.append((inversionIndex, inversionIndex + inversionLen))
        print("Inversion %d: index = %d, len = %d" % (i, inversionIndex, inversionLen))
        
        invertedSegment = ""
        for n in range(1, inversionLen + 1):
            invertedSegment += compliments[originalSeq[-n]]

    return seq[:inversionIndex] + invertedSegment + seq[inversionIndex + inversionLen:]

data = "ACGTTTTTTA" # Hardcoded example sequence
invertedData = generate_inversions(data, 1, 10, 10)
print(data)
print(invertedData)


