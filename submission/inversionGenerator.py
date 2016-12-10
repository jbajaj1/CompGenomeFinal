#!/usr/bin/python

import sys
import random

READ_LENGTH = 100
NUM_READS = 500
MIN_INVERSION_LENGTH = 15
MAX_INVERSION_LENGTH = 100

def parse_input():
    data = ""
    sys.stdin.readline()
    for line in sys.stdin:
        data += line.strip().upper()
    return data

def simulate_reads():
    global READ_LENGTH
    global NUM_READS

    reads = []
    indecies = []
    
    for i in range(NUM_READS):
        readIndex = random.randint(0, len(data) - READ_LENGTH)
        read = data[readIndex:readIndex + READ_LENGTH]
        reads.append(read)    
        indecies.append(readIndex)
    return reads, indecies

def generate_inversions(seq, numInversions, readStart):
    global MIN_INVERSION_LENGTH
    global MAX_INVERSION_LENGTH
    global READ_LENGTH

    compliments = {'A':'T','T':'A','C':'G','G':'C', 'N':'N'} # Reverse complement map
    invertedSegments = [] # Keep track of inverted segments to prevent overlapping inversions

    for i in range(numInversions):
        collision = True
        
        while (collision):
            collision = False
            inversionLen = random.randint(MIN_INVERSION_LENGTH, MAX_INVERSION_LENGTH)
#print(len(seq), inversionLen)
#            print(seq, "!!!")
            inversionIndex = random.randint(0, len(seq) - inversionLen)
            
            for prevInversion in invertedSegments:
                if ((inversionIndex <= prevInversion[0] and inversionIndex + inversionLen >= prevInversion[0]) or (inversionIndex <= prevInversion[1] and inversionIndex + inversionLen >= prevInversion[1])):
                    collision = True

#        print("Read from index %d to %d in the sequence with a %dbp microinversion from %d to %d" % (readStart, readStart + READ_LENGTH, inversionLen, inversionIndex, inversionIndex + inversionLen))
        originalSeq = seq[inversionIndex:inversionIndex + inversionLen]
        invertedSegments.append((inversionIndex, inversionIndex + inversionLen))
        
        invertedSegment = ""
        for n in range(1, inversionLen + 1):
            invertedSegment += compliments[originalSeq[-n]]

    return seq[:inversionIndex] + invertedSegment + seq[inversionIndex + inversionLen:], inversionLen, inversionIndex

data = parse_input()
reads, indecies = simulate_reads()
#print(reads, indecies)

for i in range(len(reads)):
    read = reads[i]
    index = indecies[i]

    invertedRead, inversionLen, inversionIndex = generate_inversions(read, 1, index)
#    print("Read with %dbp micro inversion at index %d" % (inversionLen, inversionIndex))
    print(invertedRead)
#    print("Original read at index %d" % index)
#    print(read)


