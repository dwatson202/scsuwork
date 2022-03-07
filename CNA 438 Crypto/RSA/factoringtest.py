def Easy_DL(a, B, p):
    if (B ** ((p-1)/2)) % p == 1:
        i=1
        while not (a**i) % p == (B % p):
            i+=1
        return (1, i)
    else:
        return (-1, 0)
