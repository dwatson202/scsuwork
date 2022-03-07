import copy
#Algo from psudocode in Algorithmic Cryptoanalysis by Antione Joux page 104
#Thank you Antione Joux
def matrix_invert(a):
    #Requires m be a NxN matrix
    #zero base indexing, indexing starting at 1 or other numbers will cause this to fail
    m = copy.deepcopy(a) #makes sure we create a completely new matrix to work on.
    n = [[0.0]*i + [1] + [0.0]*(len(m)-i-1) for i in range(len(m)) ] #create an identy matrix of of floats
    P = 0
    alpha = 1 #asserts that 1 * M = M
    for i in range(len(m)):
        for j in range(i,len(m)):
            P = m[j][i]
            if P != 0:
                break
        if P == 0:
            print("not invertable")
            alpha = 0           
            return []
        
        m[i], m[j] = m[j], m[i] # swap row i for j, and vice versa in m
        n[i], n[j] = n[j], n[i] # swap row i for j, and vice versa in n
        m[i] = [elem / P for elem in m[i]] # devide line i in m by P
        n[i] = [elem / P for elem in n[i]] # devide line i in n by P
        
        #accounting for all the elementry row ops
        #alpha = alpha * -1
        alpha = alpha * -1* (P)

        for j in range(i+1, len(m)):
            C = m[j][i] #Let C = Mj,i
            m[j] = [Mj - (C * Mi) for Mi, Mj in zip(m[i],m[j])] # Substract C times line i from M from j of M
            n[j] = [Nj - (C * Ni) for Ni, Nj in zip(n[i],n[j])] # Substract C times line i from M from j of N
    #M is upper trangular now with Diagnoal of 1 It does work.
    
    
    for i in range(len(m)-1, 0, -1):
        for j in range(0, i):
            C = m[j][i]
            m[j] = [Mj - (C * Mi) for Mi, Mj in zip(m[i],m[j])] # Mj <- Mj - (C * Mi)
            n[j] = [Nj - (C * Ni) for Ni, Nj in zip(n[i],n[j])] # Nj <- Nj - (C * Ni)
    #Assert (NOW) N is inverse matrix
            
    if len(m) % 2 == 1:
        alpha *=-1
    #print(alpha) #print the det(a)
    return m, n, [alpha] #output inverse of matrix M

aa = [[10,-2,-2,4],[0,-2,-1,-6],[-1,2,3,-2],[0,1,-1,0]]
a = [[4,3],[5,-2]]
#inverse = matrix_invert(a)
#print(inverse)

d = [[5,3],[-5,4]]

e = [[1,2,3],[0,1,5],[5,6,0]]

f = [[1,2,3],[0,1,5],[0,0,5]]

fivebyfive = [[1,8,-9,7,5],[0,1,0,4,4],[0,0,1,2,5],[0,0,0,1,-5],[0,0,0,0,1]]

inverse = matrix_invert(a)

for matrice in inverse:
    print()
    for row in matrice:
        print(row)
