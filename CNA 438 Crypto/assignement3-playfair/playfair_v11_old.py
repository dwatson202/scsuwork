##Dustin Watson
##CNA 438
##Playfair
##Heavy use of Typesafe checking

import math
import re
from random import *
import string

def pf_rules(offset, messagedict):
    if not isinstance(offset, int):
        print("Error (pf_rules): offset is not a Integer")
        return -1
        if not isinstance(messagedict,dict):
        print("Error (encrypt_pf): messagedict Input is not a Dict type")
        return -1
 

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

def playfair_message_blocks(message, table, removespaces=True):
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
    i=0
    while i < len(messagelist)-1:
        if messagelist[i] == messagelist[i+1]: ##Rule 2
            messagelist.insert(i+1, "x")
            i += 1
        i += 1
    if len(messagelist) % 2 != 0: #Rule 3:
        messagelist.append("x")
    #Rule 1:
    newmessagelist = [messagelist[i*2:(i*2)+2] for i in range(0,(len(messagelist)//2))]
    #decomp the list back into a string:
    newmessagestr = ""
    for char in messagelist:
        newmessagestr += char
    ##if table is set, then also output a table comp of the message
    ##using a list of pairs into tables index numbers matching the letters.
    if table is not None:
        tablecomp = []
        if not isinstance(table, list):
            print("Error (playfair_message_blocks): Table Input is not a List")
            return -4
        #convert each 2 char block into numbers from the table
        for block in newmessagelist:
            currentblocklist = []
            for letter in block:
                location = table.index(letter)
                currentblocklist.append(location)
            tablecomp.append(currentblocklist)
        return {"list": newmessagelist, "string": newmessagestr, "block_int":tablecomp}
    else:
        return {"list": newmessagelist, "string": newmessagestr}

def encrypt_pf(messagedict, playfair_table_list):
##    Rule 1:
##    If in the same Column:
##        Move each letter down one row (increase the row 1), wrap around is used.
##    Rule 2:
##    If in the same Row:
##        Move each letter right one colum (increase the colum 1), wrap around is used.
##    Rule 3:
##    If not rule 1 or 2, then swap the letter's columns
##
## Input messagedict as dict type
## Input play_table_list as list
    if not isinstance(messagedict,dict):
        print("Error (encrypt_pf): messagedict Input is not a Dict type")
        return -1
    if not isinstance(playfair_table_list,list):
        print("Error (encrypt_pf): playfair_table_list Input is not a list type")
        return -2 
    block_int = messagedict["block_int"]
    #create 6x6 table using duple values (x,y) to set the cols, rows.
    #retain the 2 blocks as well.
    table = [] #init the duple
    for block in block_int:
        temptable=[]
        for letter in block:
            temptable.append((letter%6,letter//6))
        table.append(temptable)
    newblocks = []
    newtable = []
    tempblock = []
    print("Apply rules for encrypting")
    for block in table:
        #Rule 1:
        if same_col(block[0], block[1]):
            tempblock = [increase_row(block[0],6), increase_row(block[1],6)]
            newtable.append(tempblock)
        ##Rule 2:
        if same_row(block[0], block[1]):
            tempblock = [increase_col(block[0],6), increase_col(block[1],6)]
            newtable.append(tempblock)
        ##Rule 3:
        if not same_row(block[0], block[1]) and not same_col(block[0], block[1]):
            tempblock = swap_cols(block[0], block[1])
            newtable.append(tempblock)
    #now convert the new duple values into letters on keyword table
    #playfair_table_list
    flattentablelist= []
    for block in newtable:
        for letter in block:
            flattentablelist.append((letter[1]*6)+letter[0]) #row * 6 + col (col is equvlent to remainder and row is the quoatent
    CToutputstring = ""
    for CTLetterInt in flattentablelist: #find them on the playfair table list to make an CT
        CToutputstring +=  playfair_table_list[CTLetterInt]
    return CToutputstring

def same_col(dup1, dup2):
    if dup1[0] == dup2[0]:
        return True
    else:
        return False

def same_row(dup1, dup2):
    if dup1[1] == dup2[1]:
        return True
    else:
        return False

def swap_cols(dup1, dup2):
    #print("Rule3")
    #function swaps the cols of 2 duple values
    #returns two dupl with their cols swapped as a list
    return [(dup2[0], dup1[1]), (dup1[0],dup2[1])]

def increase_row(dup1, x):
    print("Rule1 Encrypt")
    #Function increase the row of a dup by 1 with wraparound x
    #Returns: dup
    newdup = (dup1[0], (dup1[1] + 1) % x)
    return newdup

def increase_col(dup1, x):
    print("Rule2 Encrypt")
    #Function increase the row of a dup by 1 with wraparound x
    #Returns: dup
    newdup = ((dup1[0] + 1) % x, dup1[1])
    return newdup

def decrease_col(dup1, x):
    print("Rule2 Decrypt")
    #Function increase the row of a dup by 1 with wraparound x
    #Returns: dup
    newdup = ((dup1[0] - 1) % x, dup1[1])
    return newdup

def decrease_row(dup1, x):
    print("Rule1 Decrypt")
    #Function increase the row of a dup by 1 with wraparound x
    #Returns: dup
    newdup = (dup1[0], (dup1[1] - 1) % x)
    return newdup

def decrypt_pf(messagedict, playfair_table_list):
##    Rule 1:
##    If in the same Column:
##        Move each letter up one row (decrase row), wrap around is used.
##    Rule 2:
##    If in the same Row:
##        Move each letter left one col (decrase col), wrap around is used.
##    Rule 3:
##    If not rule 1 or 2, then swap the letter's columns
##
## Input messagedict as dict type
## Input play_table_list as list
    if not isinstance(messagedict,dict):
        print("Error (decrypt_pf): messagedict Input is not a Dict type")
        return -1
    if not isinstance(playfair_table_list,list):
        print("Error (decrypt_pf): playfair_table_list Input is not a list type")
        return -2 
    block_int = messagedict["block_int"]
    #create 6x6 table using duple values (x,y) to set the cols, rows.
    #retain the 2 blocks as well.
    table = [] #init the duple
    #create a visualization table, if I have the time, animate the letters moving
    vis_table = []
    for block in block_int:
        temptable=[]
        for letter in block:
            temptable.append((letter%6,letter//6))
            vis_table.append((letter%6,letter//6))
        table.append(temptable)
    newblocks = []
    newtable = []
    tempblock = []
    print("apply rules for decrypt")
    for block in table:
        #Rule 1:
        if same_col(block[0], block[1]):
            tempblock = [decrease_row(block[0],6), decrease_row(block[1],6)]
            newtable.append(tempblock)
        ##Rule 2:
        if same_row(block[0],block[1]):
            tempblock = [decrease_col(block[0],6), decrease_col(block[1],6)]
            newtable.append(tempblock)
        ##Rule 3:
        if not same_row(block[0], block[1]) and not same_col(block[0], block[1]):
            tempblock = swap_cols(block[0], block[1])
            newtable.append(tempblock)
    #now convert the new duple values into letters on keyword table
    #playfair_table_list
    flattentablelist= []
    for block in newtable:
        for letter in block:
            flattentablelist.append((letter[1]*6)+letter[0]) #row * 6 + col (col is equvlent to remainder and row is the quoatent
    CToutputstring = ""
    for CTLetterInt in flattentablelist: #find them on the playfair table list to make an CT
        CToutputstring +=  playfair_table_list[CTLetterInt]
    return CToutputstring
       
playfairlist = playfair_table("YREJSPOVCNWLG")

PT1="Superman never made any money\
Saving the world from Solomon Grundy \
And sometimes I despair \
The world will never see another man like him"

print("PT1:", PT1)     
messagedict = playfair_message_blocks(PT1,playfairlist)
CT = encrypt_pf(messagedict, playfairlist)

print("CT:", CT)

PT2 = decrypt_pf(playfair_message_blocks(CT,playfairlist), playfairlist)
print("PT:", PT2)

#TODO: Ban the use of entering more than one X
#Also, X and extra X's are a problem


