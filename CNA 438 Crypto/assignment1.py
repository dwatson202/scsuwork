##Dustin Watson
##Programming Assignment 1
##XOR crypto

import math

def class_ascii_dec(inputstring):
    listPT = list(inputstring.lower())
    modPT = list()
    for val in listPT:
        #print(val)
        if val.isalpha():
            modPT.append(ord(val) - 97)
        elif val.isdigit():
            modPT.append(ord(val) - 48)
    return modPT

def class_ascii_bin(inputstring):
    listPT = class_ascii_dec(inputstring)
    modPT = [bin(x) for x in listPT]
    return modPT

def class_ascii_anybase(inputstring, base):
    listPT = class_ascii_dec(inputstring)
    modPT = list()
    ##calc the needed number of digits to hold 36 char set used in the this class
    wordsize = math.ceil(math.log(36)/math.log(base))
    tempstr = ""
    for m in listPT:
        while(m > 0):
            tempstr = str(m % base) + tempstr
            m = int(m / base)
        ##add padding to fill out the wordsize if needed
        ##if len(tempstr) < wordsize: tempstr = "0" * (wordsize - len(tempstr)) + tempstr
        modPT.append(tempstr)
        tempstr = ""
    return modPT

def xorCT(plantext, key, base):
    # ^ char is bitwise XOR
    PT = class_ascii_anybase(plantext, base)
    K = class_ascii_anybase(key, base)
    PTstr = ""
    Kstr = ""
    for val in PT:
        PTstr += str(val)
    for val in K:
        Kstr += str(val)
##    print(PTstr)
##    print(Kstr)
##    return (PTstr ^ Kstr) //this doesn't work because it returns the wrong type of numbers


PT = "good"
K = "huge"

print("base 10")
print(class_ascii_dec(PT))
print(class_ascii_dec(K))
print("CT: ", xorCT(PT, K, 10))
print("")

print("base 2")
print(class_ascii_dec(PT))
print(class_ascii_dec(K))
print(xorCT(PT, K, 2))
print("")

print("base 3")
print(class_ascii_dec(PT))
print(class_ascii_dec(K))
print(xorCT(PT, K, 3))
print("")
