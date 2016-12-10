import fileinput
import sys
import os
import getopt

def fixNums():
	file = open("numbersUgly.txt", 'r')
	out = open("numbersClean.txt", 'w')

	for line in file:
		if line == "\n" or line == "":
			continue
		elif line[-2] == ".":
			line = line[0:-2] + line[-1]
			out.write(line)
		else:
			out.write(line)
	file.close()
	out.close()

fixNums()
