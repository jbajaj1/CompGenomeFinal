#File that returns the time each inversion took
import sys

i = 0
for line in sys.stdin:
    if i == 5:
        line = line.split(" ")
        print line[3]
        i = 0
    else:
        i += 1
