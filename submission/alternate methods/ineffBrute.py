import fileinput
import sys
import os
import getopt
import pickle
import time

numAT = 0
numCG = 0
numN = 0
INVERSION_LEN = 100
MIN_INVERSION = 15
READ_LEN = 100
def findMicroInversions(read):
	read = read.strip("\n")
	global numAT
	numAT = 0
	global numCG
	numCG = 0
	global numN
	numN = 0
	inv_len = 100
	revComp = reverseComp(read)
	while inv_len >= MIN_INVERSION:
		position = 0
		while position + inv_len <= READ_LEN:
			microInv = read[0:position] + revComp[(READ_LEN-(position+inv_len)):READ_LEN-position] + read[position+inv_len:]
			#print("micr " + microInv)
			if (numAT, numCG, numN) in sequencesDic:
				#print("elem " + sequencesDic[(numAT, numCG, numN)][0])
				for element in sequencesDic[(numAT, numCG, numN)]:
					if sequence[element:element+READ_LEN].strip("\n") == microInv:
						print("The following contains a microinversion: " + read.strip("\n"))
						print("The inversion length is " + str(inv_len))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
			position += 1	
		inv_len -= 1


def reverseComp(read):
	global numAT
	global numCG
	global numN
	revtemp = read[::-1]
	revComp = ""
	for char in revtemp:
		if char == "A": 
			revComp += "T"
			numAT += 1
		elif char == "C":
			revComp += "G"
			numCG += 1
		elif char == "G":
			revComp += "C"
			numCG += 1
		elif char == "T":
			revComp += "A"
			numAT += 1
		elif char == "N":
			revComp += "N"
			numN += 1
	return revComp



sequencesDic = pickle.load(open("sequencesDicNew.p", "rb"))
sequence = pickle.load(open("seqStringNew.p", "rb"))
start = time.time()
for line in sys.stdin:
	line.strip("\n")
	startRead = time.time()
	findMicroInversions(line.upper())
	endRead = time.time()
	print("This read took " + str(endRead - startRead) + " seconds to process.")
end = time.time()
print("This program took " + str(end-start) + " seconds to run.")
