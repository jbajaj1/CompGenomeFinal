import time
from random import randint

SEQUENCE_SIZE = 500000

def generateSeq():
	seq = ">Randomly Generated Sequence\n"
	choices = ["A", "C", "G", "T"]
	i = 0
	while i < SEQUENCE_SIZE:
		seq += choices[randint(0,3)]
		i += 1
	return seq
start = time.time()
print(generateSeq())
print(str(time.time() - start) + " seconds to generate sequence of size " + str(SEQUENCE_SIZE))