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
INVERSION_LEN = 40
READ_LEN = 100
def findMicroInversions(read):
	global numG
	global numA
	global numT
	global numC
	global numN
	position = 0
	while position + INVERSION_LEN < READ_LEN:
		numA = 0
		numC = 0
		numG = 0
		numT = 0
		numN = 0
		revComp = reverseCompliment(read, position)
		if (numA, numC, numG, numT, numN) in sequencesDic:
			for element in sequencesDic[(numA, numC, numG, numT, numN)]:
				if sequence[element:element+READ_LEN] == revComp:
					print("The following contains a microinversion: " + sequence[element:element+READ_LEN])
					print("It matches with the read that starts at position " + str(element))
					print("The microinversion occurs at character position " + str(position))
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
	#print str(len(revComp)) + "blachh"
	temprev = read[position:position+INVERSION_LEN]
	temprev = temprev[::-1]
	#print temprev
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
	#print str(len(revComp)) + "after middle for"
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



#sequencesDic = pickle.load(open("sequencesDic.p", "rb"))
#sequence = pickle.load(open("seqString.p", "rb"))
i = 0
print len("GAAGCTCTTACTTTGCGACCTTTCGCCATCAACTAACGATTCTGTCAAAAACTGACGCGTTGGATGAGGAGAAGTGGCTTAATATGCTTGGCACGTTCGT")
while i + INVERSION_LEN < READ_LEN:
	print(len(reverseCompliment("GAAGCTCTTACTTTGCGACCTTTCGCCATCAACTAACGATTCTGTCAAAAACTGACGCGTTGGATGAGGAGAAGTGGCTTAATATGCTTGGCACGTTCGT", i)))
	i += 1
'''
for line in sys.stdin:
	line.strip("\n")
	findMicroInversions(line.upper())
'''
