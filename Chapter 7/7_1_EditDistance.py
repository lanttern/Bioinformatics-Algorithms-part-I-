from sys import *
import numpy as np
from Bio.SubsMat import MatrixInfo as matlist 

with open ('7_1.txt') as r:
    v = (r.readline()).translate(None, '\n')
    w = (r.readline()).translate(None, '\n')
#v = 'PLEASANTLY'
#w = 'MEANLY'
#print v, w

def ED(seq1, seq2):
    rows = len(seq1)
    cols = len(seq2)
    Matrix = np.zeros((rows,cols),int)
    Matrix[0][0] = 0
    for i in range(1, rows):
        Matrix[i][0] = i
    for j in range(1, cols):
        Matrix[0][j] = j
    for i in range(1, rows):
        for j in range(1, cols):
            if seq1[i] == seq2[j]:
               Matrix[i][j] = min(Matrix[i-1][j-1], Matrix[i-1][j] + 1, Matrix[i][j-1] + 1)
            else:
               Matrix[i][j] = min(Matrix[i-1][j-1] + 1, Matrix[i-1][j] + 1, Matrix[i][j-1] + 1) 
    return Matrix[-1][-1]#, Matrix, rows, cols
'''
pseudocode    
    A two-dimensional matrix, m[0..|s1|,0..|s2|] is used to hold the edit distance values:

m[i,j] = d(s1[1..i], s2[1..j])

m[0,0] = 0
m[i,0] = i,  i=1..|s1|
m[0,j] = j,  j=1..|s2|

m[i,j] = min(m[i-1,j-1]
             + if s1[i]=s2[j] then 0 else 1 fi,
             m[i-1, j] + 1,
             m[i, j-1] + 1 ),  i=1..|s1|, j=1..|s2|
''' 

print ED(v, w)
