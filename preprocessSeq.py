import fileinput
import sys
import os
import getopt
import pickle

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
	position = 0
	while position + 40 < len(seqString):
		chunk = seqString[position:position+40]
		for char in chunk:
			if char == 'N' or char == 'n':
				numN += 1
			elif char == 'A' or char == 'a':
				numA += 1
			elif char == 'C' or char == 'c':
				numC += 1
			elif char == 'G' or char == 'g':
				numG += 1
			elif char == 'T' or char == 't':
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