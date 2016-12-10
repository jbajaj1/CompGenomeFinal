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
	numAT = 0
	numCG = 0

	#dictionary to store the processedData
	sequences = {}
	for line in sys.stdin:
		#throw away header line
		if i == 0:
			i += 1
		else:
			#Adds every line in the sequence to the string of nucleotides
			seqString += line.strip("\n")

	seqString = seqString.upper()
	#write our reads to a pickle file
	pickle.dump(seqString, open("seqStringNew.p", "wb"))
	#begin processing
	position = 0
	while position + READ_LEN <= len(seqString):
		chunk = seqString[position:position+READ_LEN]
		#count occurences of each character
		for char in chunk:
			if char == 'N':
				numN += 1
			elif char == 'A' or char == 'T':
				numAT += 1
			elif char == 'C' or char == 'G':
				numCG += 1
		#map tuples of character occurences to indicies
		if (numAT, numCG, numN) in sequences:
			sequences[(numAT, numCG, numN)].append(position)
		else:
			sequences[(numAT, numCG, numN)] = [position]
		numAT = 0
		numCG = 0
		numN = 0
		position += 1
	#write dictionary to file
	pickle.dump(sequences, open("sequencesDicNew.p", "wb"))
		
#timing our preprocessing
start = time.time()
preprocessSeq()
end = time.time()
print("This program took " + str(end - start) + " seconds")
