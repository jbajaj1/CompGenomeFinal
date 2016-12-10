# CompGenomeFinal

Contributors:
Oneeb Malik - omalik2
Dan Smillie
John Wilson - 
Joshan Bajaj - jbajaj1

'preprocessSeq.py' is used to preprocess a genome sequence into a dictionary.
It then saves this dictionary to a 'sequencesDic.p' pickle file

'findMicroInversions.py' is the file that actually detect micro inversions
using the dictionary. It takes in a read, and then outputs information
if a match in the genome sequence is found. 

'generateSeq.py' is used to generate a long, random sequence of nucleotide
letters for testing purposes. 

'inversionGenerator.py' can be used to generate reads to check against a
reference genome. It currently generates reads with microinversions present,
If you uncomment the last line in the program (print(read)), then the program
will just generate a normal read.


There is a folder called 'alternate methods' in our submission. This contains
'parallelInversions.py' and 'ineffBrute.py' which are two different methods
we tried to implement but did not work effectively in practice. Either can
replace the 'findMicroInversions.py' file and will run, although ineffBrute.py
is ineffective and parallelInversions.py is inaccurate. 'The inEffPreprocess.py'
file can replace the 'preProcessSeq.py' but it wasn't effective so we scrapped
it.

'run.sh' is a bash script file that automatically runs all steps for you. The 
source genome sequence file can be changed by changing the file, but below we
describe how to run our program step by step without the bash script:

1) Run 'python preprocessSeq.py < input .fa file'
2) Run 'python findMicroInversions.py < input reads file'

To generate a random sequence of nucleotides, use 'python generateSeq.py > 
stdout to file of your choice'

To generate a random set of micro inverted reads, use 'python inversionGenerator
< input .fa file > stdout to file of choice'.
