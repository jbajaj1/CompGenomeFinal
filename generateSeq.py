import time
from random import randint

SEQUENCE_SIZE = 30000

def generateSeq():
	seq = ">Randomly Generated Sequence\n"
	choices = ""
	choices += "AGTC" * 100
	choices += "N"
	i = 0
	while i < SEQUENCE_SIZE:
		seq += choices[randint(0,len(choices)-1)]
		i += 1
	return seq
start = time.time()
print(generateSeq())
#print(str(time.time() - start) + " seconds to generate sequence of size " + str(SEQUENCE_SIZE))
