#Dustin Watson
#CNA 438
#Spring 2018

import math
import re
from random import *
import string
from tkinter import *
from tkinter import messagebox

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Dynamic AVC Program")

        #Define all stringVars for use with the GUI:
        self.PTStr = StringVar()
        self.CTStr = StringVar()
        self.KeysStr = StringVar()
        self.KeywordStr = StringVar()
        self.OutputStr = StringVar()

        #Define all the GUI Elements:

        #Keyword entery and label
        self.Keyword_Label = Label(self.master, text="Keyword:")
        self.Keyword_Label.grid(row=0,column=0,pady=2,padx=2)
        
        self.Keyword = Entry(self.master, textvariable=self.KeywordStr)
        self.Keyword.insert(INSERT, "keyword")
        self.Keyword.grid(row=0,column=1,pady=2,padx=2)

        #Keys entery and label
        self.Keys_Label = Label(self.master, height=2, width=15, text="Key Values \n(common seperated)")
        self.Keys_Label.grid(row=1,column=0,pady=5,padx=5)

        self.Keys_Text = Entry(self.master, textvariable=self.KeysStr)
        self.Keys_Text.insert(INSERT, "5,7,11")
        self.Keys_Text.grid(row=1,column=1, pady=2,padx=2)

        self.outputlbl = Label(self.master, text="Output:")
        self.outputlbl.grid(row=9, column=0)

        self.outputbox = Entry(self.master, textvariable=self.OutputStr)
        self.outputbox.grid(row=9,column=1)
        
        self.PT_Label = Label(self.master, text="PlainText:")
        self.PT_Label.grid(row=4,column=0, pady=2,padx=2)
        
        self.PT = Entry(self.master, textvariable=self.PTStr)
        self.PT.insert(INSERT, "Text to Encode")
        self.PT.grid(row=4,column=1, pady=2,padx=2)
        
        self.CT_Label = Label(self.master, text="CipherText:")
        self.CT_Label.grid(row=5,column=0, pady=2,padx=2)
        
        self.CT = Entry(self.master, textvariable=self.CTStr)
        self.CT.grid(row=5,column=1, pady=2,padx=2)
        
        self.Encrypt_butt = Button(self.master, text="Encrypt", command=self.start_encrypt)
        self.Encrypt_butt.grid(row=4,column=2, pady=2,padx=2)
        
        self.Dencrypt_butt = Button(self.master, text="Decrypt", command=self.start_decrypt)
        self.Dencrypt_butt.grid(row=5,column=2, pady=2,padx=2)




    def start_encrypt(self):
        if self.PTStr.get() == "" or self.KeysStr.get() == "" or self.KeywordStr.get() == "":
            messagebox.showwarning("Warning", "Keyword, Keys and/or PlainText is blank. Correct this and try again")
            return
        else:
            #check for invalid char in the KeysTextBox
            Keys = self.KeysStr.get()
            KeysList = Keys.split(",")
            InvalidKeys = False
            for i in KeysList:
                if i.isdigit() == False:
                    InvalidKeys = True
            if InvalidKeys:
                messagebox.showwarning("Warning", "Keys have non-number values. Correct this and try again")
                return
            #Check for invalid chars in keyword and plainText Boxes
            if(invalidchars_exist(self.PTStr.get())):
                messagebox.showwarning("Warning", "Plain Text has invalid charactors. If one isn't visiable, check for spaces. Must be a-z 0-9 Correct this and try again")
                return
            if(invalidchars_exist(self.KeywordStr.get())):
               messagebox.showwarning("Warning", "Keyword has invalid charactors. If one isn't visiable, check for spaces. Must be a-z 0-9 Correct this and try again")
               return
            if(repeats_exist(self.KeywordStr.get())):
                messagebox.showwarning("Warning", "Keyword has duplicate charactors. Correct this and try again")
                return
            if(not check4reletivltyprime(KeysList)):
                return
            #Now all the checks for TypeSafe are done, compute the output
            #Enter Output code here:
            self.OutputStr = "" #clear out the output box
            self.OutputStr = avc(KeysList, self.PTStr.get(), self.KeywordStr.get())
            self.outputbox.delete(0,END)
            self.outputbox.insert(0, self.OutputStr)

            
    def start_decrypt(self):
        if self.CTStr.get() == "" or self.KeysStr.get() == "" or self.KeywordStr.get() == "":
            messagebox.showwarning("Warning", "Keyword, Keys and/or Cipher Text is blank. Correct this and try again")
            return
        else:
            #check for invalid char in the KeysTextBox
            Keys = self.KeysStr.get()
            KeysList = Keys.split(",")
            InvalidKeys = False
            for i in KeysList:
                if i.isdigit() == False:
                    InvalidKeys = True
            if InvalidKeys:
                messagebox.showwarning("Warning", "Keys have non-number values. Correct this and try again")
                return
            #Check for invalid chars in keyword and plainText Boxes
            if(invalidchars_exist(self.CTStr.get())):
                messagebox.showwarning("Warning", "Cipher Text has invalid charactors. If one isn't visiable, check for spaces. Must be a-z 0-9 Correct this and try again")
                return
            if(invalidchars_exist(self.KeywordStr.get())):
               messagebox.showwarning("Warning", "Keyword has invalid charactors. If one isn't visiable, check for spaces. Must be a-z 0-9 Correct this and try again")
               return
            if(repeats_exist(self.KeywordStr.get())):
                messagebox.showwarning("Warning", "Keyword has duplicate charactors. Correct this and try again")
                return
            if(not check4reletivltyprime(KeysList)):
                return
            #Now all the checks for TypeSafe are done, compute the output
            #Enter Output code here:
            self.OutputStr = "" #clear out the output box
            self.OutputStr = deavc(KeysList, self.CTStr.get(), self.KeywordStr.get())
            self.outputbox.delete(0,END)
            self.outputbox.insert(INSERT, self.OutputStr)
            
            
            



def xgcd(p,d):
    if p<d:
        p,d=d,p
    x0, x1, y0, y1 = 1, 0, 0, 1
    while d != 0:
        q, p, d = p // d, d, p % d
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  {"gcd":p, "p":p, "d":d, p:x0, d:y0}

def check4reletivltyprime(alpha):
    for value in alpha:
        gcdoutput = xgcd(int(value), 36)
        if gcdoutput["gcd"] != 1:
            messagebox.showwarning("Warning",str(value) + " is not realitivity prime to 36. Correct the key and try again")
            return False
    return True

def invalidchars_exist(stringvalue):
    stringvalue = stringvalue.lower()
    alphanum = string.ascii_lowercase + string.digits
    location = 0
    for char in stringvalue:
        location = alphanum.find(char)
        if location == -1:
            return True
    return False

def repeats_exist(stringvalue):
    stringvalue= stringvalue.lower()
    for i in range(0, len(stringvalue)-1):
        for j in stringvalue[i+1:len(stringvalue)]:
            if stringvalue[i] == j:
                return True
    return False

def mutplicative_inverse(modnumber, number):
    i=1
    while i:
        testvar = math.modf(((i * modnumber) + 1) / number)
        if testvar[0] == 0:
            break
        i+=1
    return int(testvar[1])
        

        
def avc(alpha, PT, keyword):
    keyword = keyword.lower()
    charset = string.ascii_lowercase + string.digits
    ##print(charset)
    i=0
    CT = list()
    PT = PT.lower()
    for char in PT:
        PTint = charset.index(char)
       # print("PTint:", PTint)
        keywordchar = keyword[(i % (len(keyword)))]
       # print("keywowrdchar", keywordchar)
        keywordint = charset.index(keywordchar)
        #print("keywordint", keywordint)
        #print("alpha",int(alpha[i % len(alpha)]))
        a = int(alpha[i % len(alpha)]) * int(PTint)
        z = (a + keywordint) % 36
##        print("final value:", z)
##        print(charset[z])
        CT.append(charset[z])
        i = i + 1
    stringCT = ""
    for char in CT:
        stringCT += char
    messagebox.showwarning("Output Value", stringCT)
    return stringCT

def deavc(alpha, CT, keyword):
    debug=False
    keyword = keyword.lower()
    charset = string.ascii_lowercase + string.digits
    i=0
    CT = CT.lower()
    PT = []
    for char in CT:
        CTint = charset.index(char)
        keywordchar = keyword[(i % (len(keyword)))]
        keywordint = charset.index(keywordchar)
        a = int(alpha[i % len(alpha)]) #* int(PTint)
        a_inverse = mutplicative_inverse(36, a)
        z = ((CTint - keywordint) * a_inverse) % 36 ##reverse the encryption
        PT.append(charset[z])
        i = i + 1
        if debug:
            print("CTint:", CTint)
            print("keywowrdchar", keywordchar)
            print("keywordint", keywordint)
            print("alpha",int(alpha[i % len(alpha)]))
            print("Co-prime", a_inverse)
            print("final value:", z)
            print(charset[z])

    stringCT = ""
    for char in PT:
        stringCT += char
    messagebox.showwarning("Output Value", stringCT)
    return stringCT
    

root = Tk()
root.geometry("350x220")
root.maxsize(width=350, height=220)
root.minsize(width=350, height=220)
app = Window(root)


root.mainloop()
