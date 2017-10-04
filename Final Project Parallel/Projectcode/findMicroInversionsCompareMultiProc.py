import fileinput
import sys
import os
import getopt
import pickle
import time
import multiprocessing

#Initialize global variables
INVERSION_LEN = 100
MIN_INVERSION = 15
READ_LEN = 100
numProcs = 8

if MIN_INVERSION < 1:
    raise ValueError("ERROR: MIN_INVERSION TOO SMALL, MUST BE >= 1")
    
if MIN_INVERSION > INVERSION_LEN:
    raise ValueError("ERROR: INVERSION_LEN SMALLER THAN MIN_INVERSION")

if INVERSION_LEN > READ_LEN:
    raise ValueError("ERROR: READ_LEN SMALLER THAN MAX INVERSION")

if numProcs <= 0:
    raise ValueError('ERROR: NUMPROCS MUST BE GREATER THAN 0')

#function to detect microinversion from a read
def findMicroInversions(read):
    global INVERSION_LEN
    global READ_LEN
    global MIN_INVERSION
    invLen = INVERSION_LEN
    density = readDensity(read)
    fullInv = fullInversion(read)
    #loop to try all inversion sizes starting from INVERSION_LEN
    while invLen >= MIN_INVERSION:
        position = 0
        charDensity = list(density)
        #loop to check all of the possible inversions of the given length
        while position + invLen <= READ_LEN:
            #generate reverse Compliment of the read given the position we are starting the inversion
            invRead, charDensity = revCompliment(read, position, charDensity, invLen, fullInv)
            results = checkDicMultiProc(invRead, charDensity)
            for el in results:
                if el[0]:
                    print("The following contains a microinversion: " + read.strip("\n"))
                    print("The inversion length is " + str(invLen))
                    print("It matches with the read that starts at position " + str(el[1]))
                    print("The microinversion occurs at character position " + str(position) + " in the read")
                    print("It matches to: " + sequence[el[1]:el[1]+READ_LEN])
                    return True
            position += 1
        invLen -= 1
    return False

#Takes the list returned by the character density and divides up the work for 8 processes to handle
def checkDicMultiProc(invRead, charDensity):
    global numProcs
    if (charDensity[0], charDensity[1], charDensity[2], charDensity[3], charDensity[4]) in sequencesDic:
        numEl = len(sequencesDic[(charDensity[0], charDensity[1], charDensity[2], charDensity[3], charDensity[4])])
        lstEl = []
        for i in range(0, numEl):
            lstEl.append((i, sequencesDic[(charDensity[0], charDensity[1], charDensity[2], charDensity[3], charDensity[4])], invRead.strip('\n')))
        p = multiprocessing.Pool(numProcs)
        results = p.map(checkDictionary, lstEl)
        p.close()
        p.join()
        return results
    return [(False, 0), (False, 0)]

#Each Process is sent to this method to check its given positions to see if there is a match.
#If there is, it returns True and the position of the match in the sequence
def checkDictionary(tup):
    el = tup[0]
    indices = tup[1]
    invRead = tup[2]
    if sequence[indices[el]:indices[el]+READ_LEN] == invRead:
        return (True, indices[el])
    return (False, 0)

#gets the reverse compliment of the read given an invLen
def revCompliment(read, position, charDensity, invLen, fullInv):
    if position == 0:
        revComp = fullInv[READ_LEN-invLen:READ_LEN] + read[invLen:]
        for i in range(position+invLen-1, position-1, -1):
            if revComp[i] == 'A':
                charDensity[0] += 1
                charDensity[3] -= 1
            elif revComp[i] == 'G':
                charDensity[2] += 1
                charDensity[1] -= 1
            elif revComp[i] == 'T':
                charDensity[3] += 1
                charDensity[0] -= 1
            elif revComp[i] == 'C':
                charDensity[1] += 1
                charDensity[2] -= 1
        return [revComp, charDensity]
    else:
        #print("inside else")
        revComp = read[0:position] + fullInv[READ_LEN-invLen-position:READ_LEN-position] + read[position+invLen:]
        if revComp[position-1] == 'A':
            charDensity[0] += 1
            charDensity[3] -= 1
        elif revComp[position-1] == 'G':
            charDensity[2] += 1
            charDensity[1] -= 1
        elif revComp[position-1] == 'T':
            charDensity[3] += 1
            charDensity[0] -= 1
        elif revComp[position-1] == 'C':
            charDensity[1] += 1
            charDensity[2] -= 1

        if revComp[position] == 'A':
            charDensity[0] += 1
            charDensity[3] -= 1
        elif revComp[position] == 'G':
            charDensity[2] += 1
            charDensity[1] -= 1
        elif revComp[position] == 'T':
            charDensity[3] += 1
            charDensity[0] -= 1
        elif revComp[position] == 'C':
            charDensity[1] += 1
            charDensity[2] -= 1

        return [revComp, charDensity]   

#returns a full inversion of the read
def fullInversion(read):
    inversion = ""
    read = read[::-1]
    compliments = {'A':'T','T':'A','C':'G','G':'C', 'N':'N'}
    for char in read:
        inversion += compliments[char]
    return inversion

#calculates the initial read's character density
def readDensity(read):
    numA = 0
    numC = 0
    numG = 0
    numT = 0
    numN = 0
    for char in read:
        if char == "A":
            numA += 1
        elif char == "C":
            numC += 1
        elif char == "G":
            numG += 1
        elif char == "T":
            numT += 1
        elif char == "N":
            numN += 1
    return (numA, numC, numG, numT, numN)

#time the run
start = time.time()
sequencesDic = pickle.load(open("sequencesDic.p", "rb"))
sequence = pickle.load(open("seqString.p", "rb"))
endPickle = time.time()
for line in sys.stdin:
    line = line.strip("\n")
    startRead = time.time()
    isFound = findMicroInversions(line.upper())
    endRead = time.time()
    if not isFound:
        print(line + " had no microinversion found!")
    print("This read took " + str(endRead - startRead) + " seconds to process.")
end = time.time()
print("The pickle files took " + str(endPickle-start) + " seconds to open.")
print("The reads took " + str(end-endPickle) + " seconds to run.")
print("This program took " + str(end-start) + " seconds to run.")
