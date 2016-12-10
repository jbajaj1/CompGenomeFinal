import fileinput
import sys
import os
import getopt
import pickle
import time
import thread
from multiprocessing import Pool

numA = 0
numC = 0
numG = 0
numT = 0
numN = 0
invN = 0
INVERSION_LEN = 100
MIN_INVERSION = 15
READ_LEN = 100
MAX_N = 2
found = False
def findMicroInversions(read):
	startRead = time.time()
	global numG
	global numA
	global numT
	global numC
	global numN
	global invN
	global MAX_N
	global found
	global INVERSION_LEN
	found = False
	INVERSION_LEN = 100
	nextRead = False
	while INVERSION_LEN >= MIN_INVERSION:
		if nextRead:
			break;
		position = 0
		skip = False
		while position + INVERSION_LEN <= READ_LEN:
			if skip:
				break
			numA = 0
			numC = 0
			numG = 0
			numT = 0
			numN = 0
			invN = 0
			revComp = reverseCompliment(read, position)
			if invN > MAX_N:
				position += 1
				break
			elif invN > 0 and invN <= MAX_N:
				result = nHandling(revComp, revComp, invN, numA, numC, numG, numT, numN, invN, position)
				if found is True:
					nextRead = True
					break

			for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
				if sequence[element:element+READ_LEN].strip("\n") == revComp.strip("\n"):
					print("The following contains a microinversion: " + read.strip("\n"))
					print("The inversion length is " + str(INVERSION_LEN))
					print("It matches with the read that starts at position " + str(element))
					print("The microinversion occurs at character position " + str(position) + " in the read")
					print("It matches to: " + sequence[element:element+READ_LEN])
					nextRead = True
					skip = True
					break
			position += 1
		INVERSION_LEN -= 1
	endRead = time.time()
	print("This read took " + str(endRead - startRead) + " seconds to process.")
	'''
	VERSION WITHOUT VARYING INVERSION LENGTH
	position = 0
	while position + INVERSION_LEN <= READ_LEN:
		numA = 0
		numC = 0
		numG = 0
		numT = 0
		numN = 0
		revComp = reverseCompliment(read, position)
		if (numA, numC, numG, numT, numN) in sequencesDic:
			for element in sequencesDic[(numA, numC, numG, numT, numN)]:
				if sequence[element:element+READ_LEN].strip("\n") == revComp.strip("\n"):
					print("The following contains a microinversion: " + sequence[element:element+READ_LEN])
					print("The inversion length is " + str(INVERSION_LEN))
					print("It matches with the read that starts at position " + str(element))
					print("The microinversion occurs at character position " + str(position))
					print("It comes from the following read: " + read)
					#return statement -- discuss with group if we should have
		position += 1
	'''


def nHandling(read, unchangedRead, Ns, As, Cs, Gs, Ts, otherNs, origNs, position):
	global found
	if found == True:
		return 0
	if Ns > 0:
		nHandling(read[0:position] + read[position:position+INVERSION_LEN].replace("N", "A", 1) + read[position+INVERSION_LEN:], unchangedRead, Ns - 1, As + 1, Cs, Gs, Ts, otherNs - 1, origNs, position)
		nHandling(read[0:position] + read[position:position+INVERSION_LEN].replace("N", "C", 1) + read[position+INVERSION_LEN:], unchangedRead, Ns - 1, As, Cs + 1, Gs, Ts, otherNs - 1, origNs, position)
		nHandling(read[0:position] + read[position:position+INVERSION_LEN].replace("N", "G", 1) + read[position+INVERSION_LEN:], unchangedRead, Ns - 1, As, Cs, Gs + 1, Ts, otherNs - 1, origNs, position)
		nHandling(read[0:position] + read[position:position+INVERSION_LEN].replace("N", "T", 1) + read[position+INVERSION_LEN:], unchangedRead, Ns - 1, As, Cs, Gs, Ts + 1, otherNs - 1, origNs, position)
	if found == True:
		return 0
	for element in sequencesDic.get((As, Cs, Gs, Ts, otherNs), []):
		if sequence[element:element+READ_LEN].strip("\n") == read.strip("\n"):
			print("The following may contain a microinversion: " + unchangedRead.strip("\n"))
			print("It contained " + str(origNs) + " N(s) that were converted into different nucleotides")
			print("The inversion length is " + str(INVERSION_LEN))
			print("It matches with the read that starts at position " + str(element))
			print("The microinversion occurs at character position " + str(position) + " in the read")
			print("It matches to: " + sequence[element:element+READ_LEN])
			found = True
	if found == True:
		return 0


def reverseCompliment(read, position):
	global numG
	global numA
	global numT
	global numC
	global numN
	global invN
	global INVERSION_LEN
	revComp = read[0:position]
	for char in revComp:
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
	temprev = read[position:position+INVERSION_LEN]
	temprev = temprev[::-1]
	for char in temprev:
		if char == "A":
			revComp += "T"
			numT += 1
		elif char == "C":
			revComp += "G"
			numG += 1
		elif char == "G":
			revComp += "C"
			numC += 1
		elif char == "T":
			revComp += "A"
			numA += 1
		elif char == "N":
			revComp += "N"
			numN += 1
			invN +=1
	revComp += read[position+INVERSION_LEN:]
	for char in read[position+INVERSION_LEN:]:
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
	return revComp


start = time.time()
sequencesDic = pickle.load(open("sequencesDic.p", "rb"))
sequence = pickle.load(open("seqString.p", "rb"))
#start = time.time()   <--- Talk to team about this
reads = []

for line in sys.stdin:
	line.strip("\n")
	reads.append(line.upper())
	#startRead = time.time()
	#findMicroInversions(line.upper())
	#endRead = time.time()
	#print("This read took " + str(endRead - startRead) + " seconds to process.")
pool = Pool(4)
pool.map(findMicroInversions, reads)
end = time.time()
print("This program took " + str(end-start) + " seconds to run.")
