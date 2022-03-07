#Dustin Watson
#CNA 438
#CRT calcutator.
#Solves where x = y mod p where x has a coefficent of 1
#Input y and p

def xgcd(p,d):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while d != 0:
        q, p, d = p // d, d, p % d
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  (int(p), int(x0), int(y0))

def check4reletivltyprime(alpha):
    #Assume alpha is a list of integers
    #return True if all reletivtiy prime
    #else return the number canadiate which fails test
    if not isinstance(alpha, (list,)):
        print(alpha, "input varaible is not a list")
        return False
    for i in range(len(alpha)):
        canadiate = alpha[i]
        for j in range(len(alpha)):
            if i != j:
                #compare all other numbers in the list to the candaidate
                gcdoutput = xgcd(canadiate, alpha[j])
                if gcdoutput[0] != 1:
                    #messagebox.showwarning("Warning",str(value) + " is not realitivity prime to 36. Correct the key and try again")
                    print(canadiate, "Not reletivity prime to", alpha[j])
                    return canadiate
    return True

def crt(y, p):
    #Works Cited:
    #Handbook of Applied Cryptography
    #by Alfred J Memezes, Paul C van Oorschot, Scott A Vanstone
    #CRC PRESS LLC 1997
    #Listed at Gauss's Algorithm
    #Sigma i=0 AiNiMi on page 68
    #Returns the solution as a drupal  in the form of (y mod p) to
    #Sum(ai * Ni * Mi) or False if no solution exists
    #assumes that all numbers in P are reltiviity prime
    if not isinstance(y, (list,)):
        print("y input is not a list")
        return False
    if not isinstance(p, (list,)):
        print(p, "input is not a list")
        return False
    #check if y and p both contain the same number of integers
    if len(y) != len(p):
        print("Not the same number of intgers.")
        return False
    #return y mod p if there is only one set integers
    if len(y) == 1:
        return (y[0] % p[0], p[0])
    #product of all the numbers in P, the list of reaptlivity prime numbers
    N = 1
    for number in p:
        N *= number
    #Assert that N is now a product of all the reletivity prime numbers in P, a list of integers
    #
    sum = 0 #create a sum variable
    for integers in zip(y, p):
        Ni = N / integers[1]
        a = integers[0] #set a to the y value in x = y mod p
        #Get inverse
        gcdvalues = xgcd(Ni, integers[1])
        Mi = gcdvalues[1]
        if Mi == 0:
            return False # no solution exists, becuse we are saying 0 * Ni * x is congruent to 0 * y mod p
            
        #print("Values: ", Ni, N, "GCDValues: ", gcdvalues)
        #print("Should be the the inverse: ", Mi)
        sum += a * Ni * Mi #ai * Ni * M
    #Assert that sum mod N solution
    #reduce it to the the solution of 0 <= sum <= N
    sum = sum % N
    return (sum, N)
        

def main():
    #Has bugs, don't work correctly yet.
    mods = []
    ys = []
    y = -1
    p = -1
    while p != 0 and y != 0: #enter 0 to terminate
        y = int(input("Enter integer y in x = y mod p: "))
        p = int(input("Enter integer p in x = y mod p: "))
        if p != 0 and y !=0:
            mods.append(p)
            ys.append(y)
        #check to make sure (mod p) are all reletivity prime:
            relprime = check4reletivltyprime(mods)
        if relprime != True:
            mods = mods[:-1] #remove the non prime number and its matching y
            ys = ys[:-1]
    returncrt = crt(ys, mods)
    print(int(returncrt[0]),"mod", int(returncrt[1]))

main()
