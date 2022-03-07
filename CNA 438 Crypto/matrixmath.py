##Dustin Watson
##Matrix Library for CNA438
##
##With some sections fomr Intruction to Programming Using Python by Y Daniel Liang
##
##Jan 16 2018
##Notice: Not all operations have been implemented.

import math
import re
import random


class matrix:
    def __init__(self, w,h):
        ##constructor for matrixmaker class
        self.matrix = [[0 for x in range(w)] for y in range(h)]
        self.w = w
        self.h = h
        self.cols = w
        self.rows = h

    def setindex(self, m,n, value):
        try:
            self.matrix[m][n] = value
        except:
            print("Error: Attempt to set a value outside the arrays of the matrix dementions")

    def getindex(self, m, n):
        return self.matrix[m][n]


    def setidentity(self):
        #TO-DO: This isn't work yet
        try:
            for i in range(0,self.w):
                for j in range(0,j):
                    self.matrix[i][j] = 0
            for i in range(0,self.w):
                setindex(i,i,1)

        except NameError:
            print("SetIdenty: Matrix doesn't yet exist")
            print("create a maxtrix first")
        else:
            print("Unknown error while trying to set an Identiy Matrix")
            print("Possiblity larger matrix requested than what this class  has been constructed")

    def setnull(self):
        try:
            for i in range(0,self.w):
                for j in range(0,j):
                    self.matrix[i][j] = 0

        except NameError:
            print("Matrix doesn't yet exist")
            print("create a maxtrix first")
        else:
            print("Unknown error while trying to set an Identiy Matrix")
            print("Possiblity larger matrix requested than what this class  has been constructed")

    def transpose(self):
        newmatrix = [[0 for x in range(self.h)] for y in range(self.w)]
        try:
            for i in range(0,self.h):
                for j in range(0,self.w):
                    newmatrix[w][h] = self.matrix[h][w]

        except NameError:
            print("Matrix doesn't yet exist")
            print("create a maxtrix first")
        else:
            print("Unknown error while trying to set an Identiy Matrix")
            print("Possiblity larger matrix requested than what this class  has been constructed")
        return newmatrix

    def getcols(self):
        return self.w

    def getrows(self):
        return self.h

    def show(self):
        return self.matrix

    def SummingAllElements(self):
        ##From Intro to Programming using Python page 364
        ##Modified for this library
        total = 0
        for row in self.matrix:
            for value in row:
                    total += value
        return total

    def SummingElementsByColumn(self):
        ##From Intro to Programming using Python page 364
        ##Modified for this library
        returnlist = []
        for column in range(len(self.matrix[0])):
            total = 0
            for row in range(len(self.matrix)):
                    total += self.matrix[row][column]
            returnlist.append(total)
        return returnlist

    def FindRowWithLargestSum(self):
        ##From Intro to Programming using Python page 364
        ##Modified for this library
        
        maxRow = sum(self.matrix[0]) # get the sum of the first row for MaxRow
        indexOfMaxRow = 0

        for row in range(1, len(self.matrix)):
            if sum(self.matrix[row]) > maxRow:
                maxRow = sum(self.matrix[row])
                indexOfMaxRow = row
        return [indexOfMaxRow, maxRow]

    def Shuffe(self):
        ##From Intro to Programming using Python page 364-365
        ##Modified for this library
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                i = random.randint(0,len(self.matrix)-1)
                j = random.randint(0, len(self.matrix)-1)
                self.matrix[row][column], self.matrix[i][j] =\
                                          self.matrix[i][j], self.matrix[row][colum]
                return self.matrix

    def Sort(self):
        ##From Intro to Programming using Python page 365
        ##Modified for this library
        ##not the most efficant sort in the world. Uses basic python sort
        return self.matrix.sort()
        
    def NNS(self):
        ##Adapted from Intro to Programming using Python page 369
        ##Modified for this library
        pass
        
    def sum_matrices(matrix1, matrix2, matrix3):
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
        return newmatrix

    def multiply_matrices(matrix1, matrix2, precision):
        ##Mutiply two matrices and return the a matrix object
        ##None otherwise if an error happens

        if not type(matrix1) is matrix or not type(matrix2) is matrix: return None ##may not work with inhartnace or multi add or sums

        if ((matrix1.getcols() != matrix2.getrows())):
            print("matrices not the correct size for multipication")
            return None
        else:
            results = matrix(matrix1.getrows(), matrix2.getcols())
            for i in range(matrix1.getrows()):
                for j in range(matrix2.getcols()):
                    for k in range(matrix1.getcols()):
                        results[i][j] = round(matrix1[i][k] * matrix2[k][j], precition)
        return results

    def isMarkovmatrix(self):
        #Returns True or False
        for i in range(0,len(self.matrix)):
            sum=0
            #Ensure that all verusables aer positive else it is anot a martof matrix
            for row in self.matrix:
                if row[i]>0:
                    sum+=row[i]
                else:
                    return False
                if sum==1:
                    continue
                else:
                    return False
            return True
                
            
               


