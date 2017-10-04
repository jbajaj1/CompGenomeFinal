#File that returns the time each inversion took
import sys

i = 0
sumTime = 0
el = 0
for line in sys.stdin:
    if i == 5:
        line = line.split(" ")
        sumTime += float(line[3])
        i = 0
        el += 1
    else:
        i += 1

print(sumTime/el)
