##Dustin Watson
##CNA 438
##Playfair
##Heavy use of Typesafe checking

import math
import re
from random import *
import string



def invalidchars_exist(stringvalue):
    if not isinstance(stringvalue, str):
        print("Error (invalidchars_exist): Input is not a string")
        return -1
    stringvalue = stringvalue.lower()
    alphanum = string.ascii_lowercase + string.digits
    location = 0
    for char in stringvalue:
        location = alphanum.find(char)
        if location == -1:
            return True
    return False

def repeats_exist(stringvalue):
    if not isinstance(stringvalue, str):
        print("Error (repeats_exist): Input is not a string")
        return -1
    stringvalue= stringvalue.lower()
    for i in range(0, len(stringvalue)-1):
        for j in stringvalue[i+1:len(stringvalue)]:
            if stringvalue[i] == j:
                return True
    return False

def playfair_table(keyword):
    if not isinstance(keyword, str):
        print("Error (playfair_table): Input is not a string")
        return -3
    #check keyword for invalid charactors
    if invalidchars_exist(keyword):
        print("Error (playfair_table): invalid Chars in PT")
        return -2
    #check for repeats in keyword
    if repeats_exist(keyword):
        print("Error (playfair_table): Repeats exist")
        return -1
    #keyword is string
    keyword = keyword.lower()
    charset = string.ascii_lowercase + string.digits
    #create a keyword list
    completedkeyword = list()
    remainingcharset = list(charset)
    for char in keyword:
        completedkeyword = completedkeyword + [remainingcharset.pop(remainingcharset.index(char))]
    completedkeyword = completedkeyword + remainingcharset #add all the reset of the 36 alphadigit to the keyword
    return completedkeyword

def playfair_message_blocks(message, table=None, removespaces=True):
    #Rules of PF
    #1. Must be split into PAIRS
    #2. Seperate all duplicated leters by inserting letter X
    #3. If there is an odd letter at the end of message, insert X
    #4. ignore all spaces
    ##Rule 1:
    #check if message is a string
    if not isinstance(message, str):
        print("Error (playfair_message_blocks): Input is not a string")
        return -1
    #check keyword for invalid charactors
    message = message.lower()
    if removespaces is True:
        message = message.replace(" ","") #Rule 4
    elif invalidchars_exist(message):
        print("Error (playfair_message_blocks): invalid Chars in message")
        return -2
    messagelist = [x for x in message]
    print(messagelist)
    i=0
    while i < len(messagelist)-1:
        if messagelist[i] == messagelist[i+1]: ##Rule 2
            messagelist.insert(i+1, "x")
            i += 1
        print(messagelist[i:i+2])
        i += 1
    if len(messagelist) % 2 != 0: #Rule 3:
        messagelist.append("x")
    print((len(messagelist)//2)-1)
    #Rule 1:
    print("Debug range:", len(messagelist)-1)
    newmessagelist = [messagelist[i*2:(i*2)+2] for i in range(0,(len(messagelist)//2))]
    #decomp the list back into a string:
    newmessagestr = ""
    for char in messagelist:
        newmessagestr += char
    print(newmessagestr)
    ##if table is set, then also output a table comp of the message
    ##using a list of pairs into tables index numbers matching the letters.
    if table is not None:
        tablecomp = []
        if not isinstance(table, list):
            print("Error (playfair_message_blocks): Table Input is not a List")
            return -4
        #convert each 2 char block into numbers from the table
        print(table)
        for block in newmessagelist:
            currentblocklist = []
            for letter in block:
                location = table.index(letter)
                currentblocklist.append(location)
            tablecomp.append(currentblocklist)
        return {"list": newmessagelist, "string": newmessagestr, "table":tablecomp}
    else:
        return {"list": newmessagelist, "string": newmessagestr}


messagedict = playfair_message_blocks("SECRET MESSAGE",playfair_table("KEYWORD"))
print(messagedict)


#todo:
#Make sure the keyword has numbers as well as letters, otherwise X and z gives away too much infomration
