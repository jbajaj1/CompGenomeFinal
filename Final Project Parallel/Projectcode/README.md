# Parallel Final Project
# Spring Semester
Contributors: 
Joshan Bajaj - jbajaj1

'generateSeq.py' is used to generate a random sequence of nucleotide
letters for testing purposes. 

'preprocessSeq.py' is used to preprocess a genome sequence into a dictionary.
It then saves this dictionary to a 'sequencesDic.p' pickle file and a string 
to 'seqString.p'

'inversionGenerator.py' can be used to generate reads to check against a
reference genome. It currently generates reads with microinversions present.
If you uncomment the last line in the program (print(read)), then the program
will just generate a normal read.

'findMicroInversions.py' is the serial version of the program that
detects micro inversions using the dictionary. It takes in a read, and then 
outputs information if a match in the genome sequence is found. 

'findMicroInversionsOriginal.py' is the original serial version of this
program. The difference between the two serial versions is that in this
vesion, the character density is recalculated from scratch every iteration
of the position loop.

'findMicroInversionsCompareMultiProcGrouped.py' is the the parallel version
of the code which checks the number of string compares the program will need
to do at a given inversion length and position and then divides them up into
n groups, where n is the number of processes specified. This version of the
code is very slow because of the start up costs associated with creating so
many processes so often.

'findMicroInversionsCompareMultiProc.py' is similar to 
findMicroInversionsCompareMultiProcGrouped.py except the comparisons are not
grouped before sending them to the processes. Instead, multiprocessing.Map 
handles it. This version of the code is very slow because of the start up 
costs associated with creating so many processes so often. 

'findMicroInversionsReadsMultiProc.py' is the parallel version of the code
which sends each read to its own process (with a maximum being the number of
processes specified). This is the fastest version of the code, but it is not
ideal since it does not speed up individual inversions.

'findMicroInversionsReadsMultiProcGrouped.py' is similar to
findMicroInversionsReadsMultiProc.py expect the reads are grouped together
before sending them to the processes. This method does not work as fast as
its non-grouped version.

'findMicroInversionsLengthMultiProc.py' is the parallel version of the code 
which speeds up an individual read's inversion finding time by handling every
inversion length in its own process (with a maximum of n inversion lengths 
being handled at a time, where n = number of processes specified). This version
of the code is the fastest one on a per read basis. 

'findMicroInversionsInverseLengthMultiProc.py' is similar to 
findMicroInversionsLengthMultiProc.py but it goes about the inversions from 
smallest inversion length to largest inversion length instead of the other way
around. This causes it to work much slower than its non inverse version on 
large inversion sizes.

'timeAvg.py' returns the average time per read for an output file.

'timeForInv.py' returns the time each read in an output file took.

'getInvLen.py' returns the inversion length for each read in an output file.

'extractReads.py' returns the reads an output file used to create itself.

'PastMethod/parallelInversions.py' is the parallel version of the code that 
was written for the original project. It did not work because of raze 
conditions, so it was scrapped.

'ParallelData/' contains all of the data collected for this project.

‘../Graphs/’ contains the graphs for this project.

‘../Final Presentation Genome2016.ppt’ is the presentation from the original project.

‘../ProjectWriteUp.pdf’ is the writeup for this project.

Here is a step by step process to run this project:

1) Run 'python generateSeq.py > sequence.fa'

2) Run 'python inversionGenerator.py < sequence.fa > reads.txt

3) Run 'python preprocessSeq.py < sequence.fa'

4) Run 'python findMicroInversions*.py < sequence.fa > output.txt


This project was originally made for Computational Genomics in Fall 2016
with Oneeb Malik, Dan Smillie, and John Wilson.