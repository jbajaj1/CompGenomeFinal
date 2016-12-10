import fileinput
import sys
import os
import getopt
import pickle

def thingie():
    i = 0
    seqString = ""
    for line in sys.stdin:
        if i == 0:
            i += 1
        else:
            seqString += line.strip("\n")
    
    chunk = seqString[55:95]
    print chunk, " NUMBER ONE!"

    chunk = seqString[71:111]
    print chunk, "NUMBER TWO!"

def main():
    thingie()

if __name__ == '__main__':
    main()
