import fileinput
import sys
import os
import getopt
import pickle


numA = 0
numC = 0
numG = 0
numT = 0
numN = 0
INVERSION_LEN = 4
READ_LEN = 10
def findMicroInversions(read):
	c = 0
	global numG
	global numA
	global numT
	global numC
	global numN
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
					print("It matches with the read that starts at position " + str(element))
					print("The microinversion occurs at character position " + str(position))
					print("It comes from the following read: " + read)
	    position += 1	


def reverseCompliment(read, position):
	global numG
	global numA
	global numT
	global numC
	global numN
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



sequencesDic = pickle.load(open("sequencesDic.p", "rb"))
sequence = pickle.load(open("seqString.p", "rb"))

for line in sys.stdin:
	line.strip("\n")
	findMicroInversions(line.upper())
