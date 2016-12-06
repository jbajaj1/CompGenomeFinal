import fileinput
import sys
import os
import getopt
import pickle

READ_LEN = 10

def preprocessSeq():
	i = 0
	seqString = ""
	numN = 0 
	numA = 0
	numC = 0
	numG = 0
	numT = 0
	sequences = {}
	for line in sys.stdin:
		if i == 0:
			i += 1
		else:
			seqString += line.strip("\n")
	seqString = seqString.upper()
	pickle.dump(seqString, open("seqString.p", "wb"))
	position = 0
	while position + READ_LEN < len(seqString):
		chunk = seqString[position:position+READ_LEN]
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
		pickle.dump(sequences, open("sequencesDic.p", "wb"))

preprocessSeq()
