##Dustin Watson
##CNA Crypto
##Library for ExtendGCD

#Modified from Discrete Mathmeatics 7th ed by Richard Johnsonbaugh page 256
#Pearson Eduation Inc Person Prentice Hall Upper Saddle River NJ

def Bezoutsgcdr(a,b,s,t):
    #this function uses Bézout's identity
    #to find GCD
    #to find the lowest common terms for s, t (coprimes), use 1 for s, -1 for t
    if(a<b):
        a,b=b,a
    if(b==0):
        s=1
        t=0
        return a
    q = a//b
    r =a%b
    g = Bezoutsgcdr(b,r,s,t)
    s = t
    t = s - t * q
    if g == 1:
        return g, s, t
    else:
        return g,s,t

a=17
b=4
s=1
t=-1


values=Bezoutsgcdr(a,b,s,t)

print(values)
