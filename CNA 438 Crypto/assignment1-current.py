##Dustin Watson
##Programming Assignment 1
##XOR crypto

import math
import re
import string


def class_ascii_dec(inputstring):
    ##Class_Ascii_Dec
    ##Class as in the charset requiremeents for CNA438 class, not class in a programming structure
    ##Converts standard ASCII string with values of A-Z and 0-9 to
    ##A restricted set of 36 ordinal values. To be used in place of ORD(X)
    ##
    ##Input: inputstring as string
    ##
    ##Returns: List of modified Ords in Base 10 for each char.
    ##
    ##Error: returns a None instead of a list

    p = re.compile("[^a-zA-Z\d:]") ##find any chars not in the this class' restricted charset
    if p.match(inputstring): return None
    InputList = list(inputstring.lower())
    charset = string.ascii_lowercase + string.ascii_lowercase + string.digits
    ModifiedList = list()
    for i in inputstring:
        ModifiedList.append(charset.index(i))    
    return ModifiedList

def restricted_ascii(InputList):
    ##restricted_ascii
    ##Converts a list of mod 36 ords 
    ##A restricted set of 36 ordinal values. To be used in place of ORD(X)
    ##
    ##Takes lists of numbers following the classes 36 charset. Example: [2,0,19] for ['c', 'a', 't']
    ##
    ##Input: List of modifed Ords in base 10
    ##
    ##Returns: List of char from the 36 char set used in the CNA 438 class.
    ##
    ##Error: returns a None instead of a list
    ModifiedList = list()
    charset = string.ascii_lowercase + string.digits
    for val in InputList:
        ModifiedList.append(charset[val % 36])
    return ModifiedList


def class_ascii_bin(inputstring):
    ##Class_Ascii_Bin
    ##Class as in the charset requiremeents for CNA438 class, not class in a programming structure
    ##Converts standard ASCII string with values of A-Z and 0-9 to
    ##A restricted set of 36 ordinal values. To be used in place of ORD(X)
    ##
    ##Input: inputstring as string
    ##
    ##Returns: List of modified Ords in Base 2 for each char.
    ##
    ##Error: returns a None instead of a list

    p = re.compile("[^a-zA-Z\d:]") ##find any chars not in the this class' restricted charset
    if p.match(inputstring): return None
    InputList = class_ascii_dec(inputstring)
    ModifiedList = [bin(x) for x in InputList]
    return ModifiedList

def class_ascii_base(inputstring, base):
    ##Class_Ascii_Base
    ##Converts standard ASCII string with values of A-Z and 0-9 to
    ##A restricted set of 36 ordinal values. To be used in place of ORD(X)
    ##
    ##Input: inputstring as string
    ##
    ##Returns: List of modified Ords into a base given by base for each char.
    ##
    ##Error cased by invalid input: returns a None instead of a list

    p = re.compile("[^a-zA-Z\d:]") ##find any chars not in the this class' restricted charset
    if p.match(inputstring): return None
    InputList = class_ascii_dec(inputstring)
    ModifiedList = list()
    ##calc the needed number of digits to hold 36 charset based on the base param.
    wordsize = math.ceil(math.log(36)/math.log(base))
    tempstr = ""
    for m in InputList:
        while(m > 0):
            tempstr = str(m % base) + tempstr
            m = int(m / base)
        ##add padding to fill out the wordsize if needed
        if len(tempstr) < wordsize: tempstr = "0" * (wordsize - len(tempstr)) + tempstr
        ModifiedList.append(tempstr)
        tempstr = ""
    return ModifiedList

def xorCT(plantext, key, base):
    if base == 2:
        PT = class_ascii_bin(plantext)
        K = class_ascii_bin(key)
        PTList = list()
        KList = list()
        if len(PT) > len(K):
            KList = [0]*(len(PT) - len(K)) + KList
        else:
            PTList = [0]*(len(K) - len(PT)) + PTList
        PTList = PTList + PT
        KList = KList + K
        CTList = list()
        for i in range(len(PTList)):
            CTList.append(int(PTList[i], 2) ^ int(KList[i], 2))
        return CTList
    elif base == 3:
        PT = class_ascii_base(plantext, 3)
        K = class_ascii_base(plantext, 3)
        PTList = list()
        KList = list()
        CTList = list()
        ##pad the smaller left with 0's if they are not the same size
        if len(PT) > len(K):
            KList = [0]*(len(PT) - len(K)) + KList
        else:
            PTList = [0]*(len(K) - len(PT)) + PTList
        PTList = PTList + PT
        KList = KList + K
                    
        for i in range(len(PTList)):
            ##(PT + K) Mod 3:
            ##Should be correct, as GF(3) is = [0, 1, 2] mod 3
            ##I think its GF(3) = x + 1 is the polynomial funiction that discribes this field.
            ##I show that any combo set of any two values exists in the set, closed under
            ##adition.
            ##I show that any combo of multipciation exists in the set, closed under mupliciation.
            ##Since 0 is in the set, the set is not null.
            ##The set has all the proprities of a field and a vector space, which implies it has an inverse.
            ##Inverse is the desired resulting funcition that makes XOR for PT XOR K = CT work correctly in both directions
            ##for bit-wise XOR. We want to create a digit wise XOR in base 3, so this logic should apply.
            ##Please forgive me if this is not 100%, I've only had MATH312, and funicinal anaylisis and number theroy is a grad
            ##course at SCSU. This falls somewhere in Albin Groups/Ring Theroy/Field Theroy.

##            My failed attempt to impliment this lays here:
##            for j in range(len(PTList[i])):
##                aval = str(int(PTList[i][j]) + int(KList[i][j]) % 3)
##                print(int(aval))
##             #   print(int(str(int(PTList[i][j]) + int(KList[i][j])), 3))
##              #  intbit = (int(PTList[i][j]) + int(KList[i][j])) % 3
##            #CTList.append((int(PTList[i],3) + int(KList[i],3)) % 3)
##            CTList.append(intbit)
            
            #try to impl x + 1 mod 3:
            CTList.append(((int(PTList[i],3) + int(KList[i]))+1) % 3)

        return CTList
    elif base == 10:
        ##If I'm correct, and we are to do base 10 GF, this isn't correct.
        ##However, this math that is important but not stated as required for the course.
        ##Currently, its doing a bitwise XOR (base 2)
        ##Deconstruction of a GF(10) is something beyond my mastery.
        ##And when writing crypto, its best not to try do something you don't understand, or it will make it
        ##less secure. Best to use a tested library.
        PT = class_ascii_base(plantext, 10)
        K = class_ascii_base(key, 10)
        PTList = list()
        KList = list()
        if len(PT) > len(K):
            KList = [0]*(len(PT) - len(K)) + KList
        else:
            PTList = [0]*(len(K) - len(PT)) + PTList
        PTList = PTList + PT
        KList = KList + K
        CTList = list()
        for i in range(len(PTList)):
            CTList.append((int(PTList[i]) ^ int(KList[i])))
        return CTList
    else:
        return "Base not yet supported"

def restricted_ascii_str(Inputlist):
    s = "".join([c for c in Inputlist])
    return s
    


PT = "good"
K = "huge"

##print("base 10")
##print("PT: ", class_ascii_dec(PT))
##print("K: ", class_ascii_dec(K))
##print("CT: ", xorCT(PT, K, 10))
##print("CT as list of Chars: ", restricted_ascii(xorCT(PT, K, 10)))
##print("CT as a string: ", restricted_ascii_str(restricted_ascii(xorCT(PT, K, 10))))
##print("De-coded CT: ", xorCT(restricted_ascii_str(restricted_ascii(xorCT(PT, K, 10))), K, 10))
##print("")
##
##print("base 2")
##print("PT: ",class_ascii_bin(PT))
##print("K: ",class_ascii_bin(K))
##print("CT numbers: ", xorCT(PT, K, 2))
##print("CT as Chars: ", restricted_ascii(xorCT(PT, K, 2)))
##print("De-coded CT: ", xorCT(restricted_ascii_str(restricted_ascii(xorCT(PT, K, 2))), K, 2))
##print("")
##
##
##print("base 3")
##print("PT: ",class_ascii_base(PT, 3))
##print("K: ",class_ascii_base(K, 3))
##print("CT numbers: ", xorCT(PT, K, 3))
##print("CT as Chars: ", restricted_ascii(xorCT(PT, K, 3)))
##print("De-coded CT: ", xorCT(restricted_ascii_str(restricted_ascii(xorCT(PT, K, 3))), K, 3))
##print("")



CT = xorCT(PT, K, 10)
print("CT: ", CT)
dCT = restricted_ascii((xorCT(CT, K, 10)))
print("De-coded: ", dCT)
