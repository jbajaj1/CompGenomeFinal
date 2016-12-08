import fileinput
import sys
import os
import getopt
import pickle
import time

numA = 0
numC = 0
numG = 0
numT = 0
numN = 0
invN = 0
INVERSION_LEN = 100
MIN_INVERSION = 15
READ_LEN = 100
def findMicroInversions(read):
	global numG
	global numA
	global numT
	global numC
	global numN
	global invN
	global INVERSION_LEN
	INVERSION_LEN = 100
	while INVERSION_LEN >= MIN_INVERSION:
		position = 0
		while position + INVERSION_LEN <= READ_LEN:
			numA = 0
			numC = 0
			numG = 0
			numT = 0
			numN = 0
			invN = 0
			revComp = reverseCompliment(read, position)
			if invN > 2:
				position += 1
				break
			elif invN == 1:
				numN -= 1 
				revCompA = read[0:position] + revComp[position:position+INVERSION_LEN].replace("N", "A", 1) + read[position+INVERSION_LEN:]
				numA += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompA.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to an A")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numA -=1
				revCompC = read[0:position] + revComp[position:position+INVERSION_LEN].replace("N", "C", 1) + read[position+INVERSION_LEN:]
				numC += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompC.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a C")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numC -= 1
				revCompG = read[0:position] + revComp[position:position+INVERSION_LEN].replace("N", "G", 1) + read[position+INVERSION_LEN:]
				numG += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompG.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a G")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numG -= 1
				revCompT = read[0:position] + revComp[position:position+INVERSION_LEN].replace("N", "T", 1) + read[position+INVERSION_LEN:]
				numT += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompT.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a T")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numN += 1
			elif invN == 2:
				numN -= 2 
				revCompA = read[0:position] + revComp[position:position+INVERSION_LEN].replace("N", "A", 1) + read[position+INVERSION_LEN:]
				numA += 1
				revCompAA = read[0:position] + revCompA[position:position+INVERSION_LEN].replace("N", "A", 1) + read[position+INVERSION_LEN:]
				numA += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompAA.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("Two Ns were converted to As")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numA -= 1
				revCompAC = read[0:position] + revCompA[position:position+INVERSION_LEN].replace("N", "C", 1) + read[position+INVERSION_LEN:]
				numC += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompAC.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to an A and one to a C")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numC -= 1
				revCompAG = read[0:position] + revCompA[position:position+INVERSION_LEN].replace("N", "G", 1) + read[position+INVERSION_LEN:]
				numG += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompAG.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to an A and one to a G")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numG -= 1
				revCompAT = read[0:position] + revCompA[position:position+INVERSION_LEN].replace("N", "T", 1) + read[position+INVERSION_LEN:]
				numT += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompAT.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to an A and one to a T")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numT -= 1
				numA -=1
				revCompC = read[0:position] + revComp[position:position+INVERSION_LEN].replace("N", "C", 1) + read[position+INVERSION_LEN:]
				numC += 1
				revCompCA = read[0:position] + revCompC[position:position+INVERSION_LEN].replace("N", "A", 1) + read[position+INVERSION_LEN:]
				numA += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompCA.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a C and one to an A")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numA -= 1
				revCompCC = read[0:position] + revCompC[position:position+INVERSION_LEN].replace("N", "C", 1) + read[position+INVERSION_LEN:]
				numC += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompCC.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("Two Ns were converted to Cs")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numC -= 1
				revCompCG = read[0:position] + revCompC[position:position+INVERSION_LEN].replace("N", "G", 1) + read[position+INVERSION_LEN:]
				numG += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompCG.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a C and one to a G")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numG -= 1
				revCompCT = read[0:position] + revCompC[position:position+INVERSION_LEN].replace("N", "T", 1) + read[position+INVERSION_LEN:]
				numT += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompCT.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a C and one to a T")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numT -= 1
				numC -=1
				revCompG = read[0:position] + revComp[position:position+INVERSION_LEN].replace("N", "G", 1) + read[position+INVERSION_LEN:]
				numG += 1
				revCompGA = read[0:position] + revCompG[position:position+INVERSION_LEN].replace("N", "A", 1) + read[position+INVERSION_LEN:]
				numA += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompGA.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a G and one to an A")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numA -= 1
				revCompGC = read[0:position] + revCompG[position:position+INVERSION_LEN].replace("N", "C", 1) + read[position+INVERSION_LEN:]
				numC += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompGC.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a G and one to a C")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN] + "\n\n")
						return 0
				numC -= 1
				revCompGG = read[0:position] + revCompG[position:position+INVERSION_LEN].replace("N", "G", 1) + read[position+INVERSION_LEN:]
				numG += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompGG.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("Two Ns were converted to Gs")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numG -= 1
				revCompGT = read[0:position] + revCompG[position:position+INVERSION_LEN].replace("N", "T", 1) + read[position+INVERSION_LEN:]
				numT += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompGT.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a G and one to a T")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numT -= 1
				numG -=1
				revCompT = read[0:position] + revComp[position:position+INVERSION_LEN].replace("N", "T", 1) + read[position+INVERSION_LEN:]
				numT += 1
				revCompTA = read[0:position] + revCompT[position:position+INVERSION_LEN].replace("N", "A", 1) + read[position+INVERSION_LEN:]
				numA += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompTA.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a T and one to an A")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numA -= 1
				revCompTC = read[0:position] + revCompT[position:position+INVERSION_LEN].replace("N", "C", 1) + read[position+INVERSION_LEN:]
				numC += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompTC.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a T and one to a C")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numC -= 1
				revCompTG = read[0:position] + revCompT[position:position+INVERSION_LEN].replace("N", "G", 1) + read[position+INVERSION_LEN:]
				numG += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompTG.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("One N was converted to a T and one to a G")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numG -= 1
				revCompTT = read[0:position] + revCompT[position:position+INVERSION_LEN].replace("N", "T", 1) + read[position+INVERSION_LEN:]
				numT += 1
				for element in sequencesDic.get((numA, numC, numG, numT, numN), []):
					if sequence[element:element+READ_LEN].strip("\n") == revCompTT.strip("\n"):
						print("The following contains a microinversion: " + read.strip("\n"))
						print("Two Ns were converted to Ts")
						print("The inversion length is " + str(INVERSION_LEN))
						print("It matches with the read that starts at position " + str(element))
						print("The microinversion occurs at character position " + str(position) + " in the read")
						print("It matches to: " + sequence[element:element+READ_LEN])
						return 0
				numT -= 2
				numN +=2
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



sequencesDic = pickle.load(open("sequencesDic.p", "rb"))
sequence = pickle.load(open("seqString.p", "rb"))
start = time.time()
for line in sys.stdin:
	line.strip("\n")
	startRead = time.time()
	findMicroInversions(line.upper())
	endRead = time.time()
	print("This read took " + str(endRead - startRead) + " seconds to process.")
end = time.time()
print("This program took " + str(end-start) + " seconds to run.")