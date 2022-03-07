#Dustin Watson
#CNA 436
#DF KEP

import math
import random

def main ():
    #shared_prime=0
    #while not fermatstest(shared_prime,100):
        #while not fermatstest(shared_prime,100):
            #try:
                #shared_prime = int(input("Enter a shared prime: "))
                #break
            #except ValueError:
                #print("Not an integer")
                
        #if not fermatstest(shared_prime, 100):
            #print("Not Prime, try again")
            
    print(AKS(101))
    
            


#Funiction that calcuates PHI
def phi(n):
    if AKS(n):
        #if its a prime, return n-1, thats the number of digits releitivty prime to n
        return n-1
    else:
        count = 0
        for i in range(n):
            xgcdvalue = xgcd(n, i)
            if xgcdvalue[0] == 1:
                count += 1
        return count
            
                
   
def AKS(n):

    if n == 2 or n == 3:
        return True
    elif not isinstance(n, int):
        return False
    elif n == 1:
        return False
    elif n == 0:
        return False
    elif n < 0:
        return False
    else:
        for k in range(3, n-2):
            test = (math.factorial(n)/(math.factorial(k)*math.factorial(n-k))) % n
            if test:
                return False
        return True
    
def fermatstest(n, t):
    #buggy, doesn't work
    #Cited Works:
    #Handbook of Applied Cryptography
    #Alfred J Menezes, Paul C van Oorschot, Scott A Vanstone
    #page 136
    #From Algo outline
    if t < 1:
        return "Security param not large enough"
    if n == 0:
        return False
    if n == 2:
        return True
    elif n < 3:
        return False
    for i in range(1, t+1):
        a = random.randint(2, n-2)
        print(a)
        if 1 != FastModExp(a, n-1, n):
            return False
    return True


def MillerRabinP(n,t):
    if n == 2:
        return True
    elif (n % 2) == 0:
        return False
    elif n < 2:
        return False
    s = 0
    d = n - 1
    remainder = -1
    while remainder == 1:
        quotient, remainder = divmod(d, 2)
        s += 1
        r = quotient
        
    for i in range(1, t):
        a = random.randint(2,n-1)
        y = FastModExp(a, r, n)
        if y != 1 and y != (n - 1):
            j = 1
            while j <= s - 1 and y != n:
                y = FastModExp(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
        return True
    

def FastModExp(a, e, n):
    b = 1 #set a var to compute the remainder later
    if e == 0:
        return b
    k = list(map(int, str(bin(e)[2:]))) # convert the exponent to binary and store it in a list
    k.reverse()
    A = a
    if k[-1] == 1:
        b = a
    for i in range(1, len(k)):
        A = (A ** 2) % n
        if k[i] == 1:
            b = (A * b) % n
    return b
     
     
    
#extended Eucludean Algo
def xgcd(p,d):
    x0,x1,y0,y1 = 1,0,0,1
    while d != 0:
        q, p, d = p //d, d, p % d
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return (int(p), int(x0), int(y0))

def randomprimes(n):
    #select a prime less than n
    pass
    

main()

