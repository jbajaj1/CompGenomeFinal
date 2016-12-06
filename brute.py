def preprocessSeq():
    i = 0
    seqString = ""
    numN = 0
    numA = 0
    numC = 0
    numG = 0
    numT = 0
    sequences = {}
    for line in sys.stdin:
        if i == 0:
            i += 1
        else:
            seqString += line.strip("\n")
        position = 0
    while position + 40 < len(seqString):
        chunk = seqString[position:position+40]
        for char in chunk:
            if char == 'N' or char == 'n':
                numN += 1
            elif char == 'A' or char == 'a':
                numA += 1
            elif char == 'C' or char == 'c':
                numC += 1
            elif char == 'G' or char == 'g':
                numG += 1
            elif char == 'T' or char == 't':
                numT += 1
        if (numA, numC, numG, numT, numN) in sequences:
            sequences[(numA, numC, numG, numT, numN)].append(position)
        else:
            sequences[(numA, numC, numG, numT, numN)] = [position]
        numA = 0
        numC = 0
        numG = 0
        numT = 0
        numN = 0
        position += 1
    return sequences


def revComp(s):
    res = ''
    convert = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    for i in range(0, len(s)):
        res += convert[s[i]]
    return res.reverse()
t = 'ACTGACTGACTGACTGACTG'
seqs = preprocessSeq('ACTGACTGACTGACTGACTG')
p = 'AAGG'
pp = revComp(p)
indices = seqs[(2, 0, 2, 0, 0)]
found = False
for i in indices:
    if p == t[i:i+4]:
        found = True

if found:
    print ('Regular match')
indices = seqs[(0,2,0,2,0)]
revFound = False
for i in indices:
    if pp == t[i:i+4]:
        revFound = True
if revFound:
    print ('Complement match')
