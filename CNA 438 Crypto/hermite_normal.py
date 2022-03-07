import copy
#Algo from psudocode in Algorithmic Cryptanalysis by Antoine Joux page 104
#
#Modifed to to alpha scaler accounting for det calcuations
#Works with 2x2 and 3x3, however NxN has a bug that puts it in an infinite loop
#fix that bug, and it would do NxN
def hermite_normal(a):
    alpha = 1 # assert that scalar 1 * m = m
    #Requires m be a NxN matrix with interger entries
    #zero base indexing, indexing starting at 1 or other numbers will cause this to fail
    if len(a) != len(a[0]):
        return "Not square"
    m = copy.deepcopy(a) #makes sure we create a completely new matrix to work on.
    for i in range(0, len(m)):
        done = False
        while not done:
            P = 0
            
            for k in range(i, len(m)):
                #choose the smallest non-zero in abs in the current column to be the pivot.
                if m[i][k] != 0:
                    if (P == 0) or (abs(m[i][k]) < P):
                        j = k
                        P = m[i][j]
                        #print("updating P", P)
            if P == 0:
                print("first error")
                return [] #None invertaible matrix
            done = True
            m[i], m[j] = m[j], m[i] #exchange rows in matrix m
            #update aplha for matrix det tracking
            #alpha *= -1
            print(m)
            if P < 0:
                m[i] = [-1 * elem for elem in m[i]] #Mi <- -Mi
                P *= -1
            for j in range(i+1, len(m)):
                C = m[j][i] # C <- Mi,j
                #print(C, j, i)
                m[j] = [Mj - ((C//P) * Mi) for Mj, Mi in zip(m[j],m[i])] #Mj <- Mj - lower(C/P) * Mi
                #alpha *= -1
                if m[j][i] != 0:
                    #print(m)
                    done = False
    if m[len(m)-1][len(m)-1] == 0: #if Mn,n = 0, Mn <
        print("second error")
        return [] #Non-invertiable system
    if m[len(m)-1][len(m)-1] < 0: #if Mn,n < 0, then Mn <- -Mn
        m[len(m)-1] = [-1 * elem for elem in m[len(m)-1]] #Mi <- -Mi
    for i in range(2, len(m)):
        P = m[i][i]
        for j in range(1, i - 1):
            C = m[j][i]
            m[j] = [Mj - ((C//P) * Mi) for Mj, Mi in zip(m[j],m[i])] #Mj <- Mj - lower(C/P) * Mi
            alpha *= -1
    #M is not in Mermite Normal Form, so to find the Det, mutlipy the diagnal then apply alpha
    for z in range(0, len(m)):
        alpha *= m[z][z]
    if len(m) % 2 == 0:
        alpha *=-1
    print(alpha)
    return m #output the Mermite Normal Form of M
c = [[10,-2,-2,4],[0,-2,-1,-6],[-1,2,3,-2],[0,1,-1,0]]
a = [[4,3],[5,-2]] #has an inverse

b = [[3,0,1,1],[0,1,0,0],[0,0,19,1],[0,0,0,3]]

d = [[5,3],[-5,4]]

e = [[1,2,3],[0,1,5],[5,6,0]]

herm = hermite_normal(e)
#print(herm)


for row in herm:
    print(row)
