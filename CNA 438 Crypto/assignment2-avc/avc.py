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

        Keyword_Label = Label(self.master, text="Keyword:")
        Keyword_Label.pack()
        Keyword = Text(self.master, height=1, width=15)
        Keyword.pack()
        
        Add_Alpha_Keys_Label = Label(self.master, text="Current Alpha Values:")
        Add_Alpha_Keys_Label.pack()
        Add_Alpha_Keys = Button(self, text="Add Keys to Alpha Values")
        Add_Alpha_Keys.pack()
        Add_Alpha_Keys_Text = Text(self.master, height=1, width=15)
        Add_Alpha_Keys_Text.pack()

        alphakeys = Listbox(self.master, height=5)
        alphakeys.pack()

        #list of Alpha Keys
        PT_Label = Label(self.master, text="PlanText:")
        PT_Label.pack()
        PT = Text(self.master, height=1, width=15)
        PT.pack()
        CT_Label = Label(self.master, text="CipherText:")
        CT_Label.pack()
        CT = Text(self.master, height=1, width=15)
        CT.pack()
        Encrypt_butt = Button(self, text="Encrypt")
        Encrypt_butt.pack()
        Dencrypt_butt = Button(self, text="Dencrypt")
        Dencrypt_butt.pack()
##        List1 = Listbox(self.master, height=5).pack()
##        List1.insert(1,"Alpha List")
##        List1.pack()
##        List2 = Listbox(self.master)
##        List2.insert(1,"Beta List")
##        List2.pack()
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)



        # creating a button instance
        #quitButton = Button(self, text="Quit",command=self.client_exit)

        # placing the button on my window
        #quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()


def xgcd(p,d):
    if p<d:
        p,d=d,p
    x0, x1, y0, y1 = 1, 0, 0, 1
    while d != 0:
        q, p, d = p // d, d, p % d
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  p, x0, y0

def check4reletivltyprime(alpha):
    for value in alpha:
        gcdoutput = xgcd(value, 36)
        if gcdoutput[0] != 1:
            messagebox.showwarning("Warning",str(value) + " is not realitivity prime to 36")
            return False
    return True

def avc(alpha, PT, keyword):
    keyword = keyword.lower()
    charset = string.ascii_lowercase + string.digits
    print(charset)
    i=0
    CTint = list()
    PT = PT.lower()
    for char in PT:
        PTint = charset.index(char)
        keywordchar = keyword[(i % (len(keyword)))]
        keywordint = charset.index(keywordchar)
        CTint.append((((alpha[i % len(alpha)]) * (PTint)) + keywordint) % 36)
        i = i + 1
    stringCT = ""
    for digit in CTint:
        stringCT = stringCT+charset[digit]
    return stringCT

def deavc(alpha, CT, keyword):
    keyword = keyword.lower()
    charset = string.ascii_lowercase + string.digits
    print(charset)
    i=0
    PTint = list()
    PT = CT.lower()
    for char in CT:
        CTint = charset.index(char)
        keywordchar = keyword[(i % (len(keyword)))]
        keywordint = charset.index(keywordchar)
        PTint.append((((alpha) * (CTint)) - keywordint) % 36)
        i = i + 1
    stringCT = ""
    for digit in PTint:
        stringPT = stringPT + charset[digit]
    return stringPT
    

#print(avc(5, "BAD", "GOT"))
print()
print(xgcd(7,4))

root = Tk()
root.geometry("300x400")
app = Window(root)


alist = [1,4,5,2]
check4reletivltyprime(alist)

root.mainloop()
