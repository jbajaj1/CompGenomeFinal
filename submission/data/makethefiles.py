import fileinput
import sys
import os
import getopt

def organizenums():
	file = open("100ktricky.output", "r")
	output1 = open("graph1.txt", "w")
	output2 = open("graph2.txt", "w")
	i = 0
	for line in file:
		if i == 0:
			output1.write(line)
			i = 1
		elif i == 1:
			output2.write(line)
			i = 0
organizenums()