#!/bin/bash

python preprocessSeq.py < phix.fa
python inversionGenerator.py < phix.fa > reads.txt
python bruteJoshan.py < reads.txt
