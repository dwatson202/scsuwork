#Dustin Watson
#HillCipher/Block cipher
#CNA 438
#python 3.x script



#import math
#import re
#from random import *
#import fractions
import copy
import string


class matrix:
    #cites:
    #https://people.richland.edu/james/lecture/m116/matrices/determinant.html
    #Linear algerba Daniel Scully 2015
    def __init__(self, w,h):
        ##constructor for matrixmaker class
        self.threshold = 0.000001 # deals with small amounts that cause compuation errors
        self.matrix = [[0.0 for x in range(w)] for y in range(h)]
        self.w = w
        self.h = h
        self.determinant = 0
        self.invertaible = False
        self.invertedmatrix = []
        self.hermite_normal_matrix = []
        
    def __del__(self):
        #Delete all the values to uninstanate the class object
        del self.threshold
        del self.matrix
        del self.w
        del self.h
        del self.determinant
        del self.invertaible
        del self.invertedmatrix
        del self.hermite_normal_matrix

    def setMatrix(self,d):
        self.matrix = d
        #self.rowechelon = self.REF(d)

    def setindex(self, m,n, value):
        try:
            self.matrix[m][n] = value
        except:
            print("Error: Attempt to set a value outside the arrays of the matrix dementions")

    def getindex(self, m, n):
        return self.matrix[m][n]

    def humanreadable(self):
        try:
            print("print out of matrix:")
            print("---------------")
            for rows in self.matrix:
                print(rows)
            print("---------------")
        except NameError:
            print("Matrix not defined or set, please set it first")
            

    def humanreadableinverse(self):
        try:
            print("print out of matrix inverse:")
            print("---------------")
            for rows in self.invertedmatrix:
                print(rows)
            print("---------------")
        except NameError:
            print("Matrix not defined or set, please set it first")
            
    def getcollist(self, n):
        return [rows[n] for rows in self.matrix]
    
    def getrowlist(self, m):
        return self.matrix[m]

    def sortbyrow(self):
        return None

    def sortbycol(self):
        return None

    def setidentity(self, n):
        self.h = n
        self.w = n
        if self.h == self.w:
            self.matrix = [[0.0]*i + [1] + [0.0]*(self.w-i-1) for i in range(self.w) ]

    def setRow(self,m,value):
        self.matrix[m] = value

    def setCol(self,n,value):
        ##Not yet working
        self.matrix[n] = value
        #newmatrix = [][]
        [rows[n] for rows in self.matrix]

    def setnull(self):
        for i in range(0,self.w):
            for j in range(0,self.h):
                self.matrix[i][j] = 0
                
    def transpose(self, update=False):
        newmatrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        if update:
            self.matrix = newmatrix
        return newmatrix

    def getcols(self):
        return self.w

    def getrows(self):
        return self.h

    def show(self):
        return self.matrix

    def sumRow(self, m):
        return sum(self.matrix[m])

    def sumCol(self, n):
        return sum([rows[n] for rows in self.matrix])

    def getDet(self):
        self.matrix_invert()
        return self.determinant
    
    def getInvertable(self):
        return self.invertaible

    def _Augment_Identy(self):
        newmatrix = [[0.0] * (self.w*2) for i in range(0, self.h)]
        for i in range(len(newmatrix)):
            for j in range(len(newmatrix[0])):
                if i < self.h and j < self.w:
                    newmatrix[i][j] = self.matrix[i][j]
                elif i == (j-self.w):
                    newmatrix[i][j] = 1
        return newmatrix

    def _DeAugment(self, M, start_row=0, start_col=0, rows=None, cols=None):
        #It slices, it dices, it makes Julian Fries, but wait, theres more
        #Now you can cut up matricies to get anwser to linar algerba problems.
        #cols and rows are the cols and rows indexed from start_col and start_row
        #assumes a left or bottom augmentaion of matrixes will always be used
        #other matrix slicing can be done with creative use of neg values
        if rows == None:
            rows = self.h
        if cols == None:
            cols = self.w
        if start_col + cols > len(M[0]):
            return None
        if start_row + rows > len(M):
            return None
        newmatrix = [[0.0] * (cols) for i in range(0, rows)]
        for i in range(start_row, rows):
            for j in range(start_col, cols):
                newmatrix[i][j] = M[i][j]
        return newmatrix

    def getInverse(self):
        if self.h != self.w:
            self.invertaible = False
            self.determinant = 0
            return []
        #check if it has an inverse
        self.invertedmatrix = self.matrix_invert()
        if self.invertaible:
            return self.invertedmatrix
        else:
            return []
        
    def getHermite(self):
        if self.h != self.w:
            self.invertaible = False
            self.determinant = 0
            return []
        #check if it has an inverse
        self.hermite_normal_matrix = self.hermite_normal()
        if self.invertaible:
            return self.hermite_normal
        else:
            return []

    def _catMatrix(self,matrix1, update=False):
        newmatrix = [x+y for x,y in zip(self.matrix, matrix1)]
        if update:
            self.matrix = newmatrix
        return newmatrix
    #Algo from psudocode in Algorithmic Cryptanalysis by Antoine Joux page 104
    #
    #Modifed to to alpha scaler accounting for det calcuations
    #Works with 2x2 and 3x3, however NxN has a bug that puts it in an infinite loop
    #fix that bug, and it would do NxN
    def hermite_normal(self):
        alpha = 1 # assert that scalar 1 * m = m
        #Requires m be a NxN matrix with interger entries
        #zero base indexing, indexing starting at 1 or other numbers will cause this to fail
        if self.h != self.w:
            return "Not square"
        m = copy.deepcopy(self.matrix) #makes sure we create a completely new matrix to work on.
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
                #print(m)
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
        #print(alpha)
        self.determinant = alpha
        self.hermite_normal_matrix = m
        self.invertaible = True
        return m #output the Mermite Normal Form of M
    
    def matrix_mod(self, mod):
        #mods each element in the matrix and update self.matrix
        for a in range(len(self.matrix)):
            for b in range(len(self.matrix[0])):
                self.matrix[a][b] = float(int(self.matrix[a][b] % mod))
    
    def matrix_scalar(self, scalar):
        #update the matrix to a scalar
        for a in range(len(self.matrix)):
            for b in range(len(self.matrix[0])):
                self.matrix[a][b] *= scalar

    def convertfrom36(self):
        #returns a string rep in base 36 (for class) of the contents of the matrix
        #first, mod 36, to make sure its in the correct place
        charset = string.ascii_lowercase + string.digits
        f = copy.deepcopy(self.matrix) #don't want to update the matrix, just return a string
        stringreturn = ""
        for m in range(len(f)):
            for n in range(len(f)):
                stringreturn += charset[(int(f[m][n]) % 36)]
        return stringreturn
                
                
        
    
    #Algo from psudocode in Algorithmic Cryptoanalysis by Antione Joux page 104
    #Thank you Antione Joux
    def matrix_invert(self):
        #Requires m be a NxN matrix
        #zero base indexing, indexing starting at 1 or other numbers will cause this to fail
        if self.h != self.w:
            self.invertaible = False
            return None
        m = copy.deepcopy(self.matrix) #makes sure we create a completely new matrix to work on.
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
                self.invertaible = False
                alpha = 0           
                self.determinant = 0
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
        self.determinant = alpha
        self.invertaible = True
        self.invertedmatrix = n
        return n#output inverse of matrix M
        

def sum_matrices(matrix1, matrix2, update_matrix=None):
    ##sum two equially sized matrices
    ##get the size of the two matrices

    if not type(matrix1) is matrix or not type(matrix2) is matrix: return None ##may not work with inhartnace or multi add or sums

    if ((matrix1.getcols() != matrix2.getcols()) or (matrix1.getrows() != matrix2.getrows())):
        print("matrices not the same size")
        return None
    else:
        newmatrix = matrix(matrix1.getrows(), matrix1.getrows())
    for m in range(0,matrix1.getrows()):
        for n in range(0, matrix1.getcols()):
            newmatrix.setindex(m,n, matrix1.getindex(m, n) + matrix2.getindex(m, n))
    if type(update_matrix) is matrix:
        update_matrix.setMatrix(newmatrix)
    return newmatrix

def multiply_matrices(matrix1, matrix2, update_matrix=None):
    ##Mutiply two matrices and return the a matrix object
    ##None otherwise if an error happens

    if not type(matrix1) is matrix or not type(matrix2) is matrix:
        print("Not both matricies")
        return None ##may not work with inhartnace or multi add or sums

    if ((matrix1.getcols() != matrix2.getrows())):
        print("matrices not the correct size for multipication")
        return None
    else:
        newmatrix = matrix(matrix1.getrows(), matrix2.getcols())
        newmatrix.setnull()
        for i in range(0, matrix1.getrows()):
            for j in range(matrix2.getcols()):
                for t in range(matrix2.getrows()):
                    #print((newmatrix.getindex(i,j)+(matrix1.getindex(i,t) * matrix2.getindex(t,j))))
                    newmatrix.setindex(i,j, (newmatrix.getindex(i,j)+(matrix1.getindex(i,t) * matrix2.getindex(t,j))))
        if type(update_matrix) is matrix:
            update_matrix.setMatrix(newmatrix)
        return newmatrix
    



def printmenu():
    print("")
    print("Hill Cipher on NxN with any length of Plain Text")
    print("------------------------------------------------------------------")
    print("Main Menu")
    print("1 Input A Matrix [Key A]")
    print("2 Input Plain Text String")
    print("3 Input Cipher Text String")
    print("4 Encrypt Plain Text")
    print("5 Decrypt Cipher Text")
    print("6 Display A [Key A]")
    print("7 Display A^-1 [Inverse of Key A]")
    if Toggle_Block_Display:
        print("8 Toggle off showing each block transfer while processing")
    else:
        print("8 Toggle on showing each block transfer while processing")
    print("9 Decrypt Cipher Text")
    print("d Display Det(A)")
    
    print("0 Quit")
    print("m Show Menu")
    print("x Decrypt last encrypted message")
    print("Pick and option by typing an number and pressing enter")
    print("")

def enter_matrix():
    #takes in no input, outputs a 2d list
    print("")
    NxN = -1
    while True:
        try:
            NxN = int(input("Please enter a interger N size of matrix: "))
            break
        except ValueError:
            print("Not a valid number, please try again")
        except UnboundLocalError:
            print("Enter a value")
        if NxN < 0:
            print("Can not be zero or less, try again")
    #fill out the matrix:
    templist = [[0 for x in range(NxN)] for y in range(NxN)]  #create an empty matrix of NxN
    for m in range(NxN):
        for n in range(NxN):
            while True:
                try:
                    element = int(input("Please enter interger for " + str(m) + ", " + str(n) + ": "))
                    templist[m][n] = element
                    break
                except ValueError:
                    print("Not a valid number, please try again")
                except UnboundLocalError:
                    print("Enter a value")
    return templist

def encrypt_function(plaintext, key, showblocks):
    Nvalue=A.getcols()
    #filler = ((-1* len(plaintext)) % (Nvalue)) ##Fill in extra spaces with x's
    filler = divmod(Nvalue,len(plaintext))
    print(filler)
    for i in range(filler[1]):
        plaintext += "x"
    #convert to integers
    intvalues = base36(plaintext)
    rowlen = len(intvalues) // Nvalue
    i = 0
    #creates an Mx(PlainText/N) list
    #instatate a PMatrix object with the set 2d list
    PMatrix = matrix(Nvalue, Nvalue)
    while i*rowlen < len(intvalues):
        print(intvalues[i*rowlen:i*rowlen+rowlen])
        PMatrix.setRow(i, intvalues[i*rowlen:i*rowlen+rowlen])
        i+=1
    if showblocks:
        PMatrix.humanreadable()
    #instatiate a CMatrix object to hold the encryption
    CMatrix = matrix(Nvalue, PMatrix.getcols())
    CMatrix = multiply_matrices(key, PMatrix)
    #mod the matrix to 36:
    CMatrix.matrix_mod(36)
    if showblocks:
        print("Ciphertext block")
        CMatrix.humanreadable()
    return CMatrix
    

def decrypt_function(ciphertextmatrix, key, showblocks):
    Nvalue=A.getcols()
    #get coprime and other values that goes along with the DET of the matrix
    gcdvalues = xgcd(36, key.getDet())
    #get the inverse of the key
    inversekey = key.matrix_inverse()
    #create a new matrix object to decrypt this CT
    Ainverse = matrix(Nvalue,Nvalue)
    Ainverse.setMatrix(inversekey)
    #Now apply the coprime as a scalar and uypdate Ainverse to be a unlocking Key
    Ainverse.matrix_scalar(gcdvalues["gcd"])
    #now mod it to 36
    Ainverse.matrix_mod(36)
    #Now apply the inverse to ciphertextmatrix
    newplain = multiply_matrices(ciphertextmatrix, Ainverse)
    #Now new plaintext is decrypted, now mod 36 it
    newplain.matrix_mod(36)
    return newplain
    
    
    
    
    

def xgcd(p,d):
    if p<d:
        p,d=d,p
    x0, x1, y0, y1 = 1, 0, 0, 1
    while d != 0:
        q, p, d = p // d, d, p % d
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  {"gcd":p, "p":p, "d":d, p:x0, d:y0}

def base36(InputStr):
    charset = string.ascii_lowercase + string.digits
    InputStr = InputStr.lower()
    IntStr = [charset.index(char) for char in InputStr]
    return IntStr

def frombase36(IntList):
    charset = string.ascii_lowercase + string.digits
    OutputStr = [charset[char] for char in IntList]
    NewOutputStr = ""
    for char in OutputStr:
        NewOutputStr = NewOutputStr + char
    return NewOutputStr

    
    
def invalidchars_exist(stringvalue):
    stringvalue = stringvalue.lower()
    alphanum = string.ascii_lowercase + string.digits
    location = 0
    for char in stringvalue:
        location = alphanum.find(char)
        if location == -1:
            return True
    return False
    

#set vars
Toggle_Block_Display = False
sentenal = True
showmenu = True
is_in_menu = ["1","2","3","4","5","6","7","8","0","m","d","x"]
PlainText = ""
CipherText = ""
ASet = True

while(sentenal):
    if showmenu:
        printmenu()
    key = input("Make a selection: ")
    if not key.lower() in is_in_menu:
        print("Not a valid entry, please try again")
        showmenu = False
        print()
    else:
        if key == "0":
          #quit the program
            sentenal = False
        if key == "1":
            while True:
                #collect the matrix from the user:
                TempA = enter_matrix()
                #instatinate the matrix
                A = matrix(len(TempA),len(TempA[0]))
                A.setMatrix(TempA)
                A_inverse = matrix(len(TempA),len(TempA[0]))
                A_inverse.setMatrix(A.matrix_invert())
                Adeterm = A.getDet()
                relprime = xgcd(36,Adeterm)
                if A.getDet() == 0:
                    print("Entered matrix has no inverse, Please enter a different matrix")
                    print("")
                    showmenu = False
                elif relprime["gcd"] !=1:
                    print("***Warning***")
                    print("Matrix determinant " + str(Adeterm) + " is not relativity prime to 36. Please pick a different matrix")
                    print("This matrix determinant is: " + str(Adeterm))
                    print("and the gcd with 36 is: " + str(relprime['gcd']))
                    print("Try again")
                    print("")
                    showmenu = False
                else:
                    print("")
                    print("Matrix key A entered")
                    showmenu = True
                    break          
            
        if key == "2":
            PlainText = input("Enter Plain Text: ")
            if invalidchars_exist(PlainText):
                print("Error:")
                print("Contains invalid charactors")
                print("Please enter only values a-z and 0-9")
                print("Try again")
                print("")
                PlainText = ""
                showmenu = False
            print(base36(PlainText))
            print(frombase36(base36(PlainText)))
                
        if key == "3":
            CipherText = input("Enter Cipher Text: ")
            if invalidchars_exist(CipherText):
                print("Error:")
                print("Contains invalid charactors")
                print("Please enter only value a-z and 0-9")
                print("Try again")
                print("")
                CipherText = ""
                showmenu = False
                
        if key == "4":
            try:
                A
            except NameError:
                print("Key not set")
            try:
                PlainText
            except NameError:
                print("Plain Text is not yet set")
            if PlainText != "" and A:
                CipherTextMatrix = encrypt_function(PlainText, A, Toggle_Block_Display)
                CipherTextMatrix.humanreadable()
                
            else:
                print("***Please enter these values before trying to encrypt plain text***")
                showmenu = False
                
                
        if key == "5":
            try:
                A
            except NameError:
                print("Key not set")
            try:
                CipherText
            except NameError:
                print("Cipher Text is not yet set")
            if CipherText != "" and A:
                PlainTextMatrix = decrypt_function(CipherText, A, Toggle_Block_Display)
                PlainTextMatrix.humanreadable()
                print("-------------")
                print("Decrypted:")
                print(PlainTextMatrix.convertfrom36())
                print("--------------")
                print("")
            else:
                print("***Please enter these values before trying to decrypt cipher text***")
                print("")
                showmenu = False

        if key == "6":
            try:
                A.humanreadable()
            except NameError:
                print("***Matrix must be set before it can be displayed***")
                print("")
                showmenu = False
                
        if key == "7":
            try:
                A.humanreadableinverse()
            except NameError:
                print("***Matrix must be set before it can be displayed***")
                print("")
                showmenu = False
        if key == "8":
            if Toggle_Block_Display == True:
                Toggle_Block_Display = False
            else:
                Toggle_Block_Display = True
            
        if key == "m":
            printmenu()
        if key == "d":
            if type(A) is matrix:
                print("Det of A: " + str(A.getDet()))
