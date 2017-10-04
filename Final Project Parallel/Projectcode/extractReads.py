#Extracts the reads used in an output file

import sys
i = 0
for line in sys.stdin:
    if i == 0:
        line = line.split(": ")
        if len(line) == 2:
            print line[1].strip('\n')
        i += 1
    else:
        i += 1
        if i == 6:
            i = 0
