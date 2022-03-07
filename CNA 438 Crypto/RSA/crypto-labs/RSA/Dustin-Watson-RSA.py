#Dustin Watson
#CNA 438
#RSA Impl

from tkinter import *
from tkinter import messagebox
import string
import random
import math

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("RSA")
        
        self.plabel = Label(self.master, text="First Prime (p):")
        self.plabel.grid(row=0, column=0)
        
        self.pbox = Entry(self.master)
        self.pbox.grid(row=0,column=1)
        
        #self.inlinedbuglabel = Label(self.master, text="Current Actions:")
        #self.inlinedbuglabel.grid(row=0,column=2)
        
        #self.inlinedebugtextbox = Text(self.master, height=10, width=30)
        #self.inlinedebugtextbox.grid(row=1,column=2, rowspan=3)
       
        self.qlabel = Label(self.master, text="Second Prime (q):")
        self.qlabel.grid(row=1,column=0)
        
        self.qbox = Entry(self.master)
        self.qbox.grid(row=1,column=1)

        self.sharedmodlabel = Label(self.master, text="Shared Modulus:")
        self.sharedmodlabel.grid(row=2, column=0)
        
        self.sharedmod = Entry(self.master, state='disabled')
        self.sharedmod.grid(row=2, column=1)

        self.publiclabel = Label(self.master, text="Public Key:")
        self.publiclabel.grid(row=3, column=0)
        
        self.publickey = Entry(self.master, state='disabled')
        self.publickey.grid(row=3, column=1)
        
        self.privatekeyLabel = Label(self.master, text="Private Key:")
        self.privatekeyLabel.grid(row=4, column=0)
        
        self.privatekey = Entry(self.master, state='disabled')
        self.privatekey.grid(row=4,column=1)
        
        
        self.inputlabel = Label(self.master, text="Input PT:")
        self.inputlabel.grid(row=5,column=0)
            
        self.inputmessage = Entry(self.master)
        self.inputmessage.grid(row=5,column=1)
        
        self.outputlabel = Label(self.master, text="Output:")
        self.outputlabel.grid(row=6, column=0)
        
        self.outputmessage = Entry(self.master)
        self.outputmessage.grid(row=6,column=1)
        
        self.ActionButton = Button(self.master, text="Encrypt/Decrept", command=self.startaction)
        self.ActionButton.grid(row=7,column=1)
        
        self.genkeys = Button(self.master, text="generate key pair", command=self.findkeys)
        self.genkeys.grid(row=2, column=3)
        
        self.customkeys = Button(self.master, text="Enable Public/Private key feilds", command=self.Enable_custom_keys)
        self.customkeys.grid(row=3, column=3)
        
    
    def Enable_custom_keys(self):
        self.publickey.configure(state="normal")
        self.privatekey.configure(state="normal")
    
    
    def findkeys(self):
        if self.qbox.get() == "":
            messagebox.showinfo("Information", "Q value is blank, please enter and try again")
            return
        if self.pbox.get() == "":
            messagebox.showinfo("Information", "P value is blank, please enter and try again")
            return
        if self.pbox.get() == self.qbox.get() and self.pbox.get() != "":
            messagebox.showerror("Error", "P and Q values must be different, please enter and try again")
            return
        #validate the entry boxes for valid input types
        validatedq = self.validatechars(self.qbox.get())
        validatedp = self.validatechars(self.pbox.get())
        qstr = validatedq[1]
        pstr = validatedp[1]
        if not validatedp[0]:
            messagebox.showwarning("Warning","Invalid input in P: " + ", ".join(pstr))
            return
        if not validatedq[0]:
            messagebox.showwarning("Warning","Invalid input in Q: "+ ", ".join(qstr))
            return
        
        q = int("".join(qstr))
        p = int("".join(pstr))
        
        #check if p and q are prime        
        if not fastfermatstest(q):
            messagebox.showwarning("Warning","The number entered for q: " + str(q) + ", is not a prime")
            return
        if not fastfermatstest(p):
            messagebox.showwarning("Warning","The number entered for p: " + str(p) + ", is not a prime")
            return


        e,d = self.key_pair(p,q)
        print("Key pair found: ", e, d)
        
        self.sharedmod.configure(state="normal")
        self.sharedmod.delete(0, END)
        self.sharedmod.insert(0, str((p-1)*(q-1)))
        self.sharedmod.configure(state="disabled")
        
        self.publickey.configure(state="normal")
        self.publickey.delete(0, END)
        self.publickey.insert(0, str(e))
        self.publickey.configure(state="disabled")
        
        self.privatekey.configure(state="normal")
        self.privatekey.delete(0, END)
        self.privatekey.insert(0, str(d))
        self.privatekey.configure(state="disabled")        
        
        
        
    def startaction(self):
        if self.pbox.get() == self.qbox.get() and self.pbox.get() != "":
            messagebox.showerror("Error", "P and Q values must be different, please enter and try again")
            return
        
        if self.qbox.get() == "":
            messagebox.showinfo("Information", "Q value is blank, please enter and try again")
            return
        if self.pbox.get() == "":
            messagebox.showinfo("Information", "P value is blank, please enter and try again")
            return
        validdigits = string.digits
        #validate the entry boxes for valid input types
        validatedq = self.validatechars(self.qbox.get())
        validatedp = self.validatechars(self.pbox.get())
        qstr = validatedq[1]
        pstr = validatedp[1]
        if not validatedp[0]:
            messagebox.showwarning("Warning","Invalid input in P: " + ", ".join(pstr))
            return
        if not validatedq[0]:
            messagebox.showwarning("Warning","Invalid input in Q: "+ ", ".join(qstr))
            return
        
        q = int("".join(qstr))
        p = int("".join(pstr))
        n = (p-1) * (q-1)
        
        #check if p and q are prime        
        if not fastfermatstest(q):
            messagebox.showwarning("Warning","The number entered for q: " + str(q) + ", is not a prime")
            return
        if not fastfermatstest(p):
            messagebox.showwarning("Warning","The number entered for p: " + str(p) + ", is not a prime")
            return
        
        self.sharedmod.configure(state="normal")
        self.sharedmod.delete(0, END)
        self.sharedmod.insert(0, str((p-1)*(q-1)))
        self.sharedmod.configure(state="disabled")
        
        #verify custom input for public and private keys
        validatedpublic = self.validatechars(self.publickey.get())
        validatedprivate = self.validatechars(self.privatekey.get())
        publicstr = validatedpublic[1]
        privatestr = validatedprivate[1]
        if not publicstr[0]:
            messagebox.showwarning("Warning","Invalid input in Public Key: " + ", ".join(publicstr))
            return
        if not privatestr[0]:
            messagebox.showwarning("Warning","Invalid input in Private Key: "+ ", ".join(privatestr))
            return
        e = int("".join(publicstr))
        d = int("".join(privatestr))
        
        inverse = modinverse(n, e)
        print(inverse)
        if (e * (gcd[2] % n)) % n != 1:
            messagebox.showwarning("Warning","Invalid input Key pair, please enter numbers where Public is releitivty prime to (p-1)*(q-1) and the private key is the public keys inverse in mod (p-1)*(q-1); Or press genrate key pair")
            return
        message = self.inputmessage.get()
        messageasint = string2int(message)
        
        #encrypt message
        ct = FastModExp(messageasint, e, n)
        self.outputmessage.delete(0, END)
        print("Cipher Text as an int:", ct)
        self.outputmessage.insert(0, int2string(ct))

        
        
    def validatechars(self, inputstring):
        #returns inputstring if all are validate charactors
        #returns a list of invalid charactors if any exist
        print(inputstring)
        validset = string.digits
        badchars = [x for x in inputstring if (x not in validset)]
        if len(badchars) > 0:
            return (False, badchars)
        else:
            return (True, inputstring)        
        
    def key_pair(self, p, q):
        #assumes p and q are primes
        #returns e and d, public, private keys
        n = (p-1) * (q-1)
        print(n)
        while True:
            e = random.randint(3,n)
            gcd = xgcd(n, e)
            print(e, fastfermatstest(e), gcd)
            if fastfermatstest(e) and gcd[0] == 1 and gcd[2] % n != e:
                #We don't want a e which is its own inverse in mod n, otherwise give the private key away
                break
        return e, gcd[2] % n
    
def string2int(inputstr):
    #converts a string into binary cancatnation as one number in base 2 and return in dec
    catcatnation = "".join([format(ord(x), '08b') for x in inputstr])
    print(catcatnation)
    return int(catcatnation,2)
    
def int2string(anumber):
    newbitstring = bin(anumber)[2::]
    while len(newbitstring) % 8 != 0:
        newbitstring = "0" + newbitstring
    charlisting = [chr(int(x,2)) for x in [newbitstring[y-8:y] for y in range(8, len(newbitstring)+8,8)]]
    final = "".join(charlisting)
    return final
        




def phi(n):
    #gives a truple of number of primes and the primes of the group ord n
    if fastfermatstest(n):
        ##if its a prime, return n-1, thats the number of digits releitivty prime to n
        return n-1, [x for x in range(1, n)]
    else:
        factors = []
        count = 0
        for i in range(n):
            xgcdvalue = xgcd(n, i)
            if xgcdvalue[0] == 1:
                count += 1
                factors.append(i)
        return count, factors
        

def coprime(m,n):
    #tests if twp numbers are coprime (reletiivty prime)
    if modinverse(m,n) != 0:
        return False
    else:
        return True


def fermatstest(n):
    #Work Cited
    #Based of Algo printed in Handbook of Applied Cryptography by Alfred J Menezes, Paul C Van Oorschot, and Scott A Vanstone CRC Press
    #Page 136
    security = 20 #scale the chance of being composite to the square of its size. Checks for a base in exponentation of fermat's little therom.
    if n == 2:
        return True
    elif n < 2:
        return False
    for i in range(security):
        a = random.randint(2, n-1)
        #finds a number a such that it is coprime to n and not a product of n
        gcd = xgcd(a,n)
        while gcd[0] != 1 and a % n == 0:
            print(gcd[0])
            a = random.randint(2, n-1)
            gcd = xgcd(a,n)
        
        #print(a,(n-1), n)
        #print(FastModExp(a, (n-1), n))
        if FastModExp(a, (n-1), n) != 1:
            return False
    return True

def xgcd(p,d):
    q = abs(p)
    r = abs(d)
    x0, x1, y0, y1 = 1, 0, 0, 1
    while r:
        p, (q, r) = r, divmod(p, r)
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  (int(p), int(x0) *(-1 if p < 0 else 1), int(y0) * (-1 if d < 0 else 1))

def modinverse(n, m):
    gcd, x, y = xgcd(n,m)
    if gcd == 1:
        return x % m
    return "composite"

    
def FastModExp(a, e, n):
    #Work Cited
    #page 153 Applied Crypto Alfred J Menezes, Paul C van Oorschor, Scott A Vanstone CRC Press
    #and
    #The Mathematics of Encryption Cozzens page 191
    #Algo in psudocode
    b = 1 #set a var to compute the remainder laterhttps://linsedition.files.wordpress.com/2017/11/war-and-peas-lucky-penny.jpg
    if e == 0:
        return b
    k = list(map(int, str(bin(e)[2:]))) # convert the exponent to binary and store it in a list
    k.reverse()
    A = a
    if k[0] == 1:
        b = a
    for i in range(1, len(k)):
        A = (A ** 2) % n
        if k[i] == 1:
            b = (A * b) % n
    return b


    
def primefactor(n):
    #Work Cited: Source of primes: http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283]
    factors = []
    for p in primes:
        q,r = divmod(n, p)
        if r == 0:
            factors.append(p)
    return factors

def trial_division(n):
    #This is sudo trial division
    #first 207+ primes
    #Work Cited: Source of primes: http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571,3581,3583,3593,3607,3613,3617,3623,3631,3637,3643,3659,3671,3673,3677,3691,3697,3701,3709,3719,3727,3733,3739,3761,3767,3769,3779,3793,3797,3803,3821,3823,3833,3847,3851,3853,3863,3877,3881,3889,3907,3911,3917,3919,3923,3929,3931,3943,3947,3967,3989,4001,4003,4007,4013,4019,4021,4027,4049,4051,4057,4073,4079,4091,4093,4099,4111,4127,4129,4133,4139,4153,4157,4159,4177,4201,4211,4217,4219,4229,4231,4241,4243,4253,4259,4261,4271,4273,4283,4289,4297,4327,4337,4339,4349,4357,4363,4373,4391,4397,4409,4421,4423,4441,4447,4451,4457,4463,4481,4483,4493,4507,4513,4517,4519,4523,4547,4549,4561,4567,4583,4591,4597,4603,4621,4637,4639,4643,4649,4651,4657,4663,4673,4679,4691,4703,4721,4723,4729,4733,4751,4759,4783,4787,4789,4793,4799,4801,4813,4817,4831,4861,4871,4877,4889,4903,4909,4919,4931,4933,4937,4943,4951,4957,4967,4969,4973,4987,4993,4999,5003,5009,5011,5021,5023,5039,5051,5059,5077,5081,5087,5099,5101,5107,5113,5119,5147,5153,5167,5171,5179,5189,5197,5209,5227,5231,5233,5237,5261,5273,5279,5281,5297,5303,5309,5323,5333,5347,5351,5381,5387,5393,5399,5407,5413,5417,5419,5431,5437,5441,5443,5449,5471,5477,5479,5483,5501,5503,5507,5519,5521,5527,5531,5557,5563,5569,5573,5581,5591,5623,5639,5641,5647,5651,5653,5657,5659,5669,5683,5689,5693,5701,5711,5717,5737,5741,5743,5749,5779,5783,5791,5801,5807,5813,5821,5827,5839,5843,5849,5851,5857,5861,5867,5869,5879,5881,5897,5903,5923,5927,5939,5953,5981,5987,6007,6011,6029,6037,6043,6047,6053,6067,6073,6079,6089,6091,6101,6113,6121,6131,6133,6143,6151,6163,6173,6197,6199,6203]
    for i in range(0, int(n**.5)):
        if n % primes[i] == 0:
            return False
    return True

def fermatstest(n):
    #Work Cited
    #Based of Algo printed in Handbook of Applied Cryptography by Alfred J Menezes, Paul C Van Oorschot, and Scott A Vanstone CRC Press
    #Page 136
    security = 10
    if n == 2:
        return True
    elif n < 2:
        return False
    for i in range(security):
        a = random.randint(2, n-1)
        #finds a number a such that it is coprime to n and not a product of n
        gcd = xgcd(a,n)
        while gcd[0] != 1 and a % n == 0:
            print(gcd[0])
            a = random.randint(2, n-1)
            gcd = xgcd(a,n)
        
        #print(a,(n-1), n)
        #print(FastModExp(a, (n-1), n))
        if FastModExp(a, (n-1), n) != 1:
            return False
    return True

def fastfermatstest(n):
    #Work Cited
    #Based of Algo printed in Handbook of Applied Cryptography by Alfred J Menezes, Paul C Van Oorschot, and Scott A Vanstone CRC Press
    #Page 136
    #removed requirment for checking if coprime, just assume so. Hope to speed up this function.
    #Test only the bases that fail for being coprime, that should speed it up a lot.
    #With 10 tests using random primes for base a in a^(n-1) mod n, it should be very unlikly that any are not prime.
    #prime list used has over 200 primes to pick from.
    n = abs(n)
    basea= [] 
    if n == 2:
        return True
    elif n < 2:
        return False
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571,3581,3583,3593,3607,3613,3617,3623,3631,3637,3643,3659,3671,3673,3677,3691,3697,3701,3709,3719,3727,3733,3739,3761,3767,3769,3779,3793,3797,3803,3821,3823,3833,3847,3851,3853,3863,3877,3881,3889,3907,3911,3917,3919,3923,3929,3931,3943,3947,3967,3989,4001,4003,4007,4013,4019,4021,4027,4049,4051,4057,4073,4079,4091,4093,4099,4111,4127,4129,4133,4139,4153,4157,4159,4177,4201,4211,4217,4219,4229,4231,4241,4243,4253,4259,4261,4271,4273,4283,4289,4297,4327,4337,4339,4349,4357,4363,4373,4391,4397,4409,4421,4423,4441,4447,4451,4457,4463,4481,4483,4493,4507,4513,4517,4519,4523,4547,4549,4561,4567,4583,4591,4597,4603,4621,4637,4639,4643,4649,4651,4657,4663,4673,4679,4691,4703,4721,4723,4729,4733,4751,4759,4783,4787,4789,4793,4799,4801,4813,4817,4831,4861,4871,4877,4889,4903,4909,4919,4931,4933,4937,4943,4951,4957,4967,4969,4973,4987,4993,4999,5003,5009,5011,5021,5023,5039,5051,5059,5077,5081,5087,5099,5101,5107,5113,5119,5147,5153,5167,5171,5179,5189,5197,5209,5227,5231,5233,5237,5261,5273,5279,5281,5297,5303,5309,5323,5333,5347,5351,5381,5387,5393,5399,5407,5413,5417,5419,5431,5437,5441,5443,5449,5471,5477,5479,5483,5501,5503,5507,5519,5521,5527,5531,5557,5563,5569,5573,5581,5591,5623,5639,5641,5647,5651,5653,5657,5659,5669,5683,5689,5693,5701,5711,5717,5737,5741,5743,5749,5779,5783,5791,5801,5807,5813,5821,5827,5839,5843,5849,5851,5857,5861,5867,5869,5879,5881,5897,5903,5923,5927,5939,5953,5981,5987,6007,6011,6029,6037,6043,6047,6053,6067,6073,6079,6089,6091,6101,6113,6121,6131,6133,6143,6151,6163,6173,6197,6199,6203]
    a = [2,3,5,7,11,23,27]
    for i in range(1):
        if not FastModExp(primes[random.randint(0,len([x for x in primes if x < n])-1)], (n-1), n) == 1:
            return False
    return True
def generateprime(bits):
    #https://www.di-mgt.com.au/rsa_alg.html#note1
    if bits <= 4:
        while True:
            n = random.randint(2,2**bits)
            if fastfermatstest(n):
                return n
    binarydigit = "0b11"
    for i in range(0, (bits-3)):
        binarydigit += str(random.randint(0,1))
    binarydigit += "1" #set the lowest bit to 1, to insure its odd
    while True:
        if fastfermatstest(int(binarydigit,2)):
            break
        binarydigit = bin(int(binarydigit,2)+2) ##incrment by 2 Its much faster than generating a new random number and testing
        #As the digit increase the odds of not finding a prime grows. 1/(ln(n)) Brute search from a composite might hit a messene prime before finding a radom prime.
    return int(binarydigit,2)
        
    
def generate_RSA_key_pair(bitlength):
    #doesn't work at all on scsu standard computers. The best prime is 65537, but that will take many mins to compute with fastexpmod
    e = 5 # {3, 5, 17, 257, 65537}
    p = generateprime(int(bitlength/2))
    while p % e != 1:
        p = generateprime(int(bitlength/2))
    q = generateprime(bitlength/2)
    while q % e != 1:
        q = generateprime((bitlength - int(bitlength/2)))
    N = p*q
    L = (p-1)*(q-1)
    d = modinverse(e, L)
    return (N, e, d)

    
    
def messurebitlength(n):
    #messure bit length of interger n
    return int(math.log(n,2)+1)

def RSAEncryption(m, e, n):
    pass

def RSADecryption(c, d, n):
    pass





def main():
    
    
    
    #GUI
    root = Tk()
    root.geometry("550x400")
    root.minsize(width=550, height=400)
    app = Window(root)
    root.mainloop()


main()
