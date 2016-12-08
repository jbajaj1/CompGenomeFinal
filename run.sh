#!/bin/bash
python generateSeq.py > seq.txt
python preprocessSeq.py < seq.txt
python inversionGenerator.py < seq.txt > reads.txt
python bruteJoshan.py < reads.txt
