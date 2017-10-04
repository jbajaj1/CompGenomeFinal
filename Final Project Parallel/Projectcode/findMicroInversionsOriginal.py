import fileinput
import sys
import os
import getopt
import pickle
import time

#Initialize global variables
numA = 0
numC = 0
numG = 0
numT = 0
numN = 0
invN = 0
INVERSION_LEN = 100
MIN_INVERSION = 15
READ_LEN = 100
#Threshold for how many N's in the read we will handle
MAX_N = 0
found = False
#function to detect microinversion from a read
def findMicroInversions(read):
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
	#loop to try all inversion sizes starting from INVERSION_LEN
	while INVERSION_LEN >= MIN_INVERSION:
		position = 0
		#loop to check all of the possible inversions of the given length
		while position + INVERSION_LEN <= READ_LEN:
			numA = 0
			numC = 0
			numG = 0
			numT = 0
			numN = 0
			invN = 0
			#generate reverse Compliment of the read given the position we are starting the inversion
			revComp = reverseCompliment(read, position)
			#if there are too many N's we throw out that position
			if invN > MAX_N:
				position += 1
				break
			#if we need to handle any N's
			elif invN > 0 and invN <= MAX_N:
				result = nHandling(revComp, revComp, invN, numA, numC, numG, numT, numN, invN, position)
				if found is True:
					return 0
			#try all the hits from the preprocessed dictionary.
			for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
				if sequence[element:element+READ_LEN].strip("\n") == revComp.strip("\n"):
					print("The following contains a microinversion: " + read.strip("\n"))
					print("The inversion length is " + str(INVERSION_LEN))
					print("It matches with the read that starts at position " + str(element))
					print("The microinversion occurs at character position " + str(position) + " in the read")
					print("It matches to: " + sequence[element:element+READ_LEN])
					return 0
			position += 1
		INVERSION_LEN -= 1
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

#recursive function to handle the case where a read has N's in it
def nHandling(read, unchangedRead, Ns, As, Cs, Gs, Ts, otherNs, origNs, position):
	global found
	global numA
	global numC
	global numG
	global numT
	if found == True:
		return 0
	#recurse on the N being an A,C,G, or T
	if Ns > 0:
		nHandling(read[0:position] + read[position:position+INVERSION_LEN].replace("N", "A", 1) + read[position+INVERSION_LEN:], unchangedRead, Ns - 1, As + 1, Cs, Gs, Ts, otherNs - 1, origNs, position)
		nHandling(read[0:position] + read[position:position+INVERSION_LEN].replace("N", "C", 1) + read[position+INVERSION_LEN:], unchangedRead, Ns - 1, As, Cs + 1, Gs, Ts, otherNs - 1, origNs, position)
		nHandling(read[0:position] + read[position:position+INVERSION_LEN].replace("N", "G", 1) + read[position+INVERSION_LEN:], unchangedRead, Ns - 1, As, Cs, Gs + 1, Ts, otherNs - 1, origNs, position)
		nHandling(read[0:position] + read[position:position+INVERSION_LEN].replace("N", "T", 1) + read[position+INVERSION_LEN:], unchangedRead, Ns - 1, As, Cs, Gs, Ts + 1, otherNs - 1, origNs, position)
	if found == True:
		return 0
	#check the dictionary hits against the converted string
	for element in sequencesDic.get((As, Cs, Gs, Ts, otherNs), []):
		if sequence[element:element+READ_LEN].strip("\n") == read.strip("\n"):
			print("The following may contain a microinversion: " + unchangedRead.strip("\n"))
			print("It contained " + str(origNs) + " N(s) that were converted into different nucleotides")
			if As > numA:
				diff = As - numA
				print(str(diff) + " N(s) were converted to A(s)")
			if Cs > numC:
				diff = Cs - numC
				print(str(diff) + " N(s) were converted to C(s)")
			if Gs > numG:
				diff = Gs - numG
				print(str(diff) + " N(s) were converted to G(s)")
			if Ts > numT:
				diff = Ts - numT
				print(str(diff) + " N(s) were converted to T(s)")
			print("The inversion length is " + str(INVERSION_LEN))
			print("It matches with the read that starts at position " + str(element))
			print("The microinversion occurs at character position " + str(position) + " in the read")
			print("It matches to: " + sequence[element:element+READ_LEN])
			found = True
	if found == True:
		return 0

#generate the reverse complement and count the number of A,C,G,&T
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

#time the run
start = time.time()
sequencesDic = pickle.load(open("sequencesDic.p", "rb"))
sequence = pickle.load(open("seqString.p", "rb"))
endPickle = time.time()
for line in sys.stdin:
	line = line.strip("\n")
	startRead = time.time()
	findMicroInversions(line.upper())
	endRead = time.time()
	print("This read took " + str(endRead - startRead) + " seconds to process.")
end = time.time()
print("The pickle files took " + str(endPickle-start) + " seconds to open.")
print("The reads took " + str(end-endPickle) + " seconds to run.")
print("This program took " + str(end-start) + " seconds to run.")
