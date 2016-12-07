import fileinput
import sys
import os
import getopt
import pickle
import time

#global to keep track of our  read length
READ_LEN = 100


def preprocessSeq():
	i = 0
	seqString = ""
	#variables to keep track of the number of occurences of each character
	numN = 0
	numA = 0
	numC = 0
	numG = 0
	numT = 0
	#dictionary to store the processedData
	sequences = {}
	for line in sys.stdin:
		#throw away lines without nucleotides
		if i == 0:
			i += 1
		else:
			seqString += line.strip("\n")

	seqString = seqString.upper()
	#write our reads to a pickle file
	pickle.dump(seqString, open("seqString.p", "wb"))

	#begin processing
	position = 0
	while position + READ_LEN <= len(seqString):
		chunk = seqString[position:position+READ_LEN]
		#count occurences of each character
		for char in chunk:
			if char == 'N':
				numN += 1
			elif char == 'A':
				numA += 1
			elif char == 'C':
				numC += 1
			elif char == 'G':
				numG += 1
			elif char == 'T':
				numT += 1
		#map tuples of character occurences to indicies
		if (numA, numC, numG, numT, numN) in sequences:
			sequences[(numA, numC, numG, numT, numN)].append(position)
		else:
			sequences[(numA, numC, numG, numT, numN)] = [position]
		numA = 0
		numC = 0
		numG = 0
		numT = 0
		numN = 0
		position += 1
		#write dictionary to file
		pickle.dump(sequences, open("sequencesDic.p", "wb"))
		
#timing our preprocessing
start = time.time()
preprocessSeq()
end = time.time()
print("This program took " + str(end - start) + " seconds")
