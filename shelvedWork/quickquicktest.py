
def stringlen():
    x = 100
    str = ""
    while x > 0:
        str += "b"
        x -= 1
    print len(str)
    print len(str[0:40])
    print len(str[0:39])

stringlen()
