#Dustin Watson
#CNA 436
#DF KEP


import math
import random

def main ():
    ###
    #Customize pram here:
    numberofusers = 3 
    ###
    for 0 in range(numberofusers):
        shared_prime=0
        print("Diff/Hilman KEP ")
        while not fermatstest(shared_prime):
            shared_prime = enterinteger("Enter a shared prime for user " +chr(65+i) +":")
            if not fermatstest(shared_prime):
                print("Not a prime, try again")
        print("Randomly selecting a generator number of prime", shared_prime, "may take some time if prime is greater than 20, please wait") 
        list_of_generators = FindPrimitiveRoots(shared_prime)
        if len(list_of_generators) == 0:
            print("Avoid using Carmical numbers or some unexepcted error has accoured")
            print("Try selecting another number for a shared prime")

        selected_generator = list_of_generators[random.randint(0,len(list_of_generators))]
        print("Selected generator:", selected_generator, " of mod", shared_prime)
        
        userskeys = {num_users: numberofusers}
            users[i][0] = enterinteger("Enter user " +chr(65+i) + "'s private prime: " )
            users[i][1] = 0
            while not users[i][1]:
                users[i][1] = enterinteger("Enter a " +chr(65+i) +" public prime: ")
                if not fermatstest(shared_prime):
                    print("Not a prime")
        print(users)
        print(FindPrimitiveRoots(enterinteger("Enter a group ord n: ")))


def FindPrimitiveRoots(ordn):
    #finds the prime roots in ord n
    #returns and empty list if it is not a cyclic group and has no prime roots/generators
    #Unit tested upto ord n = 72
    #Hand created algo based on the logic and demo of Steven Wong Primitive Roots Youtube Video: https://youtu.be/NsaXVGmuX18
    #Other cites include:
    #http://mathworld.wolfram.com/PrimitiveRoot.html
    #https://en.wikipedia.org/wiki/Primitive_root_modulo_n
    #https://math.stackexchange.com/questions/124408/finding-a-primitive-root-of-a-prime-number
    #https://www.doc.ic.ac.uk/~mrh/330tutor/ch06.html#id36080356
    #The Mathematics of Encryption by Margaret Cozzens Steven J Miller
    kmax = 10
    group = phi(ordn)
    groupwithoutord2 = [x for x in group[1] if x % 2 != 0]
    #withoutidenty = [elem for elem in group[1] if elem not in [1]]
    primeroottable = [[FastModExp(a,k,ordn) for k in range(1,ordn**2)] for a in range(1, ordn+1)]
    primeroot = []
    for a in range(len(primeroottable)):
        primeroottable[a].sort()
        primeroottable[a] = [x for y, x in enumerate(primeroottable[a]) if x not in primeroottable[a][:y]] #remove the duplicates computed from the a^k
        #Assert that only true roots will have a full set of non duplicates
        #if ord n is a power of 2, remove all numbers mod 2
        if ordn % 2 == 0:
            primeroottable[a] = [x for y, x in enumerate(primeroottable[a]) if x if x % 2 != 0]  #This is required to remove powers of 2 that exist in 2*2^k and 2^k groups
        if len(primeroottable[a]) == group[0] and primeroottable[a][-1] != ordn: #Sometimes the algo isn't smart, and things the ordn value is in the group, remove it before picking values. Nomraly happens with ordn < 10
            primeroot.append(a+1)
    return primeroot
    
    
    
    
    
def primefactor(n):
    #Work Cited: Source of primes: http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283]
    factors = []
    for p in primes:
        q,r = divmod(n, p)
        if r == 0:
            factors.append(p)
    return factors
        
    
        
        
    
       
def enterinteger(message):
    while True:
        try:
            numbers = int(input(message))
            break
        except ValueError:
            print("Not an integer")
    return numbers

def enterstring(message):
    while True:
        try:
            numbers = str(input(message))
            break
        except ValueError:
            print("Not an string")
    return numbers


#Funiction that calcuates PHI
def phi(n):
    #gives a truple of number of primes and the primes of the group ord n
    if fermatstest(n):
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
            
def fermatstest(n):
    #Work Cited
    #Based of Algo printed in Handbook of Applied Cryptography by Alfred J Menezes, Paul C Van Oorschot, and Scott A Vanstone CRC Press
    #Page 136
    security = int(math.ceil(n ** .5) * (1-(1/math.log(561)))) #scale the chance of being composite to the square of its size. Checks for a base in exponentation of fermat's little therom.
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
   


def FastModExp(a, e, n):
    #Work Cited
    #page 153 Applied Crypto Alfred J Menezes, Paul C van Oorschor, Scott A Vanstone CRC Press
    #and
    #The Mathematics of Encryption Cozzens page 191
    #Algo in psudocode
    b = 1 #set a var to compute the remainder later
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
     
     
    
#extended Eucludean Algo
def xgcd(p,d):
    x0,x1,y0,y1 = 1,0,0,1
    while d != 0:
        q, p, d = p //d, d, p % d
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return (int(p), int(x0), int(y0))


def MillerRabinRandomSearch(k):
    #works with bits 12 and less
    #returns a n (prime number) that is k <= bits long
    #Cite
    #page 153 Applied Crypto Alfred J Menezes, Paul C van Oorschor, Scott A Vanstone CRC Press
    #Algo in psudocode
    maxdec = ((2 ** k))
    prime = False
    while True:
        n = random.randint(2,maxdec)
        if trial_division(n):
            return n
        
    
        
def trial_division(n):
    #This is sudo trial division
    #first 207 primes
    #Work Cited: Source of primes: http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283]
    for i in range(0, int(n**.5)):
        if n % primes[i] == 0:
            return False
    return True
            
def MaurerGeneratingPrimes(k):
    #Cite
    #page 153 Applied Crypto Alfred J Menezes, Paul C van Oorschor, Scott A Vanstone CRC Press
    #Algo in psudocode
    #This code is bugged, dont use
    if k <= 20:
        return MillerRabinRandomSearch(k)
    c, m = 0.1, 20
    B = c * (k ** 2)
    if k > 2 * m:
        while not (k - r*k) > m:
            s = random.randint(0,2)
            r = 2 ** (s-1)
    else:
        r = 0.5
    q = MaurerGeneratingPrimes(int(r * k)+1)
    I = int((2 ** (k - 1))/ (2 * q))
    success = 0
    while not success:
        R = random.randint(I + 1, (2 * I)+1)
        n = 2*R*q + 1
        for i in range(2, B):
            if fermatstest(i):
                if not n % i != 0:                    
                    a = random.randint(2, n-2)
                    b = FastModExp(a, (n - 1), n)
                    if b == 1:
                        b = FastModExp(a, 2*R, n)
                        d = xgcd(b - 1, n)
                        if d(0) == 1:
                            success = 1
    return n
                        
def MersennePrimeGenrator(k):
    #Gernate a Merseene Prime of k-bit length
    #bugged, hand created.
    maxdec = ((2 ** k))
    r = random.randint(2, maxdec)
    PossibleMersenne = (2 ** r) - 1
    while FastModExp(2, PossibleMersenne - 1, PossibleMersenne) != 1:
        r = random.randint(2, maxdec)
        PossibleMersenne = (2 ** r) - 1        
    return PossibleMersenne
    
    
        
    

main()

