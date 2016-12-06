import fileinput
import sys
import os
import getopt
import pickle

def returnDic():
    ourDic = pickle.load(open("sequencesDic.p", "rb"))
    print(ourDic)

returnDic()
