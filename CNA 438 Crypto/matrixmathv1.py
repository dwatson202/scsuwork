##Dustin Watson
##Matrix Library for CNA438
##Hand Complied Matrix Manuplication Library
##Feb 27 2018
##Notice: Not all operations have been implemented.
##Not for use in by any other student in CNA 438
##
##No warranties or guarantees are made by the authutor. Use at your own risk.
##Works Citied are inline with code

import math
import re
from random import *
import fractions


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

    def setRand(self,lower,upper):
        for m in range(0,self.h):
            for n in range(0,self.w):
                self.matrix[m][n] = randint(lower,upper)

    def setMatrix(self,d):
        self.matrix = d
        #self.rowechelon = self.REF(d)

    def shufflematrix(self, update=False):
        ##function is currently broken - needs fixing
        #if update:
        #   self.matrix = shuffle(self.matrix)
        print([shuffle(rows) for rows in self.matrix])

    def setindex(self, m,n, value):
        try:
            self.matrix[m][n] = value
        except:
            print("Error: Attempt to set a value outside the arrays of the matrix dementions")
    def setRand(self, low, high):
        for i in range(0, self.w):
            for j in range(0,self.h):
                self.matrix[i][j] = randint(low, high)

    def getindex(self, m, n):
        return self.matrix[m][n]

    def humanreadable(self):
        returnstring = ""
        for rows in self.matrix:
            returnstring = returnstring + str(rows)

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
        self.matrix[m] = value
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

    def SummingAllElements(self):
        ##From Intro to Programming using Python 7e page 364
        ##DANIEL LIANG 
        ##Modified for this library
        total = 0
        for row in self.matrix:
            for value in row:
                    total += value
        return total

    def SummingElementsByColumn(self):
        ##From Intro to Programming using Python 7e page 364
        ##DANIEL LIANG 
        ##Modified for this library
        returnlist = []
        for column in range(len(self.matrix[0])):
            total = 0
            for row in range(len(self.matrix)):
                    total += self.matrix[row][column]
            returnlist.append(total)
        return returnlist
    
    def FindRowWithLargestSum(self):
        ##From Intro to Programming using Python 7e page 364
        ##DANIEL LIANG 
        ##Modified for this library
        
        maxRow = sum(self.matrix[0]) # get the sum of the first row for MaxRow
        indexOfMaxRow = 0

        for row in range(1, len(self.matrix)):
            if sum(self.matrix[row]) > maxRow:
                maxRow = sum(self.matrix[row])
                indexOfMaxRow = row
        return [indexOfMaxRow, maxRow]

    def Shuffe(self, update=False):
        ##From Intro to Programming using Python 7e page 364
        ##DANIEL LIANG 
        ##Modified for this library
        
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                i = random.randint(0,len(self.matrix)-1)
                j = random.randint(0, len(self.matrix)-1)
                self.matrix[row][column], self.matrix[i][j] =\
                                          self.matrix[i][j], self.matrix[row][colum]
                return self.matrix

    def Sort(self, update=False):
        ##Sort the matrix.
        ##update updates the result into the class
        if update:
            self.matrix = self.matrix.sort()
        return self.matrix

    def getRowEchelon(self):
        print(self.rowechelon)
        return self.rowechelon


    def REF(self, update=None):
##        Modifed from https://rosettacode.org/wiki/Reduced_row_echelon_form#Python
##         Modified into Row Echelon form
##        Downloaded date: 3/1/2018
        M = self.matrix
        print(M)
        lead = 0
        rowCount = len(M)
        columnCount = len(M[0])
        alpha = 1 #count up the changes to make computing the determant easy
        for r in range(rowCount):
            if lead >= columnCount:
                #not square return None
                return 
            i = r
            while M[i][lead] == 0:
                i += 1
                if i == rowCount:
                    i = r
                    lead += 1
                    if columnCount == lead:
                        return
            M[i],M[r] = M[r],M[i]
            alpha = alpha * - 1.0 #switching rows changes the alpha by mutipe of -1
            lv = M[r][lead]
            M[r] = [ mrx / float(lv) for mrx in M[r]]
            alpha = alpha * (float(lv)) # alpha changes according to row scalars.
            for i in range(i, rowCount):
                if i != r:
                    lv = M[i][lead]
                    alpha = alpha * -1 #(adding row to another row as a negitive value)
                    M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
            lead += 1
        if alpha < self.threshold:
            self.determinant = 0
        else:
            self.determinant = alpha
            self.invertaible = True
        return M
##    end of code cite

    def getDet(self):
        return self.determinant
    
    def getInvertable(self):
        return self.invertaible
    
    def upperTriangular(self, update=False):
##        Modifed from https://rosettacode.org/wiki/Reduced_row_echelon_form#Python
##         Modified from RREF into upper_tranglar form
##        Downloaded date: 3/1/2018
        #print(self.matrix)
        M = self.matrix
        print(M)
        lead = 0
        rowCount = len(M)
        columnCount = len(M[0])
        alpha = 1 #count up the changes to make computing the determant easy
        for r in range(rowCount):
            if lead >= columnCount:
                #not square return None
                return None
            i = r
            #finds the first first none zero from left to right:
            while M[i][lead] == 0:
                i += 1
                if i == rowCount:
                    i = r
                    lead += 1
                    if columnCount == lead:
                        #not square return None
                        return
            #end finding the pivot
            M[i],M[r] = M[r],M[i]
            alpha = alpha * - 1 #switching rows changes the alpha by mutipe of -1
            lv = M[r][lead]
            #M[r] = [ mrx / float(lv) for mrx in M[r]] 
            alpha = alpha * (float(lv)) # alpha changes according to row scalars.
            #for i in range(0, rowCount):
                #if i != r and M[r][i] != 0:
                    #print("ELE OP", r, i)
                    #lv = M[i][lead]
                    #alpha = alpha * -1 #(adding row to another row as a negitive value)
                    #M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
            lead += 1
        if update != False:
            self.matrix = M
        if alpha < self.threshold:
            self.determinant = 0
            self.invertaible = False
        else:
            self.determinant = alpha
        return M
##    end of code cite

    def RREF(self, update=False):
##        Modifed from https://rosettacode.org/wiki/Reduced_row_echelon_form#Python
##        Downloaded date: 3/1/2018
##         Bugfixes and conversion into python 3
        M = self.matrix
        lead = 0
        rowCount = len(M)
        columnCount = len(M[0])
        for r in range(rowCount):
            if lead >= columnCount:
                return
            i = r
            while M[i][lead] == 0:
                i += 1
                if i == rowCount:
                    i = r
                    lead += 1
                    if columnCount == lead:
                        return
            M[i],M[r] = M[r],M[i]
            lv = M[r][lead]
            M[r] = [ mrx / float(lv) for mrx in M[r]]
            for i in range(rowCount):
                if i != r:
                    lv = M[i][lead]
                    M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
            lead += 1
        if update:
            self.matrix = M
        return M
##    end of code cite
            

    def _matrixMul(self, B):
##        #Work Citied and moidifed from:
##        #https://rosettacode.org/wiki/LU_decomposition#Python
##        #Downloaded 2/28/2018
##      internal funiction for the class if needed
        A = self.matrix
        TB = zip(*B)
        return [[sum(ea*eb for ea,eb in zip(a,b)) for b in TB] for a in A]

    def pivotize(self):
        #Moidifed from:
        #https://rosettacode.org/wiki/LU_decomposition#Python
        #Downloaded 2/28/2018
##        """Creates the pivoting matrix for the same size as the class matrix""
        #if self.h != self.w: return None
        n = self.h
        m = self.matrix
        ID = [[float(i == j) for i in range(0, n)] for j in range(n)]
        for j in range(n):
            row = max(range(j, n), key=lambda i: abs(m[i][j]))
            if j != row:
                ID[j], ID[row] = ID[row], ID[j]
        return ID

        
##        #Work Citied and moidifed from:
##        #https://rosettacode.org/wiki/LU_decomposition#Python
##        #Downloaded 2/28/2018

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
            return []
        #check if it has an inverse
        if self.invertaible:
            newmatrix = self.RREF(self._Augment_Identy())
            newmatrix = self._DeAugment(newmatrix,self.h, self.w, len(newmatrix), len(newmatrix[0]))
            return newmatrix
        else:
            return []

    def _catMatrix(matrix1, update=False):
        newmatrix = [x+y for x,y in zip(self.matrix, matrix1)]
        if update:
            self.matrix = newmatrix
        return newmatrix
    
                
                
        

        


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

    if not type(matrix1) is matrix or not type(matrix2) is matrix: return None ##may not work with inhartnace or multi add or sums

    if ((matrix1.getcols() != matrix2.getrows())):
        print("matrices not the correct size for multipication")
        return None
    else:
        newmatrix = matrix(matrix1.getrows(), matrix2.getcols())
        newmatrix.setnull()
        newvalue = 0
        for i in range(0, matrix1.getrows()):
            for j in range(matrix2.getcols()):
                for t in range(matrix2.getrows()):
                    print((newmatrix.getindex(i,j)+(matrix1.getindex(i,t) * matrix2.getindex(t,j))))
                    newmatrix.setindex(i,j, (newmatrix.getindex(i,j)+(matrix1.getindex(i,t) * matrix2.getindex(t,j))))
        if type(update_matrix) is matrix:
            update_matrix.setMatrix(newmatrix)
        return newmatrix

                    
                
                


MyMatrix = matrix(3,3)
d = [[4, -1, 1], [4, 5, 3], [-2, 0, 0]]
a = [[4,3],[5,-2]]
b = [[3,5,4],[2,3,1],[2,5,11]]
c = [[1,0,1,0],[0,1,0,-1],[1,0,-1,0],[0,1,0,1]]

MyMatrix.setMatrix(b)

print(MyMatrix.getInvertable())
print(MyMatrix.getDet())


uppertri = MyMatrix.REF()
for row in uppertri:
    print(row)
print(MyMatrix.getDet())
