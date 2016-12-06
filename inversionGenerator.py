#!/usr/bin/python

import sys
import random

def parse_input():
    data = ""
    sys.stdin.readline()
    for line in sys.stdin:
        data += line.strip().upper()
    return data

def generate_inversions(seq, numInversions, minLen, maxLen, readStart):
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
#                    print("Collision!")

        print("Read from index %d to %d in the sequence with a %dbp microinversion from %d to %d" % (readStart, readStart + 100, inversionLen, inversionIndex, inversionIndex + 40))
        originalSeq = seq[inversionIndex:inversionIndex + inversionLen]
        invertedSegments.append((inversionIndex, inversionIndex + inversionLen))
#print("Inversion %d: index = %d, len = %d" % (i, inversionIndex, inversionLen))
        
        invertedSegment = ""
        for n in range(1, inversionLen + 1):
            invertedSegment += compliments[originalSeq[-n]]

    return seq[:inversionIndex] + invertedSegment + seq[inversionIndex + inversionLen:]

data = parse_input()
#data = "ACGTTTTTTA" # Hardcoded example sequence
readIndex = random.randint(100, len(data) - 100)
read = data[readIndex:readIndex + 100]

invertedRead = generate_inversions(read, 1, 40, 40, readIndex)
#print("Read with 40bp micro inversion: %s" % invertedRead)
print(invertedRead)
print("Normal read from 0 to 100")
print(data[:100])
#print
#print(data[:100])
#print(data[100:200])

