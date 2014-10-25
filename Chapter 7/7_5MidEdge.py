import sys
import numpy as np
from Bio.SubsMat import MatrixInfo as matlist 
sys.setrecursionlimit(2000)
with open ('7_5.txt') as r:
    v = (r.readline()).translate(None, '\n')
    w = (r.readline()).translate(None, '\n')

#print v, w
#v = 'PLEASANTLY'
#w = 'MEASNLY'
similarityMatrixMap = matlist.blosum62
def MidEdge(seq1, seq2, gap):
    '''This function creates alignment score matrix
    seq1 : reference sequence
    seq2 : other sequence
    gap : gap penalty '''
 
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    fMatrix = np.zeros((rows,cols),int)
    backtrack = np.zeros((rows, cols),int)
    for i in range(0, rows):
        fMatrix[i][0] = i * gap
 
    for j in range(0, cols):
        fMatrix[0][j] = j * gap
 
    for i in range(1, rows):
        for j in range(1, cols):
            if (seq1[i - 1], seq2[j - 1]) in similarityMatrixMap:
               mtch = fMatrix[i - 1][j - 1] + similarityMatrixMap[(seq1[i - 1], seq2[j - 1])]
            elif (seq2[j - 1], seq1[i - 1]) in similarityMatrixMap:
                mtch = fMatrix[i - 1][j - 1] + similarityMatrixMap[(seq2[j - 1], seq1[i - 1])]
            delete = fMatrix[i - 1][j] + gap
            insert = fMatrix[i][j - 1] + gap
            fMatrix[i][j] = max(mtch, delete, insert)
            if fMatrix[i][j] == insert:
                backtrack[i][j] = 3
            elif fMatrix[i][j] == delete:
                backtrack[i][j] = 2
            elif fMatrix[i][j] ==mtch:
                backtrack[i][j] = 1
    #print backtrack, len(seq1)/2, len(seq2)/2
    return backtrack
    
def OUTPUTMidEdge(backtrack, v, w, i, j): 
        #print seq1, seq2, i, j, backtrack[i][j]
    if i == 0 and j ==0:
            return
    else:    
        if backtrack[i][j] == 1:
            OUTPUTMidEdge(backtrack, v, w, i-1, j-1)
            if j == len(w)/2 + 1:
                print (i-1, j-1), (i, j)  
               
        elif backtrack[i][j] == 2:
            OUTPUTMidEdge(backtrack, v, w, i-1, j)
            if j == len(w)/2 + 1:
                print (i-1, j-1), (i, j)
          
        elif backtrack[i][j] == 3:
            OUTPUTMidEdge(backtrack, v, w, i, j - 1)  
            if j == len(w)/2 + 1:
                print (i-1, j-1), (i, j)
            
            
 
OUTPUTMidEdge(MidEdge(v, w, -5), v, w, len(v), len(w))
