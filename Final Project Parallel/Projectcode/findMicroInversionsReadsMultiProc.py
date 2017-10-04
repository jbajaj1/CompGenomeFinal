import fileinput
import sys
import os
import getopt
import pickle
import time
import multiprocessing
from multiprocessing import Queue

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
	starttime = time.time()
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
			#try all the hits from the preprocessed dictionary.
			for element in sequencesDic.get((charDensity[0], charDensity[1], charDensity[2], charDensity[3], charDensity[4]), []):
				if sequence[element:element+READ_LEN].strip("\n") == invRead.strip("\n"):
					resQueue.put('The following contains a microinversion: ' + read + '\nThe inversion length is ' + str(invLen) + '\nIt matches with the read that starts at position ' + str(element) + '\nThe microinversion occurs at character position ' + str(position) + ' in the read\nIt matches to: '+ sequence[element:element+READ_LEN] + '\nThis read took ' + str(time.time()-starttime) + ' seconds to process.')
					return True
			position += 1
		invLen -= 1
	resQueue.put(read + ' had no microinversion found!\nThis read took ' + str(time.time()-starttime) + ' seconds to process.')
	return False


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

def manageReads(lstReads):
	global numProcs
	numReads = len(lstReads)
	if numReads > 0:
		p = multiprocessing.Pool(numProcs)
		p.map(findMicroInversions, lstReads)
		#p.close()
		#p.join()
	else: 
		print "No reads inputted!"

#time the run
start = time.time()
sequencesDic = pickle.load(open("sequencesDic.p", "rb"))
sequence = pickle.load(open("seqString.p", "rb"))
endPickle = time.time()
lstReads = []
resQueue = Queue()
for line in sys.stdin:
	lstReads.append(line.strip('\n').upper())
manageReads(lstReads)
for q in range(resQueue.qsize()):
	print resQueue.get()
end = time.time()
print("The pickle files took " + str(endPickle-start) + " seconds to open.")
print("The reads took " + str(end-endPickle) + " seconds to run.")
print("This program took " + str(end-start) + " seconds to run.")
